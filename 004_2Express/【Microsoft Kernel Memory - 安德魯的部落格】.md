---
tags:
  - my-article
  - llm-application
Checkbox 1: true
---
【Microsoft Kernel Memory - 安德魯的部落格】

——  91APP  首席架構師 安德魯 近期在準備 AI Agent 相關工具

\-FB Link: [安德魯的部落格](https://www.facebook.com/andrew.blog.0928?\__cft_\_\[0\]=AZWcV0x_weq3h3HskWuBXiYmguwrD91uUweNeYcxKUofAaUK5LpA4Yv4AR5VsSK5oHfzC8mSAjoDsTQV4bjKbP8IaC1iCNUesbQlveKwhnO0s48ZFyZuDxZFiDTDLxI_4JHmhth4ebpbzI4o50jxQXC6h33Vlb0NpLEnvkbh7KD8-104EJvrBEPM7xtQIqfigeM&\__tn_\_=-UC%2CP-R)

\-簡介 .NET RAG 神器 : Microsoft Kernel Memory 與 Semantic Kernel 的整合應用

\-**<https://www.facebook.com/share/155gnXYSWo/>**



作者：

91APP 首席架構師

2016 \~ 2025 Microsoft MVP 微軟最有價值專家

Azure Cafe、TechDays、TechEd、DevOpsDays、 .NET Conf 等研討會講者

Azure PaaS 雲端系列課程與企業內訓講師



▋起源

作者於 2024 年底 .NET Conf，講過這主題，目前預計2025-03-25 開一場直播說明更詳細一點，彌補無法講太多 Code 的遺憾。



主題應該就是以 Kernel Memory（KM) 為主軸，整體會以 AI 應用情境來做示範。



Kernel Memory、 Semantic Kernel 是微軟同一個團隊的作品，兩個 Repo. Owner 都是這團隊架構師。



我個人稍微查了一下，將這兩個工具做以下解釋 (我個人比較好理解）。



▋什麼是 Semantic Kernel？

官方說明：

『 Semantic Kernel is a lightweight, open-source development kit that lets you easily build AI agents and integrate the latest AI models into your C#, Python, or Java codebase. It serves as an efficient middleware that enables rapid delivery of enterprise-grade solutions. 』



而我直接將 Semantic Kernel 類比成 LangChain，就是讓你的程式更容易跟 LLM 整合互動。

但 Semantic Kernel 設計理念與 LangChain 有幾個主要不同:

．More enterprise-focused with stronger formal versioning commitments

．Microsoft-backed with deeper integration into Microsoft ecosystems

．More emphasis on connecting existing code as plugins

．More structured approach to function calling





▋什麼是 Kernel Memory？

官方說明：

『 Kernel Memory (KM) is a multi-modal AI Service specialized in the efficient indexing of datasets through custom continuous data hybrid pipelines, with support for Retrieval Augmented Generation ( RAG), synthetic memory, prompt engineering, and custom semantic memory processing. 』



我是把 Kernel Memory 想成是一個專注於文檔處理和知識管理的微服務。



核心功能就是將各種格式的文檔和資料高效地處理、索引，然後以最優化的方式提供給 LLM API 使用。



**Kernel Memory 就像是 AI 系統的「企業級數據庫」或「智能記憶庫」**。如果把 Semantic Kernel 比作是 AI 與您代碼之間的通用翻譯器，那麼 Kernel Memory 則是為 AI 提供「記憶」和「知識」的專業倉庫。



具體來說，Kernel Memory：

**1\.接收和處理文檔**：接收各種格式的文件（PDF、Word、Excel、網頁等），將其轉換為可被 AI 理解的格式

**2\.建立智能索引**：為文檔內容創建向量嵌入，支持高效的語義搜索

**3\.提供 RAG 功能**：在需要時檢索相關知識片段，並將其作為上下文提供給 LLM API

**4\.維護引用關係**：追踪信息來源，確保 AI 能引用原始資料

**5\.管理知識庫**：按用途或用戶組織不同的知識集合，支持權限控制





安德魯提到 KM 定位:

．能靈活運用調配的服務

．能獨立運作 (只靠 API)

．可大可小 (單機 + 橫向擴充)

．甚至能小到像 SQLite 那樣 serverless mode ...

即使使用 API, 他也緊密地跟 Semantic Kernel 整合，內建 SK plugins, 整套設計其實就是為了跟 SK 一起使用的服務





▋ 安德魯預計說明？

會從 LLM 基本動作組合，挖掘一些 AI 操作的基本動作



基本動作的組合元素：

chat completion, structured output, function calling, agen



幾種不同的實作方式 ：

openai api, openai .net sdk, semantic kernel



搞懂以上，作者最後會再 demo KM plugins 的整合應用，示範一下 LLM + KM plugins 來做 RAG 的威力。



要使用的更靈活，甚至還可直接把 KM 封裝成 MCP server，可以直接在 claude desktop, cursor .... 等支援 MCP 的 Host 上面使用



以下是 安德魯 在直播前逐步貼出的前情提要，到 3/23 為止貼文如下：

．LLM - Structured Output

．Function Calling

．Function Calling (Case Study) 

．RAG with Function Calling

．RAG as a Service, Microsoft Kernel Memory

．進階 RAG 應用, 生成檢索專用的資訊

．我猜 3/24 還會有一篇





▋JSON Schema：結構化輸出的基礎

![CleanShot 2025-03-22 at 21.06.33@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.06.33@2x.png)



現代 LLM (GPT4o-mini 及更新版本) 支援 JSON Schema，這為開發者提供了強大的結構化數據處理能力。

### 開發者最佳實踐

**1\.結構化輸出設計**

．使用 JSON Schema 定義明確的輸出格式

．直接將 AI 回應反序列化為程式物件，無需中間解析步驟

**2\.明確的狀態標記**

．實作類似 HTTP 狀態碼的成功/失敗指示器

．避免模糊判斷，減少 try-catch 的依賴

**3\.職責分離**

．LLM 專注於需要 AI 能力的任務

．程式碼處理常規操作：搜尋、格式轉換、數值計算等

．成本考量：Azure Function Call 與 ChatCompletion API Call 費用差距顯著



實作考量要點

開發 AI 應用時需思考：

．輸出格式與錯誤處理機制

．失敗率與程式容錯設計

．任務分配：AI vs. 傳統 API

．規模化後的效能與成本優化





技術實現路徑

不同實現方式各有優勢：

．HTTP Client 直接調用

．OpenAI .NET SDK

．Microsoft Semantic Kernel

選擇適當的實現方式可顯著簡化開發流程，如用 Semantic Kernel 可直接映射 C# 類型，無需手動定義 JSON Schema。

適當的開發決策在大規模部署時能帶來顯著的效率與成本優勢。





▋Function Calling

![CleanShot 2025-03-22 at 21.08.00@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.08.00@2x.png)



Function Calling (工具使用)是LLM技術中最具革命性的突破，成為AI主動操控外部系統的關鍵能力。它建立了自然語言與程式碼之間的雙向溝通管道，是未來AI應用開發的基石技術。



運作機制:

**\-預先定義功能集**：在對話開始前向LLM聲明可用函數及其參數結構

**\-意圖識別與轉換**：LLM分析用戶自然語言，判斷何時需調用函數

**\-結構化輸出**：將語言指令轉換為符合預定義結構的JSON指令序列



技術實現示例

當用戶說「記得買些奶油和兩個櫛瓜，麵包已經買了」，具備Function Calling能力的LLM可自動解析為：

```
[
  { "action": "add", "item": "butter", "quantity": "1" },
  { "action": "add", "item": "zucchinis", "quantity": "2" },
  { "action": "delete", "item": "bread" }
]

```



開發價值與應用

**\-自動化指令轉換**：LLM充當自然語言到程式碼的智能編譯器

**\-系統整合能力**：啟用AI與各種外部系統和API的互操作

**\-Agent技術基礎**：為自主AI代理提供與環境交互的關鍵機制

Function Calling代表了從被動回應到主動執行的範式轉變，是理解與開發下一代AI應用的必備知識。





▋Function Calling (Case Study) 

![CleanShot 2025-03-22 at 21.09.17@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.09.17@2x.png)



系統架構揭秘

Function Calling真正的威力在於完整的調用-返回循環，實現了AI與程式的深度整合：

**1\.決策機制**：LLM不僅能發出指令，還能根據函數返回結果做出後續判斷

**2\.工作流管理**：支持順序相依的函數調用，構建複雜業務邏輯





實例解析：智能行程安排

當用戶要求「幫我找明早30分鐘空檔去慢跑」時，整個交互過程如下：

```
系統定義可用工具：[check_schedules, add_event]

用戶：find a 30 min slot for a run tomorrow morning

AI內部決策：調用 check_schedule(03/21 06:00, 03/21 12:00)

工具返回：["07:00-08:00, 起床換裝", "08:00-09:00, 吃早餐", "10:00~12:00, 跟同事視訊會議"]

AI分析結果：9:00-9:30有空檔，調用 add_event(03/21 09:00-09:30)

工具返回：["success"]

AI最終回應：Morning run scheduled for tomorrow at 9am!

```





技術要點

**對話狀態管理**：每次AI調用都包含完整的聊天歷史



**角色類型區分**：

．system：系統指令（最高優先權）

．user：用戶輸入

．assistant：AI公開回覆

．tool：AI向應用程式發出的私有指令

．tool-result：程式執行結果返回給AI





開發建議

此類應用已有成熟框架支持，無需從零構建：

．框架選項：Semantic Kernel

．無代碼平台：n8n, dify

．集成客戶端：Claude Desktop, Cursor等



Function Calling構成了現代AI應用的基礎架構，掌握此概念對開發者而言如同掌握基本的程序控制結構（if, for loop等）一樣必不可少。





▋RAG with Function Calling

![CleanShot 2025-03-22 at 21.10.09@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.10.09@2x.png)



核心機制剖析

RAG (檢索增強生成) 技術為LLM提供了實時獲取外部知識的能力，有效解決了模型知識時效性與專業性的限制。



運作流程解構

**1\.查詢轉換**：將用戶問題精確轉換為檢索條件

**2\.知識檢索**：從向量資料庫或其他資訊源獲取相關資料

**3\.增強生成**：將檢索結果與原始問題整合到提示中，指導LLM生成答案



Function Calling與RAG的整合

RAG本質上是Function Calling的特定應用案例：

```
系統指令：
"你的任務是協助使用者，代替他到xxxx檢索資料，並依據檢索結果回答問題。
回答時請附上來源網址，勿回答檢索內容未提及的資訊。"

```

當LLM配備檢索工具定義時，它會：

1\.自動決定何時需要檢索外部知識

2\.生成最佳查詢條件和參數

3\.整合檢索結果與用戶問題

4\.合成最終答案



實際應用場景

此架構使LLM能夠：

．回答最新資訊問題

．檢索私有知識庫

．提供有出處的精確答案



例如，當用戶詢問「請問我現在這邊有哪些值得逛逛的景點？以及提醒我出門前應該準備哪些東西」時，配備多種工具的LLM會：

．檢索用戶所在位置

．查詢當地天氣狀況

．搜尋附近景點資訊

．綜合分析結果提供全面建議

RAG技術結合 Function Calling 框架，已成為構建知識型AI應用的基礎架構。







▋RAG as a Service, Microsoft Kernel Memory

![CleanShot 2025-03-22 at 21.11.18@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.11.18@2x.png)

![CleanShot 2025-03-22 at 21.11.34@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-22%20at%2021.11.34@2x.png)



核心價值定位

Microsoft Kernel Memory (MSKM) 作為開源項目，填補了AI應用中長期記憶管理的關鍵缺口，提供了完整的文檔處理、索引和檢索框架：

**1\.架構彈性**：從單機內嵌到大規模分布式部署

**2\.完整RAG流程**：覆蓋從文檔導入、分段、向量化到檢索的全流程

**3\.無縫整合**：提供RESTful API和SDK雙重訪問模式

## 服務模式創新

MSKM突破了傳統記憶管理的局限，提供兩種核心部署模式：

．**Web服務模式**：通過HTTP API進行分布式訪問

．**內嵌式模式**：類似SQLite的應用內集成方案，無需額外服務器





與Semantic Kernel的協同優勢

MSKM與SK形成完美互補關係：

**1\.原生插件支持**：MSKM內建SK記憶插件

．自動暴露為Function Calling可用工具

．智能判斷何時需要檢索外部知識

**2\.技術堆棧共享**：MSKM本身基於SK構建

．支持相同的AI服務連接器(OpenAI, Azure OpenAI, Ollama, Claude等)

．文檔處理流水線支持自定義擴展





開發價值

MSKM為開發者提供了長期記憶管理的完整解決方案，填補了SK在文檔處理流水線上的空白，特別適合需要以下專業開發團隊使用:

．大規模文檔處理

．分布式任務執行

．複雜記憶管理邏輯



[作為.NET](作為.NET)領域最成熟的AI基礎設施組合，掌握前面介紹的Function Calling和RAG基礎知識，將使開發者能充分發揮MSKM的潛力。





▋進階 RAG 應用, 生成檢索專用的資訊

![CleanShot 2025-03-23 at 19.41.58@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-23%20at%2019.41.58@2x.png)

![CleanShot 2025-03-23 at 19.42.22@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-23%20at%2019.42.22@2x.png)

![CleanShot 2025-03-23 at 19.42.56@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-23%20at%2019.42.56@2x.png)

![CleanShot 2025-03-23 at 19.43.20@2x.png](./【Microsoft%20Kernel%20Memory%20-%20安德魯的部落格】-assets/CleanShot%202025-03-23%20at%2019.43.20@2x.png)



傳統RAG的局限性

標準RAG流程（文字提取→分段→向量化→儲存）面臨關鍵挑戰：

．**視角不匹配**：用戶以問題視角查詢，內容以作者視角撰寫

．**資訊密度不均**：自動分段難以保留文章邏輯結構

．**語意差距**：純向量相似性無法捕捉深層語意關聯





優化RAG的前處理策略

通過LLM預處理生成多視角內容：

**1\.文章摘要生成**：為每篇文章創建濃縮版（1000字內）

**2\.段落級摘要**：保留原始文章結構的同時提供精簡視角

**3\.問答對轉換**：將敘述型內容轉換為FAQ格式

**4\.問題解決框架**：重構為「問題/根本原因/解決方案/示例」格式



實施方法

1\.使用高性能模型（如OpenAI o1）進行內容預處理

2\.為不同視角內容添加適當標籤

3\.分別向量化並存入MSKM

4\.查詢時混合多視角結果



核心見解

RAG不應被視為固定產品，而是需要定制的設計模式：

．理解目標內容特性（如技術博客vs.新聞文章）

．分析用戶查詢模式與視角

．設計合適的內容轉換策略

．利用工具組合（SK + MSKM）實現端到端流程

通過這種方法，即使面對像「WSL能幹嘛」這樣的概括性問題，RAG系統也能提供更相關、更全面的回應，而不是僅返回片段資訊。