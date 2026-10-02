# Memory in the Age of AI Agents

来源：https://arxiv.org/abs/2512.13564  
年份：2025

## 为什么 Agent Memory 不能简单等于 Vector Store

这篇综述的一个重要价值，是把 Agent Memory 与普通 RAG、Context Engineering 分开讨论。

Memory 至少有不同形式和用途。

按功能，可以区分：

- factual：事实；
- experiential：过去做过什么、什么方法有效；
- working：当前任务临时信息。

按生命周期，还需要讨论：

- formation；
- retrieval；
- evolution。

因此“把聊天记录 embedding 后丢进向量库”只是 Memory 的一种实现，甚至未必是合理的长期方案。

## Memory 最难的是写，不是读

多数系统先解决 recall：

~~~text
query → retrieve old memories
~~~

但长期 Agent 真正容易失控的地方是 write：

~~~text
observe
  ↓
extract
  ↓
store
~~~

什么都存会导致：

- 噪声越来越大；
- 旧事实和新事实冲突；
- 临时推理污染长期记忆；
- 错误信息被反复召回。

因此 Memory 需要 Write Policy。

## 一个更完整的 Memory 生命周期

可以把系统做成：

~~~text
Observe
  ↓
Extract candidate memory
  ↓
Validate
  ↓
Store
  ↓
Retrieve
  ↓
Use
  ↓
Reflect
  ↓
Promote / Update / Forget
~~~

这里最重要的是“candidate”。

不是所有 Agent observation 都应该直接成为长期事实。

## Memory 与 Business State 的边界

例如：

- 上一次任务记得“客户准备购买”是 memory；
- 客户账户当前状态是业务系统里的 business state。

二者可能相关，但 authority 完全不同。

如果两边冲突：

> Business System 应该赢，Memory 需要被更新。

## Memory 需要 Provenance

一个长期 memory 最少应该能回答：

- 谁/什么产生了它；
- 来自用户、工具、文档还是模型推断；
- 什么时候产生；
- 是否被验证；
- 当前是否仍有效。

这意味着 Memory 的对象设计不能只有 embedding。

## 对当前项目

建议把 Memory primitive 从一开始定义成：

~~~text
Memory
├── content
├── type
├── source
├── createdAt
├── validTime
├── authority
├── confidence
├── status
└── links
~~~

实现层可以先简单，但抽象层不能假设所有 memory 都是“文本相似度”。
