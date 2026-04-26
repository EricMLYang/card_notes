---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-09
---

## [重點]
Rivet 的 Sandbox Agent SDK，提供統一 API 層讓開發者寫一次整合、跨多個 Agent runtime 部署（Claude Code、Codex、OpenCode、Amp）

## [摘要]


## [詮釋]


---
# Rivet Launches the Sandbox Agent SDK to Solve Agent API Fragmentation

> 來源：InfoQ
> 連結：https://www.infoq.com/news/2026/02/rivet-agent-sandbox-sdk/
> 搜集日期：2026-02-28
> 搜集原因：Agent SDK 與工程落地

## 摘要

Rivet 發布 Sandbox Agent SDK，提供統一 API 層讓開發者寫一次整合、跨多個 Agent runtime 部署（Claude Code、Codex、OpenCode、Amp）。解決的問題：Agent 生態缺乏標準化——每個平台各自實作事件格式（Claude Code 用 JSONL over stdout，Codex 用 JSON-RPC）、session model、權限系統、部署 API。技術實作：15MB 靜態 Rust binary，零 runtime 依賴，可部署到任何 Linux 環境。開發者透過配置切換 Agent 而非重寫整合邏輯，使得跨 Agent 的效能比較和供應商遷移成為可能。

## 關鍵段落

碎片化現狀：「Each platform implements its own event formats, session models, permission systems, and deployment APIs」——每換一個 Agent 就要重寫整合。

統一抽象：所有 Agent 事件（lifecycle、streaming、human-in-the-loop、tool approvals、errors）遵循一致格式。開發者用 config 換 Agent，不用改 code。

架構：15MB 靜態 Rust binary，零 runtime 依賴，部署到 Docker/E2B/Vercel/Daytona 無需平台特定修改。

## 潛在卡片方向

- Agent API 碎片化問題與統一抽象層的出現
- 與 [[3-Agent SDK 兩種設計哲學：減法（抽取核心）vs 加法（遙控 CLI）]] 形成第三條路線：統一適配層

---
*由 scout-news 自動搜集，待 process-inbox 處理*

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Agent runtime 生態（Claude Code、Codex、OpenCode、Amp）各有自己的事件格式、session model、權限、部署 API；Rivet Sandbox SDK 用 15MB 靜態 Rust binary 做統一抽象層，讓開發者寫一次、跨 runtime 部署。
- 挑戰的預設：Agent SDK 只有「減法（Anthropic Agent SDK 抽核心）」與「加法（CLI 遙控）」兩條路；Rivet 提供第三條路——「適配層」。
- 個人映射：對 D2D Architect 視角而言，這條路線解鎖了「跨 Agent 比效能」「換供應商不重寫」的可能性，是 Vertical AI 在多 runtime 共存時的潛在治理層。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent SDK 的第三條路 — 統一適配層（Adapter Pattern for Agent Runtimes）
- 分級：Core
- 類型：Pattern
- 核心內容：除了「減法（抽取核心 SDK）」與「加法（遙控 CLI）」之外，Rivet 示範了第三條路：在多個 Agent runtime 上面架統一抽象層，所有 lifecycle / streaming / human-in-the-loop / tool approval / error 事件走同一格式。配 config 換 Agent，不用改程式。
- 保留理由：把 SDK 設計哲學從「兩條路」擴張到「三條路」，更新既有卡片（[[3-Agent SDK 兩種設計哲學]]）。
- 待補強處：抽象層常見的「最小公分母」問題——當底層 runtime 有獨特能力時會被吃掉。
- 初步知識鉤子：Adapter Pattern、跨平台抽象的取捨、Agent runtime fragmentation。

序號 2
- 候選標題：Agent 生態當前處於「沒有 HTTP / SQL 的階段」 — 標準化缺位是基礎建設窗口
- 分級：Support
- 類型：Pattern
- 核心內容：原文點出每個平台自實作 event format、session model、permission system、deployment API。這是新生態尚未經歷標準化的典型徵兆——類比 Web 還沒 HTTP、資料庫還沒 SQL 之前。Rivet 出手就是搶這個 timing。對 D2D 視角：在 Agent 生態的標準化窗口期，誰先建立 lingua franca，誰拿到後續治理話語權。
- 保留理由：是判斷「現在投資哪一層 Agent 工具」的時序信號。
- 待補強處：歷史上抽象層先行者通常會被後來的官方標準輾過（如 jQuery vs DOM API）；需追蹤 Anthropic 是否會出官方 spec。
- 初步知識鉤子：協議標準化的時間窗口、Adapter 先行 vs 規範後到、生態位卡位。

## C. 建議送 refine 的項目
- 序號 1（高優先：可直接擴充已有的 SDK 哲學卡片）
- 序號 2（中優先：是趨勢判讀類卡片，待後續事件驗證）

## D. 呼叫 refine-cards
- 將上述 2 張候選卡交由 refine-cards 精煉。
