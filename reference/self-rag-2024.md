# Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

Source: https://arxiv.org/abs/2310.11511
Publication: ICLR 2024

## Main idea

Self-RAG argues that always retrieving a fixed number of passages is not ideal.

The model learns a loop of:

retrieve when useful → generate → critique → continue or revise

## Why it matters

Retrieval becomes part of reasoning rather than a fixed preprocessing step.

The paper reports strong results across open-domain QA, reasoning, fact verification and long-form generation, including improvements in factuality and citation accuracy.

## Strategic implication

The roadmap should progress from:

always RAG

toward:

adaptive knowledge access

where the Agent can decide when more evidence is needed.