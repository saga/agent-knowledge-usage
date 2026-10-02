# Snowflake 上的 Ontology、Knowledge Graph 与 Semantic Layer 实现模式

来源：https://snowflakewiki.medium.com/ontology-knowledge-graphs-the-semantic-layer-on-snowflake-the-implementation-c1c0d4a4cb09  
发布时间：2026-09-14

## 这篇文章值得看什么

它不是 Snowflake 官方架构规范，而是一种很具体的实现探索：把 physical storage、ontology metadata、generated views、semantic models 和 Agent / UDF 组合起来。

因此它更适合当作 implementation pattern，而不是产品事实。

## 五层结构

~~~text
Physical data
    ↓
Ontology metadata
    ↓
Generated views
    ↓
Semantic model
    ↓
Agent / UDF
~~~

其价值在于：业务概念不必硬编码在 application code。

## Physical Graph

文章使用 node / edge tables。

Node 可保存：

- id；
- type；
- properties；
- source system；
- validity dates。

Edge 保存：

- source；
- target；
- relationship type；
- relationship properties；
- validity dates。

这种结构的好处是 ontology 增长时，不必每增加一个 class 就重新改物理表结构。

## Ontology Metadata

Ontology 层记录：

- classes；
- parent classes；
- property schemas；
- relationships；
- cardinality；
- relationship property schemas；
- validation rules；
- derived rules。

这里最值得吸收的不是某几个字段，而是：

> Ontology 本身可以作为 data/config 管理，而不是 application code 的 if/else。

## Generated Views 为什么有意义

如果 ontology 是 metadata，就可以用编译过程生成：

~~~text
ontology
   ↓
generated logical views
   ↓
agent / analyst
~~~

这和 compiler 很像：

- ontology = source；
- generated semantic view = compiled artifact；
- physical tables = execution substrate。

这样业务模型变化可以通过 metadata 驱动，而不是不停改 Agent 代码。

## 但它没有解决 Governance

真正企业化之后还需要：

- ownership；
- lineage；
- version；
- authorization；
- entitlement；
- conflict handling；
- provenance；
- evaluation。

特别是“ontology metadata 谁都能改”本身就是一个风险。

## 与 Snowflake 官方 Semantic View 的关系

Snowflake 当前官方 Semantic Views 本身已经把 business entities、relationships、metrics 等提升为数据库的一等对象，并可被 Cortex Analyst 使用。这个实现文章可以视为一种更底层、更自定义的 ontology 编译思路，而不是官方产品的完整替代方案。

## 对当前项目

这篇文章支持一个值得继续保留的方向：

~~~text
Business Definition
   ↓
Ontology
   ↓
Derived Semantic Views
   ↓
Agent
~~~

也支持：

> 不要为了建立 ontology，就先创造另一套完全独立的物理数据库。

如果现有 Snowflake / Postgres / catalog 已经是事实来源，ontology 可以先作为 metadata / semantic layer 演进。
