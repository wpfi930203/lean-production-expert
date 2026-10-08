"""安装就绪检查：确认 skill 可被宿主正确发现与加载。

检查项：
1. 目录位于宿主 skill 根目录
2. SKILL.md 存在且 frontmatter 可解析
3. 关键字段齐全（name / displayName / description）
4. 引用的所有内部文件真实存在（无悬空链接）
5. icon 字段与文件一致
6. manifest / meta.json 合法
"""
import json
import pathlib
import re
import struct
import sys

B = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills")
NAME = "lean-production-expert"
T = B / NAME

rows = []


def chk(label, ok, detail=""):
    rows.append((label, ok, detail))


# 1 位置
chk("位于宿主 skill 根目录", T.exists() and T.parent == B, str(T))

# 2 SKILL.md
sk = T / "SKILL.md"
chk("SKILL.md 存在", sk.exists(), f"{sk.stat().st_size:,} bytes" if sk.exists() else "缺失")
if not sk.exists():
    print("SKILL.md 缺失，终止")
    sys.exit(1)

txt = sk.read_text(encoding="utf-8")

# 3 frontmatter 解析
if not txt.startswith("---"):
    chk("frontmatter 格式", False, "缺少起始 ---")
    sys.exit(1)
parts = txt.split("---")
if len(parts) < 3:
    chk("frontmatter 格式", False, "缺少结束 ---")
    sys.exit(1)
fm = parts[1]
chk("frontmatter 格式", True, f"{len(fm):,} 字符")

# 关键字段
fields = {}
for k in ["name", "displayName", "slug", "icon", "version", "description",
          "last_research_date", "license"]:
    m = re.search(r"^" + k + r":\s*(.+)$", fm, re.M)
    fields[k] = m.group(1).strip() if m else None

for k in ["name", "displayName", "description", "version"]:
    chk(f"字段 {k}", bool(fields[k]), (fields[k][:58] + "…") if fields[k] and len(fields[k]) > 58 else (fields[k] or "缺失"))

chk("name 与目录名一致", fields["name"] == NAME, f"{fields['name']} vs {NAME}")
chk("displayName 为中文名", fields["displayName"] == "精益生产专家", fields["displayName"] or "缺失")

# triggers
trg = re.findall(r"^\s*-\s+(.+)$", fm.split("triggers:")[1], re.M) if "triggers:" in fm else []
chk("triggers 数量", len(trg) >= 100, f"{len(trg)} 个")

# 4 悬空链接检查（SKILL.md + INDEX.md 中提到的所有相对路径）
# 排除两类引用：
#   a) 废弃条目：写在 Markdown 删除线 `~~路径~~` 里的，是「已移除」的历史记录，本就不该存在；
#   b) 本地专有：`_distill/` 下是受版权保护的原著语料与蒸馏工作区，
#      仓库版**故意排除**（见 .gitignore）。从 Git 克隆后这些文件不存在是**预期行为**，不算缺陷。
LOCAL_ONLY = ("_distill/",)
refs = set()
for f in [sk, T / "INDEX.md"]:
    if not f.exists():
        continue
    body = f.read_text(encoding="utf-8")
    deprecated = set(re.findall(r"~~`([^`]+)`~~", body))
    for m in re.finditer(r"`((?:references|cli|tools|icons|knowledge|assets|_distill)/[A-Za-z0-9_\-./]+?)`", body):
        p = m.group(1)
        if p in deprecated or p.startswith(LOCAL_ONLY):
            continue
        refs.add(p)
missing = sorted(r for r in refs if not (T / r).exists())
chk(
    "内部引用无悬空",
    not missing,
    f"检查 {len(refs)} 条引用（已排除 {len(LOCAL_ONLY)} 类本地专有路径）"
    + (f"，缺失 {missing[:4]}" if missing else "，全部存在"),
)

# 4b 废弃条目必须真的不存在（防止"标记为已删但文件还在"）
ghost = sorted(r for r in deprecated if (T / r).exists())
chk("废弃条目确已移除", not ghost, f"标记废弃 {len(deprecated)} 条" + (f"，仍存在 {ghost}" if ghost else "，均已移除"))

# 5 icon 一致性
if fields["icon"]:
    ip = (T / fields["icon"].strip().strip('"').strip("'")).resolve()
    ok = ip.exists()
    if ok:
        d = ip.read_bytes()
        ok = d[:8] == b"\x89PNG\r\n\x1a\n"
        w, h = struct.unpack(">II", d[16:24])
        chk("icon 文件有效 PNG", ok, f"{w}x{h}, {len(d):,} bytes")
    else:
        chk("icon 文件有效 PNG", False, f"路径不存在: {ip}")
else:
    chk("icon 文件有效 PNG", False, "未设置 icon 字段")

# 6 meta.json
mp = T / "meta.json"
if mp.exists():
    try:
        m = json.loads(mp.read_text(encoding="utf-8"))
        chk("meta.json 合法", True, f"version {m.get('version')}")
        chk("meta.json 版本与 frontmatter 一致", m.get("version") == fields["version"],
            f"{m.get('version')} vs {fields['version']}")
    except Exception as e:
        chk("meta.json 合法", False, str(e)[:60])
else:
    chk("meta.json 合法", False, "缺失")

# 7 六轨+ cli 完整性（功能性检查）
six = ["01-figures", "02-tools", "03-workflows", "04-canon", "05-sources", "06-glossary"]
smiss = [s for s in six if not (T / "references/research" / f"{s}.md").exists()]
chk("六轨调研齐备", not smiss, f"缺失 {smiss}" if smiss else "6/6")

cli = ["protocol/agentic.sh", "decision/tool-select.sh", "decision/fact-check.sh",
       "workflow/diagnosis-sop.sh", "workflow/gemba-check.sh"]
cmiss = [c for c in cli if not (T / "cli" / c).exists()]
chk("cli 脚本齐备", not cmiss, f"缺失 {cmiss}" if cmiss else "5/5")

vols = [p for p in (T / "references").glob("*.md")]
chk("执行层分册齐备", len(vols) >= 16, f"{len(vols)} 册")

# 输出
print("=" * 72)
print(f"安装就绪检查 · {NAME}（精益生产专家）")
print("=" * 72)
ok_n = 0
for label, ok, detail in rows:
    if ok:
        ok_n += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {label:28} {detail}")
print("=" * 72)
print(f"{ok_n}/{len(rows)} 通过")
print()
print(f"安装位置: {T}")
print(f"中文名  : {fields['displayName']}")
print(f"版本    : {fields['version']}")
sys.exit(0 if ok_n == len(rows) else 1)
