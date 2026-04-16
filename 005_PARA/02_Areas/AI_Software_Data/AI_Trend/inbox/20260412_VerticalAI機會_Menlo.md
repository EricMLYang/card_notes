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
