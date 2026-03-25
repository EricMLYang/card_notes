---
name: search-notes
description: >
  在 Capture、PARA Areas、卡片庫中快速搜尋。根據關鍵字定位 [重點] 片段與卡片核心概念，
  回傳排序後的相關結果。觸發語句：「搜尋」「找一下」「有沒有關於 X 的卡片」
  「幫我找 X 相關的筆記」「search」。
---

# Skill: Search Notes（筆記快速搜尋）

## 目標

以關鍵字快速定位以下三個範圍的內容：
- `003_Capture/`：Capture 文章的 `[重點]` 區段
- `005_PARA/02_Areas/`：Areas 文章的 `[重點]` 區段
- `010_CardNotes/02_Cards/`：卡片標題與核心概念段落

## 觸發語句

- 「搜尋 XXX」「找一下 XXX」
- 「有沒有關於 XXX 的卡片/文章/筆記」
- 「幫我找 XXX 相關的內容」
- 「search XXX」

## 執行步驟

### Step 1: 解析查詢意圖

- 提取關鍵字（支援中英文混合）
- 判斷搜尋範圍：
  - 「找卡片」「卡片裡」→ `--scope cards`
  - 「找文章」「Areas 裡」→ `--scope areas`
  - 「Capture 裡」→ `--scope capture`
  - 其他 → `--scope all`（預設）
- 判斷分類篩選：若用戶指定特定分類（如「AI 相關」），加上 `--category 03`

### Step 2: 執行搜尋腳本

```bash
python .github/skills/search-notes/quick_search.py "<query>" --format json --limit 10
```

可用參數：
- `--scope cards|areas|capture|all`：限定搜尋範圍
- `--limit N`：回傳筆數，預設 10
- `--category NN`：只搜特定卡片分類前綴（如 `03`、`07`）
- `--format json|text`：輸出格式

### Step 3: 解析並展示結果

若 `total_found == 0`：
- 提示用戶換關鍵字或縮小/擴大範圍

若有結果，展示前 5 筆（格式如下），並根據結果類型提供後續行動：

```markdown
## 搜尋結果：「XXX」
找到 N 筆相關內容（掃描 M 個檔案）

### 卡片（X 張）
1. [[卡片標題]]  `score: N.N`
   > 核心概念片段...
   分類：XX_category_name

### 文章（X 篇）
1. 文章標題  `[process_level: 1]`
   > [重點] 片段...
   路徑：`005_PARA/02_Areas/.../`

### 後續建議
- 讀卡片詳情：說「讀 [[卡片名]]」
- 找相關連結：說「幫我連結 [[卡片名]]」（觸發 gather-cards）
- 拆解文章：說「幫我拆解這篇」（觸發 break-cards）
```

## 與其他 Skill 的整合

**在 `gather-cards` 中使用**：在 Step 2（搜尋索引定位）前，可先呼叫本腳本快速定位候選卡片，縮小後續的索引掃描範圍：

```bash
python .github/skills/search-notes/quick_search.py "<核心概念>" --scope cards --format json --limit 20
```

## 注意事項

- 腳本使用純 Python 標準函式庫，無需安裝額外套件
- 每次即時掃描（無預建索引），適合 500 個以下的檔案規模
- 分數 < 0.1 的結果自動過濾
- 支援 Windows 與 Mac/Linux
