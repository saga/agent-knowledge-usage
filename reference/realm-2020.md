# REALM: Retrieval-Augmented Language Model Pre-Training

来源：https://proceedings.mlr.press/v119/guu20.html  
会议：ICML 2020

## 论文在解决什么问题

REALM 更早提出了一个关键问题：

> 如果模型在推理时可以访问外部文本，为什么一定要把所有知识都压进参数？

与典型 RAG 的 query-time generation 不同，REALM 把 retrieval 更深地放进语言模型预训练过程。模型学习在大量外部文本中寻找与当前预测相关的信息。

这使“检索器”从工程插件变成了模型能力的一部分。

## 关键架构

~~~text
masked input
    ↓
retriever
    ↓
external corpus
    ↓
relevant passages
    ↓
language model
    ↓
prediction
~~~

检索器也参与学习，而不是完全固定。

## 为什么它重要

REALM 证明了一件后来反复出现的事情：

> 模型参数和外部知识库不必承载同一种职责。

参数更适合语言能力、通用模式和稳定的模型能力；外部库更适合可以更新的事实、大规模文档、领域资料和可追踪来源。

这已经很接近今天 Agent 的 Model + External Cognitive Infrastructure。

## 论文结果的边界

论文在多个 Open-Domain QA benchmark 上报告明显提升，也讨论了外部检索带来的模块化和可解释性。

但这并不意味着 external retrieval 永远有效。它依赖：

- retriever 的召回能力；
- corpus 的覆盖范围；
- 文档质量；
- index freshness；
- query 与 corpus 的匹配。

问题因此从“模型有没有知识”转移成“系统能不能找到正确知识”。

## 对企业知识系统的启发

REALM 很早就暴露了一个现在仍然容易忽略的问题：

> Knowledge Freshness 是系统属性，不是模型属性。

如果政策文档昨天更新，而索引还是上个月的版本，模型即使推理完全正确，也会回答错误。

企业 Knowledge 至少应能记录：

~~~text
source
version
effective time
indexed time
authority
scope
~~~

“最新”不能由模型自己猜。

## 和今天的 Agent 的关系

REALM 可以看成：

~~~text
Parametric Model
      +
Learned Retrieval
      +
External Corpus
~~~

而今天的 Agent 又向前走了一步：

~~~text
Model
+
Knowledge
+
Memory
+
Skills
+
Tools
+
State
+
Context
~~~

REALM 因此更像是“外部知识成为模型架构组成部分”的早期理论基础。

## 对当前项目

它支持一个长期设计原则：

> Knowledge backend 可以独立于 Agent runtime 演进。

Common Agent Library 不应该把某个 embedding model 或 vector database 写死在 Agent 核心里。
