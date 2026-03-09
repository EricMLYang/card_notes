# 6-Lakebase 作為 AI Agent 記憶層：sub-10ms 狀態管理 + Database Branching 沙盒

**類型**：Pattern

## 概念

在 Intent HQ 架構中，Lakebase（Databricks 受管無伺服器 PostgreSQL）扮演「代理人作業系統」角色：(1) 持久化狀態管理——sub-10ms 讀寫效能，儲存對話上下文、LangGraph checkpointer 狀態、中間推理步驟；(2) Database Branching——瞬時創建資料庫分支讓代理人在隔離環境沙盒測試，不影響生產環境；(3) OLTP/OLAP 統一——交易型數據近乎實時與 Delta Lake 同步，消除 ETL 管道。這揭示了 Agent 系統一個被低估的需求：Agent 若缺乏記憶會導致行為斷裂，持久化狀態管理不是可選項而是必要基礎設施。

## 重要性

為 Agent 系統設計者提供「記憶層」的參考架構——不只是 KV cache，而是有分支、有隔離、有 OLTP/OLAP 統一的完整狀態管理。

## 邊界/反例

Lakebase 目前綁定 Databricks 生態，非 Databricks 用戶需要自行組合 PostgreSQL + CDC + 分支機制。記憶層的延遲要求取決於 Agent 類型——批次分析型 Agent 對 sub-10ms 不敏感。

## 標籤

#Lakebase #Databricks #Agent記憶層 #狀態管理 #DatabaseBranching
