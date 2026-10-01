# Ontology, Knowledge Graphs & the Semantic Layer on Snowflake — The Implementation

Source: https://snowflakewiki.medium.com/ontology-knowledge-graphs-the-semantic-layer-on-snowflake-the-implementation-c1c0d4a4cb09

Published: 2026-09-14

## Main architecture

The article demonstrates a five-layer intelligence stack implemented in Snowflake:

1. physical storage;
2. ontology metadata;
3. generated views;
4. semantic models;
5. agent / UDF layer.

## Physical graph layer

The implementation uses node and edge tables.

Nodes carry:

- id;
- type;
- flexible properties;
- source system;
- validity dates.

Edges carry:

- source and target node;
- relationship type;
- relationship properties;
- validity dates.

The physical schema therefore stays stable as the ontology grows.

## Ontology layer

Meaning is stored separately from physical data through metadata describing:

- classes;
- parent classes;
- property schemas;
- relationships;
- cardinality;
- relationship property schemas;
- validation / constraint rules;
- derived rules.

A key design principle is:

> Ontology is configuration / data, not application code.

Adding an entity type therefore does not require changing the physical schema.

## Generated views

A compiler-like procedure reads ontology metadata and generates class and hierarchy views.

This gives the architecture:

physical representation → ontology → generated semantic views

That is particularly interesting for Data Agents because the Agent can operate over business concepts instead of raw warehouse structures.

## Enterprise interpretation

For financial services and data agents, the useful model is:

Business Definition → Ontology → Semantic Layer → Data / Knowledge / API → Agent

The ontology and semantic layer should supply authoritative meaning; RAG alone should not force the model to infer business definitions.

## What still needs to be added in production

The article is an implementation pattern, not a complete enterprise governance system. Production environments still need:

- ownership;
- lineage;
- authorization / entitlement;
- semantic versioning;
- conflict handling;
- provenance;
- evaluation;
- safe tool execution.