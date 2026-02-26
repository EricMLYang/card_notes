# Copilot Instructions - 第二大腦知識管理系統

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
- 卡片文件命名：`編號-標題.md`（編號見「編號分類對照表」）
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

## 編號分類對照表

| 編號 | 索引文件 | 主題範疇 |
|------|----------|----------|
| **1-** | `Idx_1-CoreConcepts.md` | 通用原則與底層思維（策略、決策、槓桿、第一性原理）；跨領域可重用的判斷框架優先放這裡。 |
| **2-** | `Idx_2-PersonKnowledgeManage.md` | 個人知識管理與能力成長（學習法、職涯定位、創作者工作流、心智升級）。 |
| **3-** | `Idx_3-AiApplication.md` | AI 應用與產品化實戰（Agent/LLM 應用、產品策略、評估方法、商業化落地）。 |
| **4-** | `Idx_4-AiCoding.md` | AI Coding 與開發工作流（程式開發協作模式、工程師角色轉型、Coding Agent 實務）。 |
| **5-** | `Idx_5-BusinessDataScience.md` | 商業分析與數據決策（因果推論、統計方法、實驗設計、Decision Science）。 |
| **6-** | `Idx_6-Databricks.md` | Databricks 生態與資料平台實作（Lakehouse、Delta、治理、產品化平台）。 |
| **7-** | `idx_7-ProductManager.md` | 產品管理與 PMF（需求洞察、驗證框架、產品策略、跨部門推進）。 |
| **8-** | `Idx_8-系統架構知識.md` | 系統架構與分散式設計（系統邊界、元件關係、架構取捨）。 |
| **9-** | `Idx_9-軟體工程知識.md` | 軟體工程方法與品質（Code Review、設計原則、開發規範、工程治理）。 |
| **10-** | `Idx_10-系統驗測與維運.md` | 測試、監控與維運（Observability、SRE、部署治理、故障處理）。 |
| **11-** | `Idx_11-投資理財房地產.md` | 投資、資產配置與房地產（資本配置、風險管理、財務思維）。 |
| **12-** | `Idx_12-個人效率與成長.md` | 個人效率與習慣系統（時間管理、習慣設計、能量管理）。 |
| **13-** | `Idx_13-AI寫作.md` | AI 寫作與表達設計（敘事、Hook、文案結構、內容傳播）。 |
| **14-** | `Idx_14-世界政經科技趨勢.md` | 宏觀趨勢與產業轉向（全球政經科技、勞動市場變化、不可逆結構性趨勢）。 |

**分類判斷順序（避免重複分類）**：
1. 先判斷是否為「宏觀趨勢/產業結構變化」：是則優先 `14-`。
2. 再判斷是否為明確專業域：Databricks (`6-`)、軟體工程方法 (`9-`)、架構 (`8-`)、測維 (`10-`)。
3. AI 主題再細分：AI 產品/應用 (`3-`) vs AI Coding/開發工作流 (`4-`)。
4. 非特定技術域但可跨域重用的思維框架：歸 `1-`。
5. 若是個人成長、知識管理、寫作表達：依內容落在 `2-`、`12-`、`13-`。

**衝突處理**：
- 同時命中多類時，只選一個主分類，原則為「這張卡片最常被用來做哪種決策」。
- 以「用途」優先於「來源」：同一篇文章可拆出不同編號卡片。

---

## 資源文件處理

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
- `break-cards`：拆解文章成原子化卡片
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
- `filename-prefix-guard`：檔名前綴守門

### Chatmodes（互動角色）
- `FiveKeyTopicGenerator`、`Hooker`、`TitleMaster`、`GoldenSentence`、`StoryLineBreak`
- `Editor`、`AISenior`、`DeepReader`、`AudienceResearcher`、`HackerReporter`
- `WritingCoach`：寫作教練（Pipeline 檢查點決策支援）

### Prompts（單次任務）
位於 `.github/prompts/`：W 系列（寫作各階段）、P 系列（產品相關）、Tool 系列（通用工具）
