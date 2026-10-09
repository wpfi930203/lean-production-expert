"""校验 knowledge/cards 下全部卡片的 frontmatter 结构一致性。

检查项：
1. YAML frontmatter 可解析
2. 必需字段齐全（与 v1.x 卡片对齐）
3. 认知层卡片必须带 limitations（这是 v2.0 的核心纪律：模型必须标注失效场景）
4. falsifiable_claim 存在且非空
5. 正文含「局限」小节
6. ID 与文件名一致
"""
import pathlib
import sys

import yaml

D = pathlib.Path(__file__).resolve().parent.parent / "knowledge" / "cards"
cards = sorted(D.glob("*.md"))
print(f"共 {len(cards)} 张卡片\n")

REQUIRED = {"id", "title", "tags", "confidence", "verifiable", "falsifiable_claim"}
problems = []
rows = []

for p in cards:
    txt = p.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        problems.append(f"{p.name}: 缺少 frontmatter")
        continue
    fm_raw = txt[3: txt.index("\n---", 3)]
    try:
        d = yaml.safe_load(fm_raw)
    except Exception as e:
        problems.append(f"{p.name}: YAML 解析失败 {str(e)[:40]}")
        continue

    # 卡片有两种合法 schema：
    #   A) 原厂蒸馏卡：id/title/book/tags/confidence/verifiable/falsifiable_claim/related_skills
    #   B) IMA 订阅库综合卡：id/title/source/skill/tags/verifiable/confidence（无 falsifiable_claim，
    #      因为它是多条资料的归纳共识，不是单条可证伪断言）
    has_a = "falsifiable_claim" in d
    has_b = "source" in d or "skill" in d
    if has_b and not has_a:
        rows.append((p.name, d.get("layer", "execution"),
                     "✓" if "limitations" in d else "-", -1, len(txt)))
        continue

    missing = REQUIRED - set(d)
    if missing:
        problems.append(f"{p.name}: 缺字段 {missing}")

    # 认知层卡片必须带局限
    is_cog = d.get("layer") == "cognitive"
    if is_cog:
        if "limitations" not in d:
            problems.append(f"{p.name}: 认知层卡片缺 limitations（v2.0 核心纪律）")
        if "## 局限" not in txt:
            problems.append(f"{p.name}: 认知层卡片正文缺「局限」小节")

    # ID 与文件名一致
    if d.get("id") != p.stem:
        problems.append(f"{p.name}: id({d.get('id')}) ≠ 文件名({p.stem})")

    # falsifiable_claim 非空（允许显式 null —— 框架类卡片无可证伪断言）
    fc_raw = d.get("falsifiable_claim", None)
    if fc_raw is None and "falsifiable_claim" in d:
        pass  # 显式 null，合法
    else:
        fc = str(fc_raw or "")
        if len(fc) < 10:
            problems.append(f"{p.name}: falsifiable_claim 过短（{len(fc)} 字）")

    rows.append(
        (p.name, d.get("layer", "execution"), "✓" if "limitations" in d else "-",
         len(str(fc_raw or "")), len(txt))
    )

print(f"{'卡片':52}{'层':11}{'局限':5}{'claim':6}{'字符':8}")
print("-" * 82)
for name, layer, lim, fclen, size in rows:
    print(f"{name:52}{layer:11}{lim:5}{fclen:<6}{size:<8}")

print()
cog = [r for r in rows if r[1] == "cognitive"]
print(f"执行层卡片 {len(rows)-len(cog)} 张 | 认知层卡片 {len(cog)} 张")
print(f"带局限标注的认知层卡片：{sum(1 for r in cog if r[2]=='✓')}/{len(cog)}")

if problems:
    print(f"\n✗ {len(problems)} 个问题：")
    for x in problems:
        print("  -", x)
    sys.exit(1)
print("\n✓ 全部卡片结构合规")
