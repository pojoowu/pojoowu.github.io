#!/usr/bin/env python3
"""Render a talk's slides (or poster) to page images under
images/decks/<pdf name>/, which the talk page shows in its own viewer instead
of an embedded PDF reader.

    python3 bin/talk-deck.py            # every deck that has no images yet
    python3 bin/talk-deck.py <slug>     # just that talk's deck, re-rendered
    python3 bin/talk-deck.py --all      # re-render every deck from scratch

The PDF comes from the talk's `slidesurl`, else `posterurl`, else the file
conventions files/<slug>-slides.pdf and files/<slug>-poster.pdf. Pages are
written as 01.png, 02.png, ... at twice the size they are displayed at, so
they stay sharp when a page is opened large; a poster is simply a deck of one
page, so the talk page needs no special case. The folder is named after the
PDF, so two talks that present the same deck share one set of images.
Needs `pdftoppm` (brew install poppler) and Pillow (pip install pillow).
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML is required: pip install pyyaml")
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_ROOT = ROOT / "images" / "decks"
WIDTH = 2000  # ~2x the widest the viewer shows a page, so zooming stays sharp
MAX_PAGES = 60


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def deck_for(slug, data):
    """Site path of the PDF to render for this talk, or None."""
    for field, suffix in (("slidesurl", "-slides.pdf"), ("posterurl", "-poster.pdf")):
        value = data.get(field)
        if value and str(value).startswith("/") and (ROOT / str(value).lstrip("/")).exists():
            return str(value)
        guess = f"/files/{slug}{suffix}"
        if (ROOT / guess.lstrip("/")).exists():
            return guess
    return None


def deck_name(pdf_site_path):
    """Folder name for a PDF: its file name without the extension, so talks
    that present the same deck share one set of images."""
    return pathlib.Path(pdf_site_path).stem


def render(pdf_site_path):
    pdf = ROOT / pdf_site_path.lstrip("/")
    name = deck_name(pdf_site_path)
    out_dir = OUT_ROOT / name
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["pdftoppm", "-png", "-scale-to-x", str(WIDTH), "-scale-to-y", "-1",
             "-f", "1", "-l", str(MAX_PAGES), str(pdf), f"{tmp}/p"],
            check=True,
        )
        pages = sorted(pathlib.Path(tmp).glob("p*.png"))
        if not pages:
            raise SystemExit(f"pdftoppm produced nothing for {pdf_site_path}")
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)
        total = 0
        for i, page in enumerate(pages, start=1):
            img = Image.open(page).convert("RGB")
            # flat slide art quantizes well and halves the file size
            img.quantize(colors=192, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG).save(
                out_dir / f"{i:02d}.png", optimize=True
            )
            total += (out_dir / f"{i:02d}.png").stat().st_size
    print(f"{name}: {len(pages)} page(s) at {WIDTH}px  ->  images/decks/{name}/  ({total / 1024 / 1024:.1f} MB)")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    every = "--all" in argv
    slug = args[0] if args else None
    talks = sorted((ROOT / "_talks").glob("*.md"))
    if slug:
        talks = [t for t in talks if t.stem == slug]
        if not talks:
            print(f"no _talks/{slug}.md")
            return 1
    made, seen = 0, set()
    for path in talks:
        deck = deck_for(path.stem, front_matter(path))
        if not deck:
            if slug:
                print(f"{path.stem}: no slides or poster to render")
            continue
        name = deck_name(deck)
        if name in seen:
            continue  # another talk presents the same deck
        seen.add(name)
        if not slug and not every and (OUT_ROOT / name).exists():
            continue  # keep what is there unless asked by name or with --all
        render(deck)
        made += 1
    if not made and not slug:
        print("every deck already has page images (use --all to re-render)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
