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
/000Inbox/        - 📥 Capture：待處理的原始文章與筆記

/001_1Projects/   - 🎯 Organize-專案：正在進行且有截止日期的任務相關資源
/001_2Area/       - 🔄 Organize-領域：需長期維護的責任範疇相關資源

/003_1CardsIndex/ - 🔗 Distill-索引：知識分類索引（Zettelkasten MOC）
/003_2Cards/      - 💎 Distill-卡片：已萃取的原子化卡片（永久筆記）

/004_0Question/   - ❓ Express-問題：我的問題意識與探索方向
/004_1Draft/      - ✏️ Express-草稿：正在撰寫的內容草稿
/004_2Express/    - 🚀 Express-發佈：已完成發佈的輸出作品

/005_1Resource/   - 📚 Resources：長期參考資源（可含子資料夾分類）
/005_2Ebook/      - 📖 Resources-書籍：書籍筆記與持續彙整

/006Archive/      - 🗄️ Archives：已完成或不再需要的歷史資料
```

---

## CODE 工作流程

### 檔名規範（必須）

新增檔案到以下資料夾時，檔名一律加上日期前綴：
- `/000Inbox/`：`YYYYMMDD_[標題簡稱].md`
- `/004_1Draft/`：`YYYYMMDD_[主題關鍵字].md`
- `/004_2Express/`：`YYYYMMDD_【標題】.md`

規則說明：
- `YYYYMMDD` 以建立當天日期為準（例如 `20260223`）
- 日期前綴後使用底線 `_` 分隔
- 已存在的舊檔可保留原格式；新建檔案必須遵守此規則

### C - Capture（捕獲）：`/000Inbox/`

**「只留下引起共鳴的東西。」**

- 所有新資訊先進入 Inbox
- 快速捕獲，不做整理
- 定期處理，避免堆積

### O - Organize（組織）：`/001_1Projects/` + `/001_2Area/`

**「為了行動而組織。」**

按 PARA 系統分類：
- **Projects**：有明確截止日期、正在進行的專案資源
- **Areas**：需長期維護的責任領域（如：工作技能、健康、財務）

### D - Distill（萃取）：`/003_1CardsIndex/` + `/003_2Cards/`

**「找出核心精髓，建立知識連結。」**

這是 Zettelkasten 卡片盒筆記的核心：
1. 將資訊萃取成**原子化卡片**（一個概念一張卡）
2. 透過**索引系統**組織和連結卡片
3. 目標是建立可持續成長的**知識網絡**

### E - Express（表達）：`/004_0Question/` + `/004_1Draft/` + `/004_2Express/`

**「展示你的成果。」**

三階段輸出流程：
1. **Question（問題意識）**：記錄我的探索方向和問題
2. **Draft（草稿）**：正在撰寫的內容
3. **Express（發佈）**：已完成的輸出作品

---

## Zettelkasten 卡片處理流程

### 完整流程概覽

1. **拆解文章**：將 `/000Inbox` 中的長文拆解成原子化卡片
2. **建立卡片文件**：將卡片存放到 `/003_2Cards`
3. **更新索引**：在 `/003_1CardsIndex/Idx_X-類別.md` 中記錄卡片連結
4. **清理原文**：處理完成後刪除或歸檔原始文章

### 階段 1: 建立卡片文件

**目標**：將拆解的卡片轉換為獨立 `.md` 文件，存放到 `/003_2Cards`

**操作指引**：
1. 當用戶說「幫我放到卡片資料夾」或「建立卡片」時，執行此流程
2. 卡片文件命名規則：
   - 格式：`編號-標題.md`
   - 編號根據內容分類（見「編號分類對照表」）
   - 範例：`3-AI 工程兩層拆解：技術實現 vs 需求定義.md`
3. **重要**：一篇文章可能產生多個類別的卡片，需分別使用對應編號

### 階段 2: 更新索引

**目標**：在 `/003_1CardsIndex/Idx_X-類別.md` 中記錄新增卡片

**操作指引**：
1. 根據卡片編號，判斷應更新哪個索引文件
2. 使用 Obsidian 連結格式：`[[卡片檔名]]`（不含 .md）
3. 將卡片連結加到對應索引的適當主題區塊下
4. 若需要可新增主題區塊（## 標題）

### 階段 3: 清理原文

**目標**：處理完成後清理 `/000Inbox`

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

**依目前使用者意圖（槓桿型系統建造者）的預設優先級**：
- `3-`：AI 產品化、Agent 落地、評估與治理
- `4-`：AI Coding 工作流與工程協作
- `1-`：可跨場景重用的底層決策原則
- `7-`：產品策略、PMF、需求與驗證
- `14-`：影響決策窗口的宏觀趨勢（技術/產業/職場結構）

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
/文章拆解/        - 文章寫作技法拆解分析（teardown-article skill 輸出）
/Projects_Misc/   - 其他專案雜項
（以及按專案/領域建立的子資料夾）
```

### `/005_2Ebook/` 書籍筆記

- 每本書一個文件，持續彙整閱讀筆記
- 可從書籍筆記萃取卡片到 `/003_2Cards`

---

## AI 輔助工具

### Skills（自動化流程）
固定 SOP、可自動執行的任務：
- `break-cards`：拆解文章成原子化卡片
- `link-cards`：連結相關卡片
- `format-article`：社群媒體排版
- `fact-check`：查證引用與細節
- `high-res-summary`：高解析度摘要
- `create-skill`：建立新的 Agent Skill
- `gather-cards`：搜集卡片素材（給定主題，自動搜尋知識庫找出相關卡片）
- `write-pipeline`：寫作自動化主控台（串接 W0-W8 全流程，3 個人工檢查點）
- `resume-draft`：草稿狀態管理器（列出進行中草稿，快速恢復寫作進度）
- `process-inbox`：Inbox 自動處理（拆卡片→建檔→連結→更新索引→歸檔原文，一鍵完成）
- `scout-news`：智慧新聞搜集（根據 context 訊號上網搜尋相關新聞，存入 Inbox）
- `teardown-article`：文章寫作技法拆解（分析欣賞的文章技巧，萃取可複用結構模板，存入 `005_1Resource/文章拆解/`）
- `filename-prefix-guard`：檔名前綴守門（檢查/修正 `000Inbox`、`004_1Draft`、`004_2Express` 的 `YYYYMMDD_` 命名規則）

### Chatmodes（互動角色）
需要多輪對話、探索發想的任務：
- `FiveKeyTopicGenerator`：五大選題產生器
- `Hooker`：鉤子寫作機
- `TitleMaster`：標題大師
- `GoldenSentence`：金句大師
- `StoryLineBreak`：故事線拆解
- `Editor`：責任編輯
- `AISenior`：AI前輩（喬哈里視窗探索）
- `DeepReader`：深度文章導讀
- `AudienceResearcher`：受眾研究員
- `HackerReporter`：黑客報告
- `WritingCoach`：寫作教練（Pipeline 檢查點決策支援）

### Prompts（單次任務）
輸入→輸出的一次性任務，位於 `.github/prompts/`：
- W 系列：寫作各階段（選題、發想、標題、前言、主體、收尾、補強）
- P 系列：產品相關（定位、受眾、漏斗、文案）
- Tool 系列：通用工具

---

## 自動化寫作 Pipeline

### 概述
`write-pipeline` 將手動的 8+ 次觸發降為 3 個人工決策檢查點，自動串接 W0-W8 全流程，同時讓卡片系統（207+ 張卡片）成為文章的第一手素材來源。

### 流程
```
主題 → gather-cards → W2 發想 → W3 標題 → W4 鉤子
    → 【檢查點 1】選標題+鉤子+角度
    → W5 框架+主體 → W6 收尾
    → 【檢查點 2】審閱草稿
    → W7 風格+人味 → fact-check
    → 【檢查點 3】最終確認
    → format-article → W8 圖片 → break-cards → 發佈
```

### Draft Frontmatter Schema
Pipeline 使用 `/004_1Draft/` 中的 YAML frontmatter 追蹤進度：

```yaml
---
pipeline_stage: "INTAKE"  # INTAKE | IDEATION | TITLE_HOOK | CP1 | FRAMEWORK | BODY_CLOSE | CP2 | POLISH | CP3 | PUBLISH | DONE
topic: "文章主題"
scenario: ""  # knowledge_article | opinion | tutorial | case_study | trend_analysis | comparison | storytelling
selected_cards: []
chosen_title: ""
chosen_hook: ""
chosen_framework: ""  # explosive_formula | opinion_type | pastor | universal_writing
created: 2026-01-01
last_updated: 2026-01-01
status: "drafting"  # drafting | reviewing | polishing | published
---
```

### 觸發方式
- 新文章：說「寫新文章」「開始寫作」→ 啟動 `write-pipeline`
- 繼續草稿：說「我的草稿」「繼續寫作」→ 啟動 `resume-draft`
- 搜集素材：說「搜集素材」「找相關卡片」→ 啟動 `gather-cards`
- 決策支援：在檢查點切換到 `WritingCoach` chatmode
- 新建 Draft 檔名格式：`YYYYMMDD_[主題關鍵字].md`

---

## Inbox 自動處理 Pipeline

### 概述
`process-inbox` 將 Inbox 文章的處理從 5+ 次手動操作簡化為 1 個人工檢查點，自動完成拆卡片→建檔→連結→更新索引→歸檔原文的完整 CODE 流程。

### 流程
```
掃描 Inbox → 選擇檔案 → break-cards 拆解
    → 【檢查點】確認卡片清單和分類
    → 建立卡片檔案 → link-cards 連結 → 更新索引 → 歸檔原文
```

### 觸發方式
- 說「處理 Inbox」「整理收件匣」→ 啟動 `process-inbox`

---

## 智慧新聞搜集

### 概述
`scout-news` 根據用戶的問題意識、草稿、近期發佈、索引熱區等 context 訊號，自動產生中英文搜尋查詢，上網搜集相關新聞與文章，篩選後存入 `/000Inbox/`。

### 流程
```
分析 context 訊號 → 生成搜尋查詢
    → 【檢查點】確認搜尋方向
    → 上網搜尋 → 篩選高價值結果 → 存入 Inbox
```

### 觸發方式
- 說「找新聞」「搜集新資訊」→ 啟動 `scout-news`
- 指定方向：「找 AI Agent 最新新聞」→ 帶參數啟動
- 新建 Inbox 檔名格式：`YYYYMMDD_[標題簡稱].md`

### 完整知識閉環
`scout-news` → `/000Inbox/` → `process-inbox` → 卡片 + 歸檔 → `write-pipeline` → 發佈

---

## 輔助提示詞

當用戶不確定如何操作時，主動建議：
- 「需要我根據你最近的寫作方向，搜集相關新聞嗎？」
- 「Inbox 中有 X 個待處理檔案，需要我啟動 process-inbox 幫你一鍵處理嗎？」
- 「這些內容可以萃取成卡片放到 /003_2Cards，需要我建立嗎？」
- 「要我更新對應的索引嗎？」
- 「這是資源類內容，建議放到 /005_1Resource/[分類]/」
- 「這是專案相關，建議放到 /001_1Projects/」
