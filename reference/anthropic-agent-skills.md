# Agent Skills

来源：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview  
相关：https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Skill 解决的不是“知识检索”

Skill 解决的是：

> 已经知道目标是什么以后，如何把一类任务稳定地做出来。

典型目录：

~~~text
skill/
  SKILL.md
  references/
  scripts/
  templates/
~~~

里面可以同时放 instructions、参考资料、脚本和模板。

因此 Skill 更接近 procedural knowledge，而不是 factual knowledge。

## Progressive Disclosure 为什么重要

Anthropic 的设计不是启动时把所有 Skill 内容全部塞给模型。

而是：

~~~text
metadata
  ↓
SKILL.md
  ↓
reference files
  ↓
scripts / resources
~~~

只有与当前任务有关的内容才进入 context。

这其实是一个上下文管理方案。

Skill 越多，越不能靠“所有 Skill 全部常驻 prompt”解决。

## Skill 与 Tool 的边界

一个 Skill 可以告诉 Agent：

- 先检查什么；
- 什么顺序做；
- 什么结果算完成；
- 哪些脚本可以复用；
- 哪些资料值得参考。

但 Skill 本身不应该成为安全边界。

例如：

~~~text
Skill:
“交易提交前先检查 suitability。”
~~~

不能等价于：

~~~text
System:
“只有 suitability passed 才允许交易。”
~~~

后者必须在 Policy / Domain / Command 层真正执行。

## Skill 与 Knowledge 的关系

可以保留：

~~~text
Knowledge = what
Skill = how
Tool = capability
Policy = boundary
~~~

四者组合后，Agent 才能做真正的业务工作。

## 重要的工程细节

Anthropic 的 Skills 文档还强调一个现实问题：Skill 本身占用 context。

因此技能应该：

- 描述清楚触发条件；
- 保持主体简洁；
- 复杂资料拆到 reference；
- 脚本交给确定性执行环境；
- 不把所有细节全部写在 SKILL.md。

## 对当前项目

这直接支持当前仓库的研究 Skill 结构。

研究型 Skill 也应该：

- frontmatter 负责发现；
- SKILL.md 负责工作流程；
- 更长的标准和案例放到 reference；
- 脚本负责确定性操作。

这比写一个几千行的万能 Agent Prompt 更容易维护。
