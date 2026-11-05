---
name: coolzone-certificate
description: >-
  Use when someone at Coolzone (Jack, Lawrence or Ping) asks for a certificate /
  cert / 证书 for a JB job, or a declaration letter for a building surveyor.
---
# Coolzone Certificate 和 Declaration Letter

先运行 @coolzone-common-rules，确认当前使用者是谁（Jack / Lawrence / Ping）。

## 规则来源
- `/home/box/coolzone/grok-handover.md` 第 7 节（格式、通风设备规则、金额来源、核对、Letter 结构）。文档里的「Lawrence」按当前使用者理解。
- 模版和工具（正本）：`G:\My Drive\CoolZone AI\Grok Bot\Workplace\skills\coolzone-certificate\`；副本 `/home/box/coolzone/Grok-Workplace/skills/coolzone-certificate/`（`CZair - Declaration Letter Rev 3.docx`、`fill_letter.py`、`signatures/`）。
- 样板：`.../deliverables/Declaration Letters/JB13647 Declaration Letter.docx` 和 `.pdf`。

## 签名人（谁负责就用谁的签名）
- 先确认这份 Letter 由谁负责签字；默认是当前使用者，不确定就问。
- 签名图片在 `signatures/<名字>.png`：`lawrence.png`（已有），`jack.png`、`ping.png`（待补）。签字人的图片还没有时先问，绝不拿别人的签名代用。
- Rev 3 模版里内嵌的是 Lawrence 的签名和名字。用 `fill_letter.py` 时在 content.json 里同时传 `signer`（签字人全名）和 `signature_image`（他的签名图片路径），脱本会把两者一起换掉。生成后打开检查名字和签名是不是同一个人。
- 签名只用在 Declaration Letter 上。

## 步骤
1. 确认 JB 号和 Commercial / Residential（没给就问，不要猜）。
2. 从 Tradify 取：site 地址、Accepted 报价 Total（含 GST）和 Scope、发票合计、空调 PO、风机厂家发票（Stock Code、MARK、数量）。取不到的让使用者贴。
3. 按第 7 节规则写 certificate，全文放代码块。金额按下面「金额档位」：低于 $750 写精确金额，其余写档位文字。
4. 只在使用者要求时写 Letter：必须有 surveyor 的要求原文，用 Rev 3 模版和 `fill_letter.py` 生成 Word/PDF，签名人按上面「签名人」处理。
5. 逐项核对并汇报每项数据来源、去掉的配件、不一致的地方，以及签字人是谁。提醒 Letter 带签字人的签名，发给 surveyor 前签字人必须自己核对。

## 金额档位（证书里写这一档的文字；低于 $750 写精确金额）
用 Accepted 报价的 Total（含 GST）落档；仍要核对 Subtotal + GST = Total，并和发票合计对照。报价 Total 和发票合计不一致 → 两个数都给使用者，问用哪个，再按他选的数落档或写精确金额。

| 含 GST 金额 | 证书里写 |
|---|---|
| **低于 $750** | **精确金额**，格式 `$123.45`（$、千位逗号、两位小数） |
| $750 – $999 | `$750 - $999` |
| $1,000 – $4,999 | `$1,000 - $4,999` |
| $5,000 – $9,999 | `$5,000 - $9,999` |
| $10,000 – $19,999 | `$10,000 - $19,999` |
| $20,000 – $39,999 | `$20,000 - $39,999` |
| $40,000 – $99,999 | `$40,000 - $99,999` |
| $100,000 及以上 | `Above $100,000` |

- 汇报里仍写出精确 Total（含 / 不含 GST）和落进的档位（或精确金额），方便核对。
