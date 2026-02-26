# Intent HQ x Verizon：從 2.5 兆列數據到 1.8 億美元增量營收

> 來源：Intent HQ 研究報告
> 案例：Databricks 數據智慧平台在極端規模數據環境下的落地標竿

## 專案概述

希望您分享這份針對 Intent HQ 的最新研究報告。這份報告詳述了他們如何協助 Verizon 在處理超過 2.5 兆列 原始數據的極限挑戰下，實現了 1.8 億美元 的預期增量營收。

這份報告將為您的團隊提供以下核心洞察：
- **營收增長實證**：Verizon 如何透過 Audience AI 代理人實現 51% 的行銷轉換率提升。
- **精準流失預測**：如何將流失預警準確度提升 3.5%，並直接轉化為長期財務回報。
- **Lakebase (Serverless PostgreSQL)**：深入了解這項 Databricks 原生服務如何作為 AI 代理人的「持久化記憶層」，消除傳統 ETL 的複雜度。
- **Built on Databricks**：解析一套通過官方認證、符合電信級隱私與安全要求的複合 AI 架構。

這份文件展示了 Intent HQ 如何在不離開數據安全環境的前提下，賦予非技術人員直接驅動商業結果的能力。

---

## Slide 1: Verizon 專案實踐：從兆級數據到 1.8 億美元增量價值的商業賦能

Intent HQ 與美國電信巨頭 Verizon 的合作，是 Databricks 數據智慧平台在極端規模數據環境下落地的標竿案例。透過將行為 AI 能力與 Databricks 的運算架構整合，Verizon 成功解決了海量行為數據難以變現的瓶頸。

### 極限規模下的數據處理與隱私合規

Verizon 的數據環境具備極高的複雜度，其原始網頁瀏覽數據（Web browsing data）規模超過 **2.5 兆列**。

**隱私安全處理**：系統在 Verizon 的防火牆後方部署了混合處理器（Hybrid Processor），對兆級原始敏感數據進行預處理。

**數據精煉**：2.5 兆列的原始數據被精煉為 **900 億列** 的去識別化特徵，隨後才進入 Intent HQ 平台進行建模。這確保了 PII（個人識別資訊）絕不離開 Verizon 的安全邊界。

### 預測性 AI 的精準化：流失預警的重大突破

Verizon 擁有累積超過 20 年的流失預測模型，但在導入 Intent HQ 的行為特徵後，性能獲得顯著提升：

- **精準度提升**：在最關鍵的「最高風險群」（Highest-risk decile）中，流失預測準確度提升了 **3.5%**。
- **整體優化**：在前 30%（Top 3 deciles）的高風險群中，準確度平均提升 **2.1%**。
- **財務回報**：這項準確度的提升預計在五年內為 Verizon 創造高達 **1.8 億美元** 的增量價值。

### 行銷代理人的商業回報：Audience AI

Verizon 利用 Intent HQ 的 Audience AI 功能，讓行銷團隊能直接從行為、興趣與事件數據中提取洞察：

- **行銷轉換率 (Take Rate)**：相較於傳統目標投放策略，Audience AI 實現了 **51% 的轉換率增長**。
- **單次活動成效**：以 Verizon Protect 專案為例，單次行銷活動即產生了約 **37.8 萬美元** 的增量營收。
- **效率革命**：行銷人員無需等待數據團隊支援，即可自主建立受眾，將開發週期從數週縮短至幾分鐘。

---

## Slide 2: 電信級數據智慧架構：Intent HQ 與 Databricks Mosaic AI 整合技術深度分析

### 1. 企業 AI 轉型的核心範式：從單一模型到複合 AI 系統

Intent HQ 在 Databricks 上的實踐代表了從單一大型語言模型 (LLM) 向 **複合 AI 系統 (Compound AI Systems)** 的轉向。

這種架構不再僅依賴通用的預訓練智慧，而是透過整合多個專門的代理人 (Agents)、檢索器與工具，讓 AI 系統能深刻理解企業數據的語義，解決傳統 AI 面對特定業務邏輯時的「幻覺」與背景知識缺失問題。

### 2. IntentOne：基於 Mosaic AI 的代理人框架 (Agentic Framework)

Intent HQ 開發的 IntentOne 是一套高度自主的代理人系統，其底層完全架構在 Mosaic AI Agent Framework 之上。

**自主決策與執行**：IntentOne 代理人能根據人類設定的行銷目標，自主拆解任務步驟、調用工具並生成執行計畫。

**競爭優化機制**：系統會生成多個「競爭代理人」來測試不同的行銷變體，透過實時的客戶反饋數據，自動篩選出表現最優的策略並進行動態調整。

**工具調用 (Tool Calling)**：透過 Unity Catalog 註冊的 Python 函數與 SQL 命令，代理人能直接操作內部的客戶數據庫或調用外部 API，實現端到端的自動化流程。

### 3. Lakebase：代理人系統的無伺服器 PostgreSQL 記憶層

在 Intent HQ 的架構中，**Lakebase** 扮演著關鍵的「代理人作業系統」角色。它是 Databricks 提供的受管無伺服器 PostgreSQL 資料庫服務。

**持久化狀態管理 (Stateful Memory)**：AI 代理人若缺乏記憶將導致行為斷裂。Lakebase 提供亞秒級 (sub-10ms) 的讀寫效能，用於儲存代理人的對話上下文、工作流狀態 (如 LangGraph checkpointer) 與中間推理步驟。

**資料庫分支與實驗 (Database Branching)**：Lakebase 支持瞬時創建資料庫分支，讓代理人能在隔離的環境中進行沙盒測試與策略驗證，而不會影響生產環境的數據一致性。

**OLTP 與 OLAP 的統一**：透過與 Lakehouse 的原生整合，Lakebase 中的交易型數據 (OLTP) 能近乎實時地與 Delta Lake (OLAP) 同步，消除了複雜的 ETL 管道與數據移動成本。

---

## Slide 3: 技術架構深度解析

### 4. 數據攝入與邊際智慧：Intent Edge 與 Delta Sharing

針對電信級的數據規模，Intent HQ 採用了雲端與邊際 (Edge) 協同的策略：

**Intent Edge SDK**：在移動端設備上進行隱私安全的信號處理，每日為每位用戶生成超過 500 個行為洞察，且所有個人識別資訊 (PII) 均不出設備。

**Delta Sharing 整合**：經過去識別化後的邊際數據，透過 Delta Sharing 安全地同步到 Databricks 空間中。

**數據壓縮與佈局優化**：Verizon 案例中，原始 2.5 兆列的網頁瀏覽數據被精煉為 900 億列的去識別化特徵，並透過 Delta Table 的 Z-Ordering 優化實現極致查詢性能。

### 5. 統一治理與安全性：Unity Catalog 與 Mosaic AI Gateway

在高度受管制的電信業，安全性是不可逾越的紅線。

**Unity Catalog**：作為唯一的治理層，管理數據、模型、向量索引與 AI 代理。這確保了從數據源到 AI 回覆的完整血緣追蹤 (Data Lineage)。

**Mosaic AI Gateway**：作為企業應用與 LLM (如 Claude, ChatGPT) 之間的智慧閘口，提供 PII 偵測、速率限制與安全護欄，確保敏感數據在模型調用過程中不外洩。

### 6. 評估驅動開發 (EDD)：確保生產環境品質

Intent HQ 利用 Mosaic AI Agent Evaluation 與 MLflow 3.0 建立持續改進的閉環：

**AI Judges 與人類回饋**：利用高性能模型作為裁判，根據自然語言準則評估代理人的輸出品質；同時透過 Review App 讓業務專家參與標註與修正。

**自定義指標**：定義與業務掛鉤的指標（如轉換率預測準確度、成本消耗），透過自動化評估集確保模型更新不發生回歸 (Regression)。

### 7. 商業價值實證：Verizon 轉型成效

| 技術組件 | 解決問題 | 業務結果指標 |
|---------|---------|-------------|
| Audience AI (代理人) | 自主精準分群，無需人工干預 | 51% 轉換率提升 (Take Rate) |
| Mosaic AI 預測建模 | 利用行為特徵優化流失預警 | 最高風險群流失預測準確度提升 3.5% |
| Databricks 統一平台 | 基礎設施成本優化與維運自動化 | 5 年預估增量營收 1.8 億美元 |

---

## 待萃取重點

- [ ] 極限規模數據處理：2.5 兆列 → 900 億列去識別化特徵
- [ ] 流失預測準確度提升 3.5%（最高風險群），5 年創造 1.8 億美元價值
- [ ] Audience AI 代理人：51% 轉換率提升，開發週期從數週縮短至分鐘
- [ ] 複合 AI 系統：從單一 LLM 到多代理人協同
- [ ] IntentOne 代理人框架：自主決策、競爭優化機制、工具調用
- [ ] Lakebase：AI 代理人的無伺服器 PostgreSQL 記憶層（sub-10ms、Database Branching）
- [ ] OLTP 與 OLAP 統一：消除 ETL 複雜度
- [ ] Intent Edge SDK：設備端隱私安全處理（每日 500+ 行為洞察）
- [ ] Unity Catalog 統一治理：完整數據血緣追蹤
- [ ] Mosaic AI Gateway：PII 偵測與安全護欄
- [ ] 評估驅動開發（EDD）：AI Judges + 人類回饋閉環
- [ ] 電信級部署模式：混合處理器在防火牆後處理敏感數據

---

# 拆解結果

## A. 主脈絡與個人映射
- **論證骨架**：從 Verizon 兆級數據處理的規模挑戰 → 數據精煉（2.5 兆 → 900 億列）→ 預測 AI 提升（流失預測 +3.5%）→ 行銷 AI 代理人（轉換率 +51%）→ 底層技術棧（Mosaic AI + Lakebase + Unity Catalog），論證 Databricks 平台上的 Compound AI System 如何在電信級場景落地並產生可量化商業價值。
- **個人映射**：對 Databricks 生態的系統建造者而言，核心價值是看到完整的「數據 → AI → 商業價值」閉環實證，特別是 Lakebase 作為 Agent 記憶層和 EDD 品質閉環的設計。

## B. 卡片（Zettel）

序號 1
- 標題：Lakebase 作為 AI Agent 記憶層：sub-10ms 狀態管理 + Database Branching 沙盒
- 類型：Pattern
- 概念（50–300 字）：在 Intent HQ 架構中，Lakebase（Databricks 受管無伺服器 PostgreSQL）扮演「代理人作業系統」角色：(1) 持久化狀態管理——sub-10ms 讀寫效能，儲存對話上下文、LangGraph checkpointer 狀態、中間推理步驟；(2) Database Branching——瞬時創建資料庫分支讓代理人在隔離環境沙盒測試，不影響生產環境；(3) OLTP/OLAP 統一——交易型數據近乎實時與 Delta Lake 同步，消除 ETL 管道。這揭示了 Agent 系統一個被低估的需求：Agent 若缺乏記憶會導致行為斷裂，持久化狀態管理不是可選項而是必要基礎設施。
- 重要性（1 句）：為 Agent 系統設計者提供「記憶層」的參考架構——不只是 KV cache，而是有分支、有隔離、有 OLTP/OLAP 統一的完整狀態管理。
- 邊界/反例（1–2 句）：Lakebase 目前綁定 Databricks 生態，非 Databricks 用戶需要自行組合 PostgreSQL + CDC + 分支機制。記憶層的延遲要求取決於 Agent 類型——批次分析型 Agent 對 sub-10ms 不敏感。
- 知識鉤子：可作為 #CPU成為Agent指令層 的狀態管理補充——CPU 做編排，Lakebase 做狀態持久化；與 #Agent架構做空檢驗 中的 thin harness 形成對比——這是「必要的 harness」而非「過度設計的腳手架」。

序號 2
- 標題：評估驅動開發（EDD）：AI Judges + 業務指標防止 Agent 品質回歸
- 類型：Heuristic
- 概念（50–300 字）：Intent HQ 利用 Mosaic AI Agent Evaluation + MLflow 3.0 建立持續改進閉環：(1) AI Judges——用高性能模型根據自然語言準則評估 Agent 輸出品質；(2) 人類回饋——透過 Review App 讓業務專家參與標註修正；(3) 自定義業務指標——定義轉換率預測準確度、成本消耗等與業務掛鉤的指標，透過自動化評估集確保模型更新不發生回歸。核心邏輯：Agent 不是部署上去就完了，你需要一個能持續驗證「Agent 在業務指標上沒有退步」的品質閉環。
- 重要性（1 句）：為 Agent 產品化提供品質保證方法論——不是測 prompt 好不好，而是測業務結果有沒有退步。
- 邊界/反例（1–2 句）：EDD 前提是有可量化的業務指標；對於探索性、創意性 Agent 任務，難以定義「回歸」。AI Judge 本身也可能有偏差，需要定期校準。
- 知識鉤子：與 #TDD作為AI控制介面 形成跨層呼應——TDD 在 code 層防止回歸，EDD 在 Agent 業務層防止回歸；可補充 #Interface+Test定義開發邊界 中「驗收條件」概念到 Agent 產品層。

[SKIP: common] Verizon 專案的具體數字（2.5 兆列、51% 轉換率）——屬於案例報導數據，缺乏可遷移的框架價值。
[SKIP: common] Unity Catalog 統一治理、Mosaic AI Gateway 的功能描述——屬於 Databricks 產品功能介紹。

## C. 連結建議（組裝藍圖）
- 內部組裝：卡片 1（Agent 記憶層）+ 卡片 2（EDD 品質閉環）可組成「Agent 產品化基礎設施」框架
- 外部對接：與 Idx_6 Databricks 生態卡片對接；EDD 可與 Idx_4 的測試驅動開發卡片形成跨層品質保證體系
