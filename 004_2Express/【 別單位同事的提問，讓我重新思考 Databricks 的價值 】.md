---
tags:
  - my-article
Checkbox 1: true
---
【 別單位同事的提問，讓我重新思考 Databricks 的價值 】



別單位同事在試 Databricks Genie，

因為他們剛入門，覺得設定很麻煩，

他跑來問我一句：

「為什麼你們要用 Databricks？」

我換個方式回答他。

我讓他想像一下，如果沒有 Databricks，

我目前有個外部客戶的電車數據管理系統，

我的小組要自己扛哪些事？



情境是這樣的：

來源：車隊不斷上傳車輛數據。

量很大、可近即時，但不要求毫秒級。

需求：要跑完流程看日常報表，後續還要做進階分析與模型。

工具：分析多半還是用 Spark / PySpark。



我先講結論：

如果沒有 Databricks，

我無法用「數據分析師」跟「軟體工程師」組成的小 Team，

去同時應付多個外部分析案子。

因為我們光處理 infra 就會塞滿我們時間，

根本無法去思考要用什麼分析來產生好的數據價值。



---

▋ 自己搞定「儲存」與「格式」

首先，我們要自己管理「檔案系統/資料湖」。

Delta Lake 本身其實是一個「開源格式 + Spark 外掛」，

你可以想成是在 Parquet 檔上加一層交易紀錄。



所謂「自己架」，

意思是你只用到這個開源格式，

其他所有 Databricks 平台功能都要自己打造。

你要自己設定 S3、Azure Data Lake Storage，

你要管理 bucket / container 權限、存取金鑰、壓縮與存儲策略。

多用戶或版本控制，要設命名空間與路徑管理規範。



接著，「schema Evolution」會多做一些事。

當你持續修改 schema（多欄位、刪欄位、改型別），

Delta Lake 會幫你「演進」而不是「報錯」。

但是當寫入多次 schema，讓 \_delta_log 檔案越來越多，

一但遇到多 Job 有修改衝突，很可能要自己處理。



這時候要自己處理 rollback 或資料修復，

這是相當麻煩的一件事。

Databricks 上的 Unity Catalog + Delta + 內建驗證，

我們自己做，就要拆成 5\~7 個元件自己拼裝。

---



▋ 處理「運算」，等於養一個叢集工程與 SRE 團隊

Delta Lake 作為儲存層，需要搭配 Spark 等運算引擎。

數據的各種處理，也都需要計算資源。

Databricks 背後是 Spark cluster manager，

幫你排程與資源分配。



自己架，就要：

架 Spark cluster 叢集管理（YARN、K8s、EMR、Dataproc）。

管理 driver / executor 數量、記憶體大小、並行度。

自管 JDK、Python、Spark 版號與 ML/科學套件。

你還得寫 job 排程（Airflow、Oozie、Argo Workflow）。

監控也要自己來： Prometheus + Grafana或雲端原生監控。



另外當 Task 跑過久，

要自己翻 Spark UI、

自己調 partition 策略、

自己改寫 SQL。

Databricks 的 Adaptive Query Execution (AQE)，

與自動調優會幫你攔下多數問題。

原本按鈕選「叢集規格」就能跑的東西，

現在變成一整套叢集工程與 SRE 作業。



---

▋ 為了「協作」，得手動組裝不易維護的開發平台

你還得把 Databricks 常用服務「自己做出來」。

不使用 Databricks，你就必須

自己動手組裝一個功能對等的平台。



這意味著你必須手動整合：

．Airflow（排程）、

．Jupyter/VS Code + GitFlow（開發）、

．Lake Formation/Purview（治理）、

．Trino/Presto（查詢）、

．MLflow（實驗）、

．以及 Kafka/Flink（流式）。



而且就算建置成功，

開發體驗也會大幅下降。

因為 Notebook 協作困難、

CI/CD 流程繁瑣、

環境隔離要自己處理，

且維運成本劇增。

Debug 困難度提高，

所有零件的權限、連線、版本相容性都得自己維護。

原本「平台型」的便利，

全部變成零件型的組裝與長期維護成本。

---

▋ 結論：Databricks 讓我們專注於「價值」，而非「維運」

Databricks 讓我們可以把精力，

放在資料治理、模型與報表/應用。

沒有 Databricks，

我們就要先當一輪平台工程師 + SRE。

要把檔案系統、事務表格、叢集、排程、治理、監控、ML 工具鏈，

一件一件拼起來。

然後，才開始做商業價值。

如果目標是「更快產出穩定的數據產品」，

Databricks 可以讓我們省去大量非核心價值的事情。


