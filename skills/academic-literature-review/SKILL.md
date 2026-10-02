---
name: academic-literature-review
description: 系统搜索、筛选、分类和整理 AI Agent 与 LLM Knowledge 相关学术论文。当用户要求论文、文献综述、研究方向、论文地图或批量下载时使用。
metadata:
  kind: capability
---

# Academic Literature Review

## 目标

建立可复用的论文集合，而不是简单返回一串搜索结果。

核心问题：

这个研究问题已经研究到了哪里？
哪些论文是基础？
哪些论文解决了什么子问题？
哪些方向正在快速发展？
还有什么空白？

## 默认分类

围绕 Agent Knowledge Stack 搜索：
- RAG / Retrieval
- Knowledge Graph / Ontology
- Business Semantics
- Memory
- Skills / Procedural Knowledge
- Tool Use / Planning
- Context Engineering
- Multi-Agent / Protocol
- Evaluation
- Safety / Governance

分类可以按任务调整，不要为了凑分类强行拆论文。

## 搜索流程

### 1. Seed papers

先找：
- foundational paper
- survey
- benchmark
- influential architecture

### 2. Citation expansion

对种子论文扩展：
- references
- citing papers
- similar / related work

### 3. Recent work

再补最近工作：
- 最近 1～2 年
- 新 benchmark
- 新 architecture
- enterprise / production-oriented work
- 与当前项目直接相关的新方向

### 4. 去重

优先按 canonical identifier 去重：
- arXiv ID
- DOI
- title + author

## 每篇论文记录

| 字段 | 内容 |
|---|---|
| Title | 论文标题 |
| Authors | 作者 |
| Year | 首次公开年份 |
| ID | arXiv / DOI |
| Abstract | 摘要入口 |
| PDF | 公开 PDF |
| Category | 所属方向 |
| Relevance | 与研究问题的关系 |
| Status | preprint / published / unknown |

## 下载纪律

用户要求下载时：
1. 首选公开 arXiv / 官方 PDF。
2. 保存 metadata 和 canonical URL。
3. 实际下载成功后才标记 downloaded。
4. 下载失败必须保留失败状态。
5. 不绕过付费墙或访问限制。
6. 不默认把大量外部 PDF 二进制提交进 Git。

## 证据边界

必须区分：

作者提出 ≠ 实验显示 ≠ 广泛复现 ≠ 业界采用

不要把论文作者的 recommendation 写成行业共识。

## 推荐输出

Research question
→ Paper map
→ Foundational papers
→ Recent papers
→ Methods / patterns
→ Limitations
→ Research gaps
