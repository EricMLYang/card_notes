---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# A2A 與 MCP 分層打造 Agentic MLOps

> 來源：InfoQ
> 連結：https://www.infoq.com/articles/architecting-agentic-mlops-a2a-mcp/
> 搜集日期：2026-04-07
> 搜集原因：Agent 架構分層、協作協議、MLOps 自動化

## 摘要
這篇 InfoQ 文章在 2026-02-16 提出一個很實用的結構：A2A 負責 agent 之間的發現與溝通，MCP 負責 agent 對工具與資源的能力存取。文章的價值不在於單一協議介紹，而在於把兩者放進同一個 layered architecture，示範如何把「編排邏輯」與「工具執行邏輯」拆開。它用 MLOps 當例子，但其實更大的啟發是任何需要多 agent 協作、又不想被硬編碼工作流綁死的系統，都能套這種結構。這對你關心的 decision system 與 agent workflow productization 很重要，因為它把 agent 從單體 prompt flow 拉回到可擴充的系統設計。

## 潛在卡片方向
- A2A 與 MCP 的關係，不是互斥，而是「溝通層」與「能力層」的分工。
- 真正可擴充的 agent 系統，要把 orchestration logic 與 execution logic 拆開。
- Agent Card 與 MCP capability exposure 是讓多 agent 協作可維護的關鍵中介結構。
- 從靜態 pipeline 走向動態 agent coordination，本質是把流程改寫成能力組合。
- 可連結的現有卡片：[[Agent組織化原則——專門context處理專門事情]]、[[DecisionOps]]、[[兩階段判斷設計_AI自動化的安全模式]]

---

## 全文翻譯

文章先指出一個很像微服務早期的問題。當軟體業進入 agentic era，系統裡會出現越來越多專門化 agent；這時工程師與架構師遇到的核心挑戰，和當年微服務爆發時很像，都需要一套標準化方式讓不同元件彼此發現、溝通、協作。作者認為，A2A 與 MCP 的組合就是這一階段的重要答案。

他們的主張很直接：A2A 與 MCP 不應該被拿來替代彼此，而應該被疊成一個分層架構。A2A 是 agent-to-agent 的 communication bus，處理「誰跟誰說話、怎麼找到對方、怎麼委派工作」；MCP 則像一種通用能力介面，處理「一個 agent 一旦接到任務後，要如何發現與使用底下的工具、資料與資源」。把這兩層分開之後，系統就可以在不改核心 communication logic 的前提下，持續增加新能力。

作者特別強調，這種 layered pattern 的價值在於 decoupling orchestration logic from execution logic。也就是說，負責規劃任務流程的 orchestrator，不需要知道底下每一個 specialist agent 內部是怎麼做事的；同樣地，specialist agent 也不必理解整個商業工作流，它只要透過 MCP 發現適合的 tools / resources，完成自己那一段能力就好。這樣系統的可擴充性會大幅提升。

在範例裡，他們用一個常見的 MLOps use case 來示範：目標是「如果 validation 成功，就部署最新模型」。系統裡有三種 agent。第一個是 Orchestrator Agent，收到高層目標後，先把它拆成 validation 與 deployment 兩個子任務，再透過 A2A 找到對應 specialist。第二個是 Validation Agent，專門處理模型驗證。第三個是 Deployment Agent，專門處理部署。A2A 讓 orchestrator 不需要硬編碼綁定某一個 validation service 或 deployment service，而是透過 agent discovery 與 capability description 去互動。

這裡的 Agent Card 很重要。每個 agent 都有一張「能力卡」，描述它能做什麼、支援哪些 request 類型、有哪些協定。這張卡本質上是一個 discovery layer，讓其他 agent 能在不暴露敏感內部細節的情況下，知道它可不可以處理某件事。對多 agent 系統來說，這其實就是可維護性的前提，不然一切都會退化成手工硬接。

接著文章轉到 MCP。MCP 被描述成 AI integrations 的 USB-C，目的是標準化 AI 系統如何接到工具、服務與資料來源。MCP server 可以暴露三種主要實體：tools、resources、prompts。Tools 是能被呼叫的動作，像執行驗證或部署；resources 是 agent 可查詢或載入的結構化資料；prompts 則是引導 agent 行為的預設模板。因為這些 primitive 有共同定義，所以任何相容的 client 都能在不寫 custom glue code 的前提下發現並使用它們。

文章中的 MCP server 例子很清楚。它把 `fetch_model`、`validate_churn_model`、`deploy_churn_model` 暴露成 tools，同時提供像 `list_agent_cards`、`retrieve_agent_skills` 這類 resources。作者刻意把實際商業邏輯留空，因為他們要強調的不是某個框架 API，而是能力被如何定義、命名、暴露、發現。只要這層做對，底下具體要接哪家 cloud、哪套 validation library、哪個 deploy mechanism，就都能被替換。

從執行流程來看，整個系統是這樣運作的：MLOps engineer 提出一個高層 query；Orchestrator 先用自己的 reasoning 把任務拆成 `TaskList`；接著透過 A2A 找到 Validation Agent，把子任務交出去。Validation Agent 收到之後，不再往下委派，而是改成透過 MCP 進行 tool-use planning，發現需要的工具，例如 `fetch_model` 與 `validate_churn_model`，然後照順序執行。驗證成功後，Orchestrator 再透過 A2A 把部署任務交給 Deployment Agent；Deployment Agent 同樣透過 MCP 找到適當 tools 完成動作。

作者用這個範例在對比傳統 pipeline 與 agent-driven operations 的差異。傳統 orchestrator 雖然強大，但相對僵硬；當商業邏輯一變，整條 pipeline 常常要重寫、重部署。相反地，分層 agent 架構比較像能力編排系統，你要適應新需求時，不是去改一大段靜態流程，而是新增或重組可發現的能力。

文章也沒有忽略風險。A2A 主要處理安全通信與互操作；MCP 則因為會把外部能力接進來，所以伴隨 prompt injection、tool poisoning、未授權資料存取等風險。換句話說，分層帶來擴充性，但同時也要求更清楚的治理與權限設計。這點對你在想的「哪些判斷能交給 agent、哪些一定要保留控制介面」特別重要。

最終，這篇文章最值得收的地方，在於它不是把 agent 看成一個會做事的單體，而是把 agent 系統視為一種新的架構分層：A2A 處理協作，MCP 處理能力暴露，orchestrator 處理目標分解，specialists 處理局部責任。這種結構非常適合拿來思考未來的 decision workflow、analysis workflow，甚至 coding workflow 要怎麼從單體 prompt flow 進化成可維護的多代理系統。
