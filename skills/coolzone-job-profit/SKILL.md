---
name: coolzone-job-profit
description: >-
  Use when someone at Coolzone (Jack, Lawrence or Ping) names a JB job or site
  and asks about profit, cost, margin, or 利润/成本/毛利.
---
# Coolzone Job 利润计算

先运行 @coolzone-common-rules，确认当前使用者是谁（Jack / Lawrence / Ping）。

## 规则来源
- `/home/box/coolzone/grok-handover.md` 第 8 节（收入、PO 四类、自有人工费率、人×日期工时表、公式、坑、报告格式）。文档里的「Lawrence」按当前使用者理解。
- 完整操作步骤：`/home/box/coolzone/Grok-Workplace/skills/backup_from_Claude/tradify-job-profit/SKILL.md` 和 `references/tradify-ui-map.md`（`Workspace/skills/tradify-job-profit/` 为同步别名）。
- 历史结果：`/home/box/coolzone/Grok-Workplace/Project History/backup_from_Claude/`（JB12468、JB14725、JB15842）。

## 步骤
1. 确认是哪个 Job，有歧义就列候选。
2. 在 Tradify 读取（只读，不保存任何东西）：Quotes、Invoices、Purchase Orders、Bills、Costs、Schedule（每页调到 500）、Time。读不到的让使用者贴。
3. 用 Python 建「人 × 日期」工时表并计算，核对 Time 总和 = Hours、Schedule 行数 = Showing N。
4. 名字不在名单里、分包商分不清就停下来问使用者。
5. 按第 8 节格式出报告（不含 GST），用使用者的语言写，说明各项警告。
6. 最后问使用者要不要 Excel 明细表。

自检参照：JB12468 毛利 7,994.93（22.9%）；JB14725 毛利 3,311.65（6.5%）。
