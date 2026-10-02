# Externalization in LLM Agents：把 Agent 能力从模型内部搬到系统外

来源：https://arxiv.org/abs/2604.08224  
发布时间：2026-04-09

## 这篇综述提供了一个很有用的总框架

近年来很多 Agent 技术看起来彼此独立：

- RAG；
- Memory；
- Skills；
- MCP；
- A2A；
- Sandbox；
- Evaluation；
- Harness。

把它们放在一起看，会发现共同趋势：

> 越来越多原本希望模型自己完成的能力，被外置成可以独立管理的系统组件。

可以画成：

~~~text
Model capability
      ↓
externalize what must persist / be governed
      ↓
Memory
Skills
Protocols
Tools
State
Sandbox
Evaluation
Harness
~~~

## 为什么“外置”比“让模型更聪明”更重要

模型提升主要增加：

- reasoning quality；
- language understanding；
- planning ability。

但很多企业问题根本不是模型智力问题：

### 状态持久化
模型不是 durable database。

### 权限
模型不是 authorization service。

### 工具
模型不能直接变成 enterprise system。

### 业务定义
模型不知道组织内部某个指标真正是什么意思。

### 审计
模型输出不是可靠的 regulatory evidence store。

所以真正的系统能力来自：

~~~text
Model intelligence
+
External system guarantees
~~~

## Memory、Skill、Protocol 各自外置了什么

### Memory
把跨时间经验外置。

### Skill
把 procedural knowledge 外置。

### Protocol
把 Agent 与 Agent / Tool 的交互结构外置。

### Harness
把上下文、工具、sandbox、evaluation、limits 等组织起来。

这不是简单“把 prompt 拆文件”，而是把长期依赖变成独立生命周期的系统资产。

## 一个重要推论

能力外置以后，新的问题不再是“这个能力会不会”。

而是：

> 这个能力是谁拥有、谁能改、什么版本、何时生效、谁能使用？

因此 externalization 必然带来 governance。

~~~text
External Capability
      ↓
Owner
Version
Scope
Permission
Evidence
Evaluation
~~~

## 对当前项目的意义

这很好地解释为什么当前几个看似不同的项目其实属于同一条路线：

~~~text
Knowledge
Memory
Skills
Tools
State
Workflow
Sandbox
Evaluation
Governance
~~~

Common Agent Library 更应该定义这些 capability 的边界和契约，而不是再次创建一个“大 Agent 类”。

## 但不要把一切都外置

外置也有代价：

- 更多组件；
- latency；
- consistency 问题；
- version coordination；
- operational cost。

所以原则不应是“能外置就外置”，而是：

> 需要持久化、共享、治理、独立更新或受到确定性约束的能力，才值得成为外部 primitive。
