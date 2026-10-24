# Claude Code 2.1.310 本机架构分析

这是一个基于本机实际发行件完成的 Claude Code 2.1.310 架构分析与证据整理项目，覆盖运行时、Agent 主循环、工具系统、权限与沙箱、会话状态、MCP、插件和 Hooks 等部分。

在线阅读：<https://huangzhuangjia.github.io/claude-code-architecture/>

## 项目内容

- `index.html`：可直接访问的静态分析页面
- `Claude-Code-2.1.310-Architecture.md`：Markdown 版本正文
- `evidence/`：CLI 输出、Mach-O 检查结果、提取清单和证据索引

## 说明

- 分析对象是本机 Claude Code 2.1.310 ARM64 发布件。
- 文档区分静态事实、CLI 契约和架构推断。
- 项目中的本机用户名、绝对路径和个人环境标识已做脱敏处理。
- 内容不包含账号凭据、访问令牌或聊天历史。
