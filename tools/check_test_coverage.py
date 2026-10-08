"""按**内容**（而非标签）校验 test-prompts-v2.json 的覆盖完整性。

校验 9 处事实校正是否每一条都在 expect 里被明确要求答对。
"""
import json
import pathlib

B = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert")
d = json.loads((B / "test-prompts-v2.json").read_text(encoding="utf-8"))
ps = d["prompts"]
blob = "\n".join(x["prompt"] + "\n" + x["expect"] for x in ps)

# 9 处事实校正：每条给一组「必须出现的关键锚点」
CHECKS = {
    "C01 五大原则非丰田官方": ["不是丰田官方定义", "Womack", "JIT", "两根柱"],
    "C02 14原则非丰田明文": ["Liker", "莱克", "学者归纳", "Toyota Way 2001"],
    "C03 大野生卒+门田作者": ["1912", "1990", "门田安弘", "赠言"],
    "C04 新乡重夫非丰田雇员": ["旭化成", "日本能率协会", "外部顾问"],
    "C05 两本虚构书": ["Manufacturing Excess", "Toyota Catalysts", "无法核实", "Coffey"],
    "C06 今井卒年+原创贡献": ["2023", "维持成本", "SDCA"],
    "C07 OEE 85% 性质": ["Nakajima", "拉伸目标", "0.90", "不是行业中位数"],
    "C08 自働化≠自动化": ["人」字旁", "human touch", "先lean", "先 lean"],
    "C09 3M 因果链": ["因果", "Mura", "Muri", "三分之一"],
}

print("=== 9 处事实校正 · 内容级覆盖 ===")
allok = True
for name, anchors in CHECKS.items():
    miss = [a for a in anchors if a not in blob]
    ok = not miss
    allok &= ok
    print(f"  [{'✓' if ok else '✗'}] {name:26} 锚点 {len(anchors)-len(miss)}/{len(anchors)}"
          + (f"  缺: {miss}" if miss else ""))

print()
print("=== 6 个心智模型 · 覆盖 ===")
MODELS = {
    "M1 时间优先于产能": ["M1 时间优先于产能", "增值比"],
    "M2停滞是最大浪费": ["M2 停滞是最大浪费", "症状", "换型因"],
    "M3 自働化=人的判断权": ["M3 自働化", "停而不改", "响应"],
    "M4 无标准无改善资格": ["M4 SDCA 先于 PDCA", "维持问题"],
    "M5 先lean再digital": ["M5 先lean 再 digital", "放大器"],
    "M6 系统重构非工具项目": ["M6", "项目制", "回潮"],
}
for name, anchors in MODELS.items():
    miss = [a for a in anchors if a not in blob]
    print(f"  [{'✓' if not miss else '✗'}] {name:24}" + (f"  缺: {miss}" if miss else ""))

print()
print("=== 诚实边界与反承诺 ===")
GUARDS = [
    ("不承诺改善率", ["改善率承诺", "不能承诺改善率", "60%–90%"]),
    ("跨行业争议", ["削足适履", "未经专门验证"]),
    ("数字缺口声明", ["数字化 ROI 模型", "禁止给出具体 ROI"]),
    ("阈值非通用标准", ["启发式基线", "通用硬标准", "不是行业中位数"]),
]
for name, anchors in GUARDS:
    miss = [a for a in anchors if a not in blob]
    print(f"  [{'✓' if not miss else '✗'}] {name:22}" + (f"  缺: {miss}" if miss else ""))

print()
print(f"结论：9 处事实校正{'全部覆盖 ✓' if allok else '存在缺口 ✗'}")
print(f"测试总数：{len(ps)}条（fact_check {sum(1 for x in ps if x['type']=='fact_check')} / "
      f"mental_model {sum(1 for x in ps if x['type']=='mental_model')} / "
      f"boundary {sum(1 for x in ps if x['type']=='boundary')} / "
      f"style {sum(1 for x in ps if x['type']=='style')} / "
      f"decoy {sum(1 for x in ps if x['type']=='decoy')}）")
