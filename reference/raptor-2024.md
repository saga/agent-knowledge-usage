# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

Source: https://arxiv.org/abs/2401.18059
Publication: 2024

## Core idea

RAPTOR recursively clusters and summarizes lower-level text into a tree of higher-level abstractions.

The query can retrieve at different abstraction levels.

## Why it matters

This gives Summary a correct architectural role:

- low-level nodes preserve detail;
- higher-level nodes support broad synthesis;
- retrieval chooses the right abstraction level.

The important lesson is:

> Summary can be a retrieval view without becoming the canonical source of truth.