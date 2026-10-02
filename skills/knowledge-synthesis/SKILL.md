---
name: knowledge-synthesis
description: 把论文、厂商实践、开源实现和已有研究材料综合成 Knowledge Architecture、Roadmap、分类体系或设计原则。适用于研究结果已经足够多、需要抽象共同模式时。
metadata:
  kind: capability
---

# Knowledge Synthesis

## 目标

把大量研究材料压缩成可继续使用的模型，而不是再写一个大综述。

核心流程：

Sources
→ Facts
→ Repeated patterns
→ Boundary differences
→ Common primitives
→ Architecture model
→ Roadmap

## 第一原则：不要过早统一

只有当不同来源实际表达相似职责时才统一。

例如 Snowflake Semantic View、Databricks Metric View / Ontology、Google semantic assets，可以抽取为 Business Semantics，但不能说三者完全相同。

必须保留：
- 存储位置
- 生命周期
- 权限模型
- Agent runtime
- 平台边界

## 第二原则：区分 primitive 和 implementation

长期抽象优先考虑：

Knowledge
Entity
Relation
Metric
Rule
Skill
Memory
Evidence
Permission
Context
State

而不是直接把具体产品名当 primitive。

## 第三原则：区分职责

| Primitive | 核心问题 |
|---|---|
| Knowledge | 已知什么 |
| Semantic Layer | 这些东西是什么意思 |
| RAG / Search | 怎么找到证据 |
| Graph | 关系怎么连接 |
| Skill | 怎么完成一类任务 |
| Memory | 过去发生了什么 |
| Tool | 怎么读写外部世界 |
| State | 当前是什么状态 |
| Workflow | 允许怎么推进 |
| Policy | 什么允许做 |
| Evidence | 为什么相信 |
| Context | 当前给模型什么 |

## 第四原则：保留不确定性

允许明确写：
- 尚未统一
- 不同厂商定义不同
- 当前证据不足
- 属于本文推断
- 需要进一步验证

不要为了做出整齐模型而制造确定性。

## Roadmap 原则

Roadmap 不应只是 feature backlog。

优先表达能力成熟顺序：

Shared vocabulary
→ Knowledge foundation
→ Retrieval / evidence
→ Memory
→ Skills / procedures
→ Semantic / ontology
→ Agent runtime
→ Multi-agent / protocol
→ Evaluation / governance
→ Self-improvement

实际项目已有能力优先复用，不为了 Roadmap 强行重构。

## 输出

最好形成三个东西：
1. 一张能力模型
2. 一张当前项目映射
3. 一张下一步研究 / 实现路线

不要写几十条没有优先级的建议。

## 常见失败

不要：
- 把所有研究都塞进一个 Knowledge 类
- 把所有外部资料都叫 RAG
- 把 Agent Memory 当 Business State
- 把 Tool 当 Permission
- 把 Workflow 当全部 Control Plane
- 把厂商产品名当架构 primitive
- 因为有几个案例就宣布“业界标准”

---
## 7. Synthesis 开始前：先判断材料是否足够

Knowledge Synthesis 不是“资料多了就开始总结”。

至少确认：

- 同一主题存在多个来源；
- 来源里有可比较的 atomic claims；
- 不是所有来源都来自同一个 vendor / author；
- 核心问题已有一定覆盖；
- 已知未知项已经标记。

只有一个来源时，通常是 summary，不是 synthesis。

## 8. 第一层：Atomic Claims

每个来源先拆成一个个可以重新组合的原子 Claim：

~~~text
Source:
Claim:
Evidence:
Condition:
Limitation:
Confidence:
Source type:
~~~

一个 Claim 尽量只表达一件事。这样才能跨论文、厂商和实现进行真正比较。

## 9. 第二层：按机制聚类，不按来源组织

把 atomic claims 按问题、机制和责任聚类，而不是按公司、论文或日期排列。

Theme 应该是一个判断句，而不是一个分类名。

坏：Semantic Layer

好：企业 Agent 开始把高价值业务语义从 prompt 中外置，并交给可治理对象承载。

聚类后继续问：这些来源真的解决同一个问题吗？哪些只是名称相似？

## 10. 第三层：识别真正的共同模式

一个 pattern 至少检查：

1. 多个独立来源是否重复；
2. 是否跨产品 / 跨实现；
3. 是否只是同一基础技术的不同包装；
4. 是否存在反例；
5. pattern 的边界在哪里。

推荐记录：

~~~text
Pattern:
Supporting sources:
Independent source families:
Counter-evidence:
Applicable scope:
Not applicable:
Confidence:
~~~

不要因为很多文章都用了某个词，就认为找到了共同模式。

## 11. 第四层：找冲突

高质量 synthesis 的重要输出不是只有共识，而是解释为什么来源 A 和 B 不一样。

常见原因：definition、workload、scale、benchmark、architecture boundary、product maturity、vendor incentive。

记录：

~~~text
Tension:
Position A:
Position B:
Likely boundary:
Missing evidence:
Current judgment:
~~~

不能解释的冲突就保留 unresolved，不要平均成一句“各有优势”。

## 12. 第五层：从 Pattern 到 Primitive

不要直接把“多个厂商都有 X”变成“Common Library 必须实现 X”。

中间至少经过：

~~~text
Repeated Pattern
     ↓
Stable Responsibility
     ↓
Clear Interface
     ↓
Reusable Primitive
~~~

例如：

~~~text
不同厂商都有 business semantics
        ↓
共同责任：保存和解释业务定义
        ↓
candidate interface：SemanticDefinition
        ↓
provider-specific adapters
~~~

只有 responsibility 足够稳定时才抽 primitive，否则保持 Candidate Primitive。

## 13. Primitive 必须有边界

每个候选 primitive 使用统一卡片：

~~~text
Name:
Purpose:
Inputs:
Outputs:
Owner:
Persistence:
Discovery:
Runtime use:
Permission:
Provenance:
Freshness:
Version:
Failure mode:
Current evidence:
Known implementations:
Open questions:
~~~

这样可以避免“抽象只剩一个漂亮名字”。

## 14. 保留不同层次

当前研究特别容易混淆：

~~~text
Knowledge
Semantic Meaning
Retrieval
Evidence
Context
Memory
Skill
Tool
State
Workflow
Policy
~~~

Synthesis 必须保留这些对象的责任差异。

一张推荐的分析模型是：

~~~text
Canonical Source
      ↓
Knowledge / Semantic Objects
      ↓
Retrieval / Navigation
      ↓
Evidence
      ↓
Context
      ↓
Agent Reasoning
      ↓
Skill / Tool / Workflow
      ↓
Business State
      ↓
Evaluation / Governance
~~~

这是一张分析模型，不是声称所有系统都采用同一条 pipeline。

## 15. Pattern → Project Mapping

每个重要 pattern 最终进入：

| Pattern | Evidence | Current Project | Action | Confidence |
|---|---|---|---|---|
| Business semantics externalization | | | | |
| Evidence metadata | | | | |
| Procedural knowledge | | | | |

Action 只允许：

- Adopt
- Adapt
- Observe
- Reject

不要把所有研究发现都变成 TODO。

## 16. Roadmap 的判断顺序

不要按功能热度排序，至少检查：

### Dependency
是不是其他能力的基础？

### Governance
缺失它会不会造成权限、审计或真实性问题？

### Reuse
多个 Agent / workflow 是否需要？

### Evidence
是否已经有足够学术 / 业界证据？

### Cost
实施是否明显增加平台复杂度？

因此：

~~~text
High evidence + high reuse + low/moderate cost → early
Interesting but weak evidence → research
High complexity + weak value → defer
~~~

## 17. 必须允许暂不行动

Synthesis 不是功能 Wishlist。

研究确认某模式存在，并不意味着当前项目必须立刻实现。

允许明确写：

> 研究确认该模式存在，但当前项目暂不做。

这能防止研究结果反过来制造无休止的架构复杂度。

## 18. 三种危险过度抽象

### Product abstraction
把多个不同产品对象直接合成一个类。

### Vocabulary abstraction
仅因为名字相似就认为职责相同。

### Architecture abstraction
把不同 runtime 边界压缩成一张“统一架构图”。

如果抽象后无法回答“谁拥有、谁更新、谁授权、谁消费”，这个 abstraction 很可能还不够成熟。

## 19. Synthesis Quality Gate

发布前至少检查：

### Evidence
每个重要 pattern 有 source family 证据。

### Independence
不是同一个 vendor / benchmark 的重复引用。

### Boundary
每个 pattern 有适用范围。

### Tension
重要冲突已经记录。

### Gap
仍然不知道的地方明确写出。

### Action
Project implication 与 source fact 分开。

### Simplicity
没有为了完整而增加不必要 primitive。

## 20. 输出结构

~~~markdown
# Knowledge Synthesis

## 当前结论
## Evidence Base
## Major Patterns
## Major Differences
## Candidate Primitives
## Current Project Mapping
## Adopt / Adapt / Observe / Reject
## Open Questions
## Research Gaps
~~~

不要按 source 一个一个复述。

## 21. Synthesis 完成的判据

可以结束时：

- 主要 atomic claims 已聚类；
- 主要 patterns 已出现；
- 关键冲突已处理；
- 重要 gaps 已明确；
- Candidate primitives 已有证据基础；
- 项目映射已经明确；
- 没有为了追求整齐而抹平差异。

如果 synthesis 发现“我们其实还不知道”，正确动作是回到 Deep Research，而不是强行生成架构模型。

## 22. 本 Skill 不做什么

Knowledge Synthesis 不负责：

- 发现大量原始来源；
- 证明单个 Claim；
- 判断论文实验是否正确；
- 取代 Evidence Review；
- 直接替代系统架构设计；
- 为了 roadmap 而制造结论。

典型链路保持：

~~~text
Deep Research
   ↓
Academic / Industry Research
   ↓
Evidence & Claim Review
   ↓
Knowledge Synthesis
   ↓
Architecture / Roadmap decision
~~~