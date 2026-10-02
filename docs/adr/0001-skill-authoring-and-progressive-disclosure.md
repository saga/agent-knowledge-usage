# ADR-0001: Agent-facing Skill 的写法采用渐进披露与可执行流程

- Status: Accepted
- Date: 2026-10-02
- Scope: skills/ 下全部研究型 SKILL.md
- Decision: 采用“短主流程 + 按需 reference + 明确完成标准”的 Skill 结构

## Context

当前研究库的 Skill 已经积累了较多研究纪律，但逐渐出现两个问题：

1. SKILL.md 同时承担“运行指令”和“完整研究手册”，导致主文件过长。
2. Skill 之间虽然职责不同，但写法不完全一致，触发条件、输入、步骤、完成标准和输出契约有时混在一起。
3. 长文档容易让 Agent 在真正执行步骤之前消耗上下文，也容易把参考资料误当成当前步骤。
4. 业界研究尤其容易形成固定厂商偏见，因此“研究流程本身”需要成为可执行约束，而不能只写成背景说明。

本 ADR 参考了两个公开 Skill 集合：

- Anthropic Skills: https://github.com/anthropics/skills
- Matt Pocock Skills: https://github.com/mattpocock/skills

## Reference findings

### 1. Anthropic：Skill 是一个触发器 + 执行指令 + 按需资源

Anthropic 的 Skill Creator 明确强调：

- YAML frontmatter 中 name / description 是 Skill 的核心入口；
- description 同时承担“做什么”和“什么时候使用”的触发作用；
- Skill 使用 progressive disclosure：metadata → SKILL.md → bundled resources；
- SKILL.md 应保持较小，复杂资料放到 references；
- 多分支任务按 variant 拆 reference；
- 指令应使用直接、可执行的 imperative form；
- 输出结构、步骤和完成标准应该写清楚；
- 复杂 Skill 适合通过真实任务反复评估并迭代。

本仓库采用其中与研究型 Skill 直接相关的部分。

### 2. Matt Pocock：Skill 应该像工程流程，而不是长篇说明书

参考：

- writing-for-agents/SKILL.md
- writing-for-agents/SKILL-MECHANICS.md
- engineering/research/SKILL.md
- engineering/diagnosing-bugs/SKILL.md
- engineering/domain-modeling/SKILL.md

可复用的核心做法：

- model-invoked Skill 的 description 是持续加载的 context pointer，所以 trigger wording 要精确；
- 主流程优先，参考资料按需加载；
- 每一步要有 completion criterion，避免 Agent 提前宣布完成；
- 通过共享术语减少重复解释；
- 删除 no-op、重复和环境中已经可以直接查到的信息；
- 复杂流程通过短步骤、检查点和明确边界驱动；
- ADR 只记录真正的架构 / 工作方式决策。

## Decision

### 1. 统一 Skill 顶部结构

新的研究型 Skill 默认按：

~~~
frontmatter
# Skill
## Use this skill when
## Operating contract
## Execute the loop / phases
## Completion / Stop
## Output
## Quality gate
~~~

组织。

不要从背景长文开始。

### 2. description 是触发协议

description 必须同时回答：

- 这个 Skill 做什么；
- 什么用户任务应该触发它。

对于 model-invoked Skill，description 写成足够明确的 context pointer。

本仓库的五个研究 Skill 都保持 model-invoked，因为它们需要能被 Agent 根据任务类型自动选择。

### 3. Progressive disclosure

主 SKILL.md 只保留真正影响当前执行的：

- trigger；
- inputs；
- workflow；
- decision rules；
- completion criteria；
- quality gate。

长表格、完整字段定义、扩展研究协议放到 references。

这次实际应用：

- deep-research 的完整旧协议移动到 skills/deep-research/references/full-research-protocol.md；
- industry-practice-research 的完整旧协议移动到 skills/industry-practice-research/references/vendor-research-protocol.md。

### 4. 每一步必须有“完成标准”

研究型 Skill 不能只有“做 A、做 B、做 C”。

每个阶段要说明：

> 什么条件成立后，Agent 可以进入下一阶段？

尤其关注：

- research question；
- source coverage；
- claim evidence；
- counterevidence；
- conflict resolution；
- synthesis stability；
- final unknowns。

### 5. 把“不要做什么”改成“应该做什么”

禁止语句只保留真正需要的 guardrail。

优先写成：

- “按 source family 计算独立证据”；
- “把 Unknown 保留下来”；
- “先找反例再写 common pattern”；
- “按 responsibility 聚类，而不是按产品名聚类”。

这样更容易形成稳定执行行为。

### 6. 把 Research 与 Synthesis 分开

Deep Research 负责得到可靠证据链。

Academic / Industry 负责领域特定研究方法。

Evidence Review 负责判断 Claim 是否被证据支撑。

Knowledge Synthesis 负责跨来源抽象。

不要让一个 Skill 同时承担所有职责。

### 7. 脚本只解决 deterministic work

继续采用当前仓库既有原则：

适合脚本：

- URL / citation consistency；
- JSON registry；
- duplicate detection；
- 日期 / 版本字段；
- 固定结构。

不适合脚本：

- semantic entailment；
- primitive equivalence；
- industry maturity；
- architecture judgment。

这与本仓库“不用测试、不过度工程化”的约束一致；本 ADR 不引入 skill eval 测试套件。

### 8. 保留 Agent-facing 长期词汇

稳定的 leading terms 继续复用，例如：

- Claim；
- Source Family；
- Counterevidence；
- Load-bearing Claim；
- Vendor Expansion；
- Candidate Primitive；
- Responsibility Boundary。

这样多个 Skill 可以共享同一套研究语言，而不是每个 Skill 重新发明术语。

## Consequences

### Positive

- SKILL.md 更短，进入上下文后的噪声更少；
- Agent 更容易知道“现在该做什么”和“什么时候算做完”；
- 长研究协议仍然保留，只在需要时加载；
- 五个 Skill 的写法更加一致；
- Industry Skill 的 vendor expansion 约束更容易被每次研究真正执行；
- Knowledge Synthesis 更明确地成为研究之后的独立步骤。

### Trade-offs

- Agent 需要在必要时读取 reference 文件；
- reference 文件与主 Skill 需要保持一致；
- 过度压缩 Skill 也可能隐藏当前步骤真正需要的信息，因此不能为了行数而机械拆分。

## Non-goals

本 ADR 不决定：

- 研究工具选型；
- 是否使用 subagent；
- 具体 vendor 清单；
- 具体 Agent framework；
- 论文综述是否必须 PRISMA；
- 是否建设新的自动化测试系统。

## References

### Anthropic

- https://github.com/anthropics/skills
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- https://github.com/anthropics/skills/blob/main/template/SKILL.md
- https://agentskills.io/specification

### Matt Pocock

- https://github.com/mattpocock/skills
- https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/research/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md
- https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md
