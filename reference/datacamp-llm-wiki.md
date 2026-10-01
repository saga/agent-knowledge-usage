# LLM Wiki: A New AI Knowledge Architecture in 2026

Source: https://www.datacamp.com/blog/llm-wiki

## Core idea

The article describes the 2026 LLM Wiki pattern associated with Andrej Karpathy: instead of repeatedly retrieving raw chunks for every query, an agent compiles source material into a persistent, cross-linked knowledge base during ingestion.

Traditional RAG:

source → index → query-time retrieval → temporary context

LLM Wiki:

source → compilation → persistent knowledge pages → query-time navigation

## Main design elements

- Raw sources remain immutable as an audit trail.
- Ingestion extracts concepts, entities, claims and relationships.
- Existing pages are updated when new sources arrive.
- Contradictions should be surfaced instead of silently overwritten.
- Cross-links turn the corpus into a navigable knowledge structure.
- The compiled knowledge persists across sessions.
- Different agents can consume the same compiled knowledge.

## Trade-offs

RAG has a freshness advantage because it can read source documents at query time. LLM Wiki pays ingestion cost up front and therefore can preserve cross-source synthesis for later queries.

The new risks are stale derived knowledge, compression loss, propagation of extraction errors and maintenance overhead.

## Strategic interpretation

The useful idea is not “replace RAG with Wiki”.

It is:

> Separate knowledge compilation from knowledge retrieval.

A hybrid architecture is therefore natural:

source → knowledge compilation → persistent knowledge layer → RAG / graph / direct navigation → agent

The raw source must remain authoritative and every important compiled claim should retain provenance.

## Agent relevance

This pattern is especially relevant to:

- long-running software agents;
- research agents;
- enterprise organizational memory;
- repeated domain research;
- team knowledge shared across sessions.

## Relation to this repository

This directly supports the rule:

> Summary is a derived navigation view, not the Knowledge source of truth.