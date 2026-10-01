# OpenAI：Knowledge Access 作为 Agent Capability

研究日期：2026-10-02

## 1. 核心路线

OpenAI 当前的知识路线与 Snowflake、Databricks、Google 很不一样。

它没有首先把“业务知识”定义成完整 enterprise ontology，而是把 external knowledge 封装成模型可以调用的 retrieval capability。

主要组件：Files API、Vector Stores、Retrieval API、File Search、Agents SDK FileSearchTool、MCP / hosted tools、metadata filters、ranking / query rewriting。

- https://developers.openai.com/api/docs/guides/retrieval
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://openai.github.io/openai-agents-python/ref/tool/

## 2. Knowledge 如何抽象

OpenAI 的底层抽象很简单：

```text
File
  ↓
Vector Store
  ↓
chunks + embeddings + attributes
  ↓
Search
```

Vector store file 可以拥有 attributes，用于 region、category、date、project、confidentiality 等 runtime filtering。

当前 Retrieval API 支持 query rewriting、attribute filters、ranking options、score threshold 以及 hybrid semantic / text search。

https://developers.openai.com/api/docs/guides/retrieval

## 3. 这是一种什么 Knowledge Model

更准确地说，OpenAI 提供的是 **Knowledge Access Model**，而不是完整 Business Knowledge Model。

```text
Knowledge Asset
  = File
  + Metadata
  + Indexed Chunks
  + Retrieval Configuration
```

它并没有要求开发者把 business entity、metric、ontology、semantic relationship、rule 建成 first-class object。

这让系统轻量和通用，但也意味着 business semantics 仍然要由外部系统承担。

## 4. Agent 如何使用

OpenAI 把 File Search 直接做成 hosted tool。

```text
Agent
  ↓
decide
  ↓
FileSearchTool
  ↓
results
  ↓
reason
```

Agents SDK 当前还把 Web Search、File Search、Code Interpreter、Hosted MCP、Tool Search 等统一放进 tool surface。

https://openai.github.io/openai-agents-python/zh/tools/

因此 Knowledge Access 已经成为 Agent action space 的一部分，而不是单独的 application preprocessing。

## 5. Knowledge 如何保存

Hosted storage 模式：

```text
Files API
    ↓
Vector Store
    ↓
parsed / chunked / embedded / indexed
```

开发者不需要自己维护 embedding model、vector database、基础 chunk pipeline 和 ranker。

## 6. Metadata 是重要业务扩展点

虽然 OpenAI 没有原生 enterprise ontology，但 attributes 提供了很有价值的业务过滤接口：

```text
Document
├── content
├── source
├── tenant
├── region
├── category
├── date
├── confidentiality
└── project
```

因此它很适合作为 generic Knowledge Access substrate。

## 7. 对你的架构的启发

### 7.1 Knowledge Access 应该是 Tool / Capability

Common Agent Library 不应让 Agent 直接访问 pgvector、Elasticsearch、Snowflake Search 等具体后端，而应提供：

```text
KnowledgeAccessTool
```

底层 provider 再实现具体 retrieval。

### 7.2 Retrieval configuration 应属于 runtime capability

例如：

```text
KnowledgeSearch
├── filters
├── maxResults
├── ranking
├── threshold
└── queryRewrite
```

这些不应散落在业务 Agent 代码里。

### 7.3 轻量 metadata 应先于“大而全 ontology”

很多 Agent use case 起步只需要 source、type、scope、authority、time、tenant、permissions，然后再向 proposition / graph 演进。

## 8. 局限

OpenAI 的 generic approach 低耦合，但它本身不能替企业解决 business semantics。

例如 AUM 如何定义，vector store 可以帮模型找到文档，但 Snowflake Semantic View / Databricks Metric View 可以把定义变成更直接的 machine-usable semantics。

因此更准确的架构关系是：

```text
OpenAI File Search
      ≈ Knowledge Access Layer

Snowflake / Databricks / Google Semantic Layer
      ≈ Business Semantics Layer
```

两者是互补关系，而不是二选一。