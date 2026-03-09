---
name: filename-prefix-guard
description: 統一檢查與修正 003_Capture、015_Write/Draft、015_Write/Publish 的檔名日期前綴規則。適用於用戶說「檢查檔名格式」「補上日期前綴」「rename files with date prefix」時。
---

# Skill: Filename Prefix Guard（檔名前綴守門員）

## 目標
確保以下資料夾中的 Markdown 檔名符合 `YYYYMMDD_[title].md` 規則：
- `003_Capture/`
- `015_Write/Draft/`
- `015_Write/Publish/`

## 腳本位置
本 skill 包含檢查腳本：`.github/skills/filename-prefix-guard/check.py`

### 使用方式

```bash
# 檢查所有目標資料夾的檔案
python .github/skills/filename-prefix-guard/check.py --all-files

# 只檢查 git staged 的檔案（預設）
python .github/skills/filename-prefix-guard/check.py

# 顯示建議的修正檔名
python .github/skills/filename-prefix-guard/check.py --all-files --suggest-fix
```

## 執行流程

### Step 1: 掃描目標檔案
1. 讀取三個資料夾內 `.md` 檔案
2. 檢查檔名是否符合正則：`^\d{8}_.+\.md$`
3. 檢查日期是否為有效日期（例如 `20260230` 視為無效）

### Step 2: 呈現檢查結果
1. 輸出符合與不符合的檔案數量
2. 列出不符合清單

### Step 3: 修正（需用戶同意）
1. 若用戶要求修正，優先使用 git 首次提交日期作為前綴：
   - `git log --diff-filter=A --follow --format=%ad --date=format:%Y%m%d -- <file>`
2. 若找不到 git 日期，改用最後提交日期：
   - `git log -1 --format=%ad --date=format:%Y%m%d -- <file>`
3. 仍找不到時，使用當天日期
4. 重新命名為：`YYYYMMDD_[原檔名].md`

## 觸發條件
- 用戶說「幫我檢查 Capture/Draft/Publish 檔名」
- 用戶說「補上日期前綴」
- 用戶說「rename files with date prefix」
- 用戶說「檢查檔名格式」

## 禁止事項
- ❌ 不要修改 `010_CardNotes/02_Cards/` 等非目標資料夾
- ❌ 不要移除原檔名語意，只能加上日期前綴
- ❌ 不要跳過日期有效性檢查
