# Span-Level Debug 是 Agent 工程的分水嶺

- 狀態：WEAK KEEP
- 類型：Heuristic
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Data_Engineering_and_Analytics/Databricks/01_inbox/20260412_MLflow3_AgentEvalMigration_Databricks.md（#5）

## 核心命題
Agent 出錯時，不能只看 trace 整體成敗，必須按 span 拆解 retrieval / generation / tool-call 三層，否則 debug 時間會從十分鐘漲到一下午。

## 卡片內容
診斷 agent 失敗的習慣動作：先看 retrieval span 抓到什麼 context（context 錯，prompt 再好也沒用）；再看 SQL/tool-call span 產出什麼 query（SQL 錯，generation 才是要修的點）；最後看最終 LLM 拿到什麼輸入（輸入對輸出錯，才是 prompt 或模型問題）。這個三層分流直接對應 PySpark 的 stage / task 拆解思維——分散式系統的可觀測性原則被原封不動搬到了 agent 系統。沒有 span-level 觀察的團隊會在「換 prompt → 沒效 → 換模型 → 沒效 → 不知道為什麼」之間死循環。

## 使用情境
- 設計 agent observability 的最小可行 schema
- 為團隊建立 agent debug SOP
- 解釋為什麼「換更強模型」常常解決不了根本問題

## 邊界 / 失效條件
- span 命名與 schema 一致性需要團隊規範
- 對純單輪 LLM call 價值不大

## 上游連結
- [[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]
- Distributed Tracing

## 下游連結
- [[6-001_Trace_Scorer_Labeling_Dataset是同一個閉環]]

## 關聯對照
- [[10-003_Production_Agent失靈是慢性失能而非急性故障]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
