# Improving language models by retrieving from trillions of tokens (RETRO)

Source: https://arxiv.org/abs/2112.04426
Publication: 2022

## Core idea

RETRO scales retrieval-augmented language modeling to very large external corpora.

The model retrieves neighboring text from an external database and conditions generation on it rather than expecting all useful information to live in parameters.

## Strategic relevance

RETRO reinforces a key idea:

> Model capacity and knowledge capacity can scale independently.

For Agent architecture, the implication is that the external knowledge layer can grow without requiring proportional changes to the foundation model.