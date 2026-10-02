# Research Skills

本目录保存这个研究库自己的研究型 Agent Skills。

| Skill | 用途 |
|---|---|
| [deep-research](./deep-research/SKILL.md) | 多角度深度研究、跨来源交叉验证 |
| [academic-literature-review](./academic-literature-review/SKILL.md) | 论文搜索、分类、扩展、下载 |
| [industry-practice-research](./industry-practice-research/SKILL.md) | Snowflake / Databricks / Google / OpenAI / Anthropic 等业界实践研究 |
| [evidence-and-claim-review](./evidence-and-claim-review/SKILL.md) | 审核事实、证据、推断和结论强度 |
| [knowledge-synthesis](./knowledge-synthesis/SKILL.md) | 从大量研究材料提炼共同抽象、架构模型和 Roadmap |

典型组合：

Research question
→ deep-research
→ academic-literature-review / industry-practice-research
→ evidence-and-claim-review
→ knowledge-synthesis
→ 更新研究文档


## 确定性检查脚本

Research Skill 中可以放 scripts/，但脚本只承担当机器规则明确、结果应该可重复的部分。

当前提供：

| Script | 用途 |
|---|---|
| [validate_vendor_report.py](./industry-practice-research/scripts/validate_vendor_report.py) | 检查业界实践文章的章节、来源和常见结构问题 |
| [audit_claims.py](./evidence-and-claim-review/scripts/audit_claims.py) | 检查 Claim / citation / 数字 / freshness / 常见架构边界风险 |

典型流程：

Research
→ Deep Read
→ Deterministic Script Check
→ Semantic Evidence Review
→ Knowledge Synthesis

脚本不是研究结论的替代品。特别是 citation entailment、source independence、行业共识和架构判断仍需要读取原始来源。

OpenAI 的 Skills 规范支持 Skill 中提供 scripts/；实际是否能执行取决于当前 Agent runtime 是否提供 shell / sandbox。因此 Skill 必须在“有脚本执行环境”和“只有文件读取能力”两种情况下都能工作。
