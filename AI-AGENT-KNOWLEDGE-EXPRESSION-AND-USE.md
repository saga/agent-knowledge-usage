# AI Agent 知识表达和使用：知识到底损失在哪里？

> 研究日期：2026-10-02
> 
> 主题：Knowledge Representation / Knowledge Fidelity / Knowledge Use / Dark Knowledge / Tacit Knowledge
> 
> 核心问题：如果原始知识是 100%，训练进模型以后还剩多少？RAG、摘要、Graph、Semantic Layer 把知识交给模型时，又损失了多少？

这篇文章不试图回答“RAG 还是 Graph 哪个更好”。更基础的问题是：

> 知识从原始来源一路走到 Agent 最终做决定，中间到底发生了什么变化？这些变化哪些是信息损失，哪些只是表示方式变化，哪些虽然没有删掉信息却让模型用不好？

目前没有一个公认的“知识损失率”可以回答这个问题。研究已经有很多相关指标，但它们分别测的是不同阶段：模型参数里的可回忆知识、训练数据的可提取记忆、RAG 的检索和事实忠实度、长上下文的利用能力、压缩后的任务性能等。把这些指标简单相加成一个百分比，会制造一种并不存在的精确性。

真正值得研究的不是一个数字，而是一条 Knowledge Fidelity Chain。

---

## 1. 先回答最核心的问题：100% 的知识进入模型以后，到底剩多少？

### 1.1 这里其实混了三个不同的问题

假设原始资料为：

~~~
D = 原始知识 / 文档 / 数据 / 规则
~~~

经过训练得到：

~~~
W = 模型参数
~~~

然后给模型一个问题：

~~~
Q + prompt → Answer
~~~

我们通常说“模型学会了 D”，但“学会”至少有三种含义。

### 第一种：存进去了多少？

也就是：

> D 中多少信息被某种形式编码到了 W 里？

这是最接近“100% 剩多少”的问题。

但它很难直接计算。

模型不是把数据库复制进参数，而是通过下一 token 预测等训练目标，把大量文本转成参数中的统计结构。参数是对训练分布的一种表示，不是训练语料的逐条备份。

因此：

~~~
训练语料 100%
≠
参数里存了一个 100% 可读数据库
~~~

同时，模型又确实存在很强的记忆。已有研究能够从生产模型中提取训练数据，说明“参数完全只是抽象规则、不保留原文”也不成立。

比较准确的说法是：

> 模型对训练数据进行的是高度压缩、分布式、任务导向的编码；其中既有泛化出来的规律，也有一部分可以被重新提取的具体记忆。

这两个部分无法用一个简单百分比表示。

### 1.2 第二种：能问出来多少？

这是另一个指标：

~~~
Stored Knowledge
        ↓
Prompt / Query
        ↓
Recallable Knowledge
~~~

模型可能“内部有某种知识”，但在某个 prompt 下答不出来。

已有知识边界研究说明，LLM 的知识边界不是一个简单、固定的集合，而会受到提示方式、问题形式以及模型是否能正确调用内部知识的影响。2026 年的研究进一步发现，让模型进行某种推理过程，有时会把原本答不出来的参数知识“解锁”出来。

因此：

~~~
Parametric Knowledge
≠
Queryable Knowledge
~~~

### 1.3 第三种：真的用对了吗？

还有第三层：

~~~
Queryable Knowledge
        ↓
Reasoning
        ↓
Correct Decision / Answer
~~~

模型可以知道一个事实，却没有用它。

甚至可能：

- 检索到了正确资料，但没有使用；
- context 里同时存在旧知识和新知识，模型信了旧的；
- 资料都在 context 里，但因为太长没有正确利用；
- 找到了事实 A 和 B，却在多跳推理时组合错了；
- 最终知道答案，却没有给出证据。

因此：

> 知识存在、知识可访问、知识被使用，是三个不同层次。

这也是为什么“知识库命中率”不能直接代表 Agent 知识能力。

---

## 2. 所以“知识损失率”不是一个数字，而是一条链

把整个过程画出来会更清楚：

~~~
                         ┌──────────────────┐
                         │ Canonical Source │
                         │ 100% source      │
                         └────────┬─────────┘
                                  │
                         extract / parse
                                  ↓
                         ┌──────────────────┐
                         │ Knowledge Model  │
                         │ facts / rules /  │
                         │ relations        │
                         └────────┬─────────┘
                                  │
                   index / embed / chunk / graph
                                  ↓
                         ┌──────────────────┐
                         │ Derived Views    │
                         │ vector/fulltext/ │
                         │ graph/semantic   │
                         └────────┬─────────┘
                                  │
                         retrieval / query
                                  ↓
                         ┌──────────────────┐
                         │ Selected Context │
                         └────────┬─────────┘
                                  │
                       attention / reasoning
                                  ↓
                         ┌──────────────────┐
                         │ Model Use        │
                         └────────┬─────────┘
                                  │
                            generation
                                  ↓
                         ┌──────────────────┐
                         │ Answer / Action  │
                         └──────────────────┘
~~~

这里至少有六种完全不同的“损失”：

1. **表示损失**：原始知识被转换成另一种表示。
2. **选择损失**：需要的内容没有进入下一层。
3. **压缩损失**：为了节省 token 删除了部分信息。
4. **利用损失**：信息已经存在，但模型没有成功使用。
5. **冲突损失**：模型内部知识与外部知识冲突，选择错了。
6. **表达损失**：模型最终生成的答案没有完整、正确地表达它获得的信息。

因此不能把：

~~~
RAG = 10% 损失
Graph = 5% 损失
LLM = 40% 损失
~~~

当成有意义的工程指标。

这些数字缺少统一定义。

---

## 3. 一个重要修正：RAG 本身不等于“知识蒸馏”

这个理解很容易出现，但需要拆开。

### 3.1 原文直接进入 context，并没有发生传统意义上的知识蒸馏

如果原文是：

~~~
The annual fee is waived for customers meeting condition X.
~~~

RAG 找到这段文字，并把它原样放到 context：

~~~
Question
+
"The annual fee is waived for customers meeting condition X."
~~~

此时发生的是：

~~~
Source
→
Retrieve
→
Copy into Context
~~~

这更像“传输”，而不是“蒸馏”。

只要没有截断、改写或摘要，文本层面完全可以做到近似无损。

所以：

> RAG 的知识损失不一定发生在 source → context。

真正的问题往往出现在：

~~~
context → model use
~~~

### 3.2 什么时候才真的发生了“知识蒸馏”？

例如：

~~~
100 页政策文档
      ↓
20 个 chunk
      ↓
5 个检索片段
      ↓
1 个 summary
      ↓
1 个 prompt
~~~

这里确实发生了多次压缩和选择。

典型操作包括：

- chunking；
- embedding；
- reranking；
- top-k；
- summarization；
- context compression；
- memory extraction；
- graph extraction；
- entity/relation extraction；
- structured knowledge extraction。

这时才应该认真问：

> 原文中的哪些信息没有进入下一级表示？

这才接近真正的“知识损失”。

### 3.3 Dark Knowledge 提醒我们：正确答案之外还有知识

“知识蒸馏”这个词还有一个容易被忽略的来源：Hinton、Vinyals 和 Dean 在 2015 年提出的 *Distilling the Knowledge in a Neural Network*。

他们指出，一个训练好的模型输出的不只是“正确类别”，还会给其他类别分配概率。即使这些概率非常小，它们之间的相对关系也包含模型学到的泛化结构和相似性。例如，模型把一个输入误认为 A 的概率远高于误认为 B，本身就是知识。Hinton 将这类信息称为 **dark knowledge**，并用高温 soft targets 把这部分信息传给 student。见 Hinton et al. 2015。

这对前面的“知识损失”问题很重要，因为它说明：

~~~
正确答案
≠
模型掌握的全部可用信息
~~~

更具体地，一个 richer representation 被压成 hard answer，即使“答案完全正确”，也可能丢掉：

- alternative hypotheses；
- uncertainty；
- similarity structure；
- decision boundary information；
- exception / near-miss information。

所以，一个 summary 如果把一份复杂政策压成：

~~~
客户满足条件 X，因此批准。
~~~

它可能保留了当前问题的答案，却把“为什么不是 Y”“哪些条件最容易改变结论”“哪些规则与当前规则相近但不同”等信息一起删掉。

这与 Dark Knowledge 的关系不是说 RAG summary 就等同于 knowledge distillation，而是：

> **知识表达存在“从 richer state 到 hard answer”的有损投影，而且损失的可能不是事实本身，而是事实之间的关系、相似性和不确定性。**

因此 Knowledge Fidelity 不能只问：

> 最终答案对不对？

还应该问：

> **表示转换之后，原来支撑这个答案的结构还有多少？**

需要严格区分：Hinton 所说的 Dark Knowledge 是知识蒸馏中的技术概念，主要指 soft output distribution 中超出 hard label 的信息；它不能直接等同于下面讨论的 Tacit Knowledge，也不能简单用来证明 LLM 参数中存在某种特定类型的“隐性事实库”。
---

## 4. Vector Embedding 也不等于“知识被存成向量”

Embedding 很容易制造一个误解。

例如：

~~~
Document
  ↓
Embedding
  ↓
Vector
~~~

这个 vector 并不是原文知识的一个可逆副本。

它的目标通常是让“语义相近”的东西在向量空间里接近。

因此：

~~~
Embedding
≠
lossless representation of document
~~~

但这并不意味着 embedding 已经损失了整个系统真正关心的知识。实际 RAG 一般是：

~~~
Document
   ↓
Embedding
   ↓
Retrieve candidate
   ↓
Original text
   ↓
Context
~~~

也就是说：

> Embedding 负责找路，原文负责提供证据。

所以衡量 embedding 时，与其问“它保留了原文多少信息”，更有用的问题是：

> 它能不能把完成当前任务所需的证据找出来？

这也是为什么 Retrieval Recall 与 Information Fidelity 不是同一个概念。

---

## 5. Chunking 也会损失知识，但损失的往往不是 token，而是关系

例如原文：

~~~
Rule A applies to Product B.

However, this rule does not apply when Customer C
satisfies Exception D.

Exception D is defined in Section 7.
~~~

如果简单切成三个 chunk：

~~~
Chunk 1: Rule A → Product B
Chunk 2: Exception C/D
Chunk 3: Definition of D
~~~

每个 chunk 的文字都可能 100% 保留。

但：

~~~
A
↓
B
↓
Exception D
↓
Definition D
~~~

这种跨段关系可能被破坏。

因此：

> 信息可以在 token 层面几乎没丢，在关系层面已经丢了。

这就是为什么“source token coverage”不能等于“knowledge coverage”。

---

## 6. Context 又会产生第二种完全不同的损失

直觉是：

> Context window 已经有 1M tokens 了，那知识基本都能放进去。

实验并不支持这么简单的结论。

### Lost in the Middle

经典研究发现，即使信息已经放进长 context，模型对位于 context 中间的信息使用能力仍会明显下降。相关任务中，模型通常更容易使用开头和结尾的信息。见 Liu et al., TACL 2024。

### RULER

RULER 更进一步指出，传统 Needle-in-a-Haystack 并不能代表真正的长上下文能力。很多模型虽然能找到一个孤立的 needle，但在更复杂的多 needle、聚合、多跳任务里，随着 context 变长性能明显下降。

### Perfect Retrieval 仍然不够

2025 年研究专门控制了“检索失败”这个变量：即使所有相关信息都已经完美提供给模型，输入变长本身仍会导致模型在数学、QA 和 coding 等任务上显著退化，报告的性能下降范围达到 13.9%–85%。

这件事非常关键：

> 知识已经拿到了 ≠ 模型已经成功使用知识。

因此：

~~~
Retrieval Recall = 100%
~~~

完全不能推出：

~~~
Knowledge Use = 100%
~~~

---

## 7. 这也是为什么“超长 Context 取代 RAG”不是一个简单结论

2025 年 LaRA 基准比较了 RAG 与 Long Context，在多个模型和任务上发现，没有一个方案在所有条件下都占优；结果取决于模型、context 长度、任务类型和 retrieval 特征。

原因其实很直观。

### RAG 做的是选择

~~~
Huge corpus
   ↓
small useful context
~~~

优点是减少噪声。

缺点是可能把真正需要的东西选掉。

### Long Context 做的是保留

~~~
Huge corpus
   ↓
large context
~~~

优点是少做选择。

缺点是模型未必能有效利用全部信息。

所以：

> 不检索并不等于零损失。

有时只是从“检索损失”换成了“context utilization loss”。

---

## 8. Context Compression 更直接暴露了这个问题

很多工作开始研究：

~~~
Long Context
   ↓
Compressed Context
~~~

例如 LLMLingua 报告在部分任务上实现了最高约 20× 的 prompt compression，同时保持较小的性能损失；LLMLingua-2 继续把这个问题定义为 task-agnostic prompt compression，并在多个数据集上评估压缩后的任务性能。

这类工作很有价值，但也暴露了一个问题：

> “任务性能没明显下降”不等于“信息完全没丢”。

假设：

~~~
原始知识：
100 条事实

压缩后：
保留 95 条

当前 benchmark 只问到了其中 20 条
~~~

那么：

~~~
Task Accuracy ≈ 100%
Knowledge Fidelity ≠ 100%
~~~

所以评价压缩技术时，不能只看最终 Answer Accuracy。

---

## 9. 真正缺少的是一个 Knowledge Fidelity 研究体系


### 9.1 Tacit Knowledge 提醒我们：并不是所有知识都能先拆成 facts

“知识损失”还有一个更根本的问题：**有些知识本来就很难被完整说出来。**

Michael Polanyi 在 *The Tacit Dimension* 中用一句很著名的话描述这种情况：“we can know more than we can tell”。Wikipedia 对 Tacit Knowledge 的概括也保留了这个核心：它通常指难以提取、难以完整表达和编码的 knowledge，例如经验、intuition、skill、insight 和 know-how；而且 tacit 与 explicit 并不是两个完全割裂的盒子，同一内容对一个人可能是 explicit，对另一个人可能是 tacit。

这会直接改变我们对“100% 原始知识”的定义。

如果原始知识只是：

~~~
Document
→
Facts
→
Rules
~~~

那么我们可以问：

> 保留了多少 propositions？

但如果原始知识包括：

~~~
Expert skill
+
pattern recognition
+
judgment
+
intuition
+
context-sensitive know-how
~~~

那么“100%”本身就不一定是一个可以直接写成文本的集合。

因此：

~~~
Knowledge Fidelity
≠
Text Fidelity
~~~

甚至：

~~~
Knowledge Fidelity
≠
Proposition Fidelity
~~~

这不是说 tacit knowledge 无法研究。关键问题变成：

> **它是否能通过行为、决策、例子、反馈和实践被观察和验证？**

这对 Agent 特别重要。一个金融研究员可能说不出自己为什么在第 17 个信号上觉得“这里不对”，但他可以：

- 选择 A 而不是 B；
- 在某种边界条件下改变判断；
- 给出反例；
- 解释哪些异常模式会触发进一步调查。

这些行为本身就是 tacit knowledge 的外显痕迹。

### 9.2 LLM 是否也可能具有某种 Tacit Knowledge？

这个问题已经出现了直接研究。

Céline Budding 在 2025 年发表于 *Philosophy of Science* 的论文中提出，LLM 可以获得一种符合 Martin Davies 定义的 tacit knowledge，并认为 LLM 的一些架构特征满足相关的语义描述、句法结构和因果系统性条件。这个论证属于哲学与认知解释框架，不等于已经证明“LLM 像人一样拥有 Polanyi 意义上的全部 tacit knowledge”。

2025 年另一篇开放获取研究则区分了不同类型的 tacit knowledge，并主张 LLM 可以表现出两类：理论上可以被编码但代价很高的 knowledge，以及语言中的 nuance / subtext；作者不认为当前 LLM 具有通过身体与感官经验获得的 embodied tacit knowledge。

还有一项 2025 年关于组织 tacit knowledge 的 Agent 研究，把“找专家并让专家写文档”换成了另一种思路：Agent 与组织成员持续交互，从分散在人际网络中的碎片知识重建整体知识。在其合成模拟中，作者报告了 94.9% 的 full-knowledge recall。这个结果不能证明真实企业可以达到同样水平，但它提出了一个很重要的方向：

> **Tacit Knowledge 不一定只能“转换成一份文档”，也可以通过多轮交互、观察行为和拼接分散线索逐步重建。**

这和前面提出的 Knowledge Compilation 很接近。

### 9.3 Dark Knowledge 与 Tacit Knowledge 放在一起，得到一个更完整的模型

这两个概念不能混为一谈，但放在一起很有帮助：

| 层次 | 主要含义 | 典型问题 |
|---|---|---|
| Explicit Knowledge | 可以直接表达的 facts / rules / documents | 有没有写下来？ |
| Dark Knowledge | 显式答案之外，隐藏在模型输出分布中的关系、相似性、不确定性 | “正确答案之外还知道什么？” |
| Tacit Knowledge | 难以完整表达，但可以通过行为、经验和判断表现出来的 know-how | “会不会做、会不会判断？” |
| Parametric Knowledge | 被模型参数吸收后的知识结构 | “模型内部形成了什么？” |
| Runtime Context | 当前一次推理实际看到的知识投影 | “这次给模型看了什么？” |

于是最初的问题可以重新写成：

~~~
Original Knowledge
      ↓
what is explicit?
      ↓
what is implicit / tacit?
      ↓
what gets encoded parametrically?
      ↓
what gets projected into context?
      ↓
what gets used in reasoning?
      ↓
what becomes observable in the answer/action?
~~~

这比单纯的：

~~~
Document → RAG → Answer
~~~

要准确得多。

### 9.4 这也解释了为什么“最终答案”不是一个充分的知识度量

考虑两个模型都输出：

~~~
Approve
~~~

它们可能完全不同。

模型 A 可能还保留：

~~~
Approve
P(exception) = 0.31
P(deny) = 0.04
~~~

模型 B 可能只是输出：

~~~
Approve
~~~

模型 A 还可能知道某个例外是最接近的 alternative，并且一旦条件 Y 变化，结论很可能改变。

如果我们只看最终字符串，两者完全一样，但它们携带的知识结构并不一样。

这正是 Dark Knowledge 对“知识损失率”问题最大的补充：

> **正确输出可能只是一个高维知识状态的低带宽投影。**

而 Tacit Knowledge 又进一步告诉我们：

> **有些能力甚至不一定能直接从输出文本中恢复，可能只能通过行为和反事实测试观察。**

所以未来 Knowledge Fidelity Evaluation 不应该只有：

~~~
Answer Correctness
~~~

还应该考虑：

~~~
Answer
+
Alternative / Uncertainty
+
Evidence
+
Counterfactual Behavior
+
Decision Consistency
~~~

目前已经有很多局部指标：

- factual knowledge probing；
- knowledge boundary；
- retrieval recall；
- context relevance；
- answer faithfulness；
- long-context performance；
- prompt compression ratio；
- task accuracy。

但它们分散在不同研究方向里。

例如 ARES 把 RAG 评价拆成：

- context relevance；
- answer faithfulness；
- answer relevance。

这已经比单看“最终答案对不对”进了一步。

但对于 Agent Knowledge，还需要再往前走。

---

## 10. 我认为更合理的模型不是一个损失率，而是一条 Fidelity Vector

对一个具体任务，可以把原始知识表示成一组任务相关的 atomic propositions / facts：

~~~
F = {f1, f2, ..., fn}
~~~

然后分别测：

### 10.1 Source Coverage

原始 source 中有多少与任务相关的知识被系统识别出来？

~~~
Source Coverage
=
identified relevant facts
/
relevant facts in source
~~~

### 10.2 Retrieval Recall

真正需要的事实，有多少进入候选 context？

~~~
Retrieval Recall
=
required facts retrieved
/
required facts
~~~

### 10.3 Context Fidelity

进入 context 后，是否仍保持原来的语义和关系？

这里不能只比字符串，还应该检查：

- fact；
- condition；
- exception；
- negation；
- temporal validity；
- relation。

### 10.4 Context Use

模型是否实际使用了 context 中的关键事实？

例如：

~~~
Context contains:
A, B, C, D

Answer actually depends on:
A, C
~~~

这不能简单用关键词匹配，而应通过 controlled counterfactual testing：

> 把 A 删除或者改成错误值，答案是否随之发生正确变化？

这比“prompt 里出现过 A”可靠得多。

### 10.5 Answer Faithfulness

最终答案中的 claim，有多少能被提供的 evidence 支撑。

这是现在 RAG faithfulness 研究已经在测的部分。ARES、FaithfulRAG、Context-DPO 等工作都说明，即使 context 已经提供，模型仍可能忽略、混合或者误读其中的信息。

### 10.6 Authority / Conflict Resolution

这是企业 Agent 特别需要补的一项。

假设：

~~~
Model prior:
旧规则 A

Retrieved source:
新规则 B
~~~

如果 source 是 authoritative policy，那么通常应该由 B 覆盖 A。

但现实中的模型未必这么做。

已有研究发现，LLM 对内部知识和外部知识发生冲突时，并不总能正确处理这种冲突；相关工作因此专门研究 context-faithfulness 和 knowledge conflict。

所以：

> 企业 Knowledge Fidelity 不仅是“保留了多少”，还包括“冲突时有没有信对”。

---

## 11. 因此，可以把一次 Agent Knowledge 使用写成

~~~
Source
  │
  │  completeness
  ↓
Knowledge Representation
  │
  │  preservation
  ↓
Derived View
  │
  │  retrieval
  ↓
Context
  │
  │  utilization
  ↓
Reasoning
  │
  │  faithfulness
  ↓
Answer / Action
~~~

每一层都有自己的 fidelity。

所以更合理的模型是：

~~~
Knowledge Fidelity
=
(
Source Coverage,
Representation Fidelity,
Retrieval Recall,
Context Fidelity,
Context Use,
Conflict Resolution,
Answer Faithfulness
)
~~~

这是一个向量，而不是一个数字。

我认为这比“知识损失率 23%”更科学。

---

## 12. 那能不能做到“完全不损失”？

要分层回答。

### 12.1 Source → Storage

可以。

数据库保存原文、原始表、原始结构，本身完全可以做到可逆或近似可逆。

### 12.2 Storage → Retrieval Index

可以接近，但通常不是完全可逆。

例如：

- full-text index；
- vector index；
- graph projection；
- semantic representation。

这些都是 derived views。

但只要 canonical source 仍然保留，derived view 本身有损并不一定是问题。

### 12.3 Retrieval → Context

理论上可以做到近似无损：

~~~
exact source segment
→ exact context
~~~

但这需要：

- 找对；
- 不截断；
- 不被 context budget 淘汰；
- 不被错误摘要替换。

### 12.4 Context → Model Use

这里就很难做到“100%”。

原因不一定是知识本身丢了，而是：

> 模型不保证会等价地利用所有 context。

Lost in the Middle、RULER、Context Rot 和 perfect-retrieval 长上下文实验都说明了这一点。

### 12.5 Model Use → Answer / Action

也很难保证 100%。

因为这里已经进入：

- reasoning；
- uncertainty；
- generation；
- tool selection；
- action planning。

所以：

> 无损知识传递可以在存储和传输层实现；无损知识使用则不是一个已经解决的问题。

这是两件事。

---

## 13. 一个非常重要的新认识：知识的主要问题可能不是“存”，而是“投影”

现在越来越值得关注的是：

~~~
Long-lived Knowledge
        ↓
       ??
        ↓
Current Context
~~~

这里发生了一个 Knowledge Projection：

> 从庞大的、长期存在的知识空间中，决定当前这个用户、任务、时间点，究竟应该让模型看到什么。

这其实比“建一个 Knowledge Base”更接近 Agent 的核心问题。

因此：

~~~
Knowledge Base
~~~

解决的是：

> 东西放在哪里？

而：

~~~
Knowledge Projection
~~~

解决的是：

> 这一次，到底应该给模型什么？

这两个问题完全不同。

---

## 14. 这也解释了为什么 Knowledge Base、LLM Wiki 很难真正回答这个问题

一个典型“知识库”通常会解决：

~~~
Documents
→ Index
→ Search
→ Retrieved Context
~~~

它解决的是 Access。

但用户现在问的是：

~~~
Original Knowledge
        ↓
What survives?
        ↓
What reaches model?
        ↓
What does model actually use?
        ↓
What reaches the final decision?
~~~

这已经进入：

- representation；
- information preservation；
- retrieval；
- context engineering；
- model cognition；
- evidence；
- provenance；
- evaluation。

所以：

> Knowledge Base 是基础设施对象，不是 Knowledge Fidelity 理论。

---

## 15. Graph 能不能解决这个问题？

不能直接解决，但可以解决其中一部分。

Graph 的优势不是“比文本更无损”。

把文本变成：

~~~
Entity
Relation
Entity
~~~

本身也是一种压缩和抽象。

它会丢掉：

- 原文措辞；
- 上下文；
- 修饰信息；
- 例外；
- 条件；
- 时间；
- 不确定性。

但 Graph 可以更好地表达某些关系。

例如：

~~~
Customer
  │
  ├── owns → Account
  │
  ├── hasRisk → High
  │
  └── subjectTo → Rule-123
~~~

如果任务真正需要的是关系遍历，那么 Graph Representation 可能比十个长文本 chunk 更容易被使用。

所以：

> Graph 解决的是某类结构化知识的表达和访问问题，不是 100% 知识无损保存问题。

---

## 16. Semantic Layer 可能比“更多 RAG”更接近真正的解决方向

如果企业真正关心：

~~~
Revenue
Customer
Exposure
Position
Risk
~~~

那么最重要的可能不是“把更多文档检索出来”，而是：

~~~
What does Revenue mean?
Which definition is authoritative?
What dimensions are allowed?
What calculation is approved?
What time period applies?
Who owns this definition?
~~~

这就是 Semantic Layer 的价值。

它不一定“保存更多知识”，但它可以：

> 减少表示歧义和解释歧义。

这是一种不同的 fidelity。

因此现在更值得把：

~~~
Knowledge
~~~

理解成：

~~~
Evidence
+
Meaning
+
Access
+
Context
~~~

而不是：

~~~
Documents + Vector DB
~~~

---

## 17. 对 Agent Knowledge Architecture 的直接影响

这篇研究对当前项目的结论，我认为有五个。

### 17.1 不要再定义一个 Knowledge Store 就结束

应该区分：

~~~
Canonical Knowledge
Derived Knowledge View
Knowledge Access
Context
Evidence
~~~

### 17.2 每一次知识转换都应该保留 provenance

例如：

~~~
Source
  ↓
Chunk
  ↓
Embedding
  ↓
Retrieved Chunk
  ↓
Summary
  ↓
Context Item
~~~

应该知道：

~~~
where did this come from?
what transformation happened?
which version?
which authority?
when valid?
~~~

否则一旦答案错了，只能看到“模型答错”。

却不知道：

> 是 source 错了，还是 retrieval 错了，还是 compression 错了，还是 model 没用上。

### 17.3 Context Item 应成为一个一等对象

不要只有：

~~~
string[]
~~~

更应该接近：

~~~
ContextItem {
  content
  sourceRef
  evidenceRef
  authority
  version
  validAt
  transformation
  retrievalMethod
  accessDecision
}
~~~

这样才能回答：

> 这个信息为什么出现在当前 context？

### 17.4 Evaluation 不应该只有 Retrieval Recall

建议至少分层：

~~~
Source
Semantic
Representation
Retrieval
Context
Use
Evidence
Conflict
Answer
Action
~~~

如果把 Dark / Tacit Knowledge 纳入，还应该增加两类测试：

~~~
Behavioral Fidelity
Counterfactual Fidelity
~~~

因为某些 knowledge 并不会直接出现在答案里。

例如：

> 当关键条件从 X 改成 Y 时，Agent 是否做出知识上应该发生的判断变化？

这类测试比单纯检查“答案里有没有引用某句话”更接近真正的 Knowledge Use。

特别增加：

> Knowledge Use Evaluation

它真正问的是：

> Agent 答对，是因为用了 enterprise knowledge，还是因为本来就知道？

### 17.5 Knowledge Compilation 应该成为一个正式研究方向

把：

~~~
Source
→
Extract
→
Infer
→
Validate
→
Publish
→
Index
~~~

当成一个完整 lifecycle。

其中最值得研究的不是：

> 怎么更快做 embedding？

而是：

> 从原始知识自动产生一个更适合 Agent 使用的表示时，哪些信息被保留、哪些被抽象、哪些被删除、为什么删？

这才是真正的 Knowledge Engineering for Agents。

---

## 18. 我认为下一步真正值得做一个实验

如果这个问题要从“理论讨论”变成工程事实，可以设计一个非常直接的实验，而不是继续比较各种 RAG 产品。

准备一个固定的、结构化可标注的知识集合：

~~~
F = {f1 ... fn}
~~~

然后人为构造不同的知识表达路径。

### Path A：原文

~~~
Source → Full Context
~~~

### Path B：Chunk RAG

~~~
Source → Chunk → Top-K → Context
~~~

### Path C：Summary

~~~
Source → Summary → Context
~~~

### Path D：Graph

~~~
Source → Entity/Relation Graph → Context
~~~

### Path E：Semantic

~~~
Source → Semantic Model → Structured Query → Context
~~~

然后对完全相同的问题集测：

~~~
1. Relevant Knowledge Recall
2. Context Fidelity
3. Knowledge Use
4. Evidence Faithfulness
5. Conflict Resolution
6. Final Task Accuracy
~~~

最后画的不是一个柱子，而是一条曲线：

~~~
Source Size
   vs
Context Size
   vs
Knowledge Fidelity
   vs
Task Success
~~~

这才可能真正回答：

> 到底是哪一种知识表达方式，在什么任务上，以多少 token 成本，保留了多少可用知识？

---

## 19. 最值得做的不是“知识损失率”，而是 Knowledge Fidelity Curve

如果一定要得到一个工程化指标，我建议研究：

> Knowledge Fidelity Curve

横轴：

~~~
Representation / Context compression ratio
~~~

纵轴不是单一 Accuracy，而是：

~~~
Knowledge Recall
Context Fidelity
Knowledge Use
Evidence Faithfulness
Task Success
~~~

例如：

~~~
100% source
   │
   │──── full text
   │
   │──── chunk retrieval
   │
   │──── summary
   │
   │──── graph
   │
   │──── semantic representation
   │
   └──────────────────────────────→ compression
~~~

我们真正想找的是：

> 哪种表示在减少 80% context token 的同时，只损失 2% 的知识使用能力？

这个问题是可以实验的。

而：

> RAG 到底损失了多少知识？

单独问这个问题，没有统一答案。

---

# 20. 最终结论

### 第一，LLM 本身已经是一个有损但不是简单有损的知识存储系统

训练数据不会以“数据库复制”的方式进入模型。

同时，模型又会保留大量可以被重新提取的事实和模式。

所以不能简单说：

~~~
100% → 30%
~~~

也不能说：

~~~
100% → 90%
~~~

目前没有一个普适、可比较的数字。

### 第二，RAG 本身并不必然损失知识

如果：

~~~
retrieve
→
copy original evidence
→
context
~~~

那么文本传输本身可以非常接近无损。

真正的问题转移到了：

~~~
retrieval
+
context utilization
+
reasoning
+
conflict resolution
~~~

### 第三，真正严重的损失往往发生在“选择”和“使用”

尤其是：

~~~
全部知识
 ↓
选择少量知识
 ↓
放进 context
 ↓
模型决定关注什么
 ↓
模型决定相信什么
 ↓
模型决定怎样表达
~~~

这里每一步都会改变最终知识。

### 第四，Context Window 越大，不意味着 Knowledge Fidelity 越高

现有研究已经反复观察到：

~~~
More Context
≠
More Useful Knowledge
~~~

甚至：

~~~
More Context
→
Lower performance
~~~

在某些任务上已经可以明确观察到。

### 第五，Graph、RAG、Semantic View 都只是不同的知识表达和访问方式

它们解决的是不同问题：

~~~
RAG
= 找相关证据

Graph
= 表达和遍历关系

Semantic Layer
= 明确业务意义

Vector
= 高效相似性访问

Context
= 当前推理所见

Memory
= 长期状态

LLM Weights
= 参数化知识
~~~

没有一个单独的 primitive 能解决整个 Knowledge Fidelity Chain。

### 第七，Dark Knowledge 和 Tacit Knowledge 说明“知识”比答案大得多

Dark Knowledge 提醒我们，模型的 rich predictive structure 不会全部出现在 top answer 中；Tacit Knowledge 又提醒我们，某些 know-how 甚至很难完全转换成 propositions。

所以：

~~~
Answer
⊂
Observable Knowledge
⊂
Usable Knowledge
⊂
Latent / Tacit Structure
~~~

这个关系不是严格的数学集合定义，而是一个研究模型。

对 Agent 而言，真正需要保护的不是“生成了多少字”，而是：

> **做决定所需要的知识结构，在经过表示、检索、压缩和 context 投影之后，还剩下多少可用能力？**

这也意味着下一阶段的实验不能只比较答案准确率，还应该比较：

- soft alternatives / uncertainty；
- counterfactual behavior；
- boundary cases；
- evidence linkage；
- exception handling；
- decision consistency。

---

### 第六，Agent Knowledge 真正缺的不是另一个 Knowledge Base

更可能缺的是：

~~~
Knowledge Representation
+
Knowledge Access
+
Knowledge Projection
+
Knowledge Provenance
+
Knowledge Fidelity Evaluation
~~~

也就是：

> 知识如何表达、如何被选择、如何进入 context、如何被模型使用，以及我们如何证明它被正确使用。

这才是“AI Agent 知识表达和使用”真正值得研究的问题。

---

# 21. 一个新的研究模型

基于现在的资料，我建议把这个方向暂时定义成：

~~~
             ┌─────────────────────┐
             │ Canonical Knowledge │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Representation      │
             │ text / table /      │
             │ graph / semantic    │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Knowledge Access    │
             │ retrieve/query/     │
             │ navigate/fetch      │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Knowledge Projection│
             │ context selection   │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Knowledge Use       │
             │ recall/reason/use   │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Evidence / Action   │
             └─────────────────────┘
~~~

横跨整条链的不是一个数据库，而是：

~~~
Authority
Provenance
Freshness
Permission
Version
Evaluation
~~~

所以今后研究 Agent Knowledge 时，我认为最值得问的不是：

> 有没有 Knowledge Base？

而是：

> 这份知识经过了几次表示变化？每次变化保留了什么？丢掉了什么？为什么丢？当前 Agent 是否真的使用了它？我们有没有办法证明？

这可能才是“AI Agent 知识”这个问题真正的核心。

---

## 主要研究资料

1. Knowledge Boundary of Large Language Models: A Survey — https://arxiv.org/abs/2412.12472
2. Give Me the Facts! A Survey on Factual Knowledge Probing in Pre-trained Language Models — https://arxiv.org/abs/2310.16570
3. Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation — https://arxiv.org/abs/2307.11019
4. Scalable Extraction of Training Data from (Production) Language Models — https://arxiv.org/abs/2311.17035
5. Lost in the Middle: How Language Models Use Long Contexts — https://aclanthology.org/2024.tacl-1.9/
6. RULER: What's the Real Context Size of Your Long-Context Language Models? — https://arxiv.org/abs/2404.06654
7. Context Length Alone Hurts LLM Performance Despite Perfect Retrieval — https://aclanthology.org/2025.findings-emnlp.1264/
8. Context Rot: How Increasing Input Tokens Impacts LLM Performance — https://www.trychroma.com/research/context-rot
9. Diagnosing and Mitigating Context Rot in Long-horizon Search — https://arxiv.org/abs/2606.29718
10. LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models — https://arxiv.org/abs/2310.05736
11. LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression — https://arxiv.org/abs/2403.12968
12. ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems — https://aclanthology.org/2024.naacl-long.20/
13. Context-DPO: Aligning Language Models for Context-Faithfulness — https://aclanthology.org/2025.findings-acl.536/
14. FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation — https://aclanthology.org/2025.acl-long.1062/
15. LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs — https://proceedings.mlr.press/v267/li25dv.html
16. Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs — https://arxiv.org/abs/2603.09906
17. Distilling the Knowledge in a Neural Network — https://arxiv.org/abs/1503.02531
18. What Do Large Language Models Know? Tacit Knowledge as a Potential Causal-Explanatory Structure — https://doi.org/10.1017/psa.2025.19
19. Tacit knowledge in large language models — https://link.springer.com/article/10.1007/s11138-025-00710-5
20. Leveraging Large Language Models for Tacit Knowledge Discovery in Organizational Contexts — https://arxiv.org/abs/2507.03811
21. Tacit knowledge — Wikipedia — https://en.wikipedia.org/wiki/Tacit_knowledge
