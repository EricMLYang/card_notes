---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-09
---

## [重點]
請貼上你認為的重點

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
