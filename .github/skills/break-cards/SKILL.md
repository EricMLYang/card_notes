---
name: break-cards
description: 先將長文或筆記拆成候選卡片（lite），再呼叫 refine-cards 精煉成正式卡草稿。適用於 005_PARA/01_Projects/ 與 005_PARA/02_Areas/ 內用戶指定範圍的檔案，或檔名包含 WaitBreakCard 的檔案。用戶說「幫我拆解文章」「拆成卡片」時觸發。
---

# Skill: Break Cards（Lite 候選拆解 → 呼叫 Refine）

## 目標
先把長文章或筆記拆成候選卡片，保留高潛力節點，再呼叫 `refine-cards` 將候選卡精煉為正式卡草稿。  
**本 skill 本身不直接落檔正式卡**，而是在 refine 完成後先向 user 確認。只有 user 確認後，才執行實際分類、寫檔、更新索引與原文改名。

## 適用範圍
- **主要來源**：
  - `005_PARA/01_Projects/`
  - `005_PARA/02_Areas/`
- **待處理標記**：檔名包含 `WaitBreakCard`
- **使用時機**：當 user 明確指出要拆解的文章、筆記、檔案或資料夾範圍時

## 個人化偏好來源
- 讀取檔案：`000_MyContext/break_cards_profile.md`
- 用途：
  - 在 lite 階段作為「注意力排序」參考
  - 在 refine 階段作為「同級候選卡取捨與知識鉤子方向」參考
- **絕對限制**：
  - 個人偏好只能影響排序與優先級
  - **絕不允許降低收錄門檻**
  - **不得因個人偏好忽略明顯有機制、邊界、反例、橋接價值或追蹤價值的候選卡**
- 若 `000_MyContext/break_cards_profile.md` 缺失，僅使用本 skill 的通用規則

## 核心原則

### 1. 先做 Lite，不過早過濾
第一輪目標是提高召回率，不是一步到位定稿。  
允許保留以下候選節點：
- 高訊號洞見
- 橋接節點
- 反例節點
- 概念澄清節點
- 值得持續追蹤的問題

### 2. 一卡一事
每張候選卡只保留一個概念、一個判斷、一個問題，或一個結構性模式。

### 3. 不腦補
- ❌ 不補新事實
- ❌ 不補作者沒說的案例
- 若有合理整合，明確標記 `[Inference]`

### 4. 路徑一致
所有後續正式卡與索引更新，統一使用以下路徑：
- 索引目錄：`010_CardNotes/01_Index/`
- 正式卡目錄：`010_CardNotes/02_Cards/{分類資料夾}/`（按索引對應的分類資料夾存放，如 `03_ai_applications_and_productization/`、`01_mental_models/` 等）

## 執行流程（強制順序）

### Step 0: 檢查是否已拆解（避免重複處理）
執行任務前，先使用 `check_breadcards.py` 檢查檔案狀態：

```bash
python .github/skills/break-cards/check_breadcards.py <檔案路徑>
```

**根據返回值決定動作：**
- **Exit Code 0**（已有 BreadCards）：
  - ✓ 檔案已經完成 break-cards 處理
  - **直接跳過拆解，呼叫 refine-cards skill**
  - 將檢測到的 BreadCards 內容傳給 refine-cards

- **Exit Code 2**（未拆解）：
  - ✓ 檔案尚未拆解，繼續執行下方 Step 1-6

- **Exit Code 1 或 3**（錯誤）：
  - ❌ 檔案不存在或讀取失敗
  - 告知 user 並終止

### Step 1: 閱讀全文
先讀完整篇文章或筆記。

### Step 2: 提取主脈絡與個人映射
用 4–8 行寫出：
1. **論證骨架**：作者怎麼推論到結論，挑戰了什麼預設
2. **個人化映射**：文章的核心邏輯，如何補充、挑戰或顛覆 `000_MyContext/break_cards_profile.md` 中的長期視角

### Step 3: 產出 Lite 候選卡
列出 5–12 張候選卡，每張卡先標記：
- `Core`
- `Support`
- `Question`

**保留原則**：
- 不要求一開始就非常完美
- 只要具有明確主張、機制、邊界、橋接潛力、反例價值或問題價值，就可保留為候選卡

### Step 4: 呼叫 `refine-cards`
將 Step 3 的候選卡交給 `refine-cards` skill 精煉。  
refine 需完成：
- 去重
- 合併
- 篩選
- 正式卡草稿化
- 分類建議
- 目標檔名建議
- 目標路徑建議

### Step 5: 顯示 refine 結果並向 user 確認
refine 完成後，**不得直接寫入正式卡檔案**。  
必須先向 user 顯示：
- KEEP / WEAK KEEP / SKIP 概況
- 正式卡草稿
- 每張卡的分類建議
- 每張卡的目標檔名與目標路徑

並明確詢問 user：
- 是否要正式寫入 `010_CardNotes/02_Cards/{分類資料夾}/`
- 是否要更新 `010_CardNotes/01_Index/`
- 是否要將原文改名為 `CoreNote`

### Step 6: 只有在 user 明確確認後才執行落檔
若 user 明確確認，才執行：
1. 將正式卡寫入 `010_CardNotes/02_Cards/{分類資料夾}/`（根據索引對應的分類資料夾）
2. 依分類更新 `010_CardNotes/01_Index/` 對應索引檔
3. 將原始來源檔案改名為 `YYYYMMDD_CoreNote_原本檔名.md`

若 user 未確認：
- 只輸出 refine 結果到對話
- **不修改原文**
- **不落檔正式卡**
- **不更新索引**

## Lite 候選卡寫作規格
每張候選卡必須包含：

```text
序號 N
- 候選標題：[一句話，先求清楚，不求最終命名]
- 分級：[Core / Support / Question]
- 類型：[Principle / Pattern / Heuristic / Warning / Question]
- 核心內容（40–180 字）：[這張候選卡到底在說什麼]
- 保留理由（1 句）：[為什麼值得進 refine]
- 待補強處（可選）：[還缺什麼邊界、條件、反例]
- 初步知識鉤子：[可連到哪些概念、框架、決策或反例]
```

## 類型清單（Lite 階段簡化）

| 類型 | 說明 |
|------|------|
| **Principle** | 底層規則、穩定原理 |
| **Pattern** | 反覆出現的結構或趨勢 |
| **Heuristic** | 可重複套用的判斷法 |
| **Warning** | 常見陷阱、反例、失效條件 |
| **Question** | 尚未定論但值得追蹤 |

## 輸出格式（Lite + Refine 前）

**重要**：以下內容必須 **append 到被拆解的原文檔案末尾**，而非單獨輸出到對話中。

```markdown
# BreadCards

## A. 主脈絡與個人映射
- [論證骨架]
- [作者挑戰的預設]
- [個人映射：對既有知識主軸的補充、修正或擴張]

## B. 候選卡（Lite）

序號 1
- 候選標題：
- 分級：
- 類型：
- 核心內容：
- 保留理由：
- 待補強處：
- 初步知識鉤子：

...

## C. 建議送 refine 的項目
- [列出最值得 refine 的序號]

## D. 呼叫 refine-cards
- [將上述候選卡交由 refine-cards 精煉]
```

## User 確認前禁止事項
- ❌ 不直接寫入 `010_CardNotes/02_Cards/`
- ❌ 不更新 `010_CardNotes/01_Index/`
- ❌ 不改名原始來源檔案
- ❌ 不覆蓋原文件

## User 確認後的落檔規則
若 user 確認，則：

### 正式卡落檔位置
- 目錄：`010_CardNotes/02_Cards/`

### 正式卡檔名格式
- `{分類前綴}{流水號}_{卡片標題}.md`
- 例：
  - `1-001_不要把個人偏好當過濾器_只能當排序器.md`
  - `4-012_Agent_Workflow_先求召回率_再求精煉率.md`

### 索引更新位置
- 目錄：`010_CardNotes/01_Index/`

### 原文改名規則
- 格式：`YYYYMMDD_CoreNote_原本檔名.md`
- 若原檔名已有日期前綴，保留原日期
- 若原檔名沒有日期，使用當天日期

### 寫入順序
1. 寫正式卡
2. 更新索引
3. 改名原文
