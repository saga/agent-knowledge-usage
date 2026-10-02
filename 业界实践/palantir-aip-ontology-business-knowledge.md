# Palantir：Ontology 是 Agent Knowledge 之外的整个 operational world model

研究日期：2026-10-02

## 先看结论

Palantir 与 Snowflake / Databricks 的最大差异之一，是它没有把 Ontology 仅仅看成 semantic metadata。

Palantir 明确把 Ontology 放在：

~~~
Data
+
Objects
+
Relationships
+
Logic
+
Actions
+
Security Policies
↓
Operational Ontology
↓
AI / Applications / Workflows
~~~

因此它非常适合研究企业 Agent 如何从“回答问题”走向“理解业务世界并执行”。

## 1. Ontology 不只是数据字典

Palantir 文档明确把 Ontology 描述为企业 data、logic、action、security policy 的统一表示。

Ontology 中有 object types、object sets、links / relationships、actions、functions / logic。

所以 Knowledge 的最小单位不再只是 document / claim，而可能是：

~~~
Object + Relation + Action + Rule
~~~

## 2. AIP Agents 直接建立在 Ontology 上

AIP 的 agent / workflow 能直接使用 Ontology 数据、logic 和 actions。

这意味着：

~~~
Ontology
   ↓
Context
   ↓
Reasoning
   ↓
Action
   ↓
Business system
~~~

中间不需要先把全部内容转换为自然语言文档。

## 3. Ontology MCP 是非常重要的设计

Palantir 现在可以通过 Ontology MCP 把 object types、SQL / query tools、action types、query functions、agents 暴露给外部 Agent。

这非常适合当前 Common Agent Library 的 capability boundary 研究：

~~~
Ontology Provider
      ↓
MCP tools / resources
      ↓
External Agent
~~~

也说明 MCP 可以成为 semantic / operational system 的 access layer，而不只是工具调用。

## 4. Security 与 Ontology 在同一模型中

Palantir 强调 Ontology 对 enterprise security policy 的承载。

这与单独做一个“RAG permission middleware”不同。

真正的设计更接近：

~~~
Business Object
+
Access Policy
+
Action Policy
↓
Agent-accessible operational model
~~~

## 5. 对当前项目的启发

值得进一步研究的 primitive：

~~~
Entity
Relation
BusinessState
Action
Policy
OntologyQuery
OntologyAction
Capability
Evidence
~~~

这也验证了当前项目一直强调的边界：

> Tool ≠ Authorization；但一个成熟 operational platform 可以把 action 和 policy 放到同一个受治理模型中。

## 6. 局限

Palantir Ontology 是强平台级设计，并不是所有 enterprise Agent 都需要这么完整的 operational model。

因此 Common Agent Library 只应抽取 contract，不应该复制 Ontology implementation。

## Sources

- https://www.palantir.com/docs/foundry/architecture-center/ontology-system
- https://www.palantir.com/docs/foundry/aip
- https://www.palantir.com/docs/foundry/aip/aip-features
- https://www.palantir.com/docs/foundry/ontology-mcp/sample-architecture
