"""生成「精益生产专家」skill 图标（v3）。

设计：精益屋（Lean House）—— 丰田 TPS 唯一公认的专属结构符号
  屋顶(白)   = 顾客价值 / 目的
  琥珀过梁   = 价值向下传递（同时把屋顶与双柱在视觉上连成一体）
  双柱(青)   = 准时化 JIT + 自働化 Jidoka —— TPS 两大支柱
  地基(蓝灰) = 标准作业 / 稳定 / 目视化 / 方针管理

为什么不用齿轮：齿轮只表示"制造"，不表示"精益"。
精益屋把 TPS 的结构（目的 → 两柱 → 基础）编码进一个图形，一眼可辨。

v3 相对 v2 的改动（依据渲染后视觉复核）：
  - 屋顶由「人字形雪佛龙」改为**实心三角山墙**——v2 的外飞檐 +
    底部凹口在 200px 下读成"马戏帐篷"，实心三角 unmistakably 是屋顶
  - 琥珀条改为紧贴屋顶下沿的**过梁**，消除 v2 中屋顶与琥珀之间的悬空缝隙
  - 双柱对齐过梁两端，形成"屋顶—过梁—双柱—地基"的连贯受力关系
  - 竖向节奏收紧，整体在方形内居中稳定

输出：
  icons/logo.png   200x200 PNG（对齐 linkfox-amazon-ads 规格）
  icons/logo.svg   矢量源文件（可再编辑，零版权风险）

纯 Pillow 手绘矢量形状，不调用任何图像生成 API。
"""
import pathlib

from PIL import Image, ImageDraw

OUT = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert\icons")
OUT.mkdir(parents=True, exist_ok=True)

S = 200          # 输出尺寸
SS = 4           # 超采样倍数
W = S * SS

# 配色：深海军蓝底 + 白/琥珀/青/蓝灰（与本机其他 skill 图标区分，不撞 linkfox 紫蓝）
BG_TOP = (23, 42, 71)        # #172A47
BG_BOT = (12, 26, 45)        # #0C1A2D
ROOF = (255, 255, 255)       # #FFFFFF
PILLAR = (56, 189, 248)      # #38BDF8
BASE = (150, 180, 216)       # #96B4D8
ACCENT = (250, 204, 21)      # #FACD15

# ---- 结构坐标（以 200px 画布为基准）----
ROOF_APEX = (100.0, 30.0)
ROOF_L = (22.0, 76.0)
ROOF_R = (178.0, 76.0)
LINTEL_Y0, LINTEL_Y1 = 76.0, 85.0
LINTEL_X0, LINTEL_X1 = 62.0, 138.0
COL_Y0, COL_Y1 = 89.0, 150.0
COL_W = 24.0
COL_GAP = 14.0
BASE_Y0, BASE_Y1 = 158.0, 174.0
BASE_X0, BASE_X1 = 40.0, 160.0


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rounded_bg():
    img = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    grad = Image.new("RGB", (1, W))
    for y in range(W):
        grad.putpixel((0, y), lerp(BG_TOP, BG_BOT, y / (W - 1)))
    grad = grad.resize((W, W))
    mask = Image.new("L", (W, W), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, W - 1, W - 1], radius=int(W * 0.22), fill=255)
    img.paste(grad, (0, 0), mask)
    return img


def draw_house(d):
    u = SS

    def P(pts):
        return [(x * u, y * u) for x, y in pts]

    # ---- 屋顶：实心三角山墙（顾客价值 / 目的）----
    d.polygon(P([ROOF_APEX, ROOF_R, ROOF_L]), fill=ROOF)

    # ---- 琥珀过梁：紧贴屋顶下沿，把结构连成一体 ----
    d.rectangle(
        P([(LINTEL_X0, LINTEL_Y0), (LINTEL_X1, LINTEL_Y1)]),
        fill=ACCENT,
    )

    # ---- 双柱：准时化 JIT + 自働化 Jidoka ----
    cx = 100.0
    for x0 in (cx - COL_GAP / 2 - COL_W, cx + COL_GAP / 2):
        d.rounded_rectangle(
            P([(x0, COL_Y0), (x0 + COL_W, COL_Y1)]),
            radius=6 * u,
            fill=PILLAR,
        )

    # ---- 地基：标准作业 / 稳定 / 目视化 ----
    d.rounded_rectangle(
        P([(BASE_X0, BASE_Y0), (BASE_X1, BASE_Y1)]),
        radius=5 * u,
        fill=BASE,
    )


def main():
    img = rounded_bg()
    draw_house(ImageDraw.Draw(img))
    out = img.resize((S, S), Image.LANCZOS)
    png = OUT / "logo.png"
    out.save(png, "PNG", optimize=True)
    print(f"[ok] {png}  ({png.stat().st_size:,} bytes, {S}x{S})")

    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <!-- 精益生产专家 · Lean House（丰田 TPS 结构符号）-->
  <!-- 屋顶=顾客价值  过梁=价值传递  双柱=准时化JIT+自働化Jidoka  地基=标准作业 -->
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#172A47"/>
      <stop offset="1" stop-color="#0C1A2D"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" rx="44" fill="url(#bg)"/>
  <!-- 屋顶（顾客价值 / 目的）-->
  <polygon points="100,30 178,76 22,76" fill="#FFFFFF"/>
  <!-- 过梁：价值向下传递 -->
  <rect x="62" y="76" width="76" height="9" fill="#FACD15"/>
  <!-- 双柱：准时化 JIT + 自働化 Jidoka -->
  <rect x="69" y="89" width="24" height="61" rx="6" fill="#38BDF8"/>
  <rect x="107" y="89" width="24" height="61" rx="6" fill="#38BDF8"/>
  <!-- 地基：标准作业 / 稳定 / 目视化 -->
  <rect x="40" y="158" width="120" height="16" rx="5" fill="#96B4D8"/>
</svg>
"""
    sp = OUT / "logo.svg"
    sp.write_text(svg, encoding="utf-8")
    print(f"[ok] {sp}  ({sp.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
