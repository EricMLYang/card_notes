# Copilot Instructions - 第二大腦知識管理系統

本檔為橋接摘要，完整規範以根目錄 `AGENTS.md` 為準。

## 核心判準

- `AGENTS.md` 是唯一核心指令源
- `.github/skills/_index.yaml` 是技能機器來源
- `.github/skills/README.md` 是技能人工盤點
- 卡片索引檔位於 `010_CardNotes/01_Index/{編號}_分類名稱.md`

## 目錄快查

- `000_MyContext/`：個人化配置、問題意識、人名清單
- `003_Capture/`：待處理輸入
- `005_PARA/`：Projects / Areas / Resources / Archives
- `010_CardNotes/01_Index/`：卡片索引
- `010_CardNotes/02_Cards/`：正式卡片
- `015_Write/Draft/`：寫作草稿
- `015_Write/Publish/`：已發佈文章

## 檔名規範

- `003_Capture/`：`YYYYMMDD_[標題簡稱].md`
- `015_Write/Draft/`：`YYYYMMDD_[主題關鍵字].md`
- `015_Write/Publish/`：`YYYYMMDD_【標題】.md`

## 有效技能

| alias | trigger | mode |
| --- | --- | --- |
| `break-cards` | 拆解文章成卡片 | hybrid |
| `refine-cards` | 精煉候選卡並等待確認 | hybrid |
| `gather-cards` | 搜集寫作素材或卡片連結 | autonomous |
| `write-pipeline` | 開始新文章寫作流程 | interactive |
| `resume-draft` | 查看或恢復草稿進度 | autonomous |
| `enrich-capture` | 處理 `003_Capture/` 並分類進 PARA | interactive |
| `scout-news` | 搜集相關新聞與新資訊 | interactive |
| `update-profile` | 更新閱讀偏好 | hybrid |
| `fact-check` | 查證具體細節 | autonomous |
| `format-article` | 社群媒體排版 | autonomous |
| `filename-prefix-guard` | 檢查或修正日期前綴 | hybrid |
| `workspace-stats` | 查看工作區統計與最近變動 | autonomous |
| `repo-healthcheck` | 檢查結構與治理一致性 | autonomous |
| `copilot-sync` | 同步 `.github/copilot-instructions.md` | interactive |
| `skill-expand` | 將常做流程固化成 skill | interactive |

## 已停用舊稱

- `process-inbox` → `enrich-capture`
- `sync-agent-instructions` → `copilot-sync`
- `create-skill` → `skill-expand`

完整版請參閱 `AGENTS.md`。
