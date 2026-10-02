# NVIDIA：把 Agent 能力做成框架无关的 Toolkit，并把 Memory / Retriever 独立出来

研究日期：2026-10-02

## 先看结论

NVIDIA NeMo Agent Toolkit 的价值与传统 cloud knowledge service 不同。

它更关注 framework-neutral agent orchestration、retriever / embedding provider、tool calling、profiling、evaluation、automatic memory wrapper。

这对 Common Agent Library 很有参考价值，因为它证明：

> Knowledge / Memory / Retrieval 本身可以作为跨 Agent framework 的 capability contract，而不是某个 Agent framework 的内部实现。

## 1. Agent 是可组合的 function

NeMo Agent Toolkit 把 Agent 实现成一种可以编排其他 function 的特殊 function。

这使：

~~~
Agent
   ↓
Function / Tool / Retriever
~~~

天然可组合。

## 2. Automatic Memory Wrapper

NeMo 提供 Automatic Memory Wrapper，为现有 Agent 增加 memory capture 和 retrieval。

说明 memory 可以作为：

~~~
cross-cutting capability
~~~

而不必修改每个 Agent 的主体逻辑。

这和当前 Common Agent Library 设计很接近。

## 3. Retriever Provider 是独立层

NeMo Agent Toolkit 的 framework capability matrix 把 LLM providers、embedding providers、retriever providers、tool calling、profiling 分开。

因此比较合理的抽象不是：

~~~
AgentFramework
   └── BuiltInKnowledge
~~~

而是：

~~~
Agent Runtime
├── Model Provider
├── Embedding Provider
├── Retriever Provider
├── Tool Provider
├── Memory
└── Observability
~~~

## 4. 对当前项目的启发

值得作为 Common Agent Library 的直接参考：

~~~
Retriever
Memory
Tool
Agent
Profiler
Evaluator
Provider Adapter
~~~

特别是 Provider Adapter 和 capability contract 的分离。

## 5. 局限

NVIDIA NeMo Agent Toolkit 更偏 Agent engineering infrastructure，不等价于 enterprise business semantic layer。

它解决的是：

~~~
how to compose and operate agent capabilities
~~~

而不是：

~~~
what is the authoritative business meaning
~~~

所以它应与 Snowflake / Databricks / Palantir / SAP 等路线互补研究。

## Sources

- https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/docs/source/components/agents/index.md
- https://github.com/NVIDIA/NeMo-Agent-Toolkit/blob/develop/docs/source/components/integrations/frameworks.md
- https://docs.nvidia.com/nemo/
