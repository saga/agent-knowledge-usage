# OpenAI File Search / Retrieval

Source: https://developers.openai.com/api/docs/guides/tools/file-search

## Current product model

OpenAI File Search is a hosted tool that lets models retrieve information from uploaded vector stores using semantic and keyword search. The platform handles parsing, chunking, embeddings, indexing and retrieval.

## Retrieval controls

The current API exposes vector stores, metadata / attribute filtering, query rewriting, result limits, ranking options, score thresholds and hybrid semantic / text weighting.

## Strategic implication

This is a concrete example of Agent platforms turning Knowledge Access into a tool / capability rather than forcing application code to concatenate documents into prompts.

A portable Common Agent Library should therefore abstract:

Knowledge Access = search + filter + rank + evidence

rather than binding Agent code directly to one vector database.
