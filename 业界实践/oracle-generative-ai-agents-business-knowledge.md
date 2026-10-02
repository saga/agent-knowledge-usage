# Oracle：Knowledge Base + Data Source + RAG Tool + SQL Tool

研究日期：2026-10-02

## 先看结论

Oracle OCI Generative AI Agents 的架构非常适合拿来验证一个简单事实：

> Enterprise Agent 的 Knowledge 不应该只有一个向量知识库。

Oracle 把 Agent 的访问方式拆成 Knowledge Base / RAG、Oracle Database AI Vector Search、OCI Search with OpenSearch、SQL tool、function calling。

## 1. Knowledge Base 是 RAG 的组织单位

Oracle 把 Knowledge Base 定义为 Agent 可以用于 chat answer 的 data source 集合，并通过 RAG tool 访问。

链路：

~~~
Data Source
   ↓
Knowledge Base
   ↓
RAG Tool
   ↓
Agent
~~~

这说明 Knowledge Base 是 retrieval configuration boundary，而不一定是最终 source of truth。

## 2. Data Source 和 Knowledge Base 生命周期分开

Oracle 文档明确区分 data source、ingestion、knowledge base、agent RAG tool。

而 data source 还会记录 creator、creation time、lifecycle state、ingestion jobs、failure logs。

这说明 enterprise knowledge ingestion 本身就是一个需要可观察、可管理的 lifecycle。

## 3. Structured database access 与 RAG 可以并存

Oracle 同时支持 Oracle Database AI vector search、OCI Search with OpenSearch、SQL Tool。

因此：

~~~
Structured SQL
+
Vector / semantic retrieval
+
Search
+
Functions
↓
Agent
~~~

而不是把 SQL 也强行转成 document RAG。

## 4. 对 Common Agent Library 的启发

应抽取：

~~~
KnowledgeBase
DataSource
Retriever
StructuredQuery
Function
IngestionJob
Provenance
Lifecycle
~~~

而不是只有：

~~~
VectorStore
~~~

## 5. 局限

Oracle 的实现围绕 OCI resource、Object Storage、Oracle Database 等服务组织。

通用库只抽 retrieval / query / lifecycle contract。

## Sources

- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/knowledge-bases.htm
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/ai-data-sources.htm
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/create-data-source.htm
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/
