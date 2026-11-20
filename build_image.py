#!/usr/bin/env python3
"""Render the Friday 20 November 2026 front page to a 1024x1024 PNG.

Fixed text, fixed geometry, fixed fonts: every run writes identical
bytes. This script only runs on my own machine to draw the picture;
the entry (main.py) just places the finished picture where it belongs.
"""

from PIL import Image, ImageDraw, ImageFont as F

PAGE = 1024
BLACK = (20, 20, 20)
CREAM = (250, 244, 224)
DEEP = (18, 42, 84)
SCARLET = (178, 34, 34)
AMBER = (198, 158, 24)
ASH = (96, 96, 96)
WHITE = (255, 255, 255)
MARGIN = 26

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
HEAVY = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
LIGHT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

ITEMS = (
    ("KYIV HIT BY BALLISTIC MISSILES",
     "Russia strikes Kyiv overnight, damaging three bridges over the "
     "Dnipro, while a drone hits a hospital in Kharkiv and injures four."),
    ("HOUTHIS STRIKE SAUDI TARGETS",
     "Houthi forces claim drone and missile strikes on four targets in "
     "Saudi Arabia; a tanker catches fire after hitting a mine east of "
     "the Strait of Hormuz."),
    ("COP31 CLOSES IN ANTALYA",
     "UN climate talks end with a 144-paragraph draft, $120 billion on "
     "the table, and fossil fuels left as two unresolved options."),
    ("DRONES HALT GENOA AIRPORT",
     "Genoa suspends flights after unidentified drones are spotted over "
     "the airport, the latest mystery-drone scare in Europe."),
    ("CALIFORNIA PROBES NVIDIA",
     "California targets Nvidia in a probe over AI chips bound for "
     "China, as regulators circle the chipmaker's exports."),
    ("FIONA THE HIPPO DIES",
     "Cincinnati Zoo's beloved hippo Fiona dies after swallowing a hat; "
     "the premature baby who became a social media star is gone."),
)


def font(path, size):
    return F.truetype(path, size)


def fit_lines(d, text, fnt, width):
    """Split text into lines no wider than width, word by word."""
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if d.textlength(candidate, font=fnt) <= width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def put_lines(d, x, y, lines, fnt, color, step):
    for line in lines:
        d.text((x, y), line, font=fnt, fill=color)
        y += step
    return y


def num_disc(d, x, y, n):
    """A scarlet disc holding a white story number."""
    d.ellipse([x, y, x + 32, y + 32], fill=SCARLET)
    label = str(n)
    tw = d.textlength(label, font=font(HEAVY, 20))
    d.text((x + (32 - tw) / 2, y + 4), label, font=font(HEAVY, 20), fill=WHITE)


def hline(d, y, color=BLACK, width=3):
    d.line([(MARGIN, y), (PAGE - MARGIN, y)], fill=color, width=width)


def draw():
    sheet = Image.new("RGB", (PAGE, PAGE), CREAM)
    d = ImageDraw.Draw(sheet)

    # Navy date bar with an amber rule underneath it.
    d.rectangle([0, 0, PAGE, 46], fill=DEEP)
    d.text((MARGIN, 11), "FRIDAY 20 NOVEMBER 2026",
           font=font(HEAVY, 22), fill=WHITE)
    tag = "THE WORLD IN ONE IMAGE"
    tw = d.textlength(tag, font=font(HEAVY, 22))
    d.text((PAGE - MARGIN - tw, 11), tag, font=font(HEAVY, 22), fill=AMBER)
    d.line([(0, 46), (PAGE, 46)], fill=AMBER, width=3)

    # Masthead and index strip.
    y = 66
    d.text((MARGIN, y), "FRIDAY 20 NOVEMBER 2026",
           font=font(SERIF, 56), fill=BLACK)
    y += 74
    d.text((MARGIN, y), "Six stories that sum up the day — Kyiv to Cincinnati",
           font=font(LIGHT, 24), fill=SCARLET)
    y += 38
    hline(d, y, width=4)
    y += 14
    d.text((MARGIN, y), "KYIV  ·  HORMUZ  ·  ANTALYA  ·  GENOA  ·  CALIFORNIA  ·  CINCINNATI",
           font=font(HEAVY, 17), fill=ASH)
    y += 30

    # Lead story: full width, scarlet rule across the top.
    head, body = ITEMS[0]
    lead = fit_lines(d, body, font(LIGHT, 23), PAGE - 2 * MARGIN - 40)
    box_h = 16 + 36 + len(lead) * 29 + 20
    d.rectangle([MARGIN, y, PAGE - MARGIN, y + box_h], outline=BLACK, width=2)
    d.rectangle([MARGIN, y, PAGE - MARGIN, y + 6], fill=SCARLET)
    num_disc(d, MARGIN + 16, y + 20, 1)
    d.text((MARGIN + 60, y + 18), head, font=font(HEAVY, 30), fill=SCARLET)
    put_lines(d, MARGIN + 16, y + 64, lead, font(LIGHT, 23), BLACK, 29)
    y += box_h + 18

    # Four stories in a two-by-two grid.
    cw = (PAGE - 2 * MARGIN - 16) // 2
    ch = 170
    for pos, (head, body) in enumerate(ITEMS[1:5]):
        gx = MARGIN + (pos % 2) * (cw + 16)
        gy = y + (pos // 2) * (ch + 16)
        d.rectangle([gx, gy, gx + cw, gy + ch], outline=BLACK, width=2)
        num_disc(d, gx + 12, gy + 12, pos + 2)
        heads = fit_lines(d, head, font(HEAVY, 20), cw - 64)[:2]
        ny = put_lines(d, gx + 54, gy + 12, heads, font(HEAVY, 20), BLACK, 24)
        paras = fit_lines(d, body, font(LIGHT, 19), cw - 26)[:4]
        put_lines(d, gx + 13, ny + 10, paras, font(LIGHT, 19), BLACK, 24)
    y += 2 * ch + 16 + 18

    # Last story on a deep-navy band.
    head, body = ITEMS[5]
    d.rectangle([MARGIN, y, PAGE - MARGIN, y + 104], fill=DEEP)
    num_disc(d, MARGIN + 14, y + 14, 6)
    d.text((MARGIN + 58, y + 14), head, font=font(HEAVY, 24), fill=AMBER)
    tail = fit_lines(d, body, font(LIGHT, 20), PAGE - 2 * MARGIN - 30)
    put_lines(d, MARGIN + 15, y + 50, tail, font(LIGHT, 20), WHITE, 26)

    # Amber footer rule, then the source line.
    d.line([(MARGIN, PAGE - 48), (PAGE - MARGIN, PAGE - 48)], fill=AMBER, width=2)
    d.text((MARGIN, PAGE - 34), "Sources: BBC, Reuters, AP, Le Monde, AFP  —  20 Nov 2026",
           font=font(LIGHT, 18), fill=ASH)

    sheet.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    draw()
