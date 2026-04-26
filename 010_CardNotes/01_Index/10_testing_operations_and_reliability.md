# idx_testing_and_operations

主題：Testing and Operations

關聯 Area：`005_PARA/02_Areas/AI_Software_Data/Software_Engineering`

## Topics

- testing
- QA
- observability
- DevOps and operations
- evaluation
- validation
- guardrails
- deployment responsibility

## Cards

### AI 與系統驗證
- [[AI Error Analysis：LLM 應用評估方法]]
- [[AI時代評估能力成為關鍵槓桿點]]
- [[AI 協作時代 - 衡量變重要]]
- [[當計算轉為純執行，評估標準成了唯一的控制介面]]

### Guardrails 與上線責任
- [[兩階段判斷設計_AI自動化的安全模式]]
- [[測試套件是 Agentic Engineering 的核心槓桿點]]
- [[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]]

### Agent Production 失敗模式（2026-04 batch）
- [[10-001_Agent速度撞上legacy_backend的DDoS化失敗模式]] - agent QPS 拉高 3-4 量級被 WAF 擋
- [[10-002_Policy_as_Code護欄要在LLM之外執行]] - 內層 Steering Hook + 外層 Policy Engine 雙層防線
- [[10-003_Production_Agent失靈是慢性失能而非急性故障]] - 慢性退化的監控指標體系

### Eval 與評估方法（2026-04 batch）
- [[10-004_pass@k_vs_pass^k_能上線vs只能demo的最尖銳判準]] - 連續 k 次都對 vs 至少一次對
- [[10-005_20-50個真實失敗就能啟動Eval]] - 完美覆蓋率是延遲投資的藉口
- [[10-006_三類Grader是分層防線_Swiss_Cheese_Model]] - code/model/human grader 縱深防禦
- [[10-007_Transcript≠Outcome_Agent評估必須驗環境狀態]] - eval 最小單位是世界狀態變化
- [[10-008_Span-Level_Debug是Agent工程的分水嶺]] - retrieval/generation/tool-call 三層拆解
