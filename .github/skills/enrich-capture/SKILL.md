---
name: enrich-capture
description: 處理 003_Capture 中的檔案：自動加上標頭元資料並分類移動到 005_PARA 對應的 inbox。適用於用戶說「處理 Capture」「整理捕獲檔案」「enrich capture」時。Use when user wants to enrich capture files with metadata and move to PARA structure.
---

# Skill: Enrich Capture（捕獲檔案強化與分類）

## 目標
一鍵處理 `003_Capture/` 中的檔案，自動完成「加標頭元資料 → 智能分類 → 移動到 005_PARA 對應 inbox」的流程，讓捕獲的內容快速進入 PARA 體系。

## Pipeline 總覽

```
[Step 1] SCAN       掃描 Capture 列出待處理檔案
[Step 2] SELECT     用戶選擇要處理的檔案
[Step 3] ANALYZE    分析檔案內容與最適合的分類
         ↓
【檢查點】用戶確認分類建議
         ↓
[Step 4] ENRICH     在檔案最上方加入標頭元資料
[Step 5] MOVE       移動到 005_PARA 對應資料夾的 inbox
         ↓
輸出處理摘要
```

## 執行流程（5 個 Step + 1 個檢查點）

### Step 1: SCAN（掃描）
**模式**：全自動

1. 掃描 `003_Capture/` 中所有 `.md` 檔案
2. 對每個檔案讀取前 200 字作為預覽
3. 輸出待處理清單

**輸出格式**：
```markdown
## Capture 待處理清單

| # | 檔名 | 預覽 |
|---|------|------|
| 1 | [filename.md] | [前 200 字...] |
| 2 | [filename.md] | [前 200 字...] |
```

**若 Capture 為空**：輸出「003_Capture 目前沒有待處理的檔案。」並結束。

---

### Step 2: SELECT（選擇）
**模式**：人工

讓用戶選擇要處理的檔案：
- 輸入編號（如 `1, 3, 5`）處理特定檔案
- 輸入「全部」處理所有檔案
- 可一次選多個，pipeline 會依序處理每個檔案

---

### Step 3: ANALYZE（分析）
**模式**：全自動

對每個選中的檔案：
1. 讀取完整檔案內容（前 3000 字）
2. 分析內容主題與性質
3. 根據 AGENTS.md 中的分類規則，判斷最適合的 005_PARA 分類

**分類判斷依據**（參考 AGENTS.md）：

#### 02_Areas 子分類
- `AI_Software_Data/AI知識管理和寫作/inbox/` - Zettelkasten、PKM、Second Brain、AI 輔助寫作、Build in Public
- `AI_Software_Data/Agent/inbox/` - AI Agent 設計、Agentic 工作流、MCP、評估框架
- `AI_Software_Data/AI_Coding/01_inbox/` - AI 輔助 Coding 實踐、vibe coding、AI 寫程式的架構控制、AI 時代的 code review
- `AI_Software_Data/AI_Trend/inbox/` - AI 產業趨勢、模型發布、策略觀察
- `AI_Software_Data/Software_Engineering/01_inbox/` - 傳統軟體工程、框架架構、部署、資安、權限管理
- `AI_Software_Data/BussinessDataScience/inbox/` - 商業資料分析、資料工程
- `AI_Software_Data/Databricks/inbox/` - Databricks 平台操作與架構
- `Domains_and_Industries/IoT_Domain/inbox/` - IoT、車載、Beacon、數位看板
- `Product_Business_Strategy/Product_Business/inbox/` - 產品管理、商業模式、策略
- `AI_Software_Data/AWS/inbox/` 或 `Azure/inbox/` - 雲端服務實踐與架構

#### 03_Resources 
- `03_Resources/` - 參考資料或一次性輸入（不是持續維護的工作域）

**判斷原則**：
- 若此主題是**持續在做、需長期維護**的工作域 → `02_Areas`
- 若只是參考資料或一次性輸入 → `03_Resources`

---

### 【檢查點】確認分類建議
**模式**：人工

向用戶呈現每個檔案的分析結果：

```markdown
## 分析結果

### 檔案：[filename.md]

**內容摘要**：
[3-5 行內容摘要]

**建議分類**：`005_PARA/02_Areas/AI_Software_Data/Agent/inbox/`

**分類理由**：
- 主題關鍵字：Agent、工作流、評估
- 符合 Area 定義：AI Agent 是持續學習與實踐的工作域
- 屬於 AI_Software_Data 大類下的 Agent 子類

**目標路徑**：`005_PARA/02_Areas/AI_Software_Data/Agent/inbox/[filename].md`
```

**用戶可以**：
- 確認建議（輸入「確認」或「OK」）
- 修改分類（輸入「改為 03_Resources」或指定完整路徑）
- 跳過此檔案（輸入「跳過」）

---

### Step 4: ENRICH（加標頭）
**模式**：全自動

在檔案**最上方**插入以下標頭元資料：

```markdown
---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: [今天日期 YYYY-MM-DD]
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
（原文內容從這裡開始）
```

**注意事項**：
- 如果檔案已有 YAML front matter，則將標頭放在 front matter 之後
- `last_review` 自動填入今天日期（格式：YYYY-MM-DD）
- `process_level` 預設為 `1`（找重點階段）
- 保留檔案原始內容不變

---

### Step 5: MOVE（移動）
**模式**：全自動

1. 確保目標路徑中的 `inbox/` 資料夾存在（不存在則自動建立）
2. 將檔案移動到目標路徑
3. 記錄移動結果

**目標路徑格式**：
- Area: `005_PARA/02_Areas/[大類]/[子類]/inbox/[filename].md`
- Resource: `005_PARA/03_Resources/[filename].md`
- Project: `005_PARA/01_Projects/[專案名]/inbox/[filename].md`（若用戶指定）

---

## 處理摘要

處理完成後輸出：

```markdown
## 處理完成摘要

✅ 已處理 [N] 個檔案

| 檔名 | 分類 | 目標路徑 | 狀態 |
|------|------|----------|------|
| [filename1.md] | Area/Agent | 005_PARA/02_Areas/.../inbox/ | ✅ 成功 |
| [filename2.md] | Resource | 005_PARA/03_Resources/ | ✅ 成功 |

---

**下一步建議**：
- 進入目標資料夾查看檔案
- 填寫「[重點]」區塊（process_level 1）
- 需要時可進一步撰寫「[摘要]」與「[詮釋]」
```

---

## 觸發關鍵詞

- 「處理 Capture」
- 「整理捕獲檔案」
- 「enrich capture」
- 「加標頭並分類」
- 「把 Capture 移到 PARA」

---

## 依賴

- `AGENTS.md` - 分類規則與 PARA 結構定義
- `005_PARA/` 目錄結構

---

## 注意事項

1. **檔名規範檢查**：移動後的檔案應符合目標資料夾的檔名規範（如需要日期前綴）
2. **自動建立 inbox**：若目標分類沒有 `inbox/` 資料夾，自動建立
3. **衝突處理**：若目標路徑已有同名檔案，提示用戶重新命名或覆蓋
4. **批次處理**：支援一次處理多個檔案，但每個檔案的分類需單獨確認
5. **保留彈性**：用戶可隨時修改 AI 建議的分類路徑

---

## 範例執行

```
User: 處理 Capture