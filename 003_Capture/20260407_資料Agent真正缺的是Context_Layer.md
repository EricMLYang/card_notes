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
