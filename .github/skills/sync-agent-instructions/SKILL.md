---
name: sync-agent-instructions
description: 以 AGENTS.md 為核心來源，檢查並同步 CLAUDE.md、GEMINI.md、copilot-instructions.md 的橋接一致性。
---

# Skill: Sync Agent Instructions

## 目標
確保多 Agent 入口不漂移，避免不同工具讀到不同規範。

## 執行步驟
1. 讀取 `AGENTS.md`（核心來源）
2. 檢查橋接檔是否存在：`CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md`
3. 比對橋接語義：
   - `CLAUDE.md` 明確導向 `AGENTS.md`
   - `GEMINI.md` 使用 `@./AGENTS.md`
   - `copilot-instructions.md` 標示其為 AGENTS 摘要
4. 輸出差異與修正建議；若用戶同意，再套用修正

## 觸發條件
- 「AGENTS.md 有修改，幫我確認橋接同步」
- 「確認 bridge file 一致性」
- 「sync agent instructions」

## 禁止事項
- ❌ 不要覆蓋 AGENTS.md 的主內容
- ❌ 不要把橋接檔改成獨立規範來源