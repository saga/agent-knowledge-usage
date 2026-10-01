# Scaling Karpathy's LLM Wiki: Why Your Knowledge Base Needs a Graph

Source: https://neo4j.com/blog/agentic-ai/scaling-karpathy-llm-wiki-graph/

Published: 2026-08-31

## Main thesis

The article argues that Karpathy-style LLM Wiki knowledge bases become harder to search and navigate as the Markdown corpus grows. The proposed answer is a graph index over the Wiki.

The useful distinction is:

folder of Markdown → graph index → structured navigation

## Graph model

The article models:

- Vault
- Folder
- Document
- Section

with relationships for:

- containment;
- section reading order;
- cross-document links.

The graph enables:

- hierarchy traversal;
- multi-hop navigation;
- shortest paths;
- centrality;
- community detection.

## Progressive disclosure

A notable pattern is:

outline → search → get → follow links

Instead of dumping the whole knowledge base into context, the agent first sees a compact map and then progressively opens only the relevant subtree.

This is directly relevant to context engineering.

## Reported benchmark claim

The article reports a Newcastle University / NICD comparison where a graph-enabled agent reportedly achieved more than 2× precision and recall for factual correctness, +80% truthfulness and +69% answer relevancy over a vector-only setup in the described experiment.

These are claims reported by the article and should be verified against the underlying experiment before being used as general evidence.

## Strategic interpretation

The strongest idea is not “everyone should use Neo4j”.

It is:

> Relationships should become first-class navigable state.

A summary can remain a pointer:

summary → section → source

rather than becoming a lossy replacement for the source.

This directly supports the agent-knowledge-usage principle that derived views should remain recoverable to canonical evidence.