# OpenAI File Search / Retrieval

来源：https://developers.openai.com/api/docs/guides/tools-file-search

## OpenAI 实际提供的是什么

OpenAI 的路线更像一个 hosted Knowledge Access service。

基本模型：

~~~text
File
  ↓
Vector Store
  ↓
parsed / chunked / indexed content
  ↓
Search
  ↓
Agent Tool
~~~

系统把 parsing、chunking、embedding、indexing 和部分 retrieval plumbing 托管起来。

这降低了 Agent 应用第一次接入 external knowledge 的成本。

## Retrieval 已经不只是“向量相似度”

当前 Retrieval API 包含：

- query rewriting；
- attribute filtering；
- result limits；
- ranking options；
- score threshold；
- semantic + text retrieval。

因此一个更准确的模型是：

~~~text
query
  ↓
rewrite
  ↓
filter
  ↓
retrieve
  ↓
rank
  ↓
results
~~~

这本身就是一个完整 Knowledge Access capability。

## 为什么 metadata 很重要

Vector similarity 很容易回答：

> 哪个 chunk 和我的问题像？

但企业问题往往先需要：

> 我应该在哪个范围找？

例如：

~~~text
tenant = A
region = APAC
confidentiality <= internal
date >= 2026-01-01
documentType = policy
~~~

所以 metadata filter 在企业检索里不是附属功能，而是 retrieval scope 的一部分。

## File Search 与 Business Semantic Layer 的差异

OpenAI 的 File Search 能非常方便地找到：

> “关于 AUM 的政策文件在哪里？”

但它不会自动把：

> AUM = 哪些账户 + 哪个时间口径 + 哪种货币 + 哪些排除项

变成企业级 metric definition。

因此：

~~~text
File Search
   = Knowledge Access

Semantic Layer
   = Business Meaning
~~~

两者不是互相替代。

## Agent Tool 化的意义

File Search 被作为 Agent tool 后，模型可以自己决定：

~~~text
Need external knowledge?
   ↓
FileSearchTool
   ↓
Observe result
   ↓
Continue reasoning
~~~

这和传统 application-level RAG 最大的不同，是 retrieval 已进入 Agent action space。

## 对 Common Agent Library 的启发

应用层应该依赖：

~~~text
KnowledgeAccess
├── search
├── filters
├── ranking
├── evidence
└── provenance
~~~

底层才去连接：

- OpenAI vector stores；
- pgvector；
- Elasticsearch；
- Snowflake Search；
- Databricks；
- Graph；
- enterprise search。

这样业务 Agent 不需要知道知识到底存在哪里。

## 局限

这种 generic approach 很轻量，但 business semantics、ontology、authority model、enterprise entitlement 仍然需要应用自己的系统补齐。

因此 OpenAI 路线更适合作为基础设施的 retrieval substrate，而不是完整 Business Knowledge architecture。
