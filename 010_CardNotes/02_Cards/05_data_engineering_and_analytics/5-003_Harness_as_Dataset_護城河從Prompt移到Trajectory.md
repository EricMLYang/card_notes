# Harness as Dataset — 護城河從 Prompt 移到 Trajectory

- 狀態：WEAK KEEP
- 類型：Pattern
- 分類：5-
- 索引：010_CardNotes/01_Index/05_data_engineering_and_analytics.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260412_AgentHarness2026_PhilSchmid.md（#4+#7）

## 核心命題
當 prompt 與 tool 設計都會被下一代模型抹平，真正能複利的是 harness 在執行過程中捕捉的 trajectory。

## 卡片內容
每一步的決策、tool call、verification、失敗與回補形成結構化 trace，能拿去做 fine-tuning、eval、failure analysis，形成持續放大的回饋迴路。Agent 競爭力從「誰寫得出好 prompt」轉成「誰累積得出高品質軌跡資料集」。Trace 同時讓 multi-step workflow 從黑盒變成可查詢、可標註、可打分的事件。Trace schema 設計需要區分「長期穩定欄位」（事件骨架）與「隨模型演進的欄位」（attribute payload），避免 schema 被模型升級洗掉。

## 使用情境
- 評估 agent 產品的長期 moat 來源
- 設計 trace schema 時的可演進性
- 解釋為什麼「資料工程能力」決定 agent 公司天花板

## 邊界 / 失效條件
- trajectory 作為 moat 需要更多獨立案例支撐
- 當前主要是 Phil Schmid 個人主張

## 上游連結
- [[1-002_Build_to_Delete_Harness必須假設下一代模型會推翻自己]]
- [[Harness 是品味的具體實現]]

## 下游連結
- [[6-001_Trace_Scorer_Labeling_Dataset是同一個閉環]]

## 關聯對照
- [[Distribution（分發）作為 AI 產品護城河]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
