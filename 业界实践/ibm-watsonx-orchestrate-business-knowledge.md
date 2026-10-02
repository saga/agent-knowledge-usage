# IBM：Knowledge Agent、知识库和 Agentic Control Plane

研究日期：2026-10-02

## 先看结论

IBM watsonx Orchestrate 当前值得研究的路线有两层：

1. Knowledge Agent / RAG，把企业内容转化成 source-grounded answers；
2. watsonx Orchestrate 作为 agentic control plane，负责发现、注册、路由、治理和观察 Agent。

因此 IBM 不是只研究“知识库”，而是在把 Knowledge 放进 Agent operating model。

## 1. Knowledge Agent 强调 approved sources + citations

IBM 当前的 AI Knowledge Agent 方案强调 SOP、manuals、intranet / internal content、citations、approved sources、inherited access control。

这说明企业 Knowledge 的核心不是“能搜到”，而是：

~~~
Approved Source
   ↓
Retrieval
   ↓
Grounded Answer
   ↓
Citation
~~~

## 2. watsonx Orchestrate 的 knowledge_bases 是独立能力

IBM 官方开发文档把 knowledge base provider 与 agent logic 分开。

当前知识库可以使用 managed Milvus，以及 external / configured providers。

因此：

~~~
Agent
 ├── instructions
 ├── tools
 └── knowledge_bases
~~~

而不是把 RAG 写死到 agent implementation 中。

## 3. IBM 同时强调 agent control plane

watsonx Orchestrate 当前还被定位为 register、discover、route、monitor、govern external agents 的控制平面。

这对当前 Common Agent Library 的意义在于：

> Knowledge provider、Agent capability、Agent governance 可以分别建模，再由 control plane 进行组合。

## 4. 对当前项目的启发

值得抽取：

~~~
KnowledgeBase
KnowledgeProvider
ApprovedSource
Citation
AgentRegistry
Capability
Governance
Observability
~~~

尤其应该保持：

~~~
Knowledge configuration
≠
Agent runtime
≠
Agent control plane
~~~

## 5. 局限

IBM 的 Knowledge Agent 页面中部分 time-to-value 和效果数字来自合作伙伴方案，并且 IBM 明确注明其没有独立验证。

因此不能把营销页面上的 deployment claims 当成成熟度或行业采用证据。

## Sources

- https://www.ibm.com/products/watsonx-orchestrate/ai-knowledge-agent
- https://github.com/IBM/ibm-watsonx-orchestrate-adk/blob/main/skills/wxo-builder/SKILL.md
- https://developer.ibm.com/components/watsonx-orchestrate/
