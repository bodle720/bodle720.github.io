from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("assets/favicon")
OUT_DIR.mkdir(parents=True, exist_ok=True)

BG = "#0f172a"       # site dark navy
TEXT = "#f8fafc"     # near-white
ACCENT = "#38bdf8"   # cyan accent

def load_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()

def make_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = max(2, size // 14)
    radius = max(4, size // 6)

    # Rounded dark background
    draw.rounded_rectangle(
        [pad, pad, size - pad, size - pad],
        radius=radius,
        fill=BG,
        outline=ACCENT,
        width=max(1, size // 28),
    )

    # Text
    font_size = int(size * 0.43)
    font = load_font(font_size)
    text = "CV"

    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (size - text_w) / 2
    y = (size - text_h) / 2 - size * 0.03

    draw.text((x, y), text, font=font, fill=TEXT)

    # Small accent line
    line_w = int(size * 0.38)
    line_h = max(2, size // 36)
    line_x0 = (size - line_w) / 2
    line_y0 = int(size * 0.73)
    draw.rounded_rectangle(
        [line_x0, line_y0, line_x0 + line_w, line_y0 + line_h],
        radius=line_h,
        fill=ACCENT,
    )

    return img

# Main high-res source
make_icon(512).save(OUT_DIR / "favicon-512x512.png")

# Browser favicon sizes
make_icon(32).save(OUT_DIR / "favicon-32x32.png")
make_icon(16).save(OUT_DIR / "favicon-16x16.png")

# Apple touch icon
make_icon(180).save(OUT_DIR / "apple-touch-icon.png")

# Multi-size .ico
icons = [make_icon(s) for s in [16, 32, 48, 64, 128, 256]]
icons[0].save(
    OUT_DIR / "favicon.ico",
    sizes=[(s, s) for s in [16, 32, 48, 64, 128, 256]],
    append_images=icons[1:],
)

print(f"Saved favicon files to {OUT_DIR.resolve()}")