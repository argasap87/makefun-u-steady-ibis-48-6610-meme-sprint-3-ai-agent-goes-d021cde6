#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — "It Now Works for the Cat".

Deterministic, offline meme compositor. Reads the AI-generated scene
(asset: a cat riding a robot vacuum) from assets/scene.jpg, crops the
generator watermark strip off the bottom, and lays it out as a classic
top-text / bottom-text meme on a 1024x1024 canvas, writing
/output/entry.png.

The joke: the robot vacuum was bought to clean the house. It went rogue
in the most domestic way possible — it stopped cleaning and now serves
the cat instead. The cat rides it like a chauffeur-driven limousine.
One glance, no explanation needed.

No network access at runtime; every input ships in this repository.
"""

import os

from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
TOP_BAR = 168
BOTTOM_BAR = 168
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "scene.jpg")

TOP_LINES = ["MY ROBOT VACUUM", "WENT ROGUE"]
BOTTOM_LINES = ["NOW IT'S", "THE CAT'S UBER"]


def fit_font(draw, lines, max_width, start_size, max_height):
    """Largest bold font size fitting every line in max_width and the
    whole block (all lines + gaps) in max_height."""
    size = start_size
    while size > 20:
        font = ImageFont.truetype(FONT_PATH, size)
        block = len(lines) * size + (len(lines) - 1) * 8
        if block <= max_height and all(
            draw.textlength(line, font=font) <= max_width for line in lines
        ):
            return font
        size -= 2
    return ImageFont.truetype(FONT_PATH, 20)


def draw_centered_block(draw, lines, font, cx, top, line_gap):
    """Draw lines centred on cx, starting at y=top, white with black stroke."""
    y = top
    for line in lines:
        w = draw.textlength(line, font=font)
        draw.text(
            (cx - w / 2, y),
            line,
            font=font,
            fill=(255, 255, 255),
            stroke_width=max(3, font.size // 14),
            stroke_fill=(0, 0, 0),
        )
        y += font.size + line_gap
    return y


def main():
    scene = Image.open(ASSET).convert("RGB")

    # The generator stamps a small watermark along the bottom edge; crop
    # that strip off so the shipped image is clean.
    w, h = scene.size
    scene = scene.crop((0, 0, w, h - 60))

    # Build the 1024x1024 canvas: black caption bars top and bottom.
    canvas = Image.new("RGB", (SIZE, SIZE), (0, 0, 0))
    img_w, img_h = SIZE, SIZE - TOP_BAR - BOTTOM_BAR

    # Cover-fit the scene into the middle band, centre-cropped.
    scale = max(img_w / scene.width, img_h / scene.height)
    resized = scene.resize(
        (round(scene.width * scale), round(scene.height * scale)),
        Image.LANCZOS,
    )
    left = (resized.width - img_w) // 2
    top = (resized.height - img_h) // 2
    canvas.paste(resized.crop((left, top, left + img_w, top + img_h)), (0, TOP_BAR))

    draw = ImageDraw.Draw(canvas)

    # Top caption: two lines, centred in the top bar.
    font_top = fit_font(draw, TOP_LINES, SIZE - 48, 88, TOP_BAR - 16)
    block_h = len(TOP_LINES) * font_top.size + (len(TOP_LINES) - 1) * 8
    draw_centered_block(
        draw, TOP_LINES, font_top, SIZE // 2, TOP_BAR // 2 - block_h // 2, 8
    )

    # Bottom caption: two lines, centred in the bottom bar.
    font_bottom = fit_font(draw, BOTTOM_LINES, SIZE - 48, 88, BOTTOM_BAR - 16)
    block_h = len(BOTTOM_LINES) * font_bottom.size + (len(BOTTOM_LINES) - 1) * 8
    draw_centered_block(
        draw,
        BOTTOM_LINES,
        font_bottom,
        SIZE // 2,
        SIZE - BOTTOM_BAR + BOTTOM_BAR // 2 - block_h // 2,
        8,
    )

    # A thin white frame ties the meme together at thumbnail size.
    draw.rectangle([3, 3, SIZE - 4, SIZE - 4], outline=(255, 255, 255), width=6)

    os.makedirs("/output", exist_ok=True)
    canvas.save("/output/entry.png", format="PNG", optimize=True)
    print("wrote /output/entry.png", canvas.size)


if __name__ == "__main__":
    main()
