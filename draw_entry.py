"""Draw the 20 November 2026 world-news front page (1024x1024 PNG)."""
import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
NAVY = (27, 42, 74)
GOLD = (217, 164, 65)
RED = (178, 34, 34)
INK = (30, 30, 30)
GREY = (110, 108, 100)
SKY = (198, 220, 235)
SEA = (70, 110, 150)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = lambda s: ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", s)
SANS = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)
SANS_B = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, font, color, max_w, leading):
    for line in wrap(d, text, font, max_w):
        d.text((x, y), line, font=font, fill=color)
        y += leading
    return y


def flag_us(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(178, 34, 52))
    for i in range(7):
        yy = y + i * h / 7
        if i % 2 == 0:
            d.rectangle([x, yy, x + w, yy + h / 7], fill=(255, 255, 255))
    d.rectangle([x, y, x + w * 0.4, y + h * 0.54], fill=(60, 59, 110))
    for r in range(3):
        for c in range(4):
            d.ellipse([x + 4 + c * 8, y + 4 + r * 6, x + 7 + c * 8, y + 7 + r * 6], fill=(255, 255, 255))


def flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.ellipse([x + 4, y + 4, x + 16, y + 16], fill=(255, 222, 0))
    for sx, sy in [(22, 6), (26, 12), (26, 18), (22, 23)]:
        d.ellipse([x + sx, y + sy, x + sx + 4, y + sy + 4], fill=(255, 222, 0))


def flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 50))


def cyclone(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    cx, cy = x + w // 2, y + h // 2
    for r in range(18, 105, 14):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=20 + r, end=250 + r,
              fill=(255, 255, 255), width=9)
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 255, 255))
    d.polygon([(x, y + h), (x + w * 0.35, y + h * 0.62), (x + w * 0.62, y + h * 0.78),
               (x + w, y + h * 0.6), (x + w, y + h)], fill=(120, 150, 90))
    for i in range(6):
        rx = x + 150 + i * 26
        d.line([rx, y + h - 44, rx - 8, y + h - 22], fill=(255, 255, 255), width=3)
    d.rectangle([x + 10, y + h - 26, x + 92, y + h - 4], fill=NAVY)
    d.text((x + 16, y + h - 23), "ODISHA", font=SANS_B(14), fill=(255, 255, 255))


def document(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 234, 220))
    d.rectangle([x, y, x + w, y + h], outline=(150, 140, 120), width=2)
    for i in range(4):
        end = x + w - 52 if i < 2 else x + w - 14
        d.line([x + 14, y + 18 + i * 16, end, y + 18 + i * 16],
               fill=(90, 85, 75), width=3)
    d.ellipse([x + w - 44, y + 8, x + w - 8, y + 44], fill=GOLD)
    d.ellipse([x + w - 36, y + 16, x + w - 16, y + 36],
              outline=(150, 110, 20), width=2)
    flag_us(d, x + 12, y + h - 34, 34, 22)
    flag_cn(d, x + 52, y + h - 34, 34, 22)
    flag_ru(d, x + 92, y + h - 34, 34, 22)


def broken_bridge(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.rectangle([x, y + h * 0.68, x + w, y + h], fill=SEA)
    d.rectangle([x, y + h * 0.5, x + w * 0.38, y + h * 0.58], fill=(90, 90, 95))
    d.rectangle([x + w * 0.62, y + h * 0.5, x + w, y + h * 0.58], fill=(90, 90, 95))
    d.line([x + w * 0.38, y + h * 0.52, x + w * 0.5, y + h * 0.75], fill=(90, 90, 95), width=5)
    for cx, cy, r in [(x + w * 0.5, y + 26, 14), (x + w * 0.58, y + 18, 10), (x + w * 0.44, y + 34, 9)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(120, 120, 120))
    for k in range(8):
        ang = k * math.pi / 4
        d.line([x + w * 0.5 + 4 * math.cos(ang),
                y + 30 + 4 * math.sin(ang),
                x + w * 0.5 + 18 * math.cos(ang),
                y + 30 + 18 * math.sin(ang)], fill=(255, 140, 0), width=4)


def chart(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(235, 240, 245))
    bars = [0.3, 0.45, 0.4, 0.6, 0.55, 0.8, 0.75, 1.0]
    bw = w // len(bars)
    for i, b in enumerate(bars):
        bh = int(h * 0.7 * b)
        d.rectangle([x + i * bw + 4, y + h - 14 - bh, x + (i + 1) * bw - 4, y + h - 14],
                    fill=(46, 125, 50) if i < 7 else (178, 34, 34))
    d.line([x + 8, y + h * 0.2, x + w - 14, y + 12], fill=(178, 34, 34), width=4)
    d.polygon([(x + w - 14, y + 12), (x + w - 30, y + 10), (x + w - 16, y + 26)], fill=(178, 34, 34))
    d.text((x + 8, y + 4), "$2T", font=SANS_B(20), fill=(30, 30, 30))


def flag_eu(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(0, 51, 153))
    for k in range(8):
        ang = k * math.pi / 4
        d.ellipse([x + w / 2 + 8 * math.cos(ang) - 2, y + h / 2 + 5 * math.sin(ang) - 2,
                   x + w / 2 + 8 * math.cos(ang) + 2, y + h / 2 + 5 * math.sin(ang) + 2],
                  fill=(255, 222, 0))


def flag_ua(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 2], fill=(0, 91, 187))
    d.rectangle([x, y + h / 2, x + w, y + h], fill=(255, 213, 0))


def summit_table(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(228, 232, 240))
    d.ellipse([x + 10, y + h * 0.55, x + w - 10, y + h * 0.85], fill=(120, 90, 60))
    d.ellipse([x + 22, y + h * 0.6, x + w - 22, y + h * 0.78], fill=(150, 115, 75))
    flag_eu(d, x + 14, y + 12, 30, 20)
    flag_ua(d, x + 52, y + 8, 30, 20)
    flag_us(d, x + 90, y + 12, 30, 20)


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 118], fill=NAVY)
    t = "THE WORLD TODAY"
    d.text(((W - d.textlength(t, font=SERIF_B(62))) / 2, 14), t, font=SERIF_B(62), fill=(255, 255, 255))
    t = "FRIDAY 20 NOVEMBER 2026"
    d.text(((W - d.textlength(t, font=SANS_B(32))) / 2, 76), t, font=SANS_B(32), fill=GOLD)
    d.rectangle([0, 118, W, 122], fill=GOLD)
    t = "FIVE STORIES THAT DEFINED THE DAY"
    d.text(((W - d.textlength(t, font=SANS_B(15))) / 2, 132), t, font=SANS_B(15), fill=GREY)

    # Lead story: Cyclone Akvan
    lx, lw = 36, 560
    y = 158
    d.text((lx, y), "CYCLONE AKVAN", font=SANS_B(18), fill=RED)
    y = para(d, lx, y + 26, "Cyclone Akvan slams India's east coast",
             SERIF_B(42), INK, lw, 50)
    y = para(d, lx, y + 6,
             "Severe cyclone makes landfall near Gopalpur, Odisha, by noon. "
             "About 300,000 people evacuated, 423 rescue teams deployed; "
             "winds 90\u2013100 kmph, gusting to 110.",
             SANS(19), (60, 60, 60), lw, 26)
    cyclone(d, 620, 158, 368, 250)
    d.text((620, 414), "LANDFALL NEAR GOPALPUR, ODISHA", font=SANS_B(13), fill=GREY)

    d.line([36, 448, 988, 448], fill=INK, width=3)

    # 2x2 grid
    cells = [
        ("SHENZHEN", "Trump, Xi and Putin sign peace declaration",
         "An 81-minute summit yields a four-point declaration on nuclear talks, "
         "oil supply and UN reform \u2014 but no binding cuts, deadlines or plans "
         "to end the wars in Ukraine and Iran.", document),
        ("KERCH BRIDGE", "Putin vows hard retaliation for bridge strikes",
         "After Ukraine's third strike on the Crimea bridge this week, Putin drops "
         "any moratorium on hitting energy infrastructure and shipping.", broken_bridge),
        ("WALL STREET", "Anthropic's record $2 trillion debut",
         "The Nasdaq debut tops SpaceX's record listing \u2014 but Wall Street ends "
         "sharply lower as it fails to revive AI fervour.", chart),
        ("BERLIN", "Coalition of the Willing meets on Ukraine",
         "European leaders join Zelensky and US envoys; Trump dials in. Europe "
         "expects to join new Ukraine peace talks soon; the E3 and Kyiv urge a "
         "winter energy ceasefire.", summit_table),
    ]
    xs = [36, 524]
    ys = [468, 712]
    for i, (kick, head, deck, art) in enumerate(cells):
        cx, cy = xs[i % 2], ys[i // 2]
        art(d, cx, cy, 140, 140)
        tx = cx + 156
        d.text((tx, cy), kick, font=SANS_B(14), fill=RED)
        yy = para(d, tx, cy + 20, head, SERIF_B(24), INK, 308, 29)
        para(d, tx, yy + 4, deck, SANS(15), (60, 60, 60), 308, 20)

    d.line([36, 966, 988, 966], fill=INK, width=2)
    t = "THE WORLD TODAY  \u2022  20 NOVEMBER 2026"
    d.text(((W - d.textlength(t, font=SANS(13))) / 2, 978), t, font=SANS(13), fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    draw()
