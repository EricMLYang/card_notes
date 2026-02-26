---
name: sync-agent-instructions
description: 強制同步四個 AI Agent 指令檔案，以 .github/copilot-instructions.md 為主軸覆寫 CLAUDE.md、AGENTS.md、GEMINI.md。適用於「同步 agent 指令」「sync instructions」「讓四個 AI 設定檔一致」「更新 CLAUDE.md」「以 copilot-instructions 為主同步」「想確認四個檔案是否一致」。
---

# Skill: Sync Agent Instructions（Agent 指令強制同步）

## 目標
以 `.github/copilot-instructions.md` 為唯一主軸（Source of Truth），強制覆寫 `CLAUDE.md`、`AGENTS.md`、`GEMINI.md`。不比對、不確認，直接執行。

## 執行步驟
執行以下 bash 指令：

```bash
cp .github/copilot-instructions.md CLAUDE.md && \
cp .github/copilot-instructions.md AGENTS.md && \
cp .github/copilot-instructions.md GEMINI.md && \
echo "✅ 同步完成：CLAUDE.md、AGENTS.md、GEMINI.md 已與 .github/copilot-instructions.md 一致。"
```

## 輸出格式
同步完成後回報：

```
✅ 同步完成

📌 Source of Truth：.github/copilot-instructions.md
📝 已覆寫：
  - CLAUDE.md
  - AGENTS.md
  - GEMINI.md
```

## 自動執行設定
本 Skill 已透過 `.claude/settings.json` 的 PostToolUse hook 設定：
每當 Agent 修改 `.github/copilot-instructions.md`（Edit 或 Write 工具），自動觸發同步。

## 禁止事項
- ❌ 不可修改 `.github/copilot-instructions.md`（它是主軸，只讀）
- ❌ 不可在同步前做差異比對或請求確認
- ❌ 不可跳過任何一個目標檔案
