# Improving language models by retrieving from trillions of tokens（RETRO）

来源：https://arxiv.org/abs/2112.04426  
年份：2022

## RETRO 做了什么

RETRO 继续推进“模型参数与外部记忆分离”的路线，但规模扩大到万亿级 token 的外部语料。

模型生成时，从外部数据库检索与当前上下文相关的文本，再将这些结果作为额外信息进入生成过程。

~~~text
context
   ↓
chunk lookup
   ↓
nearest external text
   ↓
retrieve-conditioned generation
~~~

它强调的是一种系统结构：

> 模型容量和知识容量可以分别扩展。

## 为什么对 Agent 很重要

如果知识全部放进参数，扩容单位是模型。

如果知识可以外置，扩容单位就可以变成：

- corpus；
- index；
- domain pack；
- organization repository；
- knowledge service。

所以企业 Agent 可以在不重新训练基础模型的情况下快速接入内部政策、产品手册、研究资料、Jira / Confluence 和数据目录。

## 但 RETRO 没解决“知识组织”

这是一个重要边界。

RETRO 主要回答：

> 如何从超大语料里找相似文本？

它没有回答：

- Revenue 采用哪个业务定义？
- 两个文档冲突时哪个是权威？
- 当前用户有没有权利看到某段内容？
- 某个事实在什么时间段有效？

因此：

~~~text
Retrieval scale
≠
Knowledge governance
~~~

## 对 Business Knowledge 的直接推论

企业系统不能只有：

~~~text
documents → embeddings → similarity search
~~~

还需要：

~~~text
source
authority
scope
version
effective time
relationship
semantic meaning
~~~

这些字段决定一个检索结果“能不能使用”，不只是“像不像”。

## 对当前 Agent 架构

如果统一成：

~~~text
Agent → KnowledgeAccessTool → Search
~~~

底层 Search 可以非常复杂，但 Agent 不应该知道具体实现。

Agent 需要的是：

~~~text
search(query, filters, scope)
      ↓
evidence
~~~

而不是直接面对 vector database。

这也是把 Knowledge Access 当 capability 的原因。
