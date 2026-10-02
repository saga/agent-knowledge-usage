# Effective Context Engineering for AI Agents

来源：https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Context Engineering 到底在解决什么

Prompt Engineering 关注：

> 怎么写一段更好的指令？

Context Engineering 关注：

> 这个时间点，模型到底应该看到什么？

两者的工程层级不同。

一个长任务里，模型可能同时面对：

~~~text
system instructions
+
user request
+
retrieved knowledge
+
memory
+
workflow state
+
tool results
+
previous reasoning
~~~

这些东西全部存在，并不意味着全部应该进入当前 context。

## Context 是有限资源

上下文窗口即使越来越大，信息也不会因此自动变得同样有用。

Anthropic 的近期实践把 memory、compaction、tool-result clearing、just-in-time loading 放到同一个 Context Engineering 问题下讨论。

这和 Lost in the Middle 的研究方向是相互呼应的。

## Progressive Disclosure 是 context budget 管理

Skills 的 progressive disclosure 其实是 Context Engineering 的一种实现：

~~~text
metadata first
→ details later
→ resources only when needed
~~~

因此“知识已经存在”和“知识现在是否应该被加载”是两个不同问题。

## 一个实用的 Context Assembly 模型

可以把当前 context 看成：

~~~text
Current task
+
Relevant instructions
+
Selected knowledge
+
Relevant memory
+
Current state
+
Recent observations
+
Required evidence
~~~

每个区块都应该有进入条件。

## 为什么不能把 Context 当作状态库

如果把所有东西都塞进 context：

- 长任务会无限增长；
- 历史错误会持续存在；
- state freshness 无法保证；
- tool results 会淹没真正重要的信息。

因此：

> Context 是一个投影，不是数据库。

它应该从 Knowledge、Memory、State、Tools 等系统实时组装。

## 对当前项目的具体意义

Common Agent Library 更适合有：

- ContextAssembler；
- ContextPolicy；
- Context source adapters；
- compaction / trimming；
- evidence packing。

而不是把“prompt builder”写成一个几百行字符串模板。

这也是 Knowledge Layer 和 Runtime Layer 必须分开的原因。
