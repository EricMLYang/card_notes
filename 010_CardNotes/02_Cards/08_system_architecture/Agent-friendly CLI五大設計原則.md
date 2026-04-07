# Agent-friendly CLI 五大設計原則

- 狀態：KEEP
- 類型：Pattern
- 分類：8-
- 索引：010_CardNotes/01_Index/08_system_architecture.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260327_CoreNote_CLI是Agent重要溝通介面.md

## 核心命題
為 Agent 設計的 CLI 必須同時滿足五個條件：結構化輸出、可探索指令、機器可理解錯誤、能力可組合、可直接變工具。

## 卡片內容
Addy Osmani 從 Google Workspace CLI 實踐中提煉出 Agent-friendly CLI 的五大設計原則：(1) 輸出結構化（JSON 為主），讓模型直接解析而非猜格式；(2) 指令可被探索（discovery-driven），從「人記得住」轉為「模型查得到」；(3) 錯誤可機器理解，讓 Agent 能根據錯誤碼自動調整或重試；(4) 能力可組合，提供 primitives 讓 Agent 自行組流程，而非只給大指令；(5) 可直接變成 Tool（如透過 MCP），免寫額外 wrapper。這五條同時也是評估任何系統「Agent 可操作性」的 checklist。

## 使用情境
- 設計新 CLI 或 internal tool 時，作為設計 checklist
- 評估現有工具是否適合被 Agent 使用
- 規劃 MCP Server 或 Tool 封裝策略時，判斷該暴露哪些能力

## 邊界 / 失效條件
- 五項原則之間的優先級未被明確處理——若只能滿足部分，作者未指出哪些最關鍵
- 「可組合」要求每個 primitive 的 input/output 契約穩定，在快速迭代的系統中可能是額外負擔
- 過度為 Agent 優化（如移除人類友善的 help text）可能損害人機共用場景

## 上游連結
- [[API是能力來源CLI是能力入口——Agent時代的介面分層]]
- [[好 API 設計可以維持很久——Stripe V2 的穩定抽象哲學]]

## 下游連結
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]
- MCP 協議實作、Tool wrapping 決策

## 關聯對照
- Unix 哲學（Do One Thing Well + pipe）
- [[架構是元素與關係的總和——拆解與假說思考]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
