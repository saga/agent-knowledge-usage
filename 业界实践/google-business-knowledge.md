# Google：Knowledge Catalog + Semantic Layer + RAG / Agent Search

研究日期：2026-10-02

## 1. 核心路线

Google Cloud 当前的方向非常明确：从传统 Data Catalog 走向面向 Agent 的“universal context engine”。

Google Cloud 在 2026 年推出 Knowledge Catalog，并把传统数据目录的目标从“告诉人表是什么”提升到给 Agent 提供 enterprise business semantics、relationships 和 trusted context。

- https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog
- https://cloud.google.com/blog/products/data-analytics/unveiling-new-bigquery-capabilities-for-the-agentic-era

## 2. Knowledge Catalog 的定位

传统 catalog 通常偏技术 metadata：

```text
table
column
schema
owner
```

而 Agent 需要：

```text
business meaning
relationships
trusted definitions
data quality
lineage
business context
```

因此 Google 把 Knowledge Catalog 定位为企业 context engine：

```text
Enterprise Data / Metadata
       ↓
Knowledge Catalog
       ↓
Context for Agents
```

## 3. Google 的 Knowledge 不是单一对象

Google 的业务知识分散在多个互相组合的层次。

### A. Semantic Layer

Looker / LookML 提供成熟的 business semantics。Google 在 2026 Next 中宣布 LookML Agent 可以读取 strategy documents、spreadsheets、reports 并生成 business-ready semantics，使 Agent 和分析师使用相同的企业定义。

https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up

### B. BigQuery Measures / Business Logic

Google 正在把 programmatic business logic 直接嵌入 SQL / analytics layer，使 metrics 成为可复用、准确和受治理的计算定义。

### C. Knowledge Catalog

统一 enterprise metadata、business context 和跨平台 context。

### D. RAG / Agent Search

对于 documents、websites、unstructured data，Google 提供 Agent Search + RAG Engine。

### E. Data Products

Data Products 可以把 intent、SLA、governance constraints 与 data asset 一起封装。

因此 Google 的总体模型接近：

```text
Business Semantics
      +
Metadata
      +
Data Products
      +
Structured Data
      +
Unstructured Knowledge
      ↓
Knowledge / Context Layer
      ↓
Gemini Agents
```

## 4. RAG Engine：非结构化知识

Google 的 RAG Engine 将 RAG 明确拆成 ingestion、transformation、chunking、embedding、indexing、retrieval、generation。

https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview

Agent Search 还可以作为 RAG Engine backend，统一大规模企业搜索与 grounding。

https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-vertexai-search

因此 Google 不试图让一个 semantic model 承担所有知识，而是把：

```text
semantic layer
      +
search / retrieval
      +
agent
```

组合起来。

## 5. Agent Search

Agent Search 是 Google-quality information retrieval capability，可以处理 website data、structured data、unstructured data，并直接作为 grounding backend。

https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search

## 6. Google 当前最值得关注的一点：Context Engine

Knowledge Catalog 的意义在于：Knowledge 不再等于 search index。

它开始包含：

```text
metadata
semantic models
business definitions
relationships
data products
governance
quality
provenance
```

也就是：

> Context 是经过治理和语义化的数据资产，而不是简单检索结果。

## 7. Agent 如何使用

```text
User Task
   ↓
Gemini Agent
   ↓
Context / Knowledge Layer
   ├── Knowledge Catalog
   ├── Looker semantics
   ├── BigQuery
   ├── Agent Search
   ├── RAG Engine
   └── enterprise sources
   ↓
Reasoning / Grounding
   ↓
Tool / Action
```

这明显比“query → vector search → prompt”更接近 enterprise Agent platform。

## 8. 对你当前架构的启发

### 8.1 Knowledge Layer 最终可能应该是 Context Engine

可以把：

```text
Knowledge
+ Semantic Layer
+ Memory
+ Metadata
+ Governance
```

统一理解为 Context Infrastructure。

### 8.2 Business Semantics 与 RAG 应分层

不要让 embedding system 解决 metrics、business definitions、entity relationships 和 documents 的所有问题。

应该：

```text
Semantic Knowledge
       +
Retrieval Knowledge
       +
Runtime State
       ↓
Context Assembly
```

### 8.3 Data Product 可能成为 Agent Knowledge Asset

未来一个 Data Product 不只是“表 + owner”，还可能包括 intent、semantic definition、quality、SLA、lineage、entitlement 和 agent usage contract。

## 9. 局限

Google 的体系很强，但明显具有 cloud platform shaped 的特点。对 Common Agent Library，应该学习它的 Context Layer、semantic layer、governed data product、search / RAG separation，而不是复制 Google-specific API。