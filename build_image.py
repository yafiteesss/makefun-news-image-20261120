#!/usr/bin/env python3
"""Draw the Friday 20 November 2026 front page as a 1024x1024 PNG.

Everything is fixed: the same text, layout and fonts every run, so two
runs produce identical bytes. It only runs on my own machine to make the
picture; the entry itself (main.py) just copies the finished picture
into /output/entry.png.
"""

from PIL import Image, ImageDraw, ImageFont as F

W = H = 1024
INK = (20, 20, 20)
PAPER = (250, 244, 224)
NAVY = (18, 42, 84)
RED = (178, 34, 34)
GOLD = (198, 158, 24)
GREY = (96, 96, 96)
SNOW = (255, 255, 255)
EDGE = 26

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

STORIES = (
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


def face(path, size):
    return F.truetype(path, size)


def wrap(d, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, lines, font, color, step):
    for line in lines:
        d.text((x, y), line, font=font, fill=color)
        y += step
    return y


def number_chip(d, x, y, n):
    """A small red square with a white story number."""
    d.rectangle([x, y, x + 30, y + 30], fill=RED)
    label = str(n)
    tw = d.textlength(label, font=face(BOLD, 20))
    d.text((x + (30 - tw) / 2, y + 3), label, font=face(BOLD, 20), fill=SNOW)


def rule(d, y, color=INK, width=3):
    d.line([(EDGE, y), (W - EDGE, y)], fill=color, width=width)


def main():
    page = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(page)

    # Date bar: navy, with a gold rule underneath.
    d.rectangle([0, 0, W, 46], fill=NAVY)
    d.text((EDGE, 11), "FRIDAY 20 NOVEMBER 2026",
           font=face(BOLD, 22), fill=SNOW)
    tag = "THE WORLD IN ONE IMAGE"
    tw = d.textlength(tag, font=face(BOLD, 22))
    d.text((W - EDGE - tw, 11), tag, font=face(BOLD, 22), fill=GOLD)
    d.line([(0, 46), (W, 46)], fill=GOLD, width=3)

    # Masthead.
    y = 66
    d.text((EDGE, y), "FRIDAY, 20 NOVEMBER 2026",
           font=face(SERIF, 58), fill=INK)
    y += 76
    d.text((EDGE, y), "Six stories that sum up the day, from Kyiv to Antalya",
           font=face(PLAIN, 24), fill=RED)
    y += 38
    rule(d, y, width=4)
    y += 14
    d.text((EDGE, y), "KYIV  ·  RIYADH  ·  ANTALYA  ·  GENOA  ·  CALIFORNIA  ·  CINCINNATI",
           font=face(BOLD, 17), fill=GREY)
    y += 30

    # Lead story: full width, navy bar on the left.
    head, body = STORIES[0]
    lead = wrap(d, body, face(PLAIN, 23), W - 2 * EDGE - 52)
    box_h = 40 + 34 + len(lead) * 29 + 22
    d.rectangle([EDGE, y, W - EDGE, y + box_h], outline=INK, width=2)
    d.rectangle([EDGE, y, EDGE + 14, y + box_h], fill=NAVY)
    number_chip(d, EDGE + 30, y + 16, 1)
    d.text((EDGE + 72, y + 14), head, font=face(BOLD, 30), fill=NAVY)
    para(d, EDGE + 30, y + 62, lead, face(PLAIN, 23), INK, 29)
    y += box_h + 18

    # Four stories in a two-by-two grid.
    cw = (W - 2 * EDGE - 16) // 2
    ch = 172
    for pos, (head, body) in enumerate(STORIES[1:5]):
        gx = EDGE + (pos % 2) * (cw + 16)
        gy = y + (pos // 2) * (ch + 16)
        d.rectangle([gx, gy, gx + cw, gy + ch], outline=INK, width=2)
        number_chip(d, gx + 12, gy + 12, pos + 2)
        heads = wrap(d, head, face(BOLD, 20), cw - 62)[:2]
        ny = para(d, gx + 52, gy + 12, heads, face(BOLD, 20), INK, 24)
        paras = wrap(d, body, face(PLAIN, 19), cw - 26)[:4]
        para(d, gx + 13, ny + 10, paras, face(PLAIN, 19), INK, 24)
    y += 2 * ch + 16 + 18

    # Last story on a navy band.
    head, body = STORIES[5]
    d.rectangle([EDGE, y, W - EDGE, y + 104], fill=NAVY)
    number_chip(d, EDGE + 14, y + 14, 6)
    d.text((EDGE + 56, y + 14), head, font=face(BOLD, 24), fill=GOLD)
    tail = wrap(d, body, face(PLAIN, 20), W - 2 * EDGE - 30)
    para(d, EDGE + 15, y + 50, tail, face(PLAIN, 20), SNOW, 26)

    # Gold footer rule, then the source line.
    d.line([(EDGE, H - 48), (W - EDGE, H - 48)], fill=GOLD, width=2)
    d.text((EDGE, H - 34), "Sources: BBC, Reuters, AP, Le Monde, AFP  —  20 Nov 2026",
           font=face(PLAIN, 18), fill=GREY)

    page.save("entry.png", format="PNG", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
