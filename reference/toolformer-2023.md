# Toolformer: Language Models Can Teach Themselves to Use Tools

来源：https://arxiv.org/abs/2302.04761  
年份：2023

## Toolformer 解决的问题

一个基础模型会语言推理，不代表它知道什么时候应该使用 calculator、search、calendar 或其他外部 API。

Toolformer 研究让模型自己学习：

- 什么时候调用工具；
- 调用哪个工具；
- 用什么参数；
- 如何利用返回结果继续生成。

因此：

~~~text
Language Model
   +
Tool Invocation
   +
Tool Result
~~~

开始成为一个统一能力。

## 最重要的架构变化

过去通常把 Tool 当成系统程序：

~~~text
Application decides
   ↓
Call tool
   ↓
Send result to model
~~~

Toolformer 探索的是：

~~~text
Model
   ↓
decide
   ↓
tool call
   ↓
observation
~~~

这一步直接铺垫了今天 Agent Tool Use。

## 这和 MCP / Capability 有什么关系

Toolformer 研究的是“模型如何学会用工具”。

MCP、Tool Registry 等解决的是“工具如何被 Agent 发现和调用”。

所以二者不是同一层：

~~~text
Tool protocol / registry
    ↓
what tools exist
    ↓
Agent / model
    ↓
which tool to use
    ↓
execution system
~~~

一个解决 capability surface，一个解决 tool selection。

## Tool Use 的三个边界

必须区分：

### Tool exists
系统里有这个工具。

### Tool is available
当前 Agent / Session 能看到这个工具。

### Tool is authorized
当前身份、请求和风险条件允许执行。

模型能做前两步的决策，并不意味着它拥有第三个权限。

## 对企业 Agent 的启发

Tool 接口应该表达：

- schema；
- input constraints；
- risk；
- side effect；
- scope；
- result shape。

但真正的 authorization 不应放进 tool description 或 prompt。

否则 prompt injection 可以把“不要调用这个工具”与“系统真的不允许调用”混为一谈。

## 对当前项目

Common Agent Library 应该把：

~~~text
Tool
Capability
Permission
Authorization
Policy
~~~

分开。

Toolformer 证明的是 tool use 可以成为模型能力的一部分；它不是企业授权模型。
