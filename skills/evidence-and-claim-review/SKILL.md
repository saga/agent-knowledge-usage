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

---
## 8A. 先找承重 Claim，不要平均用力

优先审核会真正改变读者判断的 Claim：

- 结论中的关键事实；
- 直接改变架构判断的事实；
- 数字 / benchmark；
- “当前 / 最新 / GA / Preview”；
- 权限 / 安全 / 合规；
- 跨厂商共同模式；
- “必须 / 最佳实践 / 行业标准”；
- 形成具体设计建议的事实。

普通背景句可以轻量检查。

## 8B. Claim、Evidence、Wording 三栏分开

审查时分别问：

~~~text
Claim：我要声称什么？
Evidence：我有什么证据？
Wording：我现在写得有多强？
~~~

例如：

~~~text
Evidence:
官方文档说明产品支持 RBAC。

过强 wording:
“产品已经解决 Agent authorization。”

合理 wording:
“产品在该对象层面提供 RBAC；这不足以单独证明整个 Agent workflow 的 authorization 已被解决。”
~~~

很多研究的问题不是事实完全错，而是 wording 超过 evidence。

## 8C. Evidence Matrix

| Claim 类型 | 合适证据 | 常见错配 |
|---|---|---|
| Product capability | 官方 docs / API | 二次博客 |
| Runtime behavior | source / tests / runtime docs | marketing page |
| Experimental result | original paper / benchmark | 新闻报道 |
| Customer adoption | customer engineering / case | vendor feature page |
| Industry pattern | 多厂商 + independent evidence | 单一 vendor |
| Best practice | 多来源 + 条件 + failure evidence | 单篇博客 |
| Security guarantee | architecture + enforcement + testing | feature list |

不是“引用越多越强”，而是证据类型必须与 Claim 类型匹配。

## 8D. 五种 Citation Failure

### Missing

Claim 没有 citation。

### Weak

有 citation，但来源不足以支撑 Claim。

### Partial

来源只支持 Claim 的一部分。

### Misplaced

citation 离 Claim 太远，无法判断到底支持哪句话。

### Stale

来源曾经支持，但对应产品 / API / 状态已经变化。

## 8E. Claim Decomposition

遇到强句，依次问：

1. 主语是谁？
2. 动词是 support、prove、cause、guarantee 还是 recommend？
3. 对象是什么？
4. 范围是什么？
5. 时间是什么？
6. 条件是什么？
7. 有没有第二个隐含 Claim？

例如：

> RAG 能让 Agent 获得企业可信知识并保证权限。

至少包含：

~~~text
RAG 可以访问外部知识
企业知识为什么可信
retrieval 是否受权限约束
RAG 本身是否提供 entitlement
~~~

通常只有第一个 Claim 能由基础 RAG 论文直接支持。

## 8F. Evidence Strength 不只是来源等级

判断三个维度：

1. Source quality；
2. Source-Claim entailment；
3. Coverage of conditions / limitations。

一个非常权威的来源，如果只支持 Claim 的一半，仍然不能支撑整句。

## 8G. Source Independence

只有来源真正独立时，才把它们当 corroboration：

- publishing entity 不同；
- 没有明显互相转载；
- 不是同一个 benchmark 的二次报道；
- 不是同一个 vendor 的重复 statement；
- 不是同一作者换平台重发。

尤其：

~~~text
Vendor docs
Vendor blog
Vendor conference talk
~~~

通常仍然是一个 vendor source family。

## 8H. 数字 Claim 单独走验证

所有重要数字检查：

- 原始出处；
- 单位；
- denominator；
- 时间范围；
- baseline；
- rounding；
- relative vs absolute change；
- 是否改变了实验条件。

确定性计算优先交给脚本。

## 8I. Freshness Gate

以下词出现时提高审核等级：

- 当前
- 最新
- 目前
- GA
- Preview
- supported
- deprecated
- recommended
- pricing

至少应该存在可以定位到日期 / 版本的来源。

## 8J. 绝对 Claim 优先缩句，而不是疯狂补链接

如果证据无法承载强结论，先降低 Claim：

> X 是行业标准。

改成：

> X 已在多个平台中出现，当前资料足以把它视为一种常见模式，但不足以证明已经形成行业标准。

## 8K. Review Severity

| Severity | 含义 | 动作 |
|---|---|---|
| Critical | 核心结论无证据、明显反证、重大安全 / 合规误导 | 必须修复 |
| High | 会改变主要结论 | 补证据或降级 Claim |
| Medium | 边界、版本、citation proximity 等问题 | 修文案 / 加限定 |
| Low | 次要格式或出处问题 | 可延后 |

不要把十个 Low 当成比一个 Critical 更严重。

## 8L. Final Verdict

只用四种状态：

- PASS
- PASS_WITH_CAVEATS
- NEEDS_REVISION
- BLOCK

状态由关键问题严重程度决定，不由 citation 数量决定。

## 8M. Gap 要能够喂给下一轮 Research

每个重要 Gap 至少记录：

~~~text
Gap ID:
Claim:
Why insufficient:
Missing evidence type:
Suggested search:
Priority:
~~~

这样 Evidence Review 可以直接成为 Deep Research 的下一轮输入。

## 8N. Agent Architecture 默认危险跳跃

审核时自动重点检查：

~~~text
Agent Autonomy       ≠ Authorization Authority
Agent Reasoning      ≠ Security Boundary
Memory               ≠ Business Truth
RAG                  ≠ Entitlement
Prompt               ≠ Authorization
Tool                 ≠ Permission
Capability           ≠ Permission
Observability        ≠ Regulatory Audit
Workflow State       ≠ Business State
Customer Case        ≠ Industry Standard
GA                   ≠ Production Maturity
Benchmark            ≠ Production Guarantee
~~~

这些不是永远成立的“真理”，而是 review 的危险跳跃警报。

## 8O. 两阶段 Review：机械闸门 → 语义审查

### Stage A — Deterministic

优先执行：

~~~bash
python3 skills/evidence-and-claim-review/scripts/audit_claims.py report.md --json
~~~

固定检查：

- Markdown links；
- citation IDs；
- duplicate source URLs；
- absolute-claim vocabulary；
- 数字附近是否缺 citation；
- current/latest/GA/Preview 是否缺日期上下文；
- 常见 architecture-boundary 风险词。

### Stage B — Semantic

由模型 / reviewer 判断：

- citation entailment；
- evidence sufficiency；
- source independence；
- counter-evidence；
- causal reasoning；
- industry-pattern 是否真的成立。

脚本不能替代 Stage B。

## 8P. Script Fail-safe

如果脚本失败：

1. 不等于研究失败；
2. 不等于检查通过；
3. 回到人工 checklist；
4. 输出标明 deterministic checks unavailable；
5. 高风险任务不得因为脚本不可用而降低证据标准。

## 9. 最小交付物

完整 Review 至少留下：

~~~text
Verdict
Top Findings
Claim Audit
Evidence Gaps
Recommended Wording
Open Questions
Deterministic Checks
~~~

Review 结果应该可以直接反馈到 research / knowledge-synthesis，而不是一次性的人工点评。
