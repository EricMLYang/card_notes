---
tags:
  - my-article
Checkbox 1: true
---
【Databricks 正在放大「會用數據驅動決策」這群人的影響力】



記得今年初看到 Databricks 估值達 2 兆台幣新聞，

注意到了一個 Databricks CEO 訪談，

當時深覺這個人講話很有料，

撇除招募銷售主管那段，

印象最深刻的是以下幾句話，

「你企業的數據還是要先準備好才行，但大家只想趕快導入 AI 做 POC」

「不去做那些他們沒有數據優勢的 AI 項目」

「必須先把「無聊」的基礎工作做好——也就是**搞定數據策略」**

對比當時一窩蜂 AI 應用時期，

顯得比較穩健，

<https://youtu.be/oriIvbUwh2I?si=oBSZu_jguIqyXCRX>





但最近比較仔細看 Databricks AI 功能，

發現其實 Databricks 步乏相當快，

但身為一個對數據傳統分析有點著迷的人，

我覺得 Databricks 最近的 AI 佈局，

要我用一句話總結的話就是：

 Databricks 正在放大「會用數據驅動決策」這群人的影響力。



我自己覺得，它做的每一步，

本質上都在把「有判斷力的數據分析者」

推到更關鍵的位置，而不是被 AI 取代。



▋1. 從「寫 SQL」變成「把你的思路變運算單元」

AI Functions、ai_query 讓你在 SQL 裡直接叫 LLM：

．摘要、分類、情緒分析、文件解析，不用再求人建模型

．「分析邏輯」可寫成 prompt，變成可重用查詢模式



你的 domain know-how 被編進 pipeline，

變成整個團隊都能用的能力。

⸻



▋2. 從「做報表」變成「設計語意」

AI/BI + Genie、Unity Catalog 語意層：

同事可以用自然語言問問題，

背後用的是你定義好的維度、指標、商業名詞，

你把這些定義透過 Unity Catalog 的 Metrics 和 Dimensions，

變成 AI、BI、Agent 都必須遵守的語意規則，



也就是把腦中指標，抬升為平台可複用資產。

⸻



▋3. 從「一次性 insight」變成「長期運轉的 Agent / 系統」

Mosaic AI、Vector Search、RAG、Model Serving、Inference Tables：

原本在 Notebook 裡做的那條流程：

取數 → 清洗 → join → 分群/判斷 → 下結論

現在可以變成一個常駐的分析 Agent。

．同事用自然語言丟問題，它就用你設計好的步驟走一次，再把結果回寫表格

．透過 Inference Tables 儲存每次推論結果，接受持續評估與監控



現在分析方法本身變成一個「產品」，

可持續在組織裡運作、被評分、被優化

⸻



▋4. 從「敏感資料只能放著」到「敢用來驅動 AI」

Foundation Model APIs + DBRX + Unity Catalog 治理：

**．一般場景**：透過 Foundation Model APIs 直接使用託管模型（OpenAI、Anthropic、Meta、Cohere 等）

**．**高敏感場景：用開源的 DBRX 模型 + 私有 RAG，在自己控制的環境裡做分析

**．**治理框架：Unity Catalog 提供資料權限、血緣追蹤、稽核記錄



對分析者的關鍵差異：

．過去：真正有價值的文字（客服紀錄、維修單、合約備註）都不敢碰 AI

．現在：這些內容可以在治理框架下進入 LLM 流程，變成你決策分析的一部分

⸻



▋5. 從「做完就算了」到「追蹤這套 AI 真的有沒有價值」

Mosaic AI Evaluation & Monitoring：

把「這個 Agent 到底有沒有幫上忙？」變成可以量化的指標：

．準確度、成本、錯誤率

．決策品質提升（如工單處理時間、營收 lift）



不再只是被要求「上 AI」，而是可以反過來問：

．這套 AI 是否真的 outperform 原本人工流程？

．哪些場景該開、哪些該關？

你用來評估 A/B 測試、行銷活動的那套思維，現在用在評估 AI 本身。

⸻



▋6. 所有小東西加總起來：把你推向「語意與決策架構師」

Databricks Assistant 幫你 debug SQL、轉換語法、解釋錯誤，這些都是日常小加成。

真正大的變化，是整個平台設計在假設：



「懂數據、懂語意、懂業務的人」應該站在控制平面的中心。



所以：

．SQL + prompt → 變成你個人風格的「分析算子」

．Unity Catalog + Metrics → 變成你定義「這家公司怎麼看世界」的地方

．Mosaic AI + Agent → 變成你把方法論 productize 的管道

．Evaluation → 讓你以「真實表現」為標準，主導 AI 應用的生死

⸻



如果你本來就擅長用數據驅動決策， 

Databricks 這一輪 AI 佈局，

會把你腦中的那套分析直覺、語意結構與決策方法， 

放大成整個組織、甚至整個 AI 系統的「底層邏輯」。




