---
tags:
  - my-article
Checkbox 1: true
---
【Databricks Asset Bundle ：部署到客戶環境的最後一哩路】

沒想過會把 Databricks 當方案放到客戶環境，

正常經驗都是客戶使用我們的服務，

但近期我們團隊積極推廣Databricks 給客戶，

主因是合作的案子都要持續探索數據，

希望讓數據應用價值越來越高，

這樣會讓分析範疇無法確定，

因此我們團隊第一時間就跟客戶介紹 Databricks，

這樣我們 Team 才可以專注在數據的應用，

其中關鍵之一就是 Databricks Asset Bundle 的便利，

以下簡單紀錄我們的嘗試：

---

▋ 以 Databricks 為主軸的架構

我們幾個對外案子架構組成都類似，

分成數據截取、數據中心、應用層三層。

．數據擷取層

以 AWS 或 Azure 服務為主，

負責收 Edge 資料跟其他系統數據，

依照案子特性會有不同的處理，

少部分有串流服務。

．數據中心層

我個人比較喜歡稱「洞察中心」，

執行數據治理主流程，

我們還要負責探索數據，

會進行資料採礦和ML建模，

且有計畫加入 LLM 應用，

全部運行在 Databricks 上。

．應用層

把系統架在 Azure 或 AWS 的服務，

主要應用是報表、通知模組、數據傳輸，

權限模組…等一般系統需要的都有包含。

數據中心跟應用層的關係，

只有金質 Table 數據持續傳到應用層 DB，

以及部分案子會把 Databricks Dashboard 傳到應用端，

其他保持低耦合。

---

▋ 重要的一步 Databricks CICD 流程

好部署是產品方案不可缺的屬性，

我們對 Databricks 的 CICD 相對陌生許多，

前陣子我們終於跑通整個流程，

以下簡單分享

---

▋CICD 執行環境

在 Azure 用 Azure Repo + Azure DevOps，

可預期會因應 Azure 推廣 GitHub 而把 Azure Repo 換掉，

在 AWS 則採用 GitHub 企業版搭配 GitHub Action，

會在什麼雲服務是配合客戶，

我們需要兩套都可以順利運行。

---

▋Repo.內容

我們所有 Databricks 的程式 ( PySpark 為主），

都會放 GitHub 或 Azure Repo 託管，

以 \*py 檔為主，資料夾結構類似下面安排，

DataHub/

├── config/

├── docs/

├── jobs/

├── resources/

├── src/

├── setup/

├── tests/

└── dashboards/

資料夾 dashboards 就是放 Dashboard 的 Json 檔，

我們把 dashboard 當程式碼一樣託管，

其中比較重要的是 DataHub/databricks.yml 跟 resources，

我們所有的 Databricks 部署 yaml 檔都放在這裡。

備註：

Databricks Dashboard 在類 SaaS 架構下有些侷限，

我們仍開發前端報表模組，

為客戶的進階應用預做準備。

---

▋ 運用 Databricks Asset Bundle 實現更順暢的部署

這次的目標在於 Databricks Asset Bundle (DAB)，

實際動作就是透過 Databricks CLI 去把 yaml 檔上的內容，

逐一透過 Databricks API 去完成環境建設所有動作，

我們目前撰寫 DAB 的 .yaml 設定檔，

讓他可以

．設定預算資源

．排 Job Schedule

．設置 Dashboard

…等

例如以下是配置 Dashboard 的簡易範例：

---

resources:

  dashboards:

performance_analytics_v1:

display_name: "performance_analytics_v1"

warehouse_id: ${var.SQL_warehouse_id}

file_path: ../dashboards/performance_analytics_v1.lvdash.json

---

原則上 DBA 可以執行幾乎所有 Databricks 動作，

因此我們團隊會再持續去理解。

---

▋體驗- 非常順暢

目前我們只要 push 到對應分支，

CICD 流程就會啟動，

一直到部署最新內容到 Stage 環境，

持續補上更完整 CI 流程就大功告成，

惟處理 Table 結構修改 … 等重大改變，

現階段 Prod. 環境我們刻意不要太自動化，

因為擔心萬一出錯可能造成災難性後果。

---

▋ 邁向雲端市集的商業化願景

我們的方案將組件模組化抽離後，

計畫上架到 AWS 與 Azure 的 Marketplace，

Databricks 的部署便利性讓這個目標變得可行，

這是過去在內部使用時沒想過的事，

期待 Databricks 對於這樣產品化的推進可以更快速一點，

讓我們可以一個平台打天下。