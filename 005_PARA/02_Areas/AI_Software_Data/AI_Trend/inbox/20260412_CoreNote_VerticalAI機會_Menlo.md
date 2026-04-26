---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
# Software Finally Gets to Work: The Opportunity in Vertical AI — Menlo Ventures

> 來源：Menlo Ventures（Perspective）
> 來源類型：高密度觀點 + 品牌與市場訊號
> 需求層：知識建構 + 品牌建構
> 連結：https://menlovc.com/perspective/software-finally-gets-to-work-the-opportunity-in-vertical-ai/
> 搜集日期：2026-04-12
> 搜集原因：K2 — 垂直 AI / Vertical SaaS 與資料護城河

## 摘要
Menlo 的核心論點：「Vertical SaaS 是 show 與 assist，Vertical AI 是 reason 與 execute」。這把 ROI 計算從 IT 預算搬到了人力預算 — 後者規模大上一個量級。文章用一組數字定錨這個新機會：Healthcare 一年花 $740B 在行政服務，IT 只花 $63B；高教行政支出 $240B。然後提出「Clone Test」與「Compounding Data Moats」兩個判斷框架，列出 8 家代表性 vertical AI 贏家案例。

## 為什麼值得看
這是 2026 年到目前為止最完整的 Vertical AI 投資論述，**直接對應 Eric「垂直領域新創如何把資料流做成決策流」的主線**。對 Eric 特別有用的三件事：
1. **Clone Test**：「如果今天把創辦團隊和程式碼用 frontier model 重現一次，他們為什麼不會贏過原版？」這是一個極好的判準，幾乎可以直接拿來寫一篇判準文。
2. **Defensive vs Generative Moats** 的二分法：合規護城河只能拖時間，accumulated data + workflow 才能持續加寬差距 — 對應 Eric 想談的「資料優勢 vs decision moat」。
3. **8 家具體案例**（Grow Therapy、Legora、CollegeVine、Eve、NationGraph、PermitFlow、Solace、Pace）每一個都可以拿來做匿名化案例對照。

## 可能偏誤或限制
- 創投視角，偏好「能融資、能擴張」的 archetype，可能低估 bootstrap / consultancy 路線的可行性
- 案例集中在美國 regulated verticals（healthcare、legal、education、financial services），台灣市場應用要打折
- 對「forward-deployed engineering」的成本與毛利結構著墨不足，容易讓讀者低估服務型團隊的負擔
- 沒有討論「Vertical AI 失敗模式」的深度（VC Cafe 那篇是更好的補充）

## 潛在卡片方向
- 「Clone Test」判準卡：判斷一個 AI 產品是否真有護城河
- Defensive vs Generative Moat 二分法卡
- ROI 從 IT 預算搬到人力預算的論述卡（可串到 [[從資料平台到決策系統]]）
- Workflow Embedding 四個特徵卡（高人力對 IT 比例、unstructured workflow、合規複雜度、forcing function）
- 可連結現有卡片：[[資料如何形成產品護城河]]、[[從 demo 到產品的距離]]

---

## 全文翻譯（重點摘錄）

### 核心論點
Menlo 主張 vertical AI 從根本上改變了軟體的角色 — 從「協助工作」變成「執行工作」。
> Vertical SaaS showed and assisted; vertical AI reasons and executes.

這把 ROI 計算從 IT 預算搬到了人力預算 — 在服務密集型產業中，後者的規模大得多。

機會存在於：受監管的垂直產業雇用大量行政人力，做的是判斷重、處理 unstructured data 的工作。
- Healthcare 一年花 **$740B** 在行政服務，IT 只花 **$63B**
- 高教行政支出達 **$240B**

這些不是軟體投資不足 — 而是上一代技術無法自動化的工作。

### 防禦性框架：四個支柱

**Compounding Data Moats**：價值透過使用而複利。Menlo 區分「防禦性護城河」（合規要求、合規基礎設施）只能拖延競爭者，與「累積性護城河」（累積資料、跨客戶訊號、workflow 擴張）會主動拉開差距。

**Clone Test**：「如果你今天用 frontier model 把創辦團隊和程式碼重現一次，為什麼他們不會贏過原版？」能撐過這個測試的公司，是因為累積的資料、operational learning、network effect 不可能快速複製。

**Workflow Embedding**：嵌入執行層的公司會累積讓 switching 變得結構性昂貴的 contextual knowledge。
- Pace 處理保險理賠文件分析，建立保險公司特定的機構知識
- Rogo 起草銀行 memo，學會該家券商特有的 deal 結構偏好

### 具體贏家
- **Grow Therapy**：吸收 intake、scheduling、保險認證，讓臨床醫師看更多病人不需加人
- **Legora**：處理過去按小時計費的法律研究與起草，律師可接更多案不需擴編
- **CollegeVine**：在大學部署 agents 處理招生、學生服務、成績單
- **Eve**：法律 intake 系統，學習案件特徵、預測勝訴可能
- **NationGraph**：跨 10 萬+ 政府單位 mapping 採購機會，學習中標訊號
- **PermitFlow**：累積建照資料庫與司法管轄區批准 workflow
- **Solace**：引導 20 萬+ 病患做 Medicare 決策，學會哪些 billing code 與申訴論述對特定保險方有效

### 目標 workflow 的四個特徵
1. **高 labor-to-IT 預算比**：預算集中在人力，不是軟體
2. **手動、unstructured workflow**：對 messy input（文件、對話、實體環境）下判斷
3. **法規/程序複雜度**：合規要求建立 durable moat，通用競爭者無法繞過
4. **Forcing function**：人力短缺、毛利壓力或法規變動製造急迫性

### 失敗模式
- **Routine task automation 不會複利**：規則型任務（狀態檢查、預約提醒）累積不到 domain-specific 資訊
- **單一護城河脆弱**：只有 defensive 或只有 generative 的公司，會在續約時退讓
- **法規地形重要**：「技術會推平既有地景」，但 regulated verticals 會抵抗 — HIPAA、FDA、professional liability 是結構性的，無法用技術繞過
- **第一波 overhead 陷阱**：早期 vertical 軟體常常「加上的 overhead 跟移除的一樣多 — 新介面、新 workflow、新人力管理工具」

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Menlo 主張 vertical AI 改變了軟體角色 —— 從 show / assist 變成 reason / execute。這把 ROI 從 IT 預算（$63B healthcare）搬到人力預算（$740B healthcare），市場規模差一個量級。判斷護城河用 Clone Test、區分 defensive / generative moat，並列出 4 個 workflow 特徵與 4 個失敗模式。
- 作者挑戰的預設：「軟體只是讓人類工作更有效率」與「合規護城河 = 真護城河」 → vertical AI 是替代部分人力（不是助理），合規只是時間護城河，真正的護城河是累積資料 + workflow embedding。
- 個人映射：直接定義 Eric「垂直領域新創 + data product」主線的論述基準。Clone Test 是極好的判準（可拆出獨立判準卡），Defensive vs Generative 二分法直接對應「資料優勢 vs decision moat」，4 個 workflow 特徵可成為客戶機會評估的 checklist。創投視角偏好可融資擴張型，可能低估 bootstrap / consultancy 路線 —— 這個 bias 要在卡片中明確標註。

## B. 候選卡（Lite）

序號 1
- 候選標題：Vertical AI 的 ROI 從 IT 預算搬到人力預算，市場規模差一個量級
- 分級：Core
- 類型：Principle
- 核心內容：Vertical SaaS 賣的是「讓員工更有效率」，計算 ROI 看 IT 預算（healthcare 一年 $63B）；vertical AI 賣的是「替代部分人力工作」，計算 ROI 看人力預算（healthcare 行政 $740B、高教行政 $240B）。這個切換的後果是 pricing power、銷售敘事、買家身份（CFO / COO 而不只是 CIO）、合約結構全部改寫。對 PM / 創辦人，這意味著市場 sizing 的標的從 SaaS spend 換成 labor spend。
- 保留理由：機制清楚、數字具體、推翻 SaaS 時代的市場 sizing 方法。
- 待補強處：哪些 vertical 不適用這個切換（人力本來就薄但 IT 厚的產業）？labor spend 的可被 AI 替代比例怎麼估？
- 初步知識鉤子：[[從資料平台到決策系統]]、TAM / SAM / SOM 重估、買方身份遷移、AI 定價經濟學、Vertical SaaS vs Vertical AI

序號 2
- 候選標題：Clone Test —— 判斷 vertical AI 是否真有護城河的單句判準
- 分級：Core
- 類型：Heuristic
- 核心內容：問一句話：「如果今天用 frontier model 把創辦團隊和程式碼重現一次，他們為什麼不會贏過原版？」能撐過這個測試的公司，靠的不是程式碼也不是模型，而是無法被快速複製的累積資料、operational learning、跨客戶 network effect、客戶端的 workflow contextual knowledge。這個 test 同時可以套在自己的服務 / 產品 / 內容 —— 如果一個 frontier model + 一個新人就能複製你做的事，你就沒有累積護城河。
- 保留理由：原子化、可重複套用、可遷移到自己對自己的判斷、極佳的內容鉤子。
- 待補強處：通過 Clone Test 的最低累積時間？什麼類型的累積（資料量 vs workflow 深度 vs network）最難複製？
- 初步知識鉤子：[[資料如何形成產品護城河]]、Compounding moat、個人品牌的 Clone Test、defensibility 評估

序號 3
- 候選標題：Defensive Moat 與 Generative Moat 的本質差異
- 分級：Core
- 類型：Principle
- 核心內容：Defensive moat（合規認證、合規基礎設施、licensure）只能拖延競爭者進場時間 —— 它是時間護城河，不會自己變寬。Generative moat（累積資料、跨客戶訊號、workflow 擴張）會主動拉開差距 —— 用得越多越深、越不可複製。兩者組合才穩固：只有 defensive 的公司會在續約時退讓（因為價值不增長），只有 generative 的公司會在合規地震時被掃出場（因為沒有牌照緩衝）。
- 保留理由：把「護城河」這個過度使用的詞拆出可操作的二分法。
- 待補強處：什麼產業可以只靠 generative（無重監管）？兩種 moat 的投資成本與回收速度差異？
- 初步知識鉤子：[[Clone Test 判準]]、合規認證 vs 持續學習、Andrew Chen network effect、產品護城河類型學

序號 4
- 候選標題：Workflow Embedding 的 4 個目標特徵 checklist
- 分級：Core
- 類型：Heuristic
- 核心內容：Menlo 給出 vertical AI 該瞄準的 workflow 4 個特徵：(1) 高 labor-to-IT 預算比（預算在人不在軟體）、(2) 手動 unstructured workflow（要對 messy 文件 / 對話 / 實體環境下判斷）、(3) 法規 / 程序複雜度（合規門檻成為 durable moat）、(4) Forcing function（人力短缺、毛利壓力或法規變動製造急迫性）。這 4 點不是並列描述，而是篩選器 —— 4 條都中才是高潛力 workflow，少 1 條就降一級。對 Eric 在 RMN / 實體零售 / 物業 / 工程顧問領域，可立刻拿來做機會 mapping。
- 保留理由：可立即操作的客戶 / 機會診斷 checklist。
- 待補強處：4 個特徵的相對權重？台灣 / 亞洲市場有沒有特殊的 forcing function（健保、勞動法、人口結構）？
- 初步知識鉤子：[[從資料平台到決策系統]]、Crux 診斷、機會評估 framework、RMN 機會 mapping

序號 5
- 候選標題：Routine Task Automation 不會複利 —— 護城河來自 domain-specific 累積
- 分級:Support
- 類型：Warning
- 核心內容：規則型任務（狀態檢查、預約提醒、表單分發）即使做到 100% 自動化也不會形成護城河 —— 因為它累積不到任何 domain-specific 的訊號（哪些保險公司接受哪種申訴論述、哪種病患 intake 預測什麼勝訴可能）。Solace / Eve / Pace 案例顯示：護城河來自「執行過程中累積的判斷資料」，不是「執行過的任務數量」。對選題創辦人，這提醒 first project 不能挑「乾淨但無學習」的 workflow。
- 保留理由：是 Clone Test 的反例補強，可避免創辦人挑錯第一個 wedge。
- 待補強處：「domain-specific 累積」與「commodity 自動化」的判定線？哪些看似 routine 的任務其實有累積（如 OCR 持續學習文件格式變異）？
- 初步知識鉤子：[[Clone Test]]、Defensive vs Generative moat、第一個 wedge 選擇、累積學習的指標

序號 6
- 候選標題：第一波 Overhead 陷阱 —— vertical 軟體常加回它要消除的 overhead
- 分級：Support
- 類型：Warning
- 核心內容：早期 vertical 軟體常常「加上的 overhead 跟移除的一樣多」 —— 新介面要學、新 workflow 要對齊、新人力（管理員、設定員）來維護工具本身。這是個結構性陷阱，因為 vendor 對「自己增加的負擔」沒有計入 ROI 模型。對 vertical AI 採購方的 due diligence checklist：問「導入後總工作小時是否真的下降？包含學習、設定、debug、人工覆核時間嗎？」
- 保留理由：補強反例視角，幫客戶端建立採購懷疑清單。
- 待補強處：哪些案例是公開驗證 overhead 真的歸零？採購方驗證的時間長度建議？
- 初步知識鉤子：[[從 demo 到產品的距離]]、總成本 vs 邊際成本、PoC 與 production gap、採購 due diligence

序號 7
- 候選標題：法規地形是 vertical AI 結構性的反平推力
- 分級：Support
- 類型：Pattern
- 核心內容：「技術會推平既有地景」是 horizontal AI 的成立假設，但 regulated verticals（HIPAA、FDA、professional liability、各國銀行金融監管）會抵抗這種推平 —— 因為合規責任是法律層級的、不能用更好的模型繞過。這同時是新進者的進入障礙，也是給已合規 vertical 玩家的時間護城河（拖 12–36 個月不等）。對 Eric 評估「哪些 vertical 適合做 D2D / DecisionOps 服務」，法規地形是必選變量。
- 保留理由：解釋為什麼某些 vertical（如 healthcare、legal、finance）的 vertical AI 機會比想像中持久。
- 待補強處：台灣的法規地形差異（個資法、金管會、衛福部規範）對機會優先級的影響？
- 初步知識鉤子：法規護城河、Defensive moat、AWS 治理、台灣監管環境 vs 美國

## C. 建議送 refine 的項目
- 1（ROI 搬到人力預算）、2（Clone Test）、3（Defensive vs Generative moat）、4（4 特徵 checklist）為主力 KEEP
- 5（routine 不複利）、7（法規地形）作為 Clone Test / Moat 卡的補強反例
- 6（overhead 陷阱）建議獨立成 warning 卡，併入「demo 到產品的距離」鉤子群

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉，與 VC Cafe 文章的 Bad / Ugly 段、Gartner DI 文章的「decision-centric」論述串接，建立 Vertical AI 主題群。
