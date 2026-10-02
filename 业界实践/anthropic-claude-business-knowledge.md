# Anthropic / Claude：把知识拆成 Skill、Resource、Memory 和 Context

研究日期：2026-10-02

## 先看结论

Anthropic 的思路和 Snowflake、Databricks、Google 不一样。

它没有先建立统一的 Enterprise Knowledge Object，而是按知识在 Agent 中承担的职责来拆：

~~~text
Procedural Knowledge → Skills
External Resources    → MCP
Persistent Memory     → application-owned memory
Current Context       → Context Engineering
Fresh Web Knowledge   → Web Search
~~~

官方资料：
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://docs.anthropic.com/en/docs/build-with-claude/memory
- https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- https://docs.anthropic.com/en/docs/build-with-claude/context-editing

## 1. Skill 是 Procedural Knowledge

Skill 的基本结构是目录：

~~~text
skill/
├── SKILL.md
├── references/
├── scripts/
└── templates/
~~~

它表达的不是世界上有哪些事实，而是“一类工作应该怎么做”。

所以可以稳定地区分：

~~~text
Knowledge = what
Skill = how
Tool = capability
~~~

## 2. Progressive Disclosure 其实是在管理 Context

Anthropic 的 Skills 设计不是启动时把所有技能全文塞进模型，而是：

~~~text
metadata
  ↓
SKILL.md
  ↓
reference files
  ↓
scripts / resources
~~~

官方 best practices 还明确建议控制 SKILL.md 的规模，把大型参考资料拆出去。

背后的原因不是文件结构漂亮，而是 Skill 本身就是 context cost。

如果有几十个 Skill，全量常驻 prompt，Agent 很快就会失去上下文预算。

## 3. MCP 和 Skill 是不同层

MCP 更像 external interface：

~~~text
Claude
  ↓
MCP
  ├── Resource
  ├── Tool
  └── Prompt
  ↓
Enterprise System
~~~

Skill 则告诉 Agent 什么时候应该使用哪些资源、怎样完成工作。

因此组合方式是：

~~~text
Skill
  ↓
知道怎么做
  ↓
MCP
  ↓
拿到真实数据 / 执行操作
~~~

## 4. Memory 为什么由应用拥有

Anthropic 当前 memory 的设计把实际存储责任留给 application。

模型请求 memory operation，应用再决定将其写到 filesystem、database、cloud storage 或 encrypted store。

这样 memory 的生命周期、权限、删除、retention 和 backup 都可以由应用治理。

对于企业系统，这比“模型自己记住了什么”的黑盒方案更容易控制。

## 5. Context Engineering 是独立的一层

Anthropic 近期实践把 memory、compaction、tool-result clearing 和 just-in-time loading 放到 context management 中。

因此：

~~~text
Knowledge exists
       ≠
Knowledge belongs in current context
~~~

Agent 每一步真正需要的是一个 context projection。

## 6. 它和 Snowflake / Databricks 解决的问题不同

可以粗略理解：

~~~text
Snowflake / Databricks / Google
    先解决 business semantics

Anthropic
    先解决 agent capability externalization
~~~

因此企业系统真正可能采用的组合是：

~~~text
Enterprise Semantic Layer
        +
Knowledge Retrieval
        +
Skills
        +
MCP
        +
Memory
        +
Agent Harness
~~~

而不是要求一个产品把全部问题解决。

## 7. 一个值得直接吸收的设计

Anthropic 把 SKILL.md 作为入口，详细知识放进 references，确定性操作放进 scripts。

这个模式也适用于当前研究库的 Skill：

~~~text
metadata
  ↓
SKILL.md
  ↓
reference material
  ↓
deterministic script
~~~

这样研究方法和研究资料不会混成一个巨大 prompt。

## 8. Skill 不能承担 Security Boundary

例如 Skill 写“执行交易前检查 suitability”，不代表系统真的 enforce 了这一点。

真正的控制仍然应该在：

~~~text
Policy
+
Authorization
+
Domain Validation
+
Command Service
~~~

Skill 只是 procedural guidance。

## 9. 最终判断

Anthropic 的路线提醒我们：

> Knowledge 不一定要成为一个统一的大 Knowledge Store。

事实、程序、外部数据、记忆和当前上下文，可以拥有不同的存储方式和生命周期。

对 Common Agent Library，真正值得统一的是这些能力的 contract，而不是强迫它们使用同一种 Knowledge backend。
