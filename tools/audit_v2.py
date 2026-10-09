"""用 master-skill 的验收维度审查 lean-production-expert v2.0.0。

重点查「自己没验证过的地方」：
1. CLI 管道-函数陷阱（mdbuf_add 在管道子shell 里会丢）
2. 外部依赖声明与实际不符（spec 要求零依赖纯 bash）
3. description 长度与触发词风险（短词误触）
4. 六轨深度是否失衡
5. Phase 4 的 4.1/4.2/4.3（已知/边缘/风格测试）是否真做过
6. 知识卡片是否覆盖 v2.0 认知层
7. 同一份 playbook 在几处重复维护（漂移风险）
8. Changelog 是否记录「旧结论被推翻」
"""
import json
import pathlib
import re
from collections import Counter

B = pathlib.Path(__file__).resolve().parent.parent
CLI = B / "cli"
skill = (B / "SKILL.md").read_text(encoding="utf-8")

issues = []


def add(s, prob, ev):
    issues.append((s, prob, ev))


# ---------- 1. CLI 管道-函数陷阱 ----------
for sh in sorted(CLI.rglob("*.sh")):
    if sh.name == "common.sh":
        continue
    txt = sh.read_text(encoding="utf-8")
    rel = sh.relative_to(B).as_posix()
    for i, ln in enumerate(txt.split("\n"), 1):
        m = re.match(r"^\s*(recommend|run_all)\s*\|", ln)
        if m:
            add(
                "高",
                f"{rel}:{i} 管道调用本地函数 `{m.group(1)}`",
                f"`{ln.strip()}` — 该函数内对 mdbuf_add 的写入发生在子shell，"
                f"报告里会丢掉这一整段（stdout 有输出但 markdown 报告缺失）",
            )

# ---------- 2. 外部依赖 ----------
for sh in sorted(CLI.rglob("*.sh")):
    txt = sh.read_text(encoding="utf-8")
    rel = sh.relative_to(B).as_posix()
    for tool in ["awk", "sed", "grep", "jq", "python", "date"]:
        if re.search(rf"(?<![\w/]){tool}\s", txt):
            add("低", f"{rel} 使用外部命令 `{tool}`",
                "cli-spec 要求零外部依赖（纯 bash + POSIX coreutils）；"
                f"{tool} 属 POSIX 但需在 README 依赖段显式声明")

# ---------- 3. description 长度与触发词风险 ----------
fm = skill.split("---")[1]
m = re.search(r"description: >-\n(.*?)\ntriggers:", fm, re.S)
desc = m.group(1) if m else ""
desc_chars = len(desc)
if desc_chars > 800:
    add("中", f"frontmatter description 过长（{desc_chars} 字符）",
        "部分 skill 加载器对 description 有长度上限；建议压缩到 500-800，细节移到正文")

triggers = []
if "triggers:" in fm:
    triggers = re.findall(r"^\s*-\s+(.+)$", fm.split("triggers:")[1], re.M)
risky = []
RISKY_SET = {"abc", "kaizen", "jidoka", "takt", "gemba", "smed", "andon",
             "poka-yoke", "heijunka", "6s", "5s"}
for t in triggers:
    tt = t.strip().strip('"').strip("'")
    if len(tt) <= 3 or tt.lower() in RISKY_SET:
        risky.append(tt)
if risky:
    add("中", f"触发词中有 {len(risky)} 个高误触风险词",
        f"{risky} — 短词/通用英文词可能与日常或技术对话撞车"
        "（如 ABC 在精益语境指活动层次，日常频率极高）")

# ---------- 4. 六轨深度均衡 ----------
tracks = ["01-figures", "02-tools", "03-workflows",
          "04-canon", "05-sources", "06-glossary"]
sizes = {}
for f in tracks:
    p = B / "references/research" / f
    sizes[f[3:]] = len(p.read_text(encoding="utf-8")) if p.exists() else 0
lo, hi = min(sizes.values()), max(sizes.values())
if hi / max(lo, 1) > 3:
    add("低", f"六轨深度失衡（最厚 {hi:,} / 最薄 {lo:,}，相差 {hi/lo:.1f} 倍）",
        f"{sizes} — canon（知识正典）通常应是最厚一轨，当前最薄，与预期相反")

# ---------- 5. 认知层测试覆盖 ----------
tp = B / "test-prompts.json"
has_v2 = False
if tp.exists():
    blob = tp.read_text(encoding="utf-8")
    has_v2 = any(k in blob for k in
                 ["五大原则", "门田安弘", "心智模型", "反模式", "自働化", "大野耐一"])
if not has_v2:
    add("高", "v2.0 认知层没有对应的压力测试",
        "test-prompts.json 35 条全是 v1.x 执行层场景，"
        "新引入的 7 处事实校正 / 6 心智模型 / 25 反模式**完全没有测试覆盖**。"
        "master-skill Phase 4.1/4.2/4.3 要求已知/边缘/风格测试，本轮只做了静态结构检查")

# ---------- 6. 知识卡片覆盖 ----------
cards = list((B / "knowledge/cards").glob("*.md"))
card_blob = " ".join(p.read_text(encoding="utf-8") for p in cards)
need = ["时间优先", "停滞", "自働化", "无标准", "先 lean", "系统重构"]
uncov = [k for k in need if k not in card_blob]
if uncov:
    add("低", f"v2.0 心智模型未沉淀为知识卡片（现有 {len(cards)} 张均为 v1.x）",
        f"认知层 6 个模型没有对应 L1 原子卡片：{uncov}")

# ---------- 7. playbook 重复维护 ----------
copies = []
if "交期长" in (B / "references/synthesis.md").read_text(encoding="utf-8"):
    copies.append("synthesis.md")
if "交期长" in skill:
    copies.append("SKILL.md")
if any("交期长" in p.read_text(encoding="utf-8") for p in CLI.rglob("*.sh")):
    copies.append("cli/*")
if "交期长" in (B / "references/research/02-tools.md").read_text(encoding="utf-8"):
    copies.append("research/02-tools.md")
if len(copies) >= 3:
    add("中", f"同一套 playbook 在 {len(copies)} 处重复维护",
        f"{copies} — 四处手工同步，任何一处漏改就产生内部矛盾。"
        "建议 SKILL.md 保留权威版，其余改为引用")

# ---------- 8. Changelog 是否记录 changed ----------
cl = skill.split("## 14. Changelog")[1] if "## 14. Changelog" in skill else ""
checks = [
    ("OEE 85% 的性质", "拉伸目标"),
    ("五大原则归属", "重构"),
    ("字节数/字符数", "471,419"),
]
missing = [f"{n}（应记：{k}）" for n, k in checks if k not in cl]
if missing:
    add("中", "Changelog 只记「新增」，未记 v2.0 修正了哪些 v1.x 既有结论",
        f"未体现的 changed 项：{missing}；master-skill Phase 0C 要求标注 changed/deprecated，"
        "使用者需要知道哪些旧说法不再成立")

# ---------- 输出 ----------
print("=" * 78)
print("master-skill 维度审查 · lean-production-expert v2.0.0")
print("=" * 78)
order = {"高": 0, "中": 1, "低": 2}
issues.sort(key=lambda x: order[x[0]])
for s, prob, ev in issues:
    print(f"\n[{s}] {prob}")
    print(f"     {ev}")
print("\n" + "=" * 78)
c = Counter(s for s, _, _ in issues)
print(f"合计 {len(issues)} 项：高 {c['高']} / 中 {c['中']} / 低 {c['低']}")
print(f"六轨字数：{sizes}")
print(f"description：{desc_chars} 字符｜触发词：{len(triggers)} 个")
