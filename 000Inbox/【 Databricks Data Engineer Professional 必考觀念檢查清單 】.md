【 Databricks Data Engineer Professional 必考觀念檢查清單 】



要配合公司政策考 Databricks 證照，

( Data Engineer Professional )

因為平常工作還兼 PM … 等各種協調工作，

要在 1月底前考到這張較深入的證照有點挑戰，

因此先從彙考題彙整觀念清單跟同仁分享，

讓備考的效益可以高一點，

這份清單可以邊讀邊確認幾個觀念有準備到，

下面依照考試七大領域整理，

每一點 ＝ 觀念名詞＋一句解釋＋準備重點。

---



▋一、核心開發與轉換（32%）

1\.MERGE INTO: 在 Delta 表做行級 upsert／update 的宣告式寫法。

重點：搞懂 WHEN MATCHED / WHEN NOT MATCHED 行為，特別是只有 NOT MATCHED 時，舊資料會被「忽略不更新」；知道為何 Bronze 不做 MERGE、Silver 才做。



2\.Change Data Feed（CDF）:Delta 內建的行級變更紀錄，可讀出 insert/update/delete。

重點：知道什麼情境要用 CDF（例如只對最近 24 小時變更做推論），以及時間戳過濾 vs CDF 的差異與限制。



3\.SCD Type 2: 解保留歷史版本的維度表：舊紀錄標記失效，新紀錄插入。

重點：會看懂並手寫一段簡單 SQL（UNION ALL + current flag + 生效時間），分得清 Type 1 / 2 / 3。



4\.Structured Streaming：Window + Watermark + State: 用事件時間視窗聚合，配合水位線清掉舊狀態，避免 OOM。

重點：翻滾視窗 vs 滑動視窗用途、withWatermark 做什麼；能說出為什麼「不設水位線」會爆狀態。



5\.Stream-Static Join 行為: 流資料每個 micro-batch 會用「當下最新版本的靜態表」做 join。

重點：懂得用這個做維度豐富化，並知道靜態表更新後新資料會自動套用。



6\.Streaming Checkpoint 目錄: 每條 Structured Streaming 查詢必須有自己的 checkpoint

重點：能說出「兩個 stream 寫同一個 Delta 表可以，但 checkpoint 不能共用，否則 offset 會亂」。



7\.Notebook 語言作用域（Python vs SQL）: Python cell 裡的變數不能直接在 SQL cell 用

重點：知道要用 Temp View、Widget 或先寫成表，再讓 SQL 存取。



8\.CTAS（Create Table As Select）: 一次性把查詢結果存成「靜態表快照」，之後不會自動更新。

重點：清楚分辨 CTAS vs View

---



▋二、維運與自動化（20%）

1\.Jobs API：/create vs /update: jobs/create 只會「新增」Job，不會覆寫既有設定。

重點：CICD 腳本必須先查詢是否存在，再用 update/reset，而不是一律 create。



2\.流式作業標準 Job 配置: Job Cluster + 無限重試 + Max Concurrent Runs = 1。

重點：知道為什麼要限制同一時間只有一個執行個體（順序性、避免重複處理）。



3\.單元測試 vs 整合測試: Unit Test 測細節（UDF、單一步驟），Integration Test 測整條管線

重點：要有「數據管線也是軟體」的概念，能說出各自的價值



4\.Spark 錯誤類型（分析階段 vs 執行階段): 像 cannot resolve ‘col’ 這種是 Catalyst 分析錯誤，不是 runtime。

重點：由錯誤訊息判斷是 schema 問題、語法問題，還是執行資源問題。



5\.SQL Alert 評估方式: Alert 是對查詢結果的每一行檢查，只要有一行符合條件就觸發。

重點：看得懂「group by + 聚合」情境下，Alert 代表的是哪一個 group 出問題。

---



▋三、安全與治理（17%）

1\.DELETE + VACUUM: DELETE 只刪「邏輯」，VACUUM 才會從儲存上物理移除舊檔案

重點：能說出合規場景（GDPR/CCPA）為何要搭配 VACUUM，以及失去 time travel 的取捨。



2\.ACL 權限：Can Attach / Can Restart / Can Manage: 要啟動已存在的 cluster，至少需要 Can Restart。

重點：熟悉最小權限原則：不要隨便給 Can Manage。



3\.Secrets Redaction 行為: print secret 會被遮蔽，但實際用來連線時仍是明文。

重點：知道 redaction 是保護 log，不是防一切攻擊；Notebook 執行權限還是關鍵。

4\.Dynamic View（動態視圖做欄位遮蔽）: 透過 CASE WHEN is_member(‘role’) THEN email ELSE ‘REDACTED’ 在查詢時決定能不能看敏感欄位。

重點：列級／欄位級安全要怎麼用 View 實現。



5\.Managed Table vs External Table：明確指定 LOCATION 才會是 External Table，否則預設是 Managed。

重點：知道這對資料存放位置、刪表時是否刪檔案的影響。

---



▋四、成本與效能優化（13%）

1\.Auto Compaction 與 OPTIMIZE：Auto Compaction 的目標檔案大小通常是 128MB 到 1GB 之間，具體取決於配置。預設行為會嘗試產生接近最佳大小的檔案，而不是固定 128MB。OPTIMIZE 預設目標約 1GB」，但實際上會根據表的配置和資料特性動態調整

重點：知道哪種適合流式寫入（小檔多）、哪種適合定期維護大表。



2\.小檔案與 Write Amplification：頻繁 MERGE 會造成目標檔案被切小，寫入放大。

重點：懂得配合合理檔案大小、調整 MERGE 策略。



3\.Data Skipping 與 Z-Order：Delta 利用每檔案 min/max 做檔案跳過，高基數文字欄位幾乎沒幫助。

重點：知道什麼欄位適合做 Z-Order，什麼欄位不適合。



4\.Driver 瓶頸偵測：CPU 使用率低、網路 I/O 低，但 job 很慢，常是 Driver 在卡（collect()、Python 邏輯）。

重點：會判斷問題在 Driver 還是在 Executor。



5\.Data Skew 特徵：某些 task 執行時間遠大於其他（max 是 median 的數十倍）。

重點：能說出常見解法：salting key、啟用 AQE skew join。



6\.寬轉換的叢集規格選擇：同樣總資源下，少台大機器通常比多台小機器更適合大量 shuffle。

重點：知道原因在於減少跨節點網路傳輸。



7\.Trigger.Once / AvailableNow：把流量「批次化」，用批次高吞吐來消化高峰期堆積。

重點：會在延遲太高時，想到透過 Trigger 設定來緩解。



補充 8. Photon:  Databricks 的向量化執行引擎，對某些工作負載可以大幅提升效能。

補充 9.Liquid Clustering：新的替代 Z-Order 的方案，自動管理叢集欄位。

---



▋五、數據攝取（7%）

1\.dropDuplicates 的限制：只對當前 DataFrame 去重，不會看目標表裡的舊資料。

重點：要做真正冪等攝取，必須用 MERGE 或先比對 key。



2\.Auto Loader：雲端目錄自動監聽，支援 schema 推進與 checkpoint 管理。

重點：知道什麼情境比「手動 list files」更穩、容錯更好。



3\.CDF 作為增量攝取依據：相較檔名或時間戳，CDF 能包含更新與刪除。

重點：會選對場景（例如 ML 推論只跑變更部分）。



4\.%sh 在 Driver 上執行：使用 %sh 操作大量檔案無法用到叢集平行度。

重點：大檔案搬移／處理應改用 Spark API 或 dbutils.fs。

---



▋六、數據建模（6%）

1\.Medallion Architecture（Bronze / Silver / Gold）：Bronze 保留完整原始；Silver 去重、清洗、整合；Gold 專門給報表／業務分析。

重點：Bronze 多為 append-only，發生下游問題可從 Bronze 重播。



2\.Schema Inference vs Explicit Schema：推斷綱要容易被抽樣誤導，生產環境應明確定義。

重點：知道在哪些 ingestion 場景要硬性指定 schema。



3\.SCD Type 1 / 2 / 3 模式: 解釋：Type 2 最常考：保留歷史版本、用欄位或日期控制是否為 current。

重點：可以用白話說出三種差別與適用情境。



4\.View 當作 Schema Adapter：透過 View 隱藏實體表欄位調整、重命名，讓下游不用改。

重點：理解 rename Managed Delta Table 只改 Metastore，不搬動實體檔案。

---



▋七、數據共享與報表（5%）



1\.預先計算 Gold Table：高併發儀表板用預算好的 Gold 表，而不是每次即時跑複雜 View

重點：能說出這樣做對效能、成本與穩定性的好處。



2\.Notebook 語言間共享結果方式: 解釋：Python / SQL 要共享資料，應透過表或 View，而不是直接傳變數。

重點：想到「Metastore 當交換介面」這個心智模型。

---



▋最後衝刺 10 題自我檢查（考前 30 秒）：

1\.我能不能清楚講出 MERGE 的每個分支在做什麼？

2\.我知道 CDF 在哪幾種「只對變更資料」的場景一定要用嗎？

3\.我能畫出 Window + Watermark + State 的心智圖嗎？

4\.我會解釋為什麼 streaming checkpoint 不能共用嗎？

5\.我知道 DELETE + VACUUM 在合規上的關係嗎？

6\.我會用 Dynamic View 做欄位遮蔽嗎？

7\.我能說出 Auto Compaction vs OPTIMIZE 的差異與用途嗎？

8\.我看得懂 Data Skew 長什麼樣子、怎麼拆嗎？

9\.我知道 dropDuplicates 為什麼不等於冪等 ingestion 嗎？

10\.我能用一句話講清楚 Bronze / Silver / Gold 各自的責任嗎？





如果上面這 35 個點你都能用自己的話講出來，

這張證照的技術深度，已經到位了。


