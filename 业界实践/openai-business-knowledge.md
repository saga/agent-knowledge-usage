# OpenAI：把 Knowledge Access 做成 Agent Capability

研究日期：2026-10-02

## 先看结论

OpenAI 与 Snowflake、Databricks、Google 的路线明显不同。

它没有优先提供完整 enterprise ontology，而是把外部知识访问做成 Agent 可以直接调用的 capability。

官方资料：
- https://developers.openai.com/api/docs/guides/retrieval
- https://developers.openai.com/api/docs/guides/tools-file-search
- https://openai.github.io/openai-agents-python/ref/tool/

最简化的模型是：

~~~text
File
  ↓
Vector Store
  ↓
chunks + embeddings + attributes
  ↓
Search
  ↓
File Search Tool
~~~

## 1. 这个模型为什么很有价值

它把应用开发者从 parsing、chunking、embedding、indexing、search、ranking 等基础设施细节里解放出来。

开发 Agent 时主要考虑：“我什么时候需要 external knowledge？”而不是“我怎么维护 vector pipeline？”

这是 Knowledge Access as Capability 的典型例子。

## 2. Retrieval 已经不是简单向量搜索

当前 Retrieval 能支持 query rewriting、attribute filtering、result limits、ranking options、score threshold，以及 semantic / text search。

更准确的架构是：

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
evidence
~~~

企业检索通常先需要回答“我应该在哪个范围搜？”，再回答“哪个内容最相关？”。因此 scope metadata 是 Knowledge Access 的一部分。

## 3. OpenAI 的 abstraction 为什么比较轻

可以理解为：

~~~text
Knowledge Asset
=
File
+ Metadata
+ Indexed Representation
+ Retrieval Config
~~~

它通用、低耦合，适合快速接入外部资料。

但它没有直接解决 business entity、semantic metric、ontology、relationship、business rule 和 authority model。这不是缺点，只是抽象层级不同。

## 4. File Search 作为 Tool 的真正意义

传统 application-level RAG：

~~~text
Application
  ↓
search
  ↓
prompt
  ↓
LLM
~~~

Agent Tool 模式：

~~~text
Agent
  ↓
decide
  ↓
FileSearchTool
  ↓
observe
  ↓
reason
~~~

这意味着 retrieval 已经进入 Agent action space。同样的思路可以扩展到 Web Search、MCP、code execution 和 custom knowledge services。

## 5. Metadata 是企业扩展点

Vector similarity 很适合回答“哪个文本像”。企业系统还需要限制 source、scope、tenant、date、type、authority、confidentiality、project。

这些 metadata 决定搜索范围，也可以成为 entitlement 和 policy 的输入。

## 6. 为什么 OpenAI 路线不等于 Enterprise Knowledge

例如用户问“ AUM 怎么定义？”。File Search 可以找到 finance glossary。

但真正的 business definition 可能是：

~~~text
AUM
=
eligible assets
+ valuation convention
+ currency rule
+ effective time
~~~

如果这些定义已经进入 semantic layer，Agent 就不应该再靠文档相似度自己推导。

所以更完整的结构是：

~~~text
Knowledge Access
      +
Business Semantics
~~~

## 7. 对 Common Agent Library 的启发

建议抽象 KnowledgeAccess，至少包含 search、filters、ranking、evidence、provenance 和 scope。

不要让 Agent 直接依赖 pgvector、Elasticsearch、Snowflake Search 或 OpenAI Vector Store。底层 provider 可以变化，上层 Agent 不需要变化。

## 8. 最终边界

Knowledge Access 回答“怎么找到外部信息”；Business Semantics 回答“这个业务概念究竟是什么意思”。两者应该组合，而不是互相替代。

## 9. 局限

generic retrieval 很轻量，但越往企业深处走，就越需要 semantic layer、ontology、authorization、provenance、lifecycle 和 data entitlement。

因此 OpenAI 的路线很适合作为 retrieval substrate，不宜直接当成完整 Business Knowledge architecture。
