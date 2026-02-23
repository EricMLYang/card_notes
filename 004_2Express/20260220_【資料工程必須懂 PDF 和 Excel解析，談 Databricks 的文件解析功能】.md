---
tags:
  - my-article
Checkbox 1: true
---
【資料工程必須懂 PDF 和 Excel解析，談 Databricks 的文件解析功能】



近期公司積極導入 AI Agent，

但初期的文件解析往往是最麻煩的第一步，

看到一篇 Databricks 文章(連結放留言)

PDFs to Production: Announcing state-of-the-art document intelligence on Databricks

簡單分享，



▋非結構化數據處理需求大增

過去非結構化資料很難直接產生價值，

但 AI 改變了這件事，

現在透過向量化、語義搜尋、RAG 或 AI Agent，

資料可以參與決策流程、回答問題、生成洞察，

讓非結構化數據能透過系統產生價值變大了。

---

▋**新的技能需求**

資料工程師現在要懂的不只是 ETL 和 Schema 設計，

要知道怎麼切 Chunk 比較適合應用場景，

要管理向量 DB，

理解 embedding 模型的選擇與索引策略，

還要要設計搜尋流程，

平衡召回率與相關性。

但這一切的基礎，

回到最根本的問題:

要怎麼把文件內容解析成電腦容易處理的格式。

---

▋**解析的本質挑戰**

文件本質上是為了人互動而存在的，

PDF 有複雜的排版、多欄位、表格跨頁，

Excel 有合併儲存格、巢狀公式、隱藏工作表，

圖片裡可能有手寫註記、圖表、掃描的表格，

人類閱讀時可以理解語境、推測意圖、跳過不重要的部分，

但電腦需要明確的結構，

如果解析階段沒做好，

後面再怎麼調整 prompt 或優化向量搜尋都是事倍功半，

資料品質永遠是 AI 應用的瓶頸。

---

▋**Databricks 的角色**

去年記得 Databricks Summit 就提到 RAG 還有好多事可做，

像是文件解析進步空間還很大，

沒想到今年就出新功能，

這篇文章提到  Databricks 對複雜與非結構化資料的支援能力，

Databricks 在這方面的能力大致分成三類。

---

▋**第一類:結構化與半結構化文件**

Excel 檔案現在可以直接讀取，

Databricks 原生支援 .xls 與 .xlsx，

包含多工作表、自動欄位型別推斷，

以及指定儲存格範圍，

這讓 Excel 可以直接變成可查詢的表格資料，

也能透過 ETL 匯入 Delta Table，

對仍大量使用 Excel 的組織來說，

降低了不少轉換成本，

實務上要注意的是，

複雜的巢狀結構或自訂格式可能還是需要額外處理。

---

▋**第二類:PDF 與混合格式文件**

Databricks 新推出的 `ai_parse_document` preview函數，

可以處理複雜 PDF，

它支援解析文字、表格、圖片、圖表與版面資訊，

並輸出成結構化資料，

過去這類文件需要 OCR 工具或自定義解析流程，

解析品質也難保證，

現在用一個 SQL 函數就能處理，

然後直接進入 Delta Lake、Unity Catalog 或 downstream 的 AI 應用，

不過要留意幾點。

1\.preview 功能，效能、穩定性、定價都還在調整，建議先驗證。

2\.多模態模型解析的成本通常比傳統 ETL 高，文件量要估算。

3\.解析品質仍受原始文件影響，需要實測。

---

▋**第三類:更廣泛的非結構化資料**

對掃描圖片、Office 文件、混合內容或客製化文件流程，

Databricks 採用與第三方工具整合的方式，

例如 Unstructured 可以處理 60+ 種文件格式，

將結果整理成帶有 metadata 的文本或表格，

方便後續做向量搜尋、RAG，

或 AI Agent 的知識庫建置，

當企業文件來源非常多樣化，

這比自行維護 OCR 或 Parsing 程式碼更穩定，

但整合時要確認連接方式和授權成本。

---

▋**實務考量**

這些工具大幅改善了文件處理能力，

但不是完美解決所有挑戰，

如果文件涉及敏感資訊，

要注意 AI 解析過程中的隱私與合規要求，

特別是資料傳輸與儲存位置，

大量文件處理時，

建議監控 DBU 消耗與 AI 功能的計費，

避免成本超出預期，

對照 AWS Textract、Azure Document Intelligence 等服務，

Databricks 的優勢在於與 Lakehouse 生態整合更緊密，

不用在多個平台間搬運資料，

劣勢是目前部分功能還在 preview，

成熟度可能不如雲端廠商的專用服務。

---

▋**小結**

整體來看，

Databricks 在文件解析的能力正在快速成熟。

Excel 可直接讀取，

PDF 可用多模態模型解析，

更複雜的來源也能透過合作工具標準化後放入 Lakehouse，

對需要將資料來源統一導入平台，

並希望讓 AI 能處理文件內容的團隊而言，

這些能力補上了「資料在文件裡但無法用」的斷層，

如果你的資料平台或 AI 專案需要處理大量 PDF 或 Office 文件，

這些工具值得列入技術選項，

但建議先評估具體需求，

做好成本估算，

並透過小規模測試確認可行性。



<https://www.databricks.com/blog/pdfs-production-announcing-state-art-document-intelligence-databricks?utm_source=chatgpt.com>


