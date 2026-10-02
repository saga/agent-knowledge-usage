# AI Agent Knowledge & Capability Roadmap

> 目的：从理论、业界实践和架构战略层面理解并指导一系列 AI Agent 应用、Common Library、Team Agent、Data Agent、Research Agent 和金融服务 Agent 的共同基础。重点不是再做一个 RAG 框架，而是定义 Agent 如何可靠消费企业知识、业务语义、记忆、能力、状态、证据和权限。
>
> 研究日期：2026-10-02
>
> 当前阶段判断：从“Knowledge 组件研究”进入“Knowledge Access + Semantic + Governance”基础设施设计阶段。

---

# 1. 先改变一个认识：Knowledge 不是一个东西

前期 Roadmap 很容易把：

~~~
Knowledge
  ├── RAG
  ├── Graph
  ├── Ontology
  └── Vector Store
~~~

画成一个组件树。

最新的论文、Skill 设计和新增厂商实践表明，这个模型已经不够准确。

企业 Agent 真正面对的是一条 Knowledge Supply Chain：

~~~
Canonical Sources / Systems
          ↓
Knowledge Assets
          ↓
Derived Views / Compilations
          ↓
Knowledge Access
          ↓
Context Assembly
          ↓
Agent Reasoning
          ↓
Tool / Action / Business System
~~~

旁边始终伴随：

~~~
Authority
Permission / Entitlement
Provenance
Freshness
Version
Lifecycle
Evaluation
Audit
~~~

所以：

- RAG 是一种 Knowledge Access 方式；
- Graph 是一种表示 / 导航 View；
- Semantic View 是一种受治理的业务语义 + 查询界面；
- Knowledge Base 很多时候是 retrieval / ingestion configuration；
- Connector / MCP 是能力和访问协议；
- Memory 是带生命周期的 Agent interaction state；
- Context 是当前一次推理对长期信息的有目的投影。

这些不能再当成同一层的 primitive。

---

# 2. 当前最重要的统一模型：四个平面

目前最值得采用的架构不是“一个大 Knowledge Layer”，而是四个平面。

## 2.1 Meaning Plane：业务到底是什么

解决：

> 这个东西在业务上是什么意思？

典型对象：

- Entity
- Metric
- Dimension
- Relation
- Rule
- Condition
- Business Definition
- Policy Reference
- Business Object

这一层对应：

- Snowflake Semantic Views；
- Databricks semantic / inferred context；
- SAP Business Semantics；
- Palantir Ontology；
- Salesforce structured business objects；
- ServiceNow operational context。

Snowflake 当前已经把 semantic business concepts 直接建模成 schema-level Semantic Views，并让 Cortex Agents 以工具方式查询这些逻辑对象；官方文档同时强调 ownership、RBAC、masking、row-access policies 和 CI/CD。

Sources：
- https://docs.snowflake.com/en/user-guide/views-semantic/overview
- https://docs.snowflake.com/en/user-guide/views-semantic/best-practices

---

## 2.2 Evidence Plane：事实和证据是什么

解决：

> 我从哪里知道这件事？

典型对象：

- Source
- Document
- Section
- Proposition / Claim
- Evidence
- Citation
- Provenance
- Version
- Valid Time
- Authority

这一层是 RAG、搜索、知识图谱之外的“证据底座”。

关键原则：

~~~
Source
  ↓
Derived Knowledge
  ↓
Evidence / Provenance
~~~

不能只保存摘要或 embedding，然后删除原始证据。

---

## 2.3 Access Plane：Agent 怎样拿到这些东西

解决：

> 当前这个 Agent、这个用户、这个问题，怎样访问正确的信息？

可能是：

- lexical search；
- semantic retrieval；
- hybrid search；
- Graph navigation；
- structured query；
- semantic query；
- direct source lookup；
- SQL；
- connector；
- MCP resource / tool；
- agentic retrieval。

因此：

~~~
Retrieval
Query
Navigation
Fetch
~~~

应该视为 Knowledge Access modes，而不是四种 Knowledge。

AWS Agentic Retrieval 已经把复杂问题拆解、迭代检索、结果充分性评估、用户上下文和 Memory 放进一次 retrieval flow；这说明 retrieval 本身正在从“top-k search”变成 Agent Access Loop。

Source：
- https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html

Oracle 的 Generative AI Agents 也把 RAG、SQL、Function Calling、Agent-as-a-tool 等访问方式并列为 Agent Tool，而不是要求所有企业数据统一进入一个向量库。

Sources：
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/overview.htm

---

## 2.4 Runtime Cognition Plane：这次到底给模型看什么

解决：

> 长期存在的知识，哪些应该进入当前 context？

输入可能包括：

- Instructions；
- Knowledge；
- Evidence；
- Memory；
- Business State；
- Skill；
- Tool Result；
- Policy Decision；
- User Context；
- Prior Actions。

最终变成：

~~~
Context Assembly
      ↓
Current Context
      ↓
Reasoning
      ↓
Action
~~~

ServiceNow 的 direct structured context + AI Search / Knowledge Graph、AWS 的 agentic retrieval + memory，以及 Microsoft 的 knowledge source + connector 都说明：

> Context Assembly 是独立责任，不应该隐藏在 RAG 函数内部。

---

# 3. Knowledge 最好拆成三个生命周期，而不是一个存储

最新资料进一步支持：

~~~
Canonical
   ↓
Compiled
   ↓
Runtime
~~~

## 3.1 Canonical Knowledge

权威来源：

- database；
- semantic model；
- enterprise application；
- policy；
- official document；
- approved procedure。

这里解决：

> 真正的 source of truth 是谁？

---

## 3.2 Compiled / Derived Knowledge

由 canonical source 产生：

- vector index；
- full-text index；
- graph；
- search index；
- semantic view；
- summarized representation；
- extracted proposition；
- inferred ontology candidate；
- cached context；
- retrieval index。

这些都是 Derived Views，不是新的 source of truth。

Salesforce Data Library 会自动完成数据流、对象映射、search index 和 retriever 的配置；Oracle 也把 Data Source、Knowledge Base、ingestion job 和 RAG tool 分开管理。它们共同说明“Knowledge Base”更像一个受治理的 derived/access configuration，而不是企业知识本体。

Sources：
- https://help.salesforce.com/s/articleView?id=sf.data_library_concept.htm&language=en_US&type=5
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_data.htm&language=en_US&type=5
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/knowledge-bases.htm

---

## 3.3 Runtime Knowledge

Agent 真正得到的：

- selected proposition；
- semantic definition；
- query result；
- graph neighborhood；
- source evidence；
- memory；
- state；
- policy decision。

Runtime knowledge 是：

~~~
Long-lived Knowledge
      ↓
Selection
      ↓
Permission
      ↓
Context
~~~

而不是把整个 Knowledge Store 直接塞进模型。

---

# 4. 一个更准确的 Knowledge Architecture

当前建议把 Agent Knowledge 看成：

~~~
                           ┌────────────────────┐
                           │ Canonical Sources  │
                           │ DB / Docs / Apps   │
                           │ Policies / APIs    │
                           └─────────┬──────────┘
                                     │
                           extract / model / verify
                                     │
              ┌──────────────────────┴──────────────────────┐
              │                                             │
      ┌───────▼────────┐                           ┌────────▼────────┐
      │ Meaning Plane  │                           │ Evidence Plane  │
      │ Entity         │                           │ Document        │
      │ Metric         │                           │ Proposition     │
      │ Relation       │                           │ Claim           │
      │ Rule           │                           │ Citation        │
      │ Definition     │                           │ Provenance      │
      └───────┬────────┘                           └────────┬────────┘
              │                                             │
              └──────────────────┬──────────────────────────┘
                                 │
                         Derived Views
                                 │
             ┌───────────────────┼─────────────────────┐
             │                   │                     │
          Search              Graph               Semantic Query
          Vector              Index               Structured SQL
             │                   │                     │
             └───────────────────┼─────────────────────┘
                                 │
                        Knowledge Access
                                 │
                    Identity / Entitlement
                    Authority / Freshness
                    Version / Provenance
                                 │
                        Context Assembly
                                 │
              ┌──────────────────┼────────────────────┐
              │                  │                    │
          Knowledge           Memory              Business State
              │                  │                    │
              └──────────────────┼────────────────────┘
                                 │
                               Agent
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                 Skills                   Tools / MCP
                    │                         │
                    └────────────┬────────────┘
                                 │
                              Action
                                 │
                         Business Systems
~~~

这张图比“Knowledge → RAG → Agent”更接近目前不同厂商实际暴露出来的边界。

---

# 5. 一个新的关键抽象：Knowledge Access

目前 Common Agent Library 最值得抽取的可能不是 KnowledgeBase，而是：

> Knowledge Access Contract

因为不同厂商虽然存储方式完全不同，但 Agent 最终都在做：

~~~
identify user / agent
       ↓
select access path
       ↓
retrieve / query / navigate / fetch
       ↓
apply entitlement
       ↓
return evidence + provenance + authority
       ↓
assemble context
~~~

一个候选 contract 可以是：

~~~
KnowledgeAccessRequest
- subject
- question / query
- domain
- accessMode
- filters
- freshnessRequirement
- purpose
- maxContext

KnowledgeAccessResult
- items
- sourceRefs
- authority
- provenance
- version
- asOf
- accessDecision
- retrievalMode
- limitations
~~~

这不是要求现在就实现完整 schema，而是建议把 Common Library 的接口设计围绕这个责任边界，而不是围绕 Vector DB。

---

# 6. Knowledge Base 不应该成为 Common Primitive

最新业界资料已经足以支持这个调整。

不同厂商中的 Knowledge Base 实际承担的职责不同：

| Product term | 更接近什么 |
|---|---|
| Snowflake Semantic View | Business semantics / query view |
| Salesforce Data Library | Index / retriever configuration |
| Oracle Knowledge Base | RAG retrieval boundary |
| IBM knowledge_bases | Agent knowledge provider |
| Microsoft Knowledge Source | Access / grounding source |
| Palantir Ontology | Operational model |
| ServiceNow Knowledge Graph | Structured operational context |
| AWS Knowledge Base | Retrieval source |
| OpenAI File/Search | Knowledge access capability |

因此 Common Library 不应定义：

~~~
UniversalKnowledgeBase
~~~

而应定义：

~~~
Knowledge Source
Knowledge Asset
Knowledge View
Knowledge Access
Context Item
Evidence
~~~

这些对象如果最后被证明确实稳定，再进入真正的 type/schema。

---

# 7. Knowledge Asset 的建议最小集合

当前可以暂时收敛到：

| Asset | 解决的问题 |
|---|---|
| Source | 真相在哪里 |
| Definition | 业务概念是什么意思 |
| Entity | 业务对象是谁 |
| Relation | 对象如何关联 |
| Metric | 如何计算 / 口径是什么 |
| Rule | 什么条件成立 |
| Proposition / Claim | 一个可验证的事实 |
| Evidence | 为什么相信 |
| Procedure / Skill | 怎么做 |
| Memory | 过去发生了什么 / 学到了什么 |
| State | 当前业务处于什么状态 |

但最后三项故意保持不同：

~~~
Knowledge
   ≠
Skill
   ≠
Memory
   ≠
Business State
~~~

---

# 8. 一个更重要的边界：Semantic Model ≠ Operational Model

Palantir 是非常有价值的反例。

Palantir Ontology 可以把：

- objects；
- relationships；
- logic；
- actions；
- security policies

组合成 operational model，并通过 Ontology MCP 暴露给外部 Agent。

Sources：
- https://www.palantir.com/docs/foundry/ontology-mcp
- https://www.palantir.com/docs/foundry/ontology-mcp/getting-started

这说明：

> 在成熟企业平台中，语义模型可能继续向“可执行业务世界模型”发展。

但 Common Agent Library 不应该因此把：

~~~
Entity + Relation + State + Action + Policy
~~~

强行做成一个 Universal Ontology。

更合适的是：

~~~
Semantic Model
    ↓
Operational Model
    ↓
Action / State
~~~

Common Library 负责 access contract。

具体业务平台是否把这些放在同一个 Ontology 中，由 provider 决定。

---

# 9. Memory 的位置也需要调整

以前 Roadmap 把 Memory 当作 Knowledge 的一个并列组件。

现在可以更准确地说：

> Memory 是另一条长期信息生命周期，但可以被同一个 Knowledge Access / Context Assembly 过程消费。

AWS 已经允许 Agentic Retrieval 同时使用 Knowledge、Memory、User Context 和 Policy；AgentCore Memory 又区分 short-term session history 与 long-term retention。

Sources：
- https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html

NVIDIA NeMo 也把 Memory 设计成独立 provider，并提供 automatic memory wrapper，让不同 Agent runtime 可以外挂 memory backend。

Sources：
- https://docs.nvidia.com/nemo/agent-toolkit/latest/build-workflows/memory.html
- https://docs.nvidia.com/nemo/agent-toolkit/latest/extend/memory.html

因此：

~~~
Knowledge Source
      +
Memory Provider
      +
Business State
      ↓
Context Assembly
~~~

而不是：

~~~
Everything → One Memory Store
~~~

---

# 10. Memory 必须有 Write Policy

长期 Memory 的核心已经不是：

> 怎么存？

而是：

> 什么值得写进去？

建议保持：

~~~
Observe
  ↓
Extract
  ↓
Validate
  ↓
Assign Scope
  ↓
Store
  ↓
Retrieve
  ↓
Use
  ↓
Promote / Update / Forget
~~~

至少带：

- owner / subject；
- scope；
- source；
- confidence；
- createdAt；
- lastVerified；
- validFrom / validTo；
- memory type；
- promotion state。

尤其：

~~~
Memory
  ≠
Business Truth
~~~

当 Memory 与业务系统冲突时，业务系统仍然是权威来源。

---

# 11. Knowledge Compilation 应成为一条独立研究主线

新的厂商实践已经让这个方向从“有趣想法”变成明显的工程趋势。

自动发现 / 自动抽取现在可以出现在：

- semantic model generation；
- inferred context；
- connector ingestion；
- Data Library indexing；
- memory extraction；
- ontology generation。

但：

~~~
Extracted
≠
Trusted
~~~

因此更合理的路线：

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
Compile Views
  ↓
Retrieve
~~~

这将成为一个独立的 Knowledge Engineering lifecycle。

---

# 12. Authority 应成为一等概念

不同来源之间出现冲突时，单纯的 retrieval score 不够。

例如：

~~~
Document A
Metric Definition B
CRM Record C
Memory D
User Statement E
LLM General Knowledge F
~~~

它们即使都被检索到，也不能视为同等可信。

因此未来 Knowledge Access 必须考虑：

- authoritative source；
- certified definition；
- derived data；
- inferred knowledge；
- user-provided information；
- memory；
- model prior。

一个候选排序：

~~~
Certified / Authoritative
      ↓
Verified
      ↓
Derived
      ↓
Inferred
      ↓
User-provided
      ↓
Memory
      ↓
Model prior
~~~

这只是默认研究模型，不是所有业务场景都必须采用固定排序。

---

# 13. Permission 不是 Knowledge 旁边的一根“安全线”

新的 Microsoft、AWS、Palantir 等实践更加明确地说明：

> 权限必须进入 Knowledge Access 本身。

Microsoft Copilot connectors 会把 source-level permissions 带入 grounding；AWS Agentic Retrieval 的 user context 可以用于 access-control filtering；Palantir Ontology MCP 使用 application restrictions 和 permissions 控制外部 Agent 能访问哪些 ontology resources。

Sources：
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-connectors
- https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html
- https://www.palantir.com/docs/foundry/ontology-mcp

因此不能：

~~~
Search
 ↓
拿到全部结果
 ↓
Prompt 再过滤
~~~

应该：

~~~
Identity
 ↓
Entitlement
 ↓
Knowledge Access
 ↓
Context
~~~

尤其在金融服务中：

> Retrieval 本身不能成为 Data Entitlement 的绕过路径。

---

# 14. Provenance 也应该随 Access Result 一起走

当前报告以前把 Provenance 当成 Knowledge metadata。

现在建议更进一步：

> Provenance 是 Runtime Knowledge Access 的输出的一部分。

例如一个 Context Item 至少能够回答：

~~~
What?
Why this item?
Where from?
Which version?
As of when?
Who is authoritative?
What permission allowed it?
How was it retrieved?
~~~

这样未来才能回答：

- Agent 为什么知道这个？
- 用的是哪版业务定义？
- 当时用户有哪些权限？
- 哪个 document / record 支撑？
- 哪个 semantic view 被使用？
- 哪个 policy snapshot 生效？

---

# 15. Context Engineering 应从“Prompt 优化”升级成“Knowledge Projection”

Context 不只是 prompt 拼装。

可以定义：

~~~
Knowledge / Memory / State / Skill / Tool Results
                     ↓
             Context Selection
                     ↓
             Context Ordering
                     ↓
             Authority Resolution
                     ↓
             Evidence Packaging
                     ↓
                Model Context
~~~

所以 Context Engineering 的核心问题应该是：

> 为什么这一次只给模型这些信息，而不是另外那些？

这也与 ServiceNow direct context + dynamic retrieval、AWS agentic retrieval、Snowflake semantic views 等产品实践相互印证。

---

# 16. Evaluation Roadmap 要升级

原来的：

~~~
Knowledge
Retrieval
Context
Agent
System
~~~

仍然正确，但不够细。

建议新增：

| Eval Layer | 要回答的问题 |
|---|---|
| Source | Source 是否正确、完整、最新 |
| Representation | 转换成 chunk / summary / graph / semantic view 后保留了多少关键结构 |
| Semantic | 是否使用正式业务定义 |
| Access | 找到的是否是正确来源 |
| Authority | 是否选了正确权威来源 |
| Entitlement | 用户不该看到的是否被过滤 |
| Evidence | 结论能否回到 source |
| Context | 是否足够且没有明显噪声 |
| Behavioral Fidelity | 不依赖文字解释时，Agent 的判断和行为是否仍与知识一致 |
| Counterfactual Fidelity | 关键条件变化时，Agent 是否产生应该发生的判断变化 |
| Memory | 是否保存 / 使用了错误记忆 |
| State | 是否理解当前业务状态 |
| Agent | 是否完成任务 |
| Action | 是否正确执行 |
| System | safety / auth / audit / cost / latency |

尤其要新增一个：

## Knowledge Use Evaluation

不是：

> “检索到了吗？”

而是：

> “当正式业务定义存在时，Agent 是否真的使用了它？”

这还需要考虑一个更深的问题：**最终答案可能只是 richer knowledge state 的低带宽投影。**

Hinton 等人在知识蒸馏研究中把 soft output 中超出 hard label 的关系和相对概率称为 dark knowledge；Polanyi 的 tacit knowledge 则说明部分 know-how 难以完整外显。因此 Knowledge Use Evaluation 不能只检查答案文本，还应测试 alternative / uncertainty、例外处理、边界条件以及 counterfactual behavior。

这不是说 Dark Knowledge、Tacit Knowledge 和 Parametric Knowledge 是同一概念，而是它们共同说明：**Answer Correctness 不是 Knowledge Fidelity 的充分指标。**

例如：

~~~
Question
 ↓
Agent has model prior
+
Enterprise definition
 ↓
Did it use enterprise definition?
 ↓
Did it cite / identify authority?
 ↓
Did it derive answer consistently?
~~~

这比单独测 Recall@K 更贴近企业 Agent。

---

# 17. Governance Roadmap 重新组织

建议把治理链更新为：

~~~
Identity
  ↓
Authorization
  ↓
Data / Knowledge Entitlement
  ↓
Knowledge Access
  ↓
Authority / Provenance
  ↓
Context Assembly
  ↓
Agent Reasoning
  ↓
Policy Decision
  ↓
Approval
  ↓
Command
  ↓
Execution
  ↓
Audit Evidence
~~~

注意：

~~~
Knowledge Access
≠
Tool Authorization
≠
Business Action Authorization
~~~

Knowledge 可以授权“看见”。

Tool 可以允许“调用”。

Policy / Approval 决定“是否允许执行”。

不要把这三件事塞进同一个 permission flag。

---

# 18. Skill / Tool / Protocol 的位置

最新资料并没有推翻原来的：

~~~
Knowledge = what
Skill = how
Tool = capability
Workflow = enforced sequence
Policy = boundary
~~~

反而进一步支持它。

Anthropic Skill 的 progressive disclosure 说明 procedural knowledge 可以被外置、发现、加载和执行；NVIDIA NeMo 也把 Agent、Retriever、Memory provider 等能力做成可插拔组件。

Sources：
- https://github.com/anthropics/skills
- https://docs.nvidia.com/nemo/agent-toolkit/latest/components/agents/index.html
- https://docs.nvidia.com/nemo/agent-toolkit/latest/extend/custom-components/adding-a-retriever.html

因此 Common Library 仍然应该把：

~~~
Skill
Tool
Connector
MCP
A2A
~~~

作为 capability / protocol 层，而不是 Knowledge storage。

---

# 19. RAG / Graph / Semantic View 的新定位

这一部分建议正式固定下来，避免以后概念再次膨胀。

| 名称 | 新定位 |
|---|---|
| RAG | Knowledge Access / grounding strategy |
| Vector Store | Derived View / index |
| Full-text Search | Derived View / access |
| Graph | Representation / navigation View |
| GraphRAG | Graph + Retrieval access strategy |
| Semantic View | Business meaning + structured query View |
| Knowledge Base | Provider-specific retrieval / ingestion boundary |
| Connector | External source integration |
| MCP | Capability / resource access protocol |
| A2A | Agent ↔ Agent protocol |
| Memory | Stateful external cognition |
| Context | Runtime projection |

这样以后不再把“Graph 是 Knowledge primitive”之类的概念混在一起。

---

# 20. Common Agent Library：现在应该抽什么

新的优先级和原 Roadmap 不同。

## P0：最值得抽

### 1. Knowledge Access

统一：

~~~
search
query
navigate
fetch
~~~

### 2. Evidence / Provenance

统一：

~~~
sourceRef
authority
version
asOf
citation
provenance
~~~

### 3. Context Item

把：

~~~
content
source
authority
version
scope
access decision
~~~

作为 runtime knowledge 的最小可审计单位。

### 4. Provider Adapter

例如：

~~~
SnowflakeSemanticProvider
DatabricksProvider
SearchProvider
GraphProvider
DocumentProvider
MemoryProvider
~~~

底层可以换，Agent contract 不变。

---

# 21. P1：Semantic Access，而不是先做自己的 Semantic DB

目标：

~~~
BusinessEntity
Metric
Relation
Definition
Rule
~~~

但先通过 Provider 接入：

- Snowflake Semantic Views；
- Databricks；
- Palantir Ontology；
- SAP Business Semantics；
- Salesforce structured data；
- 其他企业 semantic layer。

不要现在自己实现一个 Universal Ontology Database。

Snowflake 当前已经把语义对象做成受治理 schema object，并支持查询、共享和审计；这说明 Common Library 更适合定义接入 contract，而不是重新造一套 semantic persistence。

Sources：
- https://docs.snowflake.com/en/user-guide/views-semantic/overview
- https://docs.snowflake.com/en/user-guide/views-semantic/using

---

# 22. P2：Knowledge Compilation

建立：

~~~
Source
 ↓
Candidate
 ↓
Validation
 ↓
Authority
 ↓
Publish
 ↓
Derived Views
~~~

研究：

- automatic extraction；
- inferred knowledge；
- contradiction detection；
- promotion；
- invalidation；
- versioning；
- human review。

这一阶段比“再加一个向量数据库”更值得投入。

---

# 23. P3：Memory Provider

统一：

~~~
Memory
 ├── Working
 ├── Factual
 ├── Episodic
 ├── Experiential
 └── Procedural
~~~

重点不是统一 backend，而是：

~~~
Memory Write Policy
Memory Read Policy
Memory Scope
Memory Provenance
Memory Promotion
Memory Forgetting
~~~

---

# 24. P4：Context Assembly

建立统一机制：

~~~
Instructions
+
Knowledge
+
Evidence
+
Memory
+
State
+
Skills
+
Tool Results
+
Policy
↓
Context
~~~

尤其建立：

- source authority resolution；
- conflict resolution；
- freshness filtering；
- context budget；
- evidence packaging。

---

# 25. P5：Capability / Skill / Tool / Protocol

继续统一：

~~~
Skill
Tool
Connector
MCP
A2A
~~~

但保持责任边界：

~~~
Skill = procedure
Tool = external capability
MCP = access protocol
A2A = agent protocol
Policy = boundary
~~~

---

# 26. P6：Business State / Workflow / Execution

这部分继续沿用现有 Agent 架构研究：

~~~
Read state
  ↓
Reason
  ↓
Propose transition
  ↓
Approval
  ↓
Command
  ↓
Execution
  ↓
Observe new state
~~~

不要让：

~~~
Conversation
Memory
Prompt
~~~

冒充：

~~~
Business State
~~~

---

# 27. P7：Knowledge Use Evaluation

建立至少四类测试：

### 1. Semantic correctness

是否用了正确业务定义？

### 2. Evidence correctness

是否能够回到权威 source？

### 3. Access correctness

用户是否只看到被授权的数据？

### 4. Use correctness

Agent 是否真的使用了 retrieved / semantic knowledge，而不是用模型先验回答？

### 5. Behavioral / Counterfactual correctness

当外部知识改变、删除或替换时，Agent 的判断是否发生正确变化？

最后再测：

- task success；
- tool use；
- recovery；
- latency；
- cost。

当前尚无统一的“Knowledge Loss Rate”。更适合研究的是 Knowledge Fidelity 向量：Source Coverage、Representation Fidelity、Retrieval Recall、Context Fidelity、Knowledge Use、Conflict Resolution、Evidence Faithfulness、Behavioral Fidelity。

---

# 28. P8：Multi-Agent / Adaptive

最后再进入：

~~~
A2A
Delegation
Shared Knowledge
Shared / Scoped Memory
Agent Registry
Capability Discovery
Adaptive Learning
~~~

原因很简单：

> 如果 Knowledge Access、Authority、State、Policy 和 Evaluation 还没有稳定，Multi-Agent 只会把问题复制到更多 Agent。

---

# 29. 当前项目群重新定位

| 项目 / 方向 | 当前最合适的位置 |
|---|---|
| agent-knowledge-usage | Knowledge Architecture / Research / Evidence / Primitive Design |
| common-agent-lib | Knowledge Access / Evidence / Context / Memory / Capability contracts |
| agentic-data-architect | Semantic Layer / Business Model / Knowledge Authoring |
| team-member-copilot-agent | Context / Memory / Skills / Team Capability / Agent Harness |
| copilot-server-agent | Runtime / Execution / Sandbox / Tools |
| Workflow DSL | Business State / Workflow / Policy / Execution |
| MCP | Capability / Resource Access Protocol |
| A2A | Agent ↔ Agent Protocol |
| LangSmith | Observability / Evaluation / Trace |
| Snowflake Semantic Views | Semantic Provider / Business Definition source |
| K8S Agent Sandbox | Execution Isolation |
| Cloudflare Sandbox | Execution Provider / Validation Environment |
| Learner Model | Personalized Memory + Evaluation |
| NotebookLM / Gemini Notebook | Knowledge Research / Source-grounded synthesis provider |

所以这些项目不是平行发展，而是：

~~~
agent-knowledge-usage
        ↓
Common Agent primitives
        ↓
┌───────────────┬────────────────┬──────────────────┐
│               │                │
Data Agent    Team Agent     Research Agent
│               │                │
Semantic       Memory         Knowledge
Layer          Skills         Evidence
│               │                │
└───────────────┴────────────────┴──────────────────┘
        ↓
Common Agent Runtime / Governance
~~~

---

# 30. 当前阶段不应该做什么

为了避免继续过度设计，目前明确不做：

### 不做 Universal Knowledge Store

不建设一个新的：

- vector DB；
- graph DB；
- document DB；
- all knowledge database。

### 不做 Universal Ontology

先接现有 semantic / ontology provider。

### 不做 Universal Search API

searchKnowledge() 过于粗糙。

应该保留：

~~~
search
query
navigate
fetch
~~~

不同 access mode。

### 不把 Memory 合并进 Knowledge

同一个 Context 可以消费二者，但生命周期不同。

### 不把 Policy 写进 Prompt

Policy 必须位于 runtime / control plane。

### 不把 MCP 当 Knowledge

MCP 是 access protocol。

### 不把 Observability 当 Audit Evidence

Trace 是运行观察；Regulatory Audit Evidence 需要明确的证据结构和保留策略。

---

# 31. 分阶段 Roadmap

## Phase 0 — Unified Concepts

状态：基本完成，持续维护。

统一：

- Knowledge；
- Evidence；
- Semantic；
- Memory；
- Skill；
- Tool；
- State；
- Context；
- Policy；
- Evaluation。

当前 repo 的 Skills 和研究文档已经形成这一层基础。

---

## Phase 1 — Knowledge Access Foundation

状态：现在应该进入这一阶段。

优先建立：

~~~
KnowledgeSource
KnowledgeAccess
KnowledgeItem / KnowledgeAsset
Evidence
ContextItem
Provider Adapter
~~~

重点不是实现 backend，而是稳定 contract。

首先选择 2–3 个差异明显的 provider 做验证：

- Snowflake Semantic View；
- document/search provider；
- operational / ontology provider。

---

## Phase 2 — Knowledge Compilation & Lifecycle

研究并验证：

~~~
Source
→ Extract
→ Infer
→ Validate
→ Authority
→ Publish
→ Invalidate / Update
~~~

重点：

- provenance；
- version；
- freshness；
- contradiction；
- authority；
- human review；
- derived view regeneration。

---

## Phase 3 — Business Semantic Layer

围绕：

~~~
Entity
Metric
Relation
Definition
Rule
~~~

构建 provider-independent contract。

先消费已有：

- Snowflake；
- Databricks；
- Palantir；
- SAP；
- Salesforce；
- 其他企业 semantic systems。

---

## Phase 4 — Memory

研究：

~~~
working
factual
episodic
experiential
procedural
~~~

以及：

- memory write；
- promotion；
- forgetting；
- compression；
- conflict with authoritative sources。

---

## Phase 5 — Context Engineering

把：

~~~
Knowledge
Evidence
Memory
State
Skill
Tool Result
Policy
~~~

统一组织到 runtime Context。

核心指标从：

~~~text
“How much did we retrieve?”
~~~

转向：

~~~text
“Did we give the model the right information for this decision?”
~~~

---

## Phase 6 — Capability / Skill / Workflow

完善：

~~~
Skill
Tool
MCP
A2A
Workflow
Business State
~~~

重点是 capability discovery、execution contract 和 governance。

---

## Phase 7 — Evaluation / Governance

形成：

~~~
Knowledge correctness
+
Semantic correctness
+
Access correctness
+
Evidence correctness
+
Knowledge-use correctness
+
Task success
+
Safety
+
Audit
~~~

---

## Phase 8 — Multi-Agent / Adaptive Agent

最后进入：

- A2A；
- delegation；
- shared context；
- shared / scoped memory；
- agent registry；
- self-improvement；
- adaptive retrieval / skill / planning。

---

# 32. 最值得持续研究的十个问题

新的材料使原来的十个问题需要重新排序。

## 1. Knowledge Access Contract

一个 Agent 如何以统一方式访问：

- Search；
- Semantic Query；
- Graph；
- Direct Source；
- SQL；
- MCP Resource？

## 2. Authority

多个来源冲突时：

> 谁才是真相？

## 3. Knowledge Compilation

怎样从：

~~~
Document / Data / Interaction
~~~

自动得到：

~~~
Candidate Knowledge
~~~

并经过验证后成为 trusted knowledge？

## 4. Semantic Layer

怎样让企业正式定义真正进入 Agent，而不是只作为另一个 RAG corpus？

## 5. Context Assembly

如何决定：

> 这一次到底给模型看什么？

## 6. Knowledge Use Evaluation

怎样测：

> Agent 真正用了 external knowledge，而不是用模型先验猜对了？

## 7. Memory Governance

怎样让长期 Memory：

- 有用；
- 不污染；
- 不越权；
- 不覆盖 authoritative data。

## 8. Evidence / Provenance

怎样让每个 load-bearing decision 都能回到：

~~~
source
version
authority
permission
~~~

## 9. Business State

怎样让：

~~~
reasoning
~~~

和：

~~~
execution
~~~

之间有稳定的 State / Command / Approval 边界？

## 10. Adaptive Agent

如何让 Agent 累积：

~~~
knowledge
memory
skills
retrieval strategies
~~~

而不会发生：

~~~
self-reinforcing error
stale propagation
privilege drift
knowledge pollution
~~~

---

# 33. 最终战略模型

以前可以概括为：

~~~
Agent Intelligence
=
Model Intelligence
+
External Cognitive Infrastructure
~~~

这个结论仍然成立，但现在需要进一步具体化。

更准确的是：

~~~
Agent Intelligence
=
Model
+
Knowledge Access
+
Semantic Model
+
Evidence
+
Memory
+
Context Assembly
+
Capability
+
Business State
+
Policy
+
Evaluation
~~~

而 External Cognitive Infrastructure 的核心不再是“有多少组件”，而是：

> 能否让 Agent 在正确的时间，以正确的权限，获得正确的知识，并且知道这些知识来自哪里、适用于什么时候、由谁认可。

这是企业 Agent Knowledge 真正的基础设施问题。

---

# 34. 当前 Roadmap 最重要的三个结论

### 结论 1：从“Knowledge Store”转向“Knowledge Access”

企业 Agent 最终不是问：

> 我的知识库在哪里？

而是问：

> 对这个用户、这个任务、这个时间点，什么信息可以被可靠地访问？

### 结论 2：从“RAG-first”转向“Semantic + Evidence + Access”

企业 Agent 最终至少需要两条知识主干：

~~~
Business Meaning
      +
Evidence
      ↓
Knowledge Access
      ↓
Context
~~~

RAG 仍然重要，但只是 Evidence / Document Access 的一种实现。

### 结论 3：从“组件建设”转向“责任边界建设”

当前最应该抽的是：

~~~
Who owns truth?
Who defines meaning?
Who provides access?
Who enforces entitlement?
Who supplies evidence?
Who assembles context?
Who owns business state?
Who authorizes action?
Who evaluates the result?
~~~

一旦这些责任边界稳定，Cloud / Database / Vector / Graph / MCP / Agent Framework 都只是 provider 或 implementation。

---

# 35. 研究依据

## Core research

- Externalization in LLM Agents: https://arxiv.org/abs/2604.08224
- Memory in LLM-based Agents: https://arxiv.org/abs/2512.13564
- Knowledge Boundary / LLM Knowledge research：见 学术论文/

## Core industry evidence

### Snowflake
- https://docs.snowflake.com/en/user-guide/views-semantic/overview
- https://docs.snowflake.com/en/user-guide/views-semantic/best-practices
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-manage

### AWS
- https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html

### Microsoft
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-connectors

### Salesforce
- https://help.salesforce.com/s/articleView?id=ai.agent_parent_data.htm&language=en_US&type=5
- https://trailhead.salesforce.com/content/learn/modules/grounding-an-agent-with-data/learn-the-basics-of-grounding
- https://help.salesforce.com/s/articleView?id=sf.data_library_concept.htm&language=en_US&type=5

### Oracle
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/knowledge-bases.htm
- https://docs.oracle.com/en-us/iaas/Content/generative-ai-agents/sql-tool.htm

### Palantir
- https://www.palantir.com/docs/foundry/ontology-mcp
- https://www.palantir.com/docs/foundry/ontology-mcp/getting-started

### NVIDIA
- https://docs.nvidia.com/nemo/agent-toolkit/latest/components/agents/index.html
- https://docs.nvidia.com/nemo/agent-toolkit/latest/build-workflows/memory.html
- https://docs.nvidia.com/nemo/agent-toolkit/latest/extend/memory.html
- https://docs.nvidia.com/nemo/agent-toolkit/latest/extend/custom-components/adding-a-retriever.html

## Repository industry research

详细厂商证据继续保留在：

业界实践/

包括：

- Databricks；
- Google；
- OpenAI；
- Anthropic；
- AWS；
- Microsoft；
- Salesforce；
- SAP；
- ServiceNow；
- Palantir；
- IBM；
- Oracle；
- NVIDIA；
- Snowflake。

---

# 36. 最终判断

当前 agent-knowledge-usage 不应该继续沿着：

~~~
更多 RAG
更多 Vector DB
更多 Graph
更多 Knowledge Base
~~~

这条路扩张。

真正应该形成的是：

~~~
Canonical Knowledge
      ↓
Semantic / Evidence Model
      ↓
Derived Views
      ↓
Knowledge Access
      ↓
Permission + Authority + Provenance
      ↓
Context Assembly
      ↓
Agent
      ↓
Capability / State / Action
      ↓
Evaluation
~~~

其中：

Knowledge Base 是实现细节。

RAG 是访问策略。

Graph 是 View。

Memory 是另一条生命周期。

Semantic Layer 是业务意义。

Evidence 是可信依据。

Context 是运行时投影。

Policy 是边界。

Business State 是业务事实。

Common Agent Library 真正应该统一的是这些责任边界和 access contracts，而不是统一所有底层技术。
