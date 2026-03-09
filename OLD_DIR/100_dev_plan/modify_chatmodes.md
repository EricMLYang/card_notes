段針對你的需求，我將 GitHub Copilot 的擴充機制重新整理為一份**決策準則**。這份說明旨在幫助你的 Coding Agent 自動化分類現有的 `.chatmode.md` 檔案，並將其重構至正確的位置。

---

## 🛠 GitHub Copilot 擴充機制分類指南 (2026 版)

### **1. 決策矩陣：我該放在哪？**

| 類型 | 目標路徑 | 適用情境 (Decision Rule) | 觸發方式 |
| --- | --- | --- | --- |
| **Skills** | `.github/skills/` | **被動呼叫、工具型**。適合「自動化任務」，如：自動格式化、調用外部 API、自動生成單元測試。 | 由 Copilot 根據上下文**自動決定**何時調用。 |
| **Agents** | `.github/agents/` | **特定角色、人格化**。適合「領域專家」，如：架構師、資安審查員、DBA。具備獨立的系統指令與工具權限。 | 在 Chat 視窗**手動切換**或使用 `@` 提及。 |
| **Prompts** | `.github/prompts/` | **手動觸發、範本型**。適合「重複性的長指令」，如：寫 PR 說明、固定格式的重構要求。 | 在對話中輸入 `/` **手動選擇**。 |

---

## 📂 遷移與檢討邏輯 (For Coding Agent)

你可以指示你的 Coding Agent 依照以下邏輯掃描 `.github/chatmodes/` 並進行遷移：

### **Case A：轉換為 Skills (自動化優先)**

* **特徵**：原本的 chatmode 內容是「當我寫完程式碼時，幫我檢查變數命名」或「串接外部工具獲取資訊」。
* **動作**：搬移至 `.github/skills/`，並確保 YAML 中定義了正確的 `triggers` 或 `mcp_servers`。
* **優點**：你不需要手動呼叫，Agent 會在合適時機主動介入。

### **Case B：轉換為 Agents (專業角色優先)**

* **特徵**：內容包含大量角色設定（System Prompt），例如「你是一位嚴格的 Code Reviewer，請用批判性思維審查...」。
* **動作**：搬移至 `.github/agents/`，副檔名改為 `.agent.md`。
* **優點**：當你需要深度對話時，可以直接進入該「模式」，確保模型不會受到專案其餘雜訊干擾。

### **Case C：轉換為 Prompts (指令範本)**

* **特徵**：內容純粹是一段很長的請求，且不具備特定人格，例如「請依照此 XML 格式生成文件」。
* **動作**：搬移至 `.github/prompts/`，副檔名改為 `.prompt.md`。
* **優點**：減少手動輸入負擔，隨選隨用。

---

## 📝 範例：舊版 chatmode 檔案重構

**原始檔案：`.github/chatmodes/security_check.chatmode.md**`

> 內容：你是一個資安專家，請檢查這段程式碼是否有 SQL Injection 風險。

**Coding Agent 處理建議：**

1. **判定**：這是一個具備高度專業知識的角色。
2. **目標**：`.github/agents/security-auditor.agent.md`
3. **格式優化**：
```yaml
---
name: Security Auditor
description: 專門進行弱點掃描與修補建議
tools: [ "static_analysis_tool" ]
---
# System Instructions
你是一位極度嚴格的資安專家，...

```



---

## 🚀 接下來的操作建議
> 「請掃描 `.github/chatmodes/` 目錄。如果是工具/自動化性質，遷移至 `.github/skills/`；如果是專家角色性質，遷移至 `.github/agents/` 並更名為 `.agent.md`；其餘指令範本遷移至 `.github/prompts/`。完成後請刪除舊的 chatmodes 資料夾。」