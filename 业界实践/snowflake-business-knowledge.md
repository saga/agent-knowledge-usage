# Snowflake：业务知识为什么被直接做成数据库对象

研究日期：2026-10-02

## 先看结论

Snowflake 当前最值得研究的不是 Cortex Agent 本身，而是它把 Business Semantics 从 prompt 和应用代码里拿出来，做成了数据库中的一等对象。

Semantic View 是 schema-level object，可以描述 business entities、relationships、facts、dimensions、metrics、filters 等，再由 Cortex Analyst 使用这些定义生成 SQL。

官方资料：
- https://docs.snowflake.com/en/user-guide/views-semantic/overview
- https://docs.snowflake.com/en/user-guide/views-semantic/best-practices-modeling
- https://docs.snowflake.com/en/user-guide/views-semantic/yaml-spec
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst

## 1. Semantic View 到底存什么

它不是一批自然语言说明文档，而是一个业务数据模型。

~~~text
Semantic View
├── Logical Tables
├── Relationships
├── Facts
├── Dimensions
├── Metrics
├── Filters
├── Synonyms
├── Verified Queries
└── Custom Instructions
~~~

其中最重要的是三类关系：Entity、Relationship、Metric。

Customer 不是物理表名，而是业务对象。Customer 和 Order 怎么关联，不需要模型猜 join path。Revenue 不再是“找一个叫 revenue 的字段”，而是一个受治理的计算定义。

传统 RAG 更像是在告诉模型“财务文档里这么解释 revenue”。Semantic Layer 则可以进一步让系统“Revenue 就按这个表达式计算”。

所以它从文本证据进入了可执行业务语义。

## 2. 为什么 Snowflake 强调从业务角度建模

Snowflake 当前 modeling guidance 明确建议从业务用户视角建模，而不是按数据库结构机械暴露表；同时强调 descriptions、relationships、metrics、filters 和 verified queries。

深层问题其实是：

> Physical Schema 和 Business Model 是两个不同的 ontology。

数据库可能有：

~~~text
fct_ord
dim_cst
trx_amt
prod_cd
~~~

业务用户说的是：

~~~text
Order
Customer
Revenue
Product
~~~

如果每次都让 LLM 临时完成这次映射，准确率会很大程度依赖模型本身。Semantic View 把这份映射固定下来。

## 3. 为什么不是把所有知识都做成 Semantic View

Snowflake 自己也没有这么做。

结构化业务语义：

~~~text
Semantic View
      ↓
Cortex Analyst
      ↓
SQL
~~~

非结构化知识：

~~~text
Cortex Search
      ↓
documents / text
~~~

Cortex Agents 再把 Analyst、Search、code execution、custom tools 等能力组合起来。

这给出了一个很实用的分层：

> 结构化知识应该尽量表达为可执行语义；自然语言知识保留为可检索证据。

不要强迫两者使用同一个存储模型。

## 4. Verified Query 为什么重要

一个 Semantic Model 写得再漂亮，也可能和真实用户提问方式存在偏差。

Verified Query 提供的是：

~~~text
natural language question
+
validated SQL
~~~

它有两个作用：

一是让常见问题有一个经过验证的答案路径。

二是把真实使用反馈重新用于 semantic model 优化。

因此 Snowflake 的路线实际上形成：

~~~text
Semantic Model
   ↓
Agent
   ↓
Real Questions
   ↓
Evaluation / Verified Queries
   ↓
Semantic Model refinement
~~~

这比“建一次 semantic layer 就结束”成熟得多。

## 5. Semantic View 的边界

它强在：

- structured enterprise data；
- metric semantics；
- relational joins；
- governed SQL generation。

它不直接解决：

- 长篇研究资料；
- episodic memory；
- procedural skills；
- team experience；
- cross-system agent communication。

所以 Business Knowledge 仍然应该是更大的 umbrella。

## 6. Governance 是这套设计真正值钱的地方

Semantic View 是 Snowflake schema object，可以进入 privilege、sharing、catalog 等治理体系。

这使业务语义可以和数据治理一起管理。

对于金融场景，真正的问题不只是“模型知道定义”，还包括：

> 谁可以看到这个定义？谁可以修改？什么时候生效？谁批准？

如果语义层和数据权限完全脱离，业务定义虽然标准化了，使用它的人却可能没有相应的数据权限。

## 7. 对当前架构的启发

当前项目可以抽取一个与 Snowflake 无关的模型：

~~~text
Business Semantics
├── Entity
├── Relationship
├── Metric
├── Rule
├── Filter
├── Definition
├── Source
└── Authority
~~~

Snowflake Semantic View 只是其中一种 provider。

Common Agent Library 更适合定义 SemanticProvider，让底层适配 Snowflake、Databricks、Google 或内部 semantic service。

## 8. 一个容易犯的错误

不要做成：

~~~text
All enterprise knowledge
      ↓
one giant semantic model
~~~

Snowflake 自己的 guidance 也强调按 business domain / use case 组织，而不是把整个 enterprise warehouse 塞进一个模型。

原因很现实：

- 模型选择更困难；
- context 变大；
- debugging 更难；
- 权限范围更难管理；
- semantic conflict 更容易出现。

Semantic layer 最好是多个有清晰边界的 business context，而不是一个企业大全。

## 9. 最终判断

Snowflake 的重要变化不是“RAG 被替代”，而是：

> 对有明确业务含义的结构化知识，最可靠的方式往往不是让模型检索一段解释，而是把定义变成可治理、可执行的 semantic object。

这应该成为当前 Agent Knowledge roadmap 的主线之一。
