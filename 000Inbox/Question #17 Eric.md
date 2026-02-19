## Question #17 Eric

Topic 1

A production workload incrementally applies updates from an external Change Data Capture feed to a Delta Lake table as an always-on Structured Stream job.

When data was initially migrated for this table, OPTIMIZE was executed and most data files were resized to 1 GB.

Auto Optimize and Auto Compaction were both turned on for the streaming production job.

Recent review of data files shows that most data files are under 64 MB, although each partition in the table contains at least 1 GB of data and the total table size is over 10 TB.

Which of the following likely explains these smaller file sizes?

A. Databricks has **autotuned** to a smaller target file size to reduce duration of MERGE operations

B. Z-order indices calculated on the table are preventing file compaction

C. Bloom filter indices calculated on the table are preventing file compaction

D. Databricks has autotuned to a smaller target file size based on the overall size of data in the table

E. Databricks has autotuned to a smaller target file size based on the amount of data in each partition

Correct Answer: A



 **Databricks 專有名詞 / 關鍵概念**：

---

## 1️⃣ Change Data Capture（CDC）

- **意思**：只傳「資料有變動的部分」（新增 / 更新 / 刪除）

- **在這題中**：外部系統不斷送「異動資料」進來

- **考點**：CDC 幾乎一定搭配 **MERGE INTO**

---

## 2️⃣ Delta Lake Table

- **意思**：支援 ACID、Time Travel、Schema Evolution 的資料表格式

- **關鍵特性**：

   - 資料是由 **很多 Parquet 檔案組成**

   - 檔案大小會影響效能（小檔問題）

---

## 3️⃣ Structured Streaming（Always-on）

- **意思**：不是一次跑完，是 **長時間持續跑的 streaming job**

- **在這題中**：

   - CDC → Streaming → MERGE 到 Delta Table

- **考點**：

   - Streaming 的寫入策略 ≠ Batch

   - **更保守、追求穩定與低延遲**

---

## 4️⃣ MERGE INTO

- **意思**：同時處理 INSERT / UPDATE / DELETE

- **效能特性（重點）**：

   - 需要 **讀舊檔 + 寫新檔**

   - 檔案越大，MERGE 越慢

- **👉 關鍵考點**：

   - 為了讓 MERGE 快，Databricks **偏好較小的檔案**

---

## 5️⃣ OPTIMIZE

- **意思**：主動把很多小檔案合併成大檔

- **在題目中**：

   - 初始 migration 時，OPTIMIZE → 多數檔案變成 **\~1 GB**

- **考點陷阱**：

   - OPTIMIZE 是「當下狀態」

   - **之後 streaming 寫入仍可能產生小檔**

---

## 6️⃣ Auto Optimize

- **意思**：寫入時，自動幫你優化檔案大小

- **但重點是**：

   - 不是「一定變大檔」

   - 會根據 **寫入模式與效能需求動態調整**

- **Streaming + MERGE 時**：

   - 可能 **刻意寫小一點的檔案**

---

## 7️⃣ Auto Compaction

- **意思**：在寫入後，自動嘗試合併小檔

- **限制（考試很重要）**：

   - Streaming job 下 **compaction 不是無限制**

   - 不一定會合到 1GB 那麼大

---

## 8️⃣ Partition（邏輯分區）

- **意思**：資料的「邏輯分組」（不是實體檔案）

- **題目關鍵句**：

   - 每個 partition ≥ 1 GB

   - 但單一 data file < 64 MB

- **重點理解**：

   - ❗ Partition 大小 ≠ 檔案大小

   - 一個 partition 可以有 **很多小檔**

---

## 9️⃣ Small Files（小檔問題）

- **這題的核心現象**：

   - Table 很大（10+ TB）

   - Partition 也很大

   - 但 **檔案卻很小（<64MB）**

- **關鍵原因**：

   - Streaming + MERGE

   - Databricks 為了 **降低 MERGE latency**

   - **刻意寫小檔**

---

## 🔟 Autotuning（自動調參）⭐考點核心

- **意思**：Databricks 會依 workload 自動調整參數

- **在這題中**：

   - 自動把「目標檔案大小」調小

   - 目的：**讓 MERGE 跑得更快**

- **所以正確答案是**：

   - **A. 為了降低 MERGE 的執行時間**

---

### 0\. 最終答案 (Final Answer)

- **答案：A**

- 因為 CDC 工作負載頻繁執行 `MERGE` 操作，為了避免每次更新都要重寫巨大的檔案（Write Amplification），Databricks 會自動調整目標檔案大小至較小的值（通常遠小於 1GB）。

### 1\. 考點分析 (Question Analysis)

- 核心考點：

    這題在考 Delta Lake 在 MERGE 操作下的自動調優機制 以及 寫入放大（Write Amplification） 的概念。

- **解題關鍵字**：

   - `關鍵字："Change Data Capture (CDC)"` → 代表會頻繁使用 `MERGE` 語法（Update/Delete/Insert）。

   - `關鍵字："most data files are under 64 MB"` → 檔案遠小於一般標準（1GB 或 128MB），這是為了優化重寫速度。

   - `關鍵字："reduce duration of MERGE operations"` → `MERGE` 需要重寫包含更動資料的整個檔案。



### 2\. 解題思路 

1. 這是 CDC 負載，資料會不斷地透過 `MERGE INTO` 指令合併進目標表。

2. 在 Delta Lake 中，要修改某個檔案裡的資料，必須讀出該檔案並**重寫整個檔案**（Copy-on-Write）。

3. **矛盾**：

   - 一般 `OPTIMIZE` 的目標檔案大小是 1GB。

   - 如果每次 `MERGE` 只改一筆資料，卻要重寫 1GB 的檔案，I/O 成本極高（這叫 Write Amplification）。

4. 為了讓 `MERGE` 跑得快，Databricks 的引擎（特別是 Photon 或自動調優功能）會故意將這類頻繁更新的表，其目標檔案大小設得比較小（例如 16MB - 64MB），這樣重寫時只要寫入少量數據即可。

5. **選項**：只有 **選項 A** 提到為了減少 `MERGE` 時間而調小檔案大小，符合邏輯。

### 3\. 選項詳解 (Option Analysis)

- **正確答案：A**

   - **Databricks has autotuned to a smaller target file size to reduce duration of MERGE operations**

   - 完全正確。這是 Databricks Runtime 的優化行為。針對頻繁 `MERGE` 的 Delta Table，系統會偵測到重寫大檔案的成本過高，因此自動覆蓋預設的檔案大小設定（無論是 `Auto Optimize` 的 128MB 或 `OPTIMIZE` 的 1GB），將其降低以提升 `MERGE` 效能。

- **錯誤選項：B**

   - **Z-order indices calculated on the table are preventing file compaction**

   - 錯誤。Z-Order 是一種資料佈局（Data Layout）算法，通常是在執行 `OPTIMIZE` 時一起做的。它不會「阻止」Compaction，相反地，它通常與 Compaction 是一起發生的過程。

- **錯誤選項：C**

   - **Bloom filter indices calculated on the table are preventing file compaction**

   - 錯誤。Bloom Filter 是用於加速查詢（Data Skipping）的索引結構，與檔案大小的 Compaction 邏輯無直接衝突，也不會阻止檔案合併。

- **錯誤選項：D & E**

   - **Based on overall size / data in each partition**

   - 錯誤。一般來說，表越大或分區越大，Databricks 傾向將檔案做得**更大**（接近 1GB）以減少 Metadata 壓力並提升讀取效能。只有在需要頻繁更新（`MERGE`）時，才會反向操作將檔案變小。

## 4\. 關鍵知識清單 (Key Concepts Checklist)

- `Write Amplification（寫入放大）`：在 Copy-on-Write 機制中，為了修改極少量數據而必須重寫大量數據的現象。

- `MERGE Operation`：Delta Lake 中用於處理 CDC 的指令，支援同時進行 Insert、Update 和 Delete。

- `Auto Optimize / Auto Compaction`：Databricks 的自動小檔案合併功能，預設目標通常是 128MB，但在 `MERGE` 場景下會動態調整。

## 5\. 專家補充 (Pro Tips)

- 考試陷阱：

    很多學生死記硬背「OPTIMIZE 預設是 1GB」或「Auto Compaction 預設是 128MB」，看到 64MB 就覺得系統壞了。請記住，效能優化是動態的，特別是遇到 MERGE 這種高成本操作時，"Small files are better for writes (rewrites), Large files are better for reads"。Databricks 正在犧牲一點讀取效能（檔案較碎）來換取大幅提升的寫入/合併效能。





---

# Databricks 檔案管理與 CDC 核心觀念統整

### 1\. 場景：什麼是 CDC？

想像你正在維護一本「會員通訊錄」（資料表）。

每天都有人搬家（Update）、加入（Insert）或退出（Delete）。

這種捕捉資料變動的過程，就叫 CDC (Change Data Capture)。

在 Databricks 裡，我們用 **`MERGE`** 指令來一次搞定這些變動。

---

### 2\. 挑戰：寫入放大 (Write Amplification)

Delta Lake 的檔案是 **「寫了就不能改」** (Immutable) 的 Parquet 檔。

- **機制**：如果你要修改檔案裡的「一行字」，你不能直接塗改。

- **後果**：你必須把 **「整個檔案」** 讀出來，修改那一行，然後 **「重寫成一個新檔案」**。

- **寫入放大**：如果你為了改 **1KB** 的資料，被迫重寫 **1GB** 的檔案，這就叫「寫入放大」。這會讓 `MERGE` 跑得非常慢。

---

### 3\. 策略：檔案大小的黃金三角

為了處理上述挑戰，Databricks 會根據用途，選擇不同的檔案大小。我們可以把它想像成 **「包裝策略」**：

#### A. 1GB：家庭號大包裝 (Costco)

- **適用情境**：**歷史查詢、BI 報表 (Read Heavy)**。

- **指令**：`OPTIMIZE` (預設)。

- **邏輯**：

   - **優點**：讀取時「拿一包」就有大量資料，效率極高；壓縮比最好，省空間。

   - **缺點**：如果你只想改裡面的一小部分，要拆開巨大包裝再重包，非常痛苦（寫入放大最嚴重）。

#### B. 128MB：標準鋁箔包 (Standard)

- **適用情境**：**一般 ETL、串流寫入 (General / Streaming)**。

- **指令**：`Auto Compaction` (預設)。

- **邏輯**：

   - **優點**：**平衡點**。Spark 的運算單元（Task）處理這個大小最順手；傳輸也方便。

   - **缺點**：對於超級巨大的查詢來說，檔案數量還是稍微多了一點。

#### C. < 64MB：便條紙 (CDC Optimized)

- **適用情境**：**頻繁修改 (CDC / MERGE)**。

- **指令**：系統自動調優 (針對 `MERGE` 操作)。

- **邏輯**：

   - **優點**：**重寫超快**。因為檔案小，修改資料時只要重寫一點點東西，大幅降低「寫入放大」。

   - **缺點**：讀取時像在看滿地的便條紙，比較慢且亂（所以等更新結束後，通常會再做一次 `OPTIMIZE` 整理回大檔案）。

---

### 一張表總結

| **檔案大小** | **像什麼？** | **適合做什麼？** | **為什麼？** | 
|---|---|---|---|
| **1 GB** | **大字典** | **讀取 / 查詢** | 翻閱次數少，一次讀很多。 | 
| **128 MB** | **雜誌** | **一般處理** | 大小適中，好拿好放 (Spark 最愛)。 | 
| **< 64 MB** | **便條紙** | **修改 / CDC** | **重寫成本低**，撕掉一張重寫很快。 | 

**考試與實務心法：**

> 如果系統發現你在做 CDC (MERGE)，它會自動把檔案切成 便條紙 (<64MB) 來加速寫入；
>
> 等到你要做 年終報表 (Query) 時，你再手動執行 OPTIMIZE 把便條紙整理成 大字典 (1GB) 來加速讀取。

![CleanShot 2025-12-15 at 21.27.36@2x.png](./Question%20#17%20Eric-assets/CleanShot%202025-12-15%20at%2021.27.36@2x.png)

# Question #18 Eric

Topic 1

Which statement regarding stream-static joins and static Delta tables is correct?

A. Each microbatch of a stream-static join will use the most recent version of the static Delta table as of each microbatch.

B. Each microbatch of a stream-static join will use the most recent version of the static Delta table as of the job's initialization.，

C. The checkpoint directory will be used to track state information for the unique keys present in the join.

D. Stream-static joins cannot use static Delta tables because of consistency issues.

E. The checkpoint directory will be used to track updates to the static Delta table.

Correct Answer: A

好，這一題我們一樣用 **「關鍵字清單＋考試白話」** 的方式來拆。
重點會放在 **stream-static join 為什麼選 A、其他為什麼錯**。

---

## 1️⃣ Stream-Static Join

- **意思**：
   👉 一邊是 **Streaming DataFrame**
   👉 另一邊是 **Static（非 streaming）Delta Table**

- **常見用途**：

   - Streaming event + 維度表（店家、設備、設定檔）

- **考試重點**：

   - **只有 stream 那邊是 stateful**

   - static table **不進 checkpoint**

---

## 2️⃣ Static Delta Table

- **不是什麼？（超重要）**

   - ❌ 不是 streaming source

   - ❌ 不是 state table

- **是什麼？**

   - 一張「普通的 Delta Table」

   - 每次 join 時 **讀取它的 snapshot**

- **關鍵詞**：
   👉 **Delta snapshot（版本快照）**

---

## 3️⃣ Microbatch

- **意思**：

   - Structured Streaming 不是 continuous

   - 而是「一批一批（microbatch）」處理

- **考試關鍵**

   - ❗**每個 microbatch 都是一次新的 query execution**

   - 所以可以：

      - 重新讀 table

      - 重新取得最新 snapshot

---

## 4️⃣ Delta Snapshot ⭐（這題的靈魂）

- **意思**：

   - Delta Lake 在某一個時間點的「一致性版本」

- **在這題中**

   - 每個 microbatch：

      - 都會讀取 **當下最新 commit 的 snapshot**

- **因此導出正確選項 A**

---

## 5️⃣ Most recent version *as of each microbatch*（選項 A）

- **白話翻譯**：

   > 每一個 microbatch，都會用「那一刻最新的 static Delta table」

- **為什麼是對的**

   - Streaming job 沒鎖住 static table

   - Delta 的 snapshot isolation 保證一致性

- **一句考試記憶法**：

   > **microbatch = 新查詢 = 新 snapshot**

---

## 6️⃣ Job initialization（選項 B 為什麼錯）

- **Job initialization 是什麼**

   - Streaming job 啟動的那一刻

- **為什麼錯**

   - ❌ Databricks 不會把 static table snapshot 固定在啟動時

   - ❌ 那樣會讓維度表更新完全失效

- **錯誤類型**

   - 把 stream-static join 誤認成 broadcast cache

---

## 7️⃣ Checkpoint Directory

- **真正用途**

   - 記錄：

      - streaming offset

      - streaming state（僅限 stateful operations）

- **不會記錄什麼**

   - ❌ static table 的內容

   - ❌ static table 的版本

- **所以**

   - C、E 都錯

---

## 8️⃣ Stateful Join（用來排除選項 C）

- **什麼情況才需要 state**

   - stream-stream join

   - window aggregation

- **stream-static join**

   - ❌ static side 不進 state

   - ❌ 不追蹤 key 狀態

- **因此**

   - C：「track state for unique keys」是錯的

---

## 9️⃣ Consistency Issues（用來排除選項 D）

- **Delta Lake 提供什麼**

   - ACID

   - Snapshot isolation

- **所以**

   - stream-static join **完全合法、非常常見**

   - ❌ 不存在一致性問題

---

## 🔟 用一張「考試用對照表」記住

| 概念 | Stream-Static Join | 
|---|---|
| Static table 是否 streaming | ❌ | 
| 是否進 checkpoint | ❌ | 
| 是否有 state | ❌ | 
| Snapshot 取得時機 | **每個 microbatch** | 
| 正確選項 | **A** | 

---

## 🧠 一句話背誦版（超適合考前）

> **Stream-static join：
> static table 不進 checkpoint，
> 每個 microbatch 讀最新 Delta snapshot。**

如果你願意，下一步我可以幫你做：
👉 **「Structured Streaming Join 類型一頁比較表（stream-static / stream-stream / static-static）」**
那張表幾乎可以秒殺相關考題。

# Question #18 解析

## 0\. 最終答案 (Final Answer)

- **答案：A**

- **一句話解析**：在 Stream-Static Join 中，串流的每一個 Micro-batch 執行時，都會重新讀取靜態表（Static Table）的當下最新快照（Snapshot）。

## 1\. 考點分析 (Question Analysis)

- 核心考點：

   這題在考 Stream-Static Join（串流與靜態表關聯）的語意與行為。

- **解題關鍵字**：

   - `關鍵字："stream-static joins"` → 串流資料與一張不會動（或緩慢變動）的表做 Join。

   - `關鍵字："most recent version"` → 考數據的新鮮度（Freshness）。

## 2\. 簡易解題思路 (Logic Path)

1. **理解架構**：Structured Streaming 執行時，是將無窮的資料切成一個個小批次（Micro-batch）來處理。

2. **執行流程**：

   - Batch 1 啟動 → 讀取 Stream offset → 讀取 Static Table (Version 1) → Join → 輸出。

   - (此時 Static Table 被外部程序更新成 Version 2)。

   - Batch 2 啟動 → 讀取 Stream offset → **重新讀取 Static Table** (此時會讀到 Version 2) → Join → 輸出。

3. **推導結論**：Spark 不會快取那張 Static Table 到永遠，每一個 Micro-batch 都是一個獨立的執行計畫，會去讀取當下該 Delta Table 的最新版本。

4. **比對選項**：**選項 A** 描述了這個行為。

## 3\. 選項詳解 (Option Analysis)

- **正確答案：A**

   - **Each microbatch of a stream-static join will use the most recent version of the static Delta table as of each microbatch.**

   - 正確。這是標準行為。由於 Delta Lake 支援快照隔離（Snapshot Isolation），每個 Micro-batch 啟動時都會取得靜態表當下的最新快照。這讓 Stream-Static Join 非常適合用來做「Lookup（查表）」操作（例如：ID 轉 名稱），且查表內容可以隨時間更新。

- **錯誤選項：B**

   - **...as of the job's initialization.**

   - 錯誤。如果 Spark 這麼做，那靜態表的任何更新在串流重啟前都無法生效，這不符合實務需求，也不是 Spark 的運作方式。

- **錯誤選項：C**

   - **The checkpoint directory will be used to track state information for the unique keys present in the join.**

   - 錯誤。Stream-Static Join 本質上是 **Stateless（無狀態）** 的 Join（除非你另外加了 aggregation）。Spark 不需要維護 Join 的 State Store，因為它只是單純地拿每一筆串流資料去對應靜態表。Checkpoint 主要是存 Stream 的 Offset，而不是 Join Keys。

   - *註：只有 Stream-Stream Join 才需要大量維護 State 來等待兩邊資料到達。*

- **錯誤選項：D**

   - **Stream-static joins cannot use static Delta tables...**

   - 錯誤。這是最常見的使用案例之一（Data Enrichment）。

- **錯誤選項：E**

   - **The checkpoint directory will be used to track updates to the static Delta table.**

   - 錯誤。Checkpoint 只負責追蹤「Streaming source」讀到了哪裡（Offset）。它不管靜態表發生了什麼事，靜態表就是每次讀當下最新的。

## 4\. 關鍵知識清單 (Key Concepts Checklist)

- `Stream-Static Join`：串流資料與靜態資料表的關聯操作。

- `Micro-batch Execution`：Structured Streaming 預設的執行模式，將串流視為一連串的小型批次作業。

- `Stateless Join`：Stream-Static Join 不需要 State Store，因為不需要等待另一邊的資料（靜態資料已經在那裡了）。

## 5\. 專家補充 (Pro Tips)

- 實務 vs 考試：

   雖然選項 A 是正確的（每個 batch 讀最新版），但在實務上，如果靜態表非常大，每個 Micro-batch 都重讀一次 Metadata 或數據可能會導致效能瓶頸。

   - **優化技巧**：實務上我們有時會將小的靜態表 `Broadcas` 出去，或者啟用 Delta Lake 的 `Client-side caching` 來加速讀取。

   - **考試重點**：在考試中，只要記得「靜態表不是死的，下一批次會讀到新數據」這個觀念即可。這意味著如果你的 Dimension Table（維度表）更新了，正在跑的 Streaming Job **不需要重啟**就能自動在下一個批次套用新的維度資料。

![CleanShot 2025-12-15 at 21.25.47@2x.png](./Question%20#17%20Eric-assets/CleanShot%202025-12-15%20at%2021.25.47@2x.png)