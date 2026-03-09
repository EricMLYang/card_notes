---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-09
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
gws 的作者 Justin Poehnelt 發布了這篇極為珍貴的文章，比起 gws 本身，我甚至覺得這些內容更有價值！先bookmark下來，回頭我會寫一份文件來展開深入探索。

我建議直接看原文，但我也附上了中文。

You Need to Rewrite Your CLI for AI Agents
https://justin.poehnelt.com/posts/rewrite-your-cli-for-ai-agents/

https://x.com/JPoehnelt
--

你需要為 AI Agent 重寫你的 CLI

作者：Justin Poehnelt（Google 資深開發者關係工程師）

核心觀點：人類 DX 優化的是「可探索性」和「容錯性」；Agent DX 優化的是「可預測性」和「縱深防禦」。兩者差異大到不值得硬改現有 CLI 來適配 Agent。

作者以他為 Google Workspace 打造的 CLI 為例，分享了從第一天就以 AI Agent 為主要使用者來設計 CLI 的經驗。

七大設計原則

1. 原始 JSON 優先於自訂 flag：Agent 偏好直接傳入完整 API payload（--json '{...}'），而非一堆扁平的 --title、--locale flag。JSON 直接對應 API schema，LLM 生成零損耗。實務上建議兩種路徑並存：人類用便利 flag，Agent 用 raw JSON
。

2. Schema 自省取代文件：Agent 不該靠塞進 system prompt 的靜態文件（燒 token 又會過時）。CLI 本身應可在 runtime 查詢 schema（如 gws schema drive.files.list），輸出機器可讀的 JSON，成為 API 的即時真實來源。

3. Context Window 紀律：API 回傳的巨大 JSON 會吃掉 Agent 的上下文視窗。兩個機制很重要：field mask（只取需要的欄位）和 NDJSON 分頁（串流處理，不用一次載入整個陣列）。

4. 輸入強化以防幻覺：人類會打錯字，Agent 會產生幻覺——失敗模式完全不同。CLI 必須是最後一道防線：驗證檔案路徑（防止 ../../.ssh 路徑穿越）、拒絕控制字元、拒絕資源 ID 中嵌入的查詢參數、防止雙重 URL 編碼。把 Agent 當成不可信任的操作者。

5. 發布 Agent 技能檔，不只是指令：Agent 不會看 --help 或 Stack Overflow。gws 附帶 100 多個 SKILL.md 檔案（含 YAML frontmatter），編碼了 Agent 無法自行推斷的規則，例如「變更操作一律先用 --dry-run」、「list 呼叫一律加 --fields」。

6. 多介面支援：MCP、Extension、環境變數：同一個 binary 服務多種 Agent 介面——MCP（JSON-RPC over stdio）、Gemini CLI Extension、以及透過環境變數注入憑證的 headless 模式（Agent 不該做 OAuth 互動流程）。

7. 安全護欄：Dry-Run + 回應消毒：--dry-run 讓 Agent 在真正執行前先驗證請求；--sanitize 透過 Google Cloud Model Armor 過濾 API 回應，防禦嵌入在資料中的 prompt injection（例如惡意郵件內容試圖劫持 Agent 行為）。

改造現有 CLI 的建議順序

1. 加 --output json
2. 驗證所有輸入（假設輸入是惡意的）
3. 加 schema / --describe 指令
4. 支援 field mask / --fields
5. 加 --dry-run
6. 附上 CONTEXT.md 或技能檔
7. 暴露 MCP 介面