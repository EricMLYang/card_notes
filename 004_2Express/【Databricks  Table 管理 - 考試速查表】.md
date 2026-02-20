---
tags:
  - my-article
Checkbox 1: true
---
【Databricks  Table 管理 - 考試速查表】

跟同事輪流在 Daily 時解題，

我下一輪的幾題都在考表的管理，

因此彙整了 Databricks Table 的相關資訊，

以下是簡單描述版，

方便快速複習。



▋ 資料有沒有真的存下來

Databricks 的表分兩大類，

第一類會真正把資料存起來，第二類只存查詢的定義。

會存資料的包括 Delta Table、Streaming Table，

和 Materialized View。

 這三種表都會佔用實際的儲存空間。

不存資料的是 View 和 Temp View。 

它們像是一層介面，只記錄「怎麼查」而不是「查出什麼」。

記住一個口訣：View 是介面，Table 是實體。

---



▋ 表的資料放在哪裡

表的儲存位置分成 Managed 和 External 兩種。

Managed Table 的資料由 Metastore 統一管理。 

你執行 DROP TABLE 的時候，資料會跟著一起刪除。 

這種表適合用在 PoC 階段或短期專案。

External Table 的資料位置由你自己指定 `LOCATION`。 

DROP TABLE 之後，資料檔案會保留在原地。

 正式環境或需要跨環境共用資料時，

都該用 External Table。

想確保建出來的是 External Table，

就在建表語法裡加上 `LOCATION` 參數。

---





▋ 資料分層的邏輯

Databricks 常用 Medallion Architecture 來組織資料。 

資料從原始到服務，會經過三個層級。

Bronze 層存放原始資料。 

允許雜訊存在，通常是 append-only 模式。

 常見操作包括 Auto Loader 和 Schema Evolution。

Silver 層負責清理和標準化。

 去重、品質檢查、MERGE 操作都在這裡發生。

Gold 層是最終的服務層。

 資料已經聚合完成，可以直接給 BI 或 ML 使用。 

會用到 Partition 和 Z-ORDER 來優化查詢效能。

這三層的分工很清楚：

Bronze 收、Silver 洗、Gold 用。

---





▋ 資料怎麼更新

不同的業務場景需要不同的更新模式。

Append-only 是最簡單的模式，

只追加新資料。 

適合 Event log 或點擊流這類永遠往後長的資料。

MERGE 或 Upsert 模式可以更新和去重。 

訂單狀態更新、用戶主檔維護都適用這種模式。

CDC-applied 模式會套用變更流，

產生最終狀態。

 當你從 Debezium 或 DMS 接資料進來時會用到。

Streaming 模式持續更新，

會記錄 checkpoint。 

即時事件處理就是這樣運作的。

Backfill 模式用來重跑歷史資料。

 透過 replaceWhere 或 overwrite partition 來實現。

---





▋ View 的幾種形式

View 也分成好幾種，生命週期和用途都不一樣。

Persistent View 永久存在 Metastore 裡。 

常用來做 Schema 相容層，或是簡化複雜查詢。

Temporary View 只存活在 Session 期間。

Notebook 裡做臨時拆解很方便。

Global Temp View 是 Cluster 層級的，

但已經是 legacy 功能。 現在不太建議使用。

Materialized View 會預先計算結果，

可以定期 Refresh。 

適合用來加速 BI 查詢，或是固定的彙總需求。

Schema 變更要減少中斷，

就用 Persistent View 來做欄位 alias。

---



▋ 資料模型的用途

不同的資料模型有不同的設計重點。

Fact Table 或 Event Table 通常量很大，可分割。

 適合大量追加的交易資料。

Dimension Table 比較小，會用到 SCD Type 1 或 Type 2。 

維度資料的變更需要特別處理。

Snapshot Table 會定期存一份狀態。

每日或每週快照都屬於這類。

Wide Serving Table 是寬表，把常用欄位 join 好。 

減少查詢時的 join 次數。

Aggregate Table 或 KPI Table 給 BI Dashboard 用。

已經算好的指標可以直接呈現。

Feature Table 專門給 ML 用，

有 entity 和 time 兩個維度。

---



▋ 效能優化的策略

表的效能布局有幾個關鍵技巧。

Partition 能做到 Partition Pruning，減少掃描範圍。

查詢時只讀取需要的 partition。

Z-ORDER 用在非 partition 欄位，做 Data Skipping。 

可以大幅提升過濾效率。

Liquid Clustering 是 Z-ORDER 的進化版。 

會自動維護，不需要手動執行。

OPTIMIZE 用來解決 Small Files 問題。 

把小檔案合併成大檔案。

VACUUM 清理過期的檔案版本。 

釋放儲存空間。

這幾個操作要定期執行，才能保持表的效能。

---





▋ 治理與進階功能

Databricks 提供了很多治理工具。

Unity Catalog 管理權限、審計和 Lineage。 

是整個資料治理的核心。

Constraints 可以設定 NOT NULL 或 CHECK。 

在寫入時強制檢查資料品質。

Change Data Feed（CDF）提供增量變更給下游。

下游系統只需要處理變動的部分。

Time Travel 讓你回溯到過去的版本。

稽核或復原資料都很方便。

Clone 分成 Shallow 和 Deep 兩種。

Shallow Clone 快速且共享儲存。

Deep Clone 是完整拷貝。

Delta Sharing 可以跨組織分享資料。 

不需要實際複製資料就能共用。

---



▋ DLT 是什麼角色

DLT（Delta Live Tables）不是表的種類。 它是建立和維護表的管線框架。

用 `@table` decorator 會產出 Streaming Table。

用 `@materialized_view` 會產出 Materialized View。

用 `@temporary_view` 會產出 Temporary View。

DLT 產出的結果是 Delta Table、Streaming Table 或 MV。 DLT 本身是「方式」，不是「種類」。

---





▋ 考試常見的決策情境

考試會考你在特定情境下該怎麼做。

確保表是 External 的，建表時要指定 `LOCATION`。

Schema 變更要最小中斷，就建新表加上 Persistent View 來 alias 舊欄位。

解決 Small Files 問題，執行 `OPTIMIZE`。

非 partition 欄位要加速，用 Z-ORDER 或 Liquid Clustering。

清理舊版本檔案，執行 `VACUUM`。

下游需要增量變更，就啟用 CDF。

快速複製表到 Dev 環境，用 Shallow Clone。

---



▋ 整體邏輯的核心

理解 Databricks 的表，要先分清楚有沒有存資料。

再看是 Managed 還是 External。

然後是分層架構，Bronze、Silver、Gold。

搭配更新模式、效能布局、治理功能。

DLT 是產生這些表的方式，不是表本身的種類。

把這條線理清楚，其他細節就能串起來。


