from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "promo" / "task-prompt-orchestrator-poster-base.png"
OUT = ROOT / "promo" / "task-prompt-orchestrator-poster-cn.png"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    if bold:
        arial_bold = Path(r"C:\Windows\Fonts\arialbd.ttf")
        if arial_bold.exists():
            return ImageFont.truetype(str(arial_bold), size)
    simhei = Path(r"C:\Windows\Fonts\simhei.ttf")
    return ImageFont.truetype(str(simhei), size)


def box(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=24, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def wrap(text: str, draw: ImageDraw.ImageDraw, fnt: ImageFont.FreeTypeFont, max_width: int):
    lines = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            test = line + ch
            left, top, right, bottom = draw.textbbox((0, 0), test, font=fnt)
            if right - left <= max_width or not line:
                line = test
            else:
                lines.append(line)
                line = ch
        if line:
            lines.append(line)
    return lines


def draw_text(draw, xy, value, fnt, fill, max_width=None, line_gap=8):
    x, y = xy
    lines = wrap(value, draw, fnt, max_width) if max_width else value.split("\n")
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        left, top, right, bottom = draw.textbbox((x, y), line, font=fnt)
        y += bottom - top + line_gap
    return y


img = Image.open(BASE).convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
d = ImageDraw.Draw(overlay)

box(d, (36, 34, 660, 430), (246, 250, 252, 232), (255, 255, 255, 190), 26, 2)
box(d, (42, 1126, 330, 1336), (8, 18, 28, 212), (119, 225, 255, 120), 18, 2)
box(d, (368, 1126, 657, 1336), (8, 18, 28, 212), (148, 234, 171, 120), 18, 2)
box(d, (696, 1126, 984, 1336), (8, 18, 28, 212), (255, 190, 98, 130), 18, 2)
box(d, (54, 1378, 968, 1502), (12, 15, 18, 230), (255, 187, 96, 150), 22, 2)

img = Image.alpha_composite(img, overlay)
d = ImageDraw.Draw(img)

# Header.
d.text((72, 70), "Task Prompt", font=font(62, True), fill=(15, 24, 34, 255))
d.text((72, 134), "Orchestrator", font=font(62, True), fill=(15, 24, 34, 255))
d.text((76, 216), "低 token 工作流调度台", font=font(32), fill=(20, 62, 78, 255))
d.text((76, 268), "把模糊需求变成可执行、可验证、可交接的专业工作流", font=font(24), fill=(37, 68, 86, 255))
d.text((76, 310), "先扫描能力  ·  再选择最小索引  ·  最后生成提示词包", font=font(23), fill=(38, 100, 112, 255))

for label, x in [("Capability-first", 76), ("Prompt Packets", 286), ("Low Token", 500)]:
    left, top, right, bottom = d.textbbox((0, 0), label, font=font(20, True))
    box(d, (x - 10, 354, x + right - left + 18, 398), (10, 32, 44, 230), (57, 197, 232, 180), 18, 1)
    d.text((x, 364), label, font=font(20, True), fill=(236, 251, 255, 255))

# Feature cards.
features = [
    ("01  收集输入", "目标、文件、约束、权限、验收标准先归位"),
    ("02  路由能力", "优先调用已安装 skill、插件、脚本和索引"),
    ("03  节省 token", "不全量读取提示词库，只加载命中的最小文件"),
]
for (title, body), x in zip(features, [62, 388, 716]):
    d.text((x, 1162), title, font=font(30), fill=(245, 252, 255, 255))
    draw_text(d, (x, 1212), body, font(22), (204, 225, 232, 255), max_width=230, line_gap=8)

# CTA.
d.text((92, 1404), "适合：image2 工作流 · GitHub 发布 · 插件扫描 · 多步骤自动化 · 专业提示词库路由", font=font(24), fill=(250, 245, 232, 255))
d.text((92, 1452), "Use $task-prompt-orchestrator  →  smallest useful workflow, verified output", font=font(25, True), fill=(255, 207, 126, 255))

img.convert("RGB").save(OUT, quality=94)
print(OUT)
