# Microsoft：Knowledge Source、Copilot Connector 和 Memory 是不同层

研究日期：2026-10-02

## 先看结论

Microsoft Copilot Studio 的设计非常值得拿来和 Snowflake / Databricks 对照，因为它不是先建立一个独立 ontology，而是把企业已有数据源通过连接器和 knowledge source 接入 Agent。

核心链路可以理解为：

~~~
Enterprise systems
  ↓
Copilot Connectors / Knowledge Sources
  ↓
Search / Grounding
  ↓
Agent Context
~~~

同时，Memory 又是另一个生命周期：

~~~
Conversation
  ↓
Agent Memory
  ↓
Future interactions
~~~

这再次说明：

> Enterprise Knowledge 与 Agent Memory 不应该共用一个抽象。

## 1. Knowledge Source 是 Agent 的正式输入边界

Microsoft 文档明确把 knowledge source 定义为 Agent 可以访问、用于 grounding 的数据。

来源可以包括 Power Platform、Dynamics 365、websites、external enterprise systems。

知识是在 agent design / configuration 层被声明的，不是简单把所有企业数据默认暴露给模型。

## 2. Copilot Connectors：external data 进入统一搜索层

Copilot Connectors 可以把外部企业系统的数据索引到 Microsoft Graph，并作为 Copilot Studio Agent 的 knowledge source。

一个关键点是：

> connector 必须遵守 source-level permissions。

也就是说，retrieval 本身不是 permission bypass layer。

可以理解成：

~~~
Source ACL
   ↓
Connector / Graph index
   ↓
Agent knowledge retrieval
   ↓
User-visible context
~~~

这对当前项目非常重要。

## 3. Knowledge Source ≠ Attachment

Microsoft 当前还特别区分 design-time knowledge source 和 conversation attachment。

这对应当前项目中的：

~~~
Knowledge Base
≠
Session Attachment
~~~

不能因为两者最终都会进入 context，就把生命周期合并。

## 4. Memory 是另外一个系统

Copilot Studio 当前提供 Memory preview：

- 每个 Agent 对每个用户维护独立 memory；
- 一个用户的 context 不共享给另一个用户；
- memory 用于未来交互的 personalization / continuity。

因此：

~~~
Knowledge Source
    = organization / application knowledge

Memory
    = user-agent interaction history
~~~

## 5. 对当前 Common Agent Library 的启发

值得抽取：

~~~
KnowledgeSource
Connector
UserEntitlement
Retrieval
SessionAttachment
Memory
~~~

尤其需要把 Discovery、Authorization、Retrieval 分开，而不是设计一个 searchKnowledge() 负责全部事情。

## 6. 局限

Microsoft 的价值主要来自 Microsoft Graph、Copilot connectors、Power Platform 等生态。

因此通用层应该抽 external source registration、source-level permission propagation、search / grounding、session attachment、user-scoped memory，而不是把 Microsoft Graph 作为 Common Library 的 canonical storage。

## Sources

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-copilot-studio
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-connectors
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/memory-overview
