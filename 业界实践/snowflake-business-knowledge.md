# Snowflake：业务知识抽象、保存与 Agent 使用

研究日期：2026-10-02

## 1. 核心路线

Snowflake 的方向非常清晰：把业务知识直接建模在 Snowflake 数据层，而不是只把业务语义写进 prompt。

当前核心对象是 **Semantic View**。Snowflake 文档明确将 Semantic View 定义为 schema-level object，可以在数据库中直接保存 business concepts、business metrics、business entities 及其 relationships。Cortex Analyst 使用这些语义生成针对物理表的 SQL。

- https://docs.snowflake.com/en/user-guide/views-semantic/overview
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- https://docs.snowflake.com/en/user-guide/views-semantic/best-practices-modeling

## 2. Knowledge 如何抽象

Semantic View 的基本模型不是文档 chunk，而是一个业务数据模型：

```text
Semantic View
├── Logical Tables
│   └── business entities
├── Relationships
│   └── join semantics
├── Facts
│   └── row-level quantitative meaning
├── Dimensions
│   └── business slicing
├── Metrics
│   └── governed KPI formulas
├── Filters
├── Synonyms
├── Verified Queries
└── Custom Instructions
```

例如 Customer → Order → Line Item，并定义 total_revenue、average_order_value 等业务指标。这些定义已经不是“检索提示”，而是机器可执行的 business semantics。

## 3. Knowledge 如何保存

Snowflake 把语义保存为数据库 schema object，而不是单独的知识服务。由此可以复用 Snowflake 的权限、分享、SQL 管理和数据治理能力。

当前文档仍支持 legacy semantic model YAML，但新实现推荐 Semantic Views。

## 4. Unstructured Knowledge

Snowflake 没有把所有知识都塞进 Semantic View。另一条线是 Cortex Search：

```text
Structured
  → Semantic View
  → Cortex Analyst

Unstructured
  → Cortex Search
  → Agent
```

Cortex Agents 可以同时使用 Cortex Analyst、Cortex Search、code execution、custom tools 和 web search。

https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents

## 5. Agent 如何使用

```text
User Question
   ↓
Agent orchestration
   ├── Cortex Analyst → Semantic View → SQL
   ├── Cortex Search → Search Service
   └── Custom Tool
   ↓
Combined result
   ↓
Reasoning
   ↓
Answer
```

Snowflake 的重要思想是：Knowledge Access 本身就是 Agent capability。

## 6. 业务知识工程思想

Snowflake 的 Semantic View best practices 明确强调从业务用户角度建模，而不是从数据库结构角度建模；应使用 business terminology、明确定义 proprietary terms、relationships、metrics、filters，并用 verified queries 持续迭代。

因此它已经非常接近 Business Ontology / Semantic Layer，而不是传统 schema registry。

## 7. 对你当前架构的启发

最值得吸收的不是“使用 Snowflake”，而是：

```text
Knowledge
├── Entity
├── Relationship
├── Metric
├── Rule
├── Filter
├── Definition
└── Source
```

业务语义应该是一等对象。金融场景中的 AUM、Active Client、Eligible Account、Net Flow、Suitability、Risk Level 不能只依赖 embedding 猜测。

Structured 和 Unstructured 应该统一到 Agent，但不要强行统一存储：

```text
Ontology / Semantic Layer
        +
Canonical Knowledge Corpus
        +
RAG
        +
Tools
        ↓
Evidence / Context Pack
```

## 8. 局限

Snowflake Semantic View 最强的是结构化企业数据和可执行 business semantics。它不能替代大规模自然语言 corpus、episodic memory、procedural Skill 或跨系统 knowledge interchange。