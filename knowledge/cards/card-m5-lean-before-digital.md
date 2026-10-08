---
id: card-m5-lean-before-digital
title: 先 lean 再 digital（M5 · 数字化是放大器）
book: master-skill 六轨蒸馏 · 认知层
layer: cognitive
tags: [心智模型, MES, 数字化, IIoT, 先lean再digital]
confidence: high
verifiable: true
verified: false
falsifiable_claim: "在流程未简化的前提下部署 MES/IIoT，只会把既有混乱系统化并抬高后续改动成本，不会创造流动；因此数字化必须排在流程改善之后（感知/预测类场景除外）。"
limitations: "预测性维护、基于大数据的质量预测等「感知/预测类」场景需要先有数据采集能力，可与流程改善并行，不必等流程改完。"
related_cards: [card-lean-digital-fusion, card-m3-jidoka-human-judgment]
related_skills: [digital-it, lean-system, jit]
---

# 先lean 再 digital（M5 · 数字化是放大器）
## 定义
数字化/自动化是**放大器**，不是发动机。它放大既有流程的好坏——**流程是错的，数字化就是把垃圾流程高效地固化下来**。

这行对MES / IIoT / AI 的态度是明确的不神化：数字化能暴露微停、能实时呈现在制、能自动采集数据，但它**不创造流动**。

**顺序不可反：先手工 kaizen 消除浪费/不均衡/超负荷，再让系统固化放大。** 流程未简化就上 MES = garbage in / garbage out，且混乱从此被"系统化"，改动成本更高。

## 判据
任何数字化立项先回答三问：
1. **这个流程已经是最简了吗？** 若否 → 先做流程改善。
2. **数据定义统一吗？** 否则系统会把不一致固化成"标准"。
3. **谁在消费这些数据？** 没有改善组织去消费数据 → 项目只是亮眼。

## 反例
- ❌ 流程混乱就上 MES → 数字化放大垃圾流程，混乱被系统化。
- ❌ 为"数字化指标"而数字化 → 指标无对应改善动作。
- ❌ 把 IIoT 当"精益替代品" → 物联网不改善流程，只暴露流程；**固化错流程更糟**。
- ❌ 先买自动化设备再谈流程 → 自动化的前提是先手工 kaizen 消除三 MU。

## 局限（何时可以并行）
这条模型在**数据驱动的发现型场景**中有边界：预测性维护、基于大数据的质量预测，恰恰需要**先有数据采集能力**才能做。
更准确的顺序是：**流程类的先 lean 再 digital；感知/预测类的可以并行。**

另注：Ballé（gemba 学派）明确警告「数字渲染不等于 gemba」——数字孪生可能重新制造"远离现场"的官僚距离，违背现地现物。

## 出处
〔`research/02-tools.md` 数字化层诚实结论：赋能层而非驱动层，先 lean 再 digital 顺序不可反〕〔Ballé 一手观点：digital rendition of the real place 不算 gemba〕

## 关联
`SKILL.md` §10.3 M5 · §10.4·`references/synthesis.md` §1 M5
`references/digital-it.md` · `references/lean-system.md`
