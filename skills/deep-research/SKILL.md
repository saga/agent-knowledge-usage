---
name: deep-research
description: 对需要多来源检索、证据核验、冲突处理和综合判断的开放问题进行研究。当用户要求研究、调研、事实核查、跨厂商/框架/论文比较、架构判断、趋势分析，或问题明显不能由一两个来源可靠回答时使用；只要任务需要形成多来源证据链，即使用户没有明确说“deep research”，也应使用。
metadata:
  kind: capability
---

# Deep Research

## 1. Use this skill when

研究不能靠一两个可靠来源完成，且结论需要交叉验证、反证或综合推断。

常见触发：

- research / 调研 / deep research；
- 跨厂商、框架、论文、开源实现比较；
- “业界通常怎么做”“为什么这样做”；
- 互相矛盾的技术说法；
- 需要长期沉淀、可复查的研究结论。

不要用于单页读取、单事实查询、纯总结、纯头脑风暴。

## 2. Operating contract

先定义：

- **Question**：要由证据回答什么？
- **Purpose**：支持什么决策？
- **Constraints**：时间、版本、环境、权限、成本等；
- **Success criteria**：什么条件满足后停止？

输出必须区分：

- Fact；
- Inference；
- Unknown；
- Recommendation。

完成标准：load-bearing claims 有证据，关键冲突有处理记录，未知项没有被写成事实。

## 3. Execute the loop

按以下顺序执行：

1. **Frame** — 把问题拆成 3–5 个不同信息入口。
2. **Broad search** — 建来源池，不急着下结论。
3. **Read → expand** — 深读高价值来源，追踪新实体和新术语。
4. **Ledger** — 记录 Source、Claim、条件、状态。
5. **Counterevidence** — 主动找反例、限制和替代实现。
6. **Resolve conflicts** — 先检查版本、部署、workload、权限、时间。
7. **Gap fill** — 只补会改变结论的缺口。
8. **Synthesize** — 按问题组织 findings，不按搜索顺序写流水账。

详细字段、查询策略、证据等级和冲突处理规则见：
[full-research-protocol.md](./references/full-research-protocol.md)。

## 4. Source discipline

优先：

1. 原始论文 / 技术报告；
2. 官方文档 / 官方技术文章；
3. 官方 source code / API；
4. 标准 / 规范；
5. 高质量独立材料；
6. 社区材料用于发现线索。

多个页面来自同一公告、benchmark、论文或公司时，只按一个 source family 计算独立性。

## 5. Claim discipline

重要结论拆成小 Claim。

状态使用：

- Confirmed
- Corroborated
- Inferred
- Disputed
- Weak
- Unknown
- Refuted

不要把 citation 数量当证据强度。

特别审查：

- 行业普遍；
- 最佳实践；
- 一定 / 必须；
- 当前 / latest / production-ready；
- 数字和 benchmark；
- 安全、权限、合规。

## 6. Research diversity

涉及“业界 / 大厂 / 行业趋势”时，转入
[industry-practice-research](../industry-practice-research/SKILL.md)，不要让 Deep Research 默认只研究熟悉厂商。

涉及论文体系时转入
[academic-literature-review](../academic-literature-review/SKILL.md)。

## 7. Multi-agent

只有存在至少 3 条明显独立研究线程时才并行。

每个线程应有不同 research angle 或 source family。

Lead 负责：

- dedup；
- conflict resolution；
- gap fill；
- final synthesis。

不要为了并行而并行。

## 8. Stop

停止时至少满足：

- 核心问题已覆盖；
- load-bearing claims 有证据；
- 做过 counterevidence；
- 关键冲突已解释或保留；
- 新搜索主要重复已知信息；
- remaining gaps 已列出。

## 9. Output

默认结构：

1. Executive conclusion
2. Findings
3. Evidence / Claim table
4. Differences / Boundaries
5. Gaps
6. Implications
7. Sources
8. Research cutoff

长期研究优先保存为 repo artifact，而不是只留在聊天中。

## 10. Quality gate

提交前：

- [ ] Question 可研究；
- [ ] Claim → Evidence 可追溯；
- [ ] source family 已检查；
- [ ] Fact / Inference 已分开；
- [ ] counterevidence 已执行；
- [ ] 冲突已处理；
- [ ] Unknown 明确；
- [ ] 版本 / cutoff 明确；
- [ ] 结论没有超出证据边界。

