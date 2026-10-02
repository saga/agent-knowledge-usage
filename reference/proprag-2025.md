# PropRAG：沿 Proposition Path 进行检索

来源：https://aclanthology.org/2025.emnlp-main.317/  
会议：EMNLP 2025

## 为什么只用 triples 不够

知识图谱很擅长表达：

~~~text
A --owns--> B
B --locatedIn--> C
~~~

但真实业务知识常常同时包含条件、例外、时间、主体、行为、适用范围和来源。

例如：

> 当账户满足某个条件，并且在某日期之后完成认证时，某流程才可以继续。

这不是一个普通 binary relation。

## PropRAG 的思路

PropRAG 使用 proposition 作为知识单元，再沿 proposition 之间的关系进行检索。

~~~text
Natural language proposition
       +
Graph relation
       ↓
Proposition path
       ↓
Evidence
~~~

它在两个世界之间搭桥：

~~~text
Document text
      ↕
Structured graph
~~~

## 为什么适合 Business Knowledge

企业规则经常夹在：

~~~text
table
vs
document
vs
business rule
~~~

之间。

Metric 可以结构化到 semantic layer。

但 policy exception、approval condition、operating procedure、legal clause，往往更接近自然语言 proposition。

所以现实的 Knowledge Model 不应该只有：

~~~text
Entity + Relation
~~~

还应该有：

~~~text
Proposition / Claim
~~~

## Proposition 需要哪些属性

从架构角度，一个长期可用的 proposition 至少可以带：

- stable id；
- text；
- subject / entity references；
- relation references；
- source；
- source location；
- effective time；
- authority；
- status；
- confidence。

于是 Agent 可以：

~~~text
retrieve proposition
   ↓
follow related proposition
   ↓
open source evidence
   ↓
answer
~~~

## 重要边界

Proposition 仍然是 derived knowledge，需要能回溯：

~~~text
source document
   ↓
extraction
   ↓
proposition
   ↓
graph relation
~~~

如果 proposition 自己成为唯一 source of truth，错误抽取会被永久放大。

## 对当前项目的具体意义

这支持一个值得长期保留的 primitive：

> Claim / Proposition

它可以成为 Knowledge、Graph、Evidence 三层之间的桥。

这样就不必把所有知识都强行塞进 document chunk、graph triple 或 vector embedding。
