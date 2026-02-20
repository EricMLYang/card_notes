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
| **1-** | `Idx_1-CoreConcepts.md` | 核心思維、策略原則、基礎概念、思考方法 |
| **2-** | `Idx_2-PersonKnowledgeManage.md` | 個人知識管理、學習方法、認知提升、職涯發展 |
| **3-** | `Idx_3-AiApplication.md` | AI 應用、LLM 產品、AI 工具、AI 產業分析 |
| **4-** | `Idx_4-AiCoding.md` | AI 輔助編程、軟體工程、開發實踐、工程師職涯 |
| **5-** | `Idx_5-BusinessDataScience.md` | 商業分析、數據科學、決策科學 |
| **6-** | `Idx_6-Databricks.md` | Databricks 相關技術與實踐 |
| **7-** | `Idx_7-ProductManager.md` | 產品管理、PM 思維、客戶理解、PMF 框架 |
| **8-** | `Idx_8-系統架構知識.md` | 系統架構設計、分散式系統、微服務、雲端架構 |
| **9-** | `Idx_9-軟體工程知識.md` | 軟體工程方法論、開發流程、代碼品質、測試 |
| **10-** | `Idx_10-系統驗測與維運.md` | 系統測試、監控、維運、DevOps、SRE |
| **11-** | `Idx_11-投資理財房地產.md` | 投資策略、理財規劃、房地產知識 |
| **12-** | `Idx_12-個人效率與成長.md` | 時間管理、效率工具、個人成長、習慣養成 |
| **13-** | `Idx_13-AI寫作.md` | AI 輔助寫作、內容創作、寫作方法 |
| **14-** | `Idx_14-世界政經科技趨勢.md` | 全球趨勢、政經分析、科技發展、產業變遷 |

**判斷邏輯**：
- **常用分類（1-7）**：
  - AI 產品策略、AI 時代轉型 → 3-AiApplication
  - AI 輔助開發、工程師職涯 → 4-AiCoding
  - 產品開發、PMF、客戶理解 → 7-ProductManager
  - 個人學習、職涯發展 → 2-PersonKnowledgeManage
  - 通用策略思維、決策框架 → 1-CoreConcepts
  - 商業分析、數據決策 → 5-BusinessDataScience
- **專業領域分類（8-14）**：按具體領域歸類

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

### Prompts（單次任務）
輸入→輸出的一次性任務，位於 `.github/prompts/`：
- W 系列：寫作各階段（選題、發想、標題、前言、主體、收尾、補強）
- P 系列：產品相關（定位、受眾、漏斗、文案）
- Tool 系列：通用工具

---

## 輔助提示詞

當用戶不確定如何操作時，主動建議：
- 「這些內容可以萃取成卡片放到 /003_2Cards，需要我建立嗎？」
- 「要我更新對應的索引嗎？」
- 「這是資源類內容，建議放到 /005_1Resource/[分類]/」
- 「這是專案相關，建議放到 /001_1Projects/」
