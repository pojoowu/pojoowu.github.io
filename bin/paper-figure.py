#!/usr/bin/env python3
"""Cut a key figure out of a paper PDF into images/papers/<slug>.png.

    python3 bin/paper-figure.py files/paper.pdf 3 my-slug
    python3 bin/paper-figure.py files/paper.pdf 3 my-slug --box 0.1,0.08,0.9,0.42

PAGE is 1-based. --box gives the crop as fractions of the page (left, top,
right, bottom); without it the whole page is used. White margins are trimmed
automatically afterwards, so a generous box is fine. Needs `pdftoppm`
(brew install poppler) and Pillow (pip install pillow).
"""
import pathlib
import subprocess
import sys
import tempfile

from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).resolve().parent.parent


def trim(img, pad=12):
    bg = Image.new(img.mode, img.size, (255, 255, 255))
    bbox = ImageChops.difference(img, bg).getbbox()
    if not bbox:
        return img
    l, t, r, b = bbox
    return img.crop((max(0, l - pad), max(0, t - pad), min(img.width, r + pad), min(img.height, b + pad)))


def main(argv):
    if len(argv) < 4:
        print(__doc__)
        return 2
    pdf, page, slug = pathlib.Path(argv[1]), int(argv[2]), argv[3]
    box = None
    if "--box" in argv:
        box = [float(x) for x in argv[argv.index("--box") + 1].split(",")]
    with tempfile.TemporaryDirectory() as tmp:
        prefix = pathlib.Path(tmp) / "page"
        subprocess.run(["pdftoppm", "-r", "220", "-f", str(page), "-l", str(page), "-png", str(pdf), str(prefix)], check=True)
        out_png = next(pathlib.Path(tmp).glob("page*.png"))
        img = Image.open(out_png).convert("RGB")
    if box:
        w, h = img.size
        img = img.crop((int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h)))
    img = trim(img)
    if img.width > 1600:
        img = img.resize((1600, int(img.height * 1600 / img.width)), Image.LANCZOS)
    out = ROOT / "images" / "papers" / f"{slug}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, optimize=True)
    print(f"wrote {out.relative_to(ROOT)} {img.size}; add to the paper's front matter:\n  figure: /images/papers/{slug}.png")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
