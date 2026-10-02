# ReAct: Synergizing Reasoning and Acting in Language Models

来源：https://arxiv.org/abs/2210.03629  
会议：ICLR 2023

## ReAct 为什么重要

ReAct 最核心的贡献不是又发明了一种 prompt 写法，而是把“想”和“做”放到了同一个循环里。

~~~text
Thought
  ↓
Action
  ↓
Observation
  ↓
Thought
  ↓
Action
~~~

这与只生成一段最终答案的模型有本质区别。模型可以在中间访问外部环境，根据真实结果调整下一步。

## Knowledge 为什么因此变了

静态问答是：

~~~text
question → answer
~~~

ReAct 更接近：

~~~text
question
  ↓
reason
  ↓
search / tool
  ↓
observe
  ↓
reason again
~~~

于是 Knowledge Access 不再是“回答之前统一做的一次 preprocessing”。

检索本身成为行动，观察结果又反过来改变后续 reasoning。

## ReAct 的价值和边界

它特别适合：

- 信息不完整的问题；
- 需要外部事实的问题；
- 多步环境交互；
- 工具结果会影响下一步计划的任务。

但它也带来成本：

- 每一步都可能增加 latency；
- 错误 action 会污染后续 state；
- 模型可能反复搜索；
- 工具选择和停止条件需要控制。

所以：

> ReAct 说明 Agent 可以在推理中使用工具，但没有替系统解决“什么时候必须查、谁有权限查、什么时候必须停止”的问题。

## 对 Agent Retrieval 的直接影响

成熟的 retrieval 已经不只是：

~~~text
retrieve top-k
~~~

而是：

~~~text
decide whether to retrieve
→ formulate query
→ inspect result
→ determine whether evidence is enough
→ retrieve again or continue
~~~

这就是 Agentic Retrieval 的基本形态。

## 与 Workflow 的关系

ReAct 的循环是 probabilistic。

企业 Workflow 更适合表达确定性约束：

~~~text
Agent reason
   ↓
Policy gate
   ↓
Tool
   ↓
Business validation
   ↓
Next workflow state
~~~

因此不是 ReAct 或 Workflow 二选一，而是：

> Agent 决定局部 reasoning，Workflow / Policy 决定不可绕过的边界。

## 对当前项目的关系

ReAct 支持一个重要 primitive：

> Observation 必须回到 Agent，而不是让工具调用成为黑盒。

Knowledge、Tool、Memory、Business State 最终都应该能以可验证的 Observation 进入 context。
