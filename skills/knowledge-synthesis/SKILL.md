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
