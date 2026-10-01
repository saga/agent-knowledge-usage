# ReAct: Synergizing Reasoning and Acting in Language Models

Source: https://arxiv.org/abs/2210.03629
Publication: ICLR 2023

## Core idea

ReAct interleaves reasoning and actions:

Thought → Action → Observation → Thought

## Knowledge relevance

Knowledge access becomes part of the action loop:

reason → search → observe → reason → tool call → observe

This is a conceptual bridge from static RAG to agentic retrieval and tool use.

## Strategic implication

A mature Agent should be able to decide when knowledge access or external action is necessary instead of blindly retrieving everything up front.