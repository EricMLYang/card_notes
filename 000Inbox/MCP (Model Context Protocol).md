---
tags:
  - llm-application
---
# MCP (Model Context Protocol)

from **++[ExplainThis.io](ExplainThis.io)++**



## \[Article\]

整天看 AI, Agent 好棒棒，不如持續的去理解實際運作方式，以 Agent 而言，Anthropic 出了滿多文章都很直得參考，其中 2024 年 11 月開源的 Model Context Protocol (MCP) 協定，在 AI 應用相關討論度頗高，就算 MCP 最後沒有變主流，其設計背後的思考方式也很值得去了解，而不要整天看 xx 被取代、xx 完蛋了這些沒營養的文章．



## \[MCP 是什麼\]

- MCP 的三個字分別拆開來看，分別代表：

   - Model 模型：大家熟知的 AI 模型，例如 GPT 模型

   - Context 脈絡：提供給模型的額外資料

   - Protocol 協定：也就是一個通用的標準

   (以上文字出自 from **++[ExplainThis.io](ExplainThis.io)  ++**我很喜歡的專頁)

- 最目的性的抽象解釋: 為了讓不同數據源可以用最方便無阻力的方式跟 AI 模型溝通，所定出來的一種標準化溝通方式

- **稍技術解釋：MCP 是一種標準化協議，讓 AI 模型能夠統一方式對接外部數據源與工具，實現動**態函式調用與上下文管理，避免各自開發不同的 API 介接方式

- 技術本質解釋： MCP 就是一種 Host、Client、Server 溝通架構設計，並利用 JSON-RPC 2.0 來當作溝通標準，讓 AI 模型服務可以用此標準協定來遠程呼叫伺服器相關函式，獲取所需的相關數據

   - Host:  LLM Desktop  or  集成 AI 的 IDE 等，負責協調整個交互流程，提供用戶介面

   - Client: 被 Host 管控的連線實例，具體來說是 AI 模型的運行環境或代理，發起具體的 MCP 請求

   - Server: 正確理解為提供數據和功能的服務端，可以是各種資源提供者：文件系統、GitHub、SQL 數據庫等，負責執行實際操作並返回結果

## \[ 類比 \]

可用其他技術來跟 MCP 比較，通常更能理解一個技術的本值，讓「MCP 作為標準化『協定 / 介面 / 中間件』」的定位更清楚．

### 1\. HTTP 協議

- **相似性**

   - **標準化與通用性**：HTTP 為不同的瀏覽器和伺服器之間提供了一個統一的通信協定；MCP 為不同的 AI 模型與外部工具 / 數據源之間提供了統一的交互方式

   - **關注傳輸協定**：HTTP 著重在「如何發送和接收資料」的規範，MCP 則著重在「如何對 AI 模型提供上下文與工具使用」的規範。

- **不同點**

   - **用途領域**：HTTP 的核心目標是解決「網路應用之間的傳輸」；MCP 的核心在於「AI 與外部資料 / 工具的整合與上下文管理」。雖然兩者都是協定層，但 MCP 還涉及 AI 模型對接時需要的**上下文格式**與**功能調用語意**，不只是一個純粹的請求 / 回應傳輸協定

   - **內部細節**：HTTP 使用方法（GET/POST/PUT/DELETE 等）和標頭（header）做封裝；MCP 可能需要更豐富的規範，例如「如何攜帶模型上下文」、「如何對接工具 API」、「如何表達函式參數」

### 2\. ODBC/JDBC

**相似性**

- **統一介面**：ODBC/JDBC 透過在應用程式層和資料庫之間抽象出一個「驅動介面」，讓同一段程式可以在不同資料庫上運行；MCP 為 AI 模型對不同外部工具和資料源提供統一協定，讓同一個 AI 應用可以對接各種工具或資料

- **屏蔽底層差異**：ODBC/JDBC 實現對多種資料庫（MySQL, PostgreSQL, SQL Server, Oracle 等）的抽象；MCP 則抽象出對多個外部 API 和工具的存取方式。

**不同點**

- **交互內容**：ODBC/JDBC 大多是「SQL 指令」的傳送與回應；MCP 除了「發送指令 / API 請求」，還需要**處理上下文**（例如對話歷史、模型推理狀態、函式描述等），以及**可能的 AI inference 流程**

- **生態系的複雜度**：資料庫協定（ODBC/JDBC）主要面對資料庫操作；MCP 面臨的是**千變萬化的各種 API 與工具**，因此其抽象層勢必更複雜



### 3\. Function Call + Proxy

- **相似性**

   - **讓 AI 能夠調用外部函式 / 服務**：這就像在程式中用一層 proxy 來攔截函式呼叫，然後將之轉給遠端 API；或是直接讓 AI 知道如何呼叫某個函式。MCP 與這個概念的本質確實相近：讓 AI 能夠「直接或間接地」呼叫外部服務。

   - **開發者/框架定義好函式的「簽名」**：在 Function Calling 的場景中，開發者通常需要預先告訴 AI「這個函式叫做 create_pull_request」，它需要哪些參數、什麼型別；MCP 也會有對應的標準化描述。

- **不同點**

   - **是否標準化**：Function Calling + Proxy 更著重於一個**概念或應用層設計**；然而 MCP 進一步試圖建立「**所有人都能用**」的**通用標準**。同樣都是「函式呼叫」，但 MCP 不是只有實作層，而是希望有一個「大家都能依循」的協定，避免各家都寫自己的一套。

   - **覆蓋範圍**：Function Calling + Proxy 通常在單一應用內部落地；MCP 則希望成為生態系層級的規範，從「AI 模型與外部工具接合」到「模型的上下文對接」都統一規範。



### 4\. 套件管理系統 (如 npm, pip)

- **相似性**：

   - 都有一種「對外依賴」的管理。套件管理系統提供標準化的方式去安裝、升級、卸載套件；MCP 提供標準化的方式去**宣告、呼叫**外部 API / 資料源。

- **不同點**：

   - MCP 面向的是「實時交互 / 工具使用」而非「程式組件安裝」。套件管理是一種事前「安裝」依賴；MCP 更像是**動態調用**依賴。



### 5\. 插件系統 (如瀏覽器擴充、VSCode extensions)

- **相似性**：

   - 插件系統提供一個標準化介面，讓各個插件可以在宿主應用裡「被調用 / 有效運行」。MCP 亦提供標準化介面，讓各種外部工具可以「被 AI 調用」。

- **不同點**：

   - 插件系統通常是「讓宿主應用延伸功能」；MCP 則是「讓 AI 模型能夠存取外部工具或資料源」。雖本質相似，但使用方式與場景有所差別。





## \[ Why Chose JSON-RPC 2.0 \] 

會選擇 JSON-RPC 2.0 應該是經過考量後的結果，可以從此協議的優點出發，大致上我認為最重要的就是成熟、簡單易懂、可包含各種狀況，以反應 AI 應用的複雜性：

- Simplicity and Lightweight Nature: JSON-RPC 2.0 is minimalist by design, with a very simple structure for requests and responses. This simplicity makes it:

   - Easy to implement across various programming languages

   - Lightweight with minimal overhead

   - Quick to parse and process

- JSON-Based Format

   - JSON is universally supported across virtually all programming languages

   - Human-readable, making debugging easier

   - Flexible enough to represent complex data structures

   - Native compatibility with web technologies

- Language and Platform Independence

   - Works seamlessly across different programming languages

   - Functions equally well on different operating systems

   - Enables interoperability between diverse systems

- Built-in Bidirectional Communication

   - Supports both request-response and notification patterns

   - Allows for asynchronous communication

   - Provides a standardized error handling mechanism

- Existing Widespread Adoption

   - JSON-RPC 2.0 is a mature, well-established protocol

   - Many developers are already familiar with it

   - Extensive libraries and implementations exist in most languages

   - Proven reliability in production systems

- Stateless Design

   - Each request-response pair is independent

   - Simplifies implementation and scaling

   - Reduces complexity in error handling and recovery

## JSON-RPC 2.0 的主要應用領域

JSON-RPC 2.0 作為一個輕量級的遠程過程調用協議，被廣泛應用於多種場景：

### 1\. Web 服務和 API

- **前後端通信**：Web 應用中的客戶端與服務器之間的通信

- **微服務架構**：不同微服務組件之間的輕量級通信

- **RESTful API 的替代方案**：當需要更結構化的方法調用時

### 2\. 區塊鏈和加密貨幣

- **以太坊節點通信**：以太坊的主要 RPC 接口使用 JSON-RPC 2.0

- **比特幣節點**：比特幣核心節點的 RPC 接口

### 3\. 開發工具和 IDE

- **語言服務器協議（LSP）**：VS Code 等編輯器與語言服務器之間的通信基礎

- **調試適配器協議（DAP）**：IDE 與調試器之間的通信

### 4\. IoT 和嵌入式系統

- **輕量級設備通信**：資源受限設備的輕量級通信方式

- **智能家居設備**：設備與控制中心之間的通信

### 5\. 桌面應用程序

- **進程間通信（IPC）**：電子應用中不同進程間的通信

- **插件系統**：主應用與插件之間的通信接口

### 6\. AI 和機器學習

- **模型服務接口**：ML 模型服務的簡單接口

- **MCP 協議**：連接 AI 模型與外部資源

### 7\. 遊戲開發

- **遊戲客戶端與服務器通信**：特別是對於非實時或回合制遊戲

- **遊戲開發工具**：編輯器與遊戲引擎之間的通信

### 8\. 遠程管理和監控系統

- **系統監控工具**：監控代理與中央服務器之間的通信

- **遠程配置管理**：遠程配置更新和管理





### \[ 純 OS 的 MCP 伺服器\] 

因為我個人是寫 Python 的，而 MCP 初期也是以本地機器為主，因此想用一個我自己最能直覺理解的例子，claude 提到，純地端  MCP Server 很類似寫一個 local 的 Python Socket 程式，此程式可以用 JSON-RPC 2.0 包裹 input, output, 你可以用 Python 撈取 SQL 結果、讀文件…等後，再把回覆透過 Socket 回傳給呼叫的 Client 端

## OS 層級的 MCP 伺服器與 Python Socket 的相似之處

1. **本地通信機制**：

   - 兩者都是在本地機器上提供通信服務

   - 都建立了應用程式間的數據交換渠道

2. **請求-響應模式**：

   - 都遵循接收請求、處理請求、返回響應的模式

   - 都需要處理連接生命週期

3. **協議實現**：

   - 都需要實現特定的協議（MCP 實現 JSON-RPC，Socket 可以實現自定義協議或標準協議）

   - 都需要編碼/解碼消息


