# 业界实践

本目录研究 Snowflake、Databricks、Google、OpenAI、Anthropic（Claude）如何抽象、保存、检索、使用和治理业务知识 / 企业知识。

研究日期：2026-10-02。

## 报告

- [Snowflake：业务知识抽象、保存与 Agent 使用](./snowflake-business-knowledge.md)
- [Databricks：从 Unity Catalog Semantics 到 Genie Ontology](./databricks-business-knowledge.md)
- [Google：Knowledge Catalog + Semantic Layer + RAG / Agent Search](./google-business-knowledge.md)
- [OpenAI：Knowledge Access 作为 Agent Capability](./openai-business-knowledge.md)
- [Anthropic / Claude：Skills、MCP、Memory 与 Context Engineering](./anthropic-claude-business-knowledge.md)

## 横向结论

当前五家公司的路线可以粗略分成三种：

### 1. Semantic-first

Snowflake、Databricks、Google 都在把 business semantics 提升到平台级一等对象。

```text
Business Definition
      ↓
Semantic / Ontology
      ↓
Governed Data / Knowledge
      ↓
Agent
```

### 2. Retrieval-first

OpenAI 更偏向把 external knowledge 封装成通用 retrieval capability：File → Vector Store → Search → Agent Tool。

### 3. Capability-first

Anthropic 更偏向把知识按认知职责拆成 Skills、MCP Resources、Memory、Context 等可组合 capability。

## 对本项目最重要的综合结论

不要把 `Knowledge` 定义成 Vector Store，也不要把 `Business Knowledge` 等同于 RAG。

更合适的长期抽象是：

```text
Business Knowledge
├── Canonical Source
├── Semantic Meaning
├── Entities / Relations
├── Metrics / Rules
├── Retrieval Views
├── Procedures / Skills
├── Memory / Experience
├── Provenance / Authority
├── Scope / Permission
├── Freshness / Version
└── Runtime Context Assembly
```

其中：

```text
Semantic Layer  = what the business means
Knowledge      = what is known
RAG / Search   = how to find it
Skill          = how to act on it
Memory         = what happened
Tool           = what the agent can do
Context        = what the model sees now
Policy         = what it is allowed to do
Evidence       = why the answer/action is justified
```

这比任何一家厂商的具体产品 schema 都更适合作为 Common Agent Library 的上层抽象。