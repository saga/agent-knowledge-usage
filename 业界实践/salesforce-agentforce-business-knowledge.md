# Salesforce：把 Grounding、Data Library、Structured Data 和 RAG 组合成 Agent Knowledge

研究日期：2026-10-02

## 先看结论

Salesforce Agentforce 的路线不是建立一套脱离 CRM 的通用 Knowledge Graph，而是把 Salesforce structured data、knowledge articles、uploaded files、external / web sources、Data 360 / Data Cloud、RAG 组合为 Agent 的 grounding layer。

这条路线特别适合拿来和 Snowflake / Databricks 的“semantic layer first”路线对照。

## 1. Structured data 和 unstructured data 是两类知识

Salesforce 官方把 grounding 的数据分成 structured 与 unstructured。

Structured 例如 Accounts、Contacts、Cases、Data Model Objects。

Unstructured 例如 documents、emails、chat logs、social content。

这意味着 Agent Knowledge 的 representation 并不需要统一成 document / vector。

更合理的模型是：

~~~
Business Objects
+
Documents
+
External sources
↓
Grounding layer
↓
Agent
~~~

## 2. Agentforce Data Library 是受治理的 retrieval index

Data Library 可以索引 knowledge articles、fields、uploaded files、web sources。

目标不是成为 source of truth，而是为 Agent 提供 grounding。

因此：

~~~
Canonical business data
        ↓
index / retriever
        ↓
grounded prompt
~~~

依然保持 source 与 retrieval view 分离。

## 3. RAG 只是 Grounding 的一种方法

Salesforce 明确把 RAG 描述为 grounding unstructured data 的方法。

结构化 CRM 对象可以通过直接结构化访问进入 Agent。

所以当前项目不要把 Knowledge = RAG 写死。

更通用的是：

~~~
Knowledge Access
├── structured lookup
├── semantic retrieval
├── RAG
├── web search
└── application action
~~~

## 4. 权限和数据边界仍在平台层

Salesforce 的 Agentforce 建立在原有 CRM / Data 360 权限与数据模型之上。

对 Common Agent Library 更重要的抽象不是 Salesforce Object，而是：

~~~
Knowledge Source
Data Entitlement
Retriever
Grounding Context
Citation / Provenance
~~~

## 5. 与当前项目的启发

特别值得吸收：

> Knowledge provider 可以同时提供 structured retrieval 和 unstructured retrieval，最终由 Agent Runtime 统一消费。

这比“所有知识先转成向量”更接近企业系统。

## 6. 局限

Agentforce 的优势高度依赖 Salesforce data model、Data 360 和 CRM ecosystem。

因此 Common Agent Library 不应该把对象模型或 Data 360 当成通用 primitive。

## Sources

- https://help.salesforce.com/s/articleView?id=ai.agent_parent_data.htm&language=en_US&type=5
- https://help.salesforce.com/s/articleView?id=ai.data_library_parent.htm&language=en_US&type=5
- https://trailhead.salesforce.com/content/learn/modules/grounding-an-agent-with-data/learn-the-basics-of-grounding
