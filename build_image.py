"""Draw the 18 November 2026 world-news front page (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 48
BLACK = (0, 0, 0)
RED = (178, 0, 0)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_BOLD = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def story(draw, x, max_w, y, kicker, headline, deck, head_f, deck_f, kick_f):
    draw.text((x, y), kicker, font=kick_f, fill=RED)
    y += 30
    lines = wrap(draw, headline, head_f, max_w)
    y = draw_lines(draw, lines, head_f, x, y, BLACK, 40)
    y += 4
    lines = wrap(draw, deck, deck_f, max_w)
    y = draw_lines(draw, lines, deck_f, x, y, BLACK, 29)
    return y


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    x = MARGIN
    max_w = W - 2 * MARGIN
    y = 28

    # Masthead
    mast = font(SERIF_BOLD, 88)
    d.text((x, y), "WORLD NEWS", font=mast, fill=BLACK)
    y += 108
    d.line([(x, y), (W - MARGIN, y)], fill=BLACK, width=4)
    y += 16

    # Date line
    date_f = font(SANS_BOLD, 28)
    d.text((x, y), "WEDNESDAY  •  18 NOVEMBER 2026", font=date_f, fill=RED)
    y += 48
    d.line([(x, y), (W - MARGIN, y)], fill=RED, width=2)
    y += 24

    kick_f = font(SANS_BOLD, 22)
    head_f = font(SANS_BOLD, 44)
    deck_f = font(SANS, 26)
    sub_head = font(SANS_BOLD, 34)
    sub_deck = font(SANS, 24)

    # Lead story
    d.text((x, y), "ASIA", font=kick_f, fill=RED)
    y += 30
    lines = wrap(d, "APEC opens in Shenzhen as Trump lands in Manila for Quad talks", head_f, max_w)
    y = draw_lines(d, lines, head_f, x, y, BLACK, 52)
    y += 6
    lines = wrap(d, "First-ever trilateral summit with Xi and Putin set for tomorrow in Shenzhen.", deck_f, max_w)
    y = draw_lines(d, lines, deck_f, x, y, BLACK, 32)
    y += 18
    d.line([(x, y), (W - MARGIN, y)], fill=BLACK, width=2)
    y += 18

    # Story 2
    y = story(d, x, max_w, y, "UKRAINE", "Ukraine hits Crimea bridge for a second day",
              "Russia pounds bridges in Kyiv in reply.", sub_head, sub_deck, kick_f)
    y += 16
    d.line([(x, y), (W - MARGIN, y)], fill=BLACK, width=1)
    y += 18

    # Story 3
    y = story(d, x, max_w, y, "MIDDLE EAST", "Iran drones hit U.S. radar base in Bahrain",
              "Kuwait reports interceptions as U.S. and Iran trade strikes.", sub_head, sub_deck, kick_f)
    y += 16
    d.line([(x, y), (W - MARGIN, y)], fill=BLACK, width=1)
    y += 18

    # Story 4
    y = story(d, x, max_w, y, "ASIA", "North Korea fires missile into the Sea of Japan",
              "Launch follows a landmine incident at the border.", sub_head, sub_deck, kick_f)

    # Bottom strip + footer
    strip_f = font(SANS, 22)
    foot_f = font(SANS, 20)
    strip = "Cyclone Akvan bears down on Andhra Pradesh  •  Dhoni retires from IPL  •  NVIDIA posts $115.8B quarter  •  Britain and Australia sanction Israeli settlement firms"
    foot = "18 NOVEMBER 2026 — compiled from major wire reports"
    sy = H - 108
    d.line([(x, sy - 14), (W - MARGIN, sy - 14)], fill=RED, width=2)
    slines = wrap(d, strip, strip_f, max_w)
    sy = draw_lines(d, slines, strip_f, x, sy, BLACK, 28)
    d.text((x, H - 36), foot, font=foot_f, fill=GREY)

    img.save("entry.png")
    print("saved entry.png, stories end at y =", y)


if __name__ == "__main__":
    main()
