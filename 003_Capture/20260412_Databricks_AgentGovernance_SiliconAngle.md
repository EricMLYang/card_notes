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
