---
tags:
  - business-data-science
---
# **Survey - Palantir Foundry Ontology** 

- Reference:

   - **[Implementing an Operational Data Mesh with Palantir Foundry on AWS to Transform Your Organization](https://aws.amazon.com/blogs/apn/implementing-an-operational-data-mesh-with-palantir-foundry-on-aws-to-transform-your-organization/?utm_source=chatgpt.com)**

   - [Guidance for Industrial Data Fabric with Palantir Foundry on AWS](https://aws.amazon.com/solutions/guidance/industrial-data-fabric-with-palantir-foundry-technology-on-aws/?utm_source=chatgpt.com)

   - **[Technical Majesty of Palantir Foundry OS: A Deep-Dive into Enterprise Innovation](https://www.linkedin.com/pulse/technical-majesty-palantir-foundry-os-deep-dive-gal-levinshtein-a9bee?utm_source=chatgpt.com)**



## ▋研究目標 - 概念怎麼用在企業內部特定場景

### 研究目標:

- 不同性質、型態、來源的數據如何一起混合分析

- 分析如何直接產生業務行動

- 怎樣的架構才能支持以上功能

### 暫時不深入:

- 彈性的 No-Code UI

- 大規模使用的效能
   ...





## ▋Palantir Foundry 為什麼厲害

Palantir Foundry 是一個資料操作平台，讓企業能夠：

- 建立完整的 Web 應用程式，用於
   ▸ **即時監控與可視化**（real-time visibility）
   ▸ **決策支援工具**（decision-making tools）
   ▸ **快速處理業務情境下的決策**（operational decision resolution）

厲害之處在於：

- **打通數據與業務行動**，不只是分析，而是直接驅動行動

- **整合異質系統的資料**（ERP、CRM、IoT、第三方 API 等），形成語義統一的資料模型（Ontology）

- **支援多角色、多團隊的高度協作**，資料治理與權限設計嚴謹但靈活

- **具備規模化運作能力**，從部門 PoC 到全企業 rollout 都能支援

---







## ▋概念類比 - 以便快速理解

- Ontology = 企業知識圖譜 + 數據血緣 + 業務流程引擎 + 權限管理系統**。**

- **Ontology 把「語義 + 權限 + 事件 + 行動」黏合成一個統一平台，**




| **比喻類型** | **比較對象** | **傳統工具/概念** | **Foundry Ontology** | **核心差異** | 
|---|---|---|---|---|
| 整體 | Salesforce | Salesforce CRM | 企業級 Salesforce (全領域) | 從 CRM 擴展到整個企業生態系統 | 
| 源系統與分析 | 數據倉儲 | 源系統 → ETL → 數據倉儲 → 報表 | 源系統 → Ontology → 即時操作 | 從靜態分析轉為動態行動 | 
| 處理層與儲存 | Delta Table | S3 + Parquet + 運算層Schema | OSv2 作為底層儲存 → Ontology 語義層 → 應用層 | 加入語義關係和業務邏輯 | 
| 數據流 | Thinkboard | IoT 設備管理 | 企業級 Thinkboard (全業務實體) | 從設備管理擴展到全企業對象 | 
| 應用 | 圖數據庫 | Neo4j 圖數據庫 + 知識圖譜 | 可執行業務邏輯的知識圖譜 | 圖變化可觸發實際業務流程 | 
| 平台 | 平台 | PaaS (Platform as a Service) | 智能數據操作平台即服務 | 內建語義理解和業務行動能力 | 





## ▋語義核心概念 - 業務實體

以事件為源頭的真實實體定義

- **物件類型 (Object Type)：** 物件類型定義了組織中的一個實體或事件，例如「機場」、「航班」、「員工」或「公司」。

- **屬性 (Property)：** 定義了物件類型的特徵，為真實世界實體提供了詳細的屬性。

- **連結類型 (Link Type)：** 連結類兩個物件之間關係，例如「員工」與「公司」物件的「雇主」關係

```bash
Objects (實體) → Properties (屬性) → Links (關係)
     ↓              ↓              ↓
   Customer       CustomerID      Customer ←→ Order
   Product        ProductName     Order ←→ Product
   Order          OrderDate       Product ←→ Supplier
```

```yaml
# 從事件結果提取核心實體
核心實體清單:
  Customer:
    來源事件: ["客戶註冊完成", "客戶下單", "客戶付款"]
    業務價值: "營收來源"
    優先級: "高"
    
  Order:  
    來源事件: ["訂單建立", "訂單確認", "訂單出貨"]
    業務價值: "交易記錄"
    優先級: "高"
    
  Product:
    來源事件: ["產品上架", "庫存更新", "產品下架"]  
    業務價值: "銷售標的"
    優先級: "中"


# 上下文關係
上下文關係:
  銷售-財務:
    關係類型: "客戶-供應商" (Customer-Supplier)
    資料流向: 銷售 → 財務
    整合方式: "訂單成交時觸發財務建檔"
    防腐層: "統一客戶ID轉換服務"
    
  銷售-客服:
    關係類型: "共享核心" (Shared Kernel)  
    共享實體: [客戶基本資料, 產品資訊]
    整合方式: "共用客戶主檔資料庫"
    
  財務-客服:
    關係類型: "各自獨立" (Separate Ways)
    理由: "業務關聯度低，各自維護即可"
```

![image 160.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/image%20160.png)

### 語義層基本構建塊用途：

- 提供一種結構化且靈活的方式來對任何領域進行建模

- 無論其原始結構如何，不同來源的數據都可以映射到通用、明確定義的語義結構上。

- 以業務為中心的數據視圖，從而抽象出源系統的底層技術複雜性。

- 源系統針對特定功能進行優化的技術格式（資料表、檔案、API）儲存數據。業務使用者則從真實世界的概念（客戶、產品、訂單、事件）角度進行思考。



### 之前 MI 想做類似的事

- 非結構

![CleanShot 2025-05-25 at 10.14.37@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.14.37@2x.png)

![CleanShot 2025-05-25 at 10.11.57@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.11.57@2x.png)



- 結構: 統計、時間序列、機器學習...等手法找出關係

![CleanShot 2025-05-25 at 10.20.20@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.20.20@2x.png)









## ▋語義核心概念 - 行動

**動作（Action）與函數（Function）的動態行為建模：除了靜態的對象與關聯定義，Ontology 也負責刻劃企業業務的動態行為**，這透過設定**Action 類型**與**Function**來達成

- **Action** 是一種可執行的行為定義，為使用者提供了在 Ontology 上**修改資料或觸發流程**的結構化途徑，同時遵守預先設定的組織管控和權限規則 。

   - 例如，定義「調整庫存」或「下採購單」等 Action，

- **Function** 是一段可重複使用的商業邏輯程式碼，開發者能將複雜的業務規則或計算編寫為 Functions，部署到 Foundry 平台中供 Ontology 調用 。

   - 可被視為 Serverless Functions，可在操作情境中被快速執行，用於實現各種衍生計算或決策支援 。

   - **機器學習模型的融合：Palantir Foundry 提供完整的工具鏈將 AI/ML 模型融入 Ontology，以支撐自動化決策流程。** 

```python
# Foundry 風格的業務邏輯
@ontology_function
def calculate_customer_risk(customer: Customer) -> RiskScore:
    recent_orders = customer.orders.filter(date > last_30_days)
    payment_history = customer.payment_records
  
    return RiskModel.predict(recent_orders, payment_history)
```







##  ▋語義核心概念 - 即時決策

Ontology 結合 **Function、Action、AI 模型與事件流**，可以實現「即時決策支援系統」，讓系統不再只是被動提供數據，而是主動協助做出業務決策。

### 即時決策的基本條件：

- 可觸發的事件源（例如：新訂單、客訴、庫存異動）

- 可快速存取必要資料（透過語義層統整資料來源）

- 有預先定義的決策邏輯（Function / ML 模型）

- 能直接驅動後續行動（Action）

---

### 常見的即時決策實例：

| 決策場景 | 即時事件來源 | 調用邏輯 | 執行動作（Action） | 
|---|---|---|---|
| **電商客戶風險預測** | 客戶下單 | 根據歷史付款行為評分（Function: `calculate_customer_risk`） | 若風險高，自動啟用「延後出貨」策略 | 
| **供應鏈補貨** | 庫存量低於警戒值 | 檢查最近 30 天銷量趨勢（ML 模型預測） | 自動觸發「建立補貨單」 | 
| **客服異常警示** | 客戶多次聯繫未解決 | 依照過往解決率評估服務效能 | 自動升級為「客服主管介入」任務 | 
| **設備異常預警** | IoT 回傳異常訊號 | 檢查過去 7 天震動與溫度數據 | 自動安排「維修排程」或停機 | 
| **廣告精準投放** | 使用者靠近門市 Beacon | 匹配用戶歷史偏好（Function + 模型） | 即時推送個人化商品優惠通知 | 

---

### 技術組成（以 Foundry 為例）：

- `EventStream`：串接 Kafka / IoT / webhook 資料源

- `Ontology Function`：封裝評估邏輯（可為 Rule-based 或 ML 模型）

- `Action`：可寫入資料、觸發其他系統 API

- `Policy`：控管 Action 執行權限與輸入驗證

---

### 從「數據」到「即時行動」的路徑範例：

```text
[Event: 訂單建立] 
   ↓ 
[Ontology: Order 實體更新]
   ↓
[Function: 預測客戶風險]
   ↓
[條件符合 → Trigger Action]
   ↓
[Action: 調整出貨策略 / 通知物流]
```

---

### 模擬永遠是重要功能

![image 161.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/image%20161.png)



### MI 每個月的模型預測是想做到類似事情

![CleanShot 2025-05-25 at 10.17.53@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.17.53@2x.png)

![CleanShot 2025-05-25 at 10.20.42@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.20.42@2x.png)





## ▋結構與非結構結合

### 非結構資料 → 可語義化實體 → 整合進決策流程

```yaml
非結構資料（如影像、PDF、報表文字）
        ↓
AI / NLP / 影像辨識處理（抽取關鍵資訊）
        ↓
轉換為結構化欄位或 Ontology 中的「實體屬性」
        ↓
透過 Ontology 模型串接相關實體（Customer, Order, Asset...）
        ↓
納入業務流程、風險預測、行動觸發等分析決策流程中
```





### MI 新聞與研調數據結合 ( 但還沒整合在一起 )

![CleanShot 2025-05-25 at 10.14.57@2x.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/CleanShot%202025-05-25%20at%2010.14.57@2x.png)





## ▋系統架構

- Cloud Source + OSv2 是 Foundry Ontology 的核心組件

   - 本體論元數據服務 (Ontology Metadata Service, OMS)

   - 物件資料庫 (Object Databases)： 這些服務負責儲存本體論中已索引的物件數據，並設計用於為使用者應用程式提供快速的數據查詢和查詢計算。

   - 物件集服務 (Object Set Service, OSS)： OSS 負責處理來自本體論的讀取操作；OSS 允許其他 Foundry 服務和應用程式從本體論查詢物件數據，從而實現物件的搜尋、篩選、聚合和載入 。  

   - Object Databases：儲存已索引的對象資料，支援快速查詢和用戶編輯。

   - Object Data Funnel：協調資料寫入 Ontology，從資料來源和用戶編輯中索引資料。

   - Actions：允許用戶以結構化方式修改對象資料，並建立歷史記錄。

   - Functions on Objects：支援在對象上執行快速的業務邏輯。

![image 162.png](./Survey%20-%20Palantir%20Foundry%20Ontology%20-assets/image%20162.png)

### 各種數據源的連接器

### 寫入技術 Schema-on-Read vs. Schema-on-Write：

- 可同時支援 schema-on-write 與 schema-on-read 模式。

   - schema-on-write : 資料寫入時就定義和驗證結構

   - schema-on-read: 資料以原始格式儲存，讀取時才套用結構解釋

- Foundry Pipelines 容許使用者在資料匯入過程中定義結構（如對新上傳的 CSV/JSON 資料集套用欄位定義），將原始資料轉換為結構化資料集 ￼

- Foundry 的 Ontology 也支援將多種來源的已存在資料以「讀時映射」方式定義到統一的對象模式中。

- 這意味著使用者可以先將各來源資料接入平台，之後在 Ontology 層為其建立虛擬的整合 schema，而不必在匯入時強制轉換所有來源。

- 尤其在新版 Ontology 後端 (Object Storage V2) 中，一種對象類型可以有多個後端資料源支撐，例如將同一對象的不同屬性欄位分別由不同資料表提供 

- 這種**多資料源對象類型（MDO）**機制相當於在 Ontology 層進行類似 join 的整合：透過匹配主鍵，允許對象的部分屬性來自不同來源資料集

- 此能力讓 Ontology 成為企業資料語意融合的樞紐，以 schema-on-read 式的方法在不改變底層資料的情況下，建立起跨系統的單一語義模型。





















## High Level 論述

- **Palantir Foundry 的 Ontology 是企業的運營語意層**，它建立在已整合進 Foundry 的數位資產之上（各種資料集與模型），並將它們關聯到現實世界的對應對象（從工廠、設備、產品等實體，到客戶訂單、財務交易等概念

- 「將企業所有一切（數據、應用程式、硬體等）組織在一個地方的平台」

- Palantir Foundry 的本體論 (Ontology) 不僅僅是一個數據建模層，更是一種根本性改變數據整合分析的策略性能力。它透過提供一個動態、語義豐富且受治理的組織營運現實表徵來實現此目標

- Foundry 本體論被定義為「組織的數位分身 (digital twin)，一個位於整合到 Foundry 中的數位資產（數據集和模型）之上的豐富語義層」

- 核心特性——世界的關鍵語義（物件與關係）、世界的關鍵動態（功能與行動）、整合監控以及與外部系統的可擴展性——來支援數據整合分析

- 功能 (Functions) 與行動 (Actions) 使整合數據的操作化成為可能，允許在本體論框架內直接進行複雜的轉換和決策。整合的監控特性，包括資源狀態和數據健康檢查，確保了整合數據基礎的可靠性和可信度。

- **在 Ontology 中，每個業務實體被定義為一種對象類型**，具有一組屬性來描述其特徵；不同對象類型之間可透過**關聯（Link 類型）建立起連結關係，以反映現實世界的關聯性** 

## 可能架構（概念）

- 根據 Palantir 官方文件，OSv2 是 Foundry Ontology 的核心組件，支援大規模資料索引、查詢和操作。其架構圖展示了 OSv2 如何與其他服務協同運作，包括：

   - 本體論元數據服務 (Ontology Metadata Service, OMS)

   - **物件資料庫 (Object Databases)：** 這些服務負責儲存本體論中已索引的物件數據，並設計用於為使用者應用程式提供快速的數據查詢和查詢計算。

   - **物件集服務 (Object Set Service, OSS)：** OSS 負責處理來自本體論的讀取操作；OSS 允許其他 Foundry 服務和應用程式從本體論查詢物件數據，從而實現物件的搜尋、篩選、聚合和載入 。  

   - **Object Databases**：儲存已索引的對象資料，支援快速查詢和用戶編輯。

   - **Object Data Funnel**：協調資料寫入 Ontology，從資料來源和用戶編輯中索引資料。

   - **Actions**：允許用戶以結構化方式修改對象資料，並建立歷史記錄。

   - **Functions on Objects**：支援在對象上執行快速的業務邏輯。



**開放 API 與擴充介面：Palantir Foundry 提供完善的 API，支持開發者以程式方式與 Ontology 進行互動，從而將平台能力嵌入現有系統或自定應用中。在 Foundry 定義好 Ontology 模型後，系統能自動生成 API 端點**供外部調用，允許對 Ontology 資料進行讀取和寫入 。這意味著開發團隊可以輕鬆地構建自有的前端應用或微服務，透過 REST API 查詢 Foundry 中的對象資訊，或透過API將外部事件寫回到 Ontology 中



**事件匯流與串流整合：對於需要即時響應的情境，Foundry 提供事件機制與串流資料管道來整合 IoT 裝置及消息匯流平台。Foundry 的資料連接模組內建超過 200 種連接器**，可安全接入多種資料源並支持批次或流式的資料傳輸 。例如，在物聯網 (IoT) 領域，Foundry 能夠連接常見的雲端 IoT 平台（如 AWS IoT Core、Azure Event Hub、Google IoT Core），以及工業協議系統（如 OPC-UA、OSI PI 等），將裝置感測資料源源不斷地引入 Ontology



**Foundry Pipeline Builder**，使用者可以設定**串流管道**訂閱這些事件匯流（如訂閱 Kafka topic 或 Azure Event Hub 中的消息），實現裝置資料的即時入庫 。Ontology 則將這些 IoT 數據對映到對象的屬性上，從而做到例如：設備對象的狀態屬性隨感測器讀數自動更新，當溫度或庫存量超過閾值時馬上觸發預警。Foundry 的前端模組（如 **Workshop** 應用構建器）也支援**事件觸發**功能，開發人員可定義當使用者在應用中執行某動作或特定條件發生時，觸發 Ontology 的 Action 或外部請求 。這樣的事件驅動架構允許 Foundry 與企業的事件總線（Event Bus）深度整合：不論是從 IoT/MES 系統接收生產線事件，還是向外部系統發布消息通知（如庫存不足時向採購系統發送補貨請求），都可以透過 Foundry 的事件機制來實現



為了滿足現代企業在**規模、性能、實時性**上的更高要求，Palantir 在近年重新設計了 Ontology 後端，推出**Object Storage V2**作為新一代的核心資料存儲架構 。OSv2 從**架構上拆分**了原先糾結在一起的索引、查詢、編輯等模組，採用微服務方式將不同關注點分離（例如專門的索引服務 vs. 查詢服務），從而更易於水平擴展來迎接未來需求 。同時，OSv2 引入了 **Object Data Funnel** 等新組件來處理串流資料與 Actions，使系統對實時資料和使用者操作的支持更為流暢 。以下列出 Object Storage V2 帶來的一些主要新特性與改進：



- **效能與可擴展性：提供增量索引**機制顯著提升Ontology資料索引性能，可在資料更新時僅處理變動部分；整體索引吞吐大幅提高，單一對象類型可支撐**數百億**級別對象實例的索引規模 。查詢引擎方面，採用 Spark 爲基礎的分散式查詢層，使大範圍對象檢索和關聯分析更加高效，默認支持一次查詢 10 萬個以上對象（可按需擴大） 。

- **語意靈活性與安全：支援建立多資料源對象類型（MDO）**，允許一個對象由多個來源資料拼合而成，並實現更**細粒度的權限控制**（甚至可設定到對象的單個屬性欄位） 。這意味著在 OSv2 中，不僅能輕鬆將各系統資料整合入同一對象，還可基於用戶身份對對象的部分欄位隱藏或只讀，滿足複雜的安全合規需求。

- **高並發編輯與低延遲：大幅提升使用者編輯**的吞吐量與響應速度，一次 Action 最多可同時修改 **1萬個對象**而系統仍可流暢處理，比以往大幅提高 。同時針對使用者在前端的每次編輯操作，系統縮短了從提交到在 Ontology 中反映的延遲，實現接近即時的更新呈現。

- **即時資料管道：原生支援串流資料源**直接索引到 Ontology，Funnel 可持續消費資料流（如 IoT 裝置、消息隊列）並低延遲地更新對象 。這使得企業能更好地處理實時場景，如即時監控供應鏈物流狀態或門店即時銷售，Ontology 將隨著事件流不斷“水化”更新，確保決策所依據的是最新鮮的數據。

- **架構彈性與升級便利：OSv2 容許在對象結構發生重大變更**時，對已存在的使用者編輯記錄進行平滑遷移，不再像 OSv1 那樣因結構變更而遺失編輯歷史 。另外，OSv2 不再強制要求為支持編輯而建立實體化資料集，只有在特定下游需求時才需要創建物化視圖，降低了系統複雜度。Palantir 也提供了從 OSv1 遷移至 OSv2 的工具和嚴謹流程，確保企業客戶可以在不中斷業務的情況下逐步享受到新架構帶來的優勢 。

```python
class TimeSeriesEntity:
    sensor_metadata = {
        "object_type": "Sensor",
        "properties": {
            "sensor_id": "TEMP001",
            "data_source": "influxdb://sensors/temperature",
            "sampling_rate": "1s",
            "retention_policy": "30d",
            "normal_range": {"min": 20, "max": 25}
        }
    }
    
    # 定義如何查詢實際時序數據
    def get_recent_data(self, hours: int = 24):
        query = f"""
        SELECT * FROM {self.data_source} 
        WHERE sensor_id = '{self.sensor_id}' 
        AND timestamp > now() - {hours}h
        """
        return timeseries_engine.execute(query)

    def forecase(self):
        
        # run databricks code  
        return model.forecase
```