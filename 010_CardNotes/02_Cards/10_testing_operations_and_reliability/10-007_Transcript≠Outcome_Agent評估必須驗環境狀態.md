# Transcript ≠ Outcome — Agent 評估必須驗環境狀態，不能只讀對話

- 狀態：KEEP
- 類型：Principle
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260228_Anthropic_拆解Agent評估的迷霧.md（#1）

## 核心命題
Agent 在 transcript 結尾說「已訂位」不算成功，要去查資料庫裡是否真的有訂單；任何只讀 trace 不查 outcome 的 eval 都會系統性高估 agent。

## 卡片內容
訂機票 agent 可能在最後對話說「我已經幫你訂好」，但資料庫裡根本沒寫進訂單；也可能口頭說「失敗了」但實際結果是對的。Eval 的最小單位必須從「文字輸出」改為「世界狀態變化」。Stripe 的 grader 設計就是直接檢查「實際建立的 Stripe object」，而不是讀 agent 的最終回覆。這個原則對 outcome-based pricing、24/7 自動化判斷權設計、護欄設計都是共同前提：沒有 state-based verification，所有「成果保證」都是空話。

## 使用情境
- 設計 agent eval grader 時的最低標準
- 審查 demo 影片時的批判性提問
- 為 outcome-based 商業模式建立可驗證的成果定義

## 邊界 / 失效條件
- 當 outcome 本身就是文字產出（如報告生成）時需要另一套定義
- 副作用不可回滾的環境（如真錢交易）eval 必須有 sandbox

## 上游連結
- [[3-009_Eval的對象是Stack不是模型本身]]

## 下游連結
- [[兩階段判斷設計_AI自動化的安全模式]]
- [[10-002_Policy_as_Code護欄要在LLM之外執行]]

## 關聯對照
- [[7-005_Outcome-based_Pricing不是趨勢全勝]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
