# Research Skills

本目录保存这个研究库自己的研究型 Agent Skills。Skill 的写法遵循 ADR-0001：主 SKILL.md 负责触发与执行流程，详细资料按需放入 references/。

| Skill | 用途 |
|---|---|
| [deep-research](./deep-research/SKILL.md) | 多角度深度研究、跨来源交叉验证 |
| [academic-literature-review](./academic-literature-review/SKILL.md) | 论文搜索、筛选、证据提取、研究演化与 gap |
| [industry-practice-research](./industry-practice-research/SKILL.md) | 跨厂商业界实践、产品 / 架构 / 采用证据 |
| [evidence-and-claim-review](./evidence-and-claim-review/SKILL.md) | 审核事实、证据、推断和结论强度 |
| [knowledge-synthesis](./knowledge-synthesis/SKILL.md) | 从多源研究提炼共同抽象、责任边界和 Roadmap |

典型组合：

~~~
Research question
→ deep-research
→ academic-literature-review / industry-practice-research
→ evidence-and-claim-review
→ knowledge-synthesis
→ 更新研究文档 / 架构决策
~~~

## Skill 写法

研究型 Skill 默认：

- description 负责明确触发上下文；
- 主流程使用 imperative steps；
- 每个阶段都有 completion criteria；
- Fact / Inference / Unknown 分开；
- 长资料按 progressive disclosure 放入 references/；
- 只用脚本处理 deterministic checks；
- 不为了行数机械拆分，也不把环境里已经能直接读取的事实重复写进 Skill。

详细设计决策见 [ADR-0001](../docs/adr/0001-skill-authoring-and-progressive-disclosure.md)。

## 确定性检查脚本

Skill 中可以放 scripts/，但脚本只承担当机器规则明确、结果应该可重复的部分。

当前提供：

| Script | 用途 |
|---|---|
| [validate_vendor_report.py](./industry-practice-research/scripts/validate_vendor_report.py) | 检查业界实践文章的章节、来源和常见结构问题 |
| [audit_claims.py](./evidence-and-claim-review/scripts/audit_claims.py) | 检查 Claim / citation / 数字 / freshness / 常见架构边界风险 |
| [validate_paper_registry.py](./academic-literature-review/scripts/validate_paper_registry.py) | 检查论文 registry 的结构、URL、重复项和字段 |

典型流程：

~~~
Research
→ Deep Read
→ Deterministic Script Check
→ Semantic Evidence Review
→ Knowledge Synthesis
~~~

脚本不是研究结论的替代品。citation entailment、source independence、行业共识、primitive equivalence 和架构判断仍需要读取原始来源并进行语义审查。

脚本不可执行时，Skill 仍必须能够依靠人工 checklist 完成，并明确记录 deterministic check unavailable。
