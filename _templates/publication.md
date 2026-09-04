---
# Paper. Create with `python3 bin/new.py paper <arxiv-id>` (fills everything
# but `topics` from arXiv) or `python3 bin/new.py paper <slug>` by hand.
# The file name is the URL: _publications/<slug>.md -> /publication/<slug>.
# Derived when absent: arXiv/Paper pills from the id, the one-line summary from
# the abstract, citation text and BibTeX, a PDF at files/<slug>.pdf, a key
# figure at images/papers/<slug>.png, a linked blog post (`paper:` in the post),
# related work (shared topics), MathJax when $...$ appears.
title: "Paper title exactly as published"
date: YYYY-MM-DD                          # first public version; orders the lists
venue: 'arXiv preprint'                   # or 'ICML 2026', 'COLT 2025', ... (a venue without "arXiv" counts as published)
arxiv: XXXX.XXXXX                         # arXiv id
authors: 'First Author, Yu-Han Wu, Third Author'   # comma-separated; names in _data/people.yml become links; "*" marks equal contribution
topics: [diffusion, theory]               # ids from _data/topics.yml: filters, focus cards, related work
summary: 'One line, about 110 characters, shown under the title in lists.'
news: true                                # "New preprint: Title" in the news at `date`; a text in quotes for your own wording; delete to skip
# highlights:                             # the Details box and "In brief" section; 3 bullets work best
#   - "**Problem.** What was open or wrong."
#   - "**Approach.** What the paper does about it."
#   - "**Result.** What comes out, in one sentence."
# selected: true                          # show under "Selected publications" on the home page
# short: "Short name"                     # label used on the focus cards (default: title before the colon)
# figure_caption: "Caption in the paper's own words."   # for images/papers/<slug>.png (python3 bin/paper-figure.py files/paper.pdf PAGE <slug>)
# award: 'Spotlight'                      # emerald badge; `badges: ['Oral at ...']` for more
# related: [other-slug]                   # fix the Related work list by hand
# codeurl / slidesurl / posterurl / link / paperurl / figure / blogurl: explicit URLs when the conventions do not fit
# citation: '...'                         # override the generated "Authors (Year). Title. Venue." text
# bibtex: |                               # override the generated entry, e.g. with the official proceedings entry
#   @inproceedings{...}
---
### Abstract
Paste the abstract here.
