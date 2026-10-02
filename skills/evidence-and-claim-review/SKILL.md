---
name: evidence-and-claim-review
description: 审核研究报告、Roadmap 和架构分析中的事实、引用、推断、行业判断和绝对化结论。当研究结果准备进入长期文档，或用户要求检查结论是否站得住时使用。
metadata:
  kind: capability
---

# Evidence and Claim Review

## 目标

不是只检查有没有引用，而是检查：

这句话到底被什么证据支持？
证据强度和结论强度是否匹配？

## Claim 类型

逐条识别：
- Fact
- Observation
- Experiment Result
- Interpretation
- Pattern
- Recommendation
- Principle
- Absolute Claim
- Prediction

## Evidence 类型

按强度区分：
- Primary
- Strong secondary
- Secondary
- Discovery only

## 强结论检查

出现以下词时重点审查：

必须、一定、永远、绝对、唯一、只能、所有、任何、业界标准、最佳实践、普遍、都应该、不会、保证、消除、防止。

不是出现就一定错误，而要问：
1. 是否存在合理例外？
2. 来源是否足以支持这么强的表述？
3. 是否需要增加限定条件？

## 常见错误

### 官方能力不等于行业成熟度
官方文档写支持 X，不代表 X 已经成为企业标准。

### 单个案例不等于普遍经验
公司 A 成功使用 X，不代表企业都应该使用 X。

### 没找到反例不等于没有反例
最多只能写“在当前检索范围内未发现明显反例”。

### 论文结果不等于保证
必须保留数据集、模型、方法、条件、指标和 limitation。

## Agent Architecture 专项检查

默认检查这些边界：

Agent Autonomy ≠ Authorization Authority

Memory ≠ Business Truth

RAG ≠ Entitlement

Prompt ≠ Security Boundary

Observability ≠ Regulatory Audit

Workflow State ≠ Business State

Capability ≠ Permission

Tool ≠ Authorization

## 反向搜索

重要结论至少考虑：
- claim
- claim + limitation
- claim + exception
- claim + counterexample
- claim + failure

## 输出

建议生成：

| Claim | Type | Evidence | Strength | Gap | Suggested wording |
|---|---|---|---|---|---|

证据不足时直接降低表述强度。

例如：

“X 是行业标准。”

改成：

“X 是多个平台中已经出现的一种常见架构模式。”

“X 能保证安全。”

改成：

“X 可以降低某类风险，但不能单独保证安全。”

## 最终原则

研究文档的可信度来自：

准确事实 + 正确边界 + 证据可追溯 + 承认未知

不是来自引用数量。
