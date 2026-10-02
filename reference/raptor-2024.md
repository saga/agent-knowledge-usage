# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

来源：https://arxiv.org/abs/2401.18059  
年份：2024

## 它解决的不是“向量召回不准”这么简单

很多知识系统把 chunk 当成基本单位，然后对 chunk 做 embedding 和 top-k。

但有些问题并不是局部 chunk 能回答的。

例如：

> 这篇文档对整个系统架构的核心判断是什么？

答案可能分散在几十个段落里，单个 chunk 都没有完整结论。

RAPTOR 先对低层文本聚类和摘要，再递归形成更高层的 summary nodes。

~~~text
Raw Chunks
   ↓
Cluster
   ↓
Summary
   ↓
Cluster summaries
   ↓
Higher-level summary
~~~

于是检索不再只有一个粒度。

## 为什么摘要在这里变成了结构

普通摘要：

~~~text
document → summary
~~~

是一次性压缩。

RAPTOR 的 tree：

~~~text
document
 ├── section summary
 │    ├── chunk
 │    └── chunk
 └── section summary
      ├── chunk
      └── chunk
~~~

高层节点适合回答“整体是什么”，低层节点适合回答“具体证据是什么”。

所以摘要可以成为一种 retrieval view，而不是 source 的替代品。

## 最重要的边界

Summary 是 derived data。

如果：

~~~text
source → summary
~~~

之后删掉 source，只留下 summary，系统把一个有来源的知识系统变成了不可逆压缩。

会丢掉：

- exact wording；
- 条件；
- 例外；
- provenance；
- 原文位置。

稳妥的结构是：

~~~text
Summary Node
   ↓
source references
   ↓
canonical evidence
~~~

## RAPTOR 对企业知识的启发

企业知识天然存在多粒度：

企业战略 → 产品线 → 部门 → 系统 → 业务流程 → 规则 → 文档章节 → 原文段落。

如果全部扁平化到一个 vector index，Agent 很难做“先定位领域，再进入细节”的导航。

层次化检索可以承担这个职责。

## 和 Knowledge Graph 的关系

RAPTOR 更偏 hierarchy。

Knowledge Graph 更偏 relation network。

两者可以同时存在：

~~~text
Hierarchy
   +
Graph links
   +
Original source
   ↓
Navigable Knowledge
~~~

因此，长期企业知识不需要在“树”和“图”中二选一。

## 对当前项目

当前仓库应该把 summary 看成 Derived Knowledge View，而不是 Knowledge source of truth。

这条原则对后面做 LLM Wiki、知识编译和 GraphRAG 都重要。
