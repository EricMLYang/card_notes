# Copilot Instructions - 第二大腦知識管理系統

本檔為 AGENTS.md 的橋接摘要，完整規範以根目錄 AGENTS.md 為準。

## 專案概述

這是一個結合 **Building a Second Brain (CODE)** 與 **Zettelkasten（卡片盒筆記法）** 的知識管理系統，使用 Obsidian 進行管理。

核心理念：
- **CODE 流程**：Capture（捕獲）→ Organize（組織）→ Distill（萃取）→ Express（表達）
- **Zettelkasten**：原子化卡片 + 索引連結，建立知識網絡
- **PARA 架構**：Projects、Areas、Resources、Archives 的行動導向組織

---

## 目錄結構

```
000_MyContext/    - 個人化配置：閱讀偏好、拆卡偏好、問題意識
003_Capture/      - Capture：待處理的原始文章與筆記

005_PARA/         - PARA 架構：系統化的行動導向組織
  01_Projects/    - Organize-專案：正在進行且有截止日期的任務相關資源
  02_Areas/       - Organize-領域：需長期維護的責任範疇相關資源
    AI_Software_Data/       - AI 工程、軟體開發、資料科學
    Domains_and_Industries/ - IoT、車載、產業領域
    Personal_Thinking_and_Growth/ - 個人成長、知識管理、思維框架
    Product_Business_Strategy/    - 產品管理、商業策略
  03_Resources/   - Resources：長期參考資源（可含子資料夾分類）
  04_Archives/    - Archives：已完成或不再需要的歷史資料

010_CardNotes/    - Zettelkasten 卡片系統
  01_Index/       - Distill-索引：知識分類索引（idx_*.md）
  02_Cards/       - Distill-卡片：已萃取的原子化卡片（永久筆記）

015_Write/        - 寫作輸出流程
  Draft/          - Express-草稿：正在撰寫的內容草稿
  Publish/        - Express-發佈：已完成發佈的輸出作品
```

---

## 檔名規範（必須）

新增檔案到以下資料夾時，檔名一律加上日期前綴：
- `003_Capture/`：`YYYYMMDD_[標題簡稱].md`
- `015_Write/Draft/`：`YYYYMMDD_[主題關鍵字].md`
- `015_Write/Publish/`：`YYYYMMDD_【標題】.md`

規則：`YYYYMMDD` 以建立當天日期為準，日期後用底線 `_` 分隔。已存在的舊檔可保留原格式。

---

## Zettelkasten 卡片處理流程

### 完整流程

1. **拆解文章**：將 `005_PARA` (Projects/Areas) 中的長文拆解成原子化卡片
2. **建立卡片文件**：將卡片存放到 `010_CardNotes/02_Cards`
3. **更新索引**：在 `010_CardNotes/01_Index/idx_X-類別.md` 中記錄卡片連結
4. **清理原文**：處理完成後將原始檔案重命名為 `YYYYMMDD_CoreNote_原本檔名.md`，以標記為「已提取核心筆記」

### 建立卡片文件

- 當用戶說「幫我放到卡片資料夾」或「建立卡片」時，執行此流程
- 卡片文件命名：`編號-標題.md`（編號分類規則詳見 `.github/skills/break-cards/SKILL.md`「編號分類對照表」）
- 範例：`3-AI 工程兩層拆解：技術實現 vs 需求定義.md`
- 一篇文章可能產生多個類別的卡片，需分別使用對應編號

### 更新索引

- 根據卡片編號，更新對應的 `010_CardNotes/01_Index/idx_X-類別.md`
- 使用 Obsidian 連結格式：`[[卡片檔名]]`（不含 .md）
- 將卡片連結加到對應索引的適當主題區塊下

### 清理原文

- 有價值但非卡片的內容 → 移到 `005_PARA/03_Resources/` 或 `005_PARA/02_Areas/`
- 已萃取完成的原文 → 重命名為 `YYYYMMDD_CoreNote_原檔名.md`，或移到 `005_PARA/04_Archives/`

---

## 資源文件處理

### `005_PARA/02_Areas/` 子分類依據

主要分類（細節見各子資料夾內的 README.md）：
- `AI_Software_Data/`：AI 工程、軟體開發、資料科學
- `Domains_and_Industries/`：IoT、車載、產業領域
- `Personal_Thinking_and_Growth/`：個人成長、知識管理、思維框架
- `Product_Business_Strategy/`：產品管理、商業策略

> `Area` vs `Resource` 判斷原則：若此主題是你**持續在做、需長期維護**的工作域 → `Area`；若只是參考資料或一次性輸入 → `Resource`。

---

### `005_PARA/03_Resources/` 分類結構

參考 `005_PARA/03_Resources/README.md` 的完整分類說明。主要分類包含：
- 閱讀清單與學習資源
- 書籍筆記（持續彙整）
- 英文學習資源

---

## AI 輔助工具

### Skills（自動化流程）
- `break-cards`：拆解文章成原子化卡片（含編號分類對照表，為分類規則的唯一來源）。拆解完成後將原始檔案重命名為 `YYYYMMDD_CoreNote_原本檔名.md`
- `gather-cards`：搜集卡片素材與建立連結（雙模式：模式 A 為寫作搜集 5-15 張卡片，模式 B 為當前卡片連結 3-7 張相關卡片）
- `format-article`：社群媒體排版
- `fact-check`：查證引用與細節
- `high-res-summary`：高解析度摘要
- `create-skill`：建立新的 Agent Skill
- `write-pipeline`：寫作自動化主控台（觸發：「寫新文章」「開始寫作」）
- `resume-draft`：草稿狀態管理器（觸發：「我的草稿」「繼續寫作」）
- `process-inbox`：Capture 自動處理（觸發：「處理 Capture」「整理收件匣」）
- `scout-news`：智慧新聞搜集（觸發：「找新聞」「搜集新資訊」）。根據 `000_MyContext/capture_profile.md` 搜尋相關新聞
- `teardown-article`：文章寫作技法拆解
- `update-profile`：閱讀偏好更新器，分析喜歡的文章並更新 `000_MyContext/capture_profile.md`
- `filename-prefix-guard`：檔名前綴守門
- `sync-agent-instructions`：Agent 指令同步（以 AGENTS.md 為主軸同步至 copilot-instructions.md / CLAUDE.md / GEMINI.md）

### Agents（互動角色，位於 `.github/agents/`）
- `Editor`：責任編輯（懂程式開發的讀者視角審閱）
- `DeepReader`：深度文章導讀（七步驟批判性分析）
- `FiveKeyTopicGenerator`：五大選題產生器
- `AudienceResearcher`：受眾研究員
- `HackerReporter`：黑客報告（深度研究夥伴）
- `WritingCoach`：寫作教練（Pipeline 檢查點決策支援）
- `ThinkingCoach`：思考教練（陪伴探索問題、引導問出好問題）

### Prompts（單次任務，位於 `.github/prompts/`）
命名規則：`{系列}_{序號}_{英文簡稱}.prompt.md`
- **W 系列**（W0-W8）：寫作各階段（情境、選題、發想、標題、鉤子、主體、收尾、補強、點綴）
- **P 系列**（P1-P8）：產品與商業（商業模式、定位、產品、漏斗、文案、落地頁）
- **Tool 系列**：通用工具（深度研究、書籍推薦、文章分析）
