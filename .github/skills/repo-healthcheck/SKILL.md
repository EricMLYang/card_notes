---
name: repo-healthcheck
description: 從角色 Repo 架構視角檢查資料夾結構、橋接一致性、技能索引與命名規範，輸出可執行修復建議。
---

# Skill: Repo Healthcheck（角色 Repo 結構健檢）

## 目標
用最小成本判斷本 Repo 是否符合「可持續演進的角色化知識系統」結構。

## 檢查範圍
1. 核心入口：`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md`
2. 角色治理：`.ai/identity.yaml`、`.ai/principles.md`、`.ai/knowledge/glossary.yaml`、`.ai/interfaces/*`、`.ai/memory/decisions.md`
3. 技能治理：`.github/skills/_index.yaml` 與實體 Skill 目錄一致性
4. 命名守規：`003_1CardsIndex` 命名格式 `Idx_<n>-*.md`

## 執行流程
### Step 1: 執行檢查
```bash
python .github/skills/repo-healthcheck/check.py
```

### Step 2: 解讀結果
- `PASS`：可接受
- `WARN`：建議修正
- `FAIL`：會造成流程中斷或治理失真，優先修正

### Step 3: 回報模板
```markdown
## Repo Healthcheck
- 結果：PASS / WARN / FAIL
- 主要缺口：...
- 建議修復順序：P0 / P1 / P2
```

## 觸發條件
- 「幫我檢查這個 Repo 的健康狀況」
- 「這個 Repo 有符合 Framework v2 規範嗎」
- 「檢查資料夾結構是否合理」

## 禁止事項
- ❌ 不要直接改動大量內容，先輸出可驗證的缺口
- ❌ 不要把內容品質問題誤判成結構問題