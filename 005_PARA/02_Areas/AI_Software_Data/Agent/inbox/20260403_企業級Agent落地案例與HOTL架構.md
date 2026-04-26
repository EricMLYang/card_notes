---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# 2026 企業級 AI Agent 落地案例與 HOTL 架構實踐

> 來源：綜合科技媒體與產業報告 (Gartner, juejin, meta-intelligence)
> 連結：多個來源
> 搜集日期：2026-04-03
> 搜集原因：Agentic Workflow 工程化與人機協作

## 摘要
2026 年被視為 AI Agent 的規模化落地元年。企業應用已從實驗期進入「價值實現期」，核心轉向 **Multi-Agent Systems (MAS)** 與 **Human-on-the-Loop (HOTL)** 模型。丹麥製造商 Danfoss 與全球最大製漿廠 Suzano 的案例顯示，Agent 能自主處理 80% 的交易決策或將 5 萬名員工的數據查詢效率提升 95%。

## 潛在卡片方向
- **HOTL vs HITL**：2026 年企業傾向將 Agent 視為自主運行的生產線，人類僅作為「Command Center」處理例外。
- **Agentic RAG 的閉環能力**：從被動檢索進化為「檢索-分析-決策-反饋」的自主判斷。
- **A2A (Agent-to-Agent) 協定**：透過 MCP (Model Context Protocol) 實現跨 Agent 協作，而非單一 Bot。
- **與現有卡片連結**：[[20260402_初版團隊用AgentCoding流程]]、[[20260221_AI 24-7 運作的關鍵控制點：以判斷權角色重新分類]]

---

## 核心內容整理

### 1. 標桿案例：從「自動化」到「自主化」
*   **Danfoss (丹麥製造業)**：
    *   **場景**：電子郵件訂單處理。
    *   **工作流**：Agent 自動判讀郵件、跨 5 個 ERP/CRM 系統查核庫存與價格、生成訂單草稿。
    *   **成效**：80% 交易決策實現自動化，回應時間從 42 小時縮短至近即時。
*   **Suzano (原物料業)**：
    *   **場景**：全員數據分析。
    *   **工作流**：5 萬名員工透過自然語言 Agent 直接存取 SAP 物料數據。
    *   **成效**：數據查詢與報表任務時間減少 95%，去中心化決策成為現實。

### 2. 2026 年生產級 Agent 最佳實踐：HOTL 模型
*   **Human-on-the-Loop (HOTL)**：Agent 執行端到端流程，人類在管理後台進行「例外管理」。
*   **分級授權矩陣 (Tiered Autonomy Matrix)**：
    *   **Tier 1 (完全自主)**：低風險任務（如數據格式化），僅設自動化監控。
    *   **Tier 2 (HOTL)**：中風險任務（如外發郵件），需人類「Yes/No」確認。
    *   **Tier 3 (HITL)**：高風險任務（如大額採購），由人類主導，Agent 提供「決策包 (Decision Package)」。
*   **決策包 (Decision Package)**：Agent 請求人類介入時，必須附帶「推理路徑、使用數據、潛在取捨」，避免人類成為效率瓶頸。

### 3. 工程化轉向：從推理到「Harness」
*   **結構化編排 (Structured Orchestration)**：不再依賴 LLM 的隨機推理，而是定義明確的狀態轉換（Understand → Plan → Act → Evaluate）。
*   **MCP (Model Context Protocol)**：標準化協議，讓 Agent 能無縫連結外部數據源與工具鏈，打破 SaaS 孤島。

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：2026 是企業級 Agent 的價值實現期；典範轉移有兩條主線——（1）從 HITL（人在迴圈內逐步審查）轉到 HOTL（人在迴圈外做例外管理）；（2）從靠 LLM 隨機推理轉到結構化 orchestrator + MCP。Danfoss 把訂單處理 80% 自動化；Suzano 讓 5 萬員工用自然語言查 SAP 數據效率提升 95%。
- 作者挑戰的預設：（1）Agent 應該每步都讓人確認 → 真正生產級 Agent 要把人從 loop 內移出 loop 外；（2）越自主越好 → 應該按風險分級（Tier 1/2/3）、不同任務不同自主度；（3）Agent 請求人類介入時只丟個 yes/no → 必須附「決策包」（推理路徑 + 數據 + 取捨）才不會讓人變成新的瓶頸。
- 個人映射：直接補強你的「判斷權歸屬」「兩階段判斷設計」主軸。HOTL 與分級授權矩陣是把你已有的「Agent 能做什麼 / 必須交給誰」抽象化的具體框架；「決策包」概念是你之前沒明寫的高槓桿節點——它把人類介入從「審查瓶頸」轉成「快速決策」。

## B. 候選卡（Lite）

序號 1
- 候選標題：HOTL 是企業 Agent 落地的下一站，不是 HITL 的升級版
- 分級：Core
- 類型：Principle
- 核心內容：HITL（人在迴圈內）要求每個關鍵步驟人類審查，會讓人變成 Agent 自動化的瓶頸；HOTL（人在迴圈外）讓 Agent 端到端執行，人類只在管理後台處理例外。這不是漸進升級，而是兩種根本不同的責任結構：HITL 是「人類批准 Agent」，HOTL 是「Agent 自運行 + 人類監督例外」。
- 保留理由：直接點出企業 Agent 從 PoC 到 production 過程中最容易卡住的瓶頸（人類審查容量），並給出結構性解法。對你關心的「24/7 Agent 運作」與「judgment 介入點設計」是核心拼圖。
- 待補強處：HOTL 的失敗模式（例外定義錯誤 / 例外洪水 / 例外漏抓）未交代；過渡期（HITL → HOTL）的具體門檻條件未說明。
- 初步知識鉤子：[[24-7 AI 運作的關鍵控制點]]、[[判斷權歸屬]]、[[Tiered Autonomy Matrix]]

序號 2
- 候選標題：分級授權矩陣（Tiered Autonomy）：用風險決定 Agent 自主度
- 分級：Core
- 類型：Heuristic
- 核心內容：把 Agent 任務按風險分三層——Tier 1（完全自主，如數據格式化，僅自動化監控）；Tier 2（HOTL，如外發郵件，需人類 yes/no 確認）；Tier 3（HITL，如大額採購，人類主導，Agent 提供決策包）。同一個 Agent 系統內的不同動作可分別屬於不同 Tier，不需一刀切。
- 保留理由：是一個可直接套用到任何 Agent 系統的設計判準；解決「全自動 vs 全手動」的偽兩難。對你關心的「Agent workflow productization」很實用。
- 待補強處：分層的具體門檻（金額？影響範圍？可回復性？）需更明確；Tier 動態升降級機制（從 Tier 2 升到 Tier 1 的條件）未交代。
- 初步知識鉤子：[[兩階段判斷設計]]、[[HOTL]]、[[風險分級]]

序號 3
- 候選標題：決策包（Decision Package）：避免人類介入變成新瓶頸的關鍵設計
- 分級：Core
- 類型：Principle
- 核心內容：當 Agent 請求人類介入時，必須附帶「推理路徑、使用的數據、潛在取捨方案」，而不是丟一個 yes/no 給人決定。沒有決策包的人類介入會讓 Agent 系統的瓶頸轉移到人——人變成新的 throughput 限制。決策包是讓 HITL / HOTL 真的能 scale 的關鍵中介結構。
- 保留理由：把「人類介入點」從一個介面問題抬升到一個結構問題；對你做「Agent + 決策系統」的 D2D Architect 定位非常 load-bearing。
- 待補強處：決策包的最小資訊集（哪些一定要含）；如果 Agent 推理本身有偏差，決策包是否反而讓人類被誤導？
- 初步知識鉤子：[[判斷權歸屬]]、[[Decision System]]、[[人類介入點設計]]

序號 4
- 候選標題：結構化 Orchestration > LLM 隨機推理：生產級 Agent 的工程化轉向
- 分級：Support
- 類型：Pattern
- 核心內容：生產級 Agent 不能依賴 LLM 自己的隨機推理流程，要明確定義狀態轉換（Understand → Plan → Act → Evaluate）。orchestration logic 寫在框架層，不是寫在 prompt 裡。這呼應 InfoQ 那篇「orchestration 與 execution 應分層」的主張，是同一個 pattern 的不同表達。
- 保留理由：把「Agent 可靠性」從 prompt tuning 問題拉到架構設計問題，是 production agent 的關鍵思維轉變。
- 待補強處：何時 LLM 推理仍勝過硬編碼狀態機（探索性任務）？兩者的混合策略？
- 初步知識鉤子：[[A2A 與 MCP 分層]]、[[Harness Engineering]]、[[Workflow vs Agent]]

序號 5
- 候選標題：80% 自動化的真正含意：人從處理者變成例外管理者
- 分級：Support
- 類型：Heuristic
- 核心內容：Danfoss 案例的 80% 自動化不是說 Agent 完全取代人，而是工作分工重組——80% 由 Agent 端到端處理（不需要人介入），剩下 20% 由人作為例外管理者集中處理。回應時間從 42 小時縮短到接近即時，是因為大多數案件不再排隊等人類。
- 保留理由：拆解一個常被誤讀的數字。對你關心的「AI 對角色的結構性衝擊」與「商業語言轉譯」很有用——可以把這個觀點當成向 client / management 解釋自動化效益的標準說法。
- 待補強處：剩下 20% 的人力需求是否真的減少？可能反而需要更高階人才？
- 初步知識鉤子：[[從執行力到判斷力遷移]]、[[Andy Grove 槓桿]]、[[自動化的真實效益]]

## C. 建議送 refine 的項目
- 序號 1（Core）：HOTL vs HITL 結構差異
- 序號 2（Core）：分級授權矩陣
- 序號 3（Core）：決策包
- 序號 4（Support）：結構化 orchestration
- 序號 5（Support）：80% 自動化的角色重組

## D. 呼叫 refine-cards
- 上述 5 張候選卡交由 refine-cards 精煉；建議在 refine 階段檢查序號 1+2+3 是否組成「HOTL 三件組」打包成連結串；序號 4 應與 A2A/MCP 那篇的「分層架構」做去重。

