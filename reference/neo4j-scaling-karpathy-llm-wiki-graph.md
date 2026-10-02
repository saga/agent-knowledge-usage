# Scaling Karpathy's LLM Wiki：为什么大规模知识库需要关系导航

来源：https://neo4j.com/blog/agentic-ai/scaling-karpathy-llm-wiki-graph/  
发布时间：2026-08-31

## 它观察到的问题

一个小型 LLM Wiki 用文件夹和 Markdown links 就很好用。

但规模变大以后，问题从“有没有内容”变成：

> Agent 怎样知道下一步应该沿哪条关系继续看？

文章提出 Graph Index：

~~~text
Markdown knowledge
      ↓
graph index
      ↓
navigation
~~~

图的对象可以包括 Vault、Folder、Document、Section，关系包括 containment、reading order 和 cross-document links。

## 为什么 Graph 在这里不是数据库替代品

最有用的理解不是：

> Graph 比 Vector DB 好。

而是：

> Vector Search 找候选，Graph 提供结构导航。

例如用户问：

> 这个系统为什么这样设计？

vector retrieval 可能找到一篇相关文档。

graph navigation 可以进一步沿着：

~~~text
system
 → component
 → decision
 → referenced ADR
 → dependency
 → source
~~~

进入证据链。

## Progressive disclosure

一个实用模式是：

~~~text
outline
  ↓
search
  ↓
get
  ↓
follow links
~~~

这和 Context Engineering 很接近。

Agent 先拿地图，再打开局部内容，而不是把整座知识库塞进 context。

## 文章中的 benchmark 应该怎么理解

文章报告了图增强方案在其描述的实验中对事实正确性、precision、recall 等指标的提升。

这些结果应视为特定实验中的 evidence，而不是“Graph 一定优于 Vector”的普遍结论。

真正值得保留的是架构观察：

> 当知识之间的关系本身就是问题的一部分时，关系导航比单纯相似度检索多了一条信息通道。

## Graph 的代价

Graph 不是免费能力。

必须额外处理：

- node / edge extraction；
- entity resolution；
- relationship quality；
- stale edges；
- schema evolution；
- graph growth；
- traversal explosion。

尤其是自动抽取关系时，图会把错误关系持久化。

所以：

~~~text
Graph
  ≠
authority
~~~

仍然必须能追溯到 canonical source。

## 对当前项目

这里值得抽取的是一个接口思想：

~~~text
Search
  +
Navigate
  +
Open Evidence
~~~

而不是把 Graph DB 作为 Common Agent Library 的强依赖。

未来具体实现可以是：

- Graph DB；
- SQL relationships；
- static links；
- knowledge pages；
- semantic layer relationships。

上层 Agent 不需要知道具体存储。
