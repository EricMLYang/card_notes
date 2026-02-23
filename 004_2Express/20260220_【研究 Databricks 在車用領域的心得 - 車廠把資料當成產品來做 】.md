---
tags:
  - my-article
Checkbox 1: false
---
【研究 Databricks 在車用領域的心得 - 車廠把資料當成產品來做 】



最近要準備給高層主管的專案報告，

內容是用 Databricks 來協助客戶管理車載數據，

在調查還有哪些車廠有在用 Databricks 之餘，

內心有個感想，

這些車廠他們都想把數據變成長期的持續業務，

本來分散的資料，

ECU 時序、車隊遙測、CRM、金融、物流，

變成一套可重用的能力底座，

讓後續的 AI、診斷、OTA、個人化、預測、合規，

都能像接電一樣接上去。

Databricks 在車廠的價值，

在於把車 + 客戶 + 營運變成一套可治理、可演進、可計費的資料產品基礎，

有了基礎，AI 才能從功能變成收入，

以下是查到的相關資訊：



▋車聯網數據分析

Mercedes-Benz（德國）

．應用：階層式語義資料模型分析 PB 級 ECU 時序資料，採用 Liquid Clustering 優化資料布局

．成果：平衡儲存需求與查詢速度，加速車輛開發與預測性維修



Toyota（日本）

．應用：統一數據與 AI 平台「Vista」，整合企業、車聯網與客戶數據，從 EMR 遷移至 Delta Lake

．成果：資料刪除成本削減 99%，確保隱私法規遵循



General Motors（美國）

．應用：「數據工廠」雲端平台，即時分析車隊遙測資料監測車輛健康

．成果：實現預防性維修，朝「零碰撞」目標邁進



Rivian（美國）

．應用：IoT 感測器產生 PB 級數據，分析 ADAS 動態數據（俯仰、側傾、懸吊等），Unity Catalog 統一治理

．成果：預測性維修、遠端診斷、OTA 升級，模型效能提升達 50%

---





▋客戶行為分析

Porsche Holding Salzburg（奧地利）

．應用：Lakeflow Connect 整合 Salesforce CRM 客戶資料，建立客戶 360 視圖

．成果：統一客戶旅程、個人化體驗、降低維護成本



GM Financial（美國）

．應用：與 Deloitte 合作建立雲端分析平台，整合 Customer 360 視圖與 AI 驅動分析

．成果：基礎架構成本節省、個人化體驗、強化資料治理

---





▋供應鏈與製造優化

Volvo Group（瑞典）

．應用：Databricks Workflows 與 Delta Live Tables 重塑供應鏈物流管道

．成果：即時庫存可視化，資料處理效率提升約 40%

---

資料來源：Databricks 官方客戶案例、部落格及 Data + AI Summit 會議內容


