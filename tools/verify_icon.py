"""校验 skill frontmatter 的 icon 字段与图标文件完整性。"""
import pathlib
import re
import struct

B = pathlib.Path(__file__).resolve().parent.parent
txt = (B / "SKILL.md").read_text(encoding="utf-8")
fm = txt.split("---")[1]

print("=== frontmatter 关键字段 ===")
for k in ["name", "displayName", "slug", "icon", "version", "last_research_date"]:
    m = re.search(r"^" + k + r":\s*(.+)$", fm, re.M)
    print(f"  {k:20} {m.group(1).strip() if m else '**缺失**'}")

m = re.search(r"^icon:\s*(.+)$", fm, re.M)
print()
if not m:
    print("✗ 未找到 icon 字段")
    raise SystemExit(1)

rel = m.group(1).strip().strip('"').strip("'")
ico = (B / rel).resolve()
print("=== 图标文件 ===")
print("  引用路径:", rel)
print("  解析绝对:", ico)
print("  文件存在:", ico.exists())
if not ico.exists():
    raise SystemExit(1)

d = ico.read_bytes()
assert d[:8] == b"\x89PNG\r\n\x1a\n", "不是合法 PNG"
w, h = struct.unpack(">II", d[16:24])
print(f"  PNG 尺寸: {w}x{h}")
print(f"  文件大小: {len(d):,} bytes")
print("  PNG 签名: 合法")

sv = ico.with_suffix(".svg")
if sv.exists():
    print(f"  SVG 源文件: {sv.name} ({sv.stat().st_size:,} bytes)")
else:
    print("SVG 源文件: 缺失")

print()
print("✓ icon 字段与文件一致性校验通过")
