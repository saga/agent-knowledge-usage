# Anthropic / Claude：Skills、MCP、Memory 与 Context Engineering

研究日期：2026-10-02

## 1. 核心路线

Anthropic 的思路与 Snowflake、Databricks、Google 最不同：不把所有企业知识都建成一个中央 Knowledge Object，而是把知识拆成不同类型的 external capability。

```text
Procedural Knowledge → Skills
External Resources    → MCP
Persistent Memory     → Memory Tool / App Storage
Current Context       → Context Engineering
Fresh Web Knowledge   → Web Search
```

参考：
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://docs.anthropic.com/en/docs/build-with-claude/memory
- https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- https://docs.anthropic.com/en/docs/build-with-claude/context-editing

## 2. Business Knowledge 的核心抽象：Skill

Anthropic 对 Skill 的定义非常值得注意：Skill 是一个包含 instructions、scripts、resources 的可复用能力包。

典型结构：

```text
skill/
├── SKILL.md
├── references/
├── scripts/
└── templates/
```

它表达的是“如何把一类工作做好”，而不是“世界上有哪些事实”。

## 3. Progressive Disclosure

Claude 不会启动时把所有 Skill 全塞进 context。

```text
1. metadata
   ↓
2. SKILL.md
   ↓
3. referenced files
   ↓
4. scripts / resources
```

这意味着 Knowledge 的“存在”和 Knowledge 的“进入 context”是两个不同问题。

## 4. MCP：把外部业务知识变成 Resource / Tool

MCP 可以暴露 tools、resources、prompts。Resource 可以承载 documentation、data、files、application state 和其他 contextual material。

```text
Claude
  ↓
MCP
  ├── Resource
  ├── Tool
  └── Prompt
  ↓
Enterprise System
```

这一模式适合 Jira、SharePoint、Databases、internal APIs、knowledge repositories 和 SaaS systems。

## 5. Memory：与 Knowledge 有意分开

Anthropic 当前 Memory Tool 的重要设计是：memory storage 在 application side，由开发者控制。

Claude 只请求 view / create / update / delete 等 memory operation；应用负责把这些操作落到 filesystem、database、cloud storage 或 encrypted store。

因此 Memory 是 external state，而不是模型自己的 hidden memory。

对于 long-running agent，memory 可以与 context editing、compaction 组合使用：compaction 压缩旧对话，memory 保存需要跨压缩继续存在的信息。

## 6. Context Engineering

Anthropic 把 context 当成有限资源。

当前相关能力包括：
- tool-result clearing
- thinking-block clearing
- server-side compaction
- client-side compaction
- just-in-time loading
- progressive disclosure

核心思想：

```text
Full Knowledge
     ↓
select / load
     ↓
active context
```

而不是把全部知识永久放进 system prompt。

## 7. Fresh knowledge

Claude 还可以通过 web search、MCP connector 获取外部实时信息。新版 web search 支持动态过滤：搜索后先由 code execution 过滤，再把更相关的结果送入模型 context。

这实际上又形成了 retrieval → context optimization 的组合。

## 8. Anthropic 的 Knowledge 哲学

可以概括为：

> 不要建立一个巨大 Knowledge Blob；建立一组可以按需发现、加载和调用的 external cognitive resources。

因此：

```text
Knowledge
  ├── Skill
  ├── Resource
  ├── Memory
  ├── Tool
  └── Current Context
```

各自承担不同职责。

## 9. 对你的架构的启发

### 9.1 Skill 与 Knowledge 必须分离

```text
Knowledge = what
Skill     = how
Tool      = capability
```

这非常适合 `common-agent-lib` / `team-member-copilot-agent` 当前方向。

### 9.2 Knowledge 不一定需要集中式 Knowledge Base

企业知识可能天然属于 Git repo、Jira、Snowflake、SharePoint、Confluence、internal API、file system。

Agent 可以通过 MCP / connector just in time 获取，而不必先复制成新的中心化知识库。

### 9.3 Memory 应该由应用拥有

对于 Team Agent / Member Memory，更适合：

```text
Agent
  ↓
Memory interface
  ↓
Governed storage
```

而不是一个不可控的黑盒 memory database。

### 9.4 Context Engineering 应该成为 Common Layer

无论知识来自哪里：

```text
Skill
Knowledge
Memory
State
Tool Result
Evidence
```

最终都需要进入模型 context。

因此通用抽象应是：

> Context Assembly / Context Policy

## 10. 局限

Anthropic 模式非常适合通用 Agent，但没有像 Snowflake、Databricks 那样提供完整 enterprise business ontology / semantic layer。

金融服务场景仍然需要：

```text
Enterprise Semantic Layer
        +
Claude Agent Harness
```

两者结合，而不是让 Claude 自己猜企业业务定义。