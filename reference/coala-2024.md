# Cognitive Architectures for Language Agents（CoALA）

来源：https://arxiv.org/abs/2309.02427  
年份：2024

## 为什么需要 CoALA 这样的视角

把 Agent 写成：

~~~text
prompt → LLM → tool → answer
~~~

很容易把很多不同性质的东西混成一个“Agent State”。

CoALA 借用了认知架构的思想，把 Agent 拆成工作记忆、长期记忆、行动、环境交互和 reasoning 等结构。

它的价值不是给生产系统提供一套固定组件，而是提醒工程师：

> Agent 是一个带内部状态、外部环境和记忆机制的系统，不只是一次模型调用。

## 对 Knowledge / Memory 的重要区分

工作记忆解决“这一刻我要处理什么”。

长期记忆解决“过去我知道什么 / 经历过什么”。

环境交互解决“外部世界现在是什么状态”。

因此：

~~~text
Working Context
    ≠
Long-term Memory
    ≠
External World State
~~~

这恰好对应企业 Agent 中：

~~~text
Context
Memory
Business State
~~~

三个容易混淆的层。

## 为什么这对当前架构重要

如果所有东西都存进一张 conversation history：

- 旧状态会长期污染当前任务；
- business state 变更不容易被发现；
- memory 与 current observation 无法区分；
- context 越积越大。

更合理的结构是：

~~~text
Current Context
   +
Retrieved Knowledge
   +
Relevant Memory
   +
Current Business State
   +
Tool Observations
~~~

最后才形成模型看到的 context。

## CoALA 不是企业控制模型

认知架构适合描述“Agent 如何工作”。

但金融/企业系统还需要另一条控制链：

~~~text
Identity
→ Entitlement
→ Policy
→ Authorization
→ Command
→ Domain
~~~

所以不能因为 CoALA 把 Action 当 Agent primitive，就让 Agent 自己获得业务授权。

## 对当前项目的意义

CoALA 支持长期架构里的 primitive-first 思路：

Memory、Tool、Knowledge、Context 都应该有自己的契约，不应该全部藏在一个 Agent class 里。
