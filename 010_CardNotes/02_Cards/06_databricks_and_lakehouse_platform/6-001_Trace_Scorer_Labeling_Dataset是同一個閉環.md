# Trace + Scorer + Labeling + Dataset 是同一個閉環 — Bronze/Silver/Gold 思維遷移到 Agent Eval

- 狀態：KEEP
- 類型：Pattern
- 分類：6-
- 索引：010_CardNotes/01_Index/06_databricks_and_lakehouse_platform.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Data_Engineering_and_Analytics/Databricks/01_inbox/20260412_MLflow3_AgentEvalMigration_Databricks.md（#3+#4，合併）

## 核心命題
Agent eval 的資料層次可直接套用 Medallion 架構：production traces 是 Bronze、human labeling 是 Silver、curated golden dataset 是 Gold；當這三層共用同一個 trace 資料模型，agent 品質就會複利成長。

## 卡片內容
MLflow 3 把 evaluation 結果存成 trace + assessment，意味 production trace 與 eval trace 共用資料模型，同一組 scorer 可同時跑離線 golden set 與線上抽樣。Production 發現的 bad case 可以一鍵變 golden case：觀察 → 標記 → 寫回 dataset → regression test 自動跑。這個閉環打破了過去「observability 與 evaluation 是兩套工具兩種 schema」的隔閡，也讓每個使用者 bug 都在訓練系統。對熟悉 lakehouse 的工程師，Bronze/Silver/Gold 類比能極快遷移認知——你已經知道資料品質如何分層治理，agent eval 只是另一條 medallion pipeline。

## 使用情境
- 為 agent 產品設計 evaluation 基礎設施時的資料模型決策
- 說服資料團隊把 agent eval 納入既有 lakehouse 治理範圍
- 建立 production bad case → regression suite 的回流機制

## 邊界 / 失效條件
- trace 儲存成本可能比預期高需設計抽樣策略
- 跨團隊共用 dataset 需要明確權限模型
- 此類比在 platform 沒有 trace-based 統一資料模型時失效

## 上游連結
- [[AI Error Analysis：LLM 應用評估方法]]
- Medallion Architecture

## 下游連結
- [[DecisionOps]]
- [[Lakebase 作為 AI Agent 記憶層：sub-10ms 狀態管理 + Database Branching 沙盒]]

## 關聯對照
- [[5-003_Harness_as_Dataset_護城河從Prompt移到Trajectory]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
