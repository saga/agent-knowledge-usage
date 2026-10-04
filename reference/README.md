# Reference

这里保存与 Agent Knowledge / Context / Memory / Ontology / Graph / Skills / RAG 相关的研究笔记和经典资料索引。

这些文件是研究摘要与分析，不是受版权保护文章的全文镜像；每份文件保留原始 URL，并明确区分论文/作者观点与本仓库自己的架构判断。

## 怎么读

如果重点研究 Knowledge Foundation：

RAG → Context → RAG views → Graph / Proposition → Knowledge Compilation

如果重点研究 Agent：

ReAct → Toolformer → CoALA → Memory → Skills → Context Engineering

如果重点研究企业业务知识：

Snowflake → Google Open Knowledge Format → LLM Wiki → Graph → Semantic Layer

## Knowledge / RAG

- [RAG - NeurIPS 2020](./rag-2020.md)：外部知识与参数知识的基本分工。
- [REALM - ICML 2020](./realm-2020.md)：把 retrieval 放进语言模型学习过程。
- [RETRO - 2022](./retro-2022.md)：从规模上证明模型容量和外部知识容量可以分开扩展。
- [Lost in the Middle - 2023](./lost-in-the-middle-2023.md)：说明 context 大小不等于信息利用率。
- [RAPTOR - 2024](./raptor-2024.md)：把层次化摘要变成 retrieval view。
- [Self-RAG - ICLR 2024](./self-rag-2024.md)：把“是否继续检索”变成推理决策。
- [PropRAG - EMNLP 2025](./proprag-2025.md)：用 proposition path 保存关系和自然语言语义。
- [Anthropic Contextual Retrieval](./anthropic-contextual-retrieval.md)：改善 chunk retrieval 的上下文缺失问题。

## Knowledge Representation / Compilation

- [LLM Wiki](./datacamp-llm-wiki.md)：把重复性的 query-time discovery 前移成持久知识编译。
- [Open Knowledge Format](./google-open-knowledge-format.md)：探索与 provider 无关的 Knowledge Asset 表达。
- [Snowflake Ontology / Knowledge Graph / Semantic Layer](./snowflake-ontology-knowledge-graphs-semantic-layer.md)：具体的 ontology metadata + generated view 实现模式。
- [Scaling LLM Wiki with a Graph](./neo4j-scaling-karpathy-llm-wiki-graph.md)：讨论关系导航为什么不能只靠相似度检索。

## Knowledge Fidelity / Tacit Knowledge

- [Dark Knowledge 与 Tacit Knowledge](./dark-knowledge-and-tacit-knowledge.md)：说明为什么“正确答案”不等于完整知识，以及为什么知识保真度需要加入 soft structure、uncertainty、behavior 和 tacit know-how。

## Agent Cognition / Skills / Memory

## Engineering Practice Feedback

- [agentic-data-architect 长任务实践反馈（2026-10）](./saga-agentic-data-architect-practice-2026-10.md)：从真实 Data Architecture Agent 实现中记录 checkpoint、live state、human wait 与 reasoning 的边界。

- [ReAct - ICLR 2023](./react-2023.md)：reasoning 与 acting 的基本循环。
- [Toolformer - 2023](./toolformer-2023.md)：模型如何学习什么时候调用工具。
- [CoALA - 2024](./coala-2024.md)：把 memory、action、environment interaction 放进统一 cognitive architecture。
- [Agent Memory Survey - 2025](./agent-memory-2025.md)：把 memory 的形式、功能和生命周期系统化。
- [Externalization in LLM Agents - 2026](./externalization-llm-agents-2026.md)：把 Memory、Skills、Protocols、Harness 放到同一条 externalization 路线上。
- [Anthropic Agent Skills](./anthropic-agent-skills.md)：procedural knowledge 与 progressive disclosure。
- [Anthropic Context Engineering](./anthropic-context-engineering.md)：把 active context 当成独立 runtime problem。
- [OpenAI File Search](./openai-file-search.md)：Knowledge Access 作为 hosted capability。

## 这些资料共同指向什么

单独看，每篇资料只解决一个问题：检索、摘要、图、memory、skill、tool 或 context。

放在一起后，更完整的结构是：

~~~text
Canonical Source
      ↓
Knowledge Representation
      ├── Semantic / Ontology
      ├── Entity / Relation
      ├── Claim / Proposition
      └── Compiled Views
      ↓
Retrieval / Navigation
      ↓
Evidence
      ↓
Context Assembly
      ↓
Agent
      ├── Memory
      ├── Skills
      └── Tools
      ↓
State / Evaluation / Governance
~~~

这里最重要的边界仍然是：Derived View 可以很多，Canonical Source 必须始终可追溯。
