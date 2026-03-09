# Check BreadCards - 檢測腳本使用說明

## 功能
跨平台腳本，用於檢測文件是否已完成 break-cards 拆解，並快速提取候選卡內容。

## 支援平台
- ✓ Windows
- ✓ macOS
- ✓ Linux

## 使用方式

### 基本語法
```bash
python check_breadcards.py <文件路徑>
```

### 範例
```bash
# 檢查某篇文章是否已拆解
python .github/skills/break-cards/check_breadcards.py "005_PARA/02_Areas/AI_Software_Data/某文章.md"
```

## 返回值（Exit Codes）

| Exit Code | 說明 | 含義 |
|-----------|------|------|
| **0** | 成功檢測到 BreadCards | 檔案已完成拆解，輸出 BreadCards 內容 |
| **1** | 文件不存在 | 指定的檔案路徑無效 |
| **2** | 未找到 BreadCards 標記 | 檔案尚未執行 break-cards 處理 |
| **3** | 提取失敗 | 讀取或解析過程發生錯誤 |

## 在 break-cards Skill 中的使用邏輯

```
執行 break-cards 前：
  ↓
檢查: python check_breadcards.py <檔案>
  ↓
Exit Code 0 (已拆解)
  → 跳過拆解，直接呼叫 refine-cards
  
Exit Code 2 (未拆解)
  → 繼續執行 break-cards 流程
  
Exit Code 1/3 (錯誤)
  → 告知 user 並終止
```

## 優勢
- **避免重複處理**: 自動檢測已拆解的文件，防止重複工作
- **流程銜接**: 發現已拆解直接呼叫 refine-cards，提升效率
- **跨平台**: 單一腳本支援所有作業系統
- **快速定位**: 只讀取需要的候選卡內容

## 維護說明
此腳本在 `break-cards` 和 `refine-cards` 兩個資料夾中**獨立維護**：
- `.github/skills/break-cards/check_breadcards.py`
- `.github/skills/refine-cards/check_breadcards.py`

修改時需同步更新兩邊。
