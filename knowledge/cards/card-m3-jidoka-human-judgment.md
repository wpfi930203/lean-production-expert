---
id: card-m3-jidoka-human-judgment
title: 自働化 = 人的判断权，不是自动化（M3）
book: master-skill 六轨蒸馏 · 认知层
layer: cognitive
tags: [心智模型, 自働化, 安灯, 防错, 术语陷阱]
confidence: high
verifiable: true
verified: false
falsifiable_claim: "若一条产线的设备能在异常时自动停机但停机后无人响应、异常重复发生，则该产线并未实现自働化——自働化的完整形态必须同时具备停线授权、响应时限与根因闭环。"
limitations: "高变异工艺（键合、塑封等窄工艺窗口工序）若缺少快速响应配套，自动停机会退化为噪音源，出现「停得越多越乱」。"
related_cards: [card-jidoka-stop-on-abnormal, card-lean-digital-fusion]
related_skills: [jidoka, quality-management]
---

# 自働化 = 人的判断权，不是自动化（M3）
## 定义
自働化（jidoka）带「**人**」字旁。丰田官方英文表述是 **automation with a human touch** —— 关键在 human touch。

- **自动化（automation）**：机器替人动，**不会判断好坏**。
- **自働化（jidoka）**：人或机**判断出异常就主动停下**，不让不良流到下一工序。

停下来的动作本身不产生价值，它的价值是**把问题从"被稀释"变成"被暴露"**。这解释了为什么丰田愿意频繁停线：**停机成本远低于不良流到下游的成本**。

## 判据
自働化的完整形态 = 三件事，缺一即退化：

1. **停线授权** —— 含「人可主动停」，不只是设备自动停
2. **响应时限** —— 停了多久、谁来、按什么节奏（丰田 FPS 规则）
3. **根因闭环** —— 5Why 追到底，防止换件再发

## 反例
- ❌ **把自働化当自动化/无声东** → "上了自动化设备"不等于自働化。
- ❌ 只装自动停机不给人停线权 → 自働化是"人+机"，不是纯机。
- ❌ 停了线没人响应 → 「停而不改」，停机成本付出但问题回流，变成"停得越多越乱"。
- ❌ 产量 KPI 压过异常响应 → 异常本该停，产量考核让它不敢停。

## 局限（何时失效）
高变异工艺（功率半导体的键合/塑封等窄窗口工序）偶发异常多，若没有对应的快速响应机制，"自动停机"会频繁触发却无人有效处理，退化成生产噪音。

## 出处
〔Toyota 官网 TPS 页对 jidoka 的定义：异常时自动停止〕〔`research/06-glossary.md` A 节「自働化≠自动化」专章〕〔中国机械工程学会的专业澄清〕

## 关联
`SKILL.md` §10.3 M3 · §10.8 术语表 · `references/research/06-glossary.md` A 节
`references/synthesis.md` §1 M3
