---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-09
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
# Demystifying Evals for AI Agents

> 來源：Anthropic Engineering Blog
> 連結：https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
> 搜集日期：2026-02-28
> 搜集原因：AI Agent 評估與品質保證方法

## 摘要

Anthropic 工程團隊發布的 Agent 評估實戰指南。建立了完整的評估分類學（Tasks、Trials、Graders、Transcripts、Outcomes），區分三種 Grader 類型（Code-based、Model-based、Human），並提出 pass@k（至少一次成功）vs pass^k（全部一致成功）兩個互補指標來處理 Agent 的非確定性。強調從 20-50 個真實失敗案例開始，而非等待完整覆蓋率。Eval 是產品團隊與研究團隊之間的溝通通道。

## 關鍵段落

Transcript vs Outcome 的關鍵區分：「a flight-booking agent might say 'Your flight has been booked' at the end of the transcript, but the outcome is whether a reservation exists in the environment's SQL database.」

三種 Grader 各有適用場景：Code-based 快速客觀但無法處理合理變體；Model-based 處理開放式任務但需校準；Human 是金標準但成本高延遲大。

非確定性處理：pass@k 衡量「至少一次成功的機率」，pass^k 衡量「每次都成功的一致性」——生產環境的 Agent 需要的是 pass^k。

Agent 類型決定評估策略：Coding Agent 用確定性測試（單元測試）；Research Agent 用混合方法（可靠性+覆蓋率+來源品質）；對話 Agent 用多輪模擬+persona；Computer Use Agent 需要真實/沙盒環境+後端狀態驗證。

實務建議：定期閱讀 transcript 防止 grading error 系統化；監控「eval saturation」——當 Agent 穩定通過所有可解任務時，現有 benchmark 已無法提供改進訊號。

## 潛在卡片方向

- pass@k vs pass^k：Agent 非確定性的兩個互補量化指標
- Eval 是產品與研究的溝通通道，不只是品質檢查
- 與 [[3-評估驅動開發（EDD）：AI Judges + 業務指標防止 Agent 品質回歸]] 形成方法論層互補
- 與 [[當計算轉為純執行，評估標準成了唯一的控制介面]] 形成理論-實踐對照

---
*由 scout-news 自動搜集，待 process-inbox 處理*
