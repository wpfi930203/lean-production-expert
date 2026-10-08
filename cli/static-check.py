"""静态检查 cli/ 下的 bash 脚本（无 bash 环境时的替代验证）。

检查项：
1. shebang
2. heredoc 配对（<<EOT ... EOT）
3. set -euo pipefail
4. 4 个标准 flag 是否都有 case 分支
5. local 声明是否合法（不含 risk=0issues 这类粘连）
6. 引号平衡（单引号奇数告警）
7. source ../lib/common.sh 路径是否存在
"""
import pathlib
import re
import sys

CLI = pathlib.Path(r"C:\Users\fiona\.workbuddy\skills\lean-production-expert\cli")
SCRIPTS = sorted(p for p in CLI.rglob("*.sh"))

FLAGS = ["--help", "--explain", "--dry-run", "--json"]
problems = []

for p in SCRIPTS:
    txt = p.read_text(encoding="utf-8")
    lines = txt.split("\n")
    rel = p.relative_to(CLI).as_posix()

    # 1 shebang
    if rel != "lib/common.sh" and not lines[0].startswith("#!"):
        problems.append(f"{rel}: 缺少 shebang")

    # 2 heredoc 配对
    opens = len(re.findall(r"<<'?\s*EOT", txt))
    closes = len(re.findall(r"^\s*EOT\s*$", txt, re.M))
    if opens != closes:
        problems.append(f"{rel}: heredoc 不配对 opens={opens} closes={closes}")

    # 3 set -euo
    if rel != "lib/common.sh" and "set -euo pipefail" not in txt:
        problems.append(f"{rel}: 缺少 set -euo pipefail")

    # 4 flags
    if rel != "lib/common.sh":
        for f in FLAGS:
            if f not in txt:
                problems.append(f"{rel}: 缺少 flag {f}")
        if "case \"${1:-}\" in" not in txt:
            problems.append(f"{rel}: 缺少 case 参数分发")

    # 5 local 粘连
    for i, ln in enumerate(lines, 1):
        m = re.match(r"^\s*local\s+([A-Za-z_][A-Za-z0-9_]*)=(\S*?)([A-Za-z_][A-Za-z0-9_]*)=", ln)
        if m and m.group(1) != m.group(3):
            problems.append(f"{rel}:{i}: local 声明疑似粘连 -> {ln.strip()}")

    # 6 单引号平衡（排除注释行）
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("#"):
            continue
        if ln.count("'") % 2 != 0:
            problems.append(f"{rel}:{i}: 单引号数量为奇数 -> {s[:70]}")

    # 7b 管道-函数陷阱：管道里的 while/函数对 mdbuf_add 的写入会丢（子 shell）
    # 仅当 while 块内确实调用了 mdbuf_add 才算问题；只 printf 到 stdout 是安全的。
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("#"):
            continue  # 注释里提到该模式不算问题
        if re.search(r"\|\s*while\b", ln):
            # 向下找该 while 的 do...done 块，检查是否写 mdbuf_add
            depth, block = 0, []
            for j in range(i, min(i + 25, len(lines))):
                block.append(lines[j])
                if re.search(r"\bdo\b\s*$", lines[j]) or lines[j].strip().endswith(" do"):
                    depth = 1
                    continue
                if depth:
                    if lines[j].strip() == "done":
                        break
                    depth += 1
            joined = "\n".join(block)
            if "mdbuf_add" in joined or re.search(r"^\s*\w+=", joined, re.M):
                problems.append(
                    f"{rel}:{i}: 管道中含 while 且块内有写入 —— 子shell 内对 mdbuf_add/变量的写入会丢失；"
                    f"应先用$(...) 捕获再在当前 shell 逐行处理"
                )
        m2 = re.match(r"^\s*(recommend|run_all)\s*\|", s)
        if m2:
            problems.append(
                f"{rel}:{i}: 管道调用本地函数 `{m2.group(1)}` —— "
                f"函数内 mdbuf_add 的写入发生在子 shell，报告会缺这一段"
            )

    # 8 source 路径（剥掉前导 / 再用 normpath 归一化 ../）
    import os as _os
    for m in re.finditer(r'source\s+"\$\{SCRIPT_DIR\}(/[^\"]+)"', txt):
        relfrag = m.group(1).lstrip("/")
        joined = _os.path.normpath(_os.path.join(str(p.parent), relfrag))
        if not pathlib.Path(joined).exists():
            problems.append(f"{rel}: source 路径不存在 -> {m.group(1)} (解析为 {joined})")

    print(f"[checked] {rel:38} {len(lines):4} lines")

print()
if problems:
    print(f"发现 {len(problems)} 个问题：")
    for x in problems:
        print("  ✗", x)
    sys.exit(1)
print("✓ 全部脚本静态检查通过")
