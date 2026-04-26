# Harnessability 與 Ambient Affordances — AI 友善環境的新架構競爭力

- 狀態：KEEP
- 類型：Pattern
- 分類：8-
- 索引：010_CardNotes/01_Index/08_system_architecture.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Coding/01_inbox/20260407_Harness_Engineering_給Coding_Agent的外部控制系統.md（#4+#5，合併）

## 核心命題
不是每個 codebase 都同樣適合被 harness——強型別、清楚 module boundary、穩定 conventions 的 repo 直接讓 agent 成功率上升；harnessability 是 AI 時代的新架構決策維度。

## 卡片內容
Harnessability：repo 本身被外部控制系統治理的容易度。強型別語言天然帶來 type-checking sensor；清楚的 module boundary 允許 architecture fitness rules；成熟框架抽掉 agent 不該操心的細節。Ambient Affordances（Ned Letcher）描述更隱性的層次：良好目錄結構、明確模組邊界、穩定命名、可執行測試入口、清楚 conventions——這些「無需教 agent 的環境訊號」讓 agent 自然找到方向。重要結論：**對開發者好的環境，對 AI 也好**。但有結構性陷阱——legacy 系統最需要 harness 卻最難建，是「窮者越窮」。技術選型不只看人類生產力，還要看 agent 可治理性。

## 使用情境
- 技術選型決策時的長期效益重新定價
- 評估自家或客戶 repo 的 AI-readiness
- 解釋「為什麼某些團隊用同一個模型、同一個 IDE、結果差很大」

## 邊界 / 失效條件
- Ambient affordances 與 explicit guides（AGENTS.md）有取捨
- Legacy 重構成本可能高於切換 stack
- 「對 AI 好」可能與「對人類短期好」衝突

## 上游連結
- [[4-001_Harness控制二維框架_Guides×Sensors_Computational×Inferential]]
- [[Code 是表達系統設計意圖最精準的語言，放棄它就放棄了必要性]]

## 下游連結
- [[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]]
- [[4-002_Atomic_Skill判準_一行說完邊界乾淨可單測可替換]]

## 關聯對照
- [[架構是元素與關係的總和——拆解與假說思考]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
