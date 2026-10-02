---
name: industry-practice-research
description: 研究 Snowflake、Databricks、Google、OpenAI、Anthropic 及其他厂商如何抽象、保存、检索、使用和治理企业业务知识与 Agent Knowledge。当用户要求业界实践、大厂怎么做或厂商对比时使用。
metadata:
  kind: capability
---

# Industry Practice Research

## 目标

不要只比较产品 feature，而要回答：

Knowledge 是什么？
怎么表示？
保存在哪里？
谁拥有它？
Agent 怎么获取？
什么时候进入 context？
权限在哪里检查？
怎么保证 freshness 和 provenance？

## 研究对象

优先：
- Snowflake
- Databricks
- Google Cloud
- OpenAI
- Anthropic

需要时增加其他有明确 enterprise knowledge / agent architecture 的公司。

## 每家公司统一拆成七个问题

### 1. Abstraction
业务知识被抽象成什么？
例如 semantic view、metric、ontology、entity、relationship、document、vector store、skill、memory。

### 2. Representation
实际保存成什么？
例如 database object、YAML / JSON、graph、vector index、filesystem、metadata、external application storage。

### 3. Retrieval / Access
Agent 如何获得？
例如 Search、RAG、SQL generation、Graph traversal、Tool、MCP、File Search。

### 4. Runtime Use
什么时候进入 Agent？
例如 prompt construction、tool call、retrieval result、context assembly、planning、workflow step。

### 5. Governance
检查：
- permission
- entitlement
- policy
- certification
- audit
- tenancy

### 6. Freshness / Provenance
检查：
- source
- lineage
- updated time
- version
- verification
- authority

### 7. Limitations
明确：
- 没解决什么
- 强依赖什么平台
- 哪些能力仍需要外部系统
- 哪些结论只是产品定位而不是成熟度证明

## 证据纪律

优先使用官方 docs、官方技术博客、官方 architecture / API docs、官方 source code。

新闻和普通博客主要用于发现线索。

## 横向比较

最终不要做“最佳厂商”排名。

使用统一维度：

| Dimension | Vendor A | Vendor B | Vendor C |
|---|---|---|---|
| Business semantics | | | |
| Structured knowledge | | | |
| Unstructured knowledge | | | |
| Retrieval | | | |
| Memory | | | |
| Skills | | | |
| Governance | | | |
| Provenance | | | |
| Agent runtime | | | |

## 最重要的输出

最后回答：

不同产品背后的共同抽象是什么？

例如可能抽取出：
Canonical Source
Semantic Meaning
Entity / Relation
Retrieval View
Procedure / Skill
Memory
Provenance
Permission
Runtime Context

这些是研究结论，不要伪装成某一家厂商的原话。
