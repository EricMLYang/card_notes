# Agent 速度撞上 legacy backend 的 DDoS 化失敗模式

- 狀態：KEEP
- 類型：Warning
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Trend/inbox/20260412_VerticalAI2026好壞醜_VCCafe.md（#1）

## 核心命題
為人類設計的企業 backend 在 agent 速度下會崩潰——毫秒內 5,000+ 遞迴 sub-task 被 WAF/API gateway 當成 DDoS 攻擊擋下來。

## 卡片內容
這不是模型能力問題，而是「執行頻率假設」的不對齊。Demo 過得了是因為單發呼叫，上線崩潰是因為 agent loop 把 QPS 拉高 3-4 個量級——rate limit、connection pool、auth flow、audit log 全部都是基於人類速度設計的。對「demo 到 production」最具體、最可驗證的失敗模式之一。緩解策略需在 agent 端設計 rate-aware behavior、async queue、bulkhead pattern、token bucket，並在 infrastructure 端與 SRE/Security 對齊放行規則（合法 agent traffic vs 真實攻擊的辨識）。

## 使用情境
- 寫 AI 上線責任 SOP
- 設計 agent harness
- 與客戶 SRE/Security 對齊 agent 部署
- 做 production readiness review

## 邊界 / 失效條件
- 低頻 agent（每天幾次）不會撞到此問題
- 新建內部系統可從第一天就用 agent-native 設計繞開

## 上游連結
- AWS Shared Responsibility

## 下游連結
- [[Agent 產品 95% 在 Production 失敗的原因]]
- [[兩階段判斷設計_AI自動化的安全模式]]

## 關聯對照
- [[10-011_Production_Agent失靈是慢性失能而非急性故障]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
