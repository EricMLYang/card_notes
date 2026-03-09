# 3-Agent SDK 兩種設計哲學：減法（抽取核心）vs 加法（遙控 CLI）

**類型**：Model

## 概念

Claude Agent SDK 是減法——從 CLI 成功中抽取核心邏輯為 SDK，Agent Core 在你的 Process 內運行，純 Code Library，原生 Node/Python。GitHub Copilot SDK 是加法——CLI + 通訊協定，SDK 遙控真正的 CLI，先天分離部署，內建 server mode（`--headless --port`）。關鍵差異在部署架構：Claude SDK 是同 Process（彈性高但語言綁定），Copilot SDK 是獨立 Process（語言無關但多一層通訊）。選擇取決於：語言生態（.NET 只有 Copilot 官方支援）、環境一致性需求（Prototype 和 Production 用同一套 CLI）、分散式部署需求。

## 重要性

為「用哪套 SDK 整合 Agent 到既有服務」提供明確的選型框架。

## 邊界/反例

SDK 生態快速演進，這個對比的保鮮期可能只有 6-12 個月。若需要深度客製化 Agent 行為（如自定義 tool execution），Claude SDK 的同 Process 架構更有彈性。

## 標籤

#AgentSDK #Claude #Copilot #架構選型 #SDK設計
