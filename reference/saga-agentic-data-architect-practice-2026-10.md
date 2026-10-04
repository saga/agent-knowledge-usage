# agentic-data-architect：长任务 Agent 的工程实践反馈（2026-10-05）

来源：https://github.com/saga/agentic-data-architect
最新实现基准：main，2026-10-05。

这不是“业界标准”总结，而是一条来自实际 Agent 工作台实现的工程证据。它主要补充 Knowledge、Context、State、Evidence 和 Agent Runtime 之间的边界。

## 1. 一个用户请求可以包含多个连续阶段

实际工作台把一次用户请求与一次 Copilot Session 区分开来。一个请求可以在同一个 Session 中连续执行多个阶段：

```text
User request
    ↓
Copilot Session
    ├─ execution 0
    ├─ execution 1
    ├─ execution 2
    └─ final result
```

每个阶段结束后，宿主重新读取最新的调查状态和 Workflow 位置，再决定是否继续。

这里得到的不是“需要一个新的 Workflow Engine”，而是一个更简单的边界：

> Workflow 定义高层工作阶段；Agent 决定阶段内部怎样调查。

## 2. 长任务需要 checkpoint，但不是每分钟写一条进度

运行状态只能回答 Agent 是否仍在工作；tool progress 只能说明它正在做什么。用户真正需要的是：到这里已经查清了什么。

因此增加了一个很小的 AgentCheckpoint：

```text
title
summary
confirmed
evidenceIds
unknowns
nextStep
```

Checkpoint 有三个特点：

- 它是阶段性工作成果，不是 telemetry。
- 它引用现有 Evidence，而不是复制另一套事实存储。
- 它不替代最终报告，也不负责 Workflow 编排。

最重要的限制是：没有新的实质成果时，不应该为了“看起来有进度”而生成 checkpoint。

## 3. Knowledge Projection 不只发生在最终回答

这条实现反馈对 Knowledge Architecture 有一个值得继续研究的含义：

```text
Long-lived knowledge / evidence
        ↓
selection + investigation
        ↓
current working understanding
        ↓
checkpoint
        ↓
continued investigation
        ↓
final answer
```

Checkpoint 可以理解为当前 Investigation 对知识的一次受约束投影。

它最好保留：

- 已确认事实；
- 对应 Evidence；
- 仍然未知的部分；
- 下一步调查方向。

这样中间成果不仅服务 UI，也可以帮助下一阶段继续工作，减少把完整工具日志重新塞进 context 的需要。

但 checkpoint 仍然不是 Canonical Knowledge。它是当前任务的工作产物，必须能回到 Evidence / Source。

## 4. execution state 与历史 trajectory 必须分开

实际实现中，trajectory.jsonl 用来记录历史运行事件；当前 Agent 是否真的还在运行，则由进程内 active turn 和 pending interaction 判断。

也就是说：

```text
Historical trajectory ≠ Live execution state
```

这对长期 Agent 很重要。历史上出现过 waiting、timeout 或 session_idle，并不意味着当前 turn 仍然处于那个状态。

因此 Context / State 研究中应该明确区分：

- Durable work records：已经发生过什么；
- Live execution state：现在正在发生什么；
- Working context：下一次模型调用真正需要看到什么。

## 5. execution timeout 与 human wait 是两个不同预算

实际运行发现，一个统一的 sendAndWait timeout 会把两个完全不同的时间混在一起：

```text
Agent execution
    → 有限执行预算

ask_user / human input
    → 独立等待预算
```

用户花一小时回答问题，不应该被当成 Agent 执行了一小时。

因此长期 Agent 的状态模型至少应该区分 execution、permission wait 和 user-input wait。

这不是要求做一个通用 HITL Runtime；它只是一个应该被保留的 contract / runtime boundary。

## 6. Reasoning / Think 不等于 Knowledge

实际工作台把 reasoning 增量作为可选的运行时输出，但不写入 Evidence、Knowledge、Memory 或业务 Audit。

原因很直接：

```text
reasoning stream = runtime presentation
knowledge / evidence = durable business information
```

二者需要不同生命周期、不同可信度和不同治理方式。

## 7. 对整个 Knowledge Architecture 的影响

这次工程反馈把原来的模型再往前推进了一步：

```text
Canonical Source
      ↓
Knowledge / Semantic / Evidence
      ↓
Knowledge Access
      ↓
Working Context
      ↓
Agent investigation
      ↓
Checkpoint / State
      ↓
Final answer / Action
```

Checkpoint、State 和 Memory 都可能保存“当前工作认知”，但不能因此自动获得 Canonical Authority。

一个很实用的原则是：

> 越靠近 Agent 当前工作上下文，生命周期越短；越靠近 Source / Evidence，权威性越强。

## 8. 目前不能从这个案例得出的结论

这个项目只证明这些设计在一个真实 Data Architecture Agent 中有价值，不能证明：

- 所有 Agent 都需要 checkpoint；
- 所有框架都应该采用同一种 checkpoint schema；
- 长任务一定应该自动连续执行；
- reasoning 永远不应该持久化；
- Copilot SDK 的具体实现方式适合所有 Agent runtime。

这些仍然应该通过更多项目和框架交叉验证。

## 结论

这次实现最值得留下的不是一个新组件，而是几个清晰边界：

```text
live state      ≠ historical trace
progress        ≠ work product
checkpoint      ≠ canonical knowledge
execution wait  ≠ human wait
reasoning       ≠ durable evidence
```

这些边界可以进入 Common Agent Library 的 contract / pattern 层，但不需要因此建立新的“大 Agent Framework”。

