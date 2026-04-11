---
title: 資料 Agent 撞牆的原因從來不是模型——是底下那層「上下文基建」還沒長好
status: draft
created: 2026-04-11
theme: 資料 Agent 的下一階段：從「比模型」走到「比上下文基建」
sources:
  - 20260407_資料Agent真正缺的是Context_Layer.md
  - 20260407_治理從權限進化到Business_Semantics.md
  - 20260407_A2A與MCP分層打造Agentic_MLOps.md
  - 20260408_AnalysisAgent價值案例.md
  - 20260403_Agent軟體開發將怎麼改變資料庫.md
---

# 資料 Agent 撞牆的原因從來不是模型——是底下那層「上下文基建」還沒長好

## TL;DR

- 2024–2025 每家公司都想把 agent 疊在既有 data stack 上做 chat with your data，2026 大家同時撞到同一面牆。
- 很多人第一反應是「模型不夠會寫 SQL」。但實際瓶頸更底層：**agent 不知道你公司的 revenue 到底指什麼、quarter 怎麼切、哪張表才是 source of truth**。
- 解法不是一個新模型，而是一整套「上下文基建」：Context Layer、Business Semantics、分層協作協議、甚至連資料庫架構本身都要被改寫。
- AnalysisAgent 的真實案例（Dentsu、S&P Global、Salesforce、Shell）印證了同一件事：**拉開差距的不是模型強度，而是這些基建是否到位**。
- 下一階段的資料 Agent 競賽，會從「比模型」變成「比上下文工程」。

---

## 一、為什麼大家都在撞同一面牆

a16z 在 3 月的文章裡有一句話講得很直接：現在只要跟任何在做 data + AI agent 的組織聊天，幾乎都會談到 context layer 或 context graph。

原因是整個市場剛從 hype 走出來，開始發現一件事：**資料與分析 agent 如果沒有正確 context，幾乎等於沒用**。它們沒辦法拆解含糊問題、看不懂業務定義，跨多個異質資料來源時推理也不穩定。

早期大家以為問題只是 SQL 能力不夠強。只要 text-to-SQL 再進步一點，data agent 就能自然成功。但實際不是這樣。

舉個最經典的例子：「上季營收成長是多少？」

這題看起來像 BI 入門題，實際上充滿陷阱：

- **Revenue 到底是什麼？** Run rate、ARR、gross、net？
- **Quarter 怎麼算？** 財年還是日曆年？
- **就算有 semantic layer，**裡面的 YAML 可能是已離職同事留下的舊定義，不再被 BI 工具使用，甚至沒包含最新產品線。

模型把 SQL 寫得再漂亮，只要上面任何一個定義跟不上現實，它就會產出一個「語法正確、結論錯誤」的答案——而且因為語言模型太會講話，這個錯答案還會顯得格外有說服力。

換句話說：**資料 agent 失敗的不是模型，是上下文。**

---

## 二、第一層：Context Layer —— 比 Semantic Layer 更大的那一圈

a16z 把這層基建命名為 **context layer**。它也有別的名字：context OS、context engine、contextual data layer、ontology，但核心概念一致：

> 把企業混亂的資料串起來，在上面加一層能幫 agent 理解 business logic 的 contextual layer，然後包裝成 agent 可以即時存取的資產。

這裡要特別區分 context layer 與傳統 semantic layer：

| 維度 | Semantic Layer | Context Layer |
|---|---|---|
| 主要用戶 | BI 工具 | Agent（自主運行） |
| 內容 | Metric 定義（revenue、churn、ARPU） | Metric + canonical entities + identity resolution + tribal knowledge + governance guidance |
| 建置方式 | 資料團隊手工撰寫 | LLM 自動建構 + 人工補齊 |
| 生命週期 | 相對靜態 | 必須持續 self-update |

semantic layer 不是沒用，而是不夠。它原本是給 BI 工具看的，不是給一個要自主推理的 agent 看的。

a16z 給出五步驟實作路徑：

1. **Access the right data** — 不只 warehouse 的結構化資料，也包括 GDrive、Slack、內部文件這些藏著隱性知識的地方。
2. **Automated context construction** — 從 query history、dbt、LookML 自動萃取高訊號 context。
3. **Human refinement** — 最關鍵的脈絡常常是條件式、歷史形成的（例：「2025 年後 USCAN 的新 deals 看 Affinity，之前的 global leads 看 Salesforce」），這種規則模型自己掃一圈不會懂。
4. **Agent connection** — 透過 API 或 MCP 接給 agent 即時讀取。
5. **Self-updating context flows** — 最重要的一步。資料系統不會靜止，agent 答錯之後的修正，必須回灌到 context layer，讓系統下次更準。

一句話總結：**context layer 是一個 living corpus，不是建好就結束，而是持續演化的知識與規則體系。**

---

## 三、第二層：治理不再只是權限，而是 Business Semantics

Databricks 社群的 Scott Davis 在 2026 年初那篇 data governance 的文章，剛好和 a16z 的觀點從另一個角度撞在一起。

他的論點是：2026 的 data governance 已經不是「誰能看哪些資料」，而是「資料如何被定義、追蹤、驗證、控制與信任」。治理從 observational（架在資料堆疊上方觀察）進化到 **integrated governance**（直接嵌進資料流本身）。

而 2026 最重要的升級點是 **business semantics**：讓治理變得 business-aware。

他舉的例子和 a16z 幾乎一模一樣：新分析師一上手就會卡住——revenue 到底怎麼定義、gross 還是 net、active customer 的標準是什麼、哪張表才是 source of truth、join 該怎麼做、結果怎麼驗證對錯。這些問題如果沒被制度化，人都跑不動，更別說 agent。

Davis 的結論很鮮明：

> **治理的角色正從「限制」轉成「加速」。沒有治理，AI 就無法從 lab experiment 變成 production-grade asset。**

這帶出一個隱含結論：**context layer 和 business-aware governance，本質上在做同一件事**——把組織裡分散、隱性、口耳相傳的業務語意固化成系統可用的資產。只是前者從「讓 agent 能運作」進入，後者從「讓 AI 能 scale」進入。

---

## 四、第三層：當 Agent 要協作，你需要把溝通層和能力層拆開

上下文準備好之後，下一個問題是：agent 不會一個人做完所有事。現代資料工作流，常常需要多個專業 agent 協作——validation、deployment、analysis、forecasting 各自有自己的職責。

InfoQ 在 2 月那篇 A2A + MCP 的文章給了一個很清楚的答案：

- **A2A** 負責 agent 之間的 discovery 與 communication —— 誰跟誰說話、怎麼找到對方、怎麼委派工作。
- **MCP** 負責 agent 對工具與資源的 capability exposure —— 一個 agent 接到任務後，要怎麼發現與使用底下的工具、資料、資源。

這兩層不是互斥，是疊成一個 layered architecture。它最關鍵的價值是：

> **Decoupling orchestration logic from execution logic.**

Orchestrator 不需要知道每個 specialist agent 內部怎麼做事；specialist 也不需要理解整個商業工作流，它只要透過 MCP 發現該用的工具就好。

舉一個 MLOps 的例子：「如果 validation 成功，就部署最新模型。」

- **Orchestrator Agent** 收到目標後，拆成 validation + deployment 兩個子任務，透過 A2A 找到對應 specialist。
- **Validation Agent** 收到任務，不再往下委派，改成透過 MCP 做 tool-use planning，找到 `fetch_model`、`validate_churn_model` 等工具照順序執行。
- **Deployment Agent** 走一樣的模式完成部署。

傳統 pipeline 的問題是一旦商業邏輯變了，常常要整條重寫。分層 agent 架構比較像**能力編排系統**：適應新需求時，不是改一大段靜態流程，而是新增或重組可被發現的能力。

這也是為什麼 context layer 的第四步會指名 MCP：因為 MCP 正是把「上下文資產」變成「agent 運行時能即時讀取的能力」的那個介面。

---

## 五、第四層：連資料庫本身都要被改寫

如果你以為基建只到 context 與 protocol 就結束，Databricks 的 Lakebase 論述會讓你重新思考。

他們在生產環境觀察到三個數字，直接挑戰了傳統資料庫的經濟模型：

- **AI agent 建立的資料庫數量，是人類使用者的 4 倍。**
- **約 50% agent 生成的應用，資料庫運算生命週期不到 10 秒。**
- **平均每個資料庫專案有 ~10 個分支，部分專案巢狀分支深度超過 500 次迭代。**

這三個數字意味著：agent-driven 開發不是線性規劃，而是**大規模平行試錯的演化式迭代**。每個 agent 都在大量 branch、測試、拋棄、重新生成。

傳統資料庫對這種模式完全不友善：

1. **複製狀態的成本太高** → 需要儲存層 metadata branching，實現零實體複製的瞬間分支。
2. **固定基礎設施成本太高** → 應用只跑 10 秒，固定月費根本不合理，必須 scale-to-zero。
3. **閉源格式讓 agent 不會用** → agent 的能力來自訓練語料，Postgres 這類開源系統的錯誤訊息、API 都在語料裡；專有格式因為缺乏公開 context，agent 無法穩定操作。**開源從理念偏好變成「嚴格營運需求」。**
4. **流量不可預測** → 必須支援從微型實例無縫擴展到生產規模，不能靠人工重配。

這段我最有感的一個觀察是：**開源的定義被 agent 改寫了**。過去談開源是社群、授權、生態；現在談開源是「你的系統行為有沒有在 LLM 的訓練語料裡」。Postgres 贏在這一點，很多新興專有系統反而被這條規則打下去。

---

## 六、現實檢驗：那些公開的 AnalysisAgent 成功案例到底在做什麼

把這四層基建講完，一個合理的問題是：這些東西真的在現實裡發生了嗎？還是只是架構師的願景？

我整理了最近幾個公開的企業案例，發現一個共通點：**拉開差距的從來不是「模型更強」，而是上面那四層基建哪一層到位。**

### Dentsu —— Access / Delivery Layer 到位

用 Azure AI Foundry + OpenAI 做 predictive analytics copilot，成果是 analysis time 減少 80%、time-to-insight 減少 90%。它做的其實就是 context layer 的 step 4：把既有的分析能力包成一個 agent 能即時存取的介面。

**這一型最像 context layer 先落地，模型反而是最不特別的部分。**

### S&P Global —— 高價值資料 × Access Layer

接進 Microsoft 365 Copilot 之後，客戶平均達到 95% faster data extraction、98% faster comparative analysis、96% faster customer insights。它證明了一件事：高價值資料只要上下文建好，agent 就能把交付速度拉到數十倍。

### Salesforce —— Action Layer 到位（但前提是 Data 360）

Salesforce 自家的案例是 60% lead revenue 提升、85% resolution rate、98,000 少掉的 support cases、2300 萬美元潛在續約收入。這些數字之所以能成立，關鍵是前面有 Data 360 把資料統一，**等於自己內建了一層 context + governance 基建**。如果這層沒做，Agentforce 跑出來的就只是更快的錯誤。

### Shell —— 工業型流程最佳化

管線腐蝕模擬比傳統 CFD 快 106 倍、CCS storage site assessment 加速 60%+。這一型證明 agent 不只用在報表與客服，也可以進入實體流程。但它的前置條件是更嚴格的模擬驗證與工程 context。

### causaLens —— Analytical Engine Layer 的代表

做 Causal AI + digital workers，往 decision intelligence 靠近。它代表的是 agent 呼叫專業分析引擎的方向，而不是 agent 自己演化出因果推論能力。

---

## 七、我的整理：三張地圖，一個結論

這些案例擺在一起，我會用三種視角看：

**商業模式分類**

- **A 內部自助分析**（Dentsu）—— 降低內部取用成本
- **B 外部資料產品**（S&P Global）—— 把高價值資料商品化
- **C 工業流程最佳化**（Shell）—— 進入實體與工程流程
- **D 前台行動自動化**（Salesforce）—— 從 insight 接到 action

**系統能力分層**

- **Access / Delivery Layer** —— Dentsu、S&P Global
- **Analytical Engine Layer** —— causaLens
- **Action Layer** —— Salesforce、Shell

**實作難度與順序**

- **最適合先做的**：Dentsu 型。解決的痛點最清楚（分析結果取得太慢），前置基建最輕。
- **最想達到的**：causaLens 型。但這條不是從 Dentsu 型自然升級，而是另一條更硬的路。
- **系統終局**：Salesforce 型。因為商業影響最終要走到能推動 action，不能只停在更好的分析介面。

一個很重要的提醒：**這三層不是一條線性升級的階梯**。很多團隊以為做好 Dentsu 型就能升級到 Salesforce 型，但實際上你需要的是完全不同的基建——前者卡在 context，後者卡在 write-back 與 orchestration。

---

## 八、下一階段的資料 Agent 競賽，從「比模型」變成「比上下文基建」

把這五篇拼起來，我看到一個一致的方向：

> **過去一年大家在比模型；接下來一年大家會比誰的上下文基建更完整、更新、更可維護。**

這層基建由四塊組成：

1. **Context Layer** —— 讓 agent 真的懂你的業務語意與隱性知識。
2. **Business-aware Governance** —— 讓語意被治理、被追溯、被信任。
3. **A2A + MCP 分層** —— 讓多 agent 的協作不靠硬編碼，能持續擴充。
4. **Agent-native Database** —— 讓底層存儲支援 branching、scale-to-zero、開源格式。

這四塊任何一塊沒做好，agent 再強也只是在不穩定的語意地板上奔跑——而且因為語言模型太會講話，它會用非常有說服力的方式輸出錯誤結論。

a16z 最後的一句話我覺得很適合當這篇的收尾：

> **真正能讓自助式 analytics、BI、data science 進一步被 AI 重寫的，不只是更強的模型，而是更完整、更活的 context infrastructure。**

如果你正在思考組織裡「資料 agent 為什麼做不起來」，先不要再換模型。先問自己這四層基建在哪一層卡住了。

---

## 寫作備註（TODO）

- [ ] 開頭鉤子太長，考慮砍成 2-3 句就進主論點
- [ ] 第五節「資料庫改寫」這段跟前面 context 主軸的連結還不夠緊，需要補一句收束——意思是「上層 context 改變了，連底層儲存的經濟模型都被改寫」
- [ ] AnalysisAgent 案例的引用來源需要在發布前再 fact-check 一次（數字與原始 Microsoft / Salesforce / Shell 案例對照）
- [ ] causaLens 的段落比較弱，可以考慮刪掉或另外拉成一篇
- [ ] 標題可以再琢磨：備選「資料 Agent 卡關的不是模型」「上下文基建才是 2026 的競賽場」
- [ ] 結尾可以加一個 checklist：這四層我自己/我的組織分別在哪個成熟度
- [ ] 是否加入 skills 原子性、harness eng 那條線做對照（但可能會失焦，先不加）
