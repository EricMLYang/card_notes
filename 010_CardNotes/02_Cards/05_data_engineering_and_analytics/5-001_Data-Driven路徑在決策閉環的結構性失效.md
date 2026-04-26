# Data-Driven 路徑在決策閉環的結構性失效

- 狀態：KEEP
- 類型：Principle
- 分類：5-
- 索引：010_CardNotes/01_Index/05_data_engineering_and_analytics.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Trend/inbox/20260412_DecisionIntelligence_GartnerMQ_FlexRule.md（#2）

## 核心命題
BI/dashboard 回答「發生了什麼」，但無法閉合「決策建模 → 執行 → 監控 → 學習」這個 loop——因為 BI 的 product surface 不在這條路徑上。

## 卡片內容
FlexRule CEO 提出的機制化解釋：data-driven 路徑不是做不好 BI，而是 BI 沒有顯性的 decision model、沒有執行通路、沒有 outcome feedback。這給「為什麼在 BI 之上還要有一層 DecisionOps/DI」一個非情緒化的論證——不是「BI 過時了」，而是「BI 在閉環這個目標上結構性失效」。對 D2D Architect 是論述底座：你賣的不是更好的 dashboard，而是把 dashboard 接不上的最後一段路徑（執行通路、outcome feedback、persistence of decision context）補齊。

## 使用情境
- 撰寫 D2D/DecisionOps 定位文章
- 回答客戶「我有 BI 為什麼還要 DI」
- 設計 decision system 架構

## 邊界 / 失效條件
- 對單純探索性分析/一次性決策/低頻策略決策，BI + 人工判斷其實夠用
- 不是所有 dashboard 場景都需要閉環

## 上游連結
- [[DecisionOps]]
- [[因果推論商業應用：從相關性到指導性分析]]

## 下游連結
- [[13-001_FlexRule_Decision-Centric論述母句可平移成D2D定位]]
- [[三層進化：從 GenAI 圖表建議到 Agent]]

## 關聯對照
- [[兩階段判斷設計_AI自動化的安全模式]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
