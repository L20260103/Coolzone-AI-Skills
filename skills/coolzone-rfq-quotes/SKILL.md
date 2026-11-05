---
name: coolzone-rfq-quotes
description: >-
  Use when someone at Coolzone (Jack, Lawrence or Ping) wants to request
  manufacturer quotes (RFQ) for a project, check or update the Tender log and
  due dates, or file supplier quotes that came back.
---
# Coolzone 询价、Tender log 和报价归档

先运行 @coolzone-common-rules，确认当前使用者是谁（Jack / Lawrence / Ping）。

## 规则来源
- 流程 F 询价 + Tender log：`/home/box/coolzone/grok-handover.md` 第 9 节（品牌→收件人表、邮件模板、log 格式）。
- 流程 G 报价归档：第 10 节（什么算厂家报价、G 盘项目文件夹结构、找项目规则、文件规则）。
- 交接文档里的「Lawrence」按当前使用者理解；邮件模板措辞不改，只把签名档换成使用者自己的。
- Tender log 正本：`G:\My Drive\CoolZone AI\Grok Bot\Workplace\data\Tender log.md`；副本 `/home/box/coolzone/Grok-Workplace/data/Tender log.md`（2026-11-05 起新建空表，Claude 侧未找到旧文件）。三个人共用同一份 log。

## 询价步骤
1. 先读 Tender log，把 2 天内到期或已过期的项目用 ⚠️ 放最前面（日期按悉尼时间算）。
2. 从 Mechanical 图纸或 spec 找品牌和型号，没写品牌的风机默认 Fantech 并注明。
3. 先给使用者确认品牌清单和 due date，再起草。
4. 每个品牌一封邮件草稿（存在使用者的 Outlook），模板不改措辞，默认附机械图纸；表里没有收件人的品牌不起草。
5. 更新 Tender log（改 G 盘正本），备注里写是谁发起的询价。

## 归档步骤
1. 在使用者的 Outlook 里找厂家报价邮件（只读，不回复、不转发、不删除）。
2. 按第 10 节规则在 `G:\Other computers\My laptop\Coolzone\1. Projects\` 找项目，唯一匹配才存到 `Quote\<厂家名>\`；多个候选或找不到就问，不新建项目文件夹。
3. 文件名不改，不覆盖。
4. 汇报每封报价的厂家、项目、完整保存路径、金额摘要。
