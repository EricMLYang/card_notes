【Liquid Clustering 考前惡補筆記】

---

一句話講完它在幹嘛

Delta table 的資料組織方式，

讓檔案布局自動整理，查詢跑更快、維運更省事。

---

▋ 為什麼會有這東西

傳統做法的痛點：

Partition：要事先猜好怎麼切，

猜錯就是過度分割、小檔案、資料傾斜



Z-ORDER：

要定期手動跑 OPTIMIZE 維護



Liquid Clustering 的想法很單純：

用更彈性的 clustering keys + 增量重整，讓表布局能隨需求調整。

---

▋核心特性速記

1\.維運負擔低：不用一直煩惱 partition 策略、不用手動調 ZORDER

2\.keys 選擇彈性：高基數欄位也能用（以前這是 partition 的禁區）

3\.keys 可以改：用 ALTER TABLE 調整，既有資料靠後續 OPTIMIZE 逐步轉換

4\.互斥限制：Clustering 跟 partitioning 不能共用，也不能再做 ZORDER

---

▋怎麼啟用

建表時指定：

 CREATE TABLE my_table (...) USING DELTA CLUSTER BY (col0);

CTAS： CREATE TABLE my_table CLUSTER BY (col0) AS SELECT ...;



觸發整理：OPTIMIZE my_table;



關於「自動調整 keys」這件事要分清楚： 

手動指定 CLUSTER BY (cols...)：不會自己發現新 keys，



要你自己改 用 AUTO / Predictive Optimization：

才會根據 query history 自動選 key

---



▋運作原理（白話版）

Delta table 底下就是一堆 Parquet 檔。

查詢時引擎最怕「很多檔看起來都可能符合」，結果掃一堆。



Liquid Clustering 做兩件事：

第一層：多維資料壓成一個排序數字

用演算法（Hilbert curve）把多個 clustering keys 的值，

壓成「一個排序用的數字」。

數字越接近，代表欄位值越接近。

OPTIMIZE 照這個數字重排、重寫檔案。



第二層：檔案之間也有區間感

如果只有「檔案內排序」，

每個檔裡面整齊了，

但 A、B、C 檔可能各自混著很多 key 範圍。



做到「檔案間分布」：

重寫時照排序後的連續區間切檔，

形成「檔案 1 大多是 key 0\~50、檔案 2 大多是 50\~100」這種分段感。

查 100\~120 時，前面的檔直接跳過。



▋技術上在做什麼

每個 Parquet 檔都有欄位統計（min/max、null count），

Delta 用這些做 data skipping。

Liquid clustering 透過重排 + 重寫同時改善：

1\.檔案內分布：

同檔案資料在 clustering keys 上更連續，

row group 的 min/max 更窄，

跳過更多 row group

2\.檔案間分布：

不同檔案的 min/max 更少重疊，直接跳過整個檔案

---

▋實際例子

零售銷售分析表 sales，常見聚合：

某門市 + 某商品類別 + 近 7 天的銷售額。

資料亂的話，

很多檔案的 min/max 都涵蓋很廣的 store/category/date，

引擎要掃大量檔案。



設 CLUSTER BY (store_id, category_id, event_date) 後，

Hilbert ordering 把三維接近的資料排一起，



OPTIMIZE 重寫後：

某些檔案主要落在特定 store ，

該 store 內又集中某些 category 日期區間也更連續，

查「store=12、category=3、近 7 天」時，

大量不相關檔案被跳過，聚合的 I/O 明顯下降。

---



▋新功能補充

Automatic Liquid Clustering（DBR 15.4 LTS+）

CREATE TABLE t1 (...) CLUSTER BY AUTO; ALTER TABLE t1 CLUSTER BY AUTO;

需啟用 Predictive Optimization，平台分析歷史查詢自動調整 keys。



OPTIMIZE FULL（DBR 16.0+）

OPTIMIZE table_name FULL;

一般 OPTIMIZE 是增量的，

FULL 會強制全表重新聚類（首次啟用或變更 keys 時用）。



Clustering on Write 觸發門檻

Clustering Keys 數量 / UC Managed Tables / 其他 Delta Tables 1 個 key / 64 MB / 256 MB 2 個 keys / 256 MB / 1 GB 3 個 keys / 512 MB / 2 GB 4 個 keys / 1 GB / 4 GB



小批次寫入不會自動觸發，仍需定期跑 OPTIMIZE。

---



▋實務建議

．Unity Catalog managed tables → 

直接用 CLUSTER BY AUTO + Predictive Optimization 



．小表（<10TB）→ 限制 1-2 個 clustering keys 



．首次啟用或變更 keys → 

執行 OPTIMIZE FULL 



．高頻 insert/update → 

每 1-2 小時排程 OPTIMIZE（或啟用 Predictive Optimization）

---

---



▋考前重點整理

Liquid Clustering = 更彈性的資料組織，

取代傳統 partition + ZORDER，

用 Hilbert curve 把多維資料壓成一維排序，

同時改善檔案內、檔案間的資料分布 keys 可以調整，

靠後續 OPTIMIZE 逐步轉換 跟 partitioning 互斥，

二選一 小批次寫入不會自動觸發 clustering，

要排程 OPTIMIZE






