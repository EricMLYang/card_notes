# Skills Registry

本檔是 `.github/skills/` 的人工盤點來源。

- 機器來源：[`_index.yaml`](./_index.yaml)
- 核心指令源：[`AGENTS.md`](../../AGENTS.md)
- 詳細規範：各 skill 目錄下的 `SKILL.md`

## Active Skills

| Alias | 用途 | Trigger 摘要 | Mode | Path |
| --- | --- | --- | --- | --- |
| `break-cards` | 長文拆成 lite 候選卡 | 拆解文章、拆成卡片 | `hybrid` | `break-cards/SKILL.md` |
| `refine-cards` | 精煉正式卡並等待確認 | 精煉候選卡、正式卡草稿 | `hybrid` | `refine-cards/SKILL.md` |
| `gather-cards` | 搜集卡片素材與連結 | 搜集素材、找相關卡片 | `autonomous` | `gather-cards/SKILL.md` |
| `write-pipeline` | 啟動寫作流程 | 寫新文章、開始寫作 | `interactive` | `write-pipeline/SKILL.md` |
| `resume-draft` | 恢復草稿進度 | 我的草稿、繼續寫作 | `autonomous` | `resume-draft/SKILL.md` |
| `enrich-capture` | 處理 `003_Capture/` 並移入 PARA | 處理 Capture、整理捕獲檔案 | `interactive` | `enrich-capture/SKILL.md` |
| `scout-news` | 搜集新聞與深度文章 | 找新聞、搜集新資訊 | `interactive` | `scout-news/SKILL.md` |
| `update-profile` | 更新閱讀偏好 | 更新偏好、分析喜歡的文章 | `hybrid` | `update-profile/SKILL.md` |
| `fact-check` | 事實查證 | 幫我查證、檢查引用 | `autonomous` | `fact-check/SKILL.md` |
| `format-article` | 社群媒體排版 | 幫我排版、調整排版 | `autonomous` | `format-article/SKILL.md` |
| `filename-prefix-guard` | 檢查日期前綴 | 檢查檔名格式、補上日期前綴 | `hybrid` | `filename-prefix-guard/SKILL.md` |
| `workspace-stats` | 工作區統計與變更回顧 | 統計工作區、查看最近變動 | `autonomous` | `workspace-stats/SKILL.md` |
| `repo-healthcheck` | 結構與治理健檢 | 檢查 Repo 健康狀況 | `autonomous` | `repo-healthcheck/SKILL.md` |
| `copilot-sync` | 同步 Copilot 橋接檔 | 確認橋接同步狀態 | `interactive` | `copilot-sync/SKILL.md` |
| `skill-expand` | 把常做流程固化成新 skill | 固化成技能、Repo 缺少某類技能 | `interactive` | `skill-expand/SKILL.md` |

## Deprecated Aliases

| 舊稱 | 現況 | 替代 |
| --- | --- | --- |
| `process-inbox` | renamed | `enrich-capture` |
| `sync-agent-instructions` | renamed | `copilot-sync` |
| `create-skill` | merged | `skill-expand` |
| `high-res-summary` | removed | 無 |
| `teardown-article` | removed | 無 |
| `archive-article` | removed | 無 |

## Governance Notes

- 新增或移除 skill 時，需同步更新 `_index.yaml`、本檔與必要的橋接文件。
- `AGENTS.md` 只保留能力摘要，不再手動維護完整技能細節。
- `CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md` 屬橋接檔，不應成為額外的規範來源。
