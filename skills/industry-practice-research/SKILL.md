---
name: industry-practice-research
description: 研究云厂商、企业软件厂商、Data/AI 平台、Agent runtime、企业应用和大型 AI 基础设施如何做 Knowledge、Memory、Semantic Layer、Retrieval、Governance 与 Agent Context。当用户问“业界怎么做”“大厂怎么做”“厂商对比”或需要产品/架构/采用证据时使用；每次研究都主动扩展厂商，不允许长期固定在少数熟悉厂商。
metadata:
  kind: capability
---

# Industry Practice Research

## 1. Use this skill when

研究对象是：

- 云厂商；
- Data / AI platform；
- Enterprise application；
- Agent / model platform；
- Operational / workflow platform；
- AI infrastructure / open source。

不要把某 3–5 家熟悉厂商当成固定白名单。

## 2. Vendor expansion contract

默认满足：

- 至少 5 家相关厂商；
- 至少 3 家不是上一轮固定集合；
- 至少 2 个厂商类别；
- 至少 1 条明显不同的架构路线；
- 至少 1 次 counterexample search。

研究问题非常窄时可以缩小，但必须记录原因。

按架构问题发现厂商，而不是只搜：

~~~text
<vendor> knowledge
~~~

优先搜：

~~~text
enterprise agent knowledge graph
agent semantic layer
business semantics for agents
agentic retrieval
enterprise grounding permissions
agent memory service
AI search enterprise permissions
agent knowledge lifecycle
operational ontology for agents
~~~

详细 vendor candidate、来源独立性和厂商卡片见：
[vendor-research-protocol.md](./references/vendor-research-protocol.md)。

## 3. Operating contract

每家公司先填 Vendor Card，再写结论。

至少比较：

- Problem；
- Abstraction；
- Representation；
- Discovery；
- Retrieval；
- Runtime；
- Authorization / Entitlement；
- Provenance；
- Freshness；
- Lifecycle；
- Adoption；
- Limitations。

## 4. Evidence layers

严格区分：

| Layer | 证明什么 |
|---|---|
| Product | 产品提供什么 |
| Architecture | 运行时怎样工作 |
| Adoption | 用户怎样使用、是否有生产证据 |

不要把：

~~~text
Product capability
  ↓
Architecture fact
  ↓
Industry adoption
~~~

当成自动成立的推导。

## 5. Cross-vendor synthesis

结论按五级：

1. Vendor Fact
2. Cross-source Observation
3. Cross-vendor Pattern
4. Engineering Practice
5. Candidate Primitive

Level 5 是仓库自己的 synthesis，不是厂商原话。

重点抽责任，不抽产品名：

~~~text
Canonical Source
      ↓
Semantic / Knowledge Object
      ↓
Retrieval / Query View
      ↓
Permission / Authority
      ↓
Context Assembly
      ↓
Agent
      ↓
Action / Business System
~~~

## 6. Independence and counterevidence

检查：

- same announcement；
- same benchmark；
- same company；
- same ecosystem；
- same upstream provider。

并主动找：

- incompatible architecture；
- documented limitation；
- independent implementation；
- different permission model；
- failed or constrained customer case。

“没找到反例”不能写成“没有反例”。

## 7. Unknown is a valid result

允许：

- Confirmed
- Partial
- Unknown
- Not documented
- Preview
- Independent evidence missing
- Conflicting

“官方没写”不等于“不支持”。

## 8. Completion criteria

研究结束前必须能回答：

- 是否只研究了熟悉厂商？
- 是否新增至少 3 家？
- 是否覆盖至少 2 类厂商？
- 是否搜索过不兼容路线？
- 新证据有没有改变 candidate primitive？

输出默认包括：

1. Scope / cutoff
2. Vendor set and selection rationale
3. Vendor Cards
4. Capability Matrix
5. Architecture Matrix
6. Lifecycle Matrix
7. Common patterns
8. Real differences
9. Evidence gaps
10. Candidate primitives
11. Open questions

不要做“最佳厂商”排名。

## 9. Deterministic check

有 shell 时运行：

~~~bash
python3 skills/industry-practice-research/scripts/validate_vendor_report.py 业界实践/<report>.md
~~~

脚本只承担结构、URL、matrix、明显强结论等 deterministic checks。

脚本不能判断：

- primitive equivalence；
- industry maturity；
- customer case representativeness。

不能执行时记录 unavailable，不得声称“脚本检查通过”。

