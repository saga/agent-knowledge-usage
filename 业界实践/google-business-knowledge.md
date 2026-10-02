# Google：从 Data Catalog 走向面向 Agent 的 Context Engine

研究日期：2026-10-02

## 先看结论

Google Cloud 当前的路线不是再做一个更强的文档搜索，而是把传统 Data Catalog 往 enterprise context engine 推。

传统 catalog 解决：“这张表是什么？”

Agent 需要的是：“这个数据在业务上是什么意思、和什么有关、哪个定义可信、谁能用、怎样把它和其他知识放在一起？”

2026 年推出的 Knowledge Catalog 正沿着这个方向组合 metadata、semantic models、business context、relationships、data products 和搜索。

官方资料：
- https://cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog
- https://cloud.google.com/blog/products/data-analytics/unveiling-new-bigquery-capabilities-for-the-agentic-era
- https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up
- https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search

## 1. 为什么传统 Data Catalog 不够

传统 catalog 更偏技术 metadata：table、column、schema、owner、description。

这些对 Agent 有用，但不足以支持真正的业务推理。Agent 还需要 business meaning、relationships、trusted definitions、quality、lineage、intent、usage context 和 governance。

所以 Google 开始把 catalog 的角色从“资产目录”变成“上下文基础设施”。

## 2. Google 的 Knowledge 不是一个对象

当前体系大致由几层组成。

### Looker / semantic layer

LookML 表达 business semantics。

### BigQuery measures / business logic

业务计算定义进入数据分析层。

### Knowledge Catalog

聚合企业 metadata 和 business context。

### Agent Search / RAG Engine

处理文档、网站和非结构化知识。

### Data Products

把 intent、SLA、governance constraints 等和数据资产一起组织起来。

整体更接近：

~~~text
Semantic Layer
+
Catalog
+
Data Products
+
Structured Data
+
Unstructured Search
      ↓
Context Layer
      ↓
Agent
~~~

## 3. Knowledge Catalog 的三件事

### Aggregation

从不同平台把 metadata、semantic assets 和 context 汇聚起来。

### Enrichment

从已有资产和非结构化内容中补充 entity relationships、business glossary、自然语言描述和 verified SQL patterns。

### Search

让这些 context 可以被 Agent 发现和使用。

因此：

~~~text
Collect
  ↓
Understand
  ↓
Find
~~~

三个阶段缺一不可。

## 4. Data Product 为什么值得关注

传统数据资产常常只有 dataset + owner。

Agent 真正需要的可能是：

~~~text
data
+
intent
+
semantic definition
+
quality
+
SLA
+
lineage
+
entitlement
+
usage contract
~~~

这意味着一个 Data Product 最终可以成为 Agent Knowledge Asset。

Agent 不只是知道“这张表有什么”，还知道它适合回答什么问题、多久更新、有什么限制、谁可以使用。

## 5. RAG Engine 为什么仍然存在

Knowledge Catalog 不能替代文档检索。

RAG Engine 主要处理 ingestion、transformation、chunking、embedding、indexing、retrieval、generation。

semantic/catalog layer 处理 meaning、relation、trust、governance。

所以两者应该组合：

~~~text
Business Semantics
+
Retrieval
+
Governed Assets
      ↓
Context Assembly
      ↓
Agent
~~~

## 6. Context Engine 是真正值得抽象的词

一个 Agent 当前真正需要的可能是 metric definition、customer entity、policy paragraph、data asset、lineage、current state 和 permission。

它们的存储方式完全不同，但最终都会进入同一个 reasoning context。

因此：

> Knowledge Layer 管理长期知识；Context Layer 负责这一轮真正给模型看的知识投影。

两个层最好不要合并。

## 7. 最难的问题其实是冲突解决

统一 context engine 最难的不是搜索，而是不同来源冲突时谁赢。

例如 Finance 把 Revenue 定义为 X，Sales dashboard 用 Y，历史报告写 Z。

如果没有 authority、scope、effective time，统一搜索只会把三个答案一起交给模型。

所以仍然需要 Source、Authority、Scope、Effective Time 和 Permission。

搜索不是治理。

## 8. 对当前项目

当前项目可以抽取：

~~~text
Canonical Knowledge
+
Semantic Layer
+
Data Products
+
Search / Retrieval
+
Memory
+
State
+
Permission
      ↓
Context Assembly
      ↓
Agent
~~~

不需要复制 Google API。真正要借鉴的是它把数据目录、业务语义、检索和 Agent context 放到了一条完整链上。

## 9. 局限

Google 的方案明显带有 Google Cloud ecosystem 的形状。

Common Agent Library 更应该学习 semantic layer、context aggregation、governed data product、search / RAG separation 和 source authority，而不是复制 cloud-specific API。
