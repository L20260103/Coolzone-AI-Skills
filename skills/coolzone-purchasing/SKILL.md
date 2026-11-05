---
name: coolzone-purchasing
description: >-
  Use when Lawrence wants to order materials, create a delivery PO, order
  grilles (bar grille / linear slot / WPL), order duct materials from PolyPlan,
  or update PO / Grille logs.
---
# Coolzone 采购：送货 PO、订 Grille、PolyPlan 风管

先运行 @coolzone-common-rules。

## 系统入口（浏览器已登录）
- Tradify：https://go.tradifyhq.com/
- PolyPlan：在 Polyaire Price Book 里，https://www.polyairepricebook.com.au/polyplan （登录页 https://www.polyairepricebook.com.au/login ，登录已存在 vault 里，名称 polyairepricebook.com.au）。编辑器打开是空白 New Plan，用工具栏 Load 找项目；项目链接格式如 `/polyplan?nm=86b-Kooyong-Road-Armadale-Church-Rev-1&tn=43262134`。Pricing 标签是要取的表。只读，不保存、不修改、不删除项目。

## 规则来源
- 流程 A 送货 PO + 供应商邮件：`/home/box/coolzone/grok-handover.md` 第 4 节。更细的 Tradify / Outlook 操作步骤见 `/home/box/coolzone/Grok-Workplace/skills/backup_from_Claude/tradify-delivery-po/SKILL.md` 和它的 `references/staff-contacts.md`（`Workspace/skills/tradify-delivery-po/` 为同步别名）。
- 流程 B 订 Grille：第 5 节。
- 流程 C PolyPlan 订风管材料：第 6 节。
- 记录正本：`G:\My Drive\CoolZone AI\Grok Bot\Workplace\data\PO-log.md`、`Grille_order_Log.md`；副本 `/home/box/coolzone/Grok-Workplace/data/`。

## 步骤
1. 判断是 A / B / C 哪个流程，打开对应章节。
2. 收集必填项（供应商、Job、送货日期），缺的一次问完。能在 Tradify / PolyPlan 自己查的（Job Address、排班、已有 PO、Pricing 表）就用浏览器去查，列表过滤器调到 All。
3. 先查重：已有 PO 里对上任何一项就停下来问。
4. 按规则选地址和现场联系人，写 PO Description。
5. 在 Tradify 建 Draft PO（按固定设置，不点 Approve），在 Outlook 存邮件草稿（不发送）。做不到就把内容给 Lawrence 复制。
6. 逐项列发送前核对：四处 PO 号一致、星期日期、送货方式、联系人电话、地址、Draft 状态。
7. 更新 PO log / Grille log（改 G 盘正本）。
8. 按对应章节的汇报格式汇报，最后提醒 Lawrence 检查后自己发送。
