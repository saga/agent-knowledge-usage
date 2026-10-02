---
name: industry-practice-research
description: 研究云厂商、企业软件厂商、Agent/AI 平台厂商和大型互联网公司如何抽象、保存、检索、使用和治理企业业务知识与 Agent Knowledge。当用户要求业界实践、大厂怎么做或厂商对比时使用。
metadata:
  kind: capability
---

# Industry Practice Research

## 目标

不要只比较产品 feature，而要回答：

Knowledge 是什么？
怎么表示？
保存在哪里？
谁拥有它？
Agent 怎么获取？
什么时候进入 context？
权限在哪里检查？
怎么保证 freshness 和 provenance？

## 研究对象

### 不允许固定厂商白名单

研究对象不能长期固定成 Snowflake、Databricks、Google、OpenAI、Anthropic 五家。

这五家可以作为初始 seed，但**每次新的业界研究都必须做 vendor expansion**。研究结果如果连续多次只来自同一批厂商，说明研究偏倚，需要主动补充新的厂商、不同产品类别或不同架构路线。

### Vendor Expansion 的最小规则

每次涉及“业界、大厂、企业实践、行业趋势、怎么做”的研究：

1. 先从当前已有厂商集合之外寻找候选；
2. 至少覆盖 **3 个新增厂商或新厂商类别**，除非问题本身明显只涉及某一特定生态；
3. 优先选择不同的架构路线，而不是只增加同类 SaaS 产品；
4. 至少包含一种：
   - Cloud / infrastructure vendor；
   - Enterprise application / business platform vendor；
   - Data / AI platform vendor；
   - 或大型互联网 / AI infrastructure vendor；
5. 已有厂商如果已经能充分回答问题，可以保留，但不能让它们占据全部 primary evidence；
6. 对“行业共同模式”的结论，优先要求来自不同厂商类别，而不是同一生态中的多个产品。

### 候选厂商池只作为搜索起点，不是白名单

可以考虑但不应机械遍历：

- AWS
- Microsoft
- IBM
- Oracle
- Salesforce
- ServiceNow
- SAP
- Palantir
- NVIDIA
- Alibaba Cloud
- Tencent
- 百度
- Adobe
- Cisco
- Workday
- Atlassian
- Cloudflare
- Cohere
- Mistral
- Meta
- 其他在目标问题上有正式产品、公开 architecture、source code、customer engineering 或 research evidence 的公司

是否纳入，以**问题相关性 + 一手证据质量**决定，而不是“公司名气”。

## Vendor Discovery Protocol

每次研究开始前记录：

~~~text
Seed Vendors:
Existing Vendors:
New Vendor Candidates:
Selected New Vendors:
Why Selected:
Excluded Candidates:
Why Excluded:
Architecture Diversity:
Evidence Diversity:
~~~

### 候选厂商怎么找

优先按“架构问题”搜索，而不是直接搜索“某某公司 knowledge”。

例如研究 Agent Knowledge 时，不只搜：

~~~text
OpenAI knowledge
Anthropic knowledge
Google agent knowledge
~~~

还要搜：

~~~text
enterprise agent knowledge graph
agent semantic layer
agent memory service
enterprise grounding permissions
agent ontology
agentic retrieval
AI search enterprise permissions
agent knowledge lifecycle
business semantics for agents
agent governance knowledge access
~~~

然后从结果中反向发现新的厂商。

### Vendor Diversity Check

在正式形成 cross-vendor conclusion 前，检查：

| Dimension | Requirement |
|---|---|
| Vendor count | 至少 5 家，除非研究问题很窄 |
| New vendors | 至少 3 家不是上一轮固定集合 |
| Vendor categories | 至少 2 类 |
| Primary sources | 尽可能直接来自 vendor / source code |
| Architecture diversity | 不要全部来自同一种平台模型 |
| Counterexamples | 至少主动寻找 1 个反例或明显不同路线 |

如果达不到，不要把结论写成“行业普遍”。

## 每家公司统一拆成七个问题

### 1. Abstraction
业务知识被抽象成什么？
例如 semantic view、metric、ontology、entity、relationship、document、vector store、skill、memory。

### 2. Representation
实际保存成什么？
例如 database object、YAML / JSON、graph、vector index、filesystem、metadata、external application storage。

### 3. Retrieval / Access
Agent 如何获得？
例如 Search、RAG、SQL generation、Graph traversal、Tool、MCP、File Search。

### 4. Runtime Use
什么时候进入 Agent？
例如 prompt construction、tool call、retrieval result、context assembly、planning、workflow step。

### 5. Governance
检查：
- permission
- entitlement
- policy
- certification
- audit
- tenancy

### 6. Freshness / Provenance
检查：
- source
- lineage
- updated time
- version
- verification
- authority

### 7. Limitations
明确：
- 没解决什么
- 强依赖什么平台
- 哪些能力仍需要外部系统
- 哪些结论只是产品定位而不是成熟度证明

## 证据纪律

优先使用官方 docs、官方技术博客、官方 architecture / API docs、官方 source code。

新闻和普通博客主要用于发现线索。

同时记录：

- source family
- publication / update date
- product version
- GA / Preview
- whether evidence is product, architecture, adoption, experiment, or independent observation

不要因为不同网页都引用同一个官方公告，就把它们当作独立来源。

## 横向比较

最终不要做“最佳厂商”排名。

使用统一维度：

| Dimension | Vendor A | Vendor B | Vendor C |
|---|---|---|---|
| Business semantics | | | |
| Structured knowledge | | | |
| Unstructured knowledge | | | |
| Retrieval | | | |
| Memory | | | |
| Skills | | | |
| Governance | | | |
| Provenance | | | |
| Agent runtime | | | |

## 最重要的输出

最后回答：

不同产品背后的共同抽象是什么？

例如可能抽取出：
Canonical Source
Semantic Meaning
Entity / Relation
Retrieval View
Procedure / Skill
Memory
Provenance
Permission
Runtime Context

这些是研究结论，不要伪装成某一家厂商的原话。

---
## 8A. 产品、架构、采用：三层证据不要混

横向研究前，先把每个能力拆成三层：

| 层次 | 要回答的问题 | 典型证据 |
|---|---|---|
| Product | 产品到底提供什么？ | 官方 docs / API |
| Architecture | 它在运行时怎样工作？ | architecture / source / examples |
| Adoption | 用户实际怎样使用？ | customer engineering / production reports / independent evidence |

常见错误是：

~~~text
产品文档能力
  ↓
被写成架构事实
  ↓
又被写成行业采用结论
~~~

每向上走一级，都必须新增证据。

## 8B. Vendor Card

不要边读边写散文。每家公司先填固定卡片：

~~~text
Vendor:
Product / Capability:
Research cutoff:
Version / GA status:

Problem:
Abstraction:
Canonical representation:
Derived views / indexes:
Discovery:
Retrieval:
Runtime integration:
Authorization / entitlement:
Ownership:
Lifecycle:
Provenance:
Freshness:
Evaluation:
Adoption signals:
Known limitations:
Independent evidence:
Unknown:
~~~

先填卡片，再写文章。这样跨厂商比较不会被各自的产品术语带偏。

## 8C. 追踪能力生命周期

重要能力尽量沿着：

~~~text
Announced
  ↓
Preview / Experimental
  ↓
GA
  ↓
Adoption
  ↓
Certification / Governance
  ↓
Deprecation / Replacement
~~~

研究中至少记录：

- first_seen
- last_verified
- current_status
- product_version
- source_updated_at
- research_cutoff

“已经发布”不等于“已经形成稳定企业实践”。

## 8D. Customer Case 的证据边界

Customer case 可以证明：

- 某公司做过；
- 某种部署方式可行；
- 某场景下解决了某问题；
- 当时的约束和架构选择。

通常不能单独证明：

- 行业普遍采用；
- 对所有企业都适用；
- 所有 workload 下效果一致；
- 已经形成最佳实践。

优先写：

> 公开案例显示 A 公司采用了 X。

不要直接升级为：

> 企业通常都会采用 X。

## 8E. 共同模式必须跨来源验证

一个候选“行业共同模式”至少检查：

1. 两个或以上独立 vendor / implementation；
2. 名称不同但机制确实相似；
3. 是否存在明显反例；
4. 是否只适用于某类 workload；
5. 是否存在共同上游技术导致虚假的“共识”。

特别警惕：

~~~text
same API provider
same underlying database
same benchmark
same consulting pattern
same source article
same parent company / ecosystem
~~~

这些都可能制造假独立性。

## 8F. 不抽产品名，抽责任边界

发现多个厂商都提供某种“Knowledge”时，优先问：

- 谁保存 canonical meaning？
- 谁提供 retrieval view？
- 谁执行 entitlement？
- 谁保存 provenance / evidence？
- 谁负责 lifecycle？
- 谁组装 runtime context？
- 谁最终执行 business action？

很多产品看起来是一个 feature，拆开后其实是多个责任。

一个候选通用结构可能是：

~~~text
Canonical Source
    ↓
Semantic / Knowledge Object
    ↓
Retrieval View
    ↓
Context Assembly
    ↓
Agent Reasoning
    ↓
Action / Business System
~~~

这只是研究模型，不要直接说成某一家厂商的原话。

## 8G. 对比表允许 Unknown

推荐使用：

- Confirmed
- Partial
- Unknown
- Not documented
- Preview
- Independent evidence missing
- Conflicting

尤其注意：

“官方资料没有说明” ≠ “官方明确不支持”。

不要为了让矩阵看起来完整而填充模型自己的常识。

## 8H. Industry conclusion 分级

### Level 1 — Vendor Fact

单个厂商明确公开的产品能力。

### Level 2 — Cross-source Observation

多个直接证据对同一机制的观察。

### Level 3 — Cross-vendor Pattern

多个独立厂商 / implementation 反复出现相似机制。

### Level 4 — Engineering Practice

除厂商能力外，还有真实使用、独立工程经验、失败案例或 benchmark 支持。

### Level 5 — Candidate Primitive

本仓库根据上述证据提出的通用抽象。

Level 5 是 synthesis，不是 industry fact。

## 8I. 冲突先查上下文

厂商 A 与 B 对同一能力说法不同，先检查：

- product version
- deployment model
- workload
- data scale
- user persona
- authorization model
- GA / preview
- benchmark methodology

很多“厂商冲突”最后是条件不同，而不是一个一定正确、另一个一定错误。

## 8J. Vendor Expansion Review

完成初轮研究后必须回看：

~~~text
Did we only study our usual vendors?
        ↓
Did we include at least 3 new vendors?
        ↓
Did we include at least 2 vendor categories?
        ↓
Did we search for an incompatible / alternative architecture?
        ↓
Did any new vendor change the candidate primitive?
~~~

如果最后一个答案是“是”，必须在 synthesis 中明确写出这个变化。

如果前三项做不到，必须记录原因，而不是默认为“无关”。

## 8K. 防止“固定大厂偏见”

以下模式视为研究质量问题：

- 连续多次只引用同一 3–5 家厂商；
- 先决定抽象，再只寻找支持它的厂商；
- 只研究 AI model vendors，不研究 enterprise software vendors；
- 只研究 cloud vendors，不研究 application/data vendors；
- 只看官方 feature，不看 architecture / customer engineering；
- 把同一生态中的多个产品当成独立行业证据。

发现这些情况时，应主动扩展研究集合或降低结论强度。

## 8L. 最终必须回答三个问题

### What is common?

真正跨来源重复出现的机制是什么？

### What is different?

差异到底发生在 representation、runtime、governance、lifecycle 还是 deployment？

### What should we reuse?

哪些应该成为当前项目的 primitive，哪些只应该保留为 adapter / integration / vendor-specific implementation？

## 19. 确定性校验脚本

OpenAI 的 Skills 规范允许 Skill 目录包含 scripts，并把它用于 repeatable actions；但真正执行脚本仍依赖具体 agent runtime 是否提供 shell / sandbox。因此脚本是质量闸门，不是唯一执行路径。

有 shell / sandbox 时优先运行：

~~~bash
python3 skills/industry-practice-research/scripts/validate_vendor_report.py 业界实践/snowflake-business-knowledge.md
~~~

脚本固定检查：

- 必要章节；
- research cutoff / 日期；
- Sources；
- Capability / Architecture / Lifecycle matrix；
- Unknown / Limitations；
- 重复 source URL；
- 明显的高强度结论风险。

脚本通过只代表机械规则通过，不代表研究结论正确。

不要让脚本承担：

- 产品能力语义判断；
- 两个 primitive 是否真的等价；
- 行业模式是否成熟；
- customer case 是否有代表性。

### 脚本不可执行时

1. 不阻断研究；
2. 回到手工 checklist；
3. 记录 deterministic check unavailable；
4. 不得声称“脚本检查通过”。

## 20. 研究输出的最小复用形态

研究沉淀到仓库时，建议同时保存：

~~~text
Vendor Card
Capability Matrix
Architecture Matrix
Lifecycle Matrix
Common Patterns
Real Differences
Evidence Gaps
Candidate Primitives
Open Questions
Vendor Expansion Log
~~~

这样一次厂商研究才能直接反馈到当前 Agent Knowledge / Common Agent Library 的架构讨论。
