#!/usr/bin/env bash
# gemba-check.sh — 30 分钟车间快诊（资深者进厂就问的 5 个问题）
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../lib/common.sh"

MODE="interactive"

usage() {
  cat <<'EOT'
用法: gemba-check.sh [--help] [--explain] [--dry-run] [--json]

资深精益人走进车间 30 分钟判断"工具用得对不对"的 5 个问题。

解决什么问题:
  不用开诊断会、不用要报表，走一遍车间就能判断一家企业的精益是
  "系统重构"还是"工具装饰"。5 问中≥3 问答不出 → 工具用错了。

选项:
  --help     显示本帮助
  --explain  打印 5 问的判读逻辑与背后信号
  --dry-run  走完不写文件
  --json     JSON 输出
EOT
}

explain() {
  cat <<'EOT'
【30 分钟车间快诊 · 5 问与判读】

问 1  "这条线换一次型要多久？**谁记的**？"
  答不出具体数 / 没人记录 → 换型未管控，SMED 与数据采集缺失，
                看板拉动必受其累
心智模型 M2 · 停滞是最大浪费 / 组合拳 1（SMED 必须先于线平衡）

问 2  "在制品堆在哪？**为什么堆在这**？"
  答"一直都这样" → 无停滞意识，未在 VSM/标准手持层面管控，
                流动层工具缺位
心智模型 M1 · 时间优先于产能 —— 机会在队列不在机器

问 3  "这块板（标准作业/目视/安灯）谁负责更新？**最后更新是什么时候**？"
  板子过期 / 无人更新 → SDCA 维持机制失效，5S 与标准作业在反弹边缘
心智模型 M4 · 无标准无改善资格（SDCA 先于 PDCA）

问 4  "异常发生时**谁停的线**？停了多久、怎么响应的？"
  从不/ 很少停 → 自働化/安灯形同虚设，不良在流出；
                或产量 KPI 压过了异常响应
心智模型 M3 · 自働化 = 人的判断权 —— 停了不响应 = 停而不改

问 5  "上个月改善改了**哪一条**标准作业？"
  标准长期不变 → 改善未闭环，PDCA 没转；所谓"精益"停在表面工具
心智模型 M6 · 精益是系统重构非工具项目

【判读规则】
  5 问中 ≥3 问答不出 / 答非所问 → "工具用得不对"。
  多因三条反模式：
    ① 反模式 1先上工具再诊断（拿看板当装修）
    ② 反模式 11  一次性大项目式精益（无固化）
    ③ 反模式 13  顾问代替现场人员做诊断（违反现地现物）
  → 应回到 **VSM + SDCA 地基**，而不是继续堆工具。

【资深者的一眼信号（补充观察，不必提问）】
  搬运路线交叉 / 在制品堆积的位置在入口还是出口 / 看板有空白格 /
  员工等待的姿态 / 标准作业表的填写痕迹（是否真的天天填）/
  物料积灰日期标签 / 安灯亮着没人动 / 地面画线被踩模糊 /
  换型时众人围观一人干 / 报表与现场计数器对不上

【纪律】
  一切结论必须来自**实地观察**，不能靠会议室推理或二手报表（现地现物）。
  发现矛盾保留，不和稀泥。

来源: research/02-tools.md §5、research/03-workflows.md §E
EOT
}

run() {
  h1 "30 分钟车间快诊"
  dim "现地现物：一切结论来自实地观察，不靠报表推理。"

  local ans=() miss=0
  local qs=(
    "这条线换一次型要多久？谁记的？"
    "在制品堆在哪？为什么堆在这？"
    "这块板谁负责更新？最后更新是什么时候？"
    "异常发生时谁停的线？停了多久、怎么响应的？"
    "上个月改善改了哪一条标准作业？"
  )
  local judge=(
    "答不出具体数/没人记录 → 换型未管控，看板拉动必受其累"
    "答'一直都这样' → 无停滞意识，流动层工具缺位"
    "板子过期/无人更新 → SDCA 维持机制失效，5S 在反弹边缘"
    "从不/很少停 → 自働化形同虚设，或产量 KPI 压过了异常响应"
    "长期不变 → 改善未闭环，PDCA 没转，精益停在表面工具"
  )

  for i in 0 1 2 3 4; do
    h2 "问 $((i+1)) · ${qs[$i]}"
    dim "判读: ${judge[$i]}"
    local a
    ask a "你的观察结果" ""
    ans+=("$a")
    if [[ -z "$a" || "$a" == "答不出" || "$a" == "无人记录" || "$a" == "不知道" || "$a" == "不清楚" || "$a" == "没有更新" || "$a" == "长期不变" ]]; then
      miss=$((miss+1))
      err "记为未答出"
    else
      ok "已记录"
    fi
    echo
  done

  h1 "快诊结论"
  printf '  答不出：%d / 5\n' "$miss"
  echo
  if [[ "$miss" -ge 3 ]]; then
    err "≥3 问答不出 → **工具用得不对**"
    cat <<'EOT'

  多因三条反模式：
    ① 先上工具再诊断（拿看板当装修）—— 无诊断就开药治不到根
    ② 一次性大项目式精益 —— 无固化，项目结束即回潮
    ③ 顾问代替现场人员做诊断 —— 违反现地现物，改善不可持续

  正确动作：回到 **VSM + SDCA 地基**，而不是继续堆工具。
EOT
  elif [[ "$miss" -eq 2 ]]; then
    warn "2 问未答出 → 存在薄弱环节，建议复查对应工具的使用方式。"
  else
    ok "多数问题有答案 → 工具使用方式基本健康，继续看固化机制。"
  fi
  echo
  info "进阶观察：资深者还会看搬运路线交叉、在制品堆积位置、看板空白格、"
  info "标准作业表填写痕迹、报表与现场计数器是否对得上。运行 $0 --explain"

  local REPORT="gemba-check-$(TODAY).md"
  mdbuf_reset
  mdbuf_add "# 30 分钟车间快诊"
  mdbuf_add ""
  mdbuf_add "- 日期：$(TODAY)"
  mdbuf_add "- 来源：lean-production-expert v2.0 · cli/workflow/gemba-check.sh"
  mdbuf_add ""
  mdbuf_add "## 结论"
  mdbuf_add ""
  mdbuf_add "- 答不出：${miss} / 5"
  mdbuf_add "- 判定：$([[ "$miss" -ge 3 ]] && echo '工具用得不对（≥3 问答不出）' || ([[ "$miss" -eq 2 ]] && echo '存在薄弱环节' || echo '基本健康'))"
  mdbuf_add ""
  mdbuf_add "## 5 问记录"
  mdbuf_add ""
  mdbuf_add "| # | 问题 | 观察结果 | 判读 |"
  mdbuf_add "|---|---|---|---|"
  for i in 0 1 2 3 4; do
    mdbuf_add "| $((i+1)) | ${qs[$i]} | ${ans[$i]} | ${judge[$i]} |"
  done
  mdbuf_add ""
  mdbuf_add "## 诚实边界"
  mdbuf_add ""
  mdbuf_add "- 本次为**用户自述**，非现场核实结果。"
  mdbuf_add "- 5 问是资深者的启发式快筛，**不能替代实地诊断**。"
  mdbuf_add "- 一切结论应以现场一手观察为准（现地现物）。"

  if [[ "$MODE" == "json" ]]; then
    printf '{"date":"%s","missed":"%s","total":"5","verdict":"%s"}\n' "$(TODAY)" "$miss" \
      "$([[ "$miss" -ge 3 ]] && echo tools_misused || ([[ "$miss" -eq 2 ]] && echo weak_spots || echo healthy))"
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
  --dry-run)   MODE="dry-run"; run ;;
  --json)      MODE="json"; run ;;
  "")          run ;;
  *)err "未知参数：$1"; echo; usage; exit 1 ;;
esac
