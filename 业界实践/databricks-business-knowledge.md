# Databricks：从受治理的语义对象走向显式 + 推断的 Ontology

研究日期：2026-10-02

## 先看结论

Databricks 的路线与 Snowflake 相似，但多走了一步。

Snowflake 更突出“把 business semantics 变成数据库对象”。

Databricks 当前的 Genie Ontology 则进一步加入“从已有资产和实际使用中自动推断上下文，再把显式定义与推断结果放到同一个 context layer”。

官方资料：
- https://docs.databricks.com/aws/en/uc-semantics
- https://docs.databricks.com/aws/en/uc-semantics/metric-views
- https://docs.databricks.com/aws/en/uc-semantics/agent-metadata
- https://docs.databricks.com/aws/en/genie/genie-ontology

## 1. Unity Catalog Semantics 解决“明确告诉系统”

当前显式语义主要包括：

~~~text
Unity Catalog Semantics
├── Metric Views
├── Domains
├── Pages
└── Certification / Deprecation
~~~

Metric View 的意义不仅是保存 SQL，而是让 KPI 定义进入一个受治理的对象。

例如：

~~~text
total_revenue
active_customer
conversion_rate
~~~

这些指标可以有统一定义，并进入 Unity Catalog 权限与生命周期管理。

## 2. Agent Metadata 是小但关键的设计

Databricks 允许给 semantic objects 附加：

- display name；
- synonym；
- formatting；
- semantic metadata。

很多 AI-specific metadata 可以直接附着在已有业务对象上。

这个思路对于当前项目很实用：

> Knowledge metadata 最好跟着真正的资产走，而不是复制一份独立 AI-only copy。

否则很容易出现三套内容：

~~~text
Data Definition
+
AI Definition
+
Documentation Definition
~~~

然后慢慢漂移。

## 3. Genie Ontology 的真正变化

Databricks 当前把 context 分成两条来源。

### Modeled context

企业明确创建、治理、认证：

- Metric Views；
- Domains；
- Pages。

### Inferred context

系统从已有资产和使用情况中自动抽取并持续维护：

- metric definitions；
- authoritative sources；
- business rules；
- existing agent knowledge。

最终：

~~~text
Modeled Context
       +
Inferred Context
       ↓
Genie Ontology
~~~

这和传统 Knowledge Base 的差别很大。

传统思路是“人把所有知识写进去”。

Databricks 开始探索“人定义关键真值，系统从组织已有行为中补足周边知识”。

## 4. Authority Score 为什么很重要

自动推断的知识天然不应该和人工认证的知识拥有相同可信度。

Databricks 给 snippet 建 authority score，并考虑来源、使用频率和 freshness。

这实际上引入了一个重要的 Knowledge primitive：

> Knowledge 不是二值的“存在 / 不存在”，而应该有 authority。

当前项目可以进一步区分：

~~~text
Canonical
Certified
Observed
Inferred
Generated
Hypothesis
~~~

它们都可能有用，但不应该被同样使用。

## 5. Permission 不能和 retrieval 分开

Databricks 文档明确说明 ontology snippet 受到 Unity Catalog permissions 约束。

这解决了一个经常被忽略的问题：

> 如果系统从 dashboard、query、agent 中自动抽取知识，抽出的知识也可能带有原资产的访问边界。

因此：

~~~text
Source permission
      ↓
Inferred knowledge visibility
      ↓
Agent retrieval
~~~

而不是：

~~~text
Source was once indexed
      ↓
everyone can retrieve it
~~~

## 6. 真正难的地方

自动推断 context 会引入：

- stale knowledge；
- source quality differences；
- conflicting definitions；
- popularity bias；
- usage bias；
- false authority。

比如一个错误 SQL 被复制了一年，usage 很高，但并不会因此成为正确的 business definition。

因此 authority score 更适合作为 ranking signal，而不是自动成为 business truth。

## 7. 和 Snowflake 的真正差异

可以粗略理解：

~~~text
Snowflake
Explicit semantic object
        ↓
Agent

Databricks
Explicit semantic object
        +
Inferred context
        ↓
Ontology
        ↓
Agent
~~~

不是谁“更先进”，而是解决的痛点不同。

Snowflake 更强调 semantic object 的治理和可执行性。

Databricks 更进一步探索知识自动积累和 context discovery。

## 8. 对当前项目的启发

Knowledge Foundation 不应该只有 KnowledgeNode。

还应该区分：

~~~text
Knowledge Source
Knowledge Assertion
Knowledge Authority
Knowledge Status
Knowledge Freshness
Knowledge Scope
~~~

更重要的是：

> 自动发现出来的知识和人工批准的知识，应该进入同一模型，但拥有不同状态。

这样才能实现：

~~~text
Documents
+
SQL
+
Dashboards
+
Code
+
Usage
      ↓
Candidate Knowledge
      ↓
Validation
      ↓
Trusted Knowledge
~~~

这比完全手工维护 ontology 更有实际落地可能。

## 9. 局限

Genie Ontology 强依赖 Unity Catalog。

Common Agent Library 应只抽取：

~~~text
Definition
Entity
Metric
Source
Authority
Scope
Freshness
Status
~~~

具体 provider 再负责平台实现。
