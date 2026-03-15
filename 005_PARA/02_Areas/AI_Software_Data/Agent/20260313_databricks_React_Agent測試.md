在 Databricks 上跑 AI Agent 分析資料，一些過程紀錄

晚上睡前空檔，想說試一下 PydanticAI，
想讓 Agent 自己去分析 Delta Table，不用每次手動寫查詢。

快速簡單測試最精簡版本
能跑之後，第一個直覺是把資料拉成 pandas 丟給 Agent。能動，但根本就錯了。toPandas() 把全部資料從 Worker 拉進 Driver 記憶體，資料一大就 OOM，而且 Agent 用 pandas 在跑 groupby，跟 Spark 完全沒關係了。等於搭了整個叢集，只用單機。


正確的做法：聚合在 Spark，Agent 只看摘要
原則：Tool 不回傳原始資料，只回傳聚合結果。運算留在 Spark 側，最後 limit 幾十列再 toPandas()。Agent 看到的永遠是摘要，不是原始資料列。這樣 Spark 的分散式效率才真的有用上。

讓 Agent 自己判斷要撈多久
我的場景是每天跑一次報告，但資料 pipeline 有時候會延遲，最新資料可能是三天前的。
原本日期寫死 days=7，Agent 根本不知道資料有多新，報告很容易失真。
改成給 Agent 一個工具先查資料的時間範圍，讓它自己決定要撈哪段。判斷邏輯寫在 system prompt 裡——資料延遲幾天就往前擴幾天，超過兩週就在報告裡標注異常。這樣 Agent 對資料環境有感知，不是盲目執行。

最終想做到的
現在這個架構，Agent 有幾個固定 Tool，跑完一輪輸出報告。但我真正想要的是一個完整的 Agentic Loop：規劃、執行、觀察，不斷迭代，直到它自己認為任務完成。

PydanticAI 本身就支援這個迴圈。我缺的不是框架，是工具的廣度。

Databricks 上可以整合的端點其實很多：Spark Functions、Genie API、Unity Catalog Functions、MLflow Model Serving、外部微服務。

把這些都包成 Tool，Agent 就可以自己規劃推理鏈——發現某台攝影機沒資料，去查設備狀態，確認是 pipeline 斷掉還是機台問題，最後給有根據的結論。這條鏈不需要我寫死。

架構還在調整，Tool 的粒度和 system prompt 怎麼寫都還在摸。

希望後續研究完的東西，萃取出比較適合產品化的，可以放到我們解決方案上．
