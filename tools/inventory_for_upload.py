#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""上传前盘点：区分「可公开」与「有版权风险」的内容。"""
import json
from pathlib import Path

B = Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert")

CATS = {
    "根文件": [B / "SKILL.md", B / "INDEX.md", B / "meta.json", B / "test-prompts.json", B / "test-prompts-v2.json"],
    "references（16 分册）": sorted((B / "references").glob("*.md")),
    "references/research（六轨）": sorted((B / "references" / "research").glob("*.md")),
    "tools": sorted((B / "tools").glob("*.py")),
    "cli": sorted((B / "cli").rglob("*")),
    "icons": sorted((B / "icons").glob("*")),
    "knowledge/cards": sorted((B / "knowledge" / "cards").glob("*.md")),
    "★_distill/normalized（原著全文 OCR）": sorted((B / "_distill" / "lean-books" / "normalized").glob("*.txt")),
    "★_distill/candidates（原文提取稿）": sorted((B / "_distill" / "lean-books" / "candidates").glob("*.md")),
    "_distill/extract（逐页 OCR 分块）": sorted((B / "_distill" / "lean-books" / "extract").glob("*")),
    "_distill 其他": [p for p in (B / "_distill").rglob("*") if p.is_file()],
}

# 去重（「其他」会包含前面已列出的）
seen = set()
print("=" * 88)
print("上传内容盘点")
print("=" * 88)
grand = 0
rows = []
for label, files in CATS.items():
    tot = 0
    n = 0
    for f in files:
        if not f.is_file():
            continue
        if f in seen:
            continue
        seen.add(f)
        tot += f.stat().st_size
        n += 1
    grand += tot
    rows.append((label, n, tot))
    print(f"  {label:38} {n:>5} 文件 {tot/1024/1024:>8.2f} MB")

print(f"  {'总计':38} {len(seen):>5} 文件 {grand/1024/1024:>8.2f} MB")

print()
print("=" * 88)
print("⚠️ 版权风险分级")
print("=" * 88)
NORM = B / "_distill" / "lean-books" / "normalized"
norm_bytes = sum(f.stat().st_size for f in NORM.glob("*.txt"))
print(f"""
【高风险 · 不建议公开】
  _distill/lean-books/normalized/*.txt  ({norm_bytes/1024/1024:.2f} MB)
  ↑ 这是 8 本受版权保护书籍的 **OCR 全文**（298 万字符）。公开等同于全文转载。
    涉及：丰田生产方式/大野耐一、The Toyota Way/Liker(McGraw-Hill)、
    改变世界的机器、精益思想、学习观察、精益工具箱、金矿Ⅰ–Ⅲ

【中风险 · 建议仅私有】
  _distill/lean-books/candidates/*.md
  ↑ 逐页原文摘录（每条 ≤150 字，但累计量大）

【低风险 · 可公开】
  SKILL.md / INDEX.md / references/*.md / tools/ / cli/ / icons/ / knowledge/
  ↑ 你的原创结构化产物 + 短引用（已遵守 ≤150 字引文纪律）
  ⚠️ 但 SKILL.md 内含对原著的观点转述与少量引用，属「合理使用」边界内，仍建议先私有
""")

lic = "内部蒸馏产物，语料版权归原始资料作者所有"
sk = (B / "SKILL.md").read_text(encoding="utf-8")
print(f"SKILL.md 自带 license 字段: 「{lic}」")
print(f"实际是否包含该声明: {lic in sk}")

# 仓库体积估算（排除 normalized）
safe_bytes = grand - norm_bytes
print()
print(f"若**排除** normalized（原著全文）：{safe_bytes/1024/1024:.2f} MB")
print(f"若**包含** normalized：{grand/1024/1024:.2f} MB")

# 检查是否有 .gitignore
print()
print(f".gitignore 存在: {(B/'.gitignore').exists()}")
print(f"是否已是 git 仓库: {(B/'.git').exists()}")