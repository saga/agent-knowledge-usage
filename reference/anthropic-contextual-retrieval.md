# Contextual Retrieval

来源：https://www.anthropic.com/engineering/contextual-retrieval

## 它针对一个非常具体的问题

Chunk retrieval 经常有一个上下文丢失问题：

原文里有一句：

> 它在上一季度增长了 18%。

如果 chunk 自己没有公司、指标和章节上下文，这句话做 embedding 后很难和用户查询准确匹配。

Contextual Retrieval 的做法，是在索引前给 chunk 补充它在原文中的上下文。

~~~text
raw document
   ↓
contextualize chunk
   ↓
embedding / BM25
   ↓
retrieval
~~~

## 为什么这个小改动有价值

它解决的是 chunk 的语义孤立问题。

传统：

~~~text
chunk = 纯局部文字
~~~

Contextual Retrieval：

~~~text
chunk = 局部文字 + document context
~~~

这不改变 canonical source，却改变 retrieval representation。

因此它和 RAPTOR 的定位有共同点：

> Retrieval View 可以增强查找，不必改变原始知识。

## Anthropic 报告的实验

Anthropic 在其公开实验中报告：

- Contextual Embeddings：top-20 retrieval failure 从 5.7% 降到 3.7%；
- Contextual Embeddings + Contextual BM25：降到 2.9%；
- 再加 reranking：报告的总体下降约 67%。

这些数字属于 Anthropic 描述的实验设置，不能当作所有企业语料的固定提升。

## 它没有解决的问题

Contextual Retrieval 主要改善 retrieval representation。

它不能单独解决：

- 权限；
- authority；
- contradictory sources；
- business semantics；
- fresh data；
- workflow state。

因此：

~~~text
better retrieval
≠
trusted knowledge
~~~

## 对企业 Knowledge Layer 的意义

Indexing pipeline 可以逐渐从：

~~~text
parse → chunk → embed
~~~

变成：

~~~text
parse
→ identify document / section
→ contextualize
→ metadata
→ embed / lexical index
→ rerank
→ retain source links
~~~

这对企业文档质量提升很实际，而且不会要求先建立复杂 Knowledge Graph。

## 当前项目可以吸收的原则

保留一个明确边界：

> Retrieval representation 可以变得很复杂，但 canonical evidence 必须保持简单、可追踪、可重新生成。

这使未来切换 embedding、reranker、GraphRAG 或其他 retrieval provider 时不会损失知识资产。
