---
tags:
  - vms
---
VMS 開發規劃

## 主架構：

- 與 AWS 顧問確認最後架構

- 考量點: 服務效能  ＆  服務成本的平衡

---

![image 143.png](./VMS%20開發規劃-assets/image%20143.png)

## 主要邊界確認

### 1\.  電車數據撈取

- T-Box 服務商   >   VMS 解譯模組

- API 規格:   與服務商確認



### 2\. 數據應用細節

- 汽車銷售商-PM    >.        VMS 分析模組

- 待釐清: 數據意義、應用價值 … 等



### 3\.  車子基本資訊匯入

- 汽車銷售商系統    >    VMS 分析模組

- API 規格:   與服務商確認

- 待釐清:  T-Box 與 車子 VIN (Vehicle Identification Number) 對照？



### 4\. 車子保修數據更新

- 汽車銷售商保修系統   >    VMS 分析模組

- API 規格:   與服務商確認



### 5\. 報表呈現

- VMS 數據治理    >.    Dashboard 服務

- Plotly Dash:  數據到 DB



### 6\. 數據服務

- 前端 Dashboard: 

   - **釐清:   應用系統  與 Databricks Dashboard 用權限管理工具串接，不需要重複登入** 

- 異常即時通知:  Databricks    >   直 call 後端 API

- 數據訂閱 API： Delta Table. >.  後端 DB 

---





## 重要分析模組領域

### Phase 1: 基本車輛管理與品情報表

- 車輛管理

- 故障碼相關

- 電池管理

- 馬達與能耗管理

- 碳排計算

![CleanShot 2025-05-04 at 00.43.22@2x.png](./VMS%20開發規劃-assets/CleanShot%202025-05-04%20at%2000.43.22@2x.png)



### Phase 2: 進階分析

- 各種進階數據探勘結果

- 診斷模組

![CleanShot 2025-05-04 at 00.45.10@2x.png](./VMS%20開發規劃-assets/CleanShot%202025-05-04%20at%2000.45.10@2x.png)



---





## Databricks 架構規劃

- Delta Table Schema

- 分析計算資源規劃

- 數據保存 與 存封

---







## \[ 給客戶的提問清單 \]

### 🧾 To 客戶  IT:

- AWS Infra 窗口

- 客戶目前服務現況

   - Have APIM (API Management)

   - Have App GW (Application Gateway)

   - AWS Env. have Domain

   - 目前現有服務是在新加坡?

- 車子基本資訊匯入

   - 是否先提供數據欄位，讓我們確認需要數據，以便開出 API 規格

   - 情境次 DMS(車籍資料系統)發現有新數據主動呼叫 VMS API，還是 VMS 主動呼叫 DMS

   - 區分 Data update, 單純 append  狀況

   - 討論: Vin Code 當作 T-Box 與 車子的 key 

- 

---

### 🔧 To T-Box 服務商

- API 的傳輸頻率（每幾秒 or 定時？）

- 提供的數據格式與欄位（JSON、CSV？）

- 是否會推送資料還是我們主動拉？

- 安全傳輸協議（HTTPS、Token、IP 白名單？）

- 請提供 T-Box 的 API 文件與測試帳號

---

### 🔔To 銷售主管

- 年底售車期望呈現形式? 系統靜態圖? 操作影片?

- 購車客戶視角的系統內容



---

### 📈To EV PM

- 數據解譯規則

- 初步部數據範疇: 需要通知、報表呈現、數據傳輸服務









- Frequency:  1-10s, ( take Median 7s)

   - T-Box SIM Card is upper limit 

- 420 variables

- Add 300-400 Cars / Each Year ( Cumulative )

- Near Real Time Requirement:

   - 50 data less than 10 seconds

      - **Client  >  ( Backend API? ) > Kansis streaming  >  Lambda  >  Fargate**

   - 370 data: day, week, month

      - ( SDK or API ?)  >  (S3?) > Databricks Pipeline 

- Data Retention:

   - S3: 

      - **Different Tier** Design

   - Delta table

      - Retain full history for 30-90 days using Delta Lake time travel

      - Keep monthly snapshots for 6-12 months

      - Archive older data to S3 with lower-cost storage classes

      - Use VACUUM operations carefully to manage storage costs while preserving needed history

- Data Acquisition Layer  ( From Client IT, Not From Vehicle  )

   - The Best Way To Get Data

- **AWS Service in Application:**

   - **AWS Fargate  VS  AWS EB**

   - Best Code Hub and CI/CD Management:  GitHub?

   - Databricks Dashboard  to  Web:  Authorization Management

   - API Management:

      - Backend  to FMS

- [x] **應用系統 ( Portal ):**

   - DB 密碼加密實作

   - 即時通知機制實作

   - 對外 API  規劃 ( 我們系統要給下游車隊數據的數據服務 API )

   - Note: 展開需求討論時，要確認權限夠不夠

   - Dashboard iframe to Web without input user info. 

   - The backend system requires a division between external API suppliers and web usage.

- [x] **Analysis in Databricks**

   - Build Example Data Simulation

   - Analysis Function Repo. ( pySpark )

   - Delta Table Schema

- [x] **CI/CD Flow**

   - **Application System Deploy Flow**

- [x] **VMS 文件規劃**

   - SA: UI, System Atchitechture 

   - Development:

      - Data Model

      - 系統參數對照表

      - API 文件

      - Coding Style


