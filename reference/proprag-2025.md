# PropRAG: Guiding Retrieval with Beam Search over Proposition Paths

Source: https://aclanthology.org/2025.emnlp-main.317/
Publication: EMNLP 2025

## Core problem

Traditional triples can flatten important semantics such as:

- conditionality;
- provenance;
- n-ary relationships;
- natural-language context.

## Main idea

PropRAG retrieves along paths of propositions instead of treating isolated triples as sufficient knowledge units.

This keeps more natural-language meaning while retaining graph structure.

## Strategic implication

A useful architecture can be:

Source → Proposition → Graph relation → Proposition path → Evidence Pack

This directly supports the principle that graph structure and natural-language evidence should coexist.