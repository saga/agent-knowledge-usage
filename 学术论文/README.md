# 学术论文

围绕本项目的核心问题，系统整理 AI Agent 中业务知识如何抽象、保存、检索、使用和治理，并向相关延展领域扩展。

当前收录 **56 篇**，按 8 个方向组织：

| 目录 | 数量 | 重点 |
|---|---:|---|
| [RAG 与检索](./01-RAG与检索/) | 7 | 外部知识访问、检索、证据 |
| [知识图谱与本体](./02-知识图谱与本体/) | 7 | Entity、Relation、Ontology、Business Semantics |
| [Memory](./03-Memory/) | 7 | Episodic / Semantic / Long-term Memory |
| [Skills / Tool / Planning](./04-Skills-Tool-Planning/) | 7 | Procedural Knowledge、Tool Use、Workflow |
| [Context Engineering](./05-Context-Engineering/) | 7 | Context Assembly、Compression、Eviction |
| [Multi-Agent 与协议](./06-Multi-Agent与协议/) | 7 | Collaboration、MCP、A2A、Interoperability |
| [Evaluation](./07-Evaluation与Benchmarks/) | 7 | Agent Benchmark、Tool Use、Knowledge Work |
| [Governance / Safety / Enterprise](./08-Governance-Safety-Enterprise/) | 7 | Safety、Policy、Runtime Governance |

## 与前面业界实践的对应

~~~text
Snowflake / Databricks / Google  → Semantic / Ontology / Business Knowledge
OpenAI                          → Retrieval / Knowledge Access
Anthropic                       → Skills / Memory / Context / MCP
Academic literature             → 上述每一层的算法、架构和评估基础
~~~

## 下载

论文索引保存在 papers.json。

本地执行：

~~~bash
python3 学术论文/download_papers.py
~~~

脚本会把公开 PDF 放进各主题目录下的 pdf/ 子目录，并支持多线程下载。仓库同时提供 GitHub Actions workflow，便于在 GitHub runner 上执行下载。

> 说明：本次提交不直接镜像 56 个 PDF 二进制，以避免把大量外部论文文件写入 Git 历史；索引、公开 PDF URL 和可重复下载脚本均已保存。

## 阅读顺序

~~~text
RAG → Knowledge Graph / Ontology → Memory → Skills / Tool Use
→ Context Engineering → Multi-Agent / Protocol → Evaluation → Governance
~~~
