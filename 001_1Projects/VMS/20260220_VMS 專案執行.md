---
tags:
  - vms
---
# VMS 專案執行

![image 144.png](./VMS%20專案執行-assets/image%20144.png)

## \[現況\]

T-Box:  我們跟架構師進階討論完，想跟 T-Box 再次確認一下:

1. T-Box 是否可以支援  MQTT 協議 ( 一般Edge 最常見的 )，這樣我們可以用 AWS IoT Core，整個架構會合理很多

2. T-Box 是否可以納入  AWS 相關服務的 SDK?

3. 數據頻率:    不急的數據可以 每 N 秒 ( ex: 20秒) 一起發一次嗎?  還是資訊會遺失

## 關於主要溝通窗口 說明如下:

	EV數據相關-

1\.台灣大昌已經跟智易討論完成需求數據的項目及頻率(請參閱附件，涵蓋VMS & VFMS) 

2\.窗口-暫請James與智易對應，建議與智易召開三方會議溝通

	使用者行為、系統設計-

1\.設計風格、色系要求等，請AUO協助提案

2\.窗口-台灣大昌售服高級主任張天佑(Max)與台北合眾保固專員陳威齊(Jim)

	系統開發(AWS 相關、DMS)-

窗口-台北合眾 IT James





- 2025/5/28:  客戶將方案提送總部

- 目前階段:  

   - 細部規畫階段 - 提問題清單給客戶(約會議)

   - AWS 環境測試: 可先開自己內部測試環境 ( 500 美優惠 )

## 重要測試一: 接收 T-Box 供應商數據並解議(雲端、預計量大)

- Aaron Note: 

   - <https://www.notion.so/T-Box-Meeting-Question-211086d31d4880c9be49ded3a0842121>

   - <https://boiling-literature-bf9.notion.site/VMS-Survey-210086d31d4880a3916ec71de314f117>

- AWS Lambda ( 類似 Azure Function )

- Amazon Kinesis ( 串流服務 )

- Databricks Auto Loader: 

## 重要測試二: 關係到是否需要評估報表服務

- AWS IAM (Identity and Access Management) 權限管理

- Databricks Dashboard  透過權限管理與前端串接，不用另外登入

## 其他需求:

- AWS Fargate x 2  ( 類 App Service)

- S3 Standard ( 類 Blob Storage)

- Amazon Aurora PostgreSQL-Compatible DB

- 可建 pipeline job 的 Databricks 

## 最後再說:

- API Gateway

- Application Load Balancer













## \[To Do\]

- 本周: 列問題清單給客戶 

- 架構測試重點:

   - 數據接收: AWS Lambda   >   Kinesis Data Streams   >   Databricks Auto Loader ( 一天 2B，3-8秒內處裡完數據 )

- AUO 自行測試環境建構

- 跟客戶訂出幾個測試階段

   - 初版系統流程: 範例數據 or 虛擬生成數據

   - 單車串接測試

   - 更接近實際狀況的最終測試

- UI 設計:  Daisy ?，追蹤人力狀況

   - 重要原因:  年底上市是看系統的殼，像樣的話今年就可過關



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

## \[新資訊\]

### 4月底客戶通知會議邀約

與香港 IT 主管完成方向性會議討論，以下結論，並同步啟動本案的內部作業流程：

- 友達團隊協助增加：

   - T-Box上傳CAN數據後的數據解譯（Decode）作業。

   - 將解譯後的物理值與訊息整合至VMS雲端平台分析模組及儀表板。

- 雲端後台建置地點規劃

   - 集團建議建置於AWS平台

   - 地區集團並無硬性規定，台灣大昌期望伺服器建置於台灣 ( 服務台灣車子 )

   - AWS 台灣區資料中心成熟前，可於新加坡建測試環境，待AWS於台灣啟用地區服務後，於上市前正式轉移至台灣區域。

- 專案架構變更及流程申請

   - 客戶重新提送DPM雲端系統開發需求申請簽核。

   - 同時針對變更內容同步向集團主管匯報並取得共識後正式啟動調整版專案。

---





會議時間：2025/4/30 地點：下午4:00 - 5:00 與會人員： AUO友達：Bonnie / Dylan wen / Backy / Eric 大禾合眾：Edward / Chirs / Jack / James 



1. 大禾合眾內部會成立 AWS雲端小組，後續會與AUO團隊一起討論雲端建置相關流程。

2. VMS的功能需求，增加 智易T-Box上傳CAN數據後的數據解譯（Decode）作業。

3. T-BOX ID與車體ID的對應方式， 由DMS(車籍資料系統)API 提供。

4. VMS預計於年底上線，開發時程及功能項目需要再重新調整確認，期望「M05 報告模組 (電池相關)」此功能能優先完成。

5. 今年年底新車上市: 期望有購車顧客可感受到的系統畫面 ( 可以是範例資料)

6. 交車時間(未定，可能是明年  Q2): 交車後才是數據服務啟用時間

---





也可以請加我的line ID: tiffany6599

- 
