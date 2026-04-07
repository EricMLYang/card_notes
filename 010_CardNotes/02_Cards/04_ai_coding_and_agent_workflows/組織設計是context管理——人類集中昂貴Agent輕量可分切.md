# 組織設計是 context 管理——人類集中昂貴，Agent 輕量可分切

- 狀態：KEEP
- 類型：Principle
- 分類：4-
- 索引：010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260324_CoreNote_用Context看組織管理.md

## 核心命題
傳統組織設計的本質是 context 成本最佳化；Agent 的 context 成本結構完全相反，因此 Agent 的最佳組織方式不應沿用人類模式。

## 卡片內容
部門、職位、SOP 都在解決同一個問題：如何讓有限且昂貴的人力承載盡可能多的任務 context。人類的 context 集中、昂貴、不可分切——透過文件與訓練轉為長期記憶，讓一人穩定處理多種不穩定任務。企業傾向「一人多工」而非「一事一人」，因為 context 切換成本雖高但比多養人便宜。Agent 的 context 模型完全相反：輕量、可分切、成本低，一百個任務可以給一百個獨立 context 處理，靠大型模型基礎知識彌補 context 不足。這個成本結構差異，決定了 Agent 的最佳組織方式應該是分切而非集中，沿用人類的多工集中模式會浪費 Agent 的結構性優勢。

## 使用情境
- 設計 Agent workflow 架構時，判斷該「一個 Agent 多工」還是「多個 Agent 各司其職」
- 向團隊解釋為什麼 Agent 架構不該照搬人類組織圖
- 評估現有 Agent 系統是否過度集中 context

## 邊界 / 失效條件
- 當任務間有強耦合（共享大量狀態）時，分切 context 反而增加 Agent 間的通訊與協調成本
- 組織設計不只是 context 管理——權力、政治、文化等因素不在此框架內
- Agent 的 context 分切也有代價：context window 限制、跨 Agent 一致性維護、錯誤傳播風險

## 上游連結
- 交易成本理論（Coase：企業存在是因為市場交易成本）
- [[Agent 時代 CPU 從配角變指令層：工具處理佔總延遲 50%-90%]]

## 下游連結
- [[Agent-friendly CLI五大設計原則]]
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]
- [[非同步 Agent 工作模式是必然趨勢]]

## 關聯對照
- [[Agent組織化原則——專門context處理專門事情]]
- 微服務 vs 單體架構（同樣的分切 vs 集中取捨，但在不同層次）
- 限制理論（TOC）：瓶頸思維與避免局部最佳化

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
