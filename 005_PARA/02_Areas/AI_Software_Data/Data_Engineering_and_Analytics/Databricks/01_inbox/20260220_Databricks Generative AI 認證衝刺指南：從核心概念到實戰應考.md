---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-20
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# **Databricks Generative AI 認證衝刺指南：從核心概念到實戰應考**

## **摘要**

本指南專為尋求快速通過 Databricks Certified Generative AI Engineer Associate 認證的技術專業人士設計。內容完全貼合官方考試大綱，旨在為備考時間有限、但需要迅速掌握核心技能的學員，提供一條最高效率的學習路徑。

本指南採用「白話」風格，將複雜的 AI 世代模型（Generative AI）概念，與 Databricks 平台上的具體服務（如 Vector Search, MLflow, Model Serving）進行一對一的緊密連結。我們將嚴格遵循「AI 概念 > Databricks 服務 > 細部技巧」的學習路徑，並在每一章節中，反覆貫徹一個核心應考心法：「Databricks 優先原則」。此原則強調，在考試中，最佳答案永遠是 Databricks 平台提供的原生、整合、自動化解決方案。

內容涵蓋完整的關鍵名詞定義、官方六大考試單元（設計、資料準備、開發、部署、治理、監控）的深度解析，並結合考古題情境，提供可立即應用的實戰策略。本指南的目標不僅是幫助學員通過認證，更是要建立一套可實際應用的知識框架，將 Databricks 上的 GenAI 解決方案從概念付諸實現。



---



# **第一部分：建立地圖 — 核心概念與關鍵詞彙 (The Glossary)**

## **引言**

本章節是您進入 Databricks GenAI 世界的「字典」。在 Databricks 的平台上，抽象的 AI 概念和具體的平台服務是緊密綁定、不可分割的。我們將用最口語化、最易懂的比喻，幫您建立這兩者之間的「連結」。在深入學習六大單元之前，熟悉這些「黑話」將使您的學習事半功倍。

## **1\.1 AI 基礎詞彙 (白話解析)**

### **LLM (大語言模型)**

- **白話解釋**：您可以想像 LLM (Large Language Model) 是一個讀過網路上幾乎所有資料、超級聰明的「大腦」1。它非常擅長「接龍」和「總結」。您給它一段話，它能基於龐大的統計知識，猜出下一個最合理的字詞，並依此生成流暢的文章、回答百科全書式的問題、翻譯語言，甚至編寫程式碼 2。

- **認證意涵**：在 Databricks 認證中，LLM 是您要「使用」、「部署」和「服務」的核心對象。

### **RAG (檢索增強生成)**

- **白話解釋**：LLM 這個「大腦」雖然聰明，但有兩大缺陷：(1) 它的知識是「舊」的，只停留在訓練截止的那一天 3；(2) 它不知道您公司的「內部機密」資料 3。RAG (Retrieval-Augmented Generation) 就是為了解決這個問題，讓大腦可以「開卷考試」4。

- **流程**：RAG 的流程就像是「先翻書、再回答」4。(1) **檢索 (Retrieval)**：當您問問題時，系統*不會*馬上問 LLM。它會先去您的「外部知識庫」（例如公司手冊 PDF、Wiki）5，「找」出最相關的幾段內容 7。(2) **增強 (Augmented)**：它會把「您的原始問題」和「找到的參考資料」打包成一個便當盒（即新的 Prompt）4。(3) **生成 (Generation)**：最後，把這個「便當盒」交給 LLM，並命令它：「請根據*這些*參考資料，回答這個問題」4。

- **認證意涵**：RAG 是本次認證*最核心*的應用場景。Databricks 平台上的許多服務（如 Vector Search）都是為了實現高效、可擴展的 RAG 而設計的 8。

### **AI Agent (AI 代理)**

- **白話解釋**：如果說 RAG 是一個「博學的學者」（只會查資料和回答），那麼 AI Agent (AI 代理) 就是一個「能幹的助理」（會動手做事）10。

- **能力**：Agent 的核心能力是「使用工具 (Tools)」12。它不僅能呼叫 LLM 進行思考，還能根據您的任務，自主「規劃步驟」並決定使用哪些工具 10。這些工具可以是：(1) 呼叫外部 API（例如：查天氣、查股價、訂機票）；(2) 查詢 SQL 資料庫；(3) 執行程式碼；(4) 甚至將 RAG 本身也當作一個「查資料」的工具 12。

- **認證意涵**：RAG 和 Agent 是考試中的兩大架構。您必須清楚知道何時該用 RAG（基於靜態知識回答），何時該用 Agent（執行動態任務、串聯多種工具）13。

### **Embeddings (嵌入)**

- **白話解釋**：電腦本質上看不懂中文或英文，它們只看得懂數字。Embeddings 就是一個「翻譯蒟蒻」，負責把「文字」翻譯成一長串的「數字座標」（即高維向量）14。

- **特性**：這種翻譯非常巧妙。在產生的「座標空間」中，語意相近的詞（例如「貓」和「狗」）會被放在很近的位置；而語意毫不相關的詞（例如「貓」和「游泳」），它們的座標就會離很遠 14。

- **認證意涵**：Embeddings 是 RAG 的技術基石。RAG 之所以能「檢索」到相關內容，就是因為它先把所有文件切塊、轉換成 Embeddings 座標，然後在「座標空間」中快速「搜尋」與您問題座標最接近的那些文件塊。

### **Fine-tuning (微調)**

- **白話解釋**：如果說 RAG 是讓 LLM「開卷考試」（提供外部知識），那麼 Fine-tuning (微調) 就像是為 LLM 請「一對一的家教」（調整內部知識）15。

- **目的**：微調的主要目的*不是*教 LLM 全新的知識（那太昂貴且效果不彰），而是「調整它的說話風格」或「強化特定領域的專業術語」15。例如，您可以微調一個通用 LLM，使其學會用「專業客服人員的禮貌口吻」來回答問題，或者讓它更精準地理解「法律」或「醫療」領域的專有名詞 15。

- **認證意涵**：考試會強調，在考慮昂貴且複雜的微調之前，應優先嘗試 RAG 15 和 Prompt Engineering，它們是 CP 值更高的解決方案。

### **Prompt Engineering (提示工程)**

- **白話解釋**：這是一門「如何對 AI 下對指令」的藝術 17。您問問題的方式，會極大地影響 AI 回答的品質。

- **核心技巧**：

- **Zero-shot (零樣本)**：不給任何範例，直接下達指令。（例如：「請把這段話翻譯成法文」）17。

- **Few-shot (少樣本)**：在下指令的同時，給 AI「幾個完整的範例」17。這對「格式化輸出」或「複雜任務」極為有效。（例如：「'蘋果' 翻成 'Apple'。'香蕉' 翻成 'Banana'。現在，請把 '櫻桃' 翻成...?」）18。

- **認證意涵**：這是「應用程式開發」（佔 30%）單元的核心考點。許多考題會測試您如何使用 Few-shot 技巧來修正 AI 的輸出格式或行為。

## **1\.2 Databricks 關鍵服務 (功能對照)**

### **Unity Catalog (UC)**

- **白話解釋**：Databricks 平台的「中央警衛室」和「總圖書館」。

- **功能**：UC 是 Databricks 實現統一治理的核心 20。它是一個「單一的」中繼存放區，用來定義和管理「所有」資料和 AI 資產的權限、血緣和版本 20。

- **洞察**：在 Databricks 的世界裡，UC 不是一個可選項，它是*一切的基礎*。它管理的「資產」包括：

1. **資料 (Tables)**：傳統的表格資料。

2. **非結構化檔案 (Volumes)**：RAG 需要的 PDF, TXT 等 20。

3. **AI 模型 (Models)**：MLflow 註冊的模型 22。

4. **向量索引 (Vector Search Indexes)**：Vector Search 的索引 23。

- **認證意涵**：考試中任何關於「治理 (Governance)」、「權限 (Permissions)」、「註冊 (Registry)」或「資料血緣 (Lineage)」的問題，其正確答案*必定*會包含 Unity Catalog 20。

### **UC Volumes (UC 卷)**

- **白話解釋**：Unity Catalog 裡的「非書區」或「檔案櫃」。

- **功能**：在 UC 統一治理的框架下，專門用來儲存、管理和保護「非表格」資料（如 PDF, TXT, Word, 圖像等）20。

- **認證意涵**：UC Volumes 是 Databricks 平台上 RAG 應用程式的「第一站」。您的原始文件（如 PDF 手冊）就應該存放在這裡，以便進行後續的處理和索引 6。

### **Vector Search (向量搜尋)**

- **白話解釋**：Databricks 內建的「AI 專用搜尋引擎」，一個原生的向量資料庫 8。

- **功能**：這是一個 Serverless (無伺服器) 服務，專門用來高效儲存和快速查詢海量的 Embeddings（向量座標）8。

- **認證意涵**：這是 Databricks 平台 RAG 解決方案的核心 8。它與平台深度整合，例如，它的安全控管和權限是直接由 Unity Catalog 統一管理的 23。

### **Delta Sync Index (Delta 同步索引)**

- **白話解釋**：Vector Search 提供的「全自動更新」功能 25。

- **功能**：Vector Search 提供兩種索引模式 25：(1) Direct Vector Access Index（需手動 API 更新）25 (2) Delta Sync Index（自動同步）。

- **洞察**：Delta Sync Index 是 Databricks 優先原則的體現。它能「監視」您指定的一張 Delta Lake 表（即您的資料來源），只要這張表有任何新增、修改或刪除，Vector Search 索引就會「自動且增量地」同步更新 25。這免去了手動維護資料管線的巨大痛苦。

- **認證意涵**：(考古題 Q7) 建立 Vector Search Endpoint 後的下一步是什麼？標準答案就是 vsc.create_delta_sync_index() 25。考試在測試您是否知道這個*自動化*、*整合*的原生功能。

### **MLflow**

- **白話解釋**：AI 專案的「全能專案管理系統」29。

- **功能**：MLflow 是一個開源平台，但在 Databricks 上被深度整合，是 MLOps 的靈魂 22。在 GenAI 時代，它的核心組件被賦予了新任務 32：

- **Tracking (追蹤)**：記錄 Prompt 實驗、參數、評估指標 22。

- **Models (打包)**：將您的「提示 + 模型 + 程式碼」打包成標準格式 (MLflow PyFunc) 22。

- **Registry (註冊)**：將打包好的模型註冊到 **Unity Catalog**，進行版本控制和權限管理 22。

- **Tracing (追蹤)**：(MLflow 3.0+ 新功能) 深入追蹤 RAG 和 Agent 應用的每一步執行細節，方便除錯 32。

- **認證意涵**：MLflow 貫穿了「開發」、「部署」和「監控」三大單元，是必考重點。

### **Model Serving (模型服務)**

- **白話解釋**：將您註冊在 Unity Catalog 裡的 AI 模型，「一鍵」變成一個穩定、可擴展的「API 服務」的工具 2。

- **功能**：提供高可用、低延遲、自動擴展的 REST API 端點，支援 CPU 和 GPU 2。

- **認證意涵**：這是 AI 專案「上線產生價值」的最後一哩路。考試會重點測試您如何為不同情境選擇「服務模式」（詳見 2.4 節）。

### **Inference Tables (推論表)**

- **白話解釋**：Model Serving 內建的「自動監視器」和「日誌記錄器」37。

- **功能**：當您在啟用 Model Serving 端點時，只需「打一個勾」，Databricks 就會「自動」把所有傳入的請求 (Prompts) 和傳出的回應 (Responses) 完整地記錄到一張 **Unity Catalog** 的 Delta 表中 37。

- **洞察**：(考古題 Q1) 這再次體現了「Databricks 優先原則」。當被問及如何監控端點時，標準答案*不是*自訂微服務或手動 logging，而是使用這個*自動化*、*原生*、且*與 UC 整合*的 Inference Tables。

- **認證意涵**：Inference Tables 是「監控」單元的標準答案 37。

### **Feature Serving (特徵服務)**

- **白話解釋**：專門為模型提供「即時」特徵資料的「高速通道」39。

- **功能**：RAG 不只可以查 PDF，有時也需要查詢「結構化資料」（例如：資料庫裡的最新庫存、用戶的即時位置）6。Feature Serving 讓我們能以極低的延遲，從 Delta Table 中撈取這些「即時特徵」40。

- **認證意涵**：(考古題 Q30) 提到「即時體育評論」需要「最新遊戲分數」，這就是 Feature Serving 的完美場景。它補足了 Vector Search（用於非結構化資料）之外的 RAG（用於結構化資料）的能力 6。

## **1\.3 關鍵表格（一）：AI 概念 vs. Databricks 服務對照表**

**目的**：本表總結了第一部分，幫助學員快速將「要做的事」（AI 概念）對應到「該用的工具」（Databricks 服務）。這是「Databricks 優先原則」的實踐地圖

| **AI 概念 (我想做...)** | **Databricks 解決方案 (你該用...)** | **白話解釋** | 
|---|---|---|
| 儲存非結構化資料 (PDF, Doc) | Unity Catalog Volumes 20 | 存放文件的「資料夾」。 | 
| 儲存與搜尋向量 (Embeddings) | Databricks Vector Search 8 | AI 專用的「座標搜尋引擎」。 | 
| 自動更新向量索引 | Delta Sync Index (Vector Search 功能) 25 | 源頭資料一改，索引就「自動」更新。 | 
| 統一管理資料/模型權限 | Unity Catalog 20 | 平台的「中央警衛室」和「總圖書館」。 | 
| 追蹤實驗、打包模型 | MLflow 22 | AI 專案的「專案管理系統」。 | 
| 將模型部署為 API | Databricks Model Serving 35 | 幫模型開一個「線上服務窗口」。 | 
| 監控 API 流量 (輸入/輸出) | Inference Tables (Model Serving 功能) 37 | 服務窗口的「自動監視器」和「日誌」。 | 
| RAG 需即時存取結構化資料 | Databricks Feature Serving 42 | 連接資料庫的「即時資料通道」。 | 



---



# **第二部分：AI 應用實戰 — 串聯 Databricks 服務的完整生命週期**

## **引言**

本章節是課程的主體核心。我們將完全依照 Databricks 官方的六大考試單元 44，從「設計」開始，一路經過「資料準備」、「開發」、「部署」，最後到「治理」與「監控」，一步步帶您走完一個 GenAI 專案的完整生命週期。

在每一節中，我們都會將抽象的「AI 概念」，連結到具體的「Databricks 服務」，並補充通過認證所必需的「細部技巧」與「考古題情境」。

## **2\.1 單元一：應用程式設計 (Design Applications, 14%)**

### **2\.1.1 AI 概念：RAG vs. Agent 架構選型 (核心考點)**

設計是專案的起點，錯誤的架構選型將導致專案從一開始就注定失敗。此單元的核心便是評估 RAG 與 Agent 的適用情境。

- **RAG (檢索增強生成)**：

- **何時使用**：當您的核心需求是「**根據靜態知識庫回答問題**」時 3。RAG 專注於從「已知的」、「靜態的」資料來源（如內部文件、手冊）中檢索知識，以提供準確且可溯源的答案。

- **範例**：公司 HR 手冊問答機器人、產品說明書查詢、歷史財報分析。

- **Databricks 實現**：使用 **Unity Catalog Volumes** 儲存文件 6，並使用 **Vector Search** 建立索引 8。

- **AI Agent (AI 代理)**：

- **何時使用**：當您的核心需求是「**執行多步驟任務**」或「**與動態/外部系統互動**」時 11。Agent 專注於「執行」和「協調」，它可以使用工具（Tools）來處理「動態資料」或「採取行動」10。

- **範例**：

1. 「幫我查明天台北的天氣，如果下雨就發送提醒郵件」（需呼叫「天氣 API」和「郵件 API」）。

2. 「幫我從 Delta 表中查詢昨天的銷售冠軍，並在 Slack 上公布」（需「查詢 SQL」和「呼叫 Slack API」）。

- **Databricks 實現**：使用 **LangChain** 框架 46，定義 Agent 和可用的 **Tools**（例如 SQL 查詢工具、API 呼叫工具等）。

### **2\.1.2 應考技巧與考古題解析**

考試會透過「**資料源的特性**」來考察架構選擇。

- 如果資料是「靜態的」、「內部的」、「非結構化文件 (PDF, Wiki)」 -> 答案選 **RAG**。

- 如果資料是「動態的」、「外部的」、「需呼叫工具 (API, SQL, Web Search)」 -> 答案選 **Agent**。

**考古題解析**：

- **(考古題 Q28)**：應用程式需同時存取「**最新新聞（網路）**」和「**股價（Delta tables）**」。

- **分析**：「最新新聞」和「股價」都是動態資料，且需要「網路搜尋」和「SQL 查詢」這兩種「工具」。這是典型的「工具調用」場景，因此答案是 **Agent**。

- **(考古題 Q29)**：需回答關於怪獸卡車隊的「**文字問題（RAG）**」、「**賽事日期（API）**」和「**排名（TABLE）**」。

- **分析**：這是一個需要協調多種工具（RAG 知識庫、API、SQL 資料庫）的複雜任務，唯一能擔任「協調者」角色的，就是 **Agent**。

### **2\.1.3 AI 概念：模型選擇 (成本、效能、領域)**

選擇基礎模型 (Foundation Model) 並非「越大越好」，而是一個工程權衡。

- **選擇標準**：

- **成本 (Cost)**：(考古題 Q20) 一家「**成本敏感**」的新創公司，應選擇「**更小、特定領域**」的 LLM，而非「可能的最大 LLM」。

- **領域 (Domain)**：(考古題 Q16) 需要為軟體團隊提供「**程式碼生成模型**」，應優先選擇專門為程式碼生成的模型（如 CodeLlama），而非通用的 Llama2。

- **延遲 (Latency)**：即時聊天機器人需要低延遲模型，而離線分析則可容忍高延遲但更強大的模型。

- **上下文視窗 (Context Window)**：RAG 應用塞入的「參考資料」總長度，不能超過模型的上下文視窗（詳見 2.2.3 節）。

## **2\.2 單元二：資料準備 (Data Preparation, 14%)**

### **2\.2.1 AI 概念：RAG 的資料流程 — 從 PDF 到向量**

在 RAG 應用中，回答品質的上限取決於「檢索」的品質，而檢索的品質完全取決於「資料準備」。這就是 RAG 的「備料」過程。

- **步驟**：

1. **擷取 (Ingest)**：從來源（如 PDF, HTML, Word）提取純文字。

2. **分塊 (Chunking)**：將大型文件切割成較小、語義連貫的「塊」47。這是最關鍵的步驟之一，因為「塊」的大小和內容，直接決定了檢索的精準度。

3. **嵌入 (Embed)**：使用嵌入模型（如 BGE-large），將每一個「塊」轉換為「向量座標」（Embeddings）。

4. **索引 (Index)**：將這些「向量座標」連同其原始文本，存入向量資料庫中，以備搜尋。

### **2\.2.2 連結 Databricks 服務：Lakehouse 原生 RAG 管線**

Databricks 平台為上述流程提供了高度整合的原生管線：

- **步驟 1：資料存放**：原始的 PDF, TXT 等非結構化檔案，應存放在 **Unity Catalog Volumes** 20。

- **步驟 2：資料塑形**：(考古題 Q36) 使用 unstructured 等 Python 函式庫解析 Volumes 中的文件。接著 (考古題 Q34)，最佳實踐是將分塊後的資料「**扁平化 (Flatten)**」，整理成「**一行一塊 (one chunk per row)**」的結構，並儲存為一張 **Delta Table**。

- **步驟 3：建立索引 (核心考點)**：

- **"Databricks 優先原則" 的體現**：您*不應該*手動將 Delta Table 的資料 write 到 Vector Search。

- **正確做法**：使用 **Databricks Vector Search** 8，並呼叫 vsc.create_delta_sync_index() 25。

- **為什麼**：(考古題 Q7) 這條指令是 Databricks RAG 生態的核心。**Delta Sync Index** 25 會自動監控您在步驟 2 建立的那張 Delta Table。當源頭資料有任何更新時，向量索引會「**自動增量更新**」，完全無需您手動維護任何ETL管線 8。

### **2\.2.3 細部技巧：Chunking 與 Token 錯誤**

- **Chunking 策略**：(考古題 Q25) 考試強調，優化分塊策略（例如，塊的大小、重疊的長度）必須是「**指標驅動 (metric-driven)**」和「**系統性實驗**」的過程，*絕非*憑「直覺」選擇。

- **Token 超限錯誤 (考古題 Q44)**：

- **情境**：RAG 系統報錯 prompt token count (4595) cannot exceed 4096。

- **白話解析**：您塞給 LLM 的「考卷 + 參考資料 + 問題」總長度太長了，大腦 (LLM) 一次讀不完（即超過了 4096 Token 的上下文視窗）。

- **公式**：總 Token = 系統提示 + 檢索到的文件塊 (k) + 用戶問題。

- **解決方案**：

1. **減少 k**：減少檢索回來的「文件塊數量」（例如：從檢索 5 塊減為 3 塊）。

2. **縮小 chunk size**：在「資料準備」階段（步驟 2），就把每一「塊」切得更小一點。

## **2\.3 單元三：應用程式開發 (Application Development, 30%)**

此單元佔比高達 30%，是考試中最重要的部分。重點在於如何控制模型的「輸入」（提示）和「輸出」（回應）。

### **2\.3.1 AI 概念：提示工程 (Prompt Engineering)**

這是 CP 值最高的技巧。在花大錢微調之前，永遠先嘗試「改提示」。

- **Few-shot (少樣本學習)**：

- **情境**：(考古題 Q2) LLM 產生摘要時，會附帶「多餘的解釋文字」，這是不希望的。

- **最佳解法**：D. 「**提供所需輸出格式的 Few-shot 範例**」17。與其用複雜的後處理程式碼去「分割」輸出，不如直接在提示中給 LLM 幾個「這才是我要的答案」的範例。

- **LangChain 實現**：使用 FewShotPromptTemplate 19，它可以幫您結構化地管理這些範例，並與用戶的即時問題組裝成最終的 Prompt。

### **2\.3.2 細部技巧：結構化輸出 (JSON)**

- **情境**：(考古題 Q3, Q8) 應用程式需要 LLM 穩定輸出「**結構化 JSON**」格式，以便下游程式碼（如 API）進行解析。

- **最佳解法**：(考古題 Q3, Q8) 僅有指令是不夠的。最佳實踐是「**明確指令」 + 「Few-shot 範例」**。

- **白話指令**：「你必須回傳 JSON。這是一個範例：{'key': 'value'}」。

- **LangChain 實現**：

- **PydanticOutputParser**：這是 LangChain 中強大且常見的做法。您只需定義一個 Pydantic BaseModel 來描述您要的 JSON 結構 50，LangChain 就會自動幫您從 BaseModel 生成提示指令（parser.get_format_instructions() 52），並在 LLM 回應後驗證及解析輸出 53。

- **.withStructuredOutput()**：新版的 LangChain 和 Databricks 支援更簡單的方法 54。您可以直接將 Pydantic class 或 JSON schema 傳給模型 54，模型會強制依此格式輸出。

### **2\.3.3 連結 Databricks 服務：MLflow PyFunc (打包神器)**

- **情境**：(考古題 Q23) 如何在將 Prompt 發送給 LLM *之前*，用「**自訂程式碼**」進行預處理（例如，從 Feature Serving 獲取即時資料來充實 Prompt）？

- **"Databricks 優先原則"**：

- **錯誤答案**：手動寫一個 Flask API。

- **正確答案**：D. 「**編寫一個 MLflow PyFunc 模型...**」。

- **為什麼**：**MLflow PyFunc** 22 是 Databricks 的標準模型打包格式。它不僅能打包「模型」本身，還能將「(1) 預處理邏輯」+「(2) 模型呼叫（即使是呼叫外部 OpenAI API）」+「(3) 後處理邏輯（如解析 JSON）」*全部封裝*在一個物件中 22。這個物件隨後可以被 MLflow 追蹤 56、註冊到 UC 22，並無縫部署到 Model Serving 33。

## **2\.4 單元四：應用程式組裝與部署 (Assembling and Deploying Apps, 22%)**

此單元佔比 22%，是考試的第二大單元。模型開發完畢，必須將其部署為穩定的 API 服務，才能產生商業價值。

### **2\.4.1 連結 Databricks 服務：MLflow 部署流程 (核心考點)**

- **情境**：(考古題 Q6) 部署已訓練 LLM 的「**最簡單流程**」是什麼？

- **"Databricks 優先原則"**：

- **錯誤答案**：手動 pickle 模型、手動打包 Docker 容器、手動編寫 Flask 應用程式 33。

- **正確答案**：B. 「**Log the model using MLflow (記錄) -> register the model to Unity Catalog (註冊到 UC) -> and start a serving endpoint (啟動服務)**」22。

- **分析**：這條路徑是 Databricks MLOps 的「標準高速公路」。它利用 MLflow 29 進行標準化打包，利用 Unity Catalog 22 進行統一治理和版本控制，並利用 Model Serving 35 進行一鍵部署。

### **2\.4.2 連結 Databricks 服務：Model Serving 模式選擇 (核心考點)**

Databricks Model Serving 2 提供兩種主要的部署（收費）模式，您必須能為特定情境選擇「最適合」的模式。

- **關鍵表格（二）：Model Serving 模式選擇**

- **目的**：(考古題 Q18) 是此單元的必考題。此表總結了兩種模式的關鍵差異。

| **比較維度** | **Provisioned Throughput (預留吞吐量)** | **Pay-per-token (按 Token 計費)** | 
|---|---|---|
| **白話比喻** | 包下一台專用伺服器 (吃到飽) | 按使用量付費 (搭計程車) | 
| **適用情境** | 生產環境、高流量、低延遲要求 2 | 開發測試、低流量、成本敏感 | 
| **成本** | 較高 (固定成本) | 較低 (變動成本)，用才付錢 35 | 
| **啟動速度** | 較慢 (需預熱時間) | 立即 (Serverless) 35 | 
| **考試關鍵字** | Production, Low Latency, High QPS | Cost-effective, Development, Low traffic | 

- **考古題解析 (Q18)**：情境提到「**請求量不夠高**」，無法使用 Provisioned Throughput，需考慮「**成本效益 (cost-effectiveness)**」。

- **分析**：關鍵字 100% 吻合，答案顯然是 **Pay-per-token** 35。

### **2\.4.3 連結 Databricks 服務：Feature Serving**

- **情境**：(考古題 Q30) 一個即時體育評論平台，需要「**即時資料（最新遊戲分數）**」來生成分析。

- **白話解析**：RAG 不只要查「靜態 PDF」（用 Vector Search），有時也要查「動態的結構化資料」（如資料庫）6。

- **正確答案**：C. **Feature Serving** 41。

- **分析**：Feature Serving 專門為即時推論（real-time inference）提供來自 Delta Table 的低延遲資料 40。這區分了 RAG 的兩種資料來源：

- Vector Search = 服務「非結構化」資料的 RAG。

- Feature Serving = 服務「結構化」資料的 RAG 6。

## **2\.5 單元五 & 六：治理 (Governance, 8%) 與 評估與監控 (Evaluation & Monitoring, 12%)**

這兩個單元佔比雖小，但重要性極高。GenAI 的風險（幻覺、資料外洩、惡意使用）遠高於傳統 ML，治理和監控是確保企業敢於將其推向生產的「煞車系統」。

### **2\.5.1 治理：Databricks 的「安全網」**

- **連結 Databricks 服務**：

- **Unity Catalog (UC)**：20 治理的基石。Databricks 上的「治理」幾乎等同於 UC。透過 UC，您可以精細控制「誰」可以存取「哪些」資料 24、Volumes 20、模型 22，並自動記錄稽核日誌 (audit logs) 20。

- **AI 概念：Safety Guardrails (安全護欄)**：

- **情境**：(考古題 Q24) 如何防範「**惡意用戶輸入 (malicious user inputs)**」？(考古題 Q41) 聊天機器人「**不得 (must not)**」回答政治問題。

- **白話解析**：這是在 LLM 的「輸入端」和「輸出端」加裝「過濾器」，用於實現「內容限制」和「主題對焦」。

- **正確答案**：A. **Safety Guardrail** (安全護欄)。

- **治理不能靠「期望」**：

- (考古題 Q37) 問哪一項「**不**」應用於緩解幻覺或資料外洩？

- **答案**：B. 「在你的資料上微調模型，*期望* (hoping) 它能學會...」。

- **分析**：這揭示了考試的核心觀點：治理必須依靠「**明確的工程工具**」（如 Guardrails, UC 存取控制, 強系統提示），*而不是*依靠「期望」或「祈禱」模型在微調後能「學會」不犯錯。

### **2\.5.2 監控：啟用「自動監視器」**

- **情境**：(考古題 Q1) 如何監控 RAG 應用的服務端點的「**傳入請求**」和「**傳出回應**」？

- **"Databricks 優先原則" 的終極體現**：

- **錯誤答案**：A. 自訂一個 micro-service 來監控。

- **正確答案**：D. **Inference Tables** (推論表) 37。

- **為什麼**：Inference Tables 是 Databricks Model Serving 的*原生功能* 37。它*自動化* 38 記錄所有流量，並將其寫入*整合*的 **Unity Catalog** Delta 表 37。這完美符合「Databricks 優先」的所有標準（原生、自動化、整合 UC）。

### **2\.5.3 評估：RAG 系統的「雙重健檢」**

- **白話解析**：RAG 應用程式如果回答錯誤，有兩種可能：

1. 「**檢索器 (Retriever)**」出錯：Vector Search 找錯了參考資料。

2. 「**生成器 (Generator)**」出錯：LLM 看著對的資料，但「腦補」或「總結」錯了。

- **RAG 評估的二元性**：

- **情境**：(考古題 Q15) RAG 應用返回「**不相關的產品**」資訊。

- **第一步**：A. 「**評估檢索到的上下文的品質**」。

- **分析**：在您花錢更換更貴的 LLM（生成器）之前，必須先檢查「檢索器」是否從 Vector Search 抓對了資料。

- (考古題 Q38) 也印證了這一點：最佳的「正式評估 (formally evaluate)」方式，是建立一個可以「**分別 (separately)**」測試檢索和生成元件的資料集。

- **AI 概念：LLM-as-a-judge**：

- **白話解析**：如何評估 LLM 回答的「品質」（例如：相關性、流暢性、忠實性）？這些指標很難用程式碼寫死。

- **解法**：使用另一個（通常更強大的，如 GPT-4）LLM 來當「**裁判 (Judge)**」，對「受測 LLM」的答案進行評分 57。

- **Databricks 實現**：(考古題 Q25) 提到此方法。Databricks 提供了 judges.custom_prompt_judge() 58 等 API 來實現此功能。



---



# **第三部分：通關秘笈 — 應考策略與學習路徑**

## **3\.1 核心心法：再次貫徹「Databricks 優先原則」**

- **白話總結**：這張認證是 Databricks 辦的，它唯一的核心目的，就是測試您會不會用「**Databricks 的方法**」來解決 GenAI 問題。

- **黃金法則**：在考試中面對任何情境題時，永遠要優先選擇最能體現 Databricks 平台「**原生**」、「**整合**」、「**自動化**」和「**Serverless**」優勢的那個選項。任何「手動」、「自訂」、「外部」或「非整合」的選項，即使在技術上可行，也極有可能是陷阱。

- **實戰演練 (回顧)**：

- (Q1) 監控？ -> 選原生的 **Inference Tables** 37。

- (Q6) 部署？ -> 選整合的 **MLflow + UC + Model Serving** 流程 22。

- (Q7) 索引？ -> 選自動化的 **create_delta_sync_index** 26。

- (Q18) 成本？ -> 選 Serverless 的 **Pay-per-token** 35。

- (Q23) 打包？ -> 選標準的 **MLflow PyFunc** 22。

- **結論**：掌握這一條黃金法則，您就掌握了考試 50% 以上的「隱藏分數」。

## **3\.2 推薦學習路徑與資源**

- **步驟一：打好地基 (免費)**：

- Databricks Academy 上的免費徽章是必修課。它們能幫您建立對平台的基本認知。

- **Databricks Fundamentals Badge** 59。

- **Generative AI Fundamentals Badge** 59。

- **步驟二：實戰為王 (Hands-on)**：

- 多位成功考生的經驗均證實，「**實作**」是通過此認證的唯一捷徑。

- **建議專案**：請務必親手使用 Databricks Notebook，搭配 **LangChain** 63，完整搭建一個 RAG 專案。

- **建議的專案流程（100% 覆蓋考點）**：

1. 在 **UC Volumes** 儲存 PDF 檔案。

2. 編寫程式碼解析文件、分塊，並將結果存入 **Delta Table**。

3. 建立 **Vector Search** 端點，並使用 **Delta Sync Index** 自動同步 Delta Table。

4. 使用 **LangChain** 建立一個 RAG 檢索鏈。

5. 將整條 RAG 鏈打包為 **MLflow PyFunc**。

6. 將 PyFunc 模型註冊到 **Unity Catalog**。

7. 將模型部署到 **Model Serving**（可測試 Pay-per-token 模式）。

8. 在端點上啟用 **Inference Tables**。

- **分析**：只要您親手完成這個流程，您就等於把六大考試單元 44 全部實作並理解了一遍。

## **3\.3 應試技巧**

- **不計分題**：官方規格說明考試包含 45 道「計分」題 65。但您在實際考試中可能遇到 50 題以上。多出來的是不計分的統計題目，用於未來設計考題。請不要因此慌張，這是正常現象。

- **時間管理**：90 分鐘 45 題 65，平均 2 分鐘一題。多位考生的經驗是時間「剛好」或「幾乎用滿」。請務必利用所有時間，不要提前交卷，應反覆檢查標記的題目。

- **系統性排除法**：這套方法被證實非常有效：

1. **讀題**：完整閱讀並理解問題。

2. **掃描**：快速掃描所有答案選項。

3. **排除**：排除 2 個或更多明顯不正確的答案（通常是「手動」、「外部」、「非整合」的選項）。

4. **重讀**：回到題目，再次閱讀，尋找「**關鍵字**」（例如：cost-effective (成本效益), easiest (最簡單), real-time (即時), not (不)）。

5. **決戰**：在剩下的 2 個選項中，選擇最符合該「關鍵字」和「Databricks 優先原則」的那一個。

#### **Works cited**

1. 超白話- 什麼是大語言模型LLM - 方格子, accessed November 12, 2025, ++<https://vocus.cc/article/6707e5f0fd897800014fbe74>++

2. Deploy models using Mosaic AI Model Serving | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/machine-learning/model-serving/>++

3. RAG vs Memory for AI Agents: Whats the Difference - GibsonAI, accessed November 12, 2025, ++<https://gibsonai.com/blog/rag-vs-memory-for-ai-agents>++

4. RAG 是什麼？白話文理解「檢索增強生成」對SEO 與AI 影響, accessed November 12, 2025, ++<https://frankchiu.io/ai-rag-intro/>++

5. RAG (Retrieval Augmented Generation) on Azure Databricks - Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/generative-ai/retrieval-augmented-generation>++

6. RAG (Retrieval Augmented Generation) on Databricks, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/generative-ai/retrieval-augmented-generation>++

7. Retrieval - Docs by LangChain, accessed November 12, 2025, ++<https://docs.langchain.com/oss/python/langchain/retrieval>++

8. Vector Search - Databricks, accessed November 12, 2025, ++<https://www.databricks.com/product/machine-learning/vector-search>++

9. Databricks RAG Architecture vs Traditional RAG Setups - Credencys, accessed November 12, 2025, ++<https://www.credencys.com/blog/databricks-rag-architecture-vs-traditional-rag/>++

10. 什麼是AI 代理？定義、範例和類型 - Google Cloud, accessed November 12, 2025, ++<https://cloud.google.com/discover/what-are-ai-agents?hl=zh-TW>++

11. LLM vs AI Agent vs RAG vs Agentic AI | by Rahul Sounder - Medium, accessed November 12, 2025, ++<https://medium.com/@sounder.rahul/llm-vs-ai-agent-vs-rag-vs-agentic-ai-b1175941ddbc>++

12. Traditional RAG vs. Agentic RAG: The Evolution of Intelligent Systems | by Shantanu Sharma | Medium, accessed November 12, 2025, ++<https://medium.com/@shantanu_sharma/traditional-rag-vs-agentic-rag-the-evolution-of-intelligent-systems-20c6331e9cc7>++

13. Agentic AI vs RAG: Choosing the Right Approach for Enterprise AI Strategy - Sprinklr, accessed November 12, 2025, ++<https://www.sprinklr.com/blog/agentic-ai-vs-rag/>++

14. 大白话讲清楚GPT嵌入（Embedding）的基本原理 - 53AI, accessed November 12, 2025, ++<https://www.53ai.com/news/LargeLanguageModel/2024071576193.html>++

15. 【AI知识点】微调（fine-tuning）\_微调ai有什么用 - CSDN博客, accessed November 12, 2025, ++<https://blog.csdn.net/weixin_43221845/article/details/142691393>++

16. 微調（Fine-tune）是什麼？成本更低，企業打造「專屬AI」的必備技術 - 數位時代, accessed November 12, 2025, ++<https://www.bnext.com.tw/article/82431/what-is-fine-tune>++

17. AI 提示工程指南 - Google Cloud, accessed November 12, 2025, ++<https://cloud.google.com/discover/what-is-prompt-engineering?hl=zh-TW>++

18. 一文读懂「Prompt Engineering」提示词工程进阶版原创 - CSDN博客, accessed November 12, 2025, ++<https://blog.csdn.net/Julialove102123/article/details/141336646>++

19. A Beginner's Guide to Few-Shot Prompting in LangChain - DEV Community, accessed November 12, 2025, ++<https://dev.to/aiengineering/a-beginners-guide-to-few-shot-prompting-in-langchain-2ilm>++

20. What is Unity Catalog? | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/data-governance/unity-catalog/>++

21. What is Unity Catalog? - Azure Databricks - Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/>++

22. MLflow for ML model lifecycle | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/mlflow/>++

23. Introducing Databricks Vector Search Public Preview, accessed November 12, 2025, ++<https://www.databricks.com/blog/introducing-databricks-vector-search-public-preview>++

24. Unity Catalog best practices | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices>++

25. How to create and query a vector search index - Azure Databricks - Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/generative-ai/create-query-vector-search>++

26. How to create and query a vector search index | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/generative-ai/create-query-vector-search>++

27. Indexes API | REST API reference | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/api/workspace/vectorsearchindexes>++

28. w.vector_search_indexes: Indexes — Databricks SDK for Python beta documentation, accessed November 12, 2025, ++<https://databricks-sdk-py.readthedocs.io/en/latest/workspace/vectorsearch/vector_search_indexes.html>++

29. accessed November 12, 2025, ++<https://kanerika.com/blogs/databricks-mlflow-implementation/#:~:text=MLflow%20in%20Databricks%20is%20an,a%20central%20registry%20for%20collaboration>[.](https://kanerika.com/blogs/databricks-mlflow-implementation/#:\~:text=MLflow%20in%20Databricks%20is%20an,a%20central%20registry%20for%20collaboration.)++

30. What is Databricks MLflow? - Quora, accessed November 12, 2025, ++<https://www.quora.com/What-is-Databricks-MLflow>++

31. MLflow for ML model lifecycle - Azure Databricks | Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/mlflow/>++

32. Get started with MLflow 3 for models | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/mlflow/mlflow-3-install>++

33. MLflow on Databricks: Benefits, Capabilities & Quick Tutorial - lakeFS, accessed November 12, 2025, ++<https://lakefs.io/blog/databricks-mlflow/>++

34. Tutorial: Build, evaluate, and deploy a retrieval agent | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/generative-ai/tutorials/agent-framework-notebook>++

35. Model Serving - Databricks, accessed November 12, 2025, ++<https://www.databricks.com/product/model-serving>++

36. Deploy models using Mosaic AI Model Serving - Azure Databricks | Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/>++

37. Inference tables for monitoring and debugging models - Azure Databricks | Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/inference-tables>++

38. Inference tables for monitoring and debugging models | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/machine-learning/model-serving/inference-tables>++

39. エンドポイントFeature Serving | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/ja/machine-learning/feature-store/feature-function-serving>++

40. Databricks Feature Serving（特徴量サービング）の一般提供開始のお知らせ, accessed November 12, 2025, ++<https://www.databricks.com/jp/blog/announcing-general-availability-databricks-feature-serving>++

41. Databricks Feature Store, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/machine-learning/feature-store/>++

42. Feature Serving endpoints - Azure Databricks | Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/machine-learning/feature-store/feature-function-serving>++

43. Feature Serving endpoints | Databricks on AWS, accessed November 12, 2025, ++<https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving>++

44. Databricks Generative AI Engineer Associate Certification: Study Guide Part 1 - Medium, accessed November 12, 2025, ++<https://medium.com/@chandadipendu/databricks-generative-ai-engineer-associate-certification-study-guide-part-1-70cf3c483085>++

45. Databricks Generative AI Engineer Associate Practice Tests 2025 - SkillCertPro, accessed November 12, 2025, ++<https://skillcertpro.com/product/databricks-generative-ai-engineer-associate-practice-tests/>++

46. Agentic Systems: Deploy and Evaluate RAG Apps with Databricks AI, accessed November 12, 2025, ++<https://www.databricks.com/resources/demos/tutorials/data-science/ai-agent>++

47. Databricks Certified Generative AI Engineer Associate Study Guide - O'Reilly, accessed November 12, 2025, ++<https://www.oreilly.com/library/view/databricks-certified-generative/9798341623446/>++

48. Databricks Generative AI Associate Exam Study Notes - vladsiv, accessed November 12, 2025, ++<https://www.vladsiv.com/resources/notes/databricks-genai-prep-notes>++

49. How to use few shot examples | 🦜️ Langchain, accessed November 12, 2025, ++<https://js.langchain.com/docs/how_to/few_shot_examples/>++

50. Structured output - Docs by LangChain, accessed November 12, 2025, ++<https://docs.langchain.com/oss/python/langchain/structured-output>++

51. PydanticOutputParser — LangChain documentation, accessed November 12, 2025, ++<https://python.langchain.com/v0.2/api_reference/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html>++

52. A Comprehensive Guide to Output Parsers - Analytics Vidhya, accessed November 12, 2025, ++<https://www.analyticsvidhya.com/blog/2024/11/output-parsers/>++

53. Control LLM output with LangChain's structured and Pydantic output parsers - [Atamel.Dev](Atamel.Dev), accessed November 12, 2025, ++<https://atamel.dev/posts/2024/12-09_control_llm_output_langchain_structured_pydantic/>++

54. How to return structured data from a model - LangChain overview, accessed November 12, 2025, ++<https://js.langchain.com/v0.2/docs/how_to/structured_output/>++

55. LangChain: Structured Outputs from LLM - Kaggle, accessed November 12, 2025, ++<https://www.kaggle.com/code/ksmooi/langchain-structured-outputs-from-llm>++

56. MLflow Models, accessed November 12, 2025, ++<https://mlflow.org/docs/3.0.0rc2/model>++

57. Evaluating Large Language Models with Giskard in MLflow | Databricks Blog, accessed November 12, 2025, ++<https://www.databricks.com/blog/evaluating-large-language-models-giskard-mlflow>++

58. LLM Judges with custom prompts - Azure Databricks | Microsoft Learn, accessed November 12, 2025, ++<https://learn.microsoft.com/en-us/azure/databricks/mlflow3/genai/eval-monitor/custom-judge/create-prompt-judge>++

59. Databricks Certification, accessed November 12, 2025, ++<https://www.databricks.com/learn/training/certification>++

60. 6 free Databricks courses and badges - Reddit, accessed November 12, 2025, ++<https://www.reddit.com/r/databricks/comments/1odjoly/6_free_databricks_courses_and_badges/>++

61. Generative AI Fundamentals Accreditation - Databricks, accessed November 12, 2025, ++<https://www.databricks.com/training/catalog/generative-ai-fundamentals-accreditation-1811>++

62. Generative AI Fundamentals - Databricks, accessed November 12, 2025, ++<https://www.databricks.com/resources/learn/training/generative-ai-fundamentals>++

63. Comparing LangChain vs RAG for AI Knowledge Management - [Lamatic.ai](Lamatic.ai) Labs, accessed November 12, 2025, ++<https://blog.lamatic.ai/guides/langchain-vs-rag/>++

64. Build a custom RAG agent - Docs by LangChain, accessed November 12, 2025, ++<https://docs.langchain.com/oss/python/langgraph/agentic-rag>++

Databricks Certified Generative AI Engineer Associate, accessed November 12, 2025, ++<https://www.databricks.com/learn/certification/genai-engineer-associate>++