# SAP：Knowledge Graph + Business Data Cloud + Process Context

研究日期：2026-10-02

## 先看结论

SAP 的 Agent 路线非常偏企业业务语义。

Joule Agents / Assistants 的设计核心不是单纯把文档拿来做 RAG，而是把 Business Data Cloud、Business Semantics、SAP Knowledge Graph、Process Context、Policies、Tools 组合起来。

~~~
Business Data Cloud
+
Business Semantics
+
SAP Knowledge Graph
+
Process Context
+
Policies
+
Tools
↓
Joule Agents
~~~

这对于金融、供应链、ERP、合规类 Agent 尤其值得研究。

## 1. SAP Knowledge Graph 是 business context 层

SAP 当前公开资料明确把 Knowledge Graph 与 Business Data Cloud、business semantics 放在 Joule grounding 架构中。

目标是让 Agent 理解 data、processes、policies、relationships。

所以这里的 Knowledge 更接近：

~~~
Enterprise Operational Ontology
~~~

而不是：

~~~
Document Corpus
~~~

## 2. Joule Agent 不只是回答

Joule Agents 可以使用 Joule Skills、other agents、third-party applications、tools，并通过业务上下文进行 reasoning 和 action。

这说明 Knowledge、Procedural capability、Business process、Action 需要一起设计，但职责不能混。

## 3. Business semantics 是 Knowledge 的核心部分

SAP 的路线提醒我们：企业 Agent 最难的问题不一定是“找文档”，而是：

- 这个 business object 是什么？
- 它和哪个对象有关？
- 当前业务流程在哪一步？
- 哪个 policy 适用？
- Agent 能否对它执行 action？

这正好对应当前项目中的 Entity、Relation、Rule、State、Policy、Action。

## 4. Governance 与 Knowledge 是同一运行链上的不同责任

SAP 强调 policy-aware reasoning 和 access to appropriate information。

因此推荐模型：

~~~
Knowledge
   ↓
Business Context
   ↓
Authorization / Policy
   ↓
Agent Reasoning
   ↓
Action
~~~

不要让 Knowledge retrieval 本身承担全部 policy decision。

## 5. 对 Common Agent Library 的启发

应重点保留 BusinessEntity、Relation、BusinessContext、PolicyReference、Procedure / Skill、Action、Authority。

Knowledge Graph provider 只是这些 primitive 的一种实现。

## 6. 局限

SAP 的 business semantics 与 SAP application ecosystem 强绑定。

它证明的是“ERP / business-process heavy enterprise Agent”的一种路线，不应直接泛化成所有 Agent 都需要完整 enterprise knowledge graph。

## Sources

- https://www.sap.com/joule-agents
- https://www.sap.com/products/artificial-intelligence/knowledge-graph.html
