# Agent Skills

Source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
Related: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Core model

A Skill packages domain expertise, workflows, instructions, scripts and reference material into a reusable filesystem-based capability.

Typical structure:

skill/
  SKILL.md
  reference/
  scripts/
  templates/

## Progressive disclosure

Agents load:

1. metadata for discovery;
2. SKILL.md when the skill matches;
3. referenced files only when needed;
4. executable resources when necessary.

## Strategic implication

A Skill is a packaging boundary for procedural knowledge.

Knowledge = what is true
Skill = how to accomplish a class of tasks
Tool = a capability that reads or changes the world

This makes Skills complementary to Knowledge Base and MCP rather than a replacement for either.