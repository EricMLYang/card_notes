---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# 資料 Agent 真正缺的是 Context Layer

> 來源：Andreessen Horowitz
> 連結：https://a16z.com/your-data-agents-need-context/
> 搜集日期：2026-04-07
> 搜集原因：Decision system、semantic layer、資料 agent 與 context engineering

## 摘要
Jason Cui 與 Jennifer Li 在 2026-03-10 的這篇文章裡，直接把「chat with your data 為什麼一直撞牆」講透了。核心論點很接近你的主線：資料 agent 失敗，往往不是因為模型不夠會寫 SQL，而是缺少可維護、可更新、帶有業務定義與隱性知識的 context layer。文章把 semantic layer 與 context layer 的差異講清楚，也提出一條五步驟路徑，從資料接入、自動建構、人工補齊、agent 連接到 self-updating flows。這篇很值得放進你的系統，因為它把「從資料平台到決策系統」裡最容易被忽略的那層東西明確命名了。

## 潛在卡片方向
- Data agent 失敗的瓶頸不是單純 text-to-SQL，而是缺乏最新、可演化的 context layer。
- Semantic layer 只是一部分；能支撐 agent autonomy 的 context layer 還要包含 canonical entities、tribal knowledge、governance guidance。
- Context layer 必須有 self-updating flow，因為商業定義與資料源會持續變。
- 建立資料 agent 其實是技術工程與組織知識收集的混合工程。
- 可連結的現有卡片：[[一切都是 Context：對 AI 和對人的底層能力是同一個]]、[[Context 是增值型投資：維護的上下文隨 AI 進步而複利成長]]、[[Context Graph 捕獲組織隱性知識]]

---

## 全文翻譯

文章一開始先說，現在只要和任何正在做 data + AI agents 的組織聊天，幾乎都會談到 context layers 或 context graphs。原因很簡單：市場在過去一年已經慢慢認清，資料與分析 agent 如果沒有正確 context，幾乎是沒有用的。它們無法拆解含糊問題、無法理解業務定義，也無法跨多個異質資料來源做穩定推理。

作者先回顧了市場演化。第一階段是 modern data stack 的崛起。資料從分散來源被慢慢集中、轉換、清理，讓企業能在 warehouse 裡寫 SQL、做 dashboard、支撐 BI。第二階段是 2024 到 2025 的 agent frenzy，幾乎每家公司都想把 agent 疊在既有 data stack 之上，做 chat with your data、support agents 等等。第三階段則是撞牆。大家發現這些部署大多失敗，原因不是概念不對，而是 workflow brittle、缺少 contextual learning，也和日常實際運作脫節。

作者特別提醒，早期很多人以為問題只是模型的 SQL 能力不夠好。也就是說，只要 text-to-SQL 再進步一點，data agent 就能自然而然成功。但他們認為這只說對了一小部分。模型在 codegen 與數學推理上確實突飛猛進，但資料場景的問題遠超過 SQL 生成本身。

為了說明這件事，他們舉了個很典型的問題：「上季營收成長是多少？」看起來像簡單的 BI 問題，實際上卻充滿上下文陷阱。首先，agent 要知道 revenue 到底指什麼，是 run rate revenue、ARR、gross 還是 net；其次，quarter 的邏輯在不同公司可能不同；再來，就算公司有 semantic layer，裡面的 YAML 也可能是已離職同事留下的舊定義，不再被 BI 工具使用，甚至沒有包含最新產品線。換句話說，問題不只是 SQL，而是「今天真正在組織裡運作的業務語意與資料真相到底是什麼」。

這時文章提出 context layer 的概念。它可以有很多名字，像 context OS、context engine、contextual data layer、ontology，但底層概念一致：把企業混亂的資料串起來，在上面加一層能幫 agent 理解 business logic 的 contextual layer，然後把它包裝成 agent 可以實時存取的資產。

作者也很清楚處理了 semantic layer 與 context layer 的關係。他們不是說 semantic layer 沒用，而是說它不夠。傳統 semantic layer 對 revenue、churn、ARPU 這類指標定義很有價值，但它往往是資料團隊用專門語法手工建的，服務對象主要是 BI tool。要支撐真正自主的 agent，還需要更多：canonical entities、identity resolution、tribal knowledge 的拆解規則、governance guidance，甚至工作流與決策脈絡。換句話說，modern context layer 應該是 semantic layer 的超集。

文章接著提出一條很實用的五步驟實作路徑。第一步是 access the right data，先確保對的資料真的都能取到，不只 warehouse 裡的結構化資料，也包括 GDrive、Slack、內部文件等隱性知識來源。第二步是 automated context construction，利用 LLM 自動從 query history、dbt、LookML 等地方萃取高訊號 context。第三步是 human refinement，因為最重要的脈絡常常是隱性的、條件式的、歷史形成的，不是模型自己掃一圈就會懂，例如「2025 年後 USCAN 的新 deals 看 Affinity，之前的 global leads 看 Salesforce」。

第四步是 agent connection，也就是把這層 context 透過 API 或 MCP 接給 agents，讓它可以在運行時即時讀取。第五步是 self-updating context flows。這一點非常重要，因為資料系統永遠不會靜止。上游欄位會變、資料格式會變、商業定義會變、團隊也會對 agent 增加新規則。如果 agent 曾經回錯資料，修正不能只停在單次對話裡，而應該回灌到 context layer，讓系統下次更準。

作者因此把 context layer 描述成一個 living corpus，不是一次性建好就算了，而是持續演化的知識與規則體系。這和你在 repo / skill / note 裡做的事很接近，本質上都是把隱性脈絡變成可被系統重用的資產。

文章後半段把這件事拉回市場。作者認為不是每家企業都應該自己從頭打造這套 context layer，因此外部產品機會很大。目前市場大致分成三類：第一類是 data gravity platforms，例如 Databricks、Snowflake，已經掌握資料 ingestion、transformation、storage，並開始在平台上疊 AI data analyst 產品；第二類是既有 AI data analyst 公司，原本只做 chat with your data，後來逐漸發現 context layer 才是產品關鍵；第三類則是新興的 dedicated context layer 公司，從零開始專做 context 建構。

作者最後的觀察很務實。我們已經看見 context 不足是 agent 失敗的根本原因，但解法仍很早期，還有很多未解問題：context layer 應該住在哪、能否分散存在、會不會變成獨立產品。即便如此，方向已經很清楚了。真正能讓自助式 analytics、BI、data science 進一步被 AI 重寫的，不只是更強的模型，而是更完整、更活的 context infrastructure。

這篇文章的高訊號不在於它發明了新 buzzword，而是把 data agent 無法落地的核心瓶頸，從「模型不夠強」矯正成「上下文資產不夠完整、不夠新、不夠可維護」。如果你在寫「從資料平台到決策系統」，這幾乎就是其中最關鍵的一層中介結構。

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：data agent 失敗的瓶頸不是 text-to-SQL 不夠強，而是缺乏可維護、可演化、帶有業務定義與 tribal knowledge 的 context layer。Semantic layer 只解決指標定義，但 context layer 還需 canonical entities、identity resolution、tribal knowledge 拆解規則、governance guidance、workflow context。建構 context layer 是「技術工程 + 組織知識收集」的混合工程，文章給出五步驟路徑：access data → automated construction → human refinement → agent connection → self-updating flows。
- 作者挑戰的預設：（1）data agent 失敗 = 模型 SQL 弱 → 真正的 bottleneck 是 context；（2）有 semantic layer 就夠 → semantic layer 只是 context layer 的子集，缺 tribal knowledge 與 governance；（3）context layer 一次建好 → 必須是 living corpus，因為商業定義、資料源、規則持續變動。
- 個人映射：直接等同於你長期的「context-as-asset」「Context Graph 捕獲組織隱性知識」「context 是增值型投資」主軸；補上「人工 refinement 處理 conditional / historical / tribal knowledge」這個你之前沒明確命名的關鍵步驟；同時把 data agent 失敗原因從「模型」糾正到「context」對應你的「Repo as Worker / Context as Capability」橋接寫作。

## B. 候選卡（Lite）

序號 1
- 候選標題：Data Agent 失敗的真正瓶頸不是 SQL，而是 Context
- 分級：Core
- 類型：Principle
- 核心內容：早期假設「text-to-SQL 再進步一點 data agent 就會成功」是只說對一小部分。真正的問題是：agent 無法解模糊問題、不懂業務定義、無法跨異質資料源穩定推理。「上季營收成長」表面是 BI 問題，實際牽涉 revenue 定義（run rate / ARR / gross / net）、quarter 邏輯、semantic layer 是否被棄用、新產品線是否包含等多重 context 陷阱。
- 保留理由：把整個資料 agent 失敗論述從技術問題轉到組織知識問題，是這篇文章的母命題；對你「從資料平台到決策系統」的核心論述是基石。
- 待補強處：何時 SQL 能力仍是真正瓶頸（pre-paradigm 階段、純結構化資料）？context 不足與 SQL 不足的鑑別診斷？
- 初步知識鉤子：[[Context-as-Asset]]、[[Semantic Layer]]、[[Decision System]]

序號 2
- 候選標題：Context Layer ⊃ Semantic Layer：四件需要補上的東西
- 分級：Core
- 類型：Principle
- 核心內容：Modern context layer 是 semantic layer 的超集。Semantic layer 處理 revenue / churn / ARPU 等指標定義，主要服務 BI tool；要支撐 agent 自主推理，還需要：（1）canonical entities + identity resolution；（2）tribal knowledge 的拆解規則；（3）governance guidance；（4）workflow 與決策脈絡。前者是手工 YAML，後者是 living corpus。
- 保留理由：明確區分了兩個常被混為一談的概念，並給出 context layer 必須補的四件套清單。對你做 data product 設計與 RMN context 整合非常實用。
- 待補強處：四件套的優先順序？小團隊資源有限時應先做哪一件？
- 初步知識鉤子：[[Semantic Layer]]、[[Context Graph]]、[[Tribal Knowledge]]、[[Identity Resolution]]

序號 3
- 候選標題：Context Layer 必須是 Self-Updating Living Corpus，不是一次性建好
- 分級：Core
- 類型：Principle
- 核心內容：資料系統永遠不會靜止——上游欄位變、資料格式變、商業定義變、團隊持續對 agent 補規則。如果 agent 回錯，修正不能停在單次對話，要回灌到 context layer 讓系統下次更準。這對應你關心的「context 是增值型投資、隨 AI 進步複利成長」主張。
- 保留理由：把 context 從「文件 / 配置」抬升到「持續演化資產」的概念躍遷；對你寫「Context Engineering 的長期主義」是核心拼圖。
- 待補強處：self-updating 的觸發機制（每次失敗都更新？還是要批次審核？）；如何避免 context drift 累積偏誤？
- 初步知識鉤子：[[Context 是增值型投資]]、[[Living Corpus]]、[[Repo as Worker]]、[[Self-Updating Flow]]

序號 4
- 候選標題：人工 Refinement 處理 Conditional / Historical / Tribal Knowledge
- 分級：Core
- 類型：Pattern
- 核心內容：context layer 五步驟的第三步「human refinement」很關鍵，因為最重要的脈絡常常是隱性、條件式、歷史形成的——不是模型自動掃一圈就會懂。例：「2025 年後 USCAN 的新 deals 看 Affinity，之前的 global leads 看 Salesforce」。這類規則需要人工補進 context layer。
- 保留理由：把「人為什麼還必須介入 context」說得最具體；對應你關心的「Agent 落地是技術 + 組織知識的混合工程」主張。
- 待補強處：refinement 的 SOP？誰負責（業務 / 工程 / 數據治理）？版本管理？
- 初步知識鉤子：[[Tribal Knowledge]]、[[Conditional Rules]]、[[Human-in-the-Loop Curation]]

序號 5
- 候選標題：建構 Context Layer 是技術工程 + 組織知識收集的混合工程
- 分級：Support
- 類型：Principle
- 核心內容：作者明確指出 data agent 工程不只是技術問題，而是「technical engineering + organizational knowledge gathering」的混合工程。這意味資料工程團隊必須擴大職責範圍，或與業務 / RevOps / GTM 等角色形成新的協作模式。
- 保留理由：把 data agent 落地從「資料工程任務」拉高到「跨職能組織任務」，影響團隊組成與責任分工。對你關心的「Solo / 小團隊如何在資源約束下落地 data product」很有用。
- 待補強處：跨職能協作的具體機制？哪些角色必須加入？外部顧問可不可以替代部分職責？
- 初步知識鉤子：[[Solo Consultant 服務包裝]]、[[小團隊資源約束]]、[[組織知識]]

序號 6
- 候選標題：Context Layer 市場三類玩家：Data Gravity / AI Data Analyst / Dedicated Context
- 分級：Support
- 類型：Pattern
- 核心內容：作者把市場分成三類：（1）data gravity platforms（Databricks、Snowflake，從資料源頭往上延伸做 AI data analyst）；（2）既有 AI data analyst 公司（從 chat with data 往下深化做 context layer）；（3）新興 dedicated context layer 公司（從零專做 context）。三類路徑不同、優劣勢不同。
- 保留理由：給出一個觀察 data + AI 市場演化的清晰分類，對你做 D2D Architect 定位 / 競爭分析 / 客戶選擇有用。
- 待補強處：三類玩家在哪些客戶情境分別更有優勢？台灣 / 亞太市場是否同樣分類成立？
- 初步知識鉤子：[[Databricks 生態]]、[[Modern Data Stack 演化]]、[[市場結構分析]]、[[D2D Architect 競品定位]]

序號 7
- 候選標題：未解問題：Context Layer 應該住在哪裡？會變成獨立產品嗎？
- 分級：Question
- 類型：Question
- 核心內容：作者誠實指出方向已清楚但解法仍早期，幾個未解問題：context layer 的物理位置（雲端集中？分散在各應用層？）、能否分散存在、會不會變成獨立產品類別、與既有 catalog / lineage 工具的關係。值得長期追蹤。
- 保留理由：作者沒給答案的開放問題，正好是寫作 hook 的好材料；可作為追蹤命題持續累積觀察。
- 待補強處：自己對這幾個問題的初步傾向是什麼？
- 初步知識鉤子：[[Context Layer 演化]]、[[Data Catalog]]、[[追蹤命題]]

## C. 建議送 refine 的項目
- 序號 1（Core）：Data Agent 真正瓶頸是 Context
- 序號 2（Core）：Context Layer ⊃ Semantic Layer 四件套
- 序號 3（Core）：Self-Updating Living Corpus
- 序號 4（Core）：人工 Refinement 處理隱性知識
- 序號 5（Support）：技術 + 組織知識的混合工程
- 序號 6（Support）：市場三類玩家
- 序號 7（Question）：保留作為追蹤命題

## D. 呼叫 refine-cards
- 上述 7 張候選卡交由 refine-cards 精煉；refine 階段需檢查與既有「[[Context 是增值型投資]]」「[[一切都是 Context]]」「[[Context Graph 捕獲組織隱性知識]]」三張現有卡的去重 / 連結關係——可能某些 lite 卡片應強化既有卡而非新建。

