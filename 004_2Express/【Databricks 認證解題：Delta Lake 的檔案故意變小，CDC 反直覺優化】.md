---
tags:
  - my-article
Checkbox 1: true
---
【Databricks 認證解題：Delta Lake 的檔案故意變小，CDC 反直覺優化】



跟同事輪流讀題目，

在 Daily 時說明給大家聽，這次又輪到我了，

分享其中一題：



▋ 題目

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



▋ 場景設定

想像你有一張 10TB 的 Delta Table，透過 CDC (Change Data Capture) 持續接收增量更新。你很認真地：

．初始遷移時執行了 OPTIMIZE，把檔案整理成標準的 1GB

．開啟了 Auto Optimize 和 Auto Compaction

．用 Structured Streaming 維持 always-on 的更新

理論上，這張表應該維持在健康的大檔案狀態。

但過了一段時間，你發現**檔案竟然都變成 64MB 以下**。



▋ 第一反應：是不是哪裡壞了？

我一開始也這樣想。畢竟我們都知道：

．OPTIMIZE 的目標是 1GB

．Auto Compaction 預設是 128MB

．Small files 通常代表效能問題

但這次不一樣。



▋ 真相：Databricks 在幫你省成本

答案藏在一個關鍵字：MERGE。

CDC 工作負載的特性是什麼？頻繁的 UPDATE、DELETE、INSERT。在 Delta Lake 的 Copy-on-Write 機制下，要修改一筆資料，就得**重寫整個包含這筆資料的檔案**。

算一下這個成本：

．如果檔案是 1GB，改一筆資料要重寫 1GB

．如果檔案是 64MB，改一筆資料只要重寫 64MB

這就是所謂的 **Write Amplification（寫入放大）**。

Databricks 偵測到這個模式後，會自動將目標檔案大小**調小**，犧牲一點讀取效能（檔案較碎），換取大幅提升的合併效能。



▋ 這改變了我什麼想法

效能優化是取捨。

以前我總覺得「檔案越大越好」、「小檔案就是問題」。但在 CDC 場景下，小檔案反而是正確的策略。

這也提醒我在設計資料架構時：

．不要死守 best practice

．理解工作負載的特性

．讓系統根據實際使用模式動態調整



▋ 給資料工程師的建議

如果你的 Delta Table 是：

．讀多寫少：OPTIMIZE 到 1GB，減少檔案數量

．頻繁 MERGE：接受較小的檔案大小（64MB 甚至更小）

．大量 Append：Auto Compaction 的 128MB 通常剛好

記住：Small files are better for writes, Large files are better for reads。

最好的優化，是理解你的資料在做什麼，然後讓系統適應它。

---




