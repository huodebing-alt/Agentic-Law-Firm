---
name: china-index
description: Index pointer for the CN agent namespace. Not directly invoked. CN-specific specialist agents live at .claude/agents/<area>/ (corporate, contracts, compliance, ip, disputes, tax, labor, real-estate, individual, research) as the default fast-path access. This file exists so cross-jurisdiction routing in task-router can refer to a china/ namespace symmetrical with singapore/ and us/.
tools: Read
model: inherit
---

# China agents (index)

CN-specific specialist agents are at `.claude/agents/<area>/` (corporate,
contracts, compliance, ip, disputes, tax, labor, real-estate, individual,
research) as the default fast-path access. These were authored against
PRC law (民法典, 公司法, 反垄断法, 数据安全法, 个人信息保护法, etc.).

This directory exists as a logical anchor so cross-jurisdiction routing
in `task-router` can refer to a `china/` namespace symmetrical with
`singapore/` and `us/`.

## When invoked
This index agent is not directly invoked. `task-router` consults this
namespace to resolve CN-jurisdiction routes.

Chinese-language triggers:
不直接调用

English-language triggers:
not directly invoked

## Process
1. Not directly invoked

## Output
None.

## Hard gates
None.

## MCP dependencies
None.

## Notes
Index only.
