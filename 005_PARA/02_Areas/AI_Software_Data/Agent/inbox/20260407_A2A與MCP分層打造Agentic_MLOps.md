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

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：A2A 與 MCP 不是替代關係，而是分層關係——A2A 是 agent 之間的 communication bus（誰跟誰說、怎麼找對方、怎麼委派），MCP 是 agent 對工具/資源/資料的能力存取介面。把兩者疊成 layered architecture，能 decouple orchestration logic from execution logic：規劃者不需要知道執行者怎麼做，執行者不需要懂整個 workflow，只需透過 MCP 找適合工具完成任務。
- 作者挑戰的預設：（1）Agent 系統設計是 prompt + tool 的事 → 是分層架構問題，與 microservices 早期挑戰同構；（2）一個強的 orchestrator 就夠了 → 強的 orchestrator + agent discovery + capability exposure 才是可擴充的；（3）MCP 只是「工具接口」 → MCP 是讓能力被定義 / 命名 / 暴露 / 發現的標準介面（USB-C for AI）。
- 個人映射：直接補強你的「從 monolithic prompt flow 到 multi-agent system」主軸；引入「Agent Card」概念補上你之前沒明寫的「discovery layer 是多 agent 可維護性的前提」。同時 prompt injection / tool poisoning 風險呼應你關心的「AI Coding 風險治理」。

## B. 候選卡（Lite）

序號 1
- 候選標題：A2A 與 MCP 是分層關係：通訊層 vs 能力層
- 分級：Core
- 類型：Principle
- 核心內容：A2A 解決「agent 之間如何發現、溝通、委派」；MCP 解決「agent 接到任務後如何發現、使用工具與資源」。兩者不應該被視為競爭協議，而是不同職責的分層：A2A 在上層處理協作 routing，MCP 在下層處理能力 routing。把兩層分開後，可以新增 capability 而不改 communication logic。
- 保留理由：解決一個目前圈子裡常見的混淆（A2A vs MCP「該選哪個」），把它從選擇題變成架構分層題。對你做 Agentic Workflow productization 是基礎概念。
- 待補強處：實際工程上兩層的邊界如何劃分？是否有反例（某些情境下分層反而是 over-engineering）？
- 初步知識鉤子：[[Agentic Workflow]]、[[MCP as USB-C]]、[[Microservices Pattern]]

序號 2
- 候選標題：Decouple Orchestration from Execution：可擴充 Agent 系統的核心原則
- 分級：Core
- 類型：Principle
- 核心內容：Orchestrator 不需要知道每個 specialist agent 內部怎麼做事；specialist agent 也不必懂整個 workflow，只需透過 MCP 發現適合的 tools / resources 完成自己那段。這個分離讓系統可以新增 specialist 不影響 orchestrator、修改 specialist 不影響其他 agent。
- 保留理由：是把單體 prompt flow 演化成可維護多代理系統的核心 architectural decision。可遷移到 decision workflow / analysis workflow / coding workflow 三條主線。
- 待補強處：何時 decoupling 反而拖慢迭代（小規模快速 prototype 階段）？orchestrator 對 specialist 內部需要多少觀測權才能保持可靠？
- 初步知識鉤子：[[Microservices vs Monolith]]、[[Agent Workflow Productization]]、[[Capability Composition]]

序號 3
- 候選標題：Agent Card 是 Multi-Agent 系統的 Discovery Layer
- 分級：Support
- 類型：Pattern
- 核心內容：每個 agent 都有一張 Agent Card，描述它能做什麼、支援哪些 request 類型、有哪些協定。本質上是 discovery layer——讓其他 agent 在不暴露敏感內部細節的前提下，知道它能不能處理某件事。沒有 Agent Card，多 agent 系統會退化成手工硬接每對連結。
- 保留理由：把「discovery」從一個 service registry 概念，落地到 agent 場景的具體中介結構。對你長期關心的「Repo as Worker / Skill 公開介面」是可借鏡的設計。
- 待補強處：Agent Card 的版本管理、權限控制、能力測試（不只 self-declaration 還需驗證）如何設計？
- 初步知識鉤子：[[Service Discovery]]、[[Skill 規格]]、[[MCP Capability Exposure]]

序號 4
- 候選標題：MCP 三件式：tools / resources / prompts 的能力暴露 primitives
- 分級：Support
- 類型：Pattern
- 核心內容：MCP server 暴露三種主要實體——tools（可被呼叫的動作）、resources（可查詢或載入的結構化資料）、prompts（引導 agent 行為的預設模板）。因為這三種 primitive 有共同定義，相容 client 都能在不寫 custom glue code 的情況下發現並使用。命名 / 暴露 / 發現的標準化是關鍵。
- 保留理由：把 MCP 從一個「協議」具象化成「三類可發現實體」，方便評估自己系統哪些能力應暴露成哪一類。
- 待補強處：何時用 tool vs prompt（兩者邊界模糊）？resources 的權限模型如何設計？
- 初步知識鉤子：[[MCP Server 設計]]、[[Capability Definition]]、[[Tool vs Prompt 邊界]]

序號 5
- 候選標題：分層架構帶來擴充性，但同時要求更明確的治理與權限
- 分級：Support
- 類型：Warning
- 核心內容：A2A 帶來安全通信與互操作問題；MCP 因為要把外部能力接進來，伴隨 prompt injection、tool poisoning、未授權資料存取等風險。換句話說，分層不是免費的——它要求清楚的權限模型、能力 scope、執行追蹤等治理機制。否則擴充性會放大攻擊面。
- 保留理由：是少數明確處理「分層後的安全成本」的觀點；對你關心的「AI Coding 風險治理」與 AWS Shared Responsibility Model 直接接軌。
- 待補強處：具體治理模式（per-tool ACL、per-agent identity、call-level audit）的設計範式？
- 初步知識鉤子：[[Prompt Injection]]、[[Tool Poisoning]]、[[Shared Responsibility Model]]、[[Agent 治理]]

序號 6
- 候選標題：能力編排取代靜態 pipeline：商業邏輯變動時的可演化性
- 分級：Support
- 類型：Pattern
- 核心內容：傳統 orchestrator 雖然強大但僵硬，商業邏輯一變整條 pipeline 常需重寫重部署。分層 agent 架構更像「能力編排系統」，要適應新需求時不是改靜態流程，而是新增或重組可發現的能力。這對應 modern data stack 從 hard-coded ETL 到模組化轉型的舊故事，只是換到 agent 層。
- 保留理由：跨領域類比（資料 pipeline 演化 vs agent pipeline 演化）的清晰範例；對你寫「從專案到產品的平台化轉型」可借用的論述骨架。
- 待補強處：能力編排在實作初期的成本是否高於靜態 pipeline？切換的觸發條件（規模、變動頻率）？
- 初步知識鉤子：[[Modern Data Stack 演化]]、[[Adapter Pattern]]、[[Configuration Driven]]

## C. 建議送 refine 的項目
- 序號 1（Core）：A2A vs MCP 分層
- 序號 2（Core）：Decouple Orchestration from Execution
- 序號 3（Support）：Agent Card / Discovery Layer
- 序號 5（Support）：分層架構的治理成本
- 序號 4 / 6：refine 階段判斷是否合併到序號 1 或 2

## D. 呼叫 refine-cards
- 上述 6 張候選卡交由 refine-cards 精煉；建議與「20260403 HOTL」的序號 4（結構化 orchestration）做去重 / 合併判斷，可能可以共構一張更大的「Agent 系統工程化原則」卡。

