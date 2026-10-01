# Contextual Retrieval

Source: https://www.anthropic.com/engineering/contextual-retrieval

## Main idea

Before embedding or indexing a chunk, add context that explains where the chunk belongs in the larger document.

## Reported experiment

Anthropic reported:

- Contextual Embeddings: top-20 retrieval failure 5.7% → 3.7%, about 35% reduction
- Contextual Embeddings + Contextual BM25: 5.7% → 2.9%, about 49% reduction
- adding reranking: about 67% reduction

These figures apply to Anthropic's described experimental setup.

## Strategic implication

Retrieval units can be small, but semantic context cannot be blindly discarded.

Important ingestion information includes:

- document identity;
- section context;
- local context;
- lexical aliases;
- metadata;
- reranking signals.