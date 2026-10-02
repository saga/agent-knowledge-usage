---
name: deep-research
description: 对 AI Agent、Knowledge、Memory、Skills、Ontology、RAG、Context、Tools、Multi-Agent、Evaluation、Governance 等主题进行多角度深度研究。当一个搜索不足以回答问题、需要跨论文、厂商和开源实现交叉验证时使用。
metadata:
  kind: capability
---

# Deep Research

## 什么时候使用

适用于：
- 搜索研究一下
- 业界都怎么做
- 找相关论文或项目
- 比较多个厂商
- 这个架构还有哪些模式
- 找出这个领域的重要方向

不适合：
- 单个已知页面读取
- 简单事实查询
- 已经有充分资料、只需改写的任务

## 标准流程

问题定义
→ 搜索角度拆分
→ 宽搜
→ 候选来源池
→ 去重与筛选
→ 深读
→ 交叉验证
→ 事实 / 解释 / 模式
→ 结论

## 第一步：定义问题

把用户问题改写成一个可验证的问题。

例如“AI Agent 的 Knowledge 除了 RAG 还有什么”，拆成：
1. 知识如何表示？
2. 知识保存在哪里？
3. 如何检索？
4. 如何进入 Agent context？
5. 如何表达业务语义？
6. 如何表达 procedural knowledge？
7. 如何保存 provenance、authority、freshness？
8. 如何评估知识是否被正确使用？

## 第二步：搜索矩阵

默认至少覆盖：

| 角度 | 目标 |
|---|---|
| Primary research | 原始论文、技术报告 |
| Industry | 厂商官方资料 |
| Implementation | 开源项目、GitHub |

企业场景再增加：

| 角度 | 目标 |
|---|---|
| Governance | permission、policy、audit、safety |
| Evaluation | benchmark、failure mode、reliability |

## 第三步：宽搜

每个角度先建立候选来源池，不要一开始深读几十个页面。

Query 应描述：
主题 + 机制 + 场景 + 目标

## 第四步：筛选

至少考虑：
- 直接相关性
- 是否原始来源
- 是否最新
- 是否有实现细节
- 是否有实验或证据
- 是否和已有来源重复

## 第五步：深读

重点看：
- 定义
- 架构
- 数据模型
- 方法
- 实验
- 限制
- 失败案例
- 版本和发布时间

## 第六步：反向验证

重要结论至少尝试：
- claim
- claim + limitation
- claim + counterexample
- claim + failure
- claim + comparison

不要只做 confirmation search。

## 输出

研究结果最好包含：
1. 核心发现
2. 证据来源
3. 共同模式
4. 分歧
5. 边界与限制
6. 对当前项目的影响
7. 仍然未知的问题

每个强结论都必须能回答：

“这个判断来自哪个来源，还是我的推断？”

如果是推断，明确写成综合判断，而不是事实。
