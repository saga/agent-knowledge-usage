# Dark Knowledge 与 Tacit Knowledge：为什么“知识”不等于“答案”

> 研究日期：2026-10-02

这份研究笔记用于补充 AI Agent Knowledge Fidelity 研究。两个概念需要严格区分：Dark Knowledge 是机器学习知识蒸馏里的技术概念；Tacit Knowledge 是认识论和知识管理里的概念。二者共同指出：可观察的最终答案通常只是更丰富知识状态的一部分。

## 1. Dark Knowledge 是什么

Hinton、Vinyals 和 Dean 在 2015 年的 *Distilling the Knowledge in a Neural Network* 中提出，训练好的模型除了给正确类别高概率，也会给其他类别分配不同的概率。错误类别之间的相对概率包含模型学到的泛化结构和相似性，例如一个输入更像某个错误类别而不是另一个错误类别。作者用 soft targets 和 temperature distillation 把这种结构传给 student。

原文：https://arxiv.org/abs/1503.02531

所以：

~~~
Hard label
= 当前标准答案

Soft distribution
= 标准答案 + alternative structure + relative confidence
~~~

这说明一个非常重要的事实：

> 答案正确，不等于所有有用知识都被保留下来了。

## 2. Dark Knowledge 对 Agent Knowledge 有什么启发

把它类比到 Agent，不应该直接说“RAG summary 就是 dark knowledge distillation”，而应该关注相同的结构性问题：

~~~
Rich knowledge state
      ↓
hard answer / short summary
~~~

这个投影可能保留：

- 当前结论；
- 最相关的事实；

但同时丢掉：

- alternative interpretation；
- uncertainty；
- boundary information；
- similarity / relation structure；
- near-miss cases；
- exception structure。

因此一个企业知识摘要即使在测试问题上 100% 答对，也不能推出它 100% 保留了原始知识。

这是 Knowledge Fidelity 研究中非常值得单独测的一层：

~~~
Representation Fidelity
        +
Alternative / Uncertainty Fidelity
~~~

## 3. Tacit Knowledge 是什么

Michael Polanyi 在 1966 年的 *The Tacit Dimension* 中把一个核心现象概括为“we can know more than we can tell”。Tacit knowledge 常用于描述难以充分提取、表达和编码的经验、技能、判断、intuition 和 know-how。

Wikipedia 当前条目也强调，tacit knowledge 与 explicit knowledge 在实践中不是两个完全离散的类别，同一内容对不同的人可能处于不同程度的 tacitness；其中还区分 relational、somatic 和 collective 等形式。

Wikipedia：https://en.wikipedia.org/wiki/Tacit_knowledge

Polanyi 相关原始资料摘要：https://tacit-knowledge-architecture.com/object/the-tacit-dimension-excerpt/

## 4. Tacit Knowledge 为什么直接影响“100% 知识”问题

如果原始知识是：

~~~
facts + rules + documents
~~~

那么可以比较容易定义一个知识集合，讨论 recall / coverage。

但如果原始知识是：

~~~
expert judgment
+
pattern recognition
+
context-sensitive skill
+
intuition
~~~

那么“原始知识 100%”本身就不一定能被定义成一个可直接序列化的文本集合。

所以：

~~~
Knowledge Fidelity
≠ Text Fidelity
≠ Proposition Fidelity
~~~

这不是说 tacit knowledge 无法验证，而是评价方式要从“内容有没有被复制”扩展到“行为是否保留”。

例如：

- 边界条件变化时，判断是否随之变化；
- 异常案例出现时，是否触发进一步调查；
- 两个相似方案之间，是否保留专家原来的区分能力；
- Agent 是否能在没有规则逐条写出的情况下完成类似判断。

## 5. LLM 是否具有 Tacit Knowledge

这个问题目前不是定论，但已经有直接学术讨论。

Céline Budding 2025 年发表于 *Philosophy of Science* 的论文认为，LLM 可以获得一种符合 Martin Davies 定义的 tacit knowledge，并把它作为解释 LLM 行为的一种理论框架。这是一个哲学与认知解释上的论证，不等于证明 LLM 拥有完整的人类式 Polanyian tacit knowledge。

论文：https://doi.org/10.1017/psa.2025.19
开放版本：https://arxiv.org/abs/2504.12187

Janna Lu 2025 年发表的 *Tacit knowledge in large language models* 又进一步区分了不同形式，认为 LLM 可以表现出“理论上可编码但代价很高”的 tacit knowledge，以及语言 nuance / subtext；作者不把当前 LLM 的 embodied knowledge 与文本学习得到的知识混为一谈。

论文：https://link.springer.com/article/10.1007/s11138-025-00710-5

这一区分非常适合 Agent Architecture：

~~~
Text-derived implicit knowledge
≠
Experience-derived embodied knowledge
~~~

## 6. Agent 可以主动发现 Tacit Knowledge

2025 年 Zuin 等人的工作研究了组织环境中的 tacit knowledge discovery。他们不是单纯要求专家写一份文档，而是让 Agent 与组织成员交互，从分散在人际网络中的碎片知识逐步重建整体知识。在 864 次合成模拟中，作者报告 94.9% full-knowledge recall。

论文：https://arxiv.org/abs/2507.03811

这个结果不能外推成真实企业的 94.9% 水平，因为研究使用的是合成组织和模拟条件，但方法论上很有价值：

> Tacit Knowledge 不一定只能通过“写文档”被 externalize，也可以通过 interview、案例对比、行为观察和多轮 questioning 被逐步重建。

这与本仓库的 Knowledge Compilation 很接近：

~~~
Observe
→
Interview
→
Compare Cases
→
Extract Pattern
→
Test Exceptions
→
Validate
→
Publish
~~~

## 7. Dark Knowledge + Tacit Knowledge 对 Knowledge Fidelity 的共同启发

两个概念回答不同问题：

| 概念 | 关注什么 | 对 Knowledge Fidelity 的启发 |
|---|---|---|
| Explicit | 能直接表达和编码的内容 | 可以测 text / proposition fidelity |
| Dark | 正确答案之外的软结构和相对概率 | 不能只测 top answer |
| Tacit | 难以完整表达但可通过行为表现的 know-how | 不能只测文本复制 |
| Parametric | 被模型参数吸收的知识结构 | 不能把参数视为简单数据库 |
| Runtime Context | 当前推理实际获得的知识投影 | 不能把“已经放进 context”当成“已经被使用” |

于是更完整的 Knowledge Fidelity 链是：

~~~
Original Knowledge
    ↓
Explicit / Implicit / Tacit
    ↓
Representation
    ↓
Knowledge Access
    ↓
Context Projection
    ↓
Behavior / Reasoning
    ↓
Answer / Action
~~~

对应的评价也应该从单一 Answer Accuracy 扩展为：

~~~
Content Fidelity
+
Structural Fidelity
+
Uncertainty / Alternative Fidelity
+
Behavioral Fidelity
+
Counterfactual Fidelity
+
Evidence Faithfulness
~~~

## 8. 一个需要避免的误区

不要把三个词混成一个词：

~~~
Dark Knowledge = Tacit Knowledge = Latent Knowledge
~~~

它们不是同义词。

- Dark Knowledge：特指知识蒸馏语境中的 soft output structure。
- Tacit Knowledge：强调难以完全显性化的 knowing。
- Latent / Parametric Knowledge：更宽泛地描述隐藏在模型参数或内部表示中的信息和结构。

当前最合理的做法，是把它们当成三个相互关联但不同的研究维度。

## 9. 当前研究问题

1. 能否定义一个 benchmark，比较 hard answer、soft distribution、summary、graph、semantic view 各自保留了多少知识结构？
2. 能否用 counterfactual tests 测量 Agent 是否真的保留 tacit-like decision behavior？
3. 能否区分“模型会做这个判断”与“模型能解释为什么这么判断”？
4. 企业 Agent 的 Knowledge Fidelity 是否应该同时记录内容保真、关系保真、不确定性、行为保真和证据保真？
5. Knowledge Compilation 能否把 tacit observations 转换为可审计的显式规则，同时不把原始上下文丢掉？

## 10. 核心资料

- Hinton, Vinyals, Dean. *Distilling the Knowledge in a Neural Network* — https://arxiv.org/abs/1503.02531
- Budding. *What Do Large Language Models Know? Tacit Knowledge as a Potential Causal-Explanatory Structure* — https://doi.org/10.1017/psa.2025.19
- Lu. *Tacit knowledge in large language models* — https://link.springer.com/article/10.1007/s11138-025-00710-5
- Zuin et al. *Leveraging Large Language Models for Tacit Knowledge Discovery in Organizational Contexts* — https://arxiv.org/abs/2507.03811
- Wikipedia. *Tacit knowledge* — https://en.wikipedia.org/wiki/Tacit_knowledge