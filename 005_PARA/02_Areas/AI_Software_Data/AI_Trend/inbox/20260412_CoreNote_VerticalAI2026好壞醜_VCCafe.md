---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
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

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：作者用 Good / Bad / Ugly 三段式拆解 vertical AI 在 2026 的實況。Good 段呼應 Menlo（人力預算 vs IT 預算、workflow embedding 護城河）；Bad / Ugly 段是核心訊號：(a) legacy backend 把 agent 高頻呼叫當 DDoS、(b) 61% 公司缺 AI governance、(c) 螢幕停留時間死亡、outcome-based pricing 取代 per-seat、(d) thin wrapper 商品化、CIO 削減實驗集中贏家。
- 作者挑戰的預設：「vertical AI 只要模型強 + UI 好就能賣訂閱」 → 真實阻力在底層 infrastructure / governance / pricing model 與創辦人服務含量。
- 個人映射：直接補強 Menlo 樂觀論述的下半身。對 Eric 兩條主線特別有用：(1) DecisionOps / 上線責任 —— infrastructure mismatch 與 governance 缺口正好是 D2D Architect 的服務切入點；(2) 接案 / 服務包裝 —— forward-deployed engineering 與 outcome-based pricing 對應 Eric 「三層服務漏斗（診斷→藍圖→導入）」的論述。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent 速度撞上 legacy backend 的 DDoS 化失敗模式
- 分級：Core
- 類型：Warning
- 核心內容：為人類 workflow 設計的企業 backend（rate limit、connection pool、auth flow、audit log）在 agent 速度下會崩潰 —— 毫秒內 5,000+ 遞迴 sub-task 被 WAF / API gateway 當成 DDoS 攻擊擋下來。這個 gap 不是模型能力問題，而是「執行頻率假設」的不對齊。Demo 過得了是因為單發呼叫，上線崩潰是因為 agent loop 把 QPS 拉高 3–4 個量級。
- 保留理由：具體、可驗證、跟 Eric AWS / 上線責任主線完全對齊；是「demo 過了上線崩潰」的高品質具體痛點。
- 待補強處：實際 case 的 QPS 倍數、哪一層先崩（API gateway / DB connection / downstream service）？緩解策略（rate-aware agent、async queue、bulkhead pattern）的取捨？
- 初步知識鉤子：[[AI 上線責任邊界]]、AWS Shared Responsibility、harness 設計、observability、rate limiting 模式、DDoS vs legitimate traffic 辨識

序號 2
- 候選標題：Engagement Metric 已死 —— vertical AI 成功訊號是「使用者花更少時間」
- 分級：Core
- 類型：Principle
- 核心內容：DAU、停留時間、session length 這些 SaaS 時代的成功指標，在 vertical AI 上會給出反向訊號。醫師自動化臨床筆記的成功標誌是「螢幕時間下降」、律師用 Legora 的成功是「同案件耗時下降」。這推翻了 PM 圈的預設儀表板，必須改用 outcome-based metric（per document、per resolution、per case closed）。對 product 團隊，這代表 dashboard 設計、北極星指標、A/B test 評估標準都要重新設計。
- 保留理由：強反共識、可遷移到所有 vertical AI 產品設計、直接挑戰 PM 圈既有指標心智。
- 待補強處：哪些 vertical 仍適合用 engagement 指標（如教育、學習類）？outcome 指標的歸因難題如何解？
- 初步知識鉤子：Business Data Science / 指標治理、北極星指標、SaaS metrics 反例、John Cutler 的產品指標反思

序號 3
- 候選標題：Outcome-based pricing 取代 per-seat SaaS 的結構壓力
- 分級：Core
- 類型：Pattern
- 核心內容：當「使用者花更少時間 = 成功」，per-seat 訂閱模型在邏輯上自我矛盾 —— 客戶用得越好越想砍 seat。所以 vertical AI 的定價會被結構性推向 per-document / per-resolution / per-case 的 outcome-based pricing，或 hybrid（基礎訂閱穩定 + 用量 tier）。這同時改寫了 forecast、CAC payback、cohort 分析、毛利結構，以及銷售流程要 sell ROI 而不是 sell user count。
- 保留理由：這是商業模型層級的轉變，影響整條 GTM 設計；與 Eric「AI 成本結構與定價經濟學」主題對齊。
- 待補強處：outcome 計量的爭議與審計（誰算對、誰賠錯）？hybrid 模型的訂閱 / 用量比例怎麼定？
- 初步知識鉤子：AI 定價經濟學、訂閱統計賭局、Cedric Chin 取捨邏輯、SaaS unit economics、合約設計

序號 4
- 候選標題：Forward-Deployed Engineering 是 vertical AI 的隱性必要條件
- 分級：Core
- 類型：Heuristic
- 核心內容：Vertical AI 落地需要創辦團隊「賣 implementation service，不只是賣軟體」 —— 派工程師到客戶現場做整合、調 prompt、接資料源、做 governance。這不是 Palantir 獨有現象，而是垂直 AI 的結構性必要條件，因為 unstructured workflow 與 governance gap 無法用標準軟體交付。對 solo consultant / fractional executive 而言，這個事實正當化了「服務含量 + 軟體含量」的混合包裝。
- 保留理由：直接對應 Eric 的「三層服務漏斗」與接案路線；可成為對抗「我做的是顧問不是產品」自我懷疑的論述。
- 待補強處：FDE 的成本對毛利率衝擊？什麼時候從 FDE 走向 self-serve？
- 初步知識鉤子：三層服務漏斗（診斷→藍圖→導入）、Palantir FDE 模型、solo consultant 服務包裝、毛利結構、Andy Grove 槓桿管理

序號 5
- 候選標題：61% 公司缺 AI governance 是 D2D / DecisionOps 的服務切入點
- 分級：Support
- 類型：Pattern
- 核心內容：61% 公司缺 AI governance 專業，導致 RAG / LLM 部署卡在 POC 階段，無法產生確定性結果。這不是「再加一個模型」能解的，需要的是 evaluation framework、guardrail 設計、權限邊界、auditability、failure recovery 的整套架構能力。這個 gap 對於走 D2D / DecisionOps 品牌的服務商，是相對乾淨的需求入口（買方知道自己缺，但不知道找誰）。
- 保留理由：把「市場數據」轉成「可入場的服務 wedge」；對應 Eric AWS 治理 / 上線責任主線。
- 待補強處：61% 數字的來源與可信度？AI governance 顧問市場已經有哪些競品？
- 初步知識鉤子：AWS Shared Responsibility、AI 治理框架、guardrail 設計、Chad Sanderson 數據契約、evaluation strategy

序號 6
- 候選標題：CIO 預算集中化擠壓「實驗預算」與 thin wrapper 新創
- 分級：Support
- 類型：Warning
- 核心內容：CIO 已從「廣撒 AI 實驗預算」轉為「集中在已驗證 ROI 的贏家」，加上 Google / Salesforce / Microsoft 用 land-and-expand 策略碾壓沒有 proprietary moat 的新創 —— 這意味著「demo 階段拿融資、之後再想 moat」的劇本失效。對於想做 vertical AI 的小團隊，必須在進入市場前就回答：proprietary data 從哪來、workflow embedding 多深、為什麼老牌玩家不會在 18 個月內推出同樣功能。
- 保留理由：直接補強 Menlo Clone Test 的市場側壓力來源。
- 待補強處：哪些 vertical 已經被老牌玩家吃下來、哪些還空著？land-and-expand 的真實成功率？
- 初步知識鉤子：[[Clone Test 判準]]、競品 mapping、CIO 採購心智、Crossing the Chasm

序號 7
- 候選標題：Progressive Delegation —— 高量低價值 workflow 先動，高風險決策保留人類
- 分級：Support
- 類型：Heuristic
- 核心內容：作者建議的創辦人路線圖第一條：先自動化「低價值 + 高量」的 workflow 切片（如資料 intake、分類、初步草稿），把「高風險決策」（核可、診斷、定價）保留給人類。這是個落地排序的判準 —— 不是「先做最酷的」也不是「先做最大的」，而是「先做最容易產生 outcome data 同時風險可控的」。對 Eric 在客戶現場做 Crux 診斷時，是個可平移的優先級規則。
- 保留理由：可遷移成 D2D Architect 落地排序框架。
- 待補強處：「低價值 vs 高風險」的二維 mapping 怎麼做？grey zone（中價值中風險）的處置？
- 初步知識鉤子：Crux 診斷、TOC 限制理論、人機判斷權歸屬、decision loop 漸進交棒

## C. 建議送 refine 的項目
- 1（DDoS 化）、2（engagement 死亡）、3（outcome pricing）、4（FDE）為核心 KEEP
- 5（governance gap）建議與其他文章的治理卡合併
- 6（CIO 集中化）建議轉為 warning 卡並與 Menlo Clone Test 對接
- 7（Progressive Delegation）若取捨原則夠強可獨立保留

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉，特別注意與 Menlo 文章 / Gartner DI 文章的鉤子串接，形成 Vertical AI / DecisionOps 主題群組。
