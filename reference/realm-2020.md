# REALM: Retrieval-Augmented Language Model Pre-Training

Source: https://proceedings.mlr.press/v119/guu20a.html
Publication: ICML 2020

## Why it matters

REALM showed that retrieval can be integrated into language-model pre-training itself.

Instead of forcing more world knowledge into parameters, a latent retriever can access a large external corpus.

## Evidence

The paper reported 4–16 percentage-point absolute gains over prior Open-QA systems on three benchmarks, together with interpretability and modularity benefits.

It also showed that stale retrieval indexes can hurt performance, making knowledge freshness a systems concern.

## Strategic implication

Model capacity and knowledge capacity do not need to scale in exactly the same place.

This is an early theoretical foundation for treating external knowledge as a modular Agent capability.