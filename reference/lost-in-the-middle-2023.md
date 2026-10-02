# Lost in the Middle: How Language Models Use Long Contexts

来源：https://arxiv.org/abs/2307.03172  
年份：2023

## 它真正击中的问题

长上下文最容易带来一个错觉：

> 上下文窗口越大，就可以把更多资料直接塞给模型。

这项研究说明不是这样。模型对长上下文中的信息利用存在明显的位置效应，相关信息放在中间时，利用效果可能下降。

所以：

~~~text
Context size ↑
≠
Useful context ↑
~~~

## 这为什么会影响 Agent Architecture

如果模型面对 100 页资料不能稳定利用全部内容，那么“把所有相关文档都放进 prompt”其实是在增加噪声。

系统真正需要处理的问题变成：

1. 哪些信息值得进入 context？
2. 什么顺序放？
3. 哪些信息可以先压缩？
4. 哪些信息必须保留原文？
5. 哪些信息应该在推理中再次检索？

Context Engineering 因此不是 prompt 修辞，而是运行时的数据选择问题。

## 对 Retrieval 的影响

传统：

~~~text
top-k retrieval
   ↓
prompt
~~~

更合理的是：

~~~text
retrieve
  ↓
dedup
  ↓
rerank
  ↓
select
  ↓
order
  ↓
compress where safe
  ↓
context
~~~

“select”和“order”会直接影响模型到底能不能用到证据。

## Retrieval 与 Context Assembly 不应该混成一个组件

Retrieval 解决：

> 候选证据在哪里？

Context Assembly 解决：

> 这一步推理究竟需要哪些信息？

两者混在一起，检索层最后会被迫承担大量 prompt 逻辑，也让不同 Agent 难以共享同一 Knowledge backend。

## 对长期 Agent

长任务的 context 会同时出现：

- 用户消息；
- tool results；
- memory；
- retrieved documents；
- plan；
- intermediate findings；
- citations；
- errors。

如果全部追加、不淘汰，最终同时遇到 token 成本和信息利用率下降。

这就是后来 Context Compaction、Memory、Tool-result clearing、progressive disclosure 等技术出现的重要背景。

## 对当前项目

一个很具体的设计结论是：

> Context 不是 Knowledge Storage。

Knowledge 可以很大；context 必须小而有目的。

Common Agent Library 因此更需要 ContextAssembler / ContextPolicy，而不是再造一个更大的 vector store。
