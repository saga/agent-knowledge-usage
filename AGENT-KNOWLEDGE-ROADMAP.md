# AI Agent Knowledge & Capability Roadmap

> 目的：从理论和战略层面理解并指导一系列 AI Agent 应用、Common Library、Team Agent、Data Agent、Research Agent、金融服务 Agent 的共同基础，而不是只优化一个 RAG 系统。
>
> 研究日期：2026-10-02

## 1. 从“LLM + Prompt + RAG + Tools”走向 External Cognitive Infrastructure

进入长期、复杂、企业级 Agent 后，会同时遇到 Knowledge、Memory、Skills、Ontology、Graph、Tools、Business State、Planning、Context Engineering、Protocols、Evaluation、Governance 等问题。

RAG 只是 Knowledge Access 的一种机制。

| Primitive | 核心问题 |
|---|---|
| Model | 我能推理什么 |
| Knowledge | 世界 / 领域是什么样 |
| Ontology | 这些概念到底是什么意思 |
| RAG | 到哪里找证据 |
| Graph | 关系怎样导航 |
| Memory | 过去发生了什么 / 记住什么 |
| Skill | 如何完成一类任务 |
| Tool | 如何读 / 改变外部世界 |
| State | 当前业务处于什么状态 |
| Workflow | 哪些步骤必须按规则执行 |
| Protocol | Agent / Tool / Agent 如何通信 |
| Context | 当前这次推理到底给模型看什么 |
| Evidence | 结论依据是什么 |
| Policy | 什么允许做 |
| Evaluation | 做得是否正确 |

## 2. 理论总模型：能力外置

2026 年的 Externalization in LLM Agents 综述将近年的 Agent 演进概括为能力外置：

- Memory 外置跨时间状态
- Skills 外置程序性知识
- Protocols 外置交互结构
- Harness 负责组织这些组件成为可靠运行环境

参考：

- https://arxiv.org/abs/2604.08224
- https://arxiv.org/abs/2512.13564

可以把演进理解成：

Model Weights → Prompt / Context → Retrieval → Structured External Cognition → Agent Harness → Adaptive Agent System

长期真正要建设的不是“一个更大的 Knowledge Base”，而是一套可组合、可治理、可评测的 external cognitive infrastructure。

## 3. Agent 的主要研究领域

### 3.1 Model / Parametric Knowledge

研究：模型参数里有什么知识？什么知识不可靠？什么时候应该信模型本身？

覆盖：

- pretraining
- post-training
- reasoning
- knowledge boundary
- knowledge editing
- fine-tuning
- continual learning

关键认识：模型参数不是一个可以直接查询的 Knowledge Base。Knowledge Boundary 研究说明“参数中存在知识”和“模型可以可靠表达知识”并不相同。

- https://aclanthology.org/2025.acl-long.256/
- https://aclanthology.org/2023.acl-long.546.pdf

### 3.2 Knowledge Engineering

研究：如何把现实世界信息变成长期可维护、可追溯的 Knowledge Assets？

应该能够表达：

- canonical source
- sections / paragraphs
- claims / propositions
- concepts / entities / relations
- rules / conditions / exceptions
- procedures
- examples / counterexamples
- provenance / version
- temporal validity

核心原则：

Source + Structured Knowledge + Derived Views

而不是：

Source → summary → delete source

### 3.3 RAG / Information Retrieval

覆盖：BM25、dense retrieval、hybrid、metadata filtering、reranking、query rewriting、contextual retrieval、late chunking、hierarchical retrieval、GraphRAG、agentic retrieval、evidence navigation。

演进：

Vector RAG → Hybrid RAG → Contextual RAG → Multi-stage Retrieval → Graph / Hierarchical Retrieval → Agentic Retrieval → Evidence Navigation

最终目标不是 Recall@K，而是：

Find → Understand → Expand → Verify → Use → Cite

### 3.4 Ontology / Semantic Layer / Knowledge Graph

RAG 解决“哪里有相关内容”；Ontology / Semantic Layer 解决“这些东西在业务上到底是什么意思”。

尤其企业数据需要表达：

- metric definition
- grain
- join path
- business entity
- ownership
- lineage
- valid time
- authoritative source

建议理解为：

Raw Data → Schema → Semantic Layer → Ontology → Knowledge Graph → Agent

### 3.5 Memory Engineering

RAG 与 Memory 有重叠，但不是一回事。

至少区分：

- Working Memory：当前任务状态
- Factual Memory：世界 / 用户 / 项目事实
- Episodic Memory：过去发生过什么
- Experiential Memory：什么方法有效 / 失败
- Procedural Memory：应该怎么做

2025 survey 明确把 agent memory 与 RAG、context engineering 区分，并从 forms、functions、dynamics 三个维度研究 memory。

- https://arxiv.org/abs/2512.13564

### 3.6 Agent Skills / Procedural Knowledge

Skill 解决“如何做”，Knowledge 解决“知道什么”。

Anthropic Agent Skills 使用 progressive disclosure：

metadata → SKILL.md → reference files → scripts / resources

- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### 3.7 Tools / Connectors / MCP / A2A

简单区分：

- Knowledge = read / understand
- Tool = query / act
- MCP = Agent → Tool / Resource
- A2A = Agent → Agent

MCP 的长期价值是 capability discovery、tool schema、resource access、execution contract 标准化；A2A 则解决跨框架 Agent delegation / collaboration。

- https://a2a-protocol.org/v1.0.0/

### 3.8 Planning / Reasoning / Workflow / Business State

复杂 Agent 不仅需要知道答案，还要知道下一步怎么做。

典型循环：

Task decomposition → Plan → Decision → Tool Call → Observation → Re-plan

企业 Agent 必须把：

Conversation ≠ Business Execution ≠ Business State ≠ Agent Memory

Agent 可以读取状态、提出 transition、请求 approval、执行 command，但不能靠 prompt 自己宣布“approved”。

### 3.9 Context Engineering / Evidence / Evaluation / Governance

Context Engineering 负责把 Instructions、Knowledge、Memory、State、Tool Results、Evidence 组织成模型当前真正看到的 context。

Evidence / Provenance 解决“为什么这么说”。

Evaluation 解决“Agent 是否正确使用知识、工具、状态和计划”。

Governance 解决“它是否被允许这么做、谁批准、访问了什么、执行了什么”。

## 4. 从 RAG 走向 Agentic Retrieval

传统 RAG：

query → top-k → prompt

成熟 Agent Retrieval：

query understanding → query rewrite / expansion → candidate retrieval → fusion / dedup → rerank → context expansion → evidence pack → agent reasoning → verify / retrieve again if necessary

Candidate Retrieval 可以并行使用：

- lexical
- semantic
- metadata
- graph
- direct source lookup

Context Expansion 可以补：

- parent section
- neighbor propositions
- graph edges
- source evidence

Self-RAG、Contextual Retrieval、GraphRAG、PropRAG 都说明 retrieval 会逐渐从单纯 search 变成 Agent 的 active cognition。

## 5. Knowledge Compilation 是新的战略层

LLM Wiki / OKF 代表了一个重要变化：

传统：source → query → retrieve → synthesize

编译式：source → compile → persistent knowledge → retrieve / navigate

这不是替代 RAG，而是增加：

Source → Knowledge Compilation → Persistent Knowledge Layer → RAG / Graph / Direct Navigation → Agent

适合：

- 重复研究
- 代码库长期工作
- 企业组织知识
- 跨 session Agent

风险：

- stale knowledge
- compression loss
- persisted model error
- contradiction propagation

因此 canonical source 和 provenance 仍必须保留。

## 6. Semantic Layer 是 Enterprise Agent 的另一条主干

对于金融、数据、合规、运营 Agent，单纯 RAG 很难解决业务语义。

建议：

Business Definition → Ontology → Semantic Layer → Data / Knowledge / API → Agent

Agent 不应该自己猜 AUM、Active Client、Net Flow、Eligible Account 的定义，而应该使用企业认可的 semantic definition。

这一点与你正在探索的 Snowflake Semantic Views / Semantic Layer 直接相关。

## 7. Memory 应该建立 Write Policy

长期 Agent Memory 的关键问题不是“存哪里”，而是“什么值得长期保存”。

推荐生命周期：

Observe → Extract → Validate → Store → Retrieve → Use → Reflect → Promote / Update / Forget

重要 memory 应带 provenance 与 confidence。

## 8. Skill 是 Procedural Knowledge 的外化

长期职责分离：

| 层 | 定义 |
|---|---|
| Knowledge | what |
| Skill | how |
| Tool | capability |
| Workflow | enforced sequence |
| Policy | boundary |

这样 Agent 可以自动加载 Skill，又不会把 security boundary 交给 prompt。

## 9. Business State 必须独立于 Agent Context

例如：

- KYC = completed
- Suitability = passed
- Approval = pending
- Trade = not executed

这些是 business state，不是 conversation 或 memory。

推荐：

read state → reason → propose transition → approval → command → execution → observe new state

## 10. Evaluation Roadmap

至少分五层：

| Layer | 关键问题 |
|---|---|
| Knowledge | 覆盖、完整性、时效、来源 |
| Retrieval | recall、precision、ranking、diversity |
| Context | 是否足够、噪声、顺序 |
| Reasoning / Agent | task success、planning、tool use、recovery |
| System | safety、auth、audit、cost、latency |

应增加 Knowledge Use Eval，直接验证 Agent 是否真正使用 external knowledge，而不仅是检索到。

## 11. Governance Roadmap

推荐控制链：

Identity → Authorization → Data Entitlement → Knowledge Retrieval → Tool Authorization → Policy Decision → Approval → Command → Execution → Audit Evidence

核心原则：

- LLM 可以 reason，但不能定义 security boundary。
- Retrieval 不能绕过 Data Entitlement。
- 高风险 action 需要 Policy / Approval。
- Runtime trace 不自动等于 regulatory audit evidence。

## 12. 分阶段 Roadmap

### Phase 0 — Unified Concepts

统一 Knowledge、Memory、Skill、Tool、State、Context、Evidence、Ontology、Protocol、Policy 的边界。

### Phase 1 — Knowledge Foundation

Canonical Source + KnowledgeNode / Ontology + Proposition / Claim + Graph + Retrieval + Evidence + Provenance

这正是当前 agent-knowledge-usage 的阶段。

### Phase 2 — Memory

建立 working / factual / episodic / experiential / procedural memory，并研究 write、promotion、compression、forgetting。

### Phase 3 — Skills / Capability

统一 Global / Team / Project / Member Skill，以及 Tool / MCP / Connector / Script 的 discovery、loading、execution、version、governance。

### Phase 4 — Semantic Layer / Business Ontology

建立企业业务定义、metric semantics、entities、relations、lineage、join path、temporal definitions。

### Phase 5 — Agent Harness

把 Context、Memory、Skills、Tools、State、Planning、Workflow、Sandbox、Observability、Evaluation 组织成统一 Runtime。

### Phase 6 — Multi-Agent / Protocol

A2A、Agent Gateway、delegation、artifact exchange、capability discovery。

### Phase 7 — Adaptive / Self-improving Agents

让 Agent 根据 Evaluation 逐渐优化 retrieval、memory、skills、planning、tool use；进入 post-training / RL 前先建立强 governance。

## 13. 与当前项目群的对应

| 项目 / 方向 | Roadmap 层 |
|---|---|
| ai-interview-questions | Knowledge + Learner Memory + Evaluation |
| agent-knowledge-usage | Knowledge Engineering + RAG + Ontology |
| common-agent-lib | Cross-framework Agent primitives |
| team-member-copilot-agent | Harness + Skills + Team Memory + State |
| copilot-server-agent | Runtime + Sandbox + Tools |
| agentic-data-architect | Ontology + Semantic Layer + Data Agent |
| Workflow DSL | Planning / Workflow / Business State / Policy |
| MCP | Tools / Capability / Protocol |
| A2A | Agent ↔ Agent Protocol |
| LangSmith | Observability / Evaluation / Trace |
| Snowflake Semantic Layer | Ontology / Semantic Layer / Business Knowledge |
| K8S Agent Sandbox | Runtime Isolation / Execution |
| Learner Model | Personalized Memory + Evaluation |

这些并不是互不相关的项目，而是同一张 Agent architecture map 上的不同区域。

## 14. Common Agent Library 应该优先抽什么

优先抽象：

Context、Knowledge Access、Memory、Skill Loader、Tool Contract、Evidence、State、Workflow、Policy、Evaluation、Observability

不要首先抽象具体 Vector DB、Graph DB、Agent framework 或 connector。

Common Library 应定义 capability contracts，而不是锁死基础设施。

## 15. 最值得持续研究的十个问题

1. Knowledge Representation：Source / Proposition / Graph / Summary / Ontology 如何共存？
2. Knowledge Compilation：是否应该从 query-time retrieval 进一步引入 ingestion-time compilation？
3. Memory Policy：Agent 什么应该记住，什么应该忘掉？
4. Context Engineering：如何在 context budget 内组合 Knowledge + Memory + Skill + State？
5. Semantic Layer：企业业务定义如何进入 Agent，而不是让模型猜？
6. Agent Skills：procedural knowledge 如何可复用、可版本化、可治理？
7. Business State：reasoning 如何与真正的 execution 解耦？
8. Evidence / Provenance：重要 claim 如何回到 source？
9. Agent Evaluation：如何评估 knowledge use / tool use / planning / safety？
10. Adaptive Agents：如何积累 knowledge、memory、skill 而不发生污染？

## 16. 最终战略模型

Agent Intelligence = Model Intelligence + External Cognitive Infrastructure

External Cognitive Infrastructure 包括：

Knowledge、Ontology、RAG、Graph、Memory、Skills、Tools、State、Planning、Protocols、Context、Evidence、Policy、Evaluation。

长期真正值得建设的不是“又一个 Agent Framework”，而是一套让不同 Agent 应用共享知识、语义、记忆、能力、状态、工具、证据与治理能力的基础设施。

## 17. 研究后的几个新判断

前面论文与厂商实践放在一起后，Roadmap 的主线已经更清楚：重点不是继续增加 Agent 组件，而是把不同种类的信息放到正确的位置。

### Knowledge 不是一种表示

同一份业务知识可以同时存在为原始文档、semantic object、claim / proposition、graph、summary 和 retrieval index。

它们之间应该是派生关系，而不是互相竞争的 source of truth。

~~~text
Canonical Source
      ↓
Knowledge Representation
      ↓
Derived Views
      ↓
Retrieval / Navigation
      ↓
Context
~~~

真正需要长期保存的是 source、provenance、version、authority 和 scope。

### Context 不是 Knowledge Storage

Knowledge 可以很大，Context 必须小而有目的。

模型当前看到的内容应该是 Knowledge、Memory、Skill、State、Tool Result、Evidence 经过选择后的投影，而不是所有长期资料的简单拼接。

### Memory 不应该变成第二个 Knowledge Base

Knowledge 主要保存领域和世界的长期事实、定义、关系与规则。

Memory 主要保存 Agent、用户、团队过去发生的事情和经验。

如果 Memory 与 Business State 冲突，业务系统应该是权威来源。

### Semantic Layer 是企业 Agent 的关键分界

通用 Agent 可以搜索到 Revenue 相关文档。

企业 Agent 还需要知道 Revenue 的正式定义、计算方式、时间口径、权威来源和适用范围。

因此金融、数据、合规类 Agent 的长期核心，很可能不是更大的 RAG，而是可靠的 Business Semantic Layer。

### 自动发现需要一个验证层

Databricks inferred context、Google enrichment、LLM Wiki 等方向都说明人工维护全部 Knowledge 不现实。

但自动抽取的结果不能直接成为真相。

更稳妥的流程是：

~~~text
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
~~~

这也意味着下一阶段值得研究的对象不只是 Knowledge Retrieval，还有 Knowledge Compilation 和 Knowledge Governance。

### 下一步最值得研究的三个问题

1. 自动发现出来的 business knowledge 怎样经过验证后成为 trusted knowledge。
2. Agent 做决定时，怎样记录它使用的 semantic definition、document、policy 和 permission snapshot。
3. 怎样建立真正的 Knowledge Use Evaluation，而不是只测 retrieval recall 和最终答案。
