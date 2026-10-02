# agent-knowledge-usage

这个仓库用于从理论和战略层面研究 AI Agent 中的 Knowledge、Memory、Skills、Ontology、Graph、Context、Tools、State、Evidence、Evaluation 和 Governance。

## Documents

- [Agent Knowledge & Capability Roadmap](./AGENT-KNOWLEDGE-ROADMAP.md)
- [AI Agent 知识表达和使用：知识到底损失在哪里？](./AI-AGENT-KNOWLEDGE-EXPRESSION-AND-USE.md)
- [Reference Index](./reference/README.md)
- [Academic Papers（56篇）](./学术论文/README.md)
- [Industry Practice](./业界实践/README.md)
- [Research Skills](./skills/README.md)

## Core question

> How should Knowledge, Memory, Skills, Ontology, Graphs, Tools, Context, State, Evidence and Agent runtime fit together so that an LLM can reliably use knowledge it did not acquire during training?

当前工作模型：

Source → Canonical Knowledge → Derived Views / Ontology / Graph / Retrieval → Evidence / Context → Agent → Memory / Skill / State / Learning

当前新增研究方向：

Source → Representation → Knowledge Access → Knowledge Projection → Knowledge Use → Evidence / Action

重点研究的不再只是“知识放在哪里”，而是知识经过不同表示、访问和上下文投影后，哪些被保留、哪些被丢失，以及 Agent 是否真正使用了它。
