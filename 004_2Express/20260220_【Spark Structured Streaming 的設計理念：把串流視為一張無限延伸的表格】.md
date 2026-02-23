---
tags:
  - my-article
Checkbox 1: true
---
【Spark Structured Streaming 的設計理念：把串流視為一張無限延伸的表格】





▋ Spark 把串流當未完成的表格

整理 Spark 與 Databricks 技術筆記時，

讀到一個核心觀念，

Structured Streaming 設計者，

Matei Zaharia 和 Michael Armbrust 定義，

Batch = 固定大小的表格（bounded table），

而 Streaming 視為不斷增長的無限表格（unbounded table），

兩者都應該用 DataFrame / SQL 處理，

這個就是 Spark Structure Streaming 設計哲學。



▋ 好處 1：Batch 和 Streaming 可用同一套語法

為了避免開發者為 Batch 和 Streaming 寫兩套程式碼，

Streaming 視為一個不斷有新資料 Append 進來的無限表格，

讓兩者可以使用相同的 DataFrame API 與 SQL 語法，

例如以下跟 batch 幾乎一樣，

\`\`

df = spark.readStream.format("kafka")...

agg = df.groupBy("event").count()

agg.writeStream.format("delta").start()

\`\`

 開發者不需要學習兩套不同的思維模式。

—

▋ 好處2: 持續沿用 Spark 的的底層強項

Spark 的底層強項在於 

．SQL 優化引擎 Catalyst

．資料格式 Tungsten / columnar

．分散式 DataFrame API

．DAG-based 批次計算

如果採用像 Flink 那樣的逐筆事件處理，

Spark 就無法利用它原本最強大的優化機制。

—

▋妥協：無法做到真正事件情串流

與真正串流最大差異在  **Micro-batch overhead，**

Spark 每個 micro-batch 必定需要:

．DAG 生成與優化：每個 micro-batch 都會重新 compile incremental query plan

．Task 調度與分配：這是 micro-batch latency 的最大來源之一)

．Shuffle 階段

．Checkpoint 寫入

．State store 讀寫

這些會至少延遲約 100ms 左右，

這與 Apache Flink 用事件模型有本質上的差異，

但如果即時性需求只是秒級，

Spark 可能會是比較合適的選項。

—



▋ Micro-batch 與 Checkpoint 的運作機制

Spark 的 Micro-batch 架構中，

Driver 負責協調，

將資料流切分成小 Batch，

資料主要流向如下，

Driver 決定每一批次的 Offset 範圍，

分派給 Executors 執行計算，

最後寫入目的地。



其中 Checkpoint 是 streaming 引擎的核心，

為了確保容錯，

Spark 必須依賴 Checkpoint 記錄 Offset 與 State Store，

如果任務失敗重啟，

它可以從上次中斷的地方繼續，

雖然這種機制存在約 100ms 左右的延遲，

因為 Spark 的最佳化作業時間無法縮短，

但換來的是高吞吐量與穩定性。

—



▋ Autoloader:設計理念的最佳實踐

Databricks Autoloader 是這個設計理念的實踐，

他是基於 Structure Streaming，

加上一層處理雲端檔案的機制，

解決 Structured Streaming 讀檔效率較差的問題，

Autoloader  本質上是：

「把雲端的檔案事件轉換成 Structured Streaming Source 的增量資料讀取引擎。」

簡單來說就是最佳化 file-based Streaming Source，

Spark Streaming 負責計算邏輯，

Autoloader 負責提供增量檔案。



當我們使用 Autoloader 時，

其實就是告訴 Spark，

把這些雲端檔案當成無限增長的表格，

透過 Checkpoint 機制追蹤哪些檔案是新的， 

並自動增量讀取，

補充 Autoloader 依賴 Structured Streaming 的 checkpoint，\
並產生自己的 metadata log。

\_checkpoint/

    └── cloudFiles-metadata/



▋ 追求的是統一，而非極致低延遲

Structured Streaming 設計不是追求極致的低延遲，

 而是追求「統一」，

它透過將串流抽象化為表格，

這個設計讓資料工程師可以用同一套思維模式，

處理批次與即時資料。