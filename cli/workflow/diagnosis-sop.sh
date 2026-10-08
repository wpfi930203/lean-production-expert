#!/usr/bin/env bash
# diagnosis-sop.sh — 五阶段诊断 SOP 走查 + 失败模式自检
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/../lib/common.sh"

MODE="interactive"

usage() {
  cat <<'EOT'
用法: diagnosis-sop.sh [--help] [--explain] [--dry-run] [--json]

按五阶段主线走查精益改善，并对照 18 条失败模式自检。

主线: 价值流识别 → 浪费分析 → 改善方案 → 标准化 → 持续改进
核心: 每阶段的「完成判据」——资深人与入门者的差别就在这里。

解决什么问题:
  诊断做完了没人看、诊断对了没执行、改善做了又反弹。
  本脚本在每个阶段卡"完成判据"，并在最后做失败模式自检。

选项:
  --help     显示本帮助
  --explain  打印五阶段完成判据与 18 条失败模式（教学模式）
  --dry-run  走完不写文件
  --json     JSON 输出
EOT
}

explain() {
  cat <<'EOT'
【五阶段完成判据 —— 怎么知道这步算做完了】

1价值流识别
   ✓ 已选定**单一产品族**（一次只画一个族，否则是没人看得懂的接线图）
   ✓ 客户/供应商边界清晰
   ✓ **亲手走线**收集 CT / 在制品 / 换型 / 稼动率 / 信息流（不是报表）
   ✓ 画出**未来状态图**并标注改善爆发点
   ✓ 有**端到端**价值流负责人（对全流程负责，非只对部门）
   ⚠ 只有当前状态图 = **墙纸**。当前图 + 未来图 + 改善计划，三者缺一不可。

2 浪费分析
   ✓ 每项等待/库存已折算到**天**与**元**（不是贴"七大浪费"标签）
   ✓ 用 3M（Muda/Mura/Muri）判断上游成因
   ✓ 区分"真浪费"与"条件型浪费"（必要的缓冲不是浪费）
   ✓ 至少识别出一个瓶颈/约束点

3 改善方案
   ✓ 高优浪费均有对策，且标"消除/减少/转移"三层
   ✓ 明确**改善幅度上限**（由瓶颈决定，非瓶颈改善对总产出无贡献）
   ✓ **先试点后推广**

4 标准化
   ✓ 执行者**参与**制定标准（不是工程师单方面发SOP）
   ✓ 有日常巡检与异常回流修订机制
   ✓ 改善已**回写**标准作业

5 持续改进
   ✓ 日常管理机制在跑
   ✓ 异常能触发根因解决（不是只换件再发）
   ✓ 改善已成日常而非项目（**资深者没有"结项"这个概念**）

【入门 vs 资深：资深者跳过了什么】

跳过            为什么跳过                    跳过风险              对冲
全员大启动会    直接去现场更有效              沟通缺失致执行阻力    轻量对齐 + 亲手走线
画完整精美 VSM  先粗诊断动手                  —                    —
长浪费清单      直奔钱与天 + 瓶颈            —                    —
凭空出方案      数据不足时**拒绝**出方案      —                    先补数据
自上而下发SOP   执行者定标准                  沟通缺失              —
"结项"概念      只有日常                      成果无处沉淀          —

【18 条失败模式（Top 8）】

1VSM 画完没人看（诊断成文档工程）
   → 一周内用它做决策，否则消耗团队耐心
2 诊断正确但没执行（诊断≠执行，断了）
   → 诊断人与改善人必须是同一个人
3 **改善做了但反弹**（最致命）
   → 无 SDCA 固化。一旦发生，其他改善都推不动，团队不再相信改善
4 只改善显眼工序，瓶颈没动
   → 没先找瓶颈，投入白费（TOC 先行）
5 把"人"的问题当"标准"的问题
   → 技能不足与标准缺失是两种病，先问"标准有吗且被执行吗"
6 用改善代替维持
   → 该修标准却做了项目（SDCA vs PDCA 混淆）
7 诊断期太长
   → 三个月诊断、产线零变化，团队失去信心。设短周期，先打一个快赢
8 精益被用作裁员工具
   → 改善完即裁员 → **改善文化死亡**，此后无人敢提提案
   （实证研究已在印度汽车业观察到）

其余 10 条见 research/03-workflows.md §C。

【实证边界 —— 引用"精益有效"前必须知道】

· 精益与**运营**绩效正相关，但与**财务**绩效弱相关甚至不显著
  （JIT→财务 r≈0.23 且不显著）
· Belekoukias 等 (2014)：**JIT 与自働化效应最强，
  而 Kaizen / TPM / VSM 效应偏低甚至对运营结果呈负向**
· 精益实施失败率常被估 **60%–90%**；连原丰田工程师 Roser 也认同
  "70%–90% 的精益项目未带来可衡量收益"
· 精益常只在**短期**改善运营，因组织无法维持而回退

结论：把精益当"项目"做，大概率失败且反弹；当作"日常管理系统的重构"做，
才可能持续。**本脚本的用途就是检查你做的是哪一种。**

来源: research/03-workflows.md §A、§C、§0
EOT
}

run() {
  h1 "精益改善五阶段走查"
  dim "每个阶段卡「完成判据」。判据不全通过 = 这步还没做完。"

  local stage_status=""

  # --- 阶段 1 ---
  h2 "阶段 1 · 价值流识别"
  ask s1_family "已选定**单一产品族**？(是/否)" ""
  ask s1_bound  "客户/供应商边界清晰？(是/否)" ""
  ask s1_walk   "是否**亲手走线**收数（非报表）？(是/否)" ""
  ask s1_future "画出**未来状态图**并标改善爆发点？(是/否)" ""
  ask s1_owner  "有端到端价值流负责人？(是/否)" ""
  local s1_ok=0
  for v in "$s1_family" "$s1_bound" "$s1_walk" "$s1_future" "$s1_owner"; do
    [[ "$v" == "是" ]] && s1_ok=$((s1_ok+1))
  done
  stage_status+="阶段1 价值流识别：${s1_ok}/5"$'\n'
  if [[ "$s1_ok" -lt 3 ]]; then
    err "阶段 1 判据严重不足 → 诊断基础不牢，后面全白做"
    [[ "$s1_future" == "否" ]] && warn "只有当前状态图 = **墙纸**。当前图+未来图+改善计划三者缺一不可。"
  else
    ok "阶段 1 通过（${s1_ok}/5）"
  fi
  echo

  # --- 阶段 2 ---
  h2 "阶段 2 · 浪费分析"
  ask s2_money "每项等待/库存已折算到**天**与**元**？(是/否)" ""
  ask s2_3m     "用 3M 判断了上游成因（不均/超负荷）？(是/否)" ""
  ask s2_cond   "区分了'真浪费'与'条件型浪费'？(是/否)" ""
  ask s2_bn     "已识别瓶颈/约束点？(是/否)" ""
  local s2_ok=0
  for v in "$s2_money" "$s2_3m" "$s2_cond" "$s2_bn"; do
    [[ "$v" == "是" ]] && s2_ok=$((s2_ok+1))
  done
  stage_status+="阶段2 浪费分析：${s2_ok}/4"$'\n'
  if [[ "$s2_ok" -lt 3 ]]; then
    warn "阶段 2 判据不足 → 只贴'七大浪费'标签而不折算，无法决策"
  else
    ok "阶段 2 通过（${s2_ok}/4）"
  fi
  echo

  # --- 阶段 3 ---
  h2 "阶段 3 · 改善方案"
  ask s3_three "对策标了'消除/减少/转移'三层？(是/否)" ""
  ask s3_limit  "明确了改善幅度上限（由瓶颈决定）？(是/否)" ""
  ask s3_pilot  "**先试点后推广**？(是/否)" ""
  local s3_ok=0
  for v in "$s3_three" "$s3_limit" "$s3_pilot"; do
    [[ "$v" == "是" ]] && s3_ok=$((s3_ok+1))
  done
  stage_status+="阶段3 改善方案：${s3_ok}/3"$'\n'
  [[ "$s3_ok" -lt 2 ]] && warn "阶段 3 判据不足 → 注意上限由瓶颈决定，非瓶颈改善对总产出无贡献"
  [[ "$s3_ok" -ge 2 ]] && ok "阶段 3 通过（${s3_ok}/3）"
  echo

  # --- 阶段 4 ---
  h2 "阶段 4 · 标准化"
  ask s4_partic "执行者**参与**制定标准？(是/否)" ""
  ask s4_daily  "有日常巡检与异常回流修订？(是/否)" ""
  ask s4_write  "改善已**回写**标准作业？(是/否)" ""
  local s4_ok=0
  for v in "$s4_partic" "$s4_daily" "$s4_write"; do
    [[ "$v" == "是" ]] && s4_ok=$((s4_ok+1))
  done
  stage_status+="阶段4 标准化：${s4_ok}/3"$'\n'
  if [[ "$s4_ok" -lt 2 ]]; then
    err "阶段 4 判据不足 → **改善做了会反弹**（最致命的一条）"
    warn "SDCA 先行：没有标准就没有改善的资格。"
  else
    ok "阶段 4 通过（${s4_ok}/3）"
  fi
  echo

  # --- 阶段 5 ---
  h2 "阶段 5 · 持续改进"
  ask s5_mech  "日常管理机制在跑？(是/否)" ""
  ask s5_root  "异常能触发根因解决（不是只换件再发）？(是/否)" ""
  ask s5_routine "改善已成日常而非项目？(是/否)" ""
  local s5_ok=0
  for v in "$s5_mech" "$s5_root" "$s5_routine"; do
    [[ "$v" == "是" ]] && s5_ok=$((s5_ok+1))
  done
  stage_status+="阶段5 持续改进：${s5_ok}/3"$'\n'
  [[ "$s5_ok" -lt 2 ]] && warn "阶段 5 判据不足 → 警惕项目制精益（失败率 60%–90%）"
  [[ "$s5_ok" -ge 2 ]] && ok "阶段 5 通过（${s5_ok}/3）"
  echo

  # --- 失败模式自检 ---
  h1 "18 条失败模式自检"
  dim "以下 8 条为最高频。详见 research/03-workflows.md §C"
  cat <<'EOT'
  1 VSM 画完没人看（诊断成文档工程）
  2 诊断正确但没执行（诊断≠执行，断了）
  3 改善做了但反弹（无固化）← 最致命，一旦发生其他改善都推不动
  4 只改善显眼工序，瓶颈没动
  5 把"人"的问题当"标准"的问题
  6 用改善代替维持（该修标准却做项目）
  7 诊断期太长（产线零变化，团队失信心）
  8 精益被用作裁员工具（改善文化死亡）
EOT
  echo
  ask f3 "你的改善**做了会反弹吗**？(是/否)" ""
  ask f8 "精益改善是否与裁员挂钩？(是/否)" ""
  ask f4 "是否只改善了显眼工序而瓶颈未动？(是/否)" ""
  ask f2 "诊断与执行是同一支团队吗？(是/否)" ""

  local fm_risk=0 fm_notes=""
  [[ "$f3" == "是" ]] && { fm_risk=1; fm_notes+="  ✗ **改善做了会反弹**——无 SDCA 固化。这是最高频也最致命的失败模式\n"; }
  [[ "$f8" == "是" ]] && { fm_risk=1; fm_notes+="  ✗ **精益与裁员挂钩**——改善文化将死亡，此后无人敢提提案（印度汽车业实证）\n"; }
  [[ "$f4" == "是" ]] && { fm_risk=1; fm_notes+="  ✗ **只改善显眼工序，瓶颈未动**——总产出没变，投入白费\n"; }
  [[ "$f2" == "否" ]] && { fm_risk=1; fm_notes+="  ✗ **诊断与执行分离**——诊断公信力归零，改善无人 own\n"; }

  h1 "走查结论"
  printf '%b' "$stage_status"
  echo
  if [[ "$fm_risk" == "0" ]]; then
    ok "未命中Top 8 失败模式"
  else
    err "命中失败模式："
    printf '%b' "$fm_notes"
  fi
  echo
  dim "$NUMCLASS_HINT"
  warn "实证提醒：精益实施失败率常被估 60%–90%；JIT 与自働化效应最强，"
  warn "而 Kaizen / TPM / VSM 工具效应偏低甚至为负（Belekoukias et al. 2014）。"
  warn "本脚本降低项目制风险，但不承诺改善率。"

  local REPORT="diagnosis-sop-$(TODAY).md"
  mdbuf_reset
  mdbuf_add "# 精益改善五阶段走查"
  mdbuf_add ""
  mdbuf_add "- 日期：$(TODAY)"
  mdbuf_add "- 来源：lean-production-expert v2.0 · cli/workflow/diagnosis-sop.sh"
  mdbuf_add ""
  mdbuf_add "## 完成判据"
  mdbuf_add ""
  mdbuf_add '```'
  mdbuf_add "$stage_status"
  mdbuf_add '```'
  mdbuf_add ""
  mdbuf_add "## 失败模式自检"
  mdbuf_add ""
  mdbuf_add "- 是否命中 Top 8：$([[ "$fm_risk" == "0" ]] && echo 否 || echo **是**)"
  if [[ "$fm_risk" != "0" ]]; then
    mdbuf_add ""
    mdbuf_add '```'
    mdbuf_add "$(printf '%b' "$fm_notes")"
    mdbuf_add '```'
  fi
  mdbuf_add ""
  mdbuf_add "## 诚实边界"
  mdbuf_add ""
  mdbuf_add "- 本走查基于用户自述，非现场核实。"
  mdbuf_add "- 完成判据来自 research/03-workflows.md §A 的方法论，非现场标准。"
  mdbuf_add "- **不承诺改善率**。精益实施失败率常被估 60%–90%（含原丰田工程师 Roser 的认同区间）。"
  mdbuf_add "- 诊断工厂必须实地走线；本脚本是提问框架，不是结论来源。"

  if [[ "$MODE" == "json" ]]; then
    printf '{"date":"%s","stage1":"%s/5","stage2":"%s/4","stage3":"%s/3","stage4":"%s/3","stage5":"%s/3","failure_mode_risk":"%s"}\n' \
      "$(TODAY)" "$s1_ok" "$s2_ok" "$s3_ok" "$s4_ok" "$s5_ok" \
      "$([[ "$fm_risk" == "0" ]] && echo false || echo true)"
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
