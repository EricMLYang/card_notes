# Stateful Runtime 是企業 AI 新基礎設施單位

- 狀態：KEEP
- 類型：Pattern
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Trend/inbox/20260414_OpenAI營收長Denise的策略方向.md（#3）

## 核心命題
企業 AI 的基礎設施單位正從「API call」演化成「stateful agent runtime」——有狀態、可恢復、可審計、可治理。

## 卡片內容
OpenAI 與 Amazon 推出的 Stateful Runtime Environment 不只是部署通路，而是把產品面從「模型存取」延伸到「長時間、多步驟 agent 的生產級運行時」。對 AWS 上做 AI 工作流的團隊，這定義了下一代基礎設施抽象層——你不再只是在管 API quota，而是在管 agent 的狀態、生命週期、checkpoint、recovery 與 audit log。對 Eric AWS Shared Responsibility 主線，這層新抽象重新切分了「AWS 負責什麼 / 平台負責什麼 / 你負責什麼」的責任邊界。

## 使用情境
- 評估 vs Bedrock Agent / 自建 LangGraph 的取捨
- 設計 long-horizon agent 架構
- 撰寫 AWS 上 agent 治理 SOP

## 邊界 / 失效條件
- 短 horizon、無狀態的 agent 不需要這層抽象
- 自建 stateful runtime 的維運成本可能高於使用平台

## 上游連結
- [[3-002_Frontier飛輪_模型平台工作流的lock-in]]

## 下游連結
- [[兩階段判斷設計_AI自動化的安全模式]]

## 關聯對照
- [[Lakebase 作為 AI Agent 記憶層：sub-10ms 狀態管理 + Database Branching 沙盒]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
