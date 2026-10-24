# Claude Code 2.1.310 本机架构分析

> 调查日期：2026-10-24（Asia/Shanghai）  
> 分析对象：本机实际执行的 Claude Code 发布件。  
> 方法：REA 静态分析、Mach-O/签名检查、发行件 JavaScript 提取与语法解析、CLI 帮助检查。  
> 结论范围：客户端实现；不涵盖 Anthropic 服务端内部架构。

## 1. 核心结论

本机 Claude Code 是一个将 **Bun / JavaScriptCore 运行环境、JavaScript 业务模块和资源打包到 ARM64 Mach-O 中的代理应用**。它的架构重点是管理一个持续、多轮、有状态的工具调用过程：接收请求，准备上下文，调用模型，处理流式响应，执行工具，回填结果，再决定继续或结束。

围绕这一核心，它还实现了终端界面、机器可读的 headless 接口、后台会话、权限决策、操作系统级命令沙箱、会话持久化、MCP、插件与生命周期 Hooks。CLI 是这些子系统的入口集合；不能把 CLI 帮助中列出的每种能力都视为本机已经启用的服务。

最值得关注的五个设计点：

1. **分发载体与业务实现分开理解。** 虽然安装物是原生可执行文件，内部依然可以观察到大量 JavaScript 模块与 JS 引擎结构。
2. **模型与本地执行器分开。** 本地程序负责上下文、策略、执行与状态管理，模型调用是其中一个外部边界。
3. **显示与执行分开。** React/Yoga 终端界面和 stream-json/headless 接口都围绕代理执行过程组织，但其适配、事件转发与交互方式不同。
4. **权限与沙箱是不同层。** 工具权限回答“是否允许这个动作”，沙箱限制特定子进程对文件系统和网络的访问。二者不能互相替代。
5. **会话是可恢复的结构化状态。** 发行代码中既有 JSONL 转录处理，也有带 namespace/key 的 storageV5 接口；恢复不只是重新读取一份可见聊天文本。

## 2. 对象身份与可重复性

| 项目 | 本次实际结果 |
|---|---|
| 命令入口 | `/Users/huangzhuangjia/.local/bin/claude` |
| 入口类型 | 指向版本文件的符号链接 |
| 实际文件 | `/Users/huangzhuangjia/.local/share/claude/versions/2.1.310` |
| CLI 自报版本 | `2.1.310 (Claude Code)` |
| 文件大小 | 274,068,224 bytes，约 261.37 MiB |
| SHA-256 | `ffb64331bc0ee1b69efb7c2c428bd3ab516bc31b75bf60886b356c97c1c25ffd` |
| 格式 | thin Mach-O，64-bit，arm64 |
| 最低系统 / 构建 SDK | macOS 13.0 / SDK 26.5 |
| 签名主体 | Developer ID Application: Anthropic PBC |
| Team ID | `Q6L2SF6YDW` |
| Bundle identifier | `com.anthropic.claude-code` |

以上是这个确切哈希对应版本的分析，不代表其他安装渠道、历史版本、Windows 或 Linux 发布件与它完全相同。[NATIVE](evidence/native.txt)、[REA Mach-O](evidence/macho.json)

### 2.1 证据等级

全文采用三种表述：

- **静态事实**：文件元数据、语法结构、函数体、参数校验、数据读写代码中直接可见。
- **CLI 契约**：目标程序自己输出的 `--help` / `--version` 描述；证明入口和声明行为，未证明成功运行。
- **架构推断**：从上述事实归纳出来的层次、职责或设计动机；不冒充原作者的内部设计文档。

调查没有发起模型推理、启动云会话、连接 MCP 服务器、运行插件、执行工具任务或更改安装；没有读取用户的凭证值、设置值和历史会话内容。目标程序只执行了版本和帮助命令。这里分析的是安装软件的能力与代码，不是账户当前配置。

### 2.2 JavaScript 提取边界

扫描发行二进制中的 `// @bun @bytecode` 文本标记，取得以 NUL 结尾的 UTF-8 文本候选，并保留原文件字节范围与 SHA-256。共发现 2,569 个候选，其中 `module-000.js` 是 Bun 运行时内部的标记模板，不能解析，已经排除；**其余 2,568 个候选通过 JavaScript 语法解析**。所有候选共约 49.6 MB，包含应用代码和打包依赖。

`module-499.js` 等名称是本次分析生成的编号，并非开发仓库的真实文件名。保留的 `/$bunfs/root/chunk-*.js` 导入路径是构建产物路径，不是可直接访问的开发源码路径。本次没有完整解码 Bun 的虚拟文件系统索引，也没有恢复 TypeScript 类型、原始模块目录或完整 sourcemap。因此，本文给出的是**功能架构重建**，不是声称恢复了原始源码工程。

REA 对 9 个选定模块执行了局部语法/语义分析，读入 311,938 bytes，访问 73,198 个 AST 节点，9 个文件均解析成功。关系图为 **partial**；1,000 条保留的 semantic unknown 达到此次容量上限。其摘要不能作为“全部代码已分析”的证明。另用惰性 AST 遍历检查其余文本，未执行这些 JavaScript。[REA 证据](evidence/rea-evidence.json)、[提取清单](evidence/extraction-manifest.json)

## 3. 总体架构

下面是依据职责归纳的架构视图；框中的功能在发行代码或 CLI 中有证据，连线表示概念数据流，不代表逐条恢复的原生调用图。

```text
使用者 / SDK 宿主 / 后台管理命令
                │
     ┌──────────┴────────────┐
     │ CLI 启动与配置、模式选择 │
     └──────────┬────────────┘
                │
   ┌────────────┼────────────────┐
   │            │                │
交互式 TUI   Headless / SDK    后台会话与云/远程入口
React/Yoga   text/json/JSONL    部分为可选集成
   │            │                │
   └────────────┼────────────────┘
                ▼
     ┌──────────────────────────────┐
     │  Agent 编排核心               │
     │  messages / prompt / context │
     │  streaming / tool loop       │
     │  compact / retry / stop      │
     └──────┬────────────────┬──────┘
            │                │
        模型适配层       工具调用调度层
            │                │
      外部推理提供方    schema / permissions / hooks
                             │
                   ┌─────────┼──────────┐
                   │         │          │
                本地工具   MCP 工具    扩展/子任务
                   │
           进程 / FS / 网络与可选沙箱

横向支撑：配置与策略 │ 认证 │ storageV5 / transcript
          插件与技能 │ IDE/LSP │ 遥测与成本记录
底层载体：Bun + JavaScriptCore + macOS 系统 API
```

模型服务端的训练、调度、模型权重、推理集群、租户隔离均不在本地文件可证明的范围内。

## 4. 分发、启动与运行时

### 4.1 单文件不等于纯原生业务实现

Mach-O 中存在 `__BUN/__bun`、`__bun_builtins`、`__jsc_int`、`__jsc_opcodes`。`__BUN` 段从文件 offset 93,241,344 开始；其 `__bun` 节约 180 MB。提取文本还能看到 `/$bunfs/root/` 虚拟路径、ESM imports 和压缩后的函数定义。两类证据共同支持“嵌入运行时 + 打包 JS”的判断。

动态依赖表列出了 `libicucore.A.dylib`、`libresolv.9.dylib`、`libc++.1.dylib` 和 `libSystem.B.dylib`。未列外置 Node 或 Bun dylib，符合运行时随 executable 交付的模式；运行时可能使用 `dlopen`，所以不能把这份表当作所有动态依赖的完整清单。

### 4.2 启动入口与工作目录

`module-001.js` 的 `bis()` 读取 cwd，尝试 `realpathSync` 并做 NFC 归一化，失败则保留归一化路径；`tRt()` 根据后台会话环境标记决定是否返回初始 cwd。说明启动目录不仅用于显示，还参与会话及宿主环境的组织。[S01](evidence/source-anchors.md#s01)

`module-848.js` 中可见选项读取、CLI 来源识别、MCP 设置迁移、模式分支、认证检查、遥测初始化和启动 Hook 的调度。它是启动协调层之一，不能据单个模块就断言它是唯一入口。[S02](evidence/source-anchors.md#s02)

### 4.3 安装与更新

实际布局是 `bin/claude → share/claude/versions/<version>`；CLI 支持 `install [stable|latest|version]` 和 `update|upgrade`。从架构上看，入口和具体版本分开，便于版本替换；本次没有执行 updater，不确定替换是否原子、旧版本保留策略和回滚机制。`respawn` 命令的帮助明确表示可重启后台会话，使其运行当前版本的 binary。[CLI 子命令](evidence/cli-subcommands.txt)

## 5. 输入输出与界面层

### 5.1 交互式终端 UI

发行代码中存在 React element/context/hooks 实现。`module-489.js` 可见 `react.transitional.element`、`useState`、`useSyncExternalStore` 等结构；`module-579.js` 包含 `R5e` 终端渲染器类、`ink-*` 节点、Yoga 布局调用、屏幕/光标/选区状态与帧调度。

`R5e.calculateYogaLayout()` 根据终端 columns 设置布局宽度；非 TTY 时采用自动宽度，并在超过上限时重新布局。`runLayoutPass()` 捕获布局异常，调用 `relayoutFromScratch()` 清理布局缓存后重试，并记录恢复或持续失败状态。这表明界面层不只是 `console.log`，而是带布局、差异绘制及终端状态管理的组件渲染系统。[S03](evidence/source-anchors.md#s03)、[S04](evidence/source-anchors.md#s04)

可以称其为 **React / Ink 风格的终端渲染架构**。存在 `ink` 节点或日志并不能证明它使用未修改的某个公开 Ink 版本；本文不指定未经验证的 UI 库精确版本。

### 5.2 Headless 与机器协议

CLI 支持 `-p/--print`，输入 `text` 或 `stream-json`，输出 `text`、`json`、`stream-json`。`module-1920.js` 还显式导出 `runHeadless`、`loadInitialMessages`、`mergeMcpClientLists`、`ownCostLedger` 和启动 SDK 事件转发相关函数名。这为“独立 headless 适配层”提供了比帮助文本更直接的代码证据。[S05](evidence/source-anchors.md#s05)

可选接口包括增量消息、用户消息重放、Hook 事件、子 Agent 的 `parent_tool_use_id`。架构上，这使外部宿主可以在不实现终端 UI 的情况下驱动会话并消费事件。但本次没有启动 SDK 会话，未验证全部事件 schema、错误编码、背压和重连语义。

### 5.3 云、Desktop、IDE 与浏览器入口

帮助项声明 `--cloud`、`--environment`、`--desktop`、`--ide`、`--chrome` 和远程控制能力。`module-848.js` 的 cloud 分支会检查 session id、认证/许可状态、会话归档状态及输出格式；例如该分支明确拒绝某些 `stream-json` 组合。因而这些入口不是简单共享所有本地选项的等价通道。

本次未连接这些集成，不推测其完整后端部署与账户可用性。

## 6. Agent 主循环：从请求到工具反馈

### 6.1 真实执行骨架

`module-745.js` 的 `yN()` 是可见的 turn 包装器，`ku()` 维护查询状态，内部 `Cu()` 执行一轮。状态包括 `guards`、`messages`、`toolUseContext`、`compactTracking` 和 `transition`。外层用 `while` 继续执行，`next_round` 表示再来一轮，其他返回值结束流程。[A1–A3](evidence/agent-loop.md)

虽然代码日志里出现 `query_recursive_call`，这里可见的实现是异步生成器加显式状态机，不能仅凭日志名字把它描述成不断增加 JS 调用栈的递归函数。

默认依赖对象 `Dd()` 包含：

```text
callModel   → YNt
 autocompact → SMr
uuid        → UUID 生成器
now         → 当前时间生成器
```

这种可注入依赖边界使查询引擎不必直接承担每个模型 SDK、时钟和压缩实现的细节。关于可测试性的解释属于架构推断；本次没有运行其内部测试。[A3](evidence/agent-loop.md)

### 6.2 一轮会做什么

1. 从最近的 compact boundary 取得当前有效历史，接收新到达的消息或状态。
2. 更新模型选择、model facts、有效窗口与上下文预算。
3. 必要时自动压缩，准备 system prompt、messages、工具描述及请求选项。
4. 通过 `callModel` 发出请求，消费异步响应流。
5. 遇到 `tool_use` 时提交到流式工具执行器，输出执行过程事件。
6. 收集工具结果与更新后的上下文；检查取消、延迟工具、Hook 阻断和轮次限制。
7. 将 assistant 消息与工具结果追加到下一轮历史，或执行 stop hooks 后结束。

这是一条从实际函数体整理出来的路径，不是根据“Agent 一般如何工作”套出的模板。工具可以在响应流处理期间入队，说明“模型输出流”和“工具执行流”在部分路径上能重叠；并不意味着任意工具调用都并行。[A4–A7](evidence/agent-loop.md)

### 6.3 失败是状态转换的一部分

核心循环区分 prompt too long、图片错误、输出 token 耗尽、无法解析的 tool_use、只输出 thinking、取消和 stop hook 等情况。部分错误触发一次或有限次上下文压缩/恢复请求，达到上限后返回明确终止状态。[A8](evidence/agent-loop.md)

因此，“失败后重试”不是一个统一重发按钮：不同故障会改变上下文、重试标记、提示或结束原因。本次只证明这些恢复分支存在，不验证其所有运行组合和重试成功率。

## 7. 模型、请求与供应商适配

### 7.1 Model facts

`module-499.js` 的 `_c()` 返回模型事实：context window、max output tokens、canonical model、settings key、长上下文状态、bytes-per-token 估算和 thinking/temperature 支持等。`module-745.js` 会取得这些数据用于请求和预算处理。[M1](evidence/agent-loop.md)

含义是：代理执行逻辑围绕一个模型能力对象工作，而非仅凭用户输入的字符串决定所有行为。窗口、输出限制和 thinking 约束属于请求编排层的输入。bytes-per-token 是预算线索，不应当作服务端精确 tokenizer 的实现。

### 7.2 可见调用关系

```text
query state machine
  → 默认 callModel: YNt
  → 请求包装 wSn / lSn
  → provider client factory: bF
  → 对应 SDK / endpoint
```

`module-231.js` 的 `bF()` 具有 gateway、Bedrock、Foundry、Anthropic AWS / Google Cloud、Mantle、Vertex 和默认客户端分支，分别处理 region、headers、baseURL、fetch override 和认证解析器。这里列的是本发布件中的分支名，不能推定每个分支都是公开可用产品或本机当前使用的路径。[M2–M4](evidence/agent-loop.md)

还观察到 `beta.messages.create(..., {signal, timeout})` 的非流式分支，以及核心查询的流式消费路径。本文不声称已穷尽全部 transport dispatch 或模型 fallback 组合。

**架构推断**：对 Agent 核心而言，模型服务通过共同的消息、工具和流事件契约接入；不同提供方的地址、认证与 SDK 差异收敛在适配层。工具本身无需分别实现每种云模型协议。[M5](evidence/agent-loop.md)

## 8. 工具系统：合同、调度与执行

### 8.1 Tool 合同

可见工具对象具有以下字段或方法，部分为可选：

| 合同部分 | 职责 |
|---|---|
| `name` / aliases / description / prompt | 标识、用户或模型可见说明 |
| `inputSchema` / `inputJSONSchema` | 输入结构合同 |
| `outputSchema` | 某些结果的结构验证 |
| `isEnabled` | 是否进入本次可用集合 |
| `isReadOnly` / `isConcurrencySafe` | 操作属性与调度提示 |
| `validateInput` | 工具特定的语义校验 |
| `checkPermissions` | 工具自己的权限决策参与点 |
| `call` | 实际执行 |
| `mapToolResultToToolResultBlockParam` | 转换为模型协议中的工具结果 |

内置工具和 MCP 适配工具都可参与这套合同。不要将可选方法描述成每个工具必须具备的固定接口。[TE-01、TE-07、TE-14](evidence/tools-extensions.md)

### 8.2 并发执行器

`module-745.js` 的 `Ls` 维护 `queued → executing → completed → yielded` 状态。调用入队前，用 schema 解析成功的数据判断 `isConcurrencySafe`；不确定或判断抛错时按不安全处理。已有工具执行时，只有新工具和所有在执行工具均允许并发，才会重叠运行。不安全工具等待独占，且会阻挡后面的队列项继续调度。[A6](evidence/agent-loop.md)、[TE-01/02](evidence/tools-extensions.md)

这更接近一个带并发约束的调度器，而不是对模型生成的调用数组直接 `Promise.all`。执行器还拥有派生取消控制器、完成结果保留和中止未完成调用的逻辑。

### 8.3 单次调用的执行链

工具执行的可见路径可概括为：

```text
模型 tool_use
 → 解析名称 / alias，必要时等待动态 MCP 工具
 → JSON / schema / validateInput
 → PreToolUse
 → HOr / T8r / canUseTool 等权限处理
 → behavior == allow
 → tool.call
 → PostToolUse
 → 对改写输出再次验证
 → tool_result 回到消息流
```

`module-499.js` 的 `D6`、`o7r`、`f7r` 等函数承担上述调度与执行职责。拒绝、取消或工具不存在等情况会形成错误工具结果，保持对话协议中的调用与反馈关联。PostToolUse 若改写输出，代码还会验证改写数据，不能认为 Hook 可以任意改变结构而无检查。[TE-03–08](evidence/tools-extensions.md)

## 9. 权限与沙箱

### 9.1 应用级权限决策

CLI 暴露 `manual`、`acceptEdits`、`auto`、`dontAsk`、`plan`、`bypassPermissions` 模式，以及 allow/deny 工具规则、额外工作目录、SDK 宿主权限回应。

继续追踪 `HOr → T8r` 可见：PreToolUse 的 deny 阻断执行；Hook 的 allow 不能覆盖匹配的 deny rule；ask rule、安全检查、plan mode 或 `requireCanUseTool` 条件仍可要求中央权限决策。因而“Hook 返回 allow = 无条件执行”的说法与本次可见实现不符。[TE-26](evidence/tools-extensions.md)

本次没有穷尽 managed policy、分类器、所有工具私有规则的完整组合优先级，不能把上面局部事实扩展成一份完整的权限形式化规范。

### 9.2 操作系统级命令沙箱

`module-320.js` 的可见实现中，macOS 路径会构造 `sandbox-exec -p <profile> ... shell -c ...`；Linux 路径构造 `bwrap` 参数。代码还包含网络代理、文件读写路径、参数长度和 NUL 检查等处理。[TE-09/10](evidence/tools-extensions.md)

这里能证明的是打包代码具有这些平台后端；**未验证本机当前会话启用了哪套沙箱，也未验证所有工具、MCP server 或插件进程均处在同样的边界内**。Linux 分支出现在 macOS 包里，不等于它在这台机器运行。

### 9.3 签名安全与 Agent 权限不是一回事

本文件的签名验证通过，hardened runtime 开启，同时声明 allow-jit、allow-unsigned-executable-memory、disable-library-validation、Apple Events 和音频输入等 entitlement。它们描述操作系统允许该程序申请或使用的能力，不能证明已取得用户 TCC 授权或正在执行录音/自动化。[签名证据](evidence/native.txt)

签名验证不等于工具权限审计，也不等于在线 notarization 验证；本次没有执行后者。

### 9.4 三种启动缩减模式

| 模式 | 本版本帮助的声明 | 架构解释与边界 |
|---|---|---|
| `--bare` | 跳过 Hooks、LSP、plugin sync、auto-memory、预取、Keychain、CLAUDE.md 自动发现等；显式技能仍可解析 | 最小启动路径，不等于无网络或无执行工具 |
| `--safe-mode` | 禁用多种用户定制；admin managed policy 仍适用，内置工具、认证和权限正常 | 排查定制问题的隔离入口，不等于 OS 沙箱 |
| `--restricted` | 默认移除部分代码执行和抓取工具，约束设置来源和路径，拒绝 bypass | 受限工具运行策略，仍需分别考虑 MCP 与 OS 隔离 |

以上是本地 `--help` 契约，未逐项运行验证。[根帮助](evidence/cli-help.txt)

## 10. 上下文、提示快照与压缩

### 10.1 Prompt snapshot

CLI 的 `--system-prompt-snapshot` 帮助明确描述：通常在首次请求记录渲染后的 system prompt，后续请求与恢复复用，直到 compact；也可选择关闭快照以每次重建。`module-499.js` 中可见 `prompt_snapshot`、`prompt_render_point`、`deferred_tools_record`、快照解析缓存及开关判断 `rje()`。[S06](evidence/source-anchors.md#s06)、[根帮助](evidence/cli-help.txt)

这说明本版本不仅保存用户和 assistant 文本，还记录某些“发送时上下文”的结构。**架构推断**：它有助于维持请求前缀稳定，并让恢复会话保留既有提示上下文；实际服务端缓存命中率未测量。

### 10.2 Compact boundary 与摘要

`module-382.js` 的 `ks()` 从最近 `compact_boundary` 起选择当前历史。自动压缩调度器 `SMr()` 检查模型窗口、预算、开关、预计算结果及失败状态；实际摘要函数 `yMr()` 运行 PreCompact、构造摘要模型请求、清理部分读文件/记忆状态、重建附件，生成 boundary 与 summary，再运行 PostCompact。[C1–C4](evidence/agent-loop.md)

压缩后的有效消息不是只把历史替换为一段字符串，而是类似：

```text
boundary
 + summaryMessages
 + optional replacement
 + messagesToKeep
 + attachments
 + hookResults
```

全量摘要路径可能不保留原消息，但不能因此断言所有压缩方式都清空原始消息。摘要需要额外模型调用，这也意味着压缩具有耗时、费用和信息选择成本；本次没有执行并测量。

### 10.3 保护与恢复

可见代码跟踪反复快速填满上下文的次数，并在满足条件时触发 rapid-refill breaker；预计算摘要在复用前检查相关 UUID 和历史变化。请求过长的 reactive compaction 也有尝试标记和有限恢复路径。[C5/C6](evidence/agent-loop.md)

本次不提供“固定到 80% 就必然压缩”这类规则：实际行为依赖模型窗口、设置和条件分支。也没有恢复完整 recall、microcompact 或服务端 tokenizer 算法。

## 11. 会话持久化、恢复与成本状态

### 11.1 不止可见对话文本

`module-499.js` 的转录处理代码维护 `uuid → parentUuid` 关系，区分 transcript、accumulate、last-wins 等记录类别，还处理 compact boundary、file-history snapshot/delta、attribution、工具记录等。[S07](evidence/source-anchors.md#s07)

父子 UUID 关系允许把会话看作结构化记录链；这是从代码结构推导的解释。本文不据此宣称已完整恢复所有分支、fork 和重写规则。

### 11.2 JSONL 与 storageV5 同时存在

本发布件包含以 `<sessionId>.jsonl` 定位转录、追加 JSON 行、修复缺少结尾换行、处理部分写入和同步 mirror 的实现。另一方面，多个函数通过 `storageV5` 的 backend、namespace/key、`readRecords`、`append`、`replaceRecords`、`stat` 等接口操作数据。

例如 `xRr()` 按反向顺序和字节窗口读取记录，并在跨页时检查锚记录是否改变；`YBe()` 使用文件描述符追加到已有文件，并显式处理 short write；`DPt()` 写入 JSON 行后通知 mirror。[S08](evidence/source-anchors.md#s08)、[S09](evidence/source-anchors.md#s09)

**架构判断**：这里存在存储抽象与兼容/过渡路径，不能简化成“所有状态都直接写到一个 JSON 文件”。也不能因为看到 `storageV5` 就断言本机启用了某个远程或数据库后端。当前实际存储后端、迁移完成度和用户文件状态未检查。

### 11.3 历史、转录与成本的区别

`module-378.js` 中的 history 写入器通过 `backend.append(historyKey, records)` 或文件路径保存输入历史，具有 pending entries、flush 和错误分类。`module-1620.js` 包含 history purge 的扫描与替换逻辑，并拒绝某些符号链接/非普通文件情形。这和完整 transcript 是不同职责。[S10](evidence/source-anchors.md#s10)

`cost-state` schema 单独记录费用、API/工具耗时、增删行数、输入/输出/thinking tokens、cache read/create tokens、web search 次数以及按模型用量。这些是客户端状态合同，不等于最终账单结算真值。[S11](evidence/source-anchors.md#s11)

CLI 的 continue/resume/fork-session、stop/attach、purge 等契约也印证：会话身份、转录、运行进程和工作树需要分别管理。

## 12. Subagent、后台任务与协作

### 12.1 主引擎复用

交互入口 `module-1892.js` 的 options 设置 `isNonInteractiveSession: false, runQuery: yN`；非交互入口 `module-1920.js` 设置 `isNonInteractiveSession: true, runQuery: yN`。子 Agent 的 `qR()` 复用父 `options.runQuery`，并重新构造自己的 messages、system/user context、工具和权限。

因此，在这两个已检查的入口中，主 Agent 和子 Agent 共用同一查询引擎接口与实现绑定；“开一个子 Agent”主要是构建新的上下文和生命周期，不是另写一套推理循环。[S8](evidence/agent-loop.md)、[S14](evidence/source-anchors.md#s14)

### 12.2 Agent tool 与任务注册

`module-692.js` 的 Agent 工具解析 agent type、model、effort、cwd、isolation 和 run_in_background；检查递归深度、允许类型和权限。异步分支注册任务，前台分支则等待或允许后续切换后台。

`Dle()` 注册的 `local_agent` 状态包含 owner/parent agent、spawn depth、selected agent、abort controller、pending messages、keepalive 与 background 标志。`UDs()` 的前台任务还有 background signal、父取消中继和可选自动后台定时器。[S1–S5](evidence/agent-loop.md)

可以将其分成四个状态域：

| 状态域 | 负责的问题 |
|---|---|
| Query state machine | 当前模型轮次、工具结果、继续或停止 |
| Tool executor | 哪些调用可并行、取消、结果交付 |
| Task registry | 子任务归属、运行状态、前台/后台生命周期 |
| Team/mailbox runner | 持续等待消息、协作者空闲和关闭 |

### 12.3 长生命周期协作者与后台进程

`module-1776.js` 中还有同进程 teammate runner：消费新消息、调用子 Agent 引擎、必要时压缩自己的历史、等待 mailbox 或 shutdown，并处理空闲退出。它是发行件中的一条能力路径，未证明当前账户已开启团队能力。[S6/S7](evidence/agent-loop.md)

另外，CLI `--background`、attach/logs/stop/rm/respawn 表示进程级后台会话控制。`module-621.js` 中可见后台 spawn 环境整理、PATH 处理、配置目录校验和隔离相关变量。**子 Agent 异步任务、同进程 teammate、独立后台会话是不同概念**，文档不把它们统称为“每个 agent 都是一个新进程”。[S12](evidence/source-anchors.md#s12)

## 13. MCP：外部工具客户端与内部工具服务器

### 13.1 作为客户端

`module-2110.js` 实现多种 transport 路由、握手/协议协商、tools/list 刷新与重试、listChanged 处理、活动调用 watchdog、错误状态与 elicitation 生命周期。stdio transport 使用 `shell: false`，管理 stdout 增量消息和子进程回收。[TE-11–13](evidence/tools-extensions.md)

调用链可以抽象为：

```text
server configuration
 → transport / handshake
 → capabilities + tools/list
 → 包装成统一 Tool
 → Agent 工具集合
 → 统一调度与权限
 → MCP call
```

上游 input schema 被转换到本地工具合同；annotations 中 readOnlyHint 可参与只读及并发判断。这个 hint 是服务器提供的声明，不是证明外部工具没有副作用。权限处理仍会 ask 或交中央策略，不是 MCP 连接成功后就默认任意执行。[TE-14](evidence/tools-extensions.md)

transport 和协议分支受配置、feature flag、denylist 等约束；公开 `mcp add` 支持的选项与内部所有 transport 类型也不完全一致，不能据内部 switch 列表给出用户通用命令。

### 13.2 作为服务器

CLI 还公开 `mcp serve`。`module-2484.js` 注册 tools/list 与 tools/call handler，动态计算工具集合，输入经过 schema、validateInput 和 `checkPlainCall` 后再调用内部工具；结果被转换为 MCP 返回格式，取消与错误另行处理。[TE-15/16](evidence/tools-extensions.md)

这里可以对外暴露工具执行能力，不能未经验证就将其描述成“通过 MCP 启动完整 Claude 对话模型”。本次未启动该服务，也未列出运行时实际可服务工具清单。

## 14. Plugin、Skill、Hooks、LSP 与 IDE

### 14.1 Plugin 是扩展组件容器

manifest 读取先尝试 `.claude-plugin/plugin.json`，再尝试 `plugin.json`。代码识别 commands、agents、skills、output styles、themes、workflows、monitors，以及 MCP、LSP 和 Hooks 配置。[TE-18](evidence/tools-extensions.md)

`module-1201.js` 的 `P$()` 刷新过程会清缓存、重读配置、并发加载 commands/skills/agent definitions、加载 MCP/LSP、应用刷新状态并注册 Hooks；错误和警告单独收集。这是一套可部分失败的扩展加载系统，并非简单拼接一段 prompt。[TE-17](evidence/tools-extensions.md)

CLI 另外提供插件安装/更新/校验、marketplace、详情和评估接口。当前机器的具体已装插件及其来源未读取。

### 14.2 Skill 是上下文和执行选项的可调用描述

实际插件 Skill 加载链 `TXo → Hje` 枚举技能路径，使用 realpath 去重，也避免重复加载已经由用户目录 loader 提供的同一路径。`Mq()` 解析 frontmatter 中的 allowed-tools、model、effort、fork context、agent、background、可调用标志等，将技能构造成 prompt 对象；`getPromptForCommand()` 在调用时展开正文、参数和变量。[TE-27–29](evidence/tools-extensions.md)

这支持按“可发现的描述元数据”和“调用时的正文”分层上下文。token 估算模块也区分 always-on 与 on-invoke，但它只作为辅助证据，不能取代实际 loader 的代码证据。完整用户/项目 Skill 的覆盖优先级仍未穷尽。[TE-25](evidence/tools-extensions.md)

### 14.3 Hooks 是生命周期中间件

注册函数 `Q9()` 有 workspace trust 门禁，并用 registration/swap epoch 避免较旧的异步注册覆盖新状态。事件涵盖工具、权限、子 Agent、任务和工作树生命周期。

Hook 结果会被规范化；PreToolUse block 可转为 deny。超时是否阻断取决于事件和 `timeoutFailsClosed` 等条件，不应笼统宣称所有 Hook 失败都放行或都拒绝。[TE-19/20](evidence/tools-extensions.md)

### 14.4 LSP 与 IDE 连接

LSP 工具把用户 1-based 行列转换为协议 0-based 坐标，映射到 definition、references、hover、document/workspace symbols、implementation 与 call hierarchy 请求。LSP 配置可来自 `.lsp.json` 和 manifest，并有 schema 与相对路径检查。[TE-21–23](evidence/tools-extensions.md)

IDE 的连接则有 SSE/WS MCP 路径与 `ide_connected` 通知。LSP 提供代码语义查询，IDE 提供编辑器环境集成，两者有关联但不是同一个组件。[TE-24](evidence/tools-extensions.md)

## 15. 配置、认证与可观测性

### 15.1 配置是带来源与策略的系统

代码区分 user、project、local、flag、policy 等来源。`module-078.js` 包含配置 schema、managed policy 合并约束和仅允许高信任来源设置的字段；`module-110.js` 可见 managed-settings 文件/目录读取、错误记录和不同 layer 的解析缓存。[S13](evidence/source-anchors.md#s13)

这意味着不能把配置实现理解为一次普通对象 merge。例如代码对项目设置放宽上级 sandbox 限制有专门限制。完整优先级和所有字段合并语义未恢复，所以本文只列来源与职责，不编造一个普适的覆盖顺序。

### 15.2 认证与凭证存储

`module-143.js` 定义可读写/删除的 secure-storage 合同，包含 macOS Keychain 访问、缓存、并发读、错误与 generation 处理，也有 plaintext backend 及条件 fallback。具体失败种类会影响是否允许降级，不能将其简写成“Keychain 失败总会写明文”。[S15](evidence/source-anchors.md#s15)

provider factory 再负责把适用的认证解析器、headers 和 endpoint 接入模型客户端。用户实际采用 OAuth、API key、云供应商凭证还是 gateway，本次没有查看，也没有执行认证状态查询。

### 15.3 遥测与成本

`module-043.js` 中可见 nonessential-traffic、DISABLE_TELEMETRY、DO_NOT_TRACK 的判断；`module-1654.js` 中有 OpenTelemetry metrics/logs/traces 与 OTLP export 分支。`module-640.js` 的 `Zfe()` 在某些路径等待 remote managed settings 后初始化遥测，并有只初始化一次及错误处理。[S16–18](evidence/source-anchors.md#s16)

**注意区别**：第三方/企业 OTLP 开关、产品自身事件、诊断日志与成本账本是不同通道。某个开关或 exporter 的存在不能证明当前向某个地址发送数据，更不能仅凭一个条件函数就断言它控制所有网络活动。本次没有抓取运行流量。

## 16. 两条关键业务链路

### 16.1 “读取代码并修改文件”的本地请求

这是依据静态职责重建的流程，不是本次实际执行记录：

```text
输入 prompt
 → 交互界面或 headless 收到输入
 → 会话/设置/可用工具/上下文准备
 → yN → ku/Cu
 → model facts + 必要压缩 + 请求构建
 → 模型响应流出现 tool_use
 → Ls 排队
 → schema / validateInput / Hooks / 权限
 → 工具实际读取或修改
 → tool_result + 上下文更新
 → 再次调用模型或 stop
 → 界面/SDK 输出，并由持久化层记录状态
```

如果是 shell 工具，还可能经过启用的命令沙箱；如果是 MCP 工具，则通过 transport 调外部服务器。文件工具和 shell 工具的执行边界不能混为一谈。

### 16.2 “把工作交给后台子 Agent”

```text
主 Agent 的 tool_use(Agent)
 → Agent 工具校验类型/深度/权限/isolation
 → 建立 agentContext 与 task registry 项
 → 构造子 messages/tools/permissions
 → qR → 父 options.runQuery
 → 独立消费查询事件
 → 完成、取消、后台等待或交付结果
 → 主会话按任务结果继续
```

在已检查的交互/headless 主入口里，runQuery 都绑定 yN。工作树隔离、独立进程和后台任务是不同维度，并非每个后台子 Agent 都自动创建工作树或新进程。

## 17. 架构评估与可借鉴之处

以下是基于重建结果的工程判断，而非 Anthropic 官方设计意图：

| 设计 | 带来的价值 | 需要承担的复杂度 |
|---|---|---|
| 异步生成器 + 显式查询状态 | UI/SDK 消费事件，恢复分支可建模 | 事件顺序、取消和跨轮状态一致性 |
| 工具合同 + 独立并发调度 | 本地/MCP 工具共享入口，区分互斥与并发 | 并发安全提示质量及队列阻塞 |
| 工具权限 + OS 沙箱分层 | 决策与执行约束各自负责 | 不同执行后端的边界覆盖需要明确 |
| prompt snapshot + compact boundary | 提示稳定、历史可恢复、上下文有预算 | 摘要失真、状态重建和快照失效 |
| task registry 与 query 分离 | 前台/后台/子任务共享查询核心 | 归属、取消、结果交付和闲置管理 |
| 插件组合 MCP/LSP/Skill/Hooks | 扩展形态丰富，可统一刷新 | 信任、配置错误、部分加载失败 |
| 版本化单文件分发 | 降低外部 JS runtime 安装依赖 | 包体较大、运行进程与磁盘版本可能不一致 |

对于自建前端 Agent，最直接可迁移的是三点：把查询核心设计成事件生产者；把工具定义与执行/权限/调度分开；把 transcript、输入历史、任务与成本状态作为不同对象管理。没有必要在早期复制所有云、团队或 marketplace 能力。

## 18. 完成度、限制与证据导航

### 18.1 本次问题覆盖

| 调查项 | 结论状态 |
|---|---|
| 本机命令、版本、哈希、格式、签名、依赖 | 已核实 |
| 单文件运行时与 JS 载荷 | 已观察，Bun/JSC 架构高置信重建 |
| 交互 TUI / headless 入口 | 代码与 CLI 契约已对应 |
| Agent 循环、工具反馈、有限恢复 | 核心静态路径已追踪 |
| 模型适配、model facts | 工厂与主要接口已追踪，全部 transport 未穷尽 |
| 工具调度、Hook、权限、沙箱后端 | 局部执行链已追踪，完整安全证明不在范围内 |
| 压缩与提示快照 | 主要实现已追踪，运行质量未测 |
| transcript / storageV5 / 成本状态 | 数据合同与部分读写路径已观察，实际后端未检查 |
| 子 Agent / task / background | 关键路径已追踪，全部专门运行模式未穷尽 |
| MCP / plugins / Skills / LSP / IDE | 主要实现存在已证明，本机启用状态未检查 |
| 模型服务端、真实网络流量、动态行为 | 未分析 |

### 18.2 必须保留的限制

- 没有 Ghidra/Hopper/IDA 原生反编译证据；未还原 Bun/JSC 的原生内部调用图。
- 没有完整 Bun 虚拟文件系统与 source map 重建。分析模块编号不能映射为真实仓库目录。
- 语法可解析不意味着每个模块逐行人工审阅；9 文件 REA 图为局部分析，其他模块采用定点追踪。
- 存在功能开关、用户/企业策略与环境分支。静态存在、CLI 宣告和运行时启用是三个不同结论。
- 未验证真实模型调用、压缩质量、外部工具副作用、权限所有组合、网络发送或账户开关。
- 这是本机 2.1.310、确切哈希的架构快照。后续更新需重新确认文件身份。

### 18.3 证据文件

| 文件 | 用途 |
|---|---|
| [source-anchors.md](evidence/source-anchors.md) | 精选代码片段、合成编号、原二进制精确字节范围 |
| [extraction-manifest.json](evidence/extraction-manifest.json) | 每个提取候选的来源范围与 SHA-256 |
| [macho.json](evidence/macho.json) | REA Mach-O 元数据，Evidence `ev_a2fab99385a995d8dade2e6b0905b08e9c7003bbae988d2b6b4d5b0d774f06bc` |
| [rea-evidence.json](evidence/rea-evidence.json) | REA 完整局部分析，父 Evidence `ev_e0b3e8a03ac1fead74315372008e676f57e494931412f0ff3b1c42bc5e11b0d0` |
| [native.txt](evidence/native.txt) | file / codesign / otool 原始输出 |
| [cli-help.txt](evidence/cli-help.txt) | 当前根命令契约 |
| [cli-subcommands.txt](evidence/cli-subcommands.txt) | 子命令能力与模式契约 |
| [cli-extra-help.txt](evidence/cli-extra-help.txt) | MCP、插件等细化契约 |
| [agent-loop.md](evidence/agent-loop.md) | 核心循环与子任务定点取证笔记 |
| [tools-extensions.md](evidence/tools-extensions.md) | 工具与扩展的 29 条定点证据 |
| [binary-cli.md](evidence/binary-cli.md) | 分发、签名与 CLI 的独立核对 |
| [extract-and-verify.py](evidence/extract-and-verify.py) | 以相同二进制重新提取并验证来源的脚本 |

`Sxx`、`TE-xx`、A/M/C 等是本次调查索引，不是 REA 自动生成的 Evidence ID。补充笔记中的 AST offset 为 JavaScript UTF-16 code unit；工具取证笔记的字符 offset 为 Python Unicode code point。复核优先使用已换算的**原二进制字节半开区间**，不要混用两种字符坐标。
