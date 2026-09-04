#!/usr/bin/env python3
"""Create a new content file from the templates in _templates/.

    python3 bin/new.py paper 2608.06107            -> _publications/<slug from title>.md, filled from arXiv
    python3 bin/new.py paper my-slug 2608.06107    -> same, with your own slug
    python3 bin/new.py paper my-slug               -> empty template to fill by hand
    python3 bin/new.py talk  my-slug               -> _talks/my-slug.md
    python3 bin/new.py post  my-slug               -> _posts/<today>-my-slug.md
    python3 bin/new.py news                        -> prints a snippet for _data/news.yml

The slug is the URL: /publication/<slug>, /talks/<slug>, /blog/<slug>/.
With an arXiv id, title, authors, date, abstract and the id are fetched from
the arXiv API; you only add `topics` (and optionally highlights). Placeholders
left in CAPITALS are reported by `python3 bin/check.py`.
"""
import datetime
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
KINDS = {
    "paper": ("_templates/publication.md", "_publications/{slug}.md"),
    "talk": ("_templates/talk.md", "_talks/{slug}.md"),
    "post": ("_templates/post.md", "_posts/{date}-{slug}.md"),
}
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STOP = {"a", "an", "the", "of", "in", "on", "for", "and", "to", "with", "via", "by", "is", "are"}


def slugify(title, words=4):
    tokens = [re.sub(r"[^a-z0-9]", "", w.lower()) for w in title.split()]
    tokens = [t for t in tokens if t and t not in STOP]
    return "-".join(tokens[:words]) or "paper"


def fetch_arxiv(arxiv_id):
    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    with urllib.request.urlopen(url, timeout=30) as r:
        root = ET.fromstring(r.read())
    ns = {"a": "http://www.w3.org/2005/Atom"}
    entry = root.find("a:entry", ns)
    if entry is None or entry.find("a:title", ns) is None:
        raise SystemExit(f"arXiv returned no entry for {arxiv_id}")
    clean = lambda s: re.sub(r"\s+", " ", (s or "").strip())
    title = clean(entry.findtext("a:title", default="", namespaces=ns))
    if title.lower().startswith("error"):
        raise SystemExit(f"arXiv returned an error for {arxiv_id}: {title}")
    abstract = clean(entry.findtext("a:summary", default="", namespaces=ns))
    authors = [clean(a.findtext("a:name", default="", namespaces=ns)) for a in entry.findall("a:author", ns)]
    published = clean(entry.findtext("a:published", default="", namespaces=ns))[:10]
    return {"title": title, "abstract": abstract, "authors": authors, "date": published}


def main(argv):
    if len(argv) < 2 or argv[1] not in (*KINDS, "news"):
        print(__doc__)
        return 2
    kind = argv[1]
    today = datetime.date.today().isoformat()
    if kind == "news":
        print(f'- date: {today}\n  text: "What happened, with a [link](/publication/SLUG) in Markdown."')
        print("\nPaste this into _data/news.yml (any position: the list is sorted by date at build time).")
        print("For a new paper or talk, `news: true` in its own file does the same without this step.")
        return 0
    args = argv[2:]
    arxiv_id = next((a for a in args if ARXIV_RE.match(a)), None)
    slug = next((a for a in args if SLUG_RE.match(a) and not ARXIV_RE.match(a)), None)
    meta = None
    if kind == "paper" and arxiv_id:
        print(f"fetching arXiv:{arxiv_id} …")
        meta = fetch_arxiv(arxiv_id)
        slug = slug or slugify(meta["title"])
    if not slug:
        print(__doc__)
        return 2
    template, target = KINDS[kind]
    out = ROOT / target.format(slug=slug, date=(meta or {}).get("date") or today)
    if out.exists():
        print(f"{out.relative_to(ROOT)} already exists")
        return 1
    text = (ROOT / template).read_text(encoding="utf-8")
    text = text.replace("SLUG", slug)
    if meta:
        text = text.replace('title: "Paper title exactly as published"', f'title: "{meta["title"].replace(chr(34), chr(39))}"')
        text = text.replace("YYYY-MM-DD", meta["date"] or today)
        text = text.replace("XXXX.XXXXX", arxiv_id)
        text = text.replace("'First Author, Yu-Han Wu, Third Author'", "'" + ", ".join(meta["authors"]) + "'")
        text = text.replace("Paste the abstract here.", meta["abstract"])
        text = re.sub(r"^summary: .*\n", "", text, flags=re.M)  # derived from the abstract unless you add one
    else:
        text = text.replace("YYYY-MM-DD", today)
    out.write_text(text, encoding="utf-8")
    print(f"created {out.relative_to(ROOT)}")
    if meta:
        print("filled: title, date, authors, arXiv id, abstract. Still yours: topics (and highlights if you like).")
    print("next: python3 bin/check.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
