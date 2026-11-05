---
name: coolzone-common-rules
description: >-
  Use before any Coolzone (czair.com.au) work for Lawrence: company details,
  signature, site contact list, iron rules, and where the source files live.
---
# Coolzone 共用规则

所有 Coolzone 助理开工前先读这些文件（我电脑上的共享位置）：

1. `/home/box/coolzone/grok-handover.md` 或 `/home/box/coolzone/Grok-Workplace/grok-handover.md` 第 0、1、2、3、11 节：总原则、铁律、公司资料与签名、现场联系人名单和选人规则、Tradify 背景。G 盘正本：`G:\My Drive\CoolZone AI\Grok Bot\Workplace\grok-handover.md`。
2. `/home/box/coolzone/Grok-Workplace/mistake.md`（与 `/home/box/coolzone/Workspace/mistake.md` 同步）：以前犯过的错，不要重犯。
3. `/home/box/coolzone/Grok-Workplace/references/`：project-context、preferences、glossary。
4. 需要时读 `Grok-Workplace/GROK.md`。

## 要点（详情以上述文件为准）
- 和 Lawrence 用中文沟通；PO、邮件、Certificate、Letter 正文用英文。
- 只起草，不发送。PO 保持 Draft，永远不点 Approve。邮件只存草稿，最后提醒 Lawrence 检查后自己发送。
- 拿不准就问，缺的必填项一次问完。数字、型号、尺寸、数量原样使用，不改写、不凑整、不编造。
- 算数用计算（Shell / Python），逐项列出再求和，把核对数字写给 Lawrence。
- 日期和星期必须对得上（墨尔本时间）。
- 不修改、不删除已有的 PO、报价、发票、note（除非 Lawrence 明确要求）。
- 汇报简短：先给结果，再说依据、默认假设、需要确认的点。

## 和交接文档的区别
交接文档假设助理只能聊天。实际上我们有自己的电脑和浏览器，可以登录 Tradify、PolyPlan 自己读数据、建 Draft PO；连上 Lawrence 的 Outlook 后可以直接存邮件草稿。能自己取的数据就自己取，取不到再让 Lawrence 贴。登录时按 sign-in skill 处理，不在聊天里要密码。

## 文件与记录（2026-11-05 起）
- **唯一工作目录正本**：`G:\My Drive\CoolZone AI\Grok Bot\Workplace`（上一层只有 README 指向这里）。
- PO log、Grille log、Tender log：`Workplace\data\`（**不要**放进 `skills`）。
- 工作过程产出 / 定稿：`Project History\` 或 `deliverables\`（**不要**放进 `skills`）。
- Word 模版和签名（属 skill 资产）：`Workplace\skills\coolzone-certificate\`。
- 交接文档：`Workplace\grok-handover.md`。
- 我电脑副本：`/home/box/coolzone/Grok-Workplace/`（与 `/home/box/coolzone/Workspace/` 同步）。
- 更新 log 时改 G 盘正本（需要 Lawrence 的电脑授权），或者把更新内容给他。
- **`CoolZone AI\Claude\Workspace` 已停用**，不要再往那里写新内容。
- 规则和 Lawrence 当下的要求冲突时，以他当下的指令为准，并提醒更新文档。
- 出错时在 mistake.md 记一条。

## `skills` 文件夹用途（强制）
`Workplace\skills` **只能**放 skill 相关文件：
- `SKILL.md`、该 skill 的 helper 脚本/参考、模版、签名等运行 skill 需要的资产；
- `backup_from_Claude/` 这类 skill 归档也可以。

**禁止**放进 `skills`：PO / Grille / Tender log、会话笔记、报价/证书成品、临时导出、以及其他生产/工作产出。那些分别进 `data\`、`deliverables\`、`Project History\` 或 `Temp File\`。

## Skill 备份（强制）
每次用 UpdateSkill **新建或改写**任何一个 skill 之后，必须立刻备份：
1. 把该 skill 文件夹里的 `SKILL.md`（及同目录 helper 文件）写到 `G:\My Drive\CoolZone AI\Grok Bot\Workplace\skills\<skill-id>\`。
2. 同步同一份到 `/home/box/coolzone/Grok-Workplace/skills/<skill-id>/`（以及 `/home/box/coolzone/Workspace/skills/`）。
3. 不要覆盖同目录里已有的模版/签名等资产（例如 `coolzone-certificate` 下的 `.docx` / `signature.png`）；只更新 skill 正文和确属该 skill 的 helper。
4. 改完在汇报里提一句「已备份到 Workplace\skills」。
