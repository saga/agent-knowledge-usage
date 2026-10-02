# 业界实践

本目录研究 Snowflake、Databricks、Google、OpenAI、Anthropic（Claude）如何抽象、保存、检索、使用和治理业务知识 / 企业知识。

研究日期：2026-10-02。

这些文章不是产品介绍。重点是把每家厂商的产品形态还原成系统设计问题：

Knowledge 是什么？
↓
保存成什么？
↓
谁拥有它？
↓
Agent 如何发现和读取？
↓
什么时候进入 Context？
↓
权限在哪里生效？
↓
如何处理版本 / Freshness / Provenance？
↓
什么问题仍然留给应用？

## 报告

- [Snowflake：业务知识为什么被直接做成数据库对象](./snowflake-business-knowledge.md)
- [Databricks：从显式语义对象走向显式 + 推断的 Ontology](./databricks-business-knowledge.md)
- [Google：从 Data Catalog 走向 Context Engine](./google-business-knowledge.md)
- [OpenAI：把 Knowledge Access 做成 Agent Capability](./openai-business-knowledge.md)
- [Anthropic / Claude：把知识拆成 Skill、Resource、Memory 和 Context](./anthropic-claude-business-knowledge.md)

## 五家公司的差异，不只是产品不同

### 谁把 Business Semantics 当成一等对象

Snowflake、Databricks、Google 都在往这个方向走。

~~~text
Business Meaning
     ↓
Semantic Object / Ontology
     ↓
Governed Data
     ↓
Agent
~~~

区别在于：
- Snowflake：强调可执行的 Semantic View；
- Databricks：在显式语义上继续加入 inferred context；
- Google：把 semantic assets、catalog、data products 和 search 组合成更大的 context layer。

### 谁优先解决 Knowledge Access

OpenAI 更偏这一层：

~~~text
File
 ↓
Index
 ↓
Search
 ↓
Agent Tool
~~~

它提供的是通用、低耦合的 retrieval capability，而不是完整的 Business Ontology。

### 谁优先解决 Agent Capability Externalization

Anthropic 更偏：

~~~text
Skill
+
MCP
+
Memory
+
Context
~~~

它把知识按“在 Agent 里承担什么职责”拆开，而不是要求所有知识进入一个中心 Knowledge Object。

## 横向模型

| 层 | Snowflake | Databricks | Google | OpenAI | Anthropic |
|---|---|---|---|---|---|
| Business semantics | 强 | 强 | 强 | 弱 | 弱 |
| Structured metrics | 强 | 强 | 强 | 弱 | 弱 |
| Ontology / context | 中 | 强 | 强 | 弱 | 间接 |
| Unstructured retrieval | Search | Search / external sources | RAG / Agent Search | File Search | MCP / Web / app |
| Procedural knowledge | 外部实现 | 外部实现 | 外部实现 | Tool / app | Skills |
| Memory | 外部 / Agent | 外部 / Agent | 外部 / Agent | 应用或服务 | App-owned memory |
| Tool capability | Cortex Agents | Genie / tools | Agent Platform | Hosted tools / MCP | MCP |
| Governance | data-layer strong | Unity Catalog strong | catalog / IAM oriented | application-defined | application-defined |
| Portable representation | 平台对象 | 平台对象 | 平台资产 | hosted resources | filesystem / MCP |

这张表不表示能力高低，只表示每家的主要抽象落在哪一层。

## 真正共同的架构

把产品名去掉后，五家的路线可以拼成：

~~~text
Canonical Source
       ↓
Semantic Meaning
       ↓
Entities / Relations / Metrics / Rules
       ↓
Retrieval Views
       ↓
Context Assembly
       ↓
Agent
       ↓
Tools / Actions
~~~

旁边还要有：

~~~text
Authority
Permission
Version
Freshness
Provenance
Evaluation
Audit
~~~

这比“Knowledge = Vector Store”更接近企业 Agent 的真实形态。

## 一个重要的共同点：Knowledge 和 Context 开始分开

五家路线虽然做法不同，但都越来越接近：

~~~text
Long-lived knowledge
        ↓
selection / retrieval / policy
        ↓
current context
        ↓
reasoning
~~~

知识库很大没有问题。真正需要控制的是：

> 这一轮为什么把这几条知识交给模型？

这正是 Context Engineering、Evidence、Authority、Permission 开始进入 Knowledge Architecture 的原因。

## 一个重要的共同点：Business Semantics 和 Retrieval 不是一层

结构化业务定义更适合 Entity、Metric、Relationship、Rule、Filter。

自然语言资料更适合 Document、Section、Proposition、Evidence。

因此实际系统更可能是：

~~~text
Semantic Layer
+
Knowledge Corpus
+
Graph / Relationship Index
+
Retrieval
+
Memory
+
Context Assembly
~~~

而不是寻找一个万能存储。

## 一个重要的共同点：自动发现开始成为下一阶段

Databricks 的 inferred context、Google 的 enrichment、LLM Wiki 类研究都在指向同一个问题：

> 如果所有业务知识都要求人手工维护，系统永远无法覆盖完整企业。

但自动抽取又不能直接成为真相。

更稳妥的流程应该是：

~~~text
Source
  ↓
Candidate Knowledge
  ↓
Extract / Infer
  ↓
Validate
  ↓
Assign Authority
  ↓
Publish
  ↓
Retrieve
~~~

所以 Knowledge Engineering 的下一阶段不是“全自动生成知识库”，而是：

> 自动发现 + 人工/系统验证 + 明确 authority。

## 对当前项目最重要的结论

Common Agent Library 不应该复制某一家公司的产品对象。

更值得统一的是这些 primitive：

~~~text
KnowledgeAsset
Definition
Entity
Relation
Metric
Rule
Claim / Proposition
Evidence
Memory
Skill
Capability
Permission
Authority
Context
State
~~~

底层可以接 Snowflake、Databricks、Google、OpenAI、Postgres、Graph、MCP 等不同 provider。

最终要解决的问题不是“我们选哪一个 Knowledge Product？”，而是：

> 不同知识资产怎样在不丢失语义、权限、来源和生命周期的前提下，被同一个 Agent Runtime 可靠消费？
