# Maintaining this site

Jekyll site (Academic Pages / Minimal Mistakes) deployed by GitHub Pages from `master`.
Content is a few Markdown files with front matter plus small data files; everything that can be
derived is derived, so adding something is two or three steps.

## Add a paper

```
python3 bin/new.py paper 2608.06107      # fetches title, authors, date, abstract from arXiv
```

Open the new file in `_publications/`, set `topics` (ids from `_data/topics.yml`), run `python3 bin/check.py`, commit.

The paper then appears in the publications list and filters, on its own page, on the CV and in the
PDF CV, on the matching focus cards, and in the news. Derived unless you say otherwise: the
arXiv and Paper pills, the one-line summary (first sentence of the abstract), citation text and
BibTeX, related work (shared topics), MathJax. Optional one-liners in the template: `highlights`
(three bullets), `selected: true` (home page), `award`, a `short` name for the cards. Drop a PDF at
`files/<slug>.pdf` or a figure at `images/papers/<slug>.png` and they are picked up
(`python3 bin/paper-figure.py files/<slug>.pdf PAGE <slug>` cuts the figure). For a published version,
change `venue` and, if you want the official entry, paste it under `bibtex:`.

## Add a talk or poster

```
python3 bin/new.py talk colt2026
```

Fill event, type, venue, location, date and the paper. Slides or a poster named
`files/colt2026-slides.pdf` / `files/colt2026-poster.pdf` are picked up automatically. `news: true` adds it to the news.

## Add a blog post

```
python3 bin/new.py post my-slug
```

Write Markdown; math works as `$x$` and `$$…$$`; figures go in `images/blog/my-slug/`.
`paper: <slug>` in the front matter links the post and the paper page to each other.

## Add a news item

`news: true` in a paper or talk file, or two lines in `_data/news.yml`:

```yaml
- date: 2026-09-04
  text: "Something happened, with a [link](/publication/my-slug)."
```

## Everything else

| To change… | Edit |
|---|---|
| Education, experience, service, skills (CV) | `_data/cv.yml` — publications, talks and distinctions are automatic |
| Research-focus cards on the home page | `_data/focus.yml` — papers, counts and links are automatic |
| Topic filters | `_data/topics.yml` |
| Co-author homepage links | `_data/people.yml` (names spelled as in the author lines) |
| Name, title lines, photos, e-mail, Scholar/GitHub | `_config.yml` → `title`, `tagline`, `author:` |
| Header links | `_data/navigation.yml` |
| About text | `_pages/about.md` |
| Colours and type | `_sass/theme/_custom.scss` (tokens), `_sass/layout/_skin.scss` (visual), `_sass/layout/_cv.scss` (CV and print) |

## Checks, preview, deployment

- `python3 bin/check.py` validates all content; GitHub Actions runs it and a full build on every pull request.
- Preview: `bundle exec jekyll serve`, then <http://localhost:4000>. A change to `_config.yml` needs a restart.
- Every push to `master` runs the Deploy workflow: it builds the site, renders `/cv/` to `files/yu-han-wu-cv.pdf`
  inside the build, and publishes the result (Settings → Pages → Source is "GitHub Actions"). The PDF is therefore
  never committed and never conflicts; it is ignored by git. To look at it locally, serve the site and run
  `BASE_URL=http://localhost:4000 node .github/scripts/cv-pdf.js` (needs `npm i puppeteer`).

## Things that bite

- Files whose names start with `_` are not published by Jekyll. Rename them.
- A paper's or talk's URL is its file name; renaming breaks links from news, talks and posts, and `bin/check.py` says where.
- Publications, Talks and CV use the `archive` layout: their content sits in `.archive`, not `.page__content`.
- Filter links are `#id+id`: the theme's smooth-scroll plugin passes fragments through a jQuery selector, so `=` or `,` would throw.
