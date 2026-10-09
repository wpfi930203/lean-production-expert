"""找出 frontmatter 中所有缩进不一致的列表项（YAML 致命）。"""
import pathlib
import re

import yaml

T = pathlib.Path(__file__).resolve().parent.parent
txt = (T / "SKILL.md").read_text(encoding="utf-8")
end = txt.index("\n---", 3)
fm = txt[3:end]
lines = fm.split("\n")

# triggers 列表从哪行开始
start = next(i for i, l in enumerate(lines) if l.startswith("triggers:"))
endlist = next(
    (i for i in range(start + 1, len(lines))
     if lines[i].strip() and not lines[i].lstrip().startswith("-")
     and not lines[i].startswith((" ", "\t"))),
    len(lines),
)

print(f"triggers 列表范围: fm L{start+1} … L{endlist}")
print()

# 统计列表项的前导空白
bad = []
for i in range(start + 1, endlist):
    l = lines[i]
    if not l.strip():
        continue
    if not l.lstrip().startswith("-"):
        continue
    indent = len(l) - len(l.lstrip())
    if indent != 1:
        bad.append((i + 1, indent, l.strip()[:60]))

if bad:
    print(f"✗ 发现 {len(bad)} 个缩进不一致的列表项（YAML 会解析失败）：")
    for ln, ind, content in bad:
        print(f"  fm L{ln}: 前导空格 {ind} 个（应为 1） | {content}")
    print()
    print("修复方案：统一为1 个前导空格，与其余列表项对齐")
else:
    print("✓ triggers 列表缩进一致")

# 修复
if bad:
    fixed = []
    for i in range(len(lines)):
        l = lines[i]
        if l.strip().startswith("- ") and not l.startswith(" "):
            lines[i] = " " + l
            fixed.append(i + 1)
    new_fm = "\n".join(lines)
    try:
        yaml.safe_load(new_fm)
        print(f"✓ 修复 {len(fixed)} 处后 YAML 解析通过")
        (T / "SKILL.md").write_text(
            txt[:3] + new_fm + txt[end:], encoding="utf-8"
        )
        print("  已写回 SKILL.md")
    except Exception as e:
        print(f"✗ 修复后仍失败: {e}")
