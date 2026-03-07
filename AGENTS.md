# AGENTS.md — 第二大腦知識管理系統

> 本文件是本 Repo 的核心指令源。完整規範以此為準。

## 專案概述

這是一個結合 **Building a Second Brain (CODE)** 與 **Zettelkasten（卡片盒筆記法）** 的知識管理系統，使用 Obsidian 進行管理。

核心理念：
- **CODE 流程**：Capture（捕獲）→ Organize（組織）→ Distill（萃取）→ Express（表達）
- **Zettelkasten**：原子化卡片 + 索引連結，建立知識網絡
- **PARA 架構**：Projects、Areas、Resources、Archives 的行動導向組織

---

## 目錄結構

```
/000Inbox/        - Capture：待處理的原始文章與筆記

/001_1Projects/   - Organize-專案：正在進行且有截止日期的任務相關資源
/001_2Area/       - Organize-領域：需長期維護的責任範疇相關資源
  /AI知識管理和寫作/  - Zettelkasten、PKM、Second Brain、AI 輔助寫作、Build in Public
  /Agent/          - AI Agent 應用、Agentic 工作流
  /AI_Trend/       - AI 趨勢觀察與策略研究
  /AISoftwareEngineering/ - AI 軟體工程實踐
  /BussinessDataScience/  - 商業資料科學
  /Databricks/     - Databricks 平台
  /IoT_Domain/     - IoT、車載領域
  /Product_Business/ - 產品管理、商業策略
  /AWS/ /Azure/    - 雲端平台實踐

/003_1CardsIndex/ - Distill-索引：知識分類索引（Zettelkasten MOC）
/003_2Cards/      - Distill-卡片：已萃取的原子化卡片（永久筆記）

/004_0Question/   - Express-問題：我的問題意識與探索方向
/004_1Draft/      - Express-草稿：正在撰寫的內容草稿
/004_2Express/    - Express-發佈：已完成發佈的輸出作品

/005_1Resource/   - Resources：長期參考資源（可含子資料夾分類）
/005_2Ebook/      - Resources-書籍：書籍筆記與持續彙整

/006Archive/      - Archives：已完成或不再需要的歷史資料
```

---

## 檔名規範（必須）

新增檔案到以下資料夾時，檔名一律加上日期前綴：
- `/000Inbox/`：`YYYYMMDD_[標題簡稱].md`
- `/004_1Draft/`：`YYYYMMDD_[主題關鍵字].md`
- `/004_2Express/`：`YYYYMMDD_【標題】.md`

規則：`YYYYMMDD` 以建立當天日期為準，日期後用底線 `_` 分隔。已存在的舊檔可保留原格式。

---

## Zettelkasten 卡片處理流程

### 完整流程

1. **拆解文章**：將 `/000Inbox` 中的長文拆解成原子化卡片
2. **建立卡片文件**：將卡片存放到 `/003_2Cards`
3. **更新索引**：在 `/003_1CardsIndex/Idx_X-類別.md` 中記錄卡片連結
4. **清理原文**：處理完成後刪除或歸檔原始文章

### 建立卡片文件

- 當用戶說「幫我放到卡片資料夾」或「建立卡片」時，執行此流程
- 卡片文件命名：`編號-標題.md`（編號分類規則詳見 `.github/skills/break-cards/SKILL.md`「編號分類對照表」）
- 範例：`3-AI 工程兩層拆解：技術實現 vs 需求定義.md`
- 一篇文章可能產生多個類別的卡片，需分別使用對應編號

### 更新索引

- 根據卡片編號，更新對應的 `/003_1CardsIndex/Idx_X-類別.md`
- 使用 Obsidian 連結格式：`[[卡片檔名]]`（不含 .md）
- 將卡片連結加到對應索引的適當主題區塊下

### 清理原文

- 有價值但非卡片的內容 → 移到 `/005_1Resource/` 或 `/001_X/`
- 已萃取完成的原文 → 刪除或移到 `/006Archive/`

---

## 資源文件處理

### `/001_2Area/` 子分類依據

| 子資料夾 | 收錄範疇 | 典型觸發關鍵詞 |
|----------|---------|----------------|
| `AI知識管理和寫作` | Zettelkasten、PKM、Second Brain 方法論、AI 輔助寫作流程、寫作技法、Build in Public | 知識管理、卡片筆記、寫作流程、第二大腦、輸出策略 |
| `Agent` | AI Agent 設計、Agentic 工作流、MCP、評估框架 | Agent、Agentic、eval、工作流 |
| `AI_Trend` | AI 產業趨勢、模型發布、策略觀察 | AI趨勢、大模型、產業 |
| `AISoftwareEngineering` | AI 輔助開發、Coding Agent、工程實踐 | Cursor、Copilot、TDD、AI開發 |
| `BussinessDataScience` | 商業資料分析、資料工程 | 資料科學、分析、Pipeline |
| `Databricks` | Databricks 平台操作與架構 | Databricks、Spark |
| `IoT_Domain` | IoT、車載、Beacon、數位看板 | IoT、車載、Beacon |
| `Product_Business` | 產品管理、商業模式、策略 | 產品、商業模式、策略 |
| `AWS` / `Azure` | 雲端服務實踐與架構 | AWS、Azure、雲端 |

> `Area` vs `Resource` 判斷原則：若此主題是你**持續在做、需長期維護**的工作域 → `Area`；若只是參考資料或一次性輸入 → `Resource`。

---

### `/005_1Resource/` 分類結構

```
/AI/              - AI 趨勢、策略、產業影響
/LLM_Tools/       - Claude、Anthropic、LLM 應用/框架
/Dev_Engineering/ - 軟體開發、架構、資安、前後端
/Product_Business/- 產品管理、商業模式、策略
/Reference/       - 學習資源、閱讀清單、概念說明
/IoT_Domain/      - IoT、車載、Beacon、數位看板
/文章拆解/        - 文章寫作技法拆解分析
/Projects_Misc/   - 其他專案雜項
```

### `/005_2Ebook/` 書籍筆記

- 每本書一個文件，持續彙整閱讀筆記
- 可從書籍筆記萃取卡片到 `/003_2Cards`

---

## AI 輔助工具

### Skills（自動化流程）
- `break-cards`：拆解文章成原子化卡片（含編號分類對照表，為分類規則的唯一來源）
- `link-cards`：連結相關卡片
- `format-article`：社群媒體排版
- `fact-check`：查證引用與細節
- `high-res-summary`：高解析度摘要
- `create-skill`：建立新的 Agent Skill
- `gather-cards`：搜集卡片素材
- `write-pipeline`：寫作自動化主控台（觸發：「寫新文章」「開始寫作」）
- `resume-draft`：草稿狀態管理器（觸發：「我的草稿」「繼續寫作」）
- `process-inbox`：Inbox 自動處理（觸發：「處理 Inbox」「整理收件匣」）
- `scout-news`：智慧新聞搜集（觸發：「找新聞」「搜集新資訊」）
- `teardown-article`：文章寫作技法拆解
- `update-profile`：閱讀偏好更新器
- `filename-prefix-guard`：檔名前綴守門
- `sync-agent-instructions`：Agent 指令同步（以 `copilot-instructions.md` 為主軸同步至 CLAUDE.md / AGENTS.md / GEMINI.md）

### Agents（互動角色，位於 `.github/agents/`）
- `Editor`：責任編輯（懂程式開發的讀者視角審閱）
- `DeepReader`：深度文章導讀（七步驟批判性分析）
- `FiveKeyTopicGenerator`：五大選題產生器
- `AudienceResearcher`：受眾研究員
- `HackerReporter`：黑客報告（深度研究夥伴）
- `WritingCoach`：寫作教練（Pipeline 檢查點決策支援）

### Prompts（單次任務，位於 `.github/prompts/`）
命名規則：`{系列}_{序號}_{英文簡稱}.prompt.md`
- **W 系列**（W0-W8）：寫作各階段（情境、選題、發想、標題、鉤子、主體、收尾、補強、點綴）
- **P 系列**（P1-P8）：產品與商業（商業模式、定位、產品、漏斗、文案、落地頁）
- **Tool 系列**：通用工具（深度研究、書籍推薦、文章分析）
