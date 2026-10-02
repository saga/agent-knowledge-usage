# 业界实践

本目录研究云厂商、企业软件厂商、Data / AI 平台厂商、Agent 平台和大型 AI 基础设施公司如何抽象、保存、检索、使用和治理业务知识 / 企业知识。

研究日期：2026-10-02。

这里不再固定研究某几家“常见大厂”。Snowflake、Databricks、Google、OpenAI、Anthropic 只是最初的 seed；每轮新的业界研究都要求主动扩展厂商和架构路线。具体规则见 [Industry Practice Research Skill](../skills/industry-practice-research/SKILL.md)。

这些文章不是产品介绍。重点是把每家厂商的产品形态还原成系统设计问题：

Knowledge 是什么？
↓
保存成什么？
↓
谁拥有它？
↓
Agent 如何发现和读取？
↓
什么时候进入 Context？
↓
权限在哪里生效？
↓
如何处理版本 / Freshness / Provenance？
↓
什么问题仍然留给应用？

## 厂商报告

### Data / AI Platform

- [Snowflake：业务知识为什么被直接做成数据库对象](./snowflake-business-knowledge.md)
- [Databricks：从受治理的语义对象走向显式 + 推断的 Ontology](./databricks-business-knowledge.md)
- [Google：从 Data Catalog 走向 Context Engine](./google-business-knowledge.md)
- [Oracle：Knowledge Base + Data Source + RAG Tool + SQL Tool](./oracle-generative-ai-agents-business-knowledge.md)
- [NVIDIA：把 Agent 能力做成框架无关的 Toolkit，并把 Memory / Retriever 独立出来](./nvidia-nemo-agent-knowledge.md)

### Agent / Model Platform

- [OpenAI：把 Knowledge Access 做成 Agent Capability](./openai-business-knowledge.md)
- [Anthropic / Claude：把知识拆成 Skill、Resource、Memory 和 Context](./anthropic-claude-business-knowledge.md)
- [AWS：把 Knowledge、Memory、Agent Runtime 拆成独立能力](./aws-bedrock-agentcore-business-knowledge.md)
- [IBM：Knowledge Agent、知识库和 Agentic Control Plane](./ibm-watsonx-orchestrate-business-knowledge.md)

### Enterprise Application / Business Platform

- [Microsoft：Knowledge Source、Copilot Connector 和 Memory 是不同层](./microsoft-copilot-studio-business-knowledge.md)
- [Salesforce：把 Grounding、Data Library、Structured Data 和 RAG 组合成 Agent Knowledge](./salesforce-agentforce-business-knowledge.md)
- [SAP：Knowledge Graph + Business Data Cloud + Process Context](./sap-joule-knowledge-business-knowledge.md)
- [ServiceNow：AI Search + Enterprise Knowledge Graph + Customer Context](./servicenow-ai-knowledge-business-knowledge.md)
- [Palantir：Ontology 是 Agent Knowledge 之外的整个 operational world model](./palantir-aip-ontology-business-knowledge.md)

## 这轮扩展后的厂商覆盖

这张表不是能力评分，而是帮助研究者避免只看一种厂商路线。

| 厂商 | 主要路线 | Knowledge 重点 | 对 Agent 的主要价值 |
|---|---|---|---|
| Snowflake | Data platform | Semantic View / business definitions | 可执行业务语义 |
| Databricks | Data + AI platform | Modeled + Inferred Context / Ontology | 受治理语义 + 自动发现 |
| Google | Cloud / AI platform | Search / context / data semantics | 企业数据 grounding |
| Oracle | Cloud / database | Knowledge Base + RAG + SQL | structured + unstructured access |
| NVIDIA | AI infrastructure | Retriever / Memory / Agent Toolkit | framework-neutral capability |
| OpenAI | Agent platform | File / Search / Tool capability | 通用 Knowledge Access |
| Anthropic | Agent / model platform | Skill / Resource / Memory | procedural knowledge externalization |
| AWS | Cloud / Agent runtime | Agentic Retrieval + AgentCore Memory | retrieval + memory + runtime |
| IBM | Enterprise AI platform | Knowledge Agent + Knowledge Base + Control Plane | source-grounded enterprise agents |
| Microsoft | Enterprise platform | Knowledge Sources + Connectors + Memory | enterprise grounding + ACL propagation |
| Salesforce | CRM / data platform | Data Library + structured data + RAG | business-object grounding |
| SAP | ERP / business platform | Knowledge Graph + Business Context | process-aware business semantics |
| ServiceNow | Workflow / ITSM platform | AI Search + Knowledge Graph + direct context | operational customer context |
| Palantir | Data / operational platform | Ontology + logic + actions + policy | operational world model |

## 五类路线

目前已经能看出至少五类不同路线：

### 1. Semantic / Ontology-first

代表：

- Snowflake
- Databricks
- SAP
- Palantir

核心问题：

> 企业业务到底是什么意思？

常见对象：

- metric；
- entity；
- relationship；
- ontology；
- rule；
- policy；
- action。

### 2. Search / Retrieval-first

代表：

- OpenAI
- Google
- IBM
- Oracle
- Salesforce
- Microsoft
- ServiceNow

核心问题：

> Agent 如何从已有企业资料中得到可信上下文？

常见机制：

- search；
- RAG；
- connector；
- data library；
- knowledge base；
- citation。

### 3. Memory-first / Agent State

代表：

- AWS AgentCore
- Microsoft Copilot Studio
- NVIDIA NeMo
- Anthropic / Claude 相关 Agent 能力

核心问题：

> Agent 怎样跨 session 保存真正值得保留的信息？

这条路线应该与 authoritative enterprise knowledge 分开研究。

### 4. Capability / Agent Runtime-first

代表：

- OpenAI
- Anthropic
- AWS
- IBM
- NVIDIA

核心问题：

> Knowledge / Memory / Skill / Tool 如何成为 Agent 可以发现、调用和治理的 capability？

### 5. Operational World Model

代表：

- Palantir
- SAP
- ServiceNow
- Salesforce

核心问题：

> Agent 不只是回答问题，而是如何理解业务对象、当前状态、关系、权限并执行动作？

## 一个重要的研究方法变化

以后研究某个主题，不应该只写：

~~~
OpenAI
Anthropic
Google
Databricks
Snowflake
~~~

而应该先做：

~~~
问题
 ↓
架构路线
 ↓
候选厂商
 ↓
不同厂商类别
 ↓
官方证据
 ↓
反例 / 不同实现
 ↓
共同模式
~~~

例如研究“Agent Knowledge”时，至少应该有：

~~~
Data Platform
+ Cloud / Agent Runtime
+ Enterprise Application
+ Operational Platform
~~~

这样才有资格把多个产品中反复出现的机制提升成 candidate primitive。

## 横向模型

### Representation

| 路线 | 典型表示 |
|---|---|
| Semantic / Ontology | Metric / Entity / Relation / Ontology / Business Object |
| Search / Retrieval | Document / Chunk / Index / Data Library / Knowledge Base |
| Memory | Fact / Preference / Episode / Summary / Memory Record |
| Capability | Skill / Tool / Connector / MCP / Provider |
| Operational | Object / State / Action / Policy / Workflow |

### Runtime

不同路线最后都会进入类似：

~~~
Canonical / Source
        ↓
Semantic / Knowledge / Memory
        ↓
Retrieval / Query / Capability
        ↓
Authorization / Policy
        ↓
Context Assembly
        ↓
Agent Reasoning
        ↓
Action / Business System
~~~

但每一家厂商把边界放在不同位置。

## 真正共同的架构

把产品名去掉后，可以得到一个更稳妥的研究模型：

~~~
Canonical Source
       ↓
Semantic Meaning / Knowledge
       ↓
Entities / Relations / Metrics / Rules
       ↓
Retrieval / Query / Navigation
       ↓
Permission / Authority / Provenance
       ↓
Context Assembly
       ↓
Agent
       ↓
Tools / Actions / Business System
~~~

旁边还要有：

~~~
Version
Freshness
Evaluation
Audit
Memory
Lifecycle
~~~

这比“Knowledge = Vector Store”更接近企业 Agent 的真实形态。

## 一个重要的共同点：Knowledge 和 Context 开始分开

不同路线虽然做法不同，但越来越接近：

~~~
Long-lived knowledge
        ↓
selection / retrieval / policy
        ↓
current context
        ↓
reasoning
~~~

真正需要控制的是：

> 这一轮为什么把这几条知识交给模型？

这正是 Context Engineering、Evidence、Authority、Permission 开始进入 Knowledge Architecture 的原因。

## 一个重要的共同点：Business Semantics 和 Retrieval 不是一层

结构化业务定义更适合：

- Entity；
- Metric；
- Relationship；
- Rule；
- Filter；
- Business Object。

自然语言资料更适合：

- Document；
- Section；
- Proposition；
- Evidence。

所以实际系统更可能是：

~~~
Semantic Layer
+
Knowledge Corpus
+
Graph / Relationship Index
+
Retrieval
+
Memory
+
Context Assembly
~~~

而不是寻找一个万能存储。

## 一个重要的共同点：自动发现开始成为下一阶段

Databricks inferred context、Google enrichment、AWS memory extraction、Microsoft connectors、Palantir ontology integration、SAP business context 等路线都说明：

> 企业知识不能全部依靠人工重新录入。

但自动抽取又不能直接成为真相。

更稳妥的流程应该是：

~~~
Source
  ↓
Candidate Knowledge
  ↓
Extract / Infer
  ↓
Validate
  ↓
Assign Authority
  ↓
Publish
  ↓
Retrieve
~~~

所以 Knowledge Engineering 的下一阶段不是“全自动生成知识库”，而是：

> 自动发现 + 验证 + authority + lifecycle。

## 对当前项目最重要的结论

Common Agent Library 不应该复制某一家公司的产品对象。

更值得统一的是这些 primitive：

~~~
KnowledgeAsset
Definition
Entity
Relation
Metric
Rule
Claim / Proposition
Evidence
Memory
Skill
Capability
Permission
Authority
Context
State
Action
Lifecycle
Provider
~~~

底层可以接 Snowflake、Databricks、Google、OpenAI、AWS、Microsoft、SAP、Palantir、Postgres、Graph、MCP 等不同 provider。

最终要解决的问题不是“我们选哪一个 Knowledge Product？”，而是：

> 不同知识资产怎样在不丢失语义、权限、来源和生命周期的前提下，被同一个 Agent Runtime 可靠消费？

## 研究边界

本目录不把“支持某个 feature”直接等同于“行业成熟”。

结论应按：

~~~
Vendor Fact
    ↓
Cross-source Observation
    ↓
Cross-vendor Pattern
    ↓
Engineering Practice
    ↓
Candidate Primitive
~~~

逐级增强。

特别关注：

- 产品能力 vs architecture；
- architecture vs adoption；
- 官方资料 vs customer evidence；
- source permission vs retrieval；
- memory vs authoritative knowledge；
- tool capability vs authorization；
- ontology vs business state；
- inference vs certified truth。

