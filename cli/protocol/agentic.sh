#!/usr/bin/env bash
# agentic.sh — 精益诊断 Agentic Protocol 落地
# 拿到一个新问题时，按这行的人的标准做功课题纲（7 个维度）再回答。
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../lib/common.sh"

MODE="interactive"

usage() {
  cat <<'EOT'
用法: agentic.sh [--help] [--explain] [--dry-run] [--json]

按精益生产的 7 个研究维度收集事实，输出一份诊断前功课单。

解决什么问题:
  资深精益人面对任何问题，不会直接开药。他们先按固定维度把事实取齐，
  避免"没基线就下结论"。本脚本把这套取数动作结构化成 7 个维度。

7 个维度:
  1 客户需求基准   2 时间结构   3 浪费与 3M 归因   4 现有标准与执行度
  5 设备与瓶颈     6 供应链与需求稳定性   7 组织与文化

选项:
  --help     显示本帮助
  --explain  打印背后的心智模型与来源（教学模式，不交互）
  --dry-run  走完所有问题但不写报告文件
  --json     报告以 JSON 输出到stdout
EOT
}

explain() {
  cat <<'EOT'
【Agentic Protocol · 为什么是这 7 个维度】

核心原则：精益不靠训练语料硬答。涉及具体企业/产线/数字时，先取数再发言。

心智模型 M1 · 时间优先于产能
  精益所有诊断的落点是时间，不是产能、成本、士气。
  → 所以维度 2（时间结构）是最优先的取数项：L/T 拆解 + 增值比。
  局限：研发周期极长/定制化极高的场景，流动价值下降，须换研发管理框架。

心智模型 M2 · 停滞（队列）是最大的浪费
  库存/搬运/等待都是症状，源头是"下游没拉动上游"。
  → 所以维度 3 要求把浪费折算成天与元，而不是贴"七大浪费"标签。

心智模型 M4 · 无标准就没有改善的资格（SDCA 先于 PDCA）
  维持问题与改善问题是两种病。
  → 所以维度 4 必须问"标准存在吗？被执行了吗？"三问，才能进入改善。

心智模型 M6 · 精益是系统重构，不是一堆工具项目
  项目制精益失败率常被估60%–90%。
  → 所以维度 7 问"谁每天看这个数字？异常谁被叫到现场？写进标准作业了吗？"

数字纪律:
  维度 2 的在制品数量、维度 5 的微停，必须【实地一手数】，
  不用报表。报告里必须标明每条数字属于【公式系数】/【某企业实测】/【语料未覆盖】。

来源: references/research/03-workflows.md §A、references/synthesis.md §9
EOT
}

# ---------- 交互主体 ----------
run() {
  h1 "精益诊断 · Agentic Protocol 取数单"
  dim "纪律：涉及具体企业/产线/数字时必须先取数，不得凭语料编造。"

  h2 "维度 1 · 客户需求基准"
  info "Takt 的分母来自这里。销售口头承诺不算数。"
  ask d1_qty"客户日需求量（件/天）" ""
  ask d1_var "需求波动幅度（高/中/低）" "中"
  ask d1_spec "客户特殊要求（IATF/客户审核/无）" "无"

  h2 "维度 2 · 时间结构（M1 优先项）"
  info "必须实地走线 + 一手数在制品，不要用报表。"
  ask d2_lt   "当前前置时间 L/T（天）" ""
  ask d2_vat  "其中增值作业时间（小时/天）" ""
  ask d2_wip  "在制品数量（一手计数）" ""
  ask d2_plt  "情报前置时间（下达订单到开工，天）" ""

  h2 "维度 3 · 浪费与 3M 归因"
  info "把等待/库存折算成天与元，而不是贴标签。"
  ask d3_top1 "最大的一段停滞在哪（工序名）" ""
  ask d3_w1   "该停滞折算（天）" ""
  ask d3_c1   "该停滞折算（元/年，或'未折算'）" "未折算"
  ask d3_mura "波动/不均衡（Mura）主要来源" "未确认"

  h2 "维度 4 · 现有标准与执行度（M4 三问）"
  warn "三问不全通过，就不要开改善方案。"
  ask d4_std  "标准作业/作业标准是否存在？(有/无/部分)" ""
  ask d4_exec "是否被执行？(是/否/部分)" ""
  ask d4_last "标准最后更新时间" "未记录"
  ask d4_chk  "点检是否真实执行？(是/否/不适用)" "不适用"

  h2 "维度 5 · 设备与瓶颈"
  info "微停通常无记录，需实测。"
  ask d5_oee  "OEE 现状（%）" ""
  ask d5_avail "时间稼动率（%）" ""
  ask d5_perf "性能稼动率（%）" ""
  ask d5_qual "良品率（%）" ""
  ask d5_sm   "换型时间（分钟）" ""
  ask d5_smr  "换型占工序时间比例（%）" ""
  ask d5_bn   "瓶颈工序" "未确认"

  h2 "维度 6 · 供应链与需求稳定性"
  info "拉动的前提是上游可信赖。不稳就先治供应链。"
  ask d6_otd  "供应商准时交付率（%）" ""
  ask d6_lt   "供应商提前期（天）" ""
  ask d6_inst "来料波动（大/中/小）" "中"

  h2 "维度 7 · 组织与文化（M6 三问）"
  warn "三问全否 = 项目制精益，会反弹。"
  ask d7_who  "谁每天看改善数字？(名字/岗位)" ""
  ask d7_resp "异常发生谁被叫到现场？(名字/岗位)" ""
  ask d7_std  "改善是否写回标准作业？(是/否)" ""
  ask d7_cut  "精益是否与裁员挂钩？(是/否/未动)" "否"

  # ---------- 派生判据 ----------
  local vr="" vr_class="语料未覆盖"
  if [[ -n "$d2_lt" && -n "$d2_vat" ]] && [[ "$d2_lt" =~ ^[0-9.]+$ && "$d2_vat" =~ ^[0-9.]+$ ]]; then
    local denom; denom="$(awk -v a="$d2_vat" -v b="$d2_lt" 'BEGIN{ if (b<=0) print "0"; else printf "%.4f", (a*24)/(b*24) }')"
    vr="$denom"
    if awk -v v="$denom" 'BEGIN{exit !(v<0.05)}'; then
      vr_class="公式系数·停滞型（<5%，启发式基线，非通用阈值）"
    else
      vr_class="公式系数·非停滞型"
    fi
  fi

  local d5_verdict="未拆解"
  if [[ -n "$d5_avail" && -n "$d5_perf" && -n "$d5_qual" ]]; then
    if [[ "$d5_avail" =~ ^[0-9.]+$ && "$d5_perf" =~ ^[0-9.]+$ && "$d5_qual" =~ ^[0-9.]+$ ]]; then
      local o; o="$(awk -v a="$d5_avail" -v b="$d5_perf" -v c="$d5_qual" 'BEGIN{printf "%.2f", a*b*c/10000}')"
      d5_verdict="OEE≈${o}%（系数相乘所得，非现场实测分项）"
      if awk -v a="$d5_avail" 'BEGIN{exit !(a<85)}'; then
        d5_verdict+=" → 时间稼动率偏低 → 方向：自主保全（不是加人）"
      elif awk -v a="$d5_perf" 'BEGIN{exit !(a<95)}'; then
        d5_verdict+=" → 性能稼动率偏低 → 方向：先数据采集暴露微停，再改善"
      fi
    fi
  fi

  local sdca="未判定"
  if [[ "$d4_std" == "有" || "$d4_std" == "部分" ]]; then
    if [[ "$d4_exec" == "否" ]]; then
      sdca="**维持问题（SDCA 失败）** → 先日常管理/带教，**不要上六西格玛大项目**"
    elif [[ "$d4_exec" == "部分" ]]; then
      sdca="**维持与改善并存** → 先把执行率拉满，再谈改善"
    elif [[ "$d4_exec" == "是" ]]; then
      sdca="**进入改善问题（PDCA）** → 标准已执行，可上改善工具"
    fi
  elif [[ "$d4_std" == "无" ]]; then
    sdca="**无标准** → 先建标准（标准作业/点检），改善资格尚未具备"
  fi

  local m6="未判定"
  if [[ -n "$d7_who" && -n "$d7_resp" && -n "$d7_std" ]]; then
    if [[ "$d7_who" == "未记录" || "$d7_resp" == "未记录" || "$d7_std" == "否" ]]; then
      m6="**项目制风险** → 三问未全过，改善极可能反弹。优先补固化机制，不是继续堆工具。"
    else
      m6="机制在跑 → 持续改进具备土壤"
    fi
  fi
  if [[ "$d7_cut" == "是" ]]; then
    m6+=" ⚠️ **精益与裁员挂钩是改善文化的死亡信号**（实证研究已在印度汽车业观察到后续无人敢提提案）"
  fi

  local pull="未判定"
  if [[ -n "$d6_otd" ]] && [[ "$d6_otd" =~ ^[0-9.]+$ ]]; then
    if awk -v v="$d6_otd" 'BEGIN{exit !(v<95)}'; then
      pull="供应商准时率 <95% → **拉动前提不成立**，此时上内部看板无效，应先治供应链"
    else
      pull="供应商基本可信赖 → 拉动/看板前提成立"
    fi
  fi

  local smed="未判定"
  if [[ -n "$d5_smr" ]] && [[ "$d5_smr" =~ ^[0-9.]+$ ]]; then
    if awk -v v="$d5_smr" 'BEGIN{exit !(v>30)}'; then
      smed="换型占比 >30%（启发式基线）→ **上 SMED，不是上线平衡**（换型会打碎平衡）"
    else
      smed="换型占比不高 → 线平衡/标准作业优先"
    fi
  fi

  # ---------- 输出 ----------
  h1 "派生判据（公式与口径，非现场结论）"
  printf '  %-22s %s [%s]\n' "增值比" "${vr:-未取数}" "$vr_class"
  printf '  %-22s %s\n' "OEE 判读" "$d5_verdict"
  printf '  %-22s %s\n' "SDCA/PDCA" "$sdca"
  printf '  %-22s %s\n' "换型优先" "$smed"
  printf '  %-22s %s\n' "拉动前提" "$pull"
  printf '  %-22s %s\n' "可持续性(M6)" "$m6"
  echo
  dim "$NUMCLASS_HINT"
  dim "启发式基线（增值比<5%、换型>30%、准时率<95%）须以本厂实测校准，非通用阈值。"

  # ---------- 报告 ----------
  local REPORT="agentic-protocol-$(TODAY).md"
  mdbuf_reset
  mdbuf_add "# 精益诊断取数单（Agentic Protocol）"
  mdbuf_add ""
  mdbuf_add "- 日期：$(TODAY)"
  mdbuf_add "- 来源：lean-production-expert v2.0 · cli/protocol/agentic.sh"
  mdbuf_add ""
  mdbuf_add "## 派生判据"
  mdbuf_add ""
  mdbuf_add "| 项 | 值 | 口径 |"
  mdbuf_add "|---|---|---|"
  mdbuf_add "| 增值比 | ${vr:-未取数} | ${vr_class} |"
  mdbuf_add "| OEE 判读 | ${d5_verdict} | 公式系数 |"
  mdbuf_add "| SDCA/PDCA | ${sdca} | 推断 |"
  mdbuf_add "| 换型优先 | ${smed} | 推断（启发式基线） |"
  mdbuf_add "| 拉动前提 | ${pull} | 推断 |"
  mdbuf_add "| 可持续性 | ${m6} | 推断 |"
  mdbuf_add ""
  mdbuf_add "## 原始输入"
  mdbuf_add ""
  for kv in \
    "d1_qty:客户日需求:${d1_qty}" "d1_var:需求波动:${d1_var}" "d1_spec:客户特殊要求:${d1_spec}" \
    "d2_lt:前置时间(天):${d2_lt}" "d2_vat:增值时间(小时/天):${d2_vat}" "d2_wip:在制品(一手):${d2_wip}" \
    "d2_plt:情报前置(天):${d2_plt}" \
    "d3_top1:最大停滞段:${d3_top1}" "d3_w1:停滞天数:${d3_w1}" "d3_c1:停滞金额:${d3_c1}" "d3_mura:波动来源:${d3_mura}" \
    "d4_std:标准存在:${d4_std}" "d4_exec:标准执行:${d4_exec}" "d4_last:标准更新:${d4_last}" "d4_chk:点检真实:${d4_chk}" \
    "d5_oee:OEE(%):${d5_oee}" "d5_avail:时间稼动(%):${d5_avail}" "d5_perf:性能稼动(%):${d5_perf}" \
    "d5_qual:良品率(%):${d5_qual}" "d5_sm:换型(分钟):${d5_sm}" "d5_smr:换型占比(%):${d5_smr}" "d5_bn:瓶颈:${d5_bn}" \
    "d6_otd:供应商准时率(%):${d6_otd}" "d6_lt:供应商提前期(天):${d6_lt}" "d6_inst:来料波动:${d6_inst}" \
    "d7_who:谁看数字:${d7_who}" "d7_resp:异常谁响应:${d7_resp}" "d7_std:写回标准:${d7_std}" "d7_cut:与裁员挂钩:${d7_cut}" ; do
    local k="${kv%%:*}" rest="${kv#*:}" lbl="${rest%%:*}" val="${rest#*:}"
    mdbuf_add "| ${lbl} | ${val} | 未分类 |"
  done
  mdbuf_add ""
  mdbuf_add "## 诚实边界"
  mdbuf_add ""
  mdbuf_add "- 本单所有数字为**用户输入**，未经交叉验证。"
  mdbuf_add "- 增值比/换型占比等判据为**启发式基线**，须以本厂实测校准。"
  mdbuf_add "- 若维度 2/5 的数字来自报表而非实地计数，结论应降级为待验证。"

  if [[ "$MODE" == "json" ]]; then
    printf '{"date":"%s","value_added_ratio":"%s","vr_class":"%s","oee":"%s","sdca":"%s","smed":"%s","pull":"%s","sustainability":"%s"}\n' \
      "$(TODAY)" "$(jnum "$vr")" "$(jesc "$vr_class")" "$(jesc "$d5_verdict")" \
      "$(jesc "$sdca")" "$(jesc "$smed")" "$(jesc "$pull")" "$(jesc "$m6")"
    return
  fi

  h1 "报告"
  printf '%s' "$MD_BUF"
  echo
  if [[ "$MODE" == "dry-run" ]]; then
    dim "[dry-run] 未写文件。去掉 --dry-run 可生成 ${REPORT}"
  else
    mdbuf_write "$REPORT"
  fi
}

case "${1:-}" in
  --help|-h)    usage ;;
  --explain)    explain ;;
  --dry-run)    MODE="dry-run"; run ;;
  --json)       MODE="json"; run ;;
  "")           run ;;
  *)err "未知参数：$1"; echo; usage; exit 1 ;;
esac
