#!/usr/bin/env python3
"""Validate the site's content before a commit.

    python3 bin/check.py        # exit 1 on errors, 0 otherwise (warnings only)

What is checked
  papers   title/date/venue/authors/summary present; a paper link (arxiv id,
           arxivurl or paperurl); arxiv id shape; topics are known ids; local
           files exist and do not start with "_" (Jekyll skips those); related
           slugs, blogurl and permalink (if given) resolve; citation/bibtex
           agree if both are given; leftover template placeholders
  talks    title/type/venue/location/date present; publication resolves; files
  posts    file-name date = front-matter date; leftover placeholders; images exist
  news     _data/news.yml items have date + text and their links resolve
  topics   unique ids, each used by some paper
  people   each entry appears in some author line (else it is stale)
  home     focus-card links point at existing papers / valid topic ids
  cv data  education/experience entries have what + when

Needs PyYAML (pip install pyyaml). Run from anywhere in the repository.
"""
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: pip install pyyaml")
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []
err = lambda where, msg: errors.append(f"{where}: {msg}")
warn = lambda where, msg: warnings.append(f"{where}: {msg}")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
PLACEHOLDER = re.compile(r"\b(SLUG|YYYY-MM-DD|XXXX\.XXXXX|PAPER-SLUG|First Author|Third Author|Paper title|Post title|Event name)\b")


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        err(rel(path), "no front matter block")
        return None, ""
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError as e:
        err(rel(path), f"front matter is not valid YAML: {e}")
        return None, m.group(2)


def rel(path):
    return str(path.relative_to(ROOT))


def local_file_ok(where, field, value):
    if not isinstance(value, str) or not value.startswith("/"):
        return
    p = ROOT / value.lstrip("/")
    if not p.exists():
        err(where, f"{field} points at {value}, which does not exist")
    elif p.name.startswith("_"):
        err(where, f"{field} file name starts with '_' ({p.name}); Jekyll does not publish such files, rename it")


def placeholders(where, data, body):
    blob = yaml.safe_dump(data, allow_unicode=True) + body
    found = sorted(set(m if isinstance(m, str) else m[0] for m in PLACEHOLDER.findall(blob)))
    if found:
        err(where, "template placeholders still present: " + ", ".join(found))


def date_ok(v):
    return DATE_RE.match(str(v)) is not None


def load_yaml(name):
    p = ROOT / name
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


topics = load_yaml("_data/topics.yml") or []
topic_ids = [t.get("id") for t in topics]
if len(topic_ids) != len(set(topic_ids)):
    err("_data/topics.yml", "duplicate topic ids")
for t in topics:
    if not t.get("label"):
        err("_data/topics.yml", f"topic {t.get('id')} has no label")

people = load_yaml("_data/people.yml") or []
people_names = [p.get("name") for p in people]

pub_files = sorted((ROOT / "_publications").glob("*.md"))
talk_files = sorted((ROOT / "_talks").glob("*.md"))
post_files = sorted((ROOT / "_posts").glob("*.md"))
pub_slugs = {p.stem for p in pub_files}
talk_slugs = {p.stem for p in talk_files}
post_slugs = {re.sub(r"^\d{4}-\d{2}-\d{2}-", "", p.stem) for p in post_files}
used_topics, author_text = set(), ""

# papers ---------------------------------------------------------------------
for path in pub_files:
    where = rel(path)
    data, body = front_matter(path)
    if data is None:
        continue
    placeholders(where, data, body)
    for f in ("title", "date", "authors"):
        if not data.get(f):
            err(where, f"missing `{f}`")
    if not data.get("summary") and not body.strip():
        warn(where, "no `summary` and no abstract: the row will have no one-line description")
    if data.get("date") and not date_ok(data["date"]):
        err(where, f"date should be YYYY-MM-DD, got {data['date']!r}")
    if data.get("permalink") and data["permalink"] != f"/publication/{path.stem}":
        err(where, f"permalink {data['permalink']} disagrees with the file name (drop it or use /publication/{path.stem})")
    if data.get("arxiv") is not None and not ARXIV_RE.match(str(data["arxiv"])):
        err(where, f"arxiv should be an id like 2608.06107, got {data['arxiv']!r}")
    if not (data.get("arxiv") or data.get("arxivurl") or data.get("paperurl")):
        warn(where, "no arxiv id, arxivurl or paperurl: the row will have no Paper pill")
    tps = data.get("topics") or []
    if not isinstance(tps, list):
        err(where, "`topics` must be a list, e.g. [diffusion, theory]")
        tps = []
    unknown = [t for t in tps if t not in topic_ids]
    if unknown:
        err(where, f"unknown topic id(s) {unknown}; ids are {topic_ids}")
    if not tps:
        warn(where, "no `topics`: the paper disappears as soon as any filter is active")
    used_topics.update(tps)
    for f in ("paperurl", "slidesurl", "posterurl", "figure"):
        if data.get(f):
            local_file_ok(where, f, data[f])
    for slug in data.get("related") or []:
        if slug not in pub_slugs:
            err(where, f"related slug '{slug}' has no file _publications/{slug}.md")
    if data.get("blogurl"):
        m = re.fullmatch(r"/blog/([^/]+)/?", str(data["blogurl"]))
        if not m or m.group(1) not in post_slugs:
            err(where, f"blogurl {data['blogurl']} matches no post in _posts/ (URLs are /blog/<slug>/)")
    if len(data.get("summary") or "") > 130:
        warn(where, "summary is over 130 characters; aim for one line")
    hl = data.get("highlights")
    if hl is not None and (not isinstance(hl, list) or not 2 <= len(hl) <= 4):
        warn(where, "`highlights` should be a list of 2–4 bullets")
    bib, cit = str(data.get("bibtex") or ""), str(data.get("citation") or "")
    if bib and cit:
        ym = re.search(r"year\s*=\s*\{?(\d{4})", bib)
        if ym and f"({ym.group(1)})" not in cit:
            err(where, f"citation year does not match the bibtex year {ym.group(1)}")
    if data.get("news") not in (None, True, False) and not isinstance(data.get("news"), str):
        err(where, "`news` must be true or a text")
    author_text += " " + str(data.get("authors") or "")
    for n in re.split(r",| and ", str(data.get("authors") or "")):
        n = n.strip(" *")
        if n and n != "Yu-Han Wu" and n not in people_names and "(" not in n and "Team" not in n and "DeepMind" not in n:
            warn(where, f"no homepage link for '{n}' (add to _data/people.yml, spelled exactly like this)")

for t in topic_ids:
    if t not in used_topics:
        warn("_data/topics.yml", f"topic '{t}' is used by no paper; its filter button will always be empty")
for n in people_names:
    if n not in author_text:
        warn("_data/people.yml", f"'{n}' appears in no author line (stale entry or spelling mismatch)")

# talks ----------------------------------------------------------------------
for path in talk_files:
    where = rel(path)
    data, body = front_matter(path)
    if data is None:
        continue
    placeholders(where, data, body)
    for f in ("title", "type", "venue", "location", "date"):
        if not data.get(f):
            err(where, f"missing `{f}`")
    if data.get("date") and not date_ok(data["date"]):
        err(where, f"date should be YYYY-MM-DD, got {data['date']!r}")
    if data.get("permalink") and data["permalink"] != f"/talks/{path.stem}":
        err(where, f"permalink {data['permalink']} disagrees with the file name")
    if data.get("type") and data["type"] not in ("Talk", "Invited talk", "Oral", "Poster", "Keynote", "Lecture"):
        warn(where, f"unusual type {data['type']!r}")
    for f in ("slidesurl", "posterurl"):
        if data.get(f):
            local_file_ok(where, f, data[f])
    pub = data.get("publication")
    if pub:
        m = re.fullmatch(r"/publication/([^/]+)/?", str(pub))
        if not m or m.group(1) not in pub_slugs:
            err(where, f"publication {pub} has no file in _publications/")
    elif not body.strip():
        warn(where, "no `publication` and no body text: the card will have no description")

# posts ----------------------------------------------------------------------
for path in post_files:
    where = rel(path)
    data, body = front_matter(path)
    if data is None:
        continue
    placeholders(where, data, body)
    m = re.match(r"^(\d{4}-\d{2}-\d{2})-", path.name)
    if not m:
        err(where, "file name must start with YYYY-MM-DD-")
    elif str(data.get("date")) != m.group(1):
        err(where, f"front-matter date {data.get('date')} differs from the file-name date {m.group(1)}")
    if not data.get("title"):
        err(where, "missing `title`")
    if not data.get("excerpt"):
        warn(where, "no `excerpt`: the blog list and link previews will use the first paragraph")
    if data.get("paper") and data["paper"] not in pub_slugs:
        err(where, f"paper '{data['paper']}' has no file _publications/{data['paper']}.md")
    for img in re.findall(r'src="(/images/[^"]+)"', body):
        local_file_ok(where, "image", img)

# focus cards ----------------------------------------------------------------
for i, card in enumerate(load_yaml("_data/focus.yml") or []):
    where = f"_data/focus.yml card {i + 1}"
    if not card.get("title") or not card.get("topics"):
        err(where, "needs `title` and `topics`")
    bad = [t for t in card.get("topics") or [] if t not in topic_ids]
    if bad:
        err(where, f"unknown topic id(s) {bad}")
    for slug in card.get("papers") or []:
        if slug not in pub_slugs:
            err(where, f"paper '{slug}' has no file in _publications/")

# news -----------------------------------------------------------------------
news = load_yaml("_data/news.yml") or []
for i, item in enumerate(news):
    where = f"_data/news.yml item {i + 1}"
    if not item.get("date") or not date_ok(item["date"]):
        err(where, "needs a `date` in YYYY-MM-DD form")
    if not item.get("text"):
        err(where, "needs `text`")
    for link in re.findall(r"\]\((/[^)]+)\)", str(item.get("text") or "")):
        m = re.fullmatch(r"/(publication|talks|blog)/([^/#]+)/?(#.*)?", link)
        if m and m.group(2) not in {"publication": pub_slugs, "talks": talk_slugs, "blog": post_slugs}[m.group(1)]:
            err(where, f"link {link} points at nothing")

# home page ------------------------------------------------------------------
about = (ROOT / "_pages/about.md").read_text(encoding="utf-8")
for slug in re.findall(r'href="/publication/([^"/]+)"', about):
    if slug not in pub_slugs:
        err("_pages/about.md", f"link to /publication/{slug} points at nothing")
for frag in re.findall(r'href="/publications/#([^"]+)"', about):
    bad = [t for t in frag.split("+") if t not in topic_ids]
    if bad:
        err("_pages/about.md", f"filter link #{frag} uses unknown topic id(s) {bad}")

# cv data --------------------------------------------------------------------
cv = load_yaml("_data/cv.yml") or {}
for section in ("education", "experience", "service"):
    for i, e in enumerate(cv.get(section) or []):
        if not e.get("what") or not e.get("when"):
            err(f"_data/cv.yml {section} entry {i + 1}", "needs `what` and `when`")

# the CV PDF is rendered at deploy time and must never be committed ---------
import subprocess
try:
    tracked = subprocess.run(["git", "ls-files", "files/yu-han-wu-cv.pdf"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if tracked:
        err("files/yu-han-wu-cv.pdf", "is tracked by git; it is rendered by the deploy workflow, run `git rm --cached files/yu-han-wu-cv.pdf`")
except OSError:
    pass

# report ---------------------------------------------------------------------
for w in warnings:
    print("warning:", w)
for e in errors:
    print("ERROR:", e)
print(f"\n{len(pub_files)} papers, {len(talk_files)} talks, {len(post_files)} posts, {len(news)} news items checked: "
      f"{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
