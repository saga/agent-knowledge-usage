# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

来源：https://arxiv.org/abs/2310.11511  
会议：ICLR 2024

## Self-RAG 在修正什么

经典 RAG 常常是：

~~~text
每个问题
→ 固定检索 k 个 chunk
→ 放进 prompt
~~~

这隐含了一个不一定成立的假设：每次回答都需要同样多的外部知识。

Self-RAG 的变化是让模型判断什么时候检索、什么时候生成、什么时候检查已经生成的内容。

于是：

~~~text
reason
 ↓
retrieve if useful
 ↓
generate
 ↓
critique
 ↓
continue / revise / retrieve again
~~~

## 为什么对 Agent 很关键

Retrieval 从 middleware 变成了 decision。

也就是说：

> “要不要继续找证据”本身就是 reasoning problem。

这条思路后来自然延伸到 agentic search、iterative retrieval、tool selection 和 evidence verification。

## 但模型自己决定检索也有风险

可能出现：

- 明明需要证据却不查；
- 查了低质量来源；
- 找到一个结果就停止；
- 当前答案看起来合理，就提前结束验证。

所以：

~~~text
adaptive retrieval
≠
uncontrolled retrieval
~~~

企业系统仍然需要：

- retrieval policy；
- permitted sources；
- scope / entitlement；
- source authority；
- verification criteria。

## Evidence 角色的变化

传统 RAG：

~~~text
retrieved chunk
~~~

就是输入。

Self-RAG 更接近：

~~~text
candidate evidence
   ↓
reason
   ↓
critique
   ↓
accepted evidence
~~~

所以 Knowledge Access 最终不应只返回字符串，还应支持 source、passage、relevance、authority、timestamp、citation location 等信息。

## 和 Business Knowledge 的关系

企业 Agent 可能面对三类问题：

### 事实查询
需要 canonical source。

### 业务定义
需要 semantic layer。

### 判断与行动
需要 policy、skill、workflow 和 evidence。

Self-RAG 主要解决“什么时候继续找证据”，不能替代这些层。

## 对当前项目

下一阶段的 KnowledgeAccess 不应只有：

~~~text
search(query) -> documents
~~~

更值得设计的是：

~~~text
search(query, scope, filters)
→ evidence candidates
→ agent decides
→ verify / expand
→ evidence pack
~~~

这已经开始接近 Agentic Retrieval。
