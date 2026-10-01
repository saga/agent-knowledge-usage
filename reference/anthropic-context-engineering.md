# Effective Context Engineering for AI Agents

Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Main idea

Context is a finite computational resource.

Agent engineering therefore asks not only “what prompt should be written?” but also:

What information should be present in the model's active context at this exact step?

## Important patterns

- progressive disclosure;
- just-in-time retrieval;
- lightweight identifiers;
- tool-based context loading;
- filesystem / environment state;
- memory;
- avoiding unnecessary context growth.

## Strategic implication

Context Engineering is the layer that assembles:

Instructions + Knowledge + Memory + State + Tool Results + Evidence

before the model makes an important decision.