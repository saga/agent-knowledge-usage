# AGENTS.md

本文件给在本仓库做研究、整理文档和维护资料的 Agent 使用。

这个仓库不是业务应用，而是持续研究 AI Agent Knowledge、Memory、Skills、Ontology、Graph、Context、Tools、State、Evidence、Evaluation 和 Governance 的研究库。

## 1. 大原则

### KISS，不 over-design

- 先回答当前研究问题，再考虑抽象。
- 不为了“完整”建立大量目录、术语、框架或中间层。
- 已经有资料能回答的问题，不重复建立另一套平行体系。
- 新概念只有在能解决现有研究问题时才加入。
- 删除重复、过时、低价值资料优先于继续堆资料。

### 研究先查证，再下结论

涉及当前产品能力、API、SDK、Framework 行为、最新论文、厂商当前架构、行业判断时，必须查外部来源，不依赖模型记忆假设当前事实。

### 事实、证据、推断分开

研究文档中明确区分：

Fact → Source / Evidence → Interpretation → Pattern → Recommendation

不要把厂商文档中的能力写成“业界标准”，不要把单个案例写成普遍经验，不要把没有发现反例写成“没有反例”。

### 不把引用当成证明

引用说明来源，不自动证明结论。

- 官方文档证明产品支持什么，不证明生产成熟度。
- 一个成功案例证明可行，不证明普遍适用。
- 一篇论文证明作者的实验结果，不证明所有场景。
- 搜索结果发现候选来源，不等于已经验证。

### 不做伪下载

只有实际下载到文件，才可以写“已下载”。

如果当前环境无法把 PDF 二进制落盘：
- 保存 metadata。
- 保存公开 PDF URL。
- 保存可重复下载脚本。
- 明确说明 PDF 尚未落盘。

不要把公开链接冒充成本地文件。

## 2. 文档规范

### 说人话

中文研究文档直接、清楚、少套话。

不要为了显得专业堆术语，也不要把一句简单的话拆成很多层标题。技术术语需要时保留，但首次出现应说明它解决什么问题。

### 当前事实和研究结论保持一致

如果研究改变了 Roadmap、分类体系、行业判断或核心模型，应同步检查相关索引和文档。

### 记录研究日期

涉及当前产品、当前论文状态、当前公司实践时，写明研究日期。

## 3. 证据优先级

默认优先：

1. 原始论文、正式论文、arXiv
2. 官方产品文档、官方技术报告、官方博客
3. 官方源代码、GitHub repository
4. 标准、规范
5. 高质量技术资料
6. 普通博客、论坛、社交媒体

低级别来源可用于发现线索，但不能单独支撑重要架构结论。

高风险结论尽量同时寻找支持证据、限制条件和反方证据。

## 4. Web 与 GitHub 研究纪律

- 当前信息优先使用 Web、GitHub 和官方资料验证。
- 不要反复读取同一个页面。
- 能保存后离线分析时，优先保存再分析。
- 大规模研究采用“先宽搜，再收敛”。
- 搜索结果必须去重。
- 不要因为关键词命中就把结果算进最终集合。
- GitHub 是实现证据，不自动等于业务真相。
- 研究 GitHub 时记录 repository、branch、commit（需要时）、查看过的文件、重要发现和未解决问题。

## 5. 论文研究规范

每篇论文尽量记录：

- Title
- Authors
- Year / first public date
- arXiv / DOI / canonical identifier
- Abstract URL
- PDF URL
- Category
- Relevance
- Status：preprint / published / unknown

必须区分：

preprint ≠ peer reviewed

对论文结论优先看 abstract、method、experiment、limitation，而不是只看标题。

## 6. 业界实践研究规范

研究厂商时统一拆成：

Business meaning
→ Representation / Storage
→ Retrieval / Access
→ Runtime use
→ Governance / Permission
→ Provenance / Freshness
→ Limitations

特别不要把 Knowledge 简化成 Vector Store。

## 7. Skill 规范

研究型 Skill 使用 SKILL.md，并在 frontmatter 声明：

metadata:
  kind: capability

Skill 必须说明：

- 什么时候使用
- 研究顺序
- 输出需要记录什么
- 证据要求
- 不负责什么

不要建立一个万能研究 Prompt。

## 8. 研究产物

- reference/：经典文章、论文和外部资料的研究摘要
- 业界实践/：厂商和行业实践分析
- 学术论文/：论文索引、分类、下载脚本和论文资料
- AGENT-KNOWLEDGE-ROADMAP.md：跨研究主题的长期路线图

新增资料后检查 README、目录 README、索引以及 Roadmap 是否需要同步。

## 9. 推荐研究流程

1. 明确研究问题
2. 拆成多个搜索角度
3. 宽搜候选来源
4. 去重与筛选
5. 深读高价值来源
6. 交叉验证与反证
7. 形成事实与证据表
8. 提炼模式和边界
9. 更新文档和索引
10. 最后检查是否把推断写成事实

## 10. 不做的事情

除非用户明确要求：

- 不把研究库变成知识管理平台。
- 不自行引入数据库、搜索服务或复杂 RAG pipeline。
- 不为了自动化而引入复杂编排框架。
- 不在研究阶段实现生产系统。
- 不因为发现一个新概念就重写已有架构。
- 不删除已有有价值的研究材料。

目标是：建立一个可信、可复用、容易继续研究的 Agent Knowledge 研究库。
