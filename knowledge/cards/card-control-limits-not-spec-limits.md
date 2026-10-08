---
id: card-control-limits-not-spec-limits
title: 管制界限 ≠ 规格界限
book: 精益工具包
tags: [管制图, SPC, 异常判定]
confidence: high
verifiable: true
verified: false
falsifiable_claim: "以规格界限（USL/LSL）替代管制界限（CL±3σ）判读管制图，会漏判大量制程异常，因为管制界限由制程自身波动决定而非由客户规格决定。"
related_skills: [qc-seven-tools-old, quality-management]
---

# 管制界限 ≠ 规格界限
## 定义
- **管制界限**：由制程自身数据计算（CL ± 3σ），代表制程**实际能力**的波动范围。
- **规格界限**：由客户/设计要求给出（USL/LSL），代表**要求**。

## 判据
- X̄-R 图用 CL / UCL / LCL 公式与 **A2 / D3 / D4 / d2** 系数表（语料示例：n=4 时 A2=0.729、D4=2.282、D3=0、d2=2.059）。
- 判稳：25 点 / 35 点 / 100 点溢出条件。
- 判异：连续 7-8 点同侧、3 点中 2 点接近界限、连续 6 点趋势、过于集中 1.5σ 等（语料给出 11 条判异法则 (a)-(k) + 检定规则 1-6）。
- 制程能力用 Ca / Cp / Cpk（双套等级表）判读，与管制图是**两件事**。

## 反例
- 把 USL/LSL 画到管制图上当界限 → 大量异常被漏判。
- 缩减每组样本数（如 n=4 改成 n=2）而不换系数表 → 界限错误。

## 缺口
X̄–S 的 A3/B3/B4、X̃–R 的 m3 完整系数表语料仅有部分数值。

## 出处
〔QC七大手法\108QC品质七手法工具\控制图\管制图.ppt〕〔QC工具PPT及文档资料\01.品管七大手法〕〔SPC表格_01〕

## 关联
`references/qc-seven-tools-old.md` §3.7、§4
