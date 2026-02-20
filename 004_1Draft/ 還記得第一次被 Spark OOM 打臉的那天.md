---
tags:
  - my-article
Checkbox 1: false
---
 **還記得第一次被 Spark OOM 打臉的那天**

那時候我寫了一個看起來很單純的 `groupBy`,結果 job 跑到一半就掛了。錯誤訊息寫著「Container killed by YARN for exceeding memory limits」。

我當下的反應是:「什麼?我只是做個分組聚合,怎麼會炸記憶體?」

後來我才發現:原來某個 user_id 佔了整個資料集的 60%,導致單一 partition 爆炸性成長。

**這不是 bug,這是 Spark 在告訴我:「你寫的 code 背後有物理代價,而你還沒學會預測它。」**

---

## 💡 中段:核心概念

### Spark 真正的價值:把混亂變得可預測

很多人說 Spark 的優勢是「分散式運算」或「in-memory computing」。但用了幾年後,我發現更關鍵的是:

**Spark 把分散式系統裡那些原本不可控的混亂,變成一種「工程師可以學習的語言」。**

什麼樣的混亂?

1. **時間的混亂** - 某個 task 為什麼跑特別慢?是 GC pause 還是資料傾斜?

2. **空間的混亂** - 為什麼記憶體突然爆了?是 shuffle 太大還是 cache 策略錯誤?

3. **資料分佈的混亂** - 為什麼 200 個 task 裡只有 3 個在跑,其他都 idle?

### 從「會用」到「會駕馭」的分水嶺

**初學者眼中:**

- Spark 好麻煩,一下 OOM,一下 shuffle 很慢,一下 skew...

**老手眼中:**

- 你加一個 `groupBy` → 我知道會產生一次 shuffle

- 你用 `cache()` → 我知道記憶體壓力會上升

- 你有個 hot key → 我知道會有某幾個 task 特別慢

**這不是超能力,而是你開始「預測」code 背後的物理行為。**

當你能預測這些,你就從「Spark 使用者」變成「混亂的駕馭者」。

---

## 🔍 承認侷限,保持客觀

當然,Spark 也沒有把所有混亂都完全馴服。

像是:

- **AQE (Adaptive Query Execution)** 會動態調整執行計畫 — 這本身又引入了新的「有管理的隨機性」

- **Cost-based optimizer** 的決策邏輯仍像黑箱

- **不同 executor 的資源競爭**、network jitter、GC timing 等,仍有無法完全預測的部分

但這些是「更高階的混亂」— 是**系統替你做決策**,而非你完全失控。

這就像:

- 原始的分散式系統 = 你在暗房裡摸索

- Spark = 房間裡有燈,但偶爾會閃爍

- 理想的系統 = 永遠明亮(但不存在)

**Spark 做到的,是把分散式的「暗房」變成「有規律的明暗交替」。**

---

## 🎯 結尾:連結到更廣的工程價值

### 這不只是談 Spark,而是工程成熟度的標誌

**真正的工程成熟度,不是把混亂消滅,而是把混亂納入模型。**

當你能夠:

- 看到一段 code,就預測它的執行計畫

- 看到 Spark UI,就知道瓶頸在哪

- 看到資料特性,就知道該用什麼優化策略

你展現的不只是「會用工具」,而是:

✅ **你理解分散式系統的本質**\
✅ **你能把不確定性變成風險管理**\
✅ **你能為團隊建立可預測的交付品質**

這也是為什麼在組織裡,「懂底層的人」價值特別高 — 不是因為他們會寫更多 code,而是**他們能讓系統行為變得可推理,讓團隊少踩坑,讓成本可控制**。

---

## 💬 金句收尾

**「我們不可能把分散式系統變得完全乾淨,但我們可以讓它『髒得有規律』。**\
**Spark 做到的,就是把這個『有規律的髒』商品化。」**

而你的工作,就是學會讀懂這套規律。

---

**你有過類似的 Spark 踩坑經驗嗎?歡迎分享你的「混亂管理」心得。**

---

---

# 📚 附錄:Spark 效能/成本/速度/分佈相關專有名詞清單

## 🏗️ 核心架構層

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **RDD** | 彈性分散式資料集 | Spark 最底層的資料抽象 | 
| **DataFrame** | 資料框 | 有 schema 的分散式資料集 | 
| **Dataset** | 資料集 | 強型別的 DataFrame (Scala/Java) | 
| **DAG** | 有向無環圖 | Spark 執行計畫的邏輯結構 | 
| **Stage** | 階段 | 一組可以平行執行的 task | 
| **Task** | 任務 | 單一 partition 上的運算單元 | 
| **Partition** | 分區 | 資料的分割單位 | 
| **Executor** | 執行器 | 運算資源的容器 (JVM process) | 
| **Driver** | 驅動程式 | 控制整個 Spark application 的節點 | 

## 🔄 資料移動與 Shuffle

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Shuffle** | 洗牌 | 跨 partition 的資料重分配 | 
| **Shuffle Partition** | Shuffle 分區數 | shuffle 後產生的 partition 數量 (預設 200) | 
| **Shuffle Write** | Shuffle 寫入 | 資料寫到磁碟準備傳輸 | 
| **Shuffle Read** | Shuffle 讀取 | 從其他 executor 讀取 shuffle 資料 | 
| **Shuffle Spill** | Shuffle 溢寫 | 記憶體不足時寫到磁碟 | 
| **Network I/O** | 網路 I/O | shuffle 過程的網路傳輸 | 
| **Wide Dependency** | 寬依賴 | 需要 shuffle 的轉換 (如 groupBy) | 
| **Narrow Dependency** | 窄依賴 | 不需 shuffle 的轉換 (如 map, filter) | 

## ⚖️ 資料傾斜 (Data Skew)

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Data Skew** | 資料傾斜 | 資料分佈不均勻 | 
| **Hot Key** | 熱點鍵 | 某個 key 的資料量遠超其他 | 
| **Straggler Task** | 落後任務 | 執行特別慢的 task | 
| **Salting** | 加鹽 | 為 skew key 加隨機後綴打散 | 
| **Skew Join** | 傾斜連接 | 處理有 skew 的 join 操作 | 
| **AQE Skew Join Optimization** | AQE 傾斜連接優化 | Spark 3.0+ 自動處理 skew join | 

## 🧠 記憶體管理

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Memory Fraction** | 記憶體分配比例 | execution vs storage 的記憶體分配 | 
| **Execution Memory** | 執行記憶體 | 用於 shuffle/join/sort 等運算 | 
| **Storage Memory** | 儲存記憶體 | 用於 cache/persist 的記憶體 | 
| **Off-Heap Memory** | 堆外記憶體 | JVM heap 之外的記憶體 | 
| **Spill to Disk** | 溢寫到磁碟 | 記憶體不足時寫到磁碟 | 
| **OOM** | 記憶體溢位 | Out of Memory 錯誤 | 
| **GC (Garbage Collection)** | 垃圾回收 | JVM 記憶體清理,會造成 pause | 
| **GC Pause** | GC 暫停 | GC 時整個 executor 暫停 | 

## ⚡ 快取與持久化

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Cache** | 快取 | 將資料存在記憶體 (= persist(MEMORY_ONLY)) | 
| **Persist** | 持久化 | 指定儲存層級保存資料 | 
| **Storage Level** | 儲存層級 | MEMORY_ONLY, DISK_ONLY, MEMORY_AND_DISK 等 | 
| **Unpersist** | 解除持久化 | 釋放 cache 的資料 | 
| **Checkpoint** | 檢查點 | 將資料寫到可靠儲存 (如 HDFS) | 
| **Lineage** | 血緣 | RDD 的依賴關係鏈 | 

## 🎛️ 執行優化

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Lazy Evaluation** | 延遲執行 | transformation 不立即執行,遇到 action 才觸發 | 
| **Action** | 行動 | 觸發實際運算的操作 (collect, count, save) | 
| **Transformation** | 轉換 | 建立新 RDD 的操作 (map, filter, join) | 
| **Catalyst Optimizer** | Catalyst 優化器 | Spark SQL 的查詢優化引擎 | 
| **Predicate Pushdown** | 謂詞下推 | 將 filter 條件推到資料源層 | 
| **Column Pruning** | 欄位裁剪 | 只讀取需要的欄位 | 
| **Broadcast Join** | 廣播連接 | 將小表廣播到所有 executor | 
| **Broadcast Variable** | 廣播變數 | 將唯讀資料廣播到所有 executor | 

## 🔧 Spark 3.0+ 進階功能

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **AQE** | 自適應查詢執行 | Adaptive Query Execution,動態優化 | 
| **Dynamic Partition Pruning** | 動態分區裁剪 | 執行時根據 join 條件過濾分區 | 
| **Coalesce Shuffle Partitions** | 合併 Shuffle 分區 | AQE 自動減少空的 shuffle partition | 
| **Dynamic Resource Allocation** | 動態資源分配 | 依據負載自動增減 executor | 
| **Speculative Execution** | 推測執行 | 為慢 task 啟動備份 task | 

## 📊 效能監控與除錯

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Spark UI** | Spark 介面 | 監控 job/stage/task 的 Web UI | 
| **Event Timeline** | 事件時間軸 | 顯示 task 執行時間分佈 | 
| **Metrics** | 指標 | CPU、記憶體、I/O 等監控數據 | 
| **Executor Logs** | 執行器日誌 | 各 executor 的 stdout/stderr | 
| **Driver Logs** | 驅動程式日誌 | Driver 的執行日誌 | 
| **Explain Plan** | 執行計畫 | 顯示 Spark 如何執行查詢 | 

## 💰 成本相關

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Cluster Mode** | 叢集模式 | Standalone, YARN, Kubernetes, Mesos | 
| **Spot Instance** | 競價實例 | AWS/GCP 等的低價但可被中斷的機器 | 
| **Auto-scaling** | 自動擴展 | 依據負載自動增減資源 | 
| **Cost Per Query** | 每查詢成本 | 單次查詢消耗的計算成本 | 
| **DBU** | Databricks 單位 | Databricks 的計費單位 | 

## 🗂️ 資料格式與分區

| 專有名詞 | 中文 | 說明 | 
|---|---|---|
| **Parquet** | Parquet 格式 | 列式儲存格式,適合分析 | 
| **ORC** | ORC 格式 | Optimized Row Columnar,另一種列式格式 | 
| **Partition Column** | 分區欄位 | 用於實體分區的欄位 (如日期) | 
| **Bucketing** | 分桶 | 將資料依 hash 分成固定數量的檔案 | 
| **Coalesce** | 合併 | 減少 partition 數量 (不 shuffle) | 
| **Repartition** | 重分區 | 調整 partition 數量 (會 shuffle) | 

---

## 🎓 學習路徑建議

如果你想深入理解這些概念,建議的學習順序:

### Level 1: 基礎概念

- RDD, DataFrame, Dataset

- Transformation vs Action

- Partition 的概念

- Lazy Evaluation

### Level 2: 執行機制

- DAG, Stage, Task

- Shuffle 的運作原理

- Wide vs Narrow Dependency

- Spark UI 的閱讀

### Level 3: 效能優化

- Cache/Persist 的使用時機

- Broadcast Join

- Data Skew 的識別與處理

- Partition 數量的調整

### Level 4: 進階調校

- AQE 的運作原理

- Memory 管理與 GC tuning

- Cost-based Optimizer

- 各種 Storage Level 的取捨

### Level 5: 生產環境

- 監控與告警

- 成本優化

- Cluster 管理

- Troubleshooting 流程

---

**這份清單涵蓋了你在處理 Spark 效能、成本、速度、資料分佈問題時,90% 會遇到的專有名詞。建議可以存起來當作 cheatsheet!**