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
所有草稿存放在 `015_Write/Draft/`，檔名格式：`YYYYMMDD_[主題關鍵字].md`
- 範例：`20260223_AI_Agent_產品探索.md`

### Frontmatter 結構
每個 Draft 檔的 YAML frontmatter 用於追蹤 pipeline 進度：

```yaml
---
pipeline_stage: "INTAKE"  # INTAKE | IDEATION | TITLE_HOOK | CP1 | FRAMEWORK | BODY_CLOSE | CP2 | POLISH | CP3 | PUBLISH | DONE
topic: "文章主題"
target_reader: ""  # 假想的具體寫作對象（一個人），留空表示不設定
scenario: ""  # knowledge_article | opinion | tutorial | case_study | trend_analysis | comparison | storytelling
core_claim: ""  # 這篇真正只想講的一句話，必須能直接成立
selected_cards: []
chosen_title: ""
chosen_hook: ""
chosen_framework: ""  # explosive_formula | direct_opinion | pastor | universal_writing
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

1. **設定假想讀者**：請用戶提供 **1 位具體的寫作對象**（例如：「剛轉職的 PM 朋友小王」「三年經驗的後端工程師」「我老闆」）。
   - 目的：心裡有一個具體的人，能讓文章切入角度更深、語氣更精準，避免寫出「對所有人說話＝對沒有人說話」的空泛文章。
   - **這不是要讓文章去跟該對象互動**，文章的本質和形式不變，只是寫作時心裡假想「這篇是寫給他/她看的」。
   - 如果用戶表示沒有特定對象，就跳過此步，`target_reader` 留空即可。
2. **確認主題**：如果用戶沒有明確主題，引導用戶釐清想寫什麼
3. **搜集卡片素材**：呼叫 `gather-cards` skill，給定主題搜尋知識庫
4. **確認寫作情境**：參考 `W0_02_SevenScenarios.prompt.md`，問用戶這篇文章屬於哪種情境：
   - 知識文（knowledge_article）
   - 觀點文（opinion）
   - 教學文（tutorial）
   - 案例分析（case_study）
   - 趨勢分析（trend_analysis）
   - 比較文（comparison）
   - 故事型（storytelling）
5. **先寫一句主張**：在進入發想前，先用一句話寫下 `core_claim`
   - 格式建議：`我真正想講的是：______`
   - 這句話必須直接、可反駁、不可同時包 2 個以上主張
   - 如果是觀點文，後面所有卡片都只允許服務這一句
6. **建立 Draft 檔**：在 `015_Write/Draft/` 建立新的 `.md` 檔，寫入 frontmatter（含 `target_reader`、`core_claim`）和 gather-cards 的結果

**產出**：Draft 檔建立，含 frontmatter + `## 原始素材`（gather-cards 結果）
**更新**：`pipeline_stage: "INTAKE"` → `"IDEATION"`

---

### Step 2: IDEATION（發想）
**模式**：全自動

> 💡 若有設定 `target_reader`，以下發想過程應帶入「這個人會在意什麼？什麼角度對他最有感？」的思維，讓素材篩選和觀點深化更聚焦。

1. **卡片素材整理**：使用 `W2_01_CardWeaver.prompt.md` 先淘汰，再選卡，不要預設每張卡都要進文章
   - 觀點文 / 趨勢分析：正文必用卡最多 4 張
   - 知識文 / 教學文 / 比較文：正文必用卡最多 5 張
   - 案例分析 / 故事型：正文必用卡最多 3 張，場景敘事優先
   - 超出的卡片一律列入「備用卡」或「淘汰卡」，不要硬塞
2. **價值維度發想**：參考 `W2_05_FourValues.prompt.md` 的 4 種價值（教育、啟發、共感、娛樂），但一次只選 1-2 個主值
   - 觀點文預設：`教育 + 啟發`
   - `共感` 只能當輔助，不能當主軸
   - `娛樂` 不能作為技術 / 觀點文主值
3. **乾貨維度發想**：參考 `W2_04_ThreeDryGoods.prompt.md`，從知識、經驗、框架三個維度發想素材
4. **觀點深化**：依現況選一個 prompt 深化觀點
   - 沒有具體故事 → `W2_06`（niche down 到真實故事再登高提煉）
   - 問題角度太模糊 → `W2_07`（加關鍵字讓問題可回答）
   - 有草稿但太空洞 → `W2_08`（12 維度橫向擴充）
   - 有材料但缺新觀點 → `W2_09`（五種視角重新發想）
   - 有觀點但論述不深 → `W2_10`（七大心智模型強化邏輯）

5. **主軸檢查**：用下面 3 題檢查文章是否開始發散
   - 如果砍掉 2 張卡，`core_claim` 還成立嗎？
   - 哪一段只是「順手想到」但不支撐主張？
   - 哪一段偏向感想抒發，但沒有新增判斷或資訊？

**產出**：在 Draft 檔追加 `## 素材地圖`（CardWeaver 結果）和 `## 發想筆記`
**更新**：`pipeline_stage: "IDEATION"` → `"TITLE_HOOK"`

---

### Step 3: TITLE+HOOK（標題與鉤子）
**模式**：全自動

1. **直白標題優先**：使用 `W3_01_ExplosiveTitle.prompt.md` 時，以「直白陳列法 / 一句話法 / 超具體」為主
   - 觀點文至少 70% 選項要是直接型標題
   - 只允許 1-2 個張力型標題作對照，不要整組都在追求反差
2. **超具體標題 × 3**：使用 `W3_02_UltraSpecificTitle.prompt.md` 補足具體版本
3. **鉤子 × 6**：使用 `W4_01_HookWriter.prompt.md` 為最合適的 2 個標題各生成 3 個鉤子
   - 以「真實經驗切入 / 問題拆解 / 明確觀察」為主
   - 不要把鉤子寫成價值承諾廣告
4. **整理選項**：將所有標題和鉤子整理成清晰的選項列表

**產出**：在 Draft 檔追加 `## 標題鉤子選項`
**更新**：`pipeline_stage: "TITLE_HOOK"` → `"CP1"`

---

### 【檢查點 1】選標題 + 鉤子 + 確認角度
**模式**：人工決策（~2 分鐘）

**暫停並向用戶呈現**：
1. 6-8 個標題選項（直接型優先）
2. 6 個鉤子選項（前 2 標題 × 3 鉤子）
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

1. **推薦框架**：根據寫作情境（scenario），參考 `W5_01_FrameworkSelector.prompt.md` 推薦合適的框架：
   - 知識文/教學文 → 萬能寫作法（`W5_03_UniversalWriting.prompt.md`）
   - 觀點文/趨勢分析 → 直接觀點框架（`W5_04_DirectOpinionWriting.prompt.md`）
   - 案例分析/故事型 → 爆文公式（`W5_02_ExplosiveTemplate.prompt.md`）
   - 比較文 → PASTOR 框架
2. **觀點文特殊規則**：
   - 開頭 3 段內必須明講 `core_claim`
   - 主體最多 3 個支撐段，不做 5-7 點大綱
   - 每個支撐段最多吃 1-2 張卡
   - 沒有增加判斷的感想段落直接刪掉
3. **用戶確認**：展示推薦框架和理由，讓用戶確認或更換

**產出**：確認文章框架
**更新**：記錄 `chosen_framework`，`pipeline_stage: "FRAMEWORK"` → `"BODY_CLOSE"`

---

### Step 5: BODY+CLOSE（主體 + 收尾）
**模式**：全自動

1. **主體撰寫**：根據選定的框架，使用對應的 W5 prompt 撰寫文章主體
   - 只嵌入正文必用卡，不要試圖把備用卡也寫進去
   - 優先寫清楚主張、判斷、因果，不優先追求段落戲劇性
   - 用選定的標題和鉤子作為開頭
2. **收尾撰寫**：
   - 觀點文 / 趨勢分析：使用 `W6_02_DirectClose.prompt.md`
   - 其他類型：可沿用 `W6_01_GoldenQuote.prompt.md`
   - 收尾要做的是收斂，不是硬做金句
   - 產出 2 個版本即可：一個更直接，一個更保留

**產出**：在 Draft 檔追加 `## Draft v1`（完整文章草稿）
**更新**：`pipeline_stage: "BODY_CLOSE"` → `"CP2"`，`status: "reviewing"`

---

### 【檢查點 2】審閱完整草稿
**模式**：人工審閱（~5 分鐘）

**暫停並向用戶呈現**：
1. 完整的 Draft v1
2. 文章結構摘要（段落數、字數、使用的卡片）
3. 收尾版本選項
4. 主軸檢查：
   - 哪一段最像在「硬塞卡片」
   - 哪一段最像「有感但不直接」
   - 哪一段刪掉後反而更集中

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

1. **直接性修稿**：先使用 `W7_07_DirectnessPass.prompt.md`
   - 先砍掉空話、抒情、鋪墊、討好語氣
2. **人味化**：再使用 `W7_01_Humanizer.prompt.md`
   - 只補經驗感，不補文采
3. **減少冗贅**：使用 `W7_02_NotButReducer.prompt.md` 精簡文字
4. **風格轉換**：
   - 觀點文 / 趨勢分析：預設跳過 `W7_05_StyleTransferMyself.prompt.md`
   - 只有在文章已經太乾、太硬時才補做一次
5. **符號排版**：使用 `W7_formatting.prompt.md` 調整標題與段落符號格式
6. **事實查證**：呼叫 `fact-check` skill 查證文章中的具體細節

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
2. **圖片生成**：使用 `W8_01_ImagePrompt.prompt.md` 生成配圖 prompt
3. **移動檔案**：將最終版本移到 `015_Write/Publish/`，檔名格式：`YYYYMMDD_【標題】.md`

**產出**：
- `015_Write/Publish/YYYYMMDD_【標題】.md` — 最終發佈版
- `010_CardNotes/02_Cards/` — 新萃取的卡片（如有）
- `015_Write/Draft/` 中的原始 Draft 檔保留作為歷史紀錄

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

## 異常處理

| 情境 | 處理方式 |
|------|----------|
| `gather-cards` 找不到任何相關卡片 | 告知用戶知識庫中無相關素材，詢問是否（a）無卡片繼續寫、（b）先用 `scout-news` 搜集資料再回來、（c）換主題 |
| 用戶在 CP1 拒絕全部標題/鉤子 | 詢問用戶偏好方向，重新執行 Step 3（不重複 Step 1-2） |
| 用戶在 CP2 要求大幅重寫 | 將回饋記錄到 Draft 檔，回退到 Step 5 重新撰寫主體，保留原始 Draft v1 作為參考 |
| 用戶在 CP3 退回 | 回退到 Step 6 重新打磨，或根據用戶指示回退到更早的階段 |
| `fact-check` 發現重大事實錯誤 | 在 CP3 呈現查證報告時標記，等用戶決定是否修正後再發佈 |

---

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
- ✅ 最終版本已移到 `015_Write/Publish/`
