---
tags:
  - llm-application
---
# LLM Design Pattern - RAG

## \[ RAG as a Design Pattern \]

- From 安德魯的部落格

- 這一年來重點其實都是圍繞著 AI 打轉，都在拿捏怎樣在我的服務內善用 AI

- 搞懂 RAG 它後才體會到，RAG 不是個 "技術"，它更像是個 design pattern，一個讓 LLM 能根據事實回答問題的設計模式

- 重點1. 如何在你的應用程式中善用 prompt 來解決問題?

   - 既然都用 "軟體" 了，該下好 prompt 的應該是 developer, 而不是 user .. 我覺得這是 RAG 的基礎，因此我的場次會花一半的時間談這主題

- 重點2.資料的檢索跟應用

   - 這部分有很多固定的模式，包含文件的擷取、分段、向量化等，這些已經很固定的模式也成熟到有獨立的服務來負責，我只要呼叫 API 就好

   - kernel-memory, 來自 microsoft 的 open source project, 這是我第二個想談的主題

- 既然都在談設計模式了，搞懂 RAG 背後怎麼一回事，而也有 kernel-memory 這樣的服務幫你把煩人的事情都解決掉，那你還需要從頭開始寫 code 嗎? 其實這很多餘，如果你環境允許 (例如是內部用，可以接受 no code platform)，在這些平台上串接 API 來達成 RAG 的效果則是絕配。最後我會用 dify 這個平台，用一個完整的案例把整個過程串起來，當作這個 session 的總結

- <https://github.com/NirDiamant/RAG_Techniques?tab=readme-ov-file> 





- RAG Evaluation 最有名的就是這個 Rag Triad，但是發現要做這三個重要指標的分析之前，其實第一步應該先做端對端（End to End） 的回覆正確性（Answer Correctness）分析才對, 否則會失了方向呀, 從回覆正確性的平均看來，Multi Query 果然會增加 Answer Correctness

![Untitled 20240504 155620.jpeg](./LLM%20Design%20Pattern%20-%20RAG-assets/Untitled%2020240504%20155620.jpeg)



## \[ Databricks LLM Video \]  

- [2024 年必備 RAG 知識，Llamaindex 創辦人講解最前沿的 RAG 流程](https://www.databricks.com/dataaisummit/session/building-production-rag-over-complex-documents)

- Databricks 舉辦，其中一個 Session 邀請 Llamaindex 的創辦人 Jerry Liu 來分享：「Building Advanced RAG Over Complex Documents」

- Jerry Liu 這次分享其實一次性的講了小編認為過去一年 RAG 最重要的 4 個提升方向的其中 2 個：

   - Data Parsing（資料解析）

      - 大家都習慣直接用 pyPDF 直接把文字抽出，但這樣一來會丟掉幾乎所有文字以外的資訊

      - Llamaindex 過去就堆出了 LlamaParse，能夠抽取表格、圖表、圖片，同時能夠應付大量常見檔案格式（pdf, docx, pptx, …），同時還能輸入指令調整抽取的模式

      - 過去小編分享過的 MAP-Neo 也提出多個各領域最佳的方法，結合處理 pdf 文件，這也是小編比較推薦的方法（像是 PP-Structure V2 可以用來讀取文件排版、讀 Latex 公式，Marker 可以多語系的讀取與清理文字，…等

   - Query Planning（問題規劃）

      - 傳統的 RAG 流程大多只能應對「User 詢問DB中某一個段落的知識」，因為 Retriever 會基於 Query 去抓 Top k 個段落，並讓 LLM 閱讀 k 個段落後進行回復。但對於 user 而言，有很多問問題的場景傳統的流程無法應對

      - Jerry Liu 提倡套用更多 Agent 的概念進入 RAG 的流程，讓 Agent 先進行 Query planning，把一個複雜性的問題拆解成多個簡單性的問題，同時再賦予 Agent 不同功能的 tools，需要摘要時就給專門為摘要設計的工具，進而應付更為複雜的 Query

      - Summarization Question（摘要型任務）

      - Comparison Question（比較型任務）

      - 像是 Perplexity, [You.com](You.com), chatPDF 這種較為成熟的產品中看到這些方法的影子

   - Database information Organization：

      - 包含人為撰寫知識內容時的格式，像是你新撰寫的知識，能不能被 retriever 正常的抽取出來？很多 document 因為語意相近或是沒有明確的關鍵字，其實在對於 retriever 是不存在的。

   - Hybrid Search

      - 如何結合各種 Meta data（關鍵字, tag, user 的身分, 語系, … ）來提高搜尋的精準性？



## \[ Knowledge Graph as Input \]

- Requirement:

   - High-performance query

   - Causal Relationship, Enterprise Business Process Flow, Other Knowledge

- Knowledge Graphs (KG): These are particularly powerful because they:

   - Represent relationships between entities explicitly through edges

   - Support reasoning through graph traversal

   - Allow for hierarchical organization of concepts

   - Can incorporate uncertainty and confidence scores

- KG Storage Design 

   1. Graph Layer:

      - Use a property graph model

         - Neo4j ( Cypher is Neo4j's declarative graph query language )

         -  azure sql with graph extension: under million node

      - Add metadata to edges:

         - Causal effect size

         - Confidence intervals

         - Temporal validity windows

         - System conditions/constraints

   2. Vector Enhancement:

      - Create embeddings for each node/subgraph

      - Use techniques like GraphSAGE or Graph Neural Networks

      - Store in vector databases (like Pinecone or Milvus)

      - Enables similarity search for complex queries

   3. Temporal Indexing:

      - Add time-based indexing for dynamic system states

      - Store state transitions with timestamps

      - Enable time-window queries


