# Databricks：从 Unity Catalog Semantics 到 Genie Ontology

研究日期：2026-10-02

## 1. 核心判断

Databricks 当前出现了一个非常值得关注的演进：从“数据治理目录”走向“业务语义 + 自动推断知识”的统一 context layer。

核心对象包括 Unity Catalog semantics、Metric Views、Domains / Subdomains、Pages、Certification / Deprecation、Genie Ontology、Inferred context。

- https://docs.databricks.com/aws/en/uc-semantics
- https://docs.databricks.com/aws/en/uc-semantics/metric-views
- https://docs.databricks.com/aws/en/genie/genie-ontology

## 2. 显式业务知识：Unity Catalog Semantics

Databricks 把显式业务语义放入 Unity Catalog：

```text
Unity Catalog Semantics
├── Metric Views
├── Domains
├── Pages
└── Certification / Deprecation
```

Metric View 把 business measure 与 dimensions 解耦。它定义指标一次，runtime 再决定如何按不同维度分析。

Metric View 本身是 governed Unity Catalog object，因此业务指标的定义、访问和生命周期进入统一治理面。

## 3. Agent Metadata

Databricks 允许在 Metric View YAML 中加入 display names、synonyms、formatting、semantic metadata。这些 metadata 会被 Genie Agents 使用。

例如：

```yaml
name: total_revenue
expr: SUM(o_totalprice)
synonyms:
  - revenue
  - total sales
```

这说明“给 LLM 的知识”不一定需要变成独立文档，也可以附着在业务语义对象上。

https://docs.databricks.com/aws/en/uc-semantics/agent-metadata

## 4. Genie Ontology：更进一步

2026 年 Databricks 的 Genie Ontology 是这一领域更重要的变化。官方将其定义为统一 context layer，把两类知识汇合：

### Modeled context

企业显式定义、治理和认证的：
- Metric Views
- Domains
- Pages

### Inferred context

Genie 根据既有资产和使用情况自动抽取并持续维护，例如：
- metric definitions
- authoritative sources
- business rules

因此：

```text
Human Modeled Context
        +
Inferred Context
        ↓
Genie Ontology
        ↓
Genie / Genie Code
```

官方还说明 ontology snippet 有 authority score，会考虑来源、使用频率和 freshness，并继承 Unity Catalog permissions。

## 5. Agent 如何使用

Genie / Genie One 不只是搜索一个 vector store，而是：

```text
User question
   ↓
Search relevant agents / assets
   ↓
Search Genie Ontology
   ↓
Rank relevant context
   ↓
Resolve conflicts
   ↓
Use permitted sources
   ↓
Answer + citations
```

Genie One 还可以搜索 dashboards、queries、metric views 以及外部来源。

https://docs.databricks.com/gcp/en/genie-one/chat

## 6. Databricks 的 Knowledge 哲学

可以概括为：

> Business Knowledge = modeled semantics + inferred context + governed source assets

这比“Documents → chunks → embeddings”高一个抽象层。

## 7. 对你当前架构的启发

### 7.1 Explicit Knowledge + Inferred Knowledge 双轨

可以考虑：

```text
Authoritative Knowledge
      +
Observed / Inferred Knowledge
      ↓
Knowledge Layer
```

但二者必须有不同 provenance / authority。

### 7.2 Authority 是 Knowledge 一等属性

不是所有知识平等。官方定义、approved semantic definition、certified asset、inferred pattern、agent-generated hypothesis 应该有不同 authority。

### 7.3 Permission 必须进入 Knowledge Retrieval

Databricks 把源资产权限延伸到 inferred ontology snippets。这与你当前 Data Entitlement 的设计原则高度一致。

## 8. 局限

Genie Ontology 强绑定 Databricks / Unity Catalog ecosystem。

Common Agent Library 更适合抽取底层 primitive：

```text
Definition
Metric
Entity
Relation
Authority
Source
Scope
Permission
Freshness
```

然后让 Databricks、Snowflake、Google 成为具体 provider，而不是复制某一家 schema。