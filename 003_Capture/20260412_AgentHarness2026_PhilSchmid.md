# Agent Harness in 2026 — Phil Schmid

> 來源：philschmid.de（Phil Schmid 個人技術部落格）
> 來源類型：高密度觀點
> 需求層：知識建構
> 連結：https://www.philschmid.de/agent-harness-2026
> 搜集日期：2026-04-12
> 搜集原因：K1 — AI Agent 工程化與 harness 設計

## 摘要
作者把 Agent Harness 類比成「Operating System」：Model 是 CPU、Context Window 是 RAM、Agent 是 Application，而 Harness 才是真正讓 Agent 從 demo 走到上線的那層作業系統。文章核心論點是「benchmark 上 1% 的差距，看不出模型在 50 步之後會不會崩」，要靠 harness 才能把多步驟、多日的 workstream 變成可被 log、可被 grade 的結構化資料。

## 為什麼值得看
這篇是少數把 harness 講成「OS 級抽象」的長文，而且舉的案例很實在：Manus 在 6 個月內把 harness 重構 5 次、LangChain 一年內把 Open Deep Research agent 重新架構 3 次、Vercel 把 agent 工具刪掉 80% 之後反而更快。對應到 Eric 自己「decision system 不是模型而是 harness」的主軸，這篇是直接的彈藥庫，特別適合拿來寫「為什麼 Agent 上不了線，問題不在模型」的判準文。

## 可能偏誤或限制
- 作者立場偏「open-source harness」與工程實作派，對於企業治理、權限邊界、人工 checkpoint 的著墨較少
- 案例都是面向「Coding Agent / Research Agent」這類技術型 Agent，未直接談垂直領域 business decision agent 的差異
- 沒有討論 harness 與 Unity Catalog / MCP / 治理層如何接合，需要自己補

## 潛在卡片方向
- Agent Harness = OS 的類比卡（CPU/RAM/OS/App 對應 Model/Context/Harness/Agent）
- 「Build to Delete」原則：harness 要模組化，因為下一代模型會讓現有控制流失效
- Harness as Dataset：競爭優勢從 prompt 移到 trajectory 資料
- 可串連卡片：[[Harness Engineering 是 Agent 上線的關鍵]]、[[Coding Agent 工作流的 verification 設計]]

---

## 全文翻譯（重點摘錄）

### 為什麼需要 Agent Harness
- 傳統 model benchmark 會錯過最關鍵的「可靠性」問題：「leaderboard 上 1% 的差距，無法偵測模型在 50 步之後會不會偏離軌道。」
- Harness 讓多日的 workstream 變得可靠，這是模型 benchmark 看不到的能力。

### 計算機類比
- **Model = CPU**：原始運算能力
- **Context Window = RAM**：有限的揮發性記憶
- **Agent Harness = OS**：管理 context、boot sequence、tool 處理
- **Agent = Application**：使用者特定的邏輯
- Harness 提供「prompt presets、tool call 的意見化處理、lifecycle hooks，以及 planning、filesystem access、sub-agent management 等開箱即用能力」

### Harness 為什麼重要的三個理由
1. 用真實 use case 驗證實際進度（而不是 leaderboard）
2. 用驗證過的 pattern 提供一致的使用者體驗
3. 建立 feedback loop：「Harness 把模糊的多步驟 agent workflow 變成可以 log、可以打分的結構化資料」

### 真實案例
- **Manus**：在 6 個月內把 harness 重構 5 次
- **LangChain**：一年內把 Open Deep Research agent 重新架構 3 次
- **Vercel**：把 agent 工具刪掉 80%，回應速度反而更快

### 三條給團隊的行動建議
1. **Start Simple**：避免巨大的控制流，讓模型自己 plan
2. **Build to Delete**：保持架構模組化，因為新模型會讓現有邏輯過時
3. **Harness as Dataset**：競爭優勢從 prompt 轉移到「Harness 捕捉的 trajectory」
