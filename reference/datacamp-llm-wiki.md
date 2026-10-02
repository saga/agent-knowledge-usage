# LLM Wiki：把一次次检索变成持续的知识整理

来源：https://www.datacamp.com/blog/llm-wiki

## 这个思路解决什么问题

普通 RAG 每次都是：

~~~text
source → index → query → retrieve → synthesize
~~~

当同一个领域被反复研究几十次时，系统每次都要重新发现概念、关系和关键结论。

LLM Wiki 的核心思路是把一次次查询过程中的“整理工作”前移到 ingestion / compilation：

~~~text
source
  ↓
knowledge compilation
  ↓
persistent knowledge pages
  ↓
navigation / retrieval
  ↓
agent
~~~

它不是简单把文档做摘要，而是在积累一个跨 session 的、可导航的知识结构。

## 为什么这和传统 RAG 不一样

RAG 的主要优化目标是：

> 当前 query 能不能找到相关文本？

Wiki-style knowledge compilation 的目标更像：

> 这批资料长期应该怎样组织，才能让下一次研究不必从零开始？

因此它更适合：

- 长期研究；
- 代码库分析；
- 组织知识；
- 重复性较高的行业研究；
- Team Agent 的共享知识。

## 一个很重要的工程边界

编译后的知识必须是 derived view。

~~~text
Canonical Source
    ↓
Compiled Knowledge
    ↓
Navigation / Retrieval
~~~

不能反过来：

~~~text
Compiled Knowledge
    ↓
delete source
~~~

否则第一轮抽取错误会永久成为新的真相。

## 为什么必须保留 provenance

一个知识页面说：

> “某系统采用 X。”

后面真正需要问的不是“这句话像不像真的”，而是：

- 来自哪份资料？
- 原文在哪？
- 哪个时间点有效？
- 有没有其他来源说相反的话？
- 谁把它编译出来？
- 什么时候最后验证？

因此 LLM Wiki 如果真的要用于企业，不只是 Markdown 页面，而应该是：

~~~text
Knowledge Page
+
Claim
+
Source reference
+
Version
+
Status
~~~

## 和 Knowledge Graph 的关系

Wiki 天然适合人阅读。

Graph 天然适合关系导航。

两者可以分工：

~~~text
Markdown / Page
  = human-readable representation

Graph
  = machine navigation index

Canonical source
  = authority
~~~

这比把 Markdown 直接当数据库真相更稳。

## 新问题也会随之出现

知识编译不是免费午餐。

它会引入：

- stale compiled knowledge；
- compression loss；
- extraction error；
- contradiction propagation；
- maintenance cost；
- compilation latency。

最危险的是“旧知识看起来非常完整”。

向量检索找不到一条旧资料，用户至少会知道系统没找到；错误的 compiled knowledge 却会非常自信地给出一个完整答案。

## 对当前项目

这个思路值得作为 Knowledge Foundation 的第二条路径保存：

~~~text
Query-time Retrieval
+
Ingestion-time Compilation
~~~

前者解决 freshness，后者解决 repeated discovery cost。

两者不应该二选一。
