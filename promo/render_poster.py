from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "promo" / "task-prompt-orchestrator-poster-base.png"
OUT = ROOT / "promo" / "task-prompt-orchestrator-poster-cn.png"


def font(size: int, weight: str = "regular") -> ImageFont.FreeTypeFont:
    fonts = {
        "light": Path(r"C:\Windows\Fonts\msyhl.ttc"),
        "regular": Path(r"C:\Windows\Fonts\msyh.ttc"),
        "bold": Path(r"C:\Windows\Fonts\msyhbd.ttc"),
        "latin_bold": Path(r"C:\Windows\Fonts\arialbd.ttf"),
    }
    path = fonts.get(weight, fonts["regular"])
    if not path.exists():
        path = Path(r"C:\Windows\Fonts\simhei.ttf")
    return ImageFont.truetype(str(path), size)


def box(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=24, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def center_text(draw, box_xy, value, fnt, fill):
    left, top, right, bottom = box_xy
    bbox = draw.textbbox((0, 0), value, font=fnt)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((left + (right - left - tw) / 2, top + (bottom - top - th) / 2 - 2), value, font=fnt, fill=fill)


img = Image.open(BASE).convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)

# Calm, premium reading zones over the generated KV.
box(d, (38, 34, 660, 408), (246, 250, 252, 236), (255, 255, 255, 205), 28, 2)
box(d, (54, 1138, 312, 1326), (8, 18, 28, 218), (83, 211, 239, 135), 18, 2)
box(d, (382, 1138, 640, 1326), (8, 18, 28, 218), (128, 232, 166, 130), 18, 2)
box(d, (710, 1138, 968, 1326), (8, 18, 28, 218), (255, 190, 98, 135), 18, 2)
box(d, (72, 1392, 952, 1492), (12, 15, 18, 228), (255, 187, 96, 155), 22, 2)

img = Image.alpha_composite(img, overlay)
d = ImageDraw.Draw(img)

# Header: fewer words, stronger hierarchy.
d.text((78, 76), "Task Prompt", font=font(56, "latin_bold"), fill=(12, 20, 30, 255))
d.text((78, 136), "Orchestrator", font=font(56, "latin_bold"), fill=(12, 20, 30, 255))
d.text((80, 222), "低 Token 工作流调度台", font=font(31, "bold"), fill=(20, 70, 86, 255))
d.text((82, 276), "把模糊需求变成专业执行路径", font=font(25, "regular"), fill=(34, 67, 82, 255))

# Minimal chips.
chips = [("能力优先", 82), ("最小索引", 244), ("验证交付", 406)]
for label, x in chips:
    chip = (x, 335, x + 128, 378)
    box(d, chip, (8, 34, 46, 238), (67, 204, 232, 150), 18, 1)
    center_text(d, chip, label, font(20, "bold"), (238, 252, 255, 255))

# Three polished cards, intentionally short.
cards = [
    ("01", "收集", "目标 / 输入 / 约束"),
    ("02", "路由", "Skill / 插件 / 工具"),
    ("03", "验收", "证据 / 链接 / 输出"),
]
for (num, title, desc), x in zip(cards, [84, 412, 740]):
    d.text((x, 1172), num, font=font(25, "light"), fill=(234, 244, 250, 230))
    d.text((x, 1212), title, font=font(36, "bold"), fill=(248, 253, 255, 255))
    d.text((x, 1268), desc, font=font(21, "regular"), fill=(202, 223, 230, 245))

# Bottom promise: one focused message.
d.text((106, 1418), "不全量读取提示词库，只加载命中的最小索引", font=font(27, "bold"), fill=(255, 239, 207, 255))
d.text((106, 1460), "Use $task-prompt-orchestrator  ->  smaller context, stronger workflow", font=font(22, "latin_bold"), fill=(255, 201, 112, 255))

img.convert("RGB").save(OUT, quality=95)
print(OUT)
