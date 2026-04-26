# Harness 六層構成 — Agent 系統工程的解構

- 狀態：KEEP
- 類型：Pattern
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260302_agent_haress_is_key.md（#2）+ 005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260412_AgentHarness2026_PhilSchmid.md（#1，合併）

## 核心命題
Harness 不是 prompt 也不是框架糖衣，而是六層可獨立設計、獨立測試的軟體工程組件——這是 IC、PM、架構師都能介入的層次。

## 卡片內容
把模型變成可上線 agent 的「外骨骼」由六層組成：(1) **迴圈協調器**（observe → decide → act → verify → update 的 OS 級 boot sequence）；(2) **工具集**（file/shell/browser/api/git/db，每個都是帶驗證的合約）；(3) **上下文管理**（摘要、壓縮、釘選、observation masking）；(4) **持久化**（state、memory、checkpoint、跨 session 身份）；(5) **驗證**（tests、lint、build、rubric、LLM-as-judge）；(6) **限制條件**（policy、權限、審批、邊界）。差別在於：六層的改進來自軟體工程而非模型訓練——這意味著它是團隊可以工程化迭代的層次，不是等模型廠商發新版。Phil Schmid 的 OS 類比（Model=CPU、Context=RAM、Harness=OS、Agent=App）描述的是同一件事的不同切面。

## 使用情境
- 設計或審查 Agent 系統時當作 checklist
- 評估投資哪一層 ROI 最高
- 對外溝通「為什麼換模型不會自動讓 agent 變好」

## 邊界 / 失效條件
- 任務極簡（單步、無副作用）時 harness 可以薄到接近 prompt
- 六層不是一次到位
- OS 類比的失效邊界——當 agent 任務天然短壽命，不需要 lifecycle 抽象

## 上游連結
- [[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]
- [[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]]

## 下游連結
- [[Agent 產品 95% 在 Production 失敗的原因]]
- [[測試套件是 Agentic Engineering 的核心槓桿點]]
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]

## 關聯對照
- [[Harness 是品味的具體實現]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
