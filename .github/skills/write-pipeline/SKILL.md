---
name: write-pipeline
description: 寫作自動化主控台，串接 W0-W8 所有環節，用 Draft 檔 YAML frontmatter 追蹤進度，自動執行各段並在 3 個檢查點暫停等待人工決策。適用於用戶說「寫新文章」「開始寫作」「help me write about...」時。Use when user wants to start or continue the automated writing pipeline.
---

# Skill: Write Pipeline（寫作自動化主控台）

## 目標
主控整個 W1-W8 寫作 pipeline，自動串接各階段，在 3 個人工檢查點暫停等待決策，將手動操作從 8+ 次降為 3 個決策點。同時讓卡片系統成為文章的第一手素材來源。

## Pipeline 總覽

```
Step 1 INTAKE     → Step 2 IDEATION  → Step 3 TITLE+HOOK
                                              ↓
                                      【檢查點 1】選標題+鉤子
                                              ↓
Step 4 FRAMEWORK  → Step 5 BODY+CLOSE
                                              ↓
                                      【檢查點 2】審閱草稿
                                              ↓
                    Step 6 POLISH
                                              ↓
                                      【檢查點 3】最終確認
                                              ↓
                    Step 7 PUBLISH
```

## Draft 檔管理

### 檔案位置
所有草稿存放在 `/004_1Draft/`，檔名格式：`[主題關鍵字].md`

### Frontmatter 結構
每個 Draft 檔的 YAML frontmatter 用於追蹤 pipeline 進度：

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

### 進度更新規則
- 每完成一個 Step，立即更新 `pipeline_stage` 和 `last_updated`
- 每個 Step 的產出追加到 Draft 檔對應段落
- 人工檢查點時更新 `status` 為 `reviewing`

## 執行流程（7 個 Step + 3 個檢查點）

### Step 1: INTAKE（進場）
**模式**：半自動

1. **確認主題**：如果用戶沒有明確主題，引導用戶釐清想寫什麼
2. **搜集卡片素材**：呼叫 `gather-cards` skill，給定主題搜尋知識庫
3. **確認寫作情境**：參考 `W0_情境_7大寫作情境.prompt.md`，問用戶這篇文章屬於哪種情境：
   - 知識文（knowledge_article）
   - 觀點文（opinion）
   - 教學文（tutorial）
   - 案例分析（case_study）
   - 趨勢分析（trend_analysis）
   - 比較文（comparison）
   - 故事型（storytelling）
4. **建立 Draft 檔**：在 `/004_1Draft/` 建立新的 `.md` 檔，寫入 frontmatter 和 gather-cards 的結果

**產出**：Draft 檔建立，含 frontmatter + `## 原始素材`（gather-cards 結果）
**更新**：`pipeline_stage: "INTAKE"` → `"IDEATION"`

---

### Step 2: IDEATION（發想）
**模式**：全自動

1. **卡片素材整理**：使用 `W2_CardWeaver.prompt.md` 將搜集到的卡片按文章角色組織
2. **價值維度發想**：參考 `W2發想_料感與4種價值.prompt.md` 的 4 種價值（教育、啟發、共感、娛樂），確定文章的價值定位
3. **乾貨維度發想**：參考 `W2發想_三大乾貨_知識_經驗_框架.prompt.md`，從知識、經驗、框架三個維度發想素材
4. **觀點深化**：參考 `W2_2發想` 系列 prompt，選擇合適的思考方式深化觀點

**產出**：在 Draft 檔追加 `## 素材地圖`（CardWeaver 結果）和 `## 發想筆記`
**更新**：`pipeline_stage: "IDEATION"` → `"TITLE_HOOK"`

---

### Step 3: TITLE+HOOK（標題與鉤子）
**模式**：全自動

1. **爆款標題 × 5**：使用 `W3_標題_爆款文標題大師.prompt.md` 生成 5 個爆款標題
2. **超具體標題 × 5**：使用 `W3_標題_超具體標題大師.prompt.md` 生成 5 個超具體標題
3. **鉤子 × 9**：使用 `W4_前言_鉤子寫作機.prompt.md` 為排名前 3 的標題各生成 3 個鉤子
4. **整理選項**：將所有標題和鉤子整理成清晰的選項列表

**產出**：在 Draft 檔追加 `## 標題鉤子選項`
**更新**：`pipeline_stage: "TITLE_HOOK"` → `"CP1"`

---

### 【檢查點 1】選標題 + 鉤子 + 確認角度
**模式**：人工決策（~2 分鐘）

**暫停並向用戶呈現**：
1. 10 個標題選項（5 爆款 + 5 超具體）
2. 9 個鉤子選項（前 3 標題 × 3 鉤子）
3. 文章角度摘要

**等待用戶決定**：
- 選擇或修改標題
- 選擇或修改鉤子
- 確認或調整文章角度

**提示用戶**：「如果需要更多引導，可以切換到 WritingCoach chatmode 進行互動式討論。」

**更新**：記錄 `chosen_title`、`chosen_hook`，`pipeline_stage: "CP1"` → `"FRAMEWORK"`

---

### Step 4: FRAMEWORK（選框架）
**模式**：半自動

1. **推薦框架**：根據寫作情境（scenario），參考 `W5_主體_決定文章框架.prompt.md` 推薦合適的框架：
   - 知識文/教學文 → 萬能寫作法（`W5_主體_萬能寫作法教練.prompt.md`）
   - 觀點文/趨勢分析 → 觀點型框架
   - 案例分析/故事型 → 爆文公式（`W5_主體_爆文模板.prompt.md`）
   - 比較文 → PASTOR 框架
2. **用戶確認**：展示推薦框架和理由，讓用戶確認或更換

**產出**：確認文章框架
**更新**：記錄 `chosen_framework`，`pipeline_stage: "FRAMEWORK"` → `"BODY_CLOSE"`

---

### Step 5: BODY+CLOSE（主體 + 收尾）
**模式**：全自動

1. **主體撰寫**：根據選定的框架，使用對應的 W5 prompt 撰寫文章主體
   - 嵌入 CardWeaver 整理好的卡片素材
   - 確保框架、論據、類比、案例自然融入
   - 用選定的標題和鉤子作為開頭
2. **收尾撰寫**：使用 `W6_收尾_金句大師.prompt.md` 撰寫文章收尾
   - 參考 CardWeaver 的 (e) 收尾素材
   - 產出 2-3 個收尾版本供後續選擇

**產出**：在 Draft 檔追加 `## Draft v1`（完整文章草稿）
**更新**：`pipeline_stage: "BODY_CLOSE"` → `"CP2"`，`status: "reviewing"`

---

### 【檢查點 2】審閱完整草稿
**模式**：人工審閱（~5 分鐘）

**暫停並向用戶呈現**：
1. 完整的 Draft v1
2. 文章結構摘要（段落數、字數、使用的卡片）
3. 收尾版本選項

**等待用戶回饋**：
- 整體方向是否正確
- 哪些段落需要修改
- 選擇收尾版本
- 任何其他修改意見

**提示用戶**：「如果需要詳細的文字回饋，可以切換到 Editor chatmode 讓責任編輯審閱。」

**更新**：根據回饋修改 Draft v1，`pipeline_stage: "CP2"` → `"POLISH"`，`status: "polishing"`

---

### Step 6: POLISH（打磨）
**模式**：全自動

1. **風格轉換**：使用 `W7_補強_風格轉換_加恩版.prompt.md` 調整文章風格
2. **人味化**：使用 `W7_補強_人味轉換器.prompt.md` 增加人味，減少 AI 感
3. **減少冗贅**：使用 `W7_補強_不是而是減少器.prompt.md` 精簡文字
4. **事實查證**：呼叫 `fact-check` skill 查證文章中的具體細節

**產出**：在 Draft 檔追加 `## Draft v2`（打磨後的文章）+ `## 查證報告`
**更新**：`pipeline_stage: "POLISH"` → `"CP3"`

---

### 【檢查點 3】最終確認
**模式**：人工確認（~1 分鐘）

**暫停並向用戶呈現**：
1. Draft v2（打磨後的完整文章）
2. 與 Draft v1 的主要差異摘要
3. 查證報告

**等待用戶確認**：
- 確認發佈 / 需要再修改 / 退回重寫

**更新**：`pipeline_stage: "CP3"` → `"PUBLISH"`

---

### Step 7: PUBLISH（發佈）
**模式**：全自動

1. **排版**：呼叫 `format-article` skill 進行社群媒體排版
2. **圖片生成**：使用 `W8_點綴_圖片生成.prompt.md` 生成配圖 prompt
3. **移動檔案**：將最終版本移到 `/004_2Express/`，檔名格式：`【標題】.md`
4. **回饋卡片**：呼叫 `break-cards` skill，從文章中萃取新的知識卡片回饋到卡片系統
5. **更新索引**：如果產生了新卡片，更新對應的索引檔

**產出**：
- `/004_2Express/【標題】.md` — 最終發佈版
- `/003_2Cards/` — 新萃取的卡片（如有）
- `/004_1Draft/` 中的原始 Draft 檔保留作為歷史紀錄

**更新**：`pipeline_stage: "PUBLISH"` → `"DONE"`，`status: "published"`

## 中斷與恢復

### 中斷處理
- Pipeline 可在任何 Step 或檢查點中斷
- 所有進度都記錄在 Draft 檔的 frontmatter 中
- 中斷時不需要額外操作，frontmatter 已保存當前狀態

### 恢復方式
- 使用 `resume-draft` skill 查看所有進行中的草稿
- 選擇草稿後，`write-pipeline` 自動從 `pipeline_stage` 記錄的階段繼續
- 恢復時會先讀取 Draft 檔的完整內容，重建上下文

## 操作指引

**觸發條件**：
- 用戶說「寫新文章」「開始寫作」
- 用戶說「help me write about...」「write an article about...」
- 用戶說「啟動 pipeline」「開始 pipeline」

**恢復觸發**：
- 用戶說「繼續寫」「繼續 pipeline」
- 用戶選擇了 `resume-draft` 列出的草稿

## 禁止事項

- ❌ 不要跳過檢查點，即使用戶催促也要暫停等待決策
- ❌ 不要在全自動階段暫停詢問不必要的問題
- ❌ 不要覆蓋 Draft 檔中已完成階段的內容（只追加新段落）
- ❌ 不要在 frontmatter 中記錄與 pipeline 無關的資訊

## 品質檢查

Pipeline 完成後確認：
- ✅ Draft 檔的 frontmatter 完整且準確
- ✅ 三個檢查點都有人工介入
- ✅ 卡片素材有自然融入文章（不是生硬引用）
- ✅ 最終版本已移到 `/004_2Express/`
- ✅ `break-cards` 已執行，新知識回饋到卡片系統
