【 Parquet 概念入門： 用比喻來搞懂 Parquet 為何這麼高效?】

<https://data-mozart.com/parquet-file-format-everything-you-need-to-know/>

不是壓縮率的問題，

也不只是欄式存儲那麼簡單，

 真正的差異藏在 Row Group、Column Chunk、Page 這些層次結構的設計細節裡。

這篇文章用比喻的方式先拆解 Parquet 的內部結構，

希望讓我自己不只知道「它很快」，

還能理解「為什麼快」、「什麼時候該用」。



▋Parquet 格式是工程師視角的智慧資料包

當我們說 Parquet 是一種高效率的資料格式時，

可以把它想像成工程師之間傳遞的大型「智慧資料包」。



在傳統的 CSV 檔案裡，

所有資料就像一張攤平的 Excel，

每一行代表一筆資料，

沒有壓縮、沒有結構。



當資料量變大時，這樣的檔案又肥又慢。

Parquet 則像是一個設計精密的「資料郵件包」，

裡面不僅整理得井井有條，

還自帶說明書與壓縮功能，

讓你寄得快、拆得準、讀得快。





▋CSV vs Parquet:收據與檔案櫃的差異

CSV 就像一張長長的收據，

從頭到尾逐行掃描，

每次查詢都要讀完整行，

即使你只需要其中一個欄位。



Parquet 就像一個有索引的檔案櫃，

直接跳到需要的抽屜(Row Group)，

打開需要的資料夾(Column Chunk)，

抽出需要的文件(Page)，

完全跳過不相關的資料。



這種「按需取用」的設計，

讓 Parquet 在大數據場景下的查詢效率遠超傳統格式。





▋Parquet 的結構比喻

每個 Parquet 檔案可以想像成一個有層次的包裹，

從外到內包含以下部分:



▋結構1. Header(封面標籤)

就像郵件外包裝上標註「這是一個 Parquet 包裹」，

讓接收系統知道該用 Parquet 的方式打開，

通常只包含 Magic Number(`PAR1`)來標示檔案類型。



▋結構2. Row Group(資料群組)

這是「水平切分」的概念，

把整批資料分成幾個大堆，

比如 100 萬筆資料可能切成 10 個 Row Group，

每個包含 10 萬筆完整的資料列。

這樣設計更方便分散式系統 (如 Spark)同時處理不同的 Row Group，

大幅提升讀取速度。



記憶體管理也很有優勢，因為不用一次載入整個檔案，

可以逐個 Row Group 處理,避免記憶體爆炸。



可以想像成把一整疊文件分成幾疊小堆，

每一小堆都是獨立可處理的單位，

團隊成員可以各自處理不同堆互不干擾。



▋結構3. Column Chunk(欄位資料區塊)

在每個 Row Group 內部，

Parquet 會把相同欄位的值全部放在一起儲存，

這是「垂直切分」的概念，

也是 Parquet 最核心的設計。

**為什麼這樣快?** 

假設你有一張 50 個欄位的大表，

但查詢只需要「員工姓名」和「薪資」兩個欄位:

**Parquet 做法就是**只讀取「姓名」和「薪資」這兩個 Column Chunk，

完全跳過其他 48 個欄位。



▋結構4.**Page(資料頁)**

這是欄位內部最細的儲存單位，

也是**實際壓縮和編碼的最小單位**，

每個 Column Chunk 內部會切分成多個 Page。

**Page 的三大功能:**

**．壓縮**:每個 Page 可以選用最適合的壓縮演算法(Snappy、GZIP、LZO)。

**．編碼**:針對資料特性選用編碼方式(例如字典編碼、RLE 編碼)。

**．**記錄 min/max/null count **統計資訊**，讓查詢引擎可以快速判斷「這個 Page 有沒有我要找的資料」，決定要不要解壓。



Page 就像每個資料夾裡的「真空壓縮袋」，

裡面的資料被壓縮、編碼,並附帶標籤註明「袋內資料範圍:1-100」，

查詢引擎看到標籤就知道要不要拆開這袋，

避免無效的解壓作業。



▋結構4. **Footer(底部說明書)**

就像包裹底部的目錄清單，標示出:

．所有 Row Group 的位置和大小

．每個 Column Chunk 的位置和統計資訊

．Schema 定義(欄位名稱、型別、巢狀結構)

．檔案層級的 metadata

 **Footer 在檔案結尾是**因為，

寫入時無法預知最終檔案大小和統計資訊，

所以 Parquet 採用「先寫資料、最後寫目錄」的設計，

讀取時，查詢引擎會先跳到檔案結尾讀 Footer，

建立完整的索引地圖，

再根據需求跳到特定位置讀取資料。

---





▋Parquet 的四大特性

透過以上結構的說明，

應該可以比較清楚知道，

為什麼 Parquet 有以下四大特性：



▋**1\. 自描述的 Metadata(Self-describing)**

每個檔案都附帶自己的說明書,記載欄位名稱、型別、統計資訊、壓縮方式等。這代表:

- **無需外部 schema 定義**:即使沒有額外的 DDL 或文件,系統也能自動解析檔案結構。

- **自動化處理更方便**:ETL 流程可以自動識別欄位變化,減少人工介入。



▋**2\. 進階壓縮(Advanced compression)**

Parquet 針對每個欄位選用最適合的壓縮演算法:

- **數值型欄位**:使用 Delta Encoding + Bit Packing,壓縮率極高。

- **字串型欄位**:使用 Dictionary Encoding(字典編碼),把重複的字串只存一次。

- **通用壓縮**:Snappy(快速)、GZIP(高壓縮率)、LZO 等可選。

**實際效果**:平均能壓縮到 CSV 的 **10-25% 體積**,大幅減少儲存成本與 I/O 時間。



▋**3\. Schema Evolution(格式演進)**

當需要在資料中新增或移除欄位時,Parquet 可以向後相容:

**實例說明:**

- 你的包裹原本只有「姓名、地址」兩個欄位

- 之後你想加上「電話號碼」欄位

- Parquet 可以讓**舊包裹依然能被正確解讀**(缺失的欄位自動填 null),**新包裹自動包含新欄位**,不會因為格式改變導致所有舊資料失效

這對持續更新的資料湖(Data Lake)尤其重要,避免因 schema 變動導致歷史資料無法讀取。



▋**4\. 巢狀資料支援(Nested data support)**

Parquet 基於 Google Dremel 的論文,能處理像 JSON 一樣的階層結構:

- 支援 `STRUCT`(巢狀物件)

- 支援 `ARRAY`(陣列/列表)

- 支援 `MAP`(鍵值對)

這讓 Parquet 非常適合記錄複雜的事件資料、物件關聯、或多層級的業務邏輯,不需要像關聯式資料庫那樣強制正規化。

---

—

用工程師的語言來說，

Parquet 是一種「壓縮 + 欄式存儲 + 自描述」的二進位資料格式，

它不是單純的檔案，而是一個能夠:

**．自帶說明**(Footer metadata)

**．按欄壓縮**(Column Chunk)

**．分塊讀取**(Row Group + Page)

**．智慧跳過無關資料**(統計資訊 + Predicate Pushdown)的**智慧資料包**。

這種設計讓資料分析、ETL、機器學習流程都能更快、更節省資源,也難怪它成為現代**數據湖(Data Lake)和Lakehouse**架構的標準基石,被 Spark、Hive、Presto、Snowflake、Databricks 等主流平台廣泛採用。





▋附件1：進入技術前的引言

Parquet 是一種欄式二進位儲存格式，

以「檔尾索引 + 分段壓縮」達到高效讀寫，

每個檔案僅有一個 Header 與 Footer，

中間包含多個 Row Group，

每個 Row Group 內又依欄位分成多個 Column Chunk，

再細分為壓縮後的 Page。

Footer 記錄所有 Row Group 與欄位的位址、大小、壓縮方式及統計資訊，

使系統能直接跳讀需要的資料區段，而非解整個檔案。

這種結構讓 Parquet 可在單一檔案中混用不同壓縮算法，

同時支援條件篩選與欄位選讀，

是資料湖中高效、可擴充的核心格式。



關鍵知識名詞清單：

．Columnar Storage（欄式儲存）

．Predicate Pushdown

．Compression Codec（Snappy、GZIP、LZO、ZSTD）

．Encoding（RLE、Dictionary、Bit Packing）

．Schema Evolution

．Offset / Byte Range

．Thrift Serialization

．File Magic Bytes ("PAR1")

．Parallel Read / Split Read

．Vectorized Reader

．Bloom Filter (optional)

---