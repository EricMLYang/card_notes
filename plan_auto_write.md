# 自動化寫作流程 Pipeline 設計計畫

## Context

目前的寫作系統有完整的 W0-W8 prompts、6 個 skills、10 個 chatmodes，但每個環節都是**手動獨立觸發**，需要人工在各階段之間複製貼上、串接結果。同時，知識庫中 207+ 張卡片是最有價值的寫作素材，但目前沒有機制能在寫作時自動調用這些卡片。

**目標**：建立自動化 pipeline，將人工操作從 8+ 次手動觸發降為 3 個決策檢查點，同時讓卡片系統成為文章的第一手素材來源。

---

## 架構總覽

```
觸發                     自動化 Pipeline                         產出
────                     ──────────                              ────
主題/問題          →  [gather-cards 搜集素材]
                      [W2 發想 + 素材整理]        ← 全自動
                      [W3 標題 × 10]
                      [W4 鉤子 × 9]
                            |
                   ──→ 【檢查點 1】選標題+鉤子+角度  ← 人工決策 (~2 min)
                            |
                      [W5 選框架+寫主體]
                      [W6 收尾+金句]               ← 全自動
                            |
                   ──→ 【檢查點 2】審閱完整草稿      ← 人工審閱 (~5 min)
                            |
                      [W7 風格轉換+人味化]
                      [fact-check 查證]             ← 全自動
                            |
                   ──→ 【檢查點 3】最終確認          ← 人工確認 (~1 min)
                            |
                      [format-article 排版]
                      [W8 圖片生成]                 ← 全自動
                      [break-cards 回饋卡片]
                            ↓
                      004_2Express/ 發佈
```

---

## 需要建立的新檔案（共 5 個）

### 1. `gather-cards` skill — 卡片素材搜集器
**檔案**: `.github/skills/gather-cards/SKILL.md`

**目的**: 給定主題，自動搜尋 `/003_2Cards/` 和 `/003_1CardsIndex/` 找出 5-15 張最相關的卡片，按文章角色分類輸出。

**執行流程**:
1. 解析主題為關鍵概念 + 相關關鍵字
2. 搜尋 14 個索引檔的段落標題，定位相關分類
3. 讀取該分類卡片，按關鍵字重疊度和概念相關性排序
4. 跨分類搜尋意外連結（最有價值的素材）
5. 輸出：核心卡片、跨域卡片、素材缺口

**輸出格式**:
```markdown
## 核心卡片（直接相關）
1. [[卡片名]] - [角色: 框架/論據/類比/案例] - [關鍵摘錄]

## 跨域卡片（意外連結）
1. [[卡片名]] - [連結理由] - [關鍵摘錄]

## 素材缺口
- [缺少哪些主題的卡片，可能需要額外研究]
```

---

### 2. `write-pipeline` skill — 寫作主控台
**檔案**: `.github/skills/write-pipeline/SKILL.md`

**目的**: 主控整個 W1-W8 pipeline，用 Draft 檔案的 YAML frontmatter 追蹤進度，自動串接各段、在檢查點暫停等待人工決策。

**觸發**: 「寫新文章」「開始寫作」「help me write about...」

**核心邏輯 — 7 個 Step**:

| Step | 動作 | 模式 |
|------|------|------|
| 1. INTAKE | 問主題 → 呼叫 gather-cards → 問寫作情境（W0 七大情境）→ 建立 Draft 檔 | 半自動 |
| 2. IDEATION | 用 W2 發想（4 種價值 × 3 種乾貨）+ 卡片素材 → 寫入 `## 原始素材` | 全自動 |
| 3. TITLE+HOOK | W3 爆款標題 5 個 + W3 超具體標題 5 個 + W4 鉤子各 3 個 → 寫入 `## 標題鉤子選項` | 全自動 |
| **CP1** | **用戶選標題 + 鉤子 + 確認角度** | **人工** |
| 4. FRAMEWORK | 根據情境推薦 W5 框架（爆文公式/觀點型/PASTOR/萬能框架）→ 用戶確認 | 半自動 |
| 5. BODY+CLOSE | W5 主體撰寫（嵌入卡片素材）+ W6 收尾金句 → 寫入 `## Draft v1` | 全自動 |
| **CP2** | **用戶審閱草稿（可叫 Editor chatmode 協助）** | **人工** |
| 6. POLISH | W7 風格轉換 → W7 人味化 → fact-check → 寫入 `## Draft v2` | 全自動 |
| **CP3** | **用戶最終確認** | **人工** |
| 7. PUBLISH | format-article 排版 → W8 圖片 → 移到 004_2Express/ → break-cards 回饋新卡片 → 更新索引 | 全自動 |

**Draft 檔 frontmatter 結構**:
```yaml
---
pipeline_stage: "W5"
topic: "AI時代的認知競爭力"
scenario: "knowledge_article"
selected_cards: ["1-好策略的三層核心結構", "3-AI Agent 的本質"]
chosen_title: "..."
chosen_hook: "..."
chosen_framework: "explosive_formula"
created: 2026-02-20
last_updated: 2026-02-20
status: "drafting"  # drafting | reviewing | polishing | published
---
```

---

### 3. `resume-draft` skill — 草稿狀態管理器
**檔案**: `.github/skills/resume-draft/SKILL.md`

**目的**: 列出 `/004_1Draft/` 中所有進行中草稿的 pipeline 狀態，讓用戶可以快速恢復任一草稿的寫作進度。

**觸發**: 「我的草稿」「繼續寫作」「resume draft」

**執行流程**:
1. 掃描 `/004_1Draft/` 所有 `.md` 檔
2. 讀取 YAML frontmatter 取得 pipeline 狀態
3. 輸出表格：草稿名、主題、目前階段、最後更新
4. 用戶選擇後交給 `write-pipeline` 從對應階段繼續

---

### 4. `W2_CardWeaver` prompt — 卡片→文章素材橋樑
**檔案**: `.github/prompts/W2_CardWeaver.prompt.md`

**目的**: 接收 gather-cards 搜集到的 5-15 張卡片 + 主題方向，將卡片內容按文章角色組織成結構化寫作素材。

**角色映射**:
- (a) 開場故事/類比
- (b) 核心框架/模型
- (c) 支持論據/數據
- (d) 反面論述/邊界條件
- (e) 收尾洞察/金句素材

---

### 5. `WritingCoach` chatmode — 寫作教練
**檔案**: `.github/chatmodes/WritingCoach.chatmode.md`

**目的**: 在 pipeline 檢查點時提供互動式引導，幫用戶在標題/鉤子選擇、草稿審閱、最終確認等環節做出更好決策。與 `write-pipeline` 互補 — pipeline 負責自動執行，WritingCoach 負責決策支援。

---

## 需要修改的既有檔案（1 個）

### `.github/copilot-instructions.md`
在 `## AI 輔助工具` 的 Skills 段落加入新的 3 個 skill 說明，Chatmodes 段落加入 WritingCoach，並新增一段 `## 自動化寫作 Pipeline` 說明整體流程和 Draft frontmatter schema。

---

## 實作順序

| Phase | 檔案 | 原因 |
|-------|------|------|
| **Phase 1** | `gather-cards` + `W2_CardWeaver` | 基礎建設：讓卡片能餵入寫作流程，這兩個獨立就能使用 |
| **Phase 2** | `write-pipeline` | 核心：主控台串接所有環節 |
| **Phase 3** | `resume-draft` + `WritingCoach` | 支援層：狀態管理 + 互動引導 |
| **Phase 4** | 更新 `copilot-instructions.md` | 文件化整個系統 |

---

## 驗證方式

1. **單元驗證**: 在 Copilot Chat 中觸發 `gather-cards`，給定一個主題，確認能搜出相關卡片
2. **流程驗證**: 觸發 `write-pipeline`，走完一輪完整的 W1→W8，確認：
   - Draft 檔正確建立在 `/004_1Draft/` 且 frontmatter 正確
   - 三個檢查點確實暫停等待人工輸入
   - 最終產出移到 `/004_2Express/` 且 break-cards 產生新卡片
3. **恢復驗證**: 中途離開後觸發 `resume-draft`，確認能從正確階段繼續
4. **品質驗證**: 用 Editor chatmode 審閱 pipeline 產出的文章，確認卡片素材有自然融入
