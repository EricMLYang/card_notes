# Eval 的對象是 Stack（Model + Harness + Tools + Environment），不是模型本身

- 狀態：KEEP
- 類型：Principle
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260407_Stripe用真實Benchmark測AI整合能力.md（#1）

## 核心命題
當你說「我們在評估某個模型」，你其實在評估「模型 + agent harness + tools + environment」整個 stack；不講邊界的 eval 報告會誤導所有後續決策。

## 卡片內容
Stripe 為了測 AI 的 payments 整合能力，建了 11 個 production-realistic 環境，每個都包含三件套：environment（含 code/db/script/test API key）、graders（含 deterministic test、API call、UI automation、Stripe object 檢查）、agent harness（terminal + browser + Stripe docs MCP）。Anthropic 也明確區分 evaluation harness 與 agent harness，並指出同一個模型換 scaffold，CORE-Bench 分數可從 42% 跳到 95%。Eval 邊界沒講清楚時，benchmark 排名容易誤判模型能力，團隊會把 harness 缺陷錯誤歸因給模型，或把模型強度當成 production 可用度。

## 使用情境
- 讀任何 benchmark 排名前先問「他評的 stack 是什麼」
- 內部 agent 表現不佳時先做 ablation
- 對外溝通評估結果時明示 stack 邊界

## 邊界 / 失效條件
- 若 stack 各層耦合很深，ablation 設計本身有難度
- 標準化 harness 可能掩蓋 harness 本身的 bug

## 上游連結
- [[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]
- [[Harness 是品味的具體實現]]

## 下游連結
- [[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]]
- [[Agent 產品 95% 在 Production 失敗的原因]]

## 關聯對照
- [[3-006_Harness六層構成_Agent系統工程的解構]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
