# Harness 控制二維框架 — Guides×Sensors / Computational×Inferential

- 狀態：KEEP
- 類型：Principle
- 分類：4-
- 索引：010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Coding/01_inbox/20260407_Harness_Engineering_給Coding_Agent的外部控制系統.md（#1+#2+#3，合併）

## 核心命題
Fowler/Böckeler 的 harness 控制框架由兩條正交軸組成：時間軸（feedforward guides ↔ feedback sensors）+ 機制軸（computational ↔ inferential）；只有 sensors 會反覆犯同樣錯，只有 guides 不知道生效沒。

## 卡片內容
外部 harness 的雙重目標：(1) 提高 agent 第一次就做對的機率（feedforward）；(2) 在人類看到結果前自我修正（feedback）。落地成兩個正交維度：**時間軸**——Guides（動手前的方向控制：AGENTS.md、skills、how-to、結構規範、codemods）vs Sensors（動作後的訊號：linters、tests、type checks、review agents、logs、browser checks）；**機制軸**——Computational controls（CPU 型，快、便宜、結果穩定）vs Inferential controls（LLM judge、AI code review，慢、貴、結果不穩但能補語意）。判準：能用 deterministic 工具的就用，真正需要語意判斷再交給 inferential，避免「LLM judge everywhere」的誤用。

## 使用情境
- 評估自家 repo 的 harness 完整度
- 設計 AI Coding workflow 時的控制策略選型
- 解釋「為什麼光靠 review agent 還是會反覆犯錯」

## 邊界 / 失效條件
- Guides 與 sensors 衝突時需要明確的優先順序機制
- 資源衝突時需要按業務風險定優先級
- 此框架來自 coding agent 觀察，遷移到 business decision agent 時 inferential 比例會更高

## 上游連結
- [[3-006_Harness六層構成_Agent系統工程的解構]]
- [[當計算轉為純執行，評估標準成了唯一的控制介面]]

## 下游連結
- [[8-002_Harnessability與Ambient_Affordances_AI友善環境的新架構競爭力]]
- [[3-007_四種Agent控制方式適用矩陣_Prompt_SOP_Workflow_SteeringHooks]]

## 關聯對照
- [[測試套件是 Agentic Engineering 的核心槓桿點]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
