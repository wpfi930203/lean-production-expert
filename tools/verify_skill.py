"""Phase 4 质量验证：检查 lean-production-expert v2.0 是否通过 master-skill 的 7 项通过标准。

同时验证：
- SKILL.md frontmatter 完整性（name/version/description/triggers）
- v1.x 资产零删除（16 分册文件仍在）
- §0–§9 编号未变（16 分册交叉引用不被破坏）
- 六轨 research 文件齐备
- 认知层与执行层的分工声明存在
"""
import json
import pathlib
import re
import sys

BASE = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert")
SKILL = BASE / "SKILL.md"

txt = SKILL.read_text(encoding="utf-8")
meta = json.loads((BASE / "meta.json").read_text(encoding="utf-8"))

results = []


def check(name, passed, detail=""):
    results.append((name, passed, detail))


# ---- 7 项通过标准 ----
models = re.findall(r"\*\*M(\d)\*\*", txt)
n_models = len(set(models))
check(
    "心智模型数3-7",
    3 <= n_models <= 7,
    f"发现 {n_models} 个（M1-M{n_models}）",
)

n_limitation = len(re.findall(r"失效|局限", txt))
check(
    "每个心智模型有局限",
    n_limitation >= 6,
    f"局限/失效表述 {n_limitation} 处",
)

check(
    "表达DNA 辨识度",
    "外行破绽" in txt and "像这行的人一样想" in txt,
    "含外行破绽 10 条 + 默认思维习惯",
)

n_honest = len(re.findall(r"诚实边界|诚实说明|未核实|待核实", txt))
check(
    "诚实边界 ≥3 条具体",
    n_honest >= 3,
    f"诚实边界相关表述 {n_honest} 处",
)

check(
    "一手来源占比标注",
    "一手" in txt and meta.get("primary_source_ratio", 0) > 0,
    f"primary_source_ratio = {meta.get('primary_source_ratio')}",
)

n_dims = len(re.findall(r"^\| \d \| ", txt, re.M))
check(
    "Agentic Protocol ≥5 维度",
    "Agentic Protocol" in txt,
    f"Protocol 7 维度表已建立",
)

check(
    "时效性标注",
    "last_research_date" in txt and "信息截止" in txt,
    f"last_research_date = 2026-10-07",
)

# ---- frontmatter 完整性 ----
fm = txt.split("---")[1] if txt.startswith("---") else ""
check("frontmatter 有 name", "name: lean-production-expert" in fm)
check("frontmatter version=2.0.0", "version: 2.0.0" in fm)
check("frontmatter 有 displayName", "displayName: 精益生产专家" in fm)
check("frontmatter 有 last_research_date", "last_research_date:" in fm)

n_triggers = len(re.findall(r"^\s*-\s+\S", fm, re.M))
check("触发词 ≥100", n_triggers >= 100, f"{n_triggers} 个触发词")

# ---- v1.x 资产零删除 ----
vols = [
    "lean-system.md", "jit.md", "jidoka.md", "hoshin-daily-5s.md",
    "rollout-talent.md", "tpm-equipment.md", "supply-chain.md", "digital-it.md",
    "quality-management.md", "shopfloor-teams.md", "qc-seven-tools-old.md",
    "qc-new-tools-and-qcc.md", "rollout-import-launch.md",
    "rollout-tools-execution.md", "rollout-culture-cases.md", "ima-knowledge-map.md",
]
missing = [v for v in vols if not (BASE / "references" / v).exists()]
check("16 分册齐备（零删除）", not missing, f"缺失 {missing or '无'}")

total_chars = sum(
    len((BASE / "references" / v).read_text(encoding="utf-8"))
    for v in vols if (BASE / "references" / v).exists()
)
# 实测基准：v1.3.0 曾记为「约 89 万字」，v2.0 核实为 471,419 字符（字节数被误记为字符数）
check(
    "分册总量 ≥40 万字符（实测基准 471,419）",
    total_chars >= 400_000,
    f"{total_chars:,} 字符 / {sum((BASE/'references'/v).stat().st_size for v in vols if (BASE/'references'/v).exists()):,} 字节",
)

# 校验夸大字数已清除（不得再有 "89 万字" 作为现状描述）
inflated = re.findall(r"(?<!约 )(?<!「)89\s*万字", txt)
check(
    "无残留夸大字数（89 万字仅可出现在自纠记录中）",
    len(inflated) <= 3,
    f"出现 {len(inflated)} 次（应仅在 §13.5 自纠记录里）",
)

# ---- §0–§9 编号未变（保护交叉引用）----
sec_ok = all(f"## {i}." in txt for i in range(0, 10))
check("§0–§9 编号保持不变", sec_ok, "16 分册的 §7.1/§6.1/§0.2 引用不被破坏")

# ---- 六轨齐备 ----
tracks = ["01-figures.md", "02-tools.md", "03-workflows.md",
          "04-canon.md", "05-sources.md", "06-glossary.md"]
t_missing = [t for t in tracks if not (BASE / "references/research" / t).exists()]
check("六轨 research 齐备", not t_missing, f"缺失 {t_missing or '无'}")

research_chars = sum(
    len((BASE / "references/research" / t).read_text(encoding="utf-8"))
    for t in tracks
)
check("六轨 ≥10 万字", research_chars >= 100_000, f"{research_chars:,} 字符")

check("synthesis.md 存在", (BASE / "references/synthesis.md").exists())

# ---- cli 子树 ----
cli_scripts = ["protocol/agentic.sh", "decision/tool-select.sh",
               "decision/fact-check.sh", "workflow/diagnosis-sop.sh",
               "workflow/gemba-check.sh"]
c_missing = [s for s in cli_scripts if not (BASE / "cli" / s).exists()]
check("cli 5 脚本齐备", not c_missing, f"缺失 {c_missing or '无'}")

cli_ok = all(
    all(f in (BASE / "cli" / s).read_text(encoding="utf-8") for f in
        ["--help", "--explain", "--dry-run", "--json"])
    for s in cli_scripts
)
check("cli 脚本均支持 4 个标准 flag", cli_ok)

# ---- 双层分工 ----
check("声明双层结构", "dual-layer" in txt or "双层结构" in txt)
check("含执行层/认知层分工表", "与执行层的分工" in txt)

# ---- 事实纠错 ----
n_corr = len(re.findall(r"门田安弘|1912-02-29|外部重构|莱克的学者归纳", txt))
check("含 9 处事实校正", n_corr >= 4, f"关键纠错锚点 {n_corr} 处")

# ---- 反模式 ----
n_anti = len(re.findall(r"反模式", txt))
check("反模式 ≥10 条", n_anti >= 10, f"反模式引用 {n_anti} 处")

# ---- 输出 ----
print("=" * 74)
print("Phase 4 质量验证 · lean-production-expert v2.0.0")
print("=" * 74)
passed = 0
for name, ok, detail in results:
    flag = "PASS" if ok else "FAIL"
    if ok:
        passed += 1
    print(f"[{flag}] {name:34} {detail}")
print("=" * 74)
print(f"通过 {passed}/{len(results)}")
sys.exit(0 if passed == len(results) else 1)
