# Vertical AI in 2026: The Good, The Bad, and The Ugly — VC Cafe

> 來源：VC Cafe
> 來源類型：高密度觀點
> 需求層：知識建構
> 連結：https://www.vccafe.com/2026/01/07/vertical-ai-in-2026-the-good-the-bad-and-the-ugly/
> 搜集日期：2026-04-12
> 搜集原因：K2 — 垂直 AI 失敗模式與取捨（Menlo 文章的反面補充）

## 摘要
這篇用 The Good / The Bad / The Ugly 三段式拆解 vertical AI 在 2026 年的真實狀態。對 Eric 來說最有價值的不是 The Good（與 Menlo 相似），而是 The Bad 與 The Ugly：揭露了三個常被忽略的結構性問題 — 企業 backend 撐不住 agent 速度（5,000+ 遞迴 sub-task 被當成 DDoS）、61% 公司缺 AI governance 專業、按螢幕停留時間計算 ROI 已經死亡（醫師上線時間「下降」才是成功）。

## 為什麼值得看
這篇是 Menlo 樂觀論述的「現實主義 counterweight」，**特別適合 Eric 寫「為什麼 demo 過了，上線後系統崩潰」的失敗覆盤類文章**。三個直接可用的論點：
1. **Infrastructure mismatch**：legacy backend 把 agent 的高頻呼叫當成 DDoS 攻擊 — 這是極好的具體痛點
2. **Death of engagement metrics**：傳統 DAU / 停留時間已不是 vertical AI 的成功指標，要改用 outcome-based pricing（per document、per resolution）
3. **Forward-deployed engineering**：創辦人必須賣 implementation service，不只是賣軟體 — 跟 Eric 自己「三層服務漏斗」的論述高度一致

## 可能偏誤或限制
- 篇幅較短，案例介紹較表面
- 「Cursor 200-developer tracking problem」當例子時細節不足
- 沒有深入討論該如何解決 infrastructure mismatch（只指出問題）
- 對 outcome-based pricing 的實作機制著墨不深

## 潛在卡片方向
- 「企業 backend 撐不住 agent 速度」現象卡（與 Eric 談 Databricks/AWS 上線責任接得起來）
- 「Death of engagement metrics」卡：vertical AI 的成功指標反而是「使用者花更少時間」
- Outcome-based pricing 取代 per-seat SaaS 的論述卡
- Forward-deployed engineering 的角色卡（與 Eric 自己的服務包設計呼應）
- 可連結現有卡片：[[從 demo 到產品的距離]]、[[AI 上線責任邊界]]

---

## 全文翻譯（重點摘錄）

### THE GOOD

**人力預算機會（10x 市場）**
Vertical AI 競爭的是人力預算，不是 IT 支出。商業/專業服務佔美國 GDP 約 13% — 大約是軟體市場的 10 倍。這些工具不是取代工人，而是透過 co-pilot 增強能力。

**Workflow Integration 作為護城河**
單靠模型表現無法持久。贏家把自己嵌入成 system of record，透過深度 workflow 整合與「協作層」協調多 agent 工作。

**多模態擴張**
視覺系統解讀建築藍圖與工地照片，自動產生施工 scope-of-work。語音 agent 已能處理 inbound 銷售電話與病患 intake，無需人工介入。

### THE BAD

**Infrastructure Mismatch**
為人類 workflow 設計的企業 backend，在 agent 速度下崩潰（毫秒內 5,000+ 遞迴 sub-task）。Legacy 系統把這當成 DDoS 攻擊。

**Data Entropy 危機**
組織淹沒在 unstructured PDF、screenshot、log 中，可靠性瓶頸難解。**61% 的公司缺乏 AI governance 專業**，RAG/LLM 部署在 POC 階段卡住，無法產生確定性結果。

**人才短缺**
落地需要「forward-deployed engineering」— 創辦人必須賣 implementation service，不只是賣軟體。

### THE UGLY

**Thin Wrapper 商品化**
只是包裝 GPT 的融資新創會被淘汰。生存需要 end-to-end workflow 自動化加 proprietary data moat。

**Engagement Metric 之死**
螢幕停留時間不再衡量價值。醫師自動化臨床筆記，意味著螢幕時間「減少」— 那才是成功。創辦人必須採用 outcome-based pricing（per document、per resolution）取代 per-seat SaaS。

**廠商整併**
CIO 削減實驗預算，集中在已驗證 ROI 的贏家。Google、Salesforce 等老牌玩家用「land and expand」策略壓過為求採用而掙扎的新創。

### 點名的案例
- **贏家**：Abridge（臨床筆記）、Hebbia（提案簡報草稿）、Rilla（銷售教練）、Pandorian（AI 監督）
- **警示**：Cursor 的 200 developer tracking problem

### 創辦人路線圖
1. **Progressive Delegation**：自動化低價值高量的 workflow 切片，把高風險決策保留給人類
2. **Magical Feature Wedge**：交付 1000x 人類能力（資料分析）或自動化邊緣 workflow（法律研究）作為入口
3. **Multiplayer Architecture**：設計能跨組織邊界協作的 agent（買方、賣方、監管者）
4. **Outcome Pricing Hybrid**：把訂閱穩定性與按交付量計價的 usage tier 結合
