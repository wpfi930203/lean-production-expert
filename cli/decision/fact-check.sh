#!/usr/bin/env bash
# fact-check.sh — 精益事实校正器（开口前必过的 7 处流行谬误）
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../lib/common.sh"

MODE="interactive"

usage() {
  cat <<'EOT'
用法: fact-check.sh [--help] [--explain] [--dry-run] [--json] [--all]

精益领域事实谬误速查与自检。

解决什么问题:
  精益这行最贵的成本不是不会做工具，而是建立在错误出处上的论证。
  本脚本把 7 处最常见的流行谬误做成速查卡，并在交互模式下自查。

选项:
  --help     显示本帮助
  --explain  打印 7 处谬误的详细论证与来源
  --dry-run  同 --all，不写文件
  --json     JSON 输出
  --all      直接打印全部速查卡（非交互）
EOT
}

# 编号|流行说法|正确结论|影响
CARDS=$(cat <<'EOT'
1|《新丰田生产方式》是大野耐一 2013 年写的|作者是门田安弘（河北大学出版社）。大野耐一 1990 年已去世，只写了赠言|讨论"大野晚年回应丰田神话"时不能引此书为大野著作
2|大野耐一 2013 年仍在出书|大野耐一生卒 1912-02-29 — 1990-05-28|大野只能引用文献记录，不能有"他最近说"
3|精益五大原则是丰田官方定义|是沃马克与琼斯的外部重构。丰田官方自述为 JIT + 自働化两根柱|学五大原则要知道这是"教学模型"非"丰田原话"
4|丰田 14 项管理原则是丰田明文|是莱克（Jeffrey Liker）的学者归纳。丰田 2001 内部文档仅公开"持续改善+尊重人"摘要|引用须说明是莱克的归纳版
5|今井正明 2024 年去世|1930-09-01 — 2023-06-12（享年 92）|—
6|新乡重夫是丰田雇员 / TPS 共同开发者|他主要在旭化成等化学企业与日本能率协会任职，是外部顾问。西方称其为"JIT 共同开发者"，丰田内部与不少研究者认为他主要是记录者与形式化者|精益史上最常被争辩的归属问题
7|Pascale Borel《Manufacturing Excess》(2010)、Steve Callahan《Toyota Catalysts》(2013)|两书均无法核实，判定误记。已替换为 Coffey《The Myth of Japanese Efficiency》(2006) 与 鎌田慧《自動車絶望工場》(1972)|两书在中文语境被广泛引用，属虚构出处
EOT
)

explain() {
  cat <<'EOT'
【为什么这份校正表值钱】

这 7 处全部来自"看起来很合理但没查"的流传。它们在中文语境被广泛引用，
包括在看似专业的培训材料里。错误的行业常识比没有常识更危险——因为它
让你以为自己知道。

【逐条论证】

#1 《新丰田生产方式》(2013, 河北大学出版社)
  作者是门田安弘（Yasuhiro Monden），他与大野耐一合著过
  《Just-in-Time for Today and Tomorrow》(1988)，是TPS 的教材化整合者。
  大野耐一在该书写了赠言，但不是作者。常见误传原因：书名带"丰田生产方式"，
  又由大野写序，读者自然归因于大野。

#2 大野耐一生卒
  1912-02-29（大连出生）— 1990-05-28。2022 年入选美国汽车名人堂。
  任何"大野最近说""大野 2013 年出版"的说法都是错的。
  常见误传原因：与大野同名的 books、门田安弘的书、以及 2013 年中文版重印
  三件事被混为一谈。

#3 五大原则的归属
  丰田官方 TPS 页自述两大柱：Just-in-Time + Jidoka（自働化）。
  五大原则（精确价值/拉动/一次做对/快速流动/友好社会）出自
  Womack & Jones《Lean Thinking》(1996)，是外部重构。
  研判：两者是"本体 vs 教学模型"关系，不矛盾。但初学者常把沃麦克模型
  误认为丰田的官方自我定义——这是概念漂移的起点。

#4 14 原则的归属
  Jeffrey Liker《The Toyota Way》(2004) 的学者归纳，四类
  （理念/流程/人/问题解决）。丰田 2001 年内部文档《Toyota Way 2001》
  未公开全文，公开摘要仅"持续改善 + 尊重人"。
  研判：莱克的归纳很有价值，但说"丰田 14 原则"时应说明这是莱克版本。

#5 今井正明卒年
  1930-09-01 — 2023-06-12。Kaizen Institute 2025 年设追授性
  "Masaaki Imai Distinctive Award"（首届得主 Shell）。

#6 新乡重夫的归属（最微妙的一条）
  他一生主要在旭化成等化学企业、日本能率协会（JMA）任职，是**外部顾问**。
  NYT 讣告称其与大野"共同开发 JIT"，但丰田内部与不少研究者认为他主要是
  "记录者与形式化者"，并非发明者。
  研判：这是精益史上最常被争辩的归属问题。他的方法（SMED/poka-yoke/源检）
  极其有价值，但"TPS 是丰田原创"与"TPS 是新乡总结的"这两种说法都不准确。

#7 两本查无此书的书
  Pascale Borel 确有其人，但是法国 Clermont 营销学教授（性别刻板研究），
  与精益无关，无此书。Steve Callahan 无此精益著作记录（Clinton Callahan
  写的是个人成长/Archiarchy）。
  正确的批判性文献是：Coffey《The Myth of Japanese Efficiency》(2006)、
  鎌田慧《自動車絶望工場》(1972)、Durand & Hatzfeld《Living Labour》(2003)。
  常见误传原因：与 Leslie Kaplan《Excess — The Factory》(1982)、
  或Burawoy 的民族志混淆。

【方法论纪律】
  任何书名 / 年份 / 人名 / 名言，出处不明就标"待核实"，绝不填充。
  引文 ≤ 30 字。矛盾并列保留，不和稀泥。

来源: references/research/01-figures.md §0、04-canon.md「已核验矛盾点」
EOT
}

run_all() {
  h1 "精益事实校正卡 · 7 处流行谬误"
  dim "开口前必过。错误的行业常识比没有常识更危险。"
  echo
  printf '%s\n' "$CARDS" | while IFS='|' read -r n claim truth impact; do
    [[ -z "${n:-}" ]] && continue
    h2 "谬误 $n"
    printf '  %s流传说法%s：%s\n' "$C_YEL" "$C_RESET" "$claim"
    printf '  %s正确结论%s：%s\n' "$C_GRN" "$C_RESET" "$truth"
    [[ -n "${impact:-}" && "$impact" != "—" ]] && printf '  %s影响%s：%s\n' "$C_DIM" "$C_RESET" "$impact"
    echo
  done
  warn "另：新乡重夫 1990 年去世（不是 1980），1909-01-08 出生。"
}

run() {
  h1 "精益事实校正 · 自检"
  dim "回答下列问题，检验你（或你的方案）是否踩了流行谬误。"
  echo
  ask q1 "你打算引用的书/文章，出处核实了吗？(是/否/不适用)" ""
  ask q2 "有没有把'五大原则'或'14 原则'说成丰田官方定义？(是/否)" ""
  ask q3 "有没有引用大野耐一'最近'的说法？(是/否)" ""
  ask q4 "有没有把新乡重夫说成丰田雇员？(是/否)" ""
  ask q5 "有没有引用 Borel《Manufacturing Excess》或 Callahan《Toyota Catalysts》？(是/否)" ""
  ask q6 "有没有把'自働化'当成'自动化/无人化'？(是/否)" ""
  echo

  local risk=0
  local issues=""
  [[ "$q1" == "否" ]] && { risk=1; issues+="  ✗ 出处未核实——任何书名/年份/人名/名言，出处不明就标'待核实'，绝不填充\n"; }
  [[ "$q2" == "是" ]] && { risk=1; issues+="  ✗ 五大原则是沃麦克/琼斯的外部重构，丰田官方是 JIT + 自働化两根柱\n"; }
  [[ "$q2" == "是" ]] && issues+="  ✗ 14 原则是莱克的学者归纳，非丰田明文\n"
  [[ "$q3" == "是" ]] && { risk=1; issues+="  ✗ 大野耐一 1990 年已去世（1912-1990），只能引用文献记录\n"; }
  [[ "$q4" == "是" ]] && { risk=1; issues+="  ✗ 新乡重夫主要在旭化成等化学企业任职，是外部顾问，非丰田雇员\n"; }
  [[ "$q5" == "是" ]] && { risk=1; issues+="  ✗ 两书均查无此书（虚构出处）。请改用 Coffey(2006) 或 鎌田慧(1972)\n"; }
  [[ "$q6" == "是" ]] && { risk=1; issues+="  ✗ 自働化 = 人的判断权（异常即停），≠ 自动化/无人化\n"; }

  h1 "自检结果"
  if [[ "$risk" == "0" ]]; then
    ok "未发现事实谬误。可继续。"
  else
    err "发现以下问题，必须修正后再输出："
    printf '%b' "$issues"
  fi
  echo
  info "完整 7 张卡：运行 $0 --all"
  info "详细论证：$0 --explain"

  local REPORT="fact-check-$(TODAY).md"
  mdbuf_reset
  mdbuf_add "# 精益事实校正自检"
  mdbuf_add ""
  mdbuf_add "- 日期：$(TODAY)"
  mdbuf_add "- 来源：lean-production-expert v2.0 · cli/decision/fact-check.sh"
  mdbuf_add ""
  mdbuf_add "## 自检结果"
  mdbuf_add ""
  mdbuf_add "- 是否踩到流行谬误：$([[ "$risk" == "0" ]] && echo 否 || echo **是**)"
  if [[ "$risk" != "0" ]]; then
    mdbuf_add ""
    mdbuf_add "## 必须修正"
    mdbuf_add ""
    mdbuf_add '```'
    mdbuf_add "$(printf '%b' "$issues")"
    mdbuf_add '```'
  fi
  mdbuf_add ""
  mdbuf_add "## 7 处谬误速查"
  mdbuf_add ""
  mdbuf_add "| # | 流传说法 | 正确结论 |"
  mdbuf_add "|---|---|---|"
  local cards_copy="$CARDS"
  while IFS='|' read -r n claim truth impact; do
    [[ -z "${n:-}" ]] && continue
    mdbuf_add "| $n | ${claim//|/／} | ${truth//|/／} |"
  done <<< "$cards_copy"

  if [[ "$MODE" == "json" ]]; then
    printf '{"date":"%s","has_myth":"%s"}\n' "$(TODAY)" "$([[ "$risk" == "0" ]] && echo false || echo true)"
    return
  fi

  if [[ "$MODE" == "dry-run" ]]; then
    dim "[dry-run] 未写文件。去掉 --dry-run 可生成 ${REPORT}"
  else
    mdbuf_write "$REPORT"
  fi
}

case "${1:-}" in
  --help|-h)   usage ;;
  --explain)   explain ;;
  --all)       run_all ;;
  --dry-run)   MODE="dry-run"; run ;;
  --json)      MODE="json"; run ;;
  "")          run ;;
  *)err "未知参数：$1"; echo; usage; exit 1 ;;
esac
