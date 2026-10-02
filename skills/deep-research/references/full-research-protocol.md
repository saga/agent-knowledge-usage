---
name: deep-research
description: 对需要多来源检索、证据核验、冲突处理和综合判断的开放问题进行深度研究。适用于业界实践、技术架构、产品能力、论文与项目、技术选型、趋势判断、事实核查和跨来源比较。默认单 Agent，只有存在明确独立研究线程时才并行扩展。
metadata:
  kind: capability
---

# Deep Research

## 1. 这是什么

Deep Research 不是“多搜几个网页”，也不是“把搜索结果整理成长文”。

它解决的是一个开放问题：

> 在资料分散、定义不一致、信息持续变化、来源质量不同、甚至互相矛盾的情况下，怎样逐步得到一个有证据、可复查、知道自己哪里不确定的结论？

研究的基本单位不是网页，而是 **Claim（主张）**。

合格的研究至少应该能回答：

- 我到底要回答什么问题？
- 哪些事实得到来源直接支持？
- 哪些是综合推断？
- 哪些来源实际上来自同一个原始出处？
- 哪些地方存在冲突？
- 哪些关键问题还没有答案？
- 什么新证据出现后，当前结论需要改变？

不要把“来源很多”误当成“研究很深”。

---

## 2. 什么时候使用

### 适合

- 用户明确要求“研究一下 / 深度研究 / 调研”
- 一个搜索无法回答的问题
- 比较多个框架、厂商、架构、论文或实现
- 调查“业界通常怎么做”
- 追踪一个能力从论文到产品再到开源实现的演变
- 判断互相矛盾的说法
- 为架构设计、技术选型或研究路线提供证据
- 产出可反复引用的研究文档

### 不适合

- 单个已知页面读取
- 单个事实查询
- 1–2 个来源即可可靠回答的问题
- 用户已经给出全部材料，只需要总结、翻译或改写
- 纯头脑风暴

### 与其他 Research Skill 的边界

- **academic-literature-review**：论文综述、系统性文献检索、论文筛选更重时优先使用。
- **industry-practice-research**：厂商实践、官方文档、产品能力和实现差异更重时优先使用。
- **evidence-and-claim-review**：已有研究结果需要逐项审计时优先使用。
- **deep-research**：当问题跨越多个证据类型，需要把论文、厂商、开源实现、失败案例放到同一条证据链上时使用。

---

## 3. 先选研究模式

默认选择能回答问题的最小模式，不要所有任务都跑满配。

| 模式 | 适用场景 | 典型做法 |
|---|---|---|
| Quick | 小型事实核查、方向已明确 | 1–2 个角度，少量高质量来源 |
| Standard | 大多数技术研究 | 3–5 个角度，宽搜→深读→反证→综合 |
| Deep | 架构决策、重要比较、争议问题 | 加入独立来源核验、冲突处理、Gap Fill、Adversarial Pass |
| Delta | 已有研究基础上继续第二轮 | 只搜索变化、反例、未解决问题 |

研究深度取决于：

- 问题开放程度
- 来源分散程度
- 信息新鲜度要求
- 决策风险
- 争议程度
- 可审计要求

不要为了“显得 Deep”制造工作量。

---

## 4. Phase 0：把问题变成可研究的问题

### 4.1 Question

把用户问题改成可以由证据回答的问题。

例如：

> “Agent Memory 应该怎么做？”

可以拆成：

> “对于长期运行、多人协作、企业权限约束的 Agent，Memory 应保存什么、不应该保存什么；业务状态、知识和经验如何分层；哪些状态应由业务系统作为权威来源？”

### 4.2 Purpose

先明确研究最终支持什么：

- 事实核查
- 架构设计
- 技术选型
- 产品判断
- 文档修订
- 下一轮研究

没有明确决策时，不要假装存在“最佳方案”。

### 4.3 Constraints

优先识别会改变答案的约束：

- 技术栈
- 时间范围
- 地域 / 法域
- 权限
- 成本
- 现有系统
- 可接受复杂度
- 是否要求官方来源

### 4.4 Success Criteria

研究开始前就定义“什么时候算完成”。

例如：

- 核心子问题都有直接证据；
- 中心结论有独立来源，或明确标成综合判断；
- 主要冲突得到解释；
- 关键未知项已经列出；
- 做过反证搜索；
- 能说明什么新证据会改变结论。

用户问题已经足够明确时，不要机械追问。

---

## 5. Phase 1：拆研究角度

研究计划不是关键词列表，而是不同的信息入口。

默认从下面选 3–5 个：

| 角度 | 主要解决什么 |
|---|---|
| Definition | 概念到底是什么意思？有没有不同定义？ |
| Primary / Original | 原始论文、官方文档、原始实现怎么说？ |
| Implementation | API、代码、数据模型、运行时怎么做？ |
| Industry Practice | 多家厂商 / 团队是否出现共同模式？ |
| Failure / Criticism | 什么情况下失败？为什么有人不用？ |
| Governance | 权限、审计、数据边界、版本、责任如何处理？ |
| Evaluation | 怎么证明它有效？有哪些实验 / benchmark？ |
| Evolution | 它相对上一代方法改变了什么？ |

不要这样拆：

- 搜索 Agent
- 再搜索 Agent framework
- 再搜索 Agent architecture

应该拆成：

- Agent 如何进行长程任务分解？
- 长程任务的 Context / State 如何持久化？
- 多 Agent 并行在哪些条件下真的有收益？

---

## 6. Phase 2：宽搜，再收敛

### 6.1 宽搜

目标是建立候选来源池，不是立即得出结论。

一个研究角度可以准备 2–3 种明显不同的 query：

- 术语
- 机制
- 实现
- 失败 / 限制
- 官方域名

不要只是机械替换同义词。

### 6.2 来源优先级

默认优先：

1. 原始论文 / 正式技术报告
2. 官方产品文档 / 官方技术文章
3. 官方源代码 / GitHub
4. 标准 / 规范
5. 高质量独立技术分析
6. 社区文章 / 讨论

搜索结果只是候选线索，不是证据。

### 6.3 Search → Read → Expand

不要一次把所有 query 搜完。

采用：

```
Search
  ↓
发现高价值来源
  ↓
深读
  ↓
抽取新术语 / 项目 / API / 数据集 / 论文
  ↓
围绕新实体继续搜索
```

很多重要信息来自深读后发现的新实体，而不是第一轮搜索结果。

---

## 7. Phase 3：Source Ledger

研究过程中就记录来源。

最小字段：

| 字段 | 含义 |
|---|---|
| Source ID | S01、S02… |
| URL | canonical URL |
| Title | 页面 / 论文标题 |
| Type | Paper / Official / Code / Standard / Secondary |
| Date | 发布时间 / 更新时间 |
| Accessed | 实际访问日期 |
| Scope | 覆盖什么问题 |
| Authority | 为什么值得相信 |
| Limitations | 它不能证明什么 |
| Source Family | 是否和其他来源共享同一原始出处 |

### 来源数量 ≠ 独立证据数量

以下 5 篇文章如果都复制同一个官方博客，只算一个原始证据源。

检查：

- 是否都引用同一篇原始文章？
- 是否都引用同一份 benchmark？
- 是否都来自同一家公司团队？
- 是否只是新闻稿互相转载？
- 是否只是同一研究的二次解读？

不要让来源复述形成虚假的“三角验证”。

---

## 8. Phase 4：Claim Ledger

重要结论拆成尽量小的 Claim。

推荐：

| Claim | Evidence | Source | Conditions | Status | Confidence |
|---|---|---|---|---|---|
| X 支持 Y | 原文直接描述 | S01 | 版本 / 场景 | Confirmed | High |
| X 因此适合 Z | 综合推断 | S01+S03 | 需要额外条件 | Inferred | Medium |
| X 是行业标准 | 没有直接证据 | — | — | Unsupported | Low |

### Claim Status

- **Confirmed**：来源直接支持，且没有明显冲突。
- **Corroborated**：多个独立来源支持。
- **Inferred**：由多个已确认事实推导，来源没有直接这样说。
- **Disputed**：高质量来源存在实质冲突。
- **Weak**：只有间接或低质量证据。
- **Unknown**：当前研究无法确认。
- **Refuted**：已有可靠证据明确反驳。

### Confidence 的含义

Confidence 表示证据质量和完整程度，不是真理概率。

“High” 不等于“99% 正确”。

---

## 9. Phase 5：深读关键来源

进入最终结论的来源必须真正打开 / 读取。

### 论文

检查：

- Abstract
- Method
- Experiment
- Baseline
- Dataset
- Limitation
- 后续工作 / 引用关系（需要时）

### 官方产品文档

检查：

- 对象定义
- API / 数据模型
- 权限模型
- 版本
- 发布时间
- GA / Preview 状态
- 具体限制

### GitHub

检查：

- README
- 核心实现
- tests / examples
- release
- issues / PR（文档不足时）

### 技术文章

检查：

- 作者和身份
- 是否第一手实现经验
- 是否有可验证数据
- 是否给出适用条件
- 是否只是对别人内容的重述

**没有真正读取的来源，不要把它当成已经核验过的引用。**

---

## 10. Phase 6：反证搜索

Deep Research 不能只做 confirmation search。

对每个 load-bearing Claim 都问：

> “什么证据会让我改变这个判断？”

然后主动搜索：

- X limitations
- X failure
- X problems
- X benchmark
- X criticism
- migrating away from X
- X postmortem
- X vs Y limitations

### 反证优先级

1. 直接反驳该 Claim 的来源
2. 相同条件下的相反实验
3. 不同版本 / 规模的结果
4. 其他实现的失败经验
5. 真实生产约束

如果没找到反例，只能写：

> “在本次检索范围内没有找到可靠反例。”

不能写“没有反例”。

---

## 11. Phase 7：冲突处理

发现冲突时先找冲突来源，而不是直接选一边。

常见原因：

1. 定义不同
2. 版本不同
3. 规模不同
4. 数据集不同
5. 工作负载不同
6. 指标不同
7. 来源利益不同
8. 一个来源已经过时
9. 一个来源本身就是错的

真正有价值的答案往往是：

> 在什么条件下 A 正确，在什么条件下 B 正确？

记录：

```text
Claim:
Source A:
Source B:
Why they conflict:
Most likely explanation:
What would resolve it:
Current conclusion:
```

不要为了让报告更流畅而删除冲突。

---

## 12. Phase 8：Gap Fill

第一轮研究完成后，专门找缺口：

- 哪个子问题没有直接来源？
- 哪个核心 Claim 只有一个来源？
- 哪个结论严重依赖推断？
- 哪个冲突没有解释？
- 哪个最新版本信息缺失？
- 哪个反方证据缺失？
- 哪个数字没有找到原始出处？

第二轮只针对这些缺口。

不要重新把整个主题搜一遍。

**每轮搜索都应该减少一个明确的未知数。**

---

## 13. Phase 9：停止条件

Deep Research 最大的问题之一不是“搜得不够”，而是“永远继续搜”。

满足大多数条件时可以停止：

### Coverage

- 主要子问题已经回答；
- 用户真正关心的决策点已经覆盖。

### Evidence

- 核心 Claim 有足够直接证据；
- 关键事实可追溯到原始来源。

### Diversity

- 主要观点不只来自一个 source family；
- 已检查反方 / 失败证据。

### Conflict

- 高价值冲突已经解释；
- 未解决冲突已经显式标记。

### Marginal Value

继续搜索只产生：

- 重复来源
- 二次转载
- 已知观点的换皮
- 对结论没有影响的新细节

这时停止比继续堆来源更好。

---

## 14. 并行 Agent 的使用边界

默认 **Single Agent First**。

只有在以下条件同时大体成立时才并行：

- 至少 3 个相对独立的研究线程；
- 不同线程使用明显不同的来源类型；
- 线程之间不会共享同一组搜索结果；
- 并行能明显降低时间，而不只是增加重复工作。

### 子 Agent 必须得到

- 明确子问题
- 时间 / 范围
- 来源要求
- 反证要求
- 输出字段
- 不负责什么

例如：

```text
研究：Anthropic Skills 的 procedural knowledge 模型

回答：
1. Skill 是什么；
2. 如何发现；
3. progressive disclosure 怎么工作；
4. 和 MCP 的边界；
5. 官方资料中的限制。

来源：
- 官方文档
- 官方实现说明
- 至少一个独立实现

输出：
Claim → Evidence → Source → Limitation

不要写最终报告。
```

### Lead Agent

Lead 负责：

- 去重
- source family 合并
- claim reconciliation
- 冲突处理
- Gap Fill
- 最终综合

不要让多个子 Agent 各写一篇“最终报告”，最后机械拼接。

---

## 15. Context 和研究状态

Deep Research 很容易因为上下文膨胀而失去判断能力。

不要：

- 把所有搜索结果全文塞进 Context；
- 每轮重复加载相同页面；
- 长期同时保留所有 raw pages、notes 和最终草稿。

采用：

```
Raw Sources
   ↓
Source Notes
   ↓
Claim Ledger
   ↓
Findings
   ↓
Final Report
```

只把当前阶段需要的信息放进活动上下文。

### 长任务 / 中断恢复

至少保留：

- Research Question
- Scope / Cutoff
- Source Registry
- Claim Ledger
- Unresolved Conflicts
- Open Questions
- Current Conclusion
- Next Search Actions

这样下一轮是继续研究，而不是从头搜索。

---

## 16. 时间和版本边界

涉及“当前 / 最新 / 最近”时必须记录 cutoff date。

区分：

- 信息发生时间
- 信息发布时间
- 当前访问时间

对于容易变化的内容：

- API
- SDK
- 产品能力
- pricing
- benchmark
- leaderboard
- release status

优先使用最新官方资料，并注明版本 / 发布时间。

不能因为旧资料仍能搜到，就把旧能力写成当前能力。

---

## 17. 企业与高风险研究

涉及金融、安全、合规、授权、数据治理、生产架构时，提高证据标准。

至少检查：

- 官方定义
- 实际实现
- 权限边界
- 数据边界
- 审计 / 日志
- 版本 / 生命周期
- 失败模式
- 责任归属

不要把：

- “LLM 能做到”
- “Framework 提供 API”
- “厂商有这个 feature”

直接写成：

- “企业生产环境已经安全地解决了这个问题”。

必须分开：

**Capability ≠ Evidence ≠ Production Maturity**

---

## 18. 输出前 Research Audit

### Scope

- 回答的是原问题吗？
- 时间、地域、范围正确吗？

### Sources

- 每个关键事实都有来源吗？
- 引用真的读取过吗？
- 是否优先使用 primary source？
- 多个来源是否其实属于同一 source family？

### Claims

- 来源事实和自己的推断分开了吗？
- 是否把相关性写成因果？
- 是否把单个案例写成行业普遍做法？
- 是否把“没有找到”写成“没有”？

### Conflicts

- 是否只留下支持结论的证据？
- 主要反方证据处理了吗？
- 冲突是否解释了条件差异？

### Freshness

- 当前能力是否用当前版本资料核验？
- 是否混入过期信息？

### Uncertainty

- 不确定的地方是否明确？
- 是否说明缺口和需要什么证据？

### Writing

- 按问题 / 发现组织，不按来源逐篇复述；
- 事实、分析、推断、建议彼此分开；
- 不为了显得全面而加入与问题无关的资料。

---

## 19. 推荐的输出结构

根据任务大小裁剪，不要机械套模板。

```markdown
# 研究主题

## 结论先行
先回答真正的问题。

## 研究范围与方法
研究时间、范围、关键假设和资料类型。

## 发现
按问题 / 主题组织，而不是按来源组织。

## 核心证据
对关键 Claim 给出来源和必要条件。

## 分歧与反证
哪些地方不一致，为什么。

## 局限与未知
这次研究没有证明什么。

## 对当前项目的影响
只写真正可以落到架构、代码或研究路线的影响。

## 下一步
哪些问题值得继续验证。

## Sources
按重要性和用途组织。
```

不要求每个任务都有：

- Executive Summary
- Recommendation
- 巨型 Claim Ledger
- 10+ 来源
- 多 Agent

这些都是手段，不是目标。

---

## 20. 可复用研究产物

当用户要求研究结果沉淀成仓库资料，优先保留四类信息。

### Research Brief

```text
Question
Scope
Cutoff
Success criteria
```

### Source Registry

```text
S01 | URL | Type | Date | Source family | Scope
```

### Claim Ledger

```text
C01 | Claim | Evidence | Source(s) | Status | Confidence | Gap
```

### Findings

- 已确认的模式
- 关键差异
- 冲突
- 限制
- 当前项目含义

Markdown / JSONL 已经够用时，不要为了研究再引入数据库或复杂编排平台。

---

## 21. 常见失败模式

### Confirmation Bias

第一轮搜索形成答案，后续全部围绕它找支持。

**修复：** 核心 Claim 必须有反证搜索。

### Source Accumulation

搜了几十篇文章，却没有增加新的证据。

**修复：** 每个来源都要回答“它解决了哪个未知问题？”

### Source Laundering

很多文章互相引用，看起来是多来源，实际都来自同一出处。

**修复：** 记录 source family。

### Search Snippet Citation

引用搜索摘要，不是实际页面。

**修复：** 最终引用必须基于真正读取的来源。

### Vendor-as-Truth

厂商官方资料被当成行业客观事实。

**修复：** 官方资料用于证明“产品怎么做”；独立来源用于判断成熟度、效果和限制。

### Old-as-Current

把旧版本行为写成当前能力。

**修复：** 对易变主题强制做版本 / 日期核验。

### Premature Synthesis

资料还不够就开始写最终答案。

**修复：** 先整理 Claims / Findings，再写 prose。

### False Precision

为了显得专业，制造无依据的数字、概率或排名。

**修复：** 不确定就保留不确定，不制造精度。

### Endless Research

没有停止条件，一直搜。

**修复：** 用 Coverage + Evidence + Conflict + Marginal Value 判断是否继续。

### Multi-Agent Duplication

多个 Agent 搜同一问题，把重复结果当成更多证据。

**修复：** 线程必须正交；Lead Agent 负责去重。

---

## 22. 核心研究循环

实际运行可以记住这一条：

```
Question
  ↓
Scope / Success Criteria
  ↓
Research Angles
  ↓
Broad Search
  ↓
Source Triage
  ↓
Deep Read
  ↓
Claim Ledger
  ↓
Counter-evidence
  ↓
Conflict Resolution
  ↓
Gap Fill
  ↓
Stop Check
  ├─ not enough → search again
  └─ enough      → synthesize
                     ↓
                   Audit
                     ↓
                  Report
```

这不是严格线性流水线。

- Verification 发现问题 → 回到 Search
- Search 发现新实体 → 扩展 Research Angles
- 冲突无法解释 → 增加证据
- 新证据推翻旧判断 → 更新 Claim Ledger，不要强行保持原结论

---

## 23. 判断边界

Deep Research 可以判断：

- 哪些来源更直接；
- 哪些证据相互独立；
- 哪些 Claim 得到支持；
- 哪里存在冲突；
- 哪些结论只是综合推断；
- 当前研究是否还有明显缺口。

Deep Research 不应假装自动保证：

- 来源一定真实；
- 来源一定没有利益冲突；
- 两个来源一定真正独立；
- 引用在语义上百分之百支持结论；
- 一个行业案例适用于所有企业；
- 一个 benchmark 代表真实生产环境。

研究框架的作用，是让这些判断显式、可检查、可复查，而不是把判断伪装成确定事实。

---

## 24. 参考的业界与 Agent Skill 实践

本 Skill 参考了 2025–2026 年公开的 Deep Research / Research Agent 实现和 Agent Skill。吸收的是方法，不复制某一个框架。

- **OpenAI Deep Research**：多步骤规划、搜索、评估来源、继续研究、可验证引用。
  - https://openai.com/index/introducing-deep-research/
  - https://help.openai.com/en/articles/10500283-deep-research-faq
- **Google Gemini Deep Research**：先生成研究计划；研究过程中反复提出查询、读取结果、发现知识缺口、再次搜索。
  - https://support.google.com/gemini/answer/15719111
  - https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/
- **Anthropic Research**：拆分子问题、跨多来源深挖、最后生成带直接引用的综合报告；Web Search 还提供来源控制能力。
  - https://www.anthropic.com/news/integrations
  - https://www.anthropic.com/news/web-search-api
- **LangChain Open Deep Research**：研究 brief、独立研究线程、工具调用循环、研究结果压缩、独立最终报告阶段和 benchmark。
  - https://github.com/langchain-ai/open_deep_research
  - https://www.langchain.com/blog/open-deep-research
- **公开 Agent Skills**：source registry、claim ledger、反证搜索、冲突处理、可恢复研究状态、citation audit。
  - https://github.com/arjunprabhulal/agent-skills/blob/main/skills/research/deep-research/SKILL.md
  - https://github.com/omnitric/agent-skills/blob/main/deep-research/SKILL.md
  - https://github.com/Firecrawl/web-agent/blob/main/agent-core/src/skills/definitions/deep-research/SKILL.md

这些实践共同指向一个比较稳定的结论：

> **Deep Research 的核心不是“搜索很多”，而是围绕 Claim 管理不确定性，并通过多轮检索、反证、冲突处理和停止条件，把证据逐步收敛成可复查的结论。**
