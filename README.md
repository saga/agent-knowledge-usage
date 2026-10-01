# Agent Knowledge Usage

> 研究主题：大模型已有的参数知识、外部 Knowledge / RAG、Agent Skill / Memory，究竟应该如何表达、保存、检索和注入，才能让 Agent 真正使用模型训练时没有用到的知识，而不是把知识粗暴蒸馏成几句 summary？
>
> 研究日期：2026-10-02

## 1. 核心结论

**不要把 Knowledge 本身定义成 Summary。**

> **Knowledge 应该是有来源、有上下文、可追溯、可按不同任务产生多种检索视图的知识资产。**

更完整的心智模型是：

```text
Canonical Source
      │
      ├── 完整文本 / 表格 / 代码
      ├── sections / paragraphs
      ├── claims / propositions
      ├── concepts / entities / relations
      ├── conditions / exceptions / temporal scope
      ├── examples / counterexamples
      └── provenance / version

Derived Views
      │
      ├── summary
      ├── aliases / keywords
      ├── synthetic questions
      ├── graph indexes
      ├── BM25 index
      ├── embedding index
      └── contextual chunks

Runtime
      │
      └── task-specific Evidence / Context Pack
```

核心原则：Summary 是导航和检索视图；Proposition 是细粒度检索单位；Graph 是关系索引；Embedding 是索引；Chunk 是运行时 retrieval unit；Source / Evidence 才是事实根。

---

## 2. 先区分三种模型知识

### 2.1 Parametric Knowledge

预训练模型把大量语言规律、概念、事实和关联压进参数，但模型里存在某知识，不等于模型在任意表达方式下都能可靠调用它。

ACL 2025 的 `Knowledge Boundary of Large Language Models: A Survey` 对知识边界做了形式化区分，讨论 Universal Knowledge Boundary、Parametric Knowledge Boundary、Outward Knowledge Boundary，并把 external retrieval、knowledge editing、knowledge-enhanced fine-tuning 作为补充模型未知知识的重要路线。

- https://aclanthology.org/2025.acl-long.256/
- https://arxiv.org/abs/2412.12472

ACL 2023 的 `When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories` 在 long-tail factual knowledge 上发现：模型规模对长尾事实的改善有限，而外部检索能够显著帮助。该工作在 POPQA 最不流行约 4000 个问题上报告 GPT-J 6B 约 16%、GPT-3 davinci-003 约 19% 的准确率；Contriever retrieval 可给 GPT-3 带来约 7 个百分点提升；Adaptive Retrieval 在其设置下达到 46.5%。

- https://aclanthology.org/2023.acl-long.546.pdf

### 2.2 Non-parametric / External Knowledge

RAG 并不会把新知识写进模型参数，而是在推理时把外部证据取出来：

```text
query
  ↓
retrieve external evidence
  ↓
context assembly
  ↓
LLM inference
```

经典 NeurIPS 2020 RAG 工作证明 parametric + non-parametric memory 能显著增强 knowledge-intensive QA，并可以热替换 external index，从而在不重新训练模型的情况下更新知识。

- https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf
- https://arxiv.org/abs/2005.11401

### 2.3 Fine-tuning / Continued Training

如果希望新知识长期进入参数，需要 fine-tuning、continued pretraining 或 knowledge editing。但对事实型新知识，简单 unsupervised fine-tuning 并不稳定。EMNLP 2024 的 `Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs` 发现，在其 knowledge-intensive 任务上 RAG 持续优于 unsupervised fine-tuning；简单 fine-tuning 对 entirely new factual knowledge 的学习能力较弱。

- https://aclanthology.org/2024.emnlp-main.15/

因此工程上可以先分：

| 目标 | 更自然的机制 |
|---|---|
| 动态企业事实 / policy / 文档 | RAG / runtime retrieval |
| 需要来源、版本、审计 | RAG / evidence |
| 项目当前状态 | Memory / state |
| 稳定 workflow / procedural behavior | Skill / prompt / fine-tuning |
| 长期能力内化 | fine-tuning / continued training |

---

## 3. 为什么 Summary 不是完整 Knowledge

假设原始规则是：某策略只允许用于 A、B、C 类 eligible account；D 类账户仅在 Exception E4 生效时允许使用；交易前必须做 suitability check；产品等级超过 L3 时还必须指定角色审批；Policy P-102 v3 自 2026-03-01 生效，历史交易继续适用旧版本。

如果只保留：策略适用于 eligible account，交易前要 suitability check，高风险产品需要审批。

那么丢掉了：

- eligible account 的完整定义
- D 类账户的 exception
- Exception E4
- L3 边界
- 审批角色
- policy version
- effective date
- 历史交易适用规则
- source location

这不是摘要“少写了一点”，而是 **semantic loss**。

```text
Summary = 高压缩率语义索引
Knowledge = 可恢复、可追溯、带条件和边界的事实/规则集合
```

因此最重要的一条规则是：

> **蒸馏应该增加一个 derived view，而不是删除 canonical source。**

---

## 4. 完整 Knowledge 应该能够表达什么

不是每条知识都需要所有字段，但模型应该能够容纳：

```text
Knowledge Asset
│
├── identity
├── canonical content
│   ├── document / section / paragraph
│   ├── tables / code / figures
│
├── structured semantics
│   ├── concepts / entities
│   ├── claims / propositions
│   └── relations
│
├── conditions
│   ├── applicability
│   ├── preconditions
│   ├── exclusions
│   └── exceptions
│
├── procedural knowledge
│   ├── steps / decisions / inputs / outputs
│
├── examples
│   ├── positive / negative / edge cases
│
├── provenance
│   ├── source / location / author / timestamp / version
│
├── temporal validity
│   ├── effectiveFrom / effectiveTo / supersedes
│
└── derived views
    ├── summary / aliases
    ├── synthetic questions
    ├── propositions
    ├── graph
    ├── BM25
    └── embeddings
```

建议的跨框架抽象可以保持在：

```ts
interface KnowledgeAsset {
  id: string
  type: KnowledgeType
  source: KnowledgeSource
  content: KnowledgeContent
  semantics?: KnowledgeSemantics
  conditions?: KnowledgeConditions
  validity?: KnowledgeValidity
  provenance: KnowledgeProvenance
  derived?: KnowledgeViews
}
```

这里 `derived` 很关键：summary、proposition、graph、embedding 都是可重建的 view，不是唯一真相。

---

## 5. 对 ai-interview-questions 最重要的抽象：KnowledgeNode 不是完整 Corpus

当前 `KnowledgeNode` 大致是：

```ts
{
  id, name, area, topic, priority,
  summary, required, misconceptions, angles
}
```

这个模型非常适合：

- taxonomy / ontology
- curriculum
- learner modeling
- rubric
- coverage
- adaptive selection
- misconception detection
- prerequisite graph
- query planning

所以它更准确地是：

> **Knowledge Ontology + Curriculum + Rubric**

而不是完整 Knowledge Corpus。

这不是当前方向有问题。相反，把 KnowledgeNode 放在 Question 前面作为一等公民是合理的。真正应该避免的是继续给 KnowledgeNode 增加字段，试图让它同时承担 source、完整知识、RAG chunk、rubric、graph node 和 memory。

更稳定的结构：

```text
KnowledgeNode
    │
    ├── ontology / taxonomy
    ├── curriculum / rubric
    ├── misconceptions
    ├── relationships
    │
    └── canonical knowledge source(s)
               │
               ├── propositions
               ├── examples
               ├── contextual chunks
               └── retrieval indexes
```

> **Ontology 告诉 Agent 这是什么；Corpus 告诉 Agent 具体内容是什么。**

---

## 6. Proposition 是非常值得增加的一层

传统 chunk 的问题是太粗；三元组的问题是太扁。一个很有价值的中间层是 Proposition / Claim：一个原子、相对独立、自包含，同时保留必要条件和上下文的知识表达。

EMNLP 2024 的 `Dense X Retrieval: What Retrieval Granularity Should We Use?` 比较不同 retrieval granularity，提出 proposition 作为细粒度 retrieval unit，并报告 proposition-level retrieval 在其任务上优于更粗的 passage-level retrieval。

- https://aclanthology.org/2024.emnlp-main.845/

FEVER 2024 的 `Question-Based Retrieval using Atomic Units for Enterprise RAG` 进一步把 chunk 拆成 atomic statements，并围绕 atomic units 生成 synthetic questions，在其 enterprise RAG 实验中改善 retrieval recall 和最终效果。

- https://aclanthology.org/2024.fever-1.25/

EMNLP 2025 的 `PropRAG: Guiding Retrieval with Beam Search over Proposition Paths` 指出传统 triples 会产生 context collapse：conditionality、provenance、n-ary relations 等信息容易被压平；其 proposition-path 方法在 2Wiki、HotpotQA、MuSiQue 等 benchmark 上改善 retrieval / QA 指标。

- https://aclanthology.org/2025.emnlp-main.317/

因此推荐：

```text
Source Text
   ↓
Section / Paragraph
   ↓
Proposition / Claim
   ↓
Concept / Entity / Relation
```

Proposition 是 retrieval view，不是 source 的替代。

---

## 7. Graph 也不是完整 Knowledge

Graph 很适合表达 `A → depends_on → B`，但它很难单独表达：何时成立、对谁成立、谁规定、是否有 exception、哪个版本、是事实还是推断、多实体条件等。

所以应该是：

```text
Graph       = relationship index
Proposition = semantic unit
Source      = evidence
```

三者共存，而不是相互替代。

---

## 8. Chunking 会丢知识，Contextual Retrieval 的证据非常直接

传统 RAG 常见：

```text
Document → fixed chunks → embedding → vector search
```

问题在于 chunk 经常失去 parent context。Anthropic 的 `Contextual Retrieval` 为每个 chunk 增加 chunk-specific context，再做 embedding 与 BM25。

Anthropic 公开实验报告：

- Contextual Embeddings：top-20 retrieval failure rate 5.7% → 3.7%，约下降 35%
- Contextual Embeddings + Contextual BM25：5.7% → 2.9%，约下降 49%
- 再加入 reranking：5.7% → 约 1.9%，约下降 67%

- https://www.anthropic.com/engineering/contextual-retrieval

这个结果对知识表达的直接含义是：

> **检索单位可以小，但不能把它需要的上下文一起切掉。**

而且单纯 document-level summary 不能替代 chunk-specific context。

---

## 9. Late Chunking 进一步说明：小 retrieval unit 不等于小 semantic context

`Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models` 的流程是：

```text
whole document
   ↓
long-context encoder
   ↓
contextual token embeddings
   ↓
chunk pooling
```

论文在多个模型和数据集上报告 late chunking 相比多种 naive chunking 有稳定收益，平均约 1.5–1.9 个百分点的绝对 retrieval 提升。

- https://arxiv.org/html/2409.04701

这再次说明：

> **检索时的小块，与知识理解时的上下文，不应该被设计成同一个东西。**

---

## 10. Long Context 也不能取代 Knowledge Architecture

`Lost in the Middle` 研究发现，模型对长 context 中间位置的信息利用能力可能显著下降，因此：

```text
long context ≠ reliable full access
```

- https://arxiv.org/abs/2307.03172

EMNLP 2024 的 `Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach` 和 2025 的 `Long Context vs. RAG for LLMs: An Evaluation and Revisits` 都显示：结果依赖任务、语料、context size 和 retrieval 方式，没有绝对的单一路线。

- https://aclanthology.org/2024.emnlp-industry.66/
- https://arxiv.org/abs/2501.01880

所以应该做 routing：

```text
small relevant corpus  → direct context
large corpus            → RAG
large document           → hierarchical / contextual retrieval
global question          → graph / hierarchical synthesis
high-value local query   → precise evidence retrieval
```

---

## 11. Summary 最适合作为 Hierarchical Retrieval View

RAPTOR 的思路很典型：从低层 chunks 出发，recursive embedding、clustering、summarization，形成多层 abstraction tree，再根据 query 访问不同层级。

- https://arxiv.org/abs/2401.18059

因此可以存在多个层级：

```text
Level 0: source text
Level 1: section / paragraph
Level 2: proposition
Level 3: concept / topic summary
Level 4: global / community summary
```

Summary 的正确位置是 hierarchy 中的一种 view，而不是 source replacement。

---

## 12. GraphRAG 说明 Local Knowledge 和 Global Knowledge 是两种问题

传统 vector RAG 很擅长“哪一段提到了 X”，但不一定擅长“整个知识库有哪些主要主题、这些主题之间有什么关系”。

Microsoft 的 GraphRAG 通过 entity graph、community、community summaries 处理 global sensemaking；BenchmarkQED 进一步把 local / global 与 data / activity 维度拆开。

- https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/
- https://www.microsoft.com/en-us/research/blog/benchmarkqed-automated-benchmarking-of-rag-systems/

因此成熟 retrieval system 不应只有 vector search，而应该根据 query 在 local retrieval、hierarchical retrieval、graph traversal、global synthesis、direct source reading 中切换。

---

## 13. Agent Knowledge 不只有 Fact

| 类型 | 回答的问题 | 推荐表示 |
|---|---|---|
| Declarative | 世界是什么样 | proposition / source / graph |
| Procedural | 应该怎么做 | procedure / Skill |
| Normative | 什么允许、禁止、必须 | rule + condition + policy source |
| Episodic | 过去发生过什么 | event / case / timeline |
| Experiential | 什么方法通常会失败 | lesson / heuristic / counterexample |

因此 Knowledge、Skill、Memory 不能简单合并成一个 vector DB。

### Knowledge

回答事实、定义、规则是什么。

### Skill

回答如何完成任务。Anthropic 当前 Agent Skills 把 metadata、SKILL.md、reference files、scripts 组合起来，并采用 progressive disclosure，让大量材料在需要时才进入 context。

- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

### Memory

回答用户、项目、Agent 过去发生了什么。2025–2026 的 memory survey 已明显把 memory 与 RAG / context engineering 分开，并讨论 factual、experiential、working memory，以及 write → manage → read。

- https://arxiv.org/abs/2512.13564
- https://arxiv.org/abs/2603.07670

可以先用一句最实用的话区分：

```text
Knowledge = world / domain state
Skill     = how to act
Memory    = what happened
```

---

## 14. 如何让模型使用训练时没有的 Knowledge

假设模型训练数据没有你的内部 Policy P-102。上传 P-102 后，并没有发生模型参数学习。

真正发生的是：

```text
User Query
   ↓
Query Understanding
   ↓
Retrieve Policy Evidence
   ↓
Rerank / Context Expansion
   ↓
Evidence Pack
   ↓
LLM
   ↓
Reasoning using evidence
```

所以真正需要优化的是：

> **在正确的时刻，把足够完整、正确、带来源的知识放进模型当前有效 context。**

Anthropic 的 context engineering 文章把 context 当成有限资源，并强调 just-in-time context：维护轻量 identifier，需要时再通过工具读取真实数据，而不是提前把所有数据塞入 prompt。

- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

---

## 15. Knowledge Injection 应该理解成 Context Assembly

不应该停在：

```text
Knowledge Base → summary → prompt
```

而应该是：

```text
Knowledge Assets
      ↓
Query-aware retrieval
      ↓
Candidate fusion
      ↓
Reranking
      ↓
Context expansion
      ↓
Evidence Pack
      ↓
LLM
```

runtime Evidence Pack 可以抽象为：

```ts
interface EvidencePack {
  query: string
  evidence: Array<{
    sourceId: string
    location?: string
    proposition?: string
    excerpt?: string
    parentSection?: string
    relatedEvidence?: string[]
    metadata?: Record<string, unknown>
  }>
}
```

这里 sourceId + location 很关键，因为最终可以追问：这个 claim 的 evidence 是什么、来自哪个 section。

---

## 16. Retrieval 应该是 Multi-stage，而不是一个 weighted score 就结束

推荐 pipeline：

```text
1. Query Understanding
2. Query Rewrite / Expansion
3. Query Classification
4. Candidate Retrieval
   ├── metadata filters
   ├── BM25 / lexical
   ├── semantic embedding
   ├── graph traversal
   └── direct source lookup
5. Merge / Deduplicate
6. Rerank
7. Context Expansion
   ├── parent section
   ├── neighboring propositions
   ├── relevant graph edges
   └── source context
8. Evidence Packing
9. LLM
10. Provenance / Citation
```

OpenAI 当前 File Search 已把 semantic + keyword retrieval、vector stores、metadata filters、ranking 作为标准能力；Agents SDK 也将 FileSearchTool 做成 tool/capability。

- https://developers.openai.com/api/docs/guides/tools-file-search
- https://openai.github.io/openai-agents-python/zh/tools/

这说明主流 Agent 平台正在把 knowledge 访问抽象为 retrieval capability，而不是简单字符串拼接。

---

## 17. 真正的目标不是 Retrieval，而是 Evidence Use

RAG 至少有四层质量：

```text
Retrieval Quality
  ↓ 找到了吗？

Context Quality
  ↓ 足够完整吗？

Reasoning Quality
  ↓ 理解和使用正确吗？

Grounding Quality
  ↓ 回答真的由 evidence 支撑吗？
```

`Good retrieval` 不等于 `good answer`；`good answer` 也不等于 `grounded answer`。

RAGCHECKER 等工作把 retrieval、generator、faithfulness 拆成不同评价维度；Provenance 方向的研究也开始把 hallucination 追溯到具体 context chunks。

- https://arxiv.org/pdf/2408.08067
- https://aclanthology.org/2024.emnlp-industry.97/

---

## 18. Knowledge Completeness 不应该测 Summary Similarity

```text
A: Product requires approval.
B: Product requires approval only above risk level L3.
```

两者语义 embedding 可能很接近，但 A 已丢掉核心条件。

因此：

```text
Semantic similarity ≠ Knowledge equivalence
```

建议把 Knowledge completeness 至少拆成：

- Fact coverage
- Condition coverage
- Exception coverage
- Negation preservation
- Temporal coverage
- Procedure coverage
- Provenance coverage
- Counterexample coverage

尤其企业、金融、法律场景，`only if / unless / except / before / after / not / must / may / cannot / effective from / supersedes` 这类词往往就是核心语义，不能在 extraction 时顺手删除。

---

## 19. Knowledge Extraction 应该增加表示，而不是替换内容

正确：

```text
Source
  + Summary
  + Claims
  + Propositions
  + Relations
  + Graph
  + Embedding
  + Keywords
  + Synthetic Questions
```

错误：

```text
Source → LLM summary → delete source
```

也不应该：

```text
Source → triples → delete source
```

原因很简单：条件、例外、上下文、来源定位一旦丢掉，很难可靠恢复。

---

## 20. 企业 / 金融 Knowledge 特别需要 Rule + Scope + Condition + Exception + Provenance + Time

```text
Rule: Trade X is permitted

Scope:
  AccountType A

Preconditions:
  Eligibility E
  Suitability S

Exceptions:
  Exception E4

Authority:
  Policy P-102 v3

Validity:
  effectiveFrom = 2026-03-01
```

所以企业规则更接近：

```text
Knowledge
  = Rule
  + Scope
  + Preconditions
  + Exceptions
  + Provenance
  + Temporal Version
```

这也是为什么金融服务 Agent 的 knowledge layer 不能被简化成普通 semantic search corpus。

---

## 21. 对 ai-interview-questions 当前架构的具体建议

当前仓库的方向本身应该保留：

```text
KnowledgeNode 是一等公民
Question 是 Knowledge 的 measurement / evidence view
Knowledge Graph 是 relation / retrieval backbone
KnowledgeDocument 是 projection layer
RetrievalMode 在 retrieval layer 处理 answer boundary
```

真正应该增加的是一个独立的 canonical knowledge corpus，而不是无限扩张 KnowledgeNode。

推荐最小演进：

### Phase 1：保留 KnowledgeNode

继续负责 ontology、curriculum、rubric、misconceptions、angles、relationships。

### Phase 2：增加 canonical source

例如：

```text
src/data/knowledge/kv-cache.md
```

或：

```text
knowledge/kv-cache/
  README.md
  reference.md
  examples.md
```

### Phase 3：从 canonical source 派生 views

```text
summary
propositions
concept anchors
synthetic questions
contextual chunks
embeddings
BM25
graph links
```

### Phase 4：Retrieval 输出 EvidencePack

从 `KnowledgeHit[]` 逐步升级成带 source、location、proposition、excerpt、parent section、related evidence、metadata 的 EvidencePack。

### Phase 5：Agent prompt 只消费 EvidencePack

这样最终形成：

```text
source
  ↓
knowledge
  ↓
retrieval
  ↓
evidence
  ↓
context
  ↓
agent
```

后续更换 BM25、embedding、GraphRAG、reranker，不需要改 Knowledge schema。

---

## 22. 最终推荐的 Knowledge Architecture

```text
┌───────────────────────────────────────────┐
│ 1. SOURCE                                 │
│ raw docs / data / code / policy / paper   │
└────────────────────┬──────────────────────┘
                     ↓
┌───────────────────────────────────────────┐
│ 2. CANONICAL KNOWLEDGE                    │
│ sections / claims / propositions / rules  │
│ conditions / examples / provenance        │
└────────────────────┬──────────────────────┘
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    GRAPH          INDEX          VIEWS
 entities        BM25/vector     summary
 relations       reranker        questions
 time/deps       metadata        curriculum
       └─────────────┼─────────────┘
                     ↓
┌───────────────────────────────────────────┐
│ 4. EVIDENCE / CONTEXT ASSEMBLY            │
│ task-specific, minimal-but-sufficient     │
│ context + provenance + constraints        │
└────────────────────┬──────────────────────┘
                     ↓
┌───────────────────────────────────────────┐
│ 5. AGENT / LLM                            │
│ reasoning + tools + actions               │
└───────────────────────────────────────────┘
```

### 最重要原则

1. Source is authoritative
2. Derived knowledge is additive
3. Retrieval unit ≠ Knowledge unit
4. Context must be sufficient, not merely relevant
5. Structure and prose must coexist
6. Provenance is part of Knowledge
7. Temporal validity is part of Knowledge
8. Authorization happens before context assembly
9. Summary is navigation
10. Evaluate knowledge use, not only retrieval

---

## 23. 最后直接回答三个问题

### Q1：什么才是合适的 Knowledge 表达？

> **Canonical source + structured semantics + propositions + relations + conditions + examples + provenance + temporal validity + derived retrieval views。**

### Q2：如何完整，而不是蒸馏成几个点？

> **不要把蒸馏当成替换。**

应该同时保留：

```text
Full Source
  + structured extraction
  + fine-grained propositions
  + graph
  + summary
  + retrieval indexes
```

所有 derived representations 都应该能回到 source。

### Q3：如何让模型使用训练时没有的知识？

不是让模型临时训练，而是：

```text
External Knowledge
      ↓
Query-aware Retrieval
      ↓
Evidence Selection
      ↓
Context Assembly
      ↓
LLM Inference
```

这就是 inference-time knowledge injection。若希望永久内化，再考虑 fine-tuning / continued pretraining / knowledge editing。

---

## 24. 重点参考资料

### LLM Knowledge Boundary / Parametric Knowledge

1. Knowledge Boundary of Large Language Models: A Survey, ACL 2025  
   https://aclanthology.org/2025.acl-long.256/

2. When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories, ACL 2023  
   https://aclanthology.org/2023.acl-long.546.pdf

### RAG / Knowledge Injection

3. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks, NeurIPS 2020  
   https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf

4. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection, ICLR 2024  
   https://arxiv.org/abs/2310.11511

5. Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs, EMNLP 2024  
   https://aclanthology.org/2024.emnlp-main.15/

### Retrieval Granularity / Knowledge Fidelity

6. Dense X Retrieval: What Retrieval Granularity Should We Use?, EMNLP 2024  
   https://aclanthology.org/2024.emnlp-main.845/

7. Question-Based Retrieval using Atomic Units for Enterprise RAG, FEVER 2024  
   https://aclanthology.org/2024.fever-1.25/

8. PropRAG: Guiding Retrieval with Beam Search over Proposition Paths, EMNLP 2025  
   https://aclanthology.org/2025.emnlp-main.317/

9. Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models  
   https://arxiv.org/html/2409.04701

### Hierarchical / Graph RAG

10. RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval  
    https://arxiv.org/abs/2401.18059

11. From Local to Global: A Graph RAG Approach to Query-Focused Summarization  
    https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/

12. BenchmarkQED: Automated benchmarking of RAG systems  
    https://www.microsoft.com/en-us/research/blog/benchmarkqed-automated-benchmarking-of-rag-systems/

### Long Context

13. Lost in the Middle: How Language Models Use Long Contexts  
    https://arxiv.org/abs/2307.03172

14. Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach  
    https://aclanthology.org/2024.emnlp-industry.66/

15. Long Context vs. RAG for LLMs: An Evaluation and Revisits  
    https://arxiv.org/abs/2501.01880

### Context Engineering / Agent Skills / Memory

16. Introducing Contextual Retrieval, Anthropic  
    https://www.anthropic.com/engineering/contextual-retrieval

17. Effective context engineering for AI agents, Anthropic  
    https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

18. Agent Skills, Anthropic  
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

19. Agent Skills Best Practices, Anthropic  
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

20. File Search, OpenAI  
    https://developers.openai.com/api/docs/guides/tools-file-search

21. OpenAI Agents SDK Tools / FileSearchTool  
    https://openai.github.io/openai-agents-python/zh/tools/

22. Memory in the Age of AI Agents, 2025 survey  
    https://arxiv.org/abs/2512.13564

23. Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers, 2026 survey  
    https://arxiv.org/abs/2603.07670

24. Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents, 2026 preprint  
    https://arxiv.org/abs/2608.29606

---

## 25. 与 ai-interview-questions 的对应关系

本研究直接对照了当前仓库中的 `src/domain/knowledge/`、`src/schemas/knowledge.ts`、`src/data/knowledge/`、`src/data/knowledgeMap.ts` 以及 Knowledge Base 改进文档。

当前架构：

```text
Knowledge Node
   ↓
Knowledge Document
   ↓
Lexical / Metadata / Graph Retrieval
   ↓
Evidence
   ↓
Copilot
```

建议的下一步不是更多 `summary` 字段，而是：

```text
Knowledge Ontology
        ↕
Canonical Knowledge Corpus
        ↓
Propositions / Contextual Views
        ↓
Retrieval
        ↓
Evidence Pack
        ↓
Agent
```

这样 KnowledgeNode、Common Agent Library、Agent Skill、RAG 和 Agent Memory 可以共享一个稳定基础：知识本体、完整文档、检索单位、评分 rubric、运行时 context 各自承担自己的职责，而不是混成一个对象。