# AI Agent Knowledge Fidelity：研究资料与证据索引

> 研究日期：2026-10-02
> 
> 用途：支持《AI Agent 知识表达和使用：知识到底损失在哪里？》

这份资料不是论文原文下载，而是本仓库的研究索引。重点记录“它能证明什么”和“它不能证明什么”。

## 1. LLM 参数知识不是一个可直接计算的数据库副本

### Knowledge Boundary of Large Language Models: A Survey
- URL：https://arxiv.org/abs/2412.12472
- 价值：系统讨论 LLM 的 knowledge boundary、知识类型、识别方法和限制。
- 支持的判断：
  - 参数中存在大量知识，但“模型知道什么”不是简单、固定集合；
  - 需要区分知识存在、知识识别和知识利用。
- 不能证明：
  - “训练数据有 100%，参数只保存 X%”这种统一比例。

### Give Me the Facts! A Survey on Factual Knowledge Probing in Pre-trained Language Models
- URL：https://arxiv.org/abs/2310.16570
- 价值：总结 factual probing、knowledge retention、prompt sensitivity 等研究。
- 支持的判断：
  - factual knowledge 可以被系统性 probing；
  - prompt 和 probing 方法会影响知识是否被观察到。
- 不能证明：
  - 一个跨模型、跨领域、跨任务的通用“知识存储率”。

### Scalable Extraction of Training Data from (Production) Language Models
- URL：https://arxiv.org/abs/2311.17035
- 价值：证明模型中确实存在可被重新提取的训练数据记忆。
- 支持的判断：
  - “训练后什么原文都不存在”是错误的；
  - 参数化学习同时包含泛化和一定程度的可提取记忆。
- 不能证明：
  - 模型总体知识保留比例。

## 2. RAG 不等于知识蒸馏

### Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation
- URL：https://arxiv.org/abs/2307.11019
- 价值：研究外部知识与 parametric knowledge 的关系，以及 retrieval 对知识边界判断的影响。
- 支持的判断：
  - internal / external knowledge 会发生冲突；
  - retrieval 能帮助模型接触外部知识，但模型并不天然正确处理冲突。

### ARES
- URL：https://aclanthology.org/2024.naacl-long.20/
- 价值：把 RAG evaluation 拆成 context relevance、answer faithfulness、answer relevance。
- 支持的判断：
  - RAG 不能只用最终答案评价；
  - “检索到了”与“答案忠实”是不同指标。

## 3. 长 Context 证明“看见”不等于“会用”

### Lost in the Middle
- URL：https://aclanthology.org/2024.tacl-1.9/
- 价值：经典长上下文实验。
- 核心证据：
  - 相关信息放在长 context 的中间时，模型性能经常显著下降。

### RULER
- URL：https://arxiv.org/abs/2404.06654
- 价值：指出 Needle-in-a-Haystack 太简单，真正复杂的长上下文任务性能会明显下降。
- 核心证据：
  - 更复杂的 retrieval / multi-hop / aggregation 任务不能由简单 NIAH 替代。

### Context Length Alone Hurts LLM Performance Despite Perfect Retrieval
- URL：https://aclanthology.org/2025.findings-emnlp.1264/
- 价值：最直接地拆掉“只要检索正确，问题就解决了”的假设。
- 核心证据：
  - 即使相关信息被完美检索出来，context 变长本身仍可能导致显著性能下降。

### Context Rot
- URL：https://www.trychroma.com/research/context-rot
- 代码：https://github.com/chroma-core/context-rot
- 价值：跨多个模型研究输入长度对实际任务性能的影响。
- 核心证据：
  - 输入越来越长时，模型使用 context 的可靠性会下降；
  - NIAH 的“找到 needle”不能代表真实长上下文能力。

### Diagnosing and Mitigating Context Rot in Long-horizon Search
- URL：https://arxiv.org/abs/2606.29718
- GitHub：https://github.com/GAIR-NLP/ContextRot
- 价值：2026 年进一步研究 long-horizon search 中的 context rot 和 premature termination。
- 核心证据：
  - 长 context 可能导致 agent 提前结束、停止探索；
  - context management 不只是 token 优化，也是 test-time scaling / search strategy。

## 4. 压缩证明“任务没坏”不等于“知识没丢”

### LLMLingua
- URL：https://arxiv.org/abs/2310.05736
- 价值：展示高压缩比下仍可能保持任务性能。
- 核心证据：
  - 部分任务中最高约 20× 压缩仍能保持较小性能损失。
- 关键限制：
  - benchmark task accuracy 不是完整 information preservation。

### LLMLingua-2
- URL：https://arxiv.org/abs/2403.12968
- 价值：进一步研究 task-agnostic prompt compression 和 faithfulness。
- 核心证据：
  - 压缩本质上是一个信息选择问题；
  - 压缩目标和“信息量”并不是完全相同的优化目标。

## 5. Knowledge Conflict / Faithfulness

### Context-DPO
- URL：https://aclanthology.org/2025.findings-acl.536/
- 价值：专门提升 context-faithfulness。
- 核心证据：
  - 即使提供了 external context，模型仍可能不忠实使用；
  - knowledge conflict 是独立问题。

### FaithfulRAG
- URL：https://aclanthology.org/2025.acl-long.1062/
- 价值：显式建模 parametric knowledge 与 retrieved context 的事实级冲突。
- 核心证据：
  - 强制“只相信 context”并不自动解决问题；
  - 更合理的是显式考虑冲突和事实关系。

### Thinking to Recall
- URL：https://arxiv.org/abs/2603.09906
- 价值：说明推理过程本身可以改变 parametric knowledge 的可召回性。
- 核心证据：
  - “模型内部有没有”和“当前一次调用能不能把它召回”进一步被实验证明是两个问题。

## 6. RAG vs Long Context

### LaRA
- URL：https://proceedings.mlr.press/v267/li25dv.html
- 价值：系统比较 RAG 与 Long Context。
- 核心证据：
  - 没有一个方案在所有任务和 context 条件下都占优；
  - routing 依赖模型、任务、context 长度和 retrieval 特征。

## 7. 本仓库当前结论

当前最合理的研究对象不是单一：

~~~
Knowledge Loss Rate
~~~

而是一条：

~~~
Canonical Source
→ Representation
→ Derived View
→ Retrieval
→ Context
→ Knowledge Use
→ Evidence
→ Answer / Action
~~~

对应至少需要分别研究：

- Source Coverage
- Representation Fidelity
- Retrieval Recall
- Context Fidelity
- Context Use
- Conflict Resolution
- Evidence Faithfulness
- Task Success

这些是本仓库当前提出的研究框架，不是已有统一工业标准指标。

## 8. 当前未解决问题

1. 是否能建立跨模型、跨任务的 parametric knowledge retention benchmark？
2. 能否区分“模型内部存在但 prompt 下无法召回”的 knowledge 与 truly absent knowledge？
3. 能否对 Source → Context 做可逆性/保真度测量，而不是只测最终 answer？
4. 能否用 counterfactual intervention 测量模型是否真正使用了某条 external knowledge？
5. 是否可以建立一套统一的 Knowledge Fidelity Curve，对 text / chunk / summary / graph / semantic representation 做可比实验？
6. 在企业 Agent 中，authority、freshness、permission 是否应该进入 fidelity measurement？
