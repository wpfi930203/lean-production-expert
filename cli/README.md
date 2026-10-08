# cli/ — 精益生产专家 v2.0 工具流子树

> 把认知OS 的「执行端」物化成可对话的 bash 工具。**思维顾问 + 实操套件**，不是 RPA。
> 零外部依赖：纯 bash 4 + POSIX coreutils。**不要求 jq / yq / Python。**

## 脚本清单

| 脚本 | 类别 | 解决什么问题 | 对应认知层章节 |
|---|---|---|---|
| `protocol/agentic.sh` | Protocol | 按 7 个研究维度收集事实，输出诊断前取数单与派生判据 | §11 Agentic Protocol |
| `decision/tool-select.sh` | 决策树 | 按 6 棵决策树选工具，给出「上什么 + 为什么不选别的 + 它掩盖了什么」 | §10.4 playbook + §10.5 反模式 |
| `decision/fact-check.sh` | 决策树 | 7 处流行谬误速查 + 自检（开口前必过） | §10.1 事实校正 |
| `workflow/diagnosis-sop.sh` | Workflow | 五阶段走查 +「完成判据」卡口 + Top 8 失败模式自检 | §10.3 心智模型 M1–M6 |
| `workflow/gemba-check.sh` | Workflow | 30 分钟车间快诊（5 问），判断工具用得对不对 | §10.3 + `research/02-tools.md` §5 |

## 快速开始

```bash
cd cli

# 1. 先过事实校正（开口前必过，7 张卡）
./decision/fact-check.sh --all

# 2. 不知道该上什么工具 → 走 6 棵决策树
./decision/tool-select.sh

# 3. 手上有个问题要诊断 → 按 7 维度取数
./protocol/agentic.sh

# 4. 改善做到一半 → 五阶段走查 + 失败模式自检
./workflow/diagnosis-sop.sh

# 5. 快速判断一家企业的精益是否"真的在做"
./workflow/gemba-check.sh
```

## 标准接口

每个脚本都支持 4 个 flag：

| Flag | 行为 |
|---|---|
| `--help` | 用法 + 这个脚本解决什么问题（< 30 行） |
| `--explain` | **教学模式**：打印背后的心智模型、判据、来源出处（不交互） |
| `--dry-run` | 走完所有问题但不写报告文件 |
| `--json` | 报告以 JSON 输出到 stdout（机器可读，可接pipeline） |

无 flag → 交互式默认模式，最后写 markdown 报告到当前目录。
额外 flag：`fact-check.sh --all` 直接打印全部 7 张速查卡（非交互）。

**建议用法**：不确定这个脚本背后的逻辑时，先跑 `--explain`，再跑交互模式。

## 设计原则

1. **CLI 是思维顾问的延伸，不是自动执行器**——输出的是"提问框架 + 判据"，不是"结论"。
2. **数字纪律贯穿所有脚本**：所有输出都区分【公式系数】/【某企业实测】/【语料未覆盖】。
   启发式基线（增值比 <5%、换型 >30%、准时率 <95%）**明确标注为非通用阈值，须本厂校准**。
3. **不承诺改善率**：所有涉及效果的脚本都带实证提醒（精益失败率常被估 60%–90%）。
4. **诚实边界**：脚本均声明"本脚本基于用户自述，非现场核实；不替代实地诊断"。

## 依赖

```bash
# bash 4+ 与标准 coreutils 即可
# Windows Git Bash / WSL / macOS / Linux 均可用
```

> 注：若在 Windows 原生 PowerShell 中运行，需通过 Git Bash 或 WSL 调用：
> `bash cli/decision/fact-check.sh --all`

### 无bash 环境时的静态检查

若当前环境没有可用的 bash（如某些精简的 Windows 环境），可用 Python 做静态检查，
验证 shebang、`set -euo pipefail`、heredoc 配对、4 个标准 flag、`local` 声明合法性、
引号平衡与 `source` 路径：

```bash
python cli/static-check.py
```

该检查不能替代真机运行，但能拦住绝大多数语法与拼写错误。

## 与 SKILL.md 的关系

CLI 是 §10–§12 认知层的**可执行投影**：

- **📌 playbook 权威版本在 `SKILL.md` §10.4**；本目录各脚本的 `--explain` 是它的对话化投影。
  修改 playbook 请只改 SKILL.md §10.4，避免脚本与文档说法不一致。
- 脚本里的每一条判据，都能追溯到 `references/research/` 的具体章节
- `--explain` 输出的心智模型，与 `SKILL.md` §10.3 六个心智模型一一对应
- 脚本的诚实边界，与 `SKILL.md` §12.1 保持一致

**认知层是权威，CLI 是它的便利实现。** 若两者冲突，以 `SKILL.md` 与 `references/research/` 为准。
