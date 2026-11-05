---
name: coolzone-common-rules
description: >-
  Use before any Coolzone (czair.com.au) work for Jack, Lawrence or Ping: who is
  using it, company details, signatures, site contact list, iron rules, and
  where the source files live.
---
# Coolzone 共用规则

## 使用者（Jack、Lawrence、Ping 共用）
- 这些 skill 由 Jack Li、Lawrence Lao、Ping 三个人共用。开工前先确认当前是谁在用（看对话里的名字、签名或发件人；看不出来就问一句）。
- 本文和各 Coolzone skill 里的「使用者」就是当前在用的人：缺资料问他，核对清单给他，最后提醒他检查后自己发送。
- 语言：对方用什么语言就用什么语言回。PO、邮件、Certificate、Letter 正文仍然用英文。
- 交接文档 `grok-handover.md` 最初是按 Lawrence 一个人写的。文档里的「Lawrence」一律理解为当前使用者，只有属于 Lawrence 本人的东西除外（他的姓名职位、邮件签名档、签名图片）。
- 邮件签名档和 Letter 签名人都用当前使用者自己的（谁负责就用谁的签名）。还没有他的签名档或签名图片时先问，不要拿别人的代用。
- 签名图片放在 `skills/coolzone-certificate/signatures/<名字>.png`：目前有 `lawrence.png`；`jack.png`、`ping.png` 待补。
- 收件人、发件邮箱和邮件习惯以当前使用者最近一封同类邮件为准；邮件草稿存进他自己的 Outlook。

## 开工前先读（我电脑上的共享位置）
1. `/home/box/coolzone/grok-handover.md` 或 `/home/box/coolzone/Grok-Workplace/grok-handover.md` 第 0、1、2、3、11 节：总原则、铁律、公司资料与签名、现场联系人名单和选人规则、Tradify 背景。G 盘正本：`G:\My Drive\CoolZone AI\Grok Bot\Workplace\grok-handover.md`。
2. `/home/box/coolzone/Grok-Workplace/mistake.md`（与 `/home/box/coolzone/Workspace/mistake.md` 同步）：以前犯过的错，不要重犯。
3. `/home/box/coolzone/Grok-Workplace/references/`：project-context、preferences、glossary。
4. 需要时读 `Grok-Workplace/GROK.md`。

## 要点（详情以上述文件为准）
- 只起草，不发送。PO 保持 Draft，永远不点 Approve。邮件只存草稿，最后提醒使用者检查后自己发送。
- 拿不准就问，缺的必填项一次问完。数字、型号、尺寸、数量原样使用，不改写、不凑整、不编造。
- 算数用计算（Shell / Python），逐项列出再求和，把核对数字写给使用者。
- 日期和星期必须对得上（墨尔本时间）。
- 不修改、不删除已有的 PO、报价、发票、note（除非使用者明确要求）。
- 汇报简短：先给结果，再说依据、默认假设、需要确认的点。

## 和交接文档的区别
交接文档假设助理只能聊天。实际上我们有自己的电脑和浏览器，可以登录 Tradify、PolyPlan 自己读数据、建 Draft PO；连上使用者的 Outlook 后可以直接存邮件草稿。能自己取的数据就自己取，取不到再让使用者贴。登录时按 sign-in skill 处理，不在聊天里要密码。

## 文件与记录（2026-11-05 起）
- **唯一工作目录正本**：`G:\My Drive\CoolZone AI\Grok Bot\Workplace`（上一层只有 README 指向这里）。
- PO log、Grille log、Tender log：`Workplace\data\`（**不要**放进 `skills`）。
- 工作过程产出 / 定稿：`Project History\` 或 `deliverables\`（**不要**放进 `skills`）。
- Word 模版和签名图片（属 skill 资产）：`Workplace\skills\coolzone-certificate\`。
- 交接文档：`Workplace\grok-handover.md`。
- 我电脑副本：`/home/box/coolzone/Grok-Workplace/`（与 `/home/box/coolzone/Workspace/` 同步）。
- 更新 log 时改 G 盘正本（需要使用者的电脑授权），或者把更新内容给他。
- **`CoolZone AI\Claude\Workspace` 已停用**，不要再往那里写新内容。
- 规则和使用者当下的要求冲突时，以他当下的指令为准，并提醒更新文档。
- 出错时在 mistake.md 记一条，写上是谁在用时发生的。

## `skills` 文件夹用途（强制）
`Workplace\skills` **只能**放 skill 相关文件：
- `SKILL.md`、该 skill 的 helper 脚本/参考、模版、签名等运行 skill 需要的资产；
- `backup_from_Claude/` 这类 skill 归档也可以。

**禁止**放进 `skills`：PO / Grille / Tender log、会话笔记、报价/证书成品、临时导出、以及其他生产/工作产出。那些分别进 `data\`、`deliverables\`、`Project History\` 或 `Temp File\`。

## Skill 备份（强制）
每次用 UpdateSkill **新建或改写**任何一个 Coolzone skill 之后：
1. 同步到 `/home/box/coolzone/Grok-Workplace/skills/<skill-id>/`（以及 `/home/box/coolzone/Workspace/skills/`）。
2. 同步到 GitHub 仓库 https://github.com/L20260103/Coolzone-Jack 的 `skills/<skill-id>/`（公开仓库：只放 SKILL.md 和脚本，**不放**签名图片、Word 模版、handover）。
3. 能访问 G 盘时，也写到 `G:\My Drive\CoolZone AI\Grok Bot\Workplace\skills\<skill-id>\`。
4. 不要覆盖同目录里已有的模版/签名等资产；只更新 skill 正文和确属该 skill 的 helper。
5. 改完在汇报里说一句已同步到哪里。
