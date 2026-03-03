---
name: archive-article
description: 依固定優先順序歸檔文章（Projects → Area → Resource → Archive），並處理電子書同步累積。適用於用戶說「幫我歸檔文章」「整理這篇到哪裡」「用這新 skills 歸檔」時。Use when user asks to archive an article with priority routing and ebook accumulation.
---

# Skill: Archive Article（文章歸檔）

## 目標
將文章依固定優先順序歸檔到 PARA 對應位置，並在非 Archive 的情境下，若判定為電子書內容則同步累積到 `/005_2Ebook/` 的同一本書筆記檔。

## 歸檔優先順序（強制）
1. `Projects`（`/001_1Projects/`）
2. `Area`（`/001_2Area/`）
3. `Resource`（`/005_1Resource/`）
4. `Archive`（`/006Archive/`）

> 同一篇原文只選一個「主歸檔位置」，嚴格依上述順序判斷；只有在前一層不成立時，才往下一層。

## 電子書同步規則（強制）
- 若文章屬於電子書內容（有明確書名、章節、書摘脈絡），且主歸檔位置是 `Projects` / `Area` / `Resource`：
  - 除主歸檔外，**同步**更新 `/005_2Ebook/[書名].md`。
  - 若該書筆記檔不存在則建立，存在則追加新章節內容。
- 若主歸檔位置是 `Archive`：
  - 不做電子書同步。

## 執行流程

### Step 1: 讀取與判斷
1. 讀取原文標題、摘要、關鍵詞與上下文。
2. 判斷是否命中 `Projects`：與進行中專案有明確交付、里程碑、需求依賴。
3. 若未命中，再判斷 `Area`：屬於需長期維護的責任領域。
4. 若未命中，再判斷 `Resource`：具參考價值但無專案/領域直接責任。
5. 以上皆不命中則歸檔到 `Archive`。

### Step 2: 主歸檔執行
1. 移動原文到主歸檔目錄。
2. 若主歸檔是 `Resource`，選定子分類（如 `AI`、`LLM_Tools`、`Dev_Engineering` 等）。
3. 保留原檔名，不主動改名（除非用戶要求）。

### Step 3: 電子書同步
1. 偵測是否為電子書內容（書名、章節、書摘語境）。
2. 若符合且主歸檔不是 `Archive`：
   - 更新 `/005_2Ebook/[書名].md`，追加：來源檔名、章節重點、引用摘要。
3. 若不符合或主歸檔是 `Archive`：略過。

### Step 4: 用戶確認
輸出歸檔決策與理由，請用戶確認後執行最終移動。

## 輸出格式

```markdown
## 歸檔建議
- 原文：[[filename.md]]
- 主歸檔：[/001_1Projects/... | /001_2Area/... | /005_1Resource/... | /006Archive/...]
- 判斷理由：[1-2 句]
- 電子書同步：[是/否]
- 電子書目標（若是）：[/005_2Ebook/書名.md]

請回覆：
- 「確認」：執行歸檔
- 或「改到 ...」：指定新路徑
```

## 操作指引

**觸發條件**：
- 用戶說「幫我歸檔文章」
- 用戶說「整理這篇到哪裡」
- 用戶說「歸檔這篇」
- 用戶說「用這新 skills 歸檔」
- 用戶說「archive this article」

**與其他流程整合**：
- `process-inbox` 在 Step 7（ARCHIVE）時，應呼叫本 skill。
- 其他需要歸檔的流程，統一使用本 skill 決策與執行。

## 禁止事項
- ❌ 不可跳過優先順序直接歸到 `Archive`（除非前三者皆不符合）
- ❌ 未經確認不可刪除原文
- ❌ 主歸檔為 `Archive` 時不可同步到 `/005_2Ebook/`
- ❌ 不可同時指定多個主歸檔位置
- ❌ 不可覆蓋已存在的電子書筆記內容（只能追加或合併）
