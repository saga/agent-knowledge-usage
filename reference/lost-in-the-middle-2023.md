# Lost in the Middle: How Language Models Use Long Contexts

Source: https://arxiv.org/abs/2307.03172
Publication: 2023

## Core finding

Longer context windows do not automatically mean better information use.

The study found a positional effect in long contexts: relevant information placed in the middle can be used less reliably than information near the beginning or end.

## Strategic implication

The naive strategy:

Load everything → ask model

should become:

Retrieve → select → order → compress → assemble context

Therefore context placement and context budgeting belong to Agent architecture, not prompt cosmetics.