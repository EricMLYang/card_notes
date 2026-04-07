---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-27
---

## [重點]
API 是能力的來源
CLI 是能力的入口

在 Agent 時代，「入口」變得更重要。

## [摘要]

## [詮釋]



先簡單介紹一下背景。

Addy Osmani 是 Google 的工程領導者，長期關注開發體驗（DX）、前端工程與工具設計。他近期推廣一個開源專案 Google Workspace CLI（gws CLI），核心概念是：這個 CLI 從一開始就同時為「人類」與「AI Agent」設計。

這個方向其實在講一件更本質的事：

過去我們設計 CLI，是為了讓人更方便操作系統；
現在開始出現一種新設計，是讓 AI 可以直接理解並操作系統。

---

接著講最關鍵的一個觀念。

API 跟 CLI 並不衝突。

API 是能力本身（例如 Drive、Gmail、Databricks 的各種服務）
CLI 是操作這些能力的介面

而且大多數 CLI，本質上就是包在 API 上面的一層。

---

但在 Agent 時代，差異開始出現。

如果直接用 API，流程通常是：

需要理解 SDK、處理驗證、組 request、解析 response
對 Agent 來說，整體成本高，而且容易出錯

如果用 CLI：

只需要呼叫指令 → 拿到結構化輸出（通常是 JSON） → 繼續決策
對 Agent 來說，就是一個「現成可用的工具」

---

所以可以用一句話理解：

API 是能力的來源
CLI 是能力的入口

在 Agent 時代，「入口」變得更重要。

---

Addy Osmani 在推的，其實是一種「Agent-friendly CLI」設計方式，重點有幾個：

1. 輸出要結構化（JSON 為主）
   讓模型不用猜格式，可以直接解析

2. 指令要可被探索（discovery-driven）
   不是讓人記，而是讓模型查得到

3. 錯誤要可機器理解
   讓 Agent 可以根據錯誤自動調整或重試

4. 能力要可組合
   提供小工具（primitives），讓 Agent 自己組流程

5. 可以直接變成 Tool（例如透過 MCP）
   讓 CLI 不用再寫一層 wrapper，就能被 Agent 使用

---

這件事可以對應到我們現在在做的事情：

不管是 Databricks、Genie Code、catalog function 或各種 internal tool，本質都在做同一件事：

把「系統能力」變成「Agent 可以直接操作的工具」

---

最後一句話總結：

過去我們優化的是「人怎麼用系統」，
接下來我們要優化的是「AI 能不能無摩擦地操作系統」。

---
