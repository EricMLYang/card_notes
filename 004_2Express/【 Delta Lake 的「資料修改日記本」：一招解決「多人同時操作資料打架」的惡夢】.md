【 Delta Lake 的「資料修改日記本」：一招解決「多人同時操作資料打架」的惡夢】

![CleanShot 2025-11-05 at 22.17.32@2x.png](./【%20Delta%20Lake%20的「資料修改日記本」：一招解決「多人同時操作資料打架」的惡夢】-assets/CleanShot%202025-11-05%20at%2022.17.32@2x.png)

\
參考書：**Databricks Certified Data Engineer Associate Study Guide**



Delta Lake 是一種讓「資料湖」變得更可靠的技術，

想像把很多資料（購物紀錄、感測器資料）放在雲端硬碟裡，

這些資料本來只是一些檔案（通常是 **Parquet 檔**），

沒有記錄誰改了什麼，也不容易保證資料正確，

因此 Delta Lake 建一張表時，除了存放資料檔之外，

系統還會多放一個「**交易日誌（Transaction Log）**」，

這是一個 **JSON 檔案**，

用來記錄每一次的變更。



可以把它想成是「資料的修改日記本」，

裡面會記下：

．誰新增了資料（像新的一筆紀錄）

．誰刪除了資料

．誰修改了資料

．哪些檔案是現在最新版的



▋**為什麼要有這個日誌？**

有了這個 Transaction Log，Delta Lake 才能：

**．保證資料一致**（不會有人在寫入時資料壞掉）

**．支援回到過去版本**（像「時間旅行」功能）

**．知道哪個檔案是最新版本**

**．支援同時多人操作資料，不會打架**

以下用幾個情境來說明：



▋**寫入與讀取的情境**

**Alice** 建立一個新的表，並放入一些資料，

Delta Lake 把資料分成幾個部分存起來，

例如：part-0001.parquet,  part-0002.parquet

這些檔案就存在雲端儲存空間裡。



當 Alice 資料寫完，

Delta Lake 會在資料夾裡多放一個

\_delta_log/000.json 檔案，

這個 JSON 檔就像一份「變更紀錄表」，裡面記下：

．這次做了什麼操作（例如「新增資料」）

．哪些檔案是新產生的（part-0001, part-0002）

．寫入的時間

．其他關於這次變更的細節

---



當 Alice 寫好資料後，**Bob 想要讀取那張表**，

**Delta Lake 先讀「交易日誌」 (\_delta_log/000.json)**

看看裡面記錄了哪些資料檔是「最新的版本」。

**根據日誌內容讀取正確的資料檔**

假設日誌裡寫著：新增檔案: part-0001.parquet, part-0002.parquet

Delta Lake 就只會去讀這兩個檔案的內容。

這樣能確保 Bob 看到的資料，跟 Alice 最後寫入的版本完全一樣。

---





▋**資料更新情境（Updating Scenario）**

**Alice** 要修改一筆原本存在於 part-1.parquet 的資料，

但因為 Parquet 檔是「**不能直接改的**」（ immutable），

Delta Lake 會把原本的資料複製出來，

改成新內容後，存成新的檔案：part-3.parquet。



Delta Lake 接著新增一個新的日誌檔：\_delta_log/001.json，

記下 part-1.parquet 已經被淘汰，

part-3.parquet 是新的版本。



當 Bob 讀資料時，

系統會先看最新的日誌（001.json），

發現有效的檔案是 part-2.parquet 和 part-3.parquet，

就只讀這兩個，忽略舊的 part-1.parquet。





---



▋**同時讀寫的情境（Concurrent Writes and Reads）**

Alice 在新增資料（產生新檔案 part-4.parquet），

而 Bob 此時正在查詢這張表。

當 Bob 開始查詢時，最新的交易日誌（001.json）

只記錄了 part-2.parquet 和 part-3.parquet。

因為 Alice 的新檔 part-4.parquet 還沒寫完，

系統只會讓 Bob 讀這兩個「已完成」的檔案。

Delta Lake 不會讓 Bob 等 Alice 寫完。

它會確保：

．Bob 讀到的是一個完整、正確的版本

．Alice 寫的資料不會被錯誤地讀到一半

．兩人操作互不干擾



當 Alice 寫完後，Delta Lake 會新增新的交易日誌 002.json，

讓這個版本正式包含 part-4.parquet。

---



---





▋**寫入失敗的情境（Failed Writes Scenario）**

**Alice** 嘗試新增一筆資料，Delta Lake 準備建立 part-5.parquet，

但在寫入過程中發生錯誤，檔案沒寫完、變成「不完整檔」，

因為寫入沒有成功，Delta Lake 不會把這筆操作

記在交易日誌裡（也不會產生新的 JSON 檔）。



當 Bob 查資料時，系統一樣會先讀交易日誌。

裡面只有 part-2.parquet、part-3.parquet、part-4.parquet 的紀錄，

所以他只會看到這些「成功版本」的資料。

那個壞掉的 part-5.parquet 根本不會被讀到。



—

**Delta Lake 的優點**



**ACID**

交易日誌讓 Delta Lake 能像資料庫一樣，支援 **ACID 特性**：

操作要嘛全部成功，要嘛全部失敗（不會半套）

確保資料一致、可靠、不出錯。



高效：

Delta Lake 把表格的結構與統計資訊都記在交易日誌裡，

不需要依賴外部的「集中式資料庫」。

這樣在處理大型資料夾或查詢大量資料時會更快。



**完整的操作記錄（Audit Logging）**

每一次新增、修改、刪除都會被記錄下來，

包含時間與操作者，方便追蹤資料變化與進行稽核。





---



---