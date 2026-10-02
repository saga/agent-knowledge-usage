# ServiceNow：AI Search + Enterprise Knowledge Graph + Customer Context

研究日期：2026-10-02

## 先看结论

ServiceNow 的实践很值得放到 Snowflake / Databricks / SAP 之外，因为它从 ITSM / CSM 业务应用内部出发，把 AI Search、Enterprise Knowledge Graph、direct structured context、citations、AI policy 一起作为 Agent grounding 基础。

## 1. AI Search 负责 unstructured / searchable knowledge

ServiceNow 的 Live Agent Assist 使用 AI Search Profile 做 RAG retrieval。

默认可以从 Knowledge table 检索，并在结果中显示来源引用。

~~~
Knowledge Article
   ↓
AI Search
   ↓
Retrieved evidence
   ↓
Agent answer
~~~

这与传统 RAG 相似，但它不是完整 Knowledge architecture。

## 2. Enterprise Knowledge Graph 负责 customer-specific context

ServiceNow 同时使用 Enterprise Knowledge Graph 从业务表中获取 contracts、cases、assets、entitlements、interactions、products、customer context。

这说明：

> “知识”不仅是文档，也可以是围绕业务实体组织起来的结构化 operational context。

## 3. Direct Context Path 和 Retrieval Path 可以并存

ServiceNow 文档描述了两种路径：

### Direct Context Builder

直接预取高优先级字段。

### Knowledge Graph / AI Search

根据查询动态获取更多信息。

可以形成：

~~~
High-priority structured context
        +
Dynamic retrieval
        ↓
LLM context
~~~

这一点很适合当前 Context Engineering 研究。

## 4. Policy / Data Layer 不是 Agent Prompt

ServiceNow 当前 Now Assist architecture 明确把 policy layer、data layer、content layer、generative / agentic layer、conversational layer 分开。

因此：

~~~
Policy
  ≠
Knowledge
  ≠
Agent
~~~

## 5. 对 Common Agent Library 的启发

非常值得抽取：

~~~
DirectContextProvider
SearchProvider
KnowledgeGraphProvider
Citation
PolicyContext
~~~

这比只定义 RAGProvider 更通用。

## 6. 局限

ServiceNow 的 Knowledge Graph 和 data model 高度围绕自身业务平台。

这里更应该抽“direct context + retrieval + graph + policy”的组合模式，而不是照搬 ServiceNow object schema。

## Sources

- https://www.servicenow.com/docs/r/customer-service-management/now-assist-for-csm/csm-live-agent-assist.html
- https://www.servicenow.com/docs/r/intelligent-experiences/sn-ai-impl-overview-tools.html?contentId=mmMt2oRsoU9S4nQqT7SK4w
- https://www.servicenow.com/docs/r/intelligent-experiences/knowledge-graph/configuring-knowledge-graph.html
