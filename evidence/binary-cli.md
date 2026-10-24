# Claude Code 2.1.310：本机二进制、CLI 与分发架构调查

调查日期：2026-10-24（Asia/Shanghai）。只读取已安装发布件和执行 `--help` / `--version`；未执行模型请求、安装、更新、认证、MCP 连接、插件加载或后台会话枚举。未读取用户凭证、对话历史或设置值。

## 1. 证据目录与身份

- E-CLI-01 `/tmp/claude-help.txt`：根命令帮助，父调查预先取得，本文复用。
- E-CLI-02 `/tmp/claude-cli-subcommands.txt`：本次取得的 version 与子命令帮助。
- E-NATIVE-01 `/tmp/claude-native-evidence.txt`：完整 hash、file、codesign、otool 输出。
- E-CLI-03 `/tmp/claude-cli-extra-help.txt`：MCP serve/add、插件 marketplace/install、auth login、respawn/import 帮助。
- `/tmp/claude-macho.json` 为父调查的 REA Mach-O 结果，本文未依赖其内部结果。

实际目标：`/Users/huangzhuangjia/.local/share/claude/versions/2.1.310`。
入口 `/Users/huangzhuangjia/.local/bin/claude` 是指向上述版本路径的 symlink。文件大小 274,068,224 字节（约 261.37 MiB）；SHA-256 `ffb64331bc0ee1b69efb7c2c428bd3ab516bc31b75bf60886b356c97c1c25ffd`。执行此文件 `--version` 输出 `2.1.310 (Claude Code)`。

**事实**：这里的当前入口采用 native build + 版本化本地目录的布局。**推断**：入口与版本文件分离能支持切换版本和保留旧版本；没有执行 updater，也没有证明其切换操作是否原子、保留多少版本。不能因此断言此机器没有其他 npm 安装。

## 2. 原生载体与嵌入运行时

E-NATIVE-01 第 4–7 行：`file` 为 `Mach-O 64-bit executable arm64`，为 thin arm64 架构，非 universal fat binary。

E-NATIVE-01 第 63 行起的 Mach-O load commands：

- `__TEXT` 约 91 MB，含 `__text`、`__jsc_int`、`__bun_builtins`。
- `__DATA` 包含 `__jsc_opcodes`、`__wtf_config`。
- 存在 `__BUN` segment / `__bun` section。
- `LC_BUILD_VERSION` 标示 `minos 13.0`、`sdk 26.5`。
- `LC_MAIN entryoff 18842024`；UUID `4C4C44E9-5555-3144-A1AF-15A99BC1C6A9`。

**强推断**：此文件封装 Bun 运行时以及 JavaScriptCore 解释器/引擎，并把应用载荷放入本地执行文件。Mach-O 不是“全部业务逻辑改写成原生代码”的证据；更符合原生运行时 + 嵌入 JavaScript 的分发架构。section 名称本身不提供应用业务调用图，具体 Bun 版本与业务代码边界需结合字符串或解包证据。

E-NATIVE-01 第 54–60 行：`otool -L` 仅列 4 个动态依赖：

| 依赖 | 本机记录版本 | 可支持的解释 |
|---|---|---|
| `/usr/lib/libicucore.A.dylib` | 78.1.0 | ICU 系统库导入，不能据此证明具体国际化业务路径 |
| `/usr/lib/libresolv.9.dylib` | 1.0.0 | 系统名称解析库导入 |
| `/usr/lib/libc++.1.dylib` | 2100.43.0 | C++ 运行库导入 |
| `/usr/lib/libSystem.B.dylib` | 1356.0.0 | 系统基础 API 导入 |

**事实**：动态依赖表没有外置 Node/Bun/JSC dylib；**推断**：这些运行时能力随可执行文件静态或嵌入交付，而非要求用户额外启动 Node。动态依赖表不枚举程序运行时 dlopen 的库，不能断言以上是全部依赖。

## 3. 签名与执行权限

E-NATIVE-01 第 9–45 行：

- Identifier `com.anthropic.claude-code`。
- 签名链 `Developer ID Application: Anthropic PBC (Q6L2SF6YDW)` → Developer ID Certification Authority → Apple Root CA。
- TeamIdentifier `Q6L2SF6YDW`。
- `flags=0x10000(runtime)`，hardened runtime；Runtime Version 26.5.0。
- 本机签名时间显示 2026-10-24 03:39:19（工具未标出时区，本文不换算）。
- `codesign --verify --strict --verbose=2` 退出 0，输出 `valid on disk`、`satisfies its Designated Requirement`。

E-NATIVE-01 第 47–51 行的 entitlement：

| entitlement | 值 | 解释边界 |
|---|---|---|
| `com.apple.security.cs.allow-jit` | true | 允许 JIT，符合嵌入 JS 引擎需求；不是特定 JIT 路径执行证明 |
| `com.apple.security.cs.allow-unsigned-executable-memory` | true | 允许未签名可执行内存 |
| `com.apple.security.cs.disable-library-validation` | true | 放宽加载库验证 |
| `com.apple.security.automation.apple-events` | true | 具备申请自动化能力的签名声明，非用户已授权证明 |
| `com.apple.security.device.audio-input` | true | 具备申请音频输入能力的签名声明，非麦克风已授权或正在录音证明 |

签名验证仅证明该文件本机签名有效、满足 designated requirement；未执行 Gatekeeper/notarization 在线验证。hardened runtime 与上述 entitlement 例外应同时描述。

## 4. CLI 分层与外部控制面

### 4.1 人机交互与 SDK/流水线输入

E-CLI-01 第 1–4、123–150 行：默认交互模式；`-p/--print` 非交互模式；输入 text 或 stream-json；输出 text/json/stream-json。`--include-partial-messages` 输出增量块；`--replay-user-messages` 回显输入确认；`--forward-subagent-text` 为转发文本标记 parent_tool_use_id；`--include-hook-events` 输出 Hook 生命周期事件。

**架构含义（推断）**：同一代理核心外接 TTY 界面与机器协议适配器；stream-json 是 SDK/宿主进程可观测和控制代理的重要边界。仅凭帮助未验证每种事件的完整 JSON schema、错误码和 backpressure。

### 4.2 运行策略与请求编排

E-CLI-01：`--model`、`--effort`、`--fallback-model`；`--max-budget-usd`（print only）；`--json-schema`（结构化输出）；`--autocompact`；`--system-prompt`、`--append-system-prompt`、`--exclude-dynamic-system-prompt-sections`。

`--system-prompt-snapshot on|off` 的帮助（233 行起）直接描述：默认在对话首次请求渲染并记录系统提示，后续请求与恢复复用，直到 compact；off 则每请求重渲染。这是本版本上下文/缓存策略的明确公开契约，仍未运行验证。

### 4.3 会话持久化与进程生命周期

E-CLI-01 第 33–40 行及命令表：`--background` 返回可供 attach/logs/stop/rm 使用的 id；agents 列表；resume/continue/fork-session/session-id；`--no-session-persistence` 仅 print；worktree/tmux。`respawn --help` 明确重启背景会话以使用当前 Claude binary。

**推断**：会话身份、对话持久化、后台进程和工作树是不同的生命周期对象；stop 保留 conversation，rm 在安全时还移除 worktree；respawn 将长寿命代理与磁盘上的版本更新衔接。未查询真实会话或验证进程管理实现（daemon/IPC/锁协议未知）。

### 4.4 本地、云、桌面和远程入口

E-CLI-01：`--cloud` 创建或附着云会话；`--environment` 指定 self-hosted 环境；`--remote-control` 为交互会话启用 Remote Control；`--desktop` 在 Claude Desktop 打开；`--ide` 自动连接唯一可用 IDE；`--chrome` 浏览器集成。E-CLI-02 226 行起 ultrareview 为 cloud-hosted multi-agent review；gateway 子命令描述为 enterprise auth/telemetry gateway。

**事实**：CLI 声明这些入口与集成；**未知**：握手协议、网络拓扑、服务端实现、云模型路径、此机器是否启用/登录这些能力。不能把这些帮助项画成已经运行的组件。

## 5. 扩展机制

### 5.1 MCP 双角色

E-CLI-02 第 5–51 行：MCP client 配置能力，add/add-json 支持 stdio、SSE、HTTP，add-json 还描述 WebSocket；login/logout 供 OAuth；project .mcp.json 未批准不连接。`mcp serve` 则公开 Claude Code MCP server 入口。

E-CLI-03 第 12 行起：MCP add 提供 local/user/project scope、环境变量、headers、OAuth client id/secret 和 callback-port；默认 stdio。注意 `mcp add --transport` 本身只列 stdio/sse/http，不能把 add-json 的 WebSocket 扩展误写为所有入口均支持。

**推断**：代理既可消费工具服务器，也可被上游 MCP client 调用。服务端实际提供哪些 tool 与资源，未启动 serve，保持未知。

### 5.2 Plugin/Marketplace/Skills

E-CLI-02 第 54–111 行：plugin install/list/enable/disable/update/validate；marketplace；details 提供组件清单和 projected token cost；init 默认 scaffold 至 ~/.claude/skills/name；eval 提供 plugin 与 baseline 对照评估并可选择真实 MCP。E-CLI-01 plugin-dir 支持 directory/zip，plugin-url 可抓取临时 zip。

E-CLI-03 插件 install 的公开帮助进一步显示：user/project/local scopes；userConfig schema 验证；.mcpb 包含自身 user_config；marketplace 可来自 repo/git/https/path，npm registry 可指定；marketplace-declared command/headersHelper 安装需确认，可通过绑定 command/plugin/catalog 的 sha256 明确接受。

**推断**：插件系统不只是 prompt 文件加载器，具有来源、安装策略、manifest/schema、配置、依赖清理、运行组件和评估面。实际 plugin runtime 调用和具体模块依赖由其他代码证据确定。

## 6. 安全/配置边界：三种模式不是同义词

| 模式 | 帮助所声明行为 | 不能据此声称 |
|---|---|---|
| `--bare` | 跳过 hooks、LSP、plugin sync、attribution、auto-memory、background prefetch、keychain、CLAUDE.md auto discovery；设置 CLAUDE_CODE_SIMPLE=1；Anthropic 认证仅 key/apiKeyHelper，skills 仍可显式解析 | 完全无扩展、无认证或无网络 |
| `--safe-mode` | 关闭 CLAUDE.md/skills/已装 plugins/hooks/MCP/custom agents/commands 等定制；保留 admin managed policy；auth/model/built-in tools and plugins/permissions 正常 | 操作系统沙箱或禁止命令执行 |
| `--restricted` | 默认移除代码执行工具与 WebFetch；忽略 user/project/local settings（managed 和显式 settings 仍适用）；文件工具限制于 workdirs；拒绝 bypassPermissions；敏感配置写入须人或 handler 批准 | 总是关闭所有 MCP（需另加 strict-mcp-config）或完整 OS 隔离 |

E-CLI-01 151–160 行：permission modes 为 acceptEdits/auto/bypassPermissions/manual/dontAsk/plan；print 的 permission prompts 可交 SDK host 或 none（自动拒绝会询问的操作）；allowed/disallowedTools 和 add-dir 提供细粒度控制。auto-mode 子命令声明 classifier config/default/reset/critique；未执行 AI critique。

配置来源有 user/project/local、managed policy、显式 settings、MCP config、agents、plugin-dir。帮助未建立完整配置优先级，切勿仅凭列表推导覆盖顺序。

## 7. 安装与更新层

`claude install [target]` 明确支持 stable/latest/固定版本 native build，--force。`update|upgrade` 检查更新并安装，package-manager 安装由 package manager 更新（E-CLI-02 第 171–189 行）。本机 symlink/version 文件布局与 native build 相符。未执行以上动作，因此下载源、版本清单、签名验证时机、差分下载、回滚策略及自动更新调度未知。

## 8. 实际执行过的命令

```sh
ls -l /Users/huangzhuangjia/.local/share/claude/versions/2.1.310 /Users/huangzhuangjia/.local/bin/claude /tmp/claude-help.txt /tmp/claude-macho.json
file /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
codesign -dv --verbose=4 /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
codesign --verify --strict --verbose=2 /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
codesign -d --entitlements :- /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
otool -L /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
otool -l /Users/huangzhuangjia/.local/share/claude/versions/2.1.310
```

Python `hashlib.sha256(Path(target).read_bytes()).hexdigest()` 与 `Path.stat()` 取得身份和大小。

以下均调用目标绝对路径，不依赖 PATH 的其他版本：

```text
--version
mcp --help
plugin --help
agents --help
gateway --help
install --help
update --help
auth --help
auto-mode --help
ultrareview --help
mcp serve --help
mcp add --help
plugin marketplace --help
plugin install --help
auth login --help
respawn --help
import --help
```

## 9. 明确保留的未知

1. 本次无 native decompiler：Mach-O/JSC 的内部 native 函数调用图与内存实现未知。
2. CLI 帮助为当前发布件的公开契约，不等于所有功能在该用户账户/开关/环境下可用，更不等于已观测执行。
3. 未做真实推理调用，工具调度/权限交互/SDK stream event 的动态顺序未知。
4. 未连接云、IDE、browser、MCP 或 gateway，网络服务拓扑、服务端状态与协议版本未知。
5. 未读取 auth/settings/transcript，文档不能声称该机器的账户、供应商、MCP 实例、插件配置或历史会话状态。
6. 签名/entitlements 仅静态事实，无 notarization/TCC 当前授权与动态加载验证。
