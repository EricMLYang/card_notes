# Policy as Code — 護欄要在 LLM 之外執行（雙層防線）

- 狀態：KEEP
- 類型：Principle
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260316_AI_Agent生產架構_工具記憶評估護欄.md（#4）+ 005_PARA/02_Areas/AI_Software_Data/Agent/20260321_agent控制流程不能只靠長prompt.md（#2+#5，合併）

## 核心命題
護欄不是「在 system prompt 裡求模型遵守」，而是用機器可讀規則在 LLM 外部強制執行；agent 內 Steering Hook + gateway Policy Engine 形成 defense in depth。

## 卡片內容
把「允許的工具、審批要求、權限邊界」寫成可單元測試、可稽核、可重複執行的程式碼，在 LLM 外執行。護欄哲學是「讓失敗變得安全、可觀察、可恢復」。實作分兩層：**內層 Steering Hook**（在 agent loop 的 pre-tool-call 與 post-output 兩個攔截點放 deterministic Python function）+ **外層 Policy Engine**（在 gateway 層用 Cedar/OPA 對工具呼叫做策略評估，如 AWS Bedrock AgentCore）。兩層獨立失敗才會出事故。對應原則：能用 deterministic 程式擋的，絕不依賴 LLM 自己判斷。

## 使用情境
- 設計面向客戶或涉及金流/合規的 agent 時
- 處理 prompt injection 風險
- 把「希望模型記得」轉成「執行點被驗證」

## 邊界 / 失效條件
- 規則需要語意判斷時仍要在 hook 內叫一次 LLM judge
- 兩層 policy 容易產生規則衝突
- 過度 policy 會讓 agent 失去推理彈性

## 上游連結
- [[3-007_四種Agent控制方式適用矩陣_Prompt_SOP_Workflow_SteeringHooks]]
- [[3-006_Harness六層構成_Agent系統工程的解構]]

## 下游連結
- [[8-001_Tool合約設計_工具是帶驗證的類型化API]]
- AWS Shared Responsibility Model

## 關聯對照
- [[兩階段判斷設計_AI自動化的安全模式]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
