"""用真实 YAML 解析器验证 frontmatter（正则近似可能漏判）。"""
import pathlib

import yaml

T = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert")
txt = (T / "SKILL.md").read_text(encoding="utf-8")

# 提取 frontmatter（起始 --- 到下一个 ---）
assert txt.startswith("---"), "未以 --- 开头"
end = txt.index("\n---", 3)
fm_raw = txt[3:end]

try:
    data = yaml.safe_load(fm_raw)
    print("✓ YAML 解析成功")
except Exception as e:
    print(f"✗ YAML 解析失败: {e}")
    raise SystemExit(1)

print()
print("=== 解析出的顶层字段 ===")
for k, v in data.items():
    if isinstance(v, str):
        disp = v.replace("\n", " ")[:70] + ("…" if len(v) > 70 else "")
        print(f"  {k:20} = {disp}")
    elif isinstance(v, list):
        print(f"  {k:20} = [list, {len(v)} 项] 首项: {v[0] if v else '-'}")
    else:
        print(f"  {k:20} = {v!r}")

print()
# 关键校验
desc = data.get("description", "")
trg = data.get("triggers", [])
print("=== 关键校验 ===")
print(f"  displayName        : {data.get('displayName')}")
print(f"  version            : {data.get('version')}")
print(f"  icon               : {data.get('icon')}")
print(f"  description 字符数 : {len(desc):,}")
print(f"  description 行数   : {len(desc.splitlines())}")
print(f"  triggers 数量      : {len(trg)}")
print(f"  triggers 类型      : {type(trg).__name__}")

# 折叠标量应把换行转成空格
assert "\n" not in desc, "description 折叠标量仍含换行（YAML 折叠失败）"
print()
print("✓ description 折叠标量正常（多行已合并为单段）")
print(f"  开头: {desc[:60]}…")
print(f"  结尾: …{desc[-40:]}")

# 检查是否有重复键（YAML 静默取后者）
import re

keys = re.findall(r"^([a-zA-Z_][a-zA-Z0-9_]*):", fm_raw, re.M)
dupes = {k for k in keys if keys.count(k) > 1}
print()
if dupes:
    print(f"⚠️ 重复键: {dupes}")
else:
    print(f"✓ 无重复键（共 {len(keys)} 个顶层键）")

# 触发词重复检查（v2.0 曾出现「节拍时间」重复）
trg = data.get("triggers", [])
tdup = sorted({x for x in trg if trg.count(x) > 1})
if tdup:
    print(f"⚠️ triggers 重复项: {tdup}")
else:
    print(f"✓ triggers 无重复（共 {len(trg)} 项）")

print()
print("=== 加载就绪判定 ===")
if dupes or tdup:
    print("⚠️ 存在重复项，建议清理")
else:
    print("✓ frontmatter 可被标准 YAML 解析器正确加载")
    print(f"  宿主读取 displayName = 「{data.get('displayName')}」")
    print(f"  宿主读取 icon= {data.get('icon')}")
