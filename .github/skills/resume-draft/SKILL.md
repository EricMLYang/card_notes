---
name: resume-draft
description: 列出所有進行中草稿的 pipeline 狀態，讓用戶快速恢復寫作進度。適用於用戶說「我的草稿」「繼續寫作」「resume draft」時。Use when user wants to see draft status or resume writing.
---

# Skill: Resume Draft（草稿狀態管理器）

## 目標
掃描 `/004_1Draft/` 中所有草稿，讀取 YAML frontmatter 取得 pipeline 狀態，讓用戶快速了解所有進行中草稿的進度並選擇恢復。

## 執行流程

### Step 1: 掃描草稿資料夾
讀取 `/004_1Draft/` 中所有 `.md` 檔案。

### Step 2: 解析 Frontmatter
逐一讀取每個檔案的 YAML frontmatter，提取：
- `pipeline_stage`：目前的 pipeline 階段
- `topic`：文章主題
- `status`：草稿狀態（drafting / reviewing / polishing / published）
- `last_updated`：最後更新日期
- `chosen_title`：已選標題（如有）

**注意**：沒有 `pipeline_stage` 欄位的檔案視為「非 pipeline 草稿」，單獨列出。

### Step 3: 輸出狀態表
按 `last_updated` 倒序排列，呈現所有草稿的狀態。

### Step 4: 等待用戶選擇
用戶選擇草稿後，將選定的草稿資訊交給 `write-pipeline`，從對應的 `pipeline_stage` 繼續執行。

## 輸出格式

```markdown
## 草稿總覽

### Pipeline 進行中
| # | 主題 | 階段 | 狀態 | 最後更新 | 下一步 |
|---|------|------|------|----------|--------|
| 1 | [topic] | [pipeline_stage] | [status] | [date] | [下一步動作描述] |
| 2 | [topic] | [pipeline_stage] | [status] | [date] | [下一步動作描述] |

### 其他草稿（無 pipeline 狀態）
| # | 檔名 | 預覽 |
|---|------|------|
| 3 | [filename] | [前 50 字] |

---
請選擇要繼續的草稿編號，或輸入「新文章」開始新的 pipeline。
```

### 階段對應的「下一步」描述
| pipeline_stage | 下一步 |
|----------------|--------|
| INTAKE | 完成主題確認和卡片搜集 |
| IDEATION | 自動發想素材 |
| TITLE_HOOK | 自動生成標題和鉤子 |
| CP1 | 等待選擇標題和鉤子 |
| FRAMEWORK | 確認文章框架 |
| BODY_CLOSE | 自動撰寫主體和收尾 |
| CP2 | 等待審閱草稿 |
| POLISH | 自動打磨文章 |
| CP3 | 等待最終確認 |
| PUBLISH | 自動排版和發佈 |
| DONE | 已完成 |

## 操作指引

**觸發條件**：
- 用戶說「我的草稿」「草稿狀態」
- 用戶說「繼續寫作」「繼續寫」
- 用戶說「resume draft」「show drafts」

**後續流程**：
- 用戶選擇 pipeline 草稿 → 交給 `write-pipeline` 從對應階段繼續
- 用戶選擇非 pipeline 草稿 → 詢問是否要將其納入 pipeline（補建 frontmatter）
- 用戶選擇「新文章」→ 啟動 `write-pipeline` Step 1

## 品質檢查

- ✅ 正確解析所有草稿的 frontmatter
- ✅ 沒有 frontmatter 的草稿也被列出（歸類為「其他草稿」）
- ✅ 狀態表按最後更新日期倒序排列
- ✅ 「下一步」描述準確對應 pipeline 階段
