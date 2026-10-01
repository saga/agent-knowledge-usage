# Open Knowledge Format (OKF)

Source: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing

Published: 2026-06-12

## Core proposal

Google Cloud introduced Open Knowledge Format (OKF) v0.1 as a vendor-neutral, human- and agent-friendly representation for portable knowledge.

The published shape is deliberately simple:

directory → Markdown files → YAML frontmatter → normal Markdown links

The format can represent concepts such as datasets, tables, metrics, playbooks, runbooks and APIs.

## Design principles

### Minimally opinionated

The interoperability surface is intentionally small. A concept needs a type, while producers can choose domain-specific fields and Markdown sections.

### Producer / consumer independence

A human, metadata pipeline or one LLM can produce the files and another tool or agent can consume them.

### Format, not platform

The format is not tied to a database, cloud, model provider or agent framework.

## Why this matters

OKF treats knowledge portability as a representation problem rather than as a requirement for another centralized knowledge service.

That is relevant to:

- Common Agent Library;
- version-controlled team knowledge;
- enterprise metadata;
- data semantics;
- cross-agent knowledge exchange.

## Important limitation

OKF is a representation / interchange format. It does not itself solve:

- semantic correctness;
- ontology alignment;
- freshness;
- contradiction resolution;
- retrieval;
- authorization;
- policy enforcement.

Therefore it fits best as a portable knowledge interchange layer inside a larger Knowledge Architecture.

## Relation to the roadmap

The most important idea for the roadmap is:

> The durable boundary can be a portable Knowledge Asset format, while retrieval and runtime infrastructure remain replaceable.