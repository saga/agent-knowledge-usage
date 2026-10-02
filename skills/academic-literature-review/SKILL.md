---
name: academic-literature-review
description: 进行论文综述、论文筛选、证据地图和研究演化分析。当用户要求找论文、比较论文、梳理研究路线、寻找研究空白、追踪最新研究，或需要系统整理论文证据时使用；不要只输出搜索结果列表。
metadata:
  kind: capability
---

# Academic Literature Review

## Skill Operating Contract

### Start with
- Research question
- Scope / population / task
- Time cutoff
- Review mode
- Completion criteria

### Execute
1. Build the corpus from seed papers.
2. Expand backward / forward / related / recent.
3. Deduplicate and screen.
4. Extract experimental evidence.
5. Synthesize by theme and mechanism.
6. Cross-check industry / implementation when relevant.
7. Record gaps and the next research question.

### Finish when
- Major research routes are represented;
- load-bearing papers were actually read;
- alternatives / challenges were checked;
- evidence conditions are preserved;
- concrete research gaps remain visible.

Keep steps imperative and keep long paper lists / detailed schemas in repository artifacts rather than in the main workflow.

## 目标

建立可复用的论文集合，而不是简单返回一串搜索结果。

核心问题：

这个研究问题已经研究到了哪里？
哪些论文是基础？
哪些论文解决了什么子问题？
哪些方向正在快速发展？
还有什么空白？

## 默认分类

围绕 Agent Knowledge Stack 搜索：
- RAG / Retrieval
- Knowledge Graph / Ontology
- Business Semantics
- Memory
- Skills / Procedural Knowledge
- Tool Use / Planning
- Context Engineering
- Multi-Agent / Protocol
- Evaluation
- Safety / Governance

分类可以按任务调整，不要为了凑分类强行拆论文。

## 搜索流程

### 1. Seed papers

先找：
- foundational paper
- survey
- benchmark
- influential architecture

### 2. Citation expansion

对种子论文扩展：
- references
- citing papers
- similar / related work

### 3. Recent work

再补最近工作：
- 最近 1～2 年
- 新 benchmark
- 新 architecture
- enterprise / production-oriented work
- 与当前项目直接相关的新方向

### 4. 去重

优先按 canonical identifier 去重：
- arXiv ID
- DOI
- title + author

## 每篇论文记录

| 字段 | 内容 |
|---|---|
| Title | 论文标题 |
| Authors | 作者 |
| Year | 首次公开年份 |
| ID | arXiv / DOI |
| Abstract | 摘要入口 |
| PDF | 公开 PDF |
| Category | 所属方向 |
| Relevance | 与研究问题的关系 |
| Status | preprint / published / unknown |

## 下载纪律

用户要求下载时：
1. 首选公开 arXiv / 官方 PDF。
2. 保存 metadata 和 canonical URL。
3. 实际下载成功后才标记 downloaded。
4. 下载失败必须保留失败状态。
5. 不绕过付费墙或访问限制。
6. 不默认把大量外部 PDF 二进制提交进 Git。

## 证据边界

必须区分：

作者提出 ≠ 实验显示 ≠ 广泛复现 ≠ 业界采用

不要把论文作者的 recommendation 写成行业共识。

## 推荐输出

Research question
→ Paper map
→ Foundational papers
→ Recent papers
→ Methods / patterns
→ Limitations
→ Research gaps

---
## 8. 先选择 Literature Review 模式

不是所有“找论文”都应该走同一种流程。

| 模式 | 适用场景 | 核心输出 |
|---|---|---|
| Rapid Map | 快速了解领域结构 | 论文地图、代表作、方向 |
| Narrative Review | 形成研究综述 | 主题、共识、争议、空白 |
| Evidence Map | 研究问题较明确，但不要求穷尽 | 检索范围、纳入集合、证据矩阵 |
| Systematic Review | 明确要求 SLR / PRISMA / exhaustive | protocol、检索式、screening、flow、证据综合 |
| Update | 已有论文库继续更新 | 新论文、变化、被扩展或挑战的结论 |

当前仓库默认使用 Rapid Map / Narrative Review / Evidence Map。只有用户明确要求 systematic review、SLR、PRISMA 或 exhaustive，才切换到系统综述纪律。公开 literature-review 实践也通常把普通 thematic review 与 protocol-driven systematic review 分开。

## 9. Phase 0：定义问题和时间边界

开始搜索前至少记录：

~~~text
Research Question:
Scope:
Domain:
Time Window:
Language:
Publication Types:
Review Mode:
Success Criteria:
~~~

特别明确“最近两年”按什么算：首次公开、正式发表还是当前版本。AI / Agent 论文经常存在 arXiv v1、revised version、conference version 和项目更新，不能自动当成四篇独立工作。

## 10. Phase 1：Seed → Snowball → Challenge Set

论文研究不要只靠关键词搜索。

~~~text
Seed Papers
   ↓
Backward Citation
   ↓
Forward Citation
   ↓
Related Work
   ↓
Recent Search
   ↓
Challenge / Contradicting Work
~~~

Seed 优先找 foundational paper、survey、benchmark、canonical architecture 和高相关 recent work。

Backward 找基础方法和依赖；Forward 找改进、replication、criticism、alternative；Challenge Set 专门找 limitation、failure、benchmark comparison 和 contrary result。

目的不是把种子论文的 framing 当成整个领域的 framing。

## 11. Phase 2：Paper Registry

不要把搜索结果直接塞进 Markdown。重要论文先进入稳定 registry。

| 字段 | 含义 |
|---|---|
| Paper ID | 稳定 ID |
| Title | 标题 |
| Authors | 作者 |
| Year | 首次公开年份 |
| arXiv ID | arXiv 标识 |
| DOI | DOI |
| Abstract URL | 摘要页 |
| PDF URL | PDF |
| Published Version | 正式发表版本 |
| Category | 分类 |
| Method | 核心方法 |
| Evidence | 实验 / benchmark |
| Limitation | 作者明确限制 |
| Relevance | 对当前研究问题的作用 |
| Status | preprint / published / unknown |
| Source Relation | seed / backward / forward / related / challenge |

当前仓库的 学术论文/papers.json 已经承担这个 registry 角色，后续研究应尽量保持字段稳定。

## 12. Phase 3：去重

至少按以下顺序去重：

1. DOI；
2. arXiv ID；
3. canonical paper URL；
4. normalized title + first author；
5. title similarity + year。

重点处理 arXiv 与 conference version、v1/v2、不同 PDF host、short paper / full paper。

不要因为标题相似就错误合并不同作者、不同方法或明确不同的后续工作。

## 13. Phase 4：从摘要升级成证据单元

每篇重要论文至少提取：

~~~text
Problem:
Core idea:
Method:
Experimental setting:
Main result:
What the experiment actually shows:
What it does NOT show:
Limitations:
Relation to prior work:
Relation to adjacent work:
Why it matters for current research:
~~~

尤其保留 What it does NOT show。Benchmark 上的提升不自动等于所有任务提升、所有模型提升、生产 latency 更好或更适合企业环境。

## 14. Phase 5：按研究对话组织

最终综述应该形成：

~~~text
Theme
├── Consensus
├── Disagreement
├── Evidence quality
├── Methodological difference
└── Gap
~~~

不要变成“2023 年 A 提出 X，2024 年 B 提出 Y，2025 年 C 提出 Z”。真正要回答的是：Y 解决了 X 的哪个限制，Z 又在哪些条件下改变了判断。

## 15. 论文质量检查

重要论文至少看：

- Relevance
- Method
- Evaluation / baseline / dataset / metric
- Fairness of comparison
- Reproducibility：code、data、prompts、configuration、evaluation procedure
- External validity
- Limitations
- preprint / peer-reviewed / published / updated status

论文“有名”不是证据质量本身。一个强 benchmark 如果只覆盖一个数据集，仍然要保留它的实验边界。

## 16. Phase 6：建立论文演化链

一个研究方向最好整理成：

~~~text
Foundation
   ↓
Limitation
   ↓
Improvement
   ↓
Alternative
   ↓
Benchmark
   ↓
Current frontier
~~~

这样论文库才能回答“这个领域为什么发展到今天”，而不只是保存一堆标题。

## 17. Research Gap 必须具体

不要写“未来还需要更多研究”。

改成：

~~~text
Gap:
当前工作主要研究 X。

Missing:
很少研究 Y。

Why it matters:
Y 是企业 Agent 的关键约束。

Evidence:
现有 A / B / C 的实验边界都避开 Y。

Next study:
需要比较 Z 条件下的方法 A / B。
~~~

对当前仓库尤其关注：enterprise business semantics、entitlement-aware retrieval、provenance / authority、knowledge-use evaluation、memory vs business truth、skill evaluation、context assembly、long-running state。

## 18. 论文与业界实践互相校验

不要让 academic literature 和 vendor research 成为两个孤岛：

~~~text
Academic primitive
      ↕
Industry implementation
      ↕
Open-source implementation
      ↕
Current architecture
~~~

论文证明“可行”不等于厂商已经产品化，厂商产品化也不等于企业已经广泛采用。

## 19. 停止条件

可以停止新增论文，当：

- 核心主题已有 seed；
- backward / forward expansion 开始明显重复；
- recent work 已覆盖时间窗口；
- challenge search 没有改变主要结论；
- 新论文主要是同一 benchmark / 同一方法的小变体；
- 再增加论文不会改变 taxonomy、pattern 或 gap。

不要把“收集 100 篇论文”当作完成条件。

## 20. 输出必须回答六个问题

1. 基础工作是什么？
2. 当前主流方法有哪些？
3. 它们解决了上一代什么限制？
4. 哪些结论已经比较稳定？
5. 哪些地方仍有争议？
6. 下一步最值得研究的 gap 是什么？

最后再回答：对当前 Agent Knowledge 架构意味着什么？

## 21. 长期研究库的质量门槛

进入长期研究库的完成级论文至少有：

~~~text
Metadata
+ Method
+ Evidence
+ Limitation
+ Relation to other work
+ Current relevance
~~~

只有标题、摘要和一句 relevance 的记录，只算索引项，不算完成的研究笔记。

## 22. 确定性脚本：Paper Registry Validator

论文 registry 中最适合机器处理的是：必填字段、arXiv / DOI 重复、normalized title 重复、URL 格式、year、status、category / directory 一致性和 order 重复。

有 shell / sandbox 时运行：

~~~bash
python3 skills/academic-literature-review/scripts/validate_paper_registry.py 学术论文/papers.json
python3 skills/academic-literature-review/scripts/validate_paper_registry.py 学术论文/papers.json --json
~~~

脚本只负责 registry integrity，不负责判断论文好不好、实验是否正确、relevance 是否合理或结论是否可信。

脚本不可执行时，回到同一套字段 checklist，不把“未运行”当成“通过”。