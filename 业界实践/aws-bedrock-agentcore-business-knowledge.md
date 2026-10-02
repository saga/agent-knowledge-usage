# AWS：把 Knowledge、Memory、Agent Runtime 拆成独立能力

研究日期：2026-10-02

## 先看结论

AWS 当前的路线已经从早期 Bedrock Agents 逐渐转向 AgentCore。对 Agent Knowledge 最有价值的不是一个“大一统 Knowledge Object”，而是把 authoritative knowledge retrieval、short-term / long-term memory、agentic retrieval、runtime、policy / guardrail 拆成可以独立组合的服务。

一个重要边界是：

~~~
Authoritative external knowledge
        ↓
Knowledge retrieval

Past interaction / learned facts
        ↓
AgentCore Memory

两者都可以进入
        ↓
Agent context
        ↓
Agent reasoning
~~~

AWS 官方明确区分 long-term memory 与 RAG：Memory 更适合保存用户偏好、过去决策、会话历史和行为模式；RAG 则用于访问大规模、当前且权威的信息源。

## 1. Knowledge：RAG 是独立的 retrieval capability

Bedrock Knowledge Bases / Agentic Retrieval 可以对复杂问题自动拆 query、迭代检索，并判断当前结果是否足够。

这说明 retrieval 已经不只是：

~~~
query → top-k
~~~

而可以是：

~~~
understand query
    ↓
decompose
    ↓
retrieve
    ↓
evaluate sufficiency
    ↓
retrieve again
    ↓
generate
~~~

对于当前项目，这更接近 Agentic Retrieval，而不是传统 Vector RAG。

## 2. Memory：不是第二个文档知识库

AgentCore Memory 明确拆成：

- Short-term memory：当前 session 的原始交互；
- Long-term memory：从历史交互中提取出的事实、偏好、summary、episode 等。

Memory strategy 又负责：

~~~
raw interaction
      ↓
extraction
      ↓
consolidation
      ↓
memory record
      ↓
semantic retrieval
~~~

Semantic memory strategy 会把事实抽取为结构化 memory record，并支持 namespace / metadata / access scope。

这给当前项目一个很明确的设计约束：

> Memory 应该有独立的 write / extraction / consolidation policy，不应该直接把所有聊天记录塞进 Knowledge。

## 3. Agentic Retrieval 可以同时使用 Knowledge + Memory

AWS 当前支持在 Agentic Retrieval 中同时配置 knowledge retrieval、memory、user context、guardrail / policy。

因此 runtime 更像：

~~~
User Context
     +
Knowledge
     +
Memory
     +
Policy
     ↓
Agentic Retrieval
     ↓
Context
     ↓
Agent
~~~

这里尤其值得关注 userContext 对 access-control filtering 的作用：retrieval 不是天然无权限的。

## 4. 对当前 Common Agent Library 的启发

建议保留四个独立 primitive：

~~~
KnowledgeProvider
MemoryProvider
RetrievalPolicy
ContextAssembler
~~~

不要抽象成一个：

~~~
UniversalKnowledgeStore
~~~

AWS 的实践更接近：

~~~
Knowledge ≠ Memory
Retrieval ≠ Storage
Memory write policy ≠ Retrieval
Context ≠ Knowledge
~~~

## 5. 局限

AWS 产品天然依赖 AWS runtime / IAM / managed services。

因此 Common Agent Library 应抽取 Knowledge Retrieval contract、Memory contract、retrieval filters、provenance、namespace、context assembly，而不是复制 AgentCore resource model。

## Sources

- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/semantic-memory-strategy.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-agentic-retrieve.html
- https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-ltm-rag.html
