# Open Knowledge Format（OKF）

来源：https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing  
发布时间：2026-06-12

## OKF 解决的是“知识怎么携带”而不是“知识怎么理解”

Google Cloud 提出的 Open Knowledge Format 很简单：

~~~text
directory
 ├── Markdown files
 ├── YAML frontmatter
 └── Markdown links
~~~

它希望让 dataset、table、metric、playbook、runbook、API 等知识对象有一个人和 Agent 都能读的交换形式。

关键点不在格式有多复杂，而在于：

> Knowledge Asset 可以有一个独立于数据库、模型和 Agent Framework 的 portable representation。

## 为什么这个方向重要

如果知识只能存在于：

- 某个 vector database；
- 某个 catalog；
- 某个 proprietary agent platform；

那么 Agent 更换框架时，知识也被绑定住了。

OKF 的思路是先有一个可版本控制的 Knowledge Asset，再让：

~~~text
Search
Graph
Semantic Layer
Agent
~~~

分别消费它。

这和软件工程中“源代码与编译器分离”很像。

## 它最适合什么

例如：

~~~text
knowledge/
  finance/
    revenue.md
    customer.md
  operations/
    incident-runbook.md
  data/
    revenue-metric.md
~~~

同一个 Knowledge Asset 可以被：

- 人直接阅读；
- Git 版本控制；
- pipeline 生成；
- Agent 检索；
- Graph indexing；
- semantic ingestion。

这使“知识 portability”成为一个独立架构问题。

## 但 OKF 本身非常有限

格式不会自动解决：

### Semantic correctness
Markdown 写错了仍然是错的。

### Ontology alignment
两个团队都定义 Revenue，不代表它们指的是同一个东西。

### Freshness
Git 里有文件，不代表它现在仍有效。

### Authorization
文件存在，不代表每个人都有权限看。

### Conflict
多个文件可能互相矛盾。

### Retrieval
文件格式本身不负责搜索。

所以：

> OKF 是 interchange layer，不是 knowledge platform。

## 对当前项目的价值

这启发 Common Agent Library 保留一个与具体 backend 无关的 Knowledge Asset contract。

可以考虑：

~~~text
Knowledge Asset
├── id
├── type
├── metadata
├── content
├── links
├── source
├── version
├── validTime
└── authority
~~~

上面可以有 Markdown / YAML / JSON / database object 等不同 representation。

真正长期稳定的应该是语义契约，而不是某个数据库 schema。
