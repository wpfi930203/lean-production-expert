---
id: card-m1-time-over-capacity
title: 时间优先于产能（M1）
book: master-skill 六轨蒸馏 · 认知层
layer: cognitive
tags: [心智模型, 交期, 增值比, VSM]
confidence: high
verifiable: true
verified: false
falsifiable_claim: "同一产线在加工时间不变的前提下，压缩前置时间中的停滞段即可缩短交期；若改善后交期未变，则该改善不成立。"
limitations: "研发周期极长、定制化极高的场景（如试制线、小批量研发），流动价值下降，瓶颈常在知识获取与决策等待而非物流队列，须改用研发管理/项目管理框架。"
related_cards: [card-stagnation-is-waste, card-m2-pull-not-push]
related_skills: [lean-system, jit, supply-chain]
---

# 时间优先于产能（M1）
## 定义
精益所有诊断的落点是**时间**，不是产能、成本、士气。大野耐一的思考单位是「动作」与「秒」；沃麦克看 lead time；今井正明问"改善有没有让交付更短"——三个背景完全不同的人，落在同一个度量上。

## 判据
- **增值比 = 增值作业时间 ÷ 前置时间 L/T**。离散制造常 <5%（启发式基线，非通用阈值）。
- 增值比低 → 问题在**停滞**不在加工 → 上VSM，不该先买设备。
- 增值比正常但各工序 C/T > T/T → 问题在**做不快** → 才谈 SMED / 线平衡。
- 资深者一句话定位："前置 12 天、加工不到 1 小时——机会在队列不在机器。"

## 反例
- ❌ 老板说"产能不足"就扩产→ 若增值比低，买了设备更浪费。
- ❌ 以"设备很忙"证明效率高 → 忙可能是在搬运、等待、返工。
- ❌ 只看加工时间（MCT）不看停滞 → 误判问题所在。

## 局限（何时失效）
研发周期极长/ 定制化极高的场景（试制车间、小批量研发线），"流动"的价值下降，此时瓶颈常在**知识获取与决策等待**，而非物流队列——须换用研发管理或项目管理框架。

## 出处
〔Toyota 官网 TPS 页：Takt 定义为"产品被卖出的节奏"〕〔LEI《Lean Thinking》五大原则：flow 先于 pull〕〔`research/03-workflows.md` §A2〕

## 关联
`SKILL.md` §10.3 M1 · §10.4 P4 · `references/research/03-workflows.md` §A2
`references/synthesis.md` §1 M1
