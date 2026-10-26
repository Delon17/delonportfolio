"""Tile a faint diagonal "delonpyle.com" across a certificate image.

    python -I scripts/watermark.py <source image> <output .webp>

Run it once on each freshly rendered certificate (never on an already
watermarked file, or the marks double up).
"""
import sys
from PIL import Image, ImageDraw, ImageFont

TEXT = "delonpyle.com"
FONT = "C:/Windows/Fonts/segoeuib.ttf"


def watermark(src, out):
    base = Image.open(src).convert("RGBA")
    w, h = base.size
    size = max(18, w // 28)
    font = ImageFont.truetype(FONT, size)

    # draw the pattern on an oversized square, rotate it, then crop to the image
    side = int((w ** 2 + h ** 2) ** 0.5) + size * 4
    tile = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    tw = d.textlength(TEXT, font=font)
    step_x, step_y = int(tw + size * 4), int(size * 5.5)
    for row, y in enumerate(range(0, side, step_y)):
        for x in range(-step_x + (row % 2) * step_x // 2, side, step_x):
            # a light and a dark pass keep it visible on both pale and dark certificates
            d.text((x + 1, y + 1), TEXT, font=font, fill=(255, 255, 255, 34))
            d.text((x, y), TEXT, font=font, fill=(40, 44, 52, 34))
    tile = tile.rotate(28, resample=Image.BICUBIC)
    left, top = (side - w) // 2, (side - h) // 2
    tile = tile.crop((left, top, left + w, top + h))

    Image.alpha_composite(base, tile).convert("RGB").save(out, "WEBP", quality=82, method=6)


if __name__ == "__main__":
    watermark(sys.argv[1], sys.argv[2])
