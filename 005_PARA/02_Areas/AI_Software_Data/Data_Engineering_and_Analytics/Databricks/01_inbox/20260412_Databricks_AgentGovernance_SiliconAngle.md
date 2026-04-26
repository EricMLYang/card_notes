---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
# Databricks 擴充 AI Agent 治理與評估工具 — SiliconANGLE

> 來源：SiliconANGLE
> 來源類型：地面訊號（第三方產業媒體報導，來自 Databricks 官方發布）
> 需求層：知識建構
> 連結：https://siliconangle.com/2025/11/03/databricks-expands-tools-governing-evaluating-ai-agents/
> 搜集日期：2026-04-12
> 搜集原因：K3 — Databricks Agent Bricks / Unity Catalog 治理演進

## 摘要
Databricks 在 2025 年 11 月一次發布四件治理工具：MLflow 評估「judges」開源、AI Gateway 透過 MCP Catalog/Marketplace 擴展到外部工具治理、Multi-Agent Supervisor（beta），以及 ai_parse_document SQL 函式（PDF → 結構化資料）。所有功能都掛在 Unity Catalog 之下，繼承權限、audit trail 與 lineage。Databricks AI/ML 產品 senior director Craig Wiley 直接點名：「我們的目標是讓 organizations 把 agents 放進高風險、高價值的 use case path，從 pilot 走到 production 同時保持控制力。」

## 為什麼值得看
這是 Eric 主線「Databricks 作為 decision platform」的最直接訊號 — 而且這次擴充不是 marketing fluff，是把 **MCP（Model Context Protocol）整合進 Unity Catalog 的權限與 audit 邊界**。對 Eric 特別有用：
1. **MCP × Unity Catalog**：告訴你 Databricks 把外部工具呼叫拉進治理層的具體做法 — 這是 Eric 寫「AI workflow 上線責任邊界」的關鍵彈藥
2. **ai_parse_document**：unstructured PDF → 結構化資料的 SQL function，直接對應「資料如何進 Agent」的判準
3. **Multi-Agent Supervisor**：beta 階段，仍可看到 Databricks 對「多 agent orchestration」的官方架構觀點

## 可能偏誤或限制
- 來自 Databricks 角度的官方論述（透過 SiliconANGLE 轉述），對其他平台（Snowflake、AWS Bedrock Agents）的對比幾乎沒提
- 沒有客戶採用數字或具體案例 — 都是 capability claim 而非 outcome claim
- 「judges」評估方法的可靠性、tunable 程度、誰來定 ground truth 等實作細節缺
- Multi-Agent Supervisor 仍是 beta，不應推論為已成熟方案

## 潛在卡片方向
- MCP × Unity Catalog：把外部工具拉進權限邊界的架構卡
- ai_parse_document：unstructured 進 lakehouse 的最後一哩
- Tunable judges 取代固定 metric 的評估範式卡
- Multi-Agent Supervisor 與 Eric 自己的 Agent Role Repo Framework 對比卡
- 可連結現有卡片：[[Unity Catalog 作為 AI 控制平面]]、[[從資料平台到決策系統]]

---

## 全文翻譯（重點摘錄）

### 1. 釋出的新工具
Databricks 公布多個治理與評估工具：

- **MLflow 強化**：開源評估能力，可調參的「judges」用 domain-specific 標準評估 agent 表現
- **AI Gateway 擴張**：透過 Model Context Protocol（MCP）Catalog 與 MCP Marketplace 把治理延伸到外部工具
- **Multi-Agent Supervisor**（beta）：協調跨多 agent 與 MCP server 的 workflow
- **ai_parse_document**：SQL 函式，從 PDF 抽結構化資料，把 unstructured 內容變成可搜尋、可治理的資料

### 2. Multi-Agent Supervisor 功能
讓 agent 能「採取自動化動作，例如建立 support ticket 或執行 SQL query，同時透過 Unity Catalog 維持治理。」

### 3. Unity Catalog 的角色
Unity Catalog 作為治理 backbone，為所有 model endpoint 與外部 MCP server 提供「logging、access control、rate limiting 與 audit trail」。控制機制對連接的工具強制執行「繼承的 Unity Catalog 權限、audit trail 與 data lineage」。

### 4. 客戶採用統計
**文章未提供具體採用數字或案例。**

### 5. 高層引述
Databricks AI/ML 產品 senior director Craig Wiley：
> 我們的目標是讓 organizations 把 agents 放進高風險、高價值的 use case path

並指出治理讓他們可以「從 pilot project 走到 production，同時保持 control。」

# BreadCards

## A. 主脈絡與個人映射
- **論證骨架**：報導以「Databricks 一次釋出四件治理工具」為主軸，串成一個 Databricks 對外宣示的方向——把 agent 從 pilot 帶到 production 必須補的能力（外部工具治理、文件結構化、多 agent 協調、可調 judge），全部掛回 Unity Catalog 的權限/audit/lineage 邊界。
- **挑戰的預設**：「外部工具呼叫（MCP）跟治理是兩回事」「文件解析是 ETL 工具不是治理問題」「judge 是固定 metric 不需要客製化」。
- **個人映射**：直接補強我關注的「AI workflow 上線責任邊界」與「Repo-as-Worker」兩條主線。MCP × Unity Catalog 是一個具體可寫的架構卡——把 Anthropic 標準與 Databricks 治理層綁起來，意味著未來 agent 即使呼叫外部工具，也能納入同一套權限/audit。對 RMN 場景特別有用：第三方資料、外部 API、廣告投放工具呼叫的治理一直是難題。但要小心：報導沒有採用數字、沒有對比 Snowflake/Bedrock，需謹慎不過度推論。

## B. 候選卡（Lite）

序號 1
- 候選標題：MCP × Unity Catalog — 把外部工具呼叫拉進治理邊界的架構模式
- 分級：Core
- 類型：Pattern
- 核心內容：Databricks 透過 AI Gateway + MCP Catalog/Marketplace 把外部工具治理納入 Unity Catalog，所有 model endpoint 與外部 MCP server 都繼承 logging、access control、rate limiting 與 audit trail。這是一個值得遷移的架構模式：用「協議 + 治理層」把外部依賴拉回控制平面，而不是讓 agent 直接呼叫外部 API 造成治理黑洞。
- 保留理由：這是少見的「外部工具 × 治理」整合做法，可作為 AI 上線責任邊界的具體彈藥
- 待補強處：rate limiting / audit 對 MCP server 真實效能的影響、跨組織 MCP 呼叫的權限傳遞、failure mode 處理
- 初步知識鉤子：[[Unity Catalog 作為 AI 控制平面]]、AWS Shared Responsibility、API Gateway pattern、Service Mesh × Identity、[[從資料平台到決策系統]]

序號 2
- 候選標題：Tunable Judges 取代固定 metric — 評估從通用走向 domain-specific
- 分級：Support
- 類型：Pattern
- 核心內容：MLflow 開源「judges」並支援可調參，讓團隊用 domain-specific 標準評估 agent 表現，而不是套通用 metric。這個方向呼應「scorer 必須是團隊資產」的趨勢——好的 agent 評估不是來自更強的固定模型 judge，而是來自可調、可治理的 domain rule。
- 保留理由：與 MLflow 3 篇的訊號互相印證，顯示 Databricks 整體在把 evaluation 變成可治理資產
- 待補強處：tunable 的具體 API 範圍、judge 本身如何被 review 與版本化、誰負責定義 ground truth
- 初步知識鉤子：[[AI時代評估能力成為關鍵槓桿點]]、LLM-as-judge 限制、scorer-as-asset

序號 3
- 候選標題：ai_parse_document — 文件結構化的 SQL 化是「資料如何進 agent」的最後一哩
- 分級：Support
- 類型：Pattern
- 核心內容：Databricks 把 PDF → 結構化資料做成 SQL 函式（ai_parse_document），意味著 unstructured ingestion 從 ETL 工具變成資料平台原語。這對 RMN / 保單 / 合約類資料特別有用——這些資料以前要走獨立 pipeline，現在可以用 SQL 直接拉進 lakehouse 並繼承治理。
- 保留理由：把「unstructured ingestion」從邊角工程升級為治理層原語，是平台化轉型的訊號
- 待補強處：抽取準確率、與 LLM extractor 的 cost / latency 對比、結構不一致時的 schema evolution
- 初步知識鉤子：[[Unstructured to Structured]]、Document AI、[[從專案交付到平台化]]

序號 4
- 候選標題：Multi-Agent Supervisor 仍是 beta — 平台廠的 agent 編排架構觀點
- 分級：Question
- 類型：Question
- 核心內容：Databricks 推出 Multi-Agent Supervisor（beta）做跨 agent 與 MCP server 的協調，雖然功能未定型但揭示一個架構觀點：平台廠認為 agent 編排不應是 application 層 ad-hoc 寫的 LangGraph，而該是平台級服務。這個取捨值得追蹤——Supervisor 是否會成為 agent 編排的 control plane，還是只是另一個 vendor lock-in 元件？
- 保留理由：作為追蹤型問題卡，記錄產業方向的不確定點
- 待補強處：beta 階段功能完整性、與 LangGraph / CrewAI / OpenAI Swarm 的取捨對比、Supervisor 對 trace 的可見度
- 初步知識鉤子：[[Agent Orchestration]]、Harness 設計、Platform vs Framework 的取捨

## C. 建議送 refine 的項目
- 序號 1（MCP × Unity Catalog）：Core，可獨立成架構卡
- 序號 2（Tunable Judges）：與 MLflow 3 篇序號合併潛力高
- 序號 3（ai_parse_document）：可作為「資料如何進 Agent」系列的卡
- 序號 4（Multi-Agent Supervisor）：保留為 Question 追蹤卡

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉

