# Tool 合約設計 — 工具是帶驗證的類型化 API，不是建議

- 狀態：KEEP
- 類型：Pattern
- 分類：8-
- 索引：010_CardNotes/01_Index/08_system_architecture.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260316_AI_Agent生產架構_工具記憶評估護欄.md（#2）+ 005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260414_李宏毅2026Agent課高解析摘要.md（#6，合併）

## 核心命題
給 agent 的工具必須有型別化合約與統一結果格式，且要避開「擬人化操作」（如分頁瀏覽）；沒有合約的工具會在規模化時變成最大的不穩定來源。

## 卡片內容
每個工具呼叫應有：型別化 input/output、超時、重試預算、成本上限、統一結果格式 `{ok, data, error, meta}`。把工具當「合約」而非「魔法函數」，讓上游 LLM 與下游 reducer 都能預期失敗模式。**反 pattern**：給 agent 過於擬人化的工具（如需要一頁一頁翻的搜尋引擎、複雜 UI 導航），反而會害模型崩潰——agent 更擅長處理結構化（JSON）或直接的 CLI 輸出，應提供支援 JSON 過濾、SQL aggregation 的底層函式。對 Vertical Data Agent 特別關鍵：每個工具的失敗模式都是 trace 上可分析、可回放、可單測的事件。

## 使用情境
- 設計新的 agent tool 時的 SOP 範本
- Code review agent 的工具註冊清單
- 把 legacy 內部 API 改成 agent-friendly 時的重構判準

## 邊界 / 失效條件
- 統一結果格式在 streaming/partial result 場景需要擴展
- 某些瀏覽器自動化任務天然需要「擬人化」操作
- 過度型別化會讓工具開發成本上升

## 上游連結
- [[3-006_Harness六層構成_Agent系統工程的解構]]

## 下游連結
- [[10-002_Policy_as_Code護欄要在LLM之外執行]]
- [[Agent-friendly CLI五大設計原則]]
- [[API是能力來源CLI是能力入口——Agent時代的介面分層]]

## 關聯對照
- [[好 API 設計可以維持很久——Stripe V2 的穩定抽象哲學]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
