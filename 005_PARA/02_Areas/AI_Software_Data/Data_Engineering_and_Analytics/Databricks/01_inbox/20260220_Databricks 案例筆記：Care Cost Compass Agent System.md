---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-20
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# **Databricks 案例筆記：Care Cost Compass Agent System**

---





#### **1\. 案例概要**



- **專案名稱：** Care Cost Compass (費用指南針)

- **目標：** 打造一個 AI Agent 聊天機器人，以 REST API 形式提供服務。使用者能透過自然語言詢問醫療程序的預估自付費用。

- **運作流程：** Agent 接收到使用者問題後，會自動化執行一連串複雜任務，包括：

   1. **理解語意：** 辨識問題中的醫療程序。

   2. **多源檢索 (RAG)：** 從 PDF 保單文件中找出相關給付條款、從資料庫查詢標準費用碼、查詢客戶目前的保險累積額度。

   3. **邏輯計算：** 根據檢索到的所有資訊，計算最終的自付金額。

   4. **生成回覆：** 將計算結果彙整成一段清晰易懂的文字回覆給使用者。



#### **2\. 特點：Databricks 內部服務託管的 Agent**



此案例的最大特點是**將 Databricks 從一個傳統的內部數據分析平台，轉變為一個能託管即時、對外 AI 應用服務的端到端平台**。它整合了從數據工程、AI 開發、安全治理到線上部署 (Serving) 的所有環節，形成一個完整的閉環。Agent 作為核心協調者，由平台內部的各種託管服務提供支援。



#### **3\. Agent 託管的服務名稱與說明**



- **服務名稱：** **Mosaic AI Model Serving**

- **說明：** 這是 Databricks 內建的 **Serverless (無伺服器) 部署平台**。開發者可以將包含 Agent 邏輯的 Python 程式碼 (打包成 MLflow `pyfunc` 模型) 一鍵部署上去。

- **功能比喻：** 類似 AWS Lambda 或 Google Cloud Run，它會自動將你的程式碼變成一個高可用、可自動擴展的 REST API 端點，並處理底層的所有維運工作。



#### **4\. Agent 可呼叫的工具和記憶相關服務**



Agent 的強大之處在於它能靈活呼叫平台上的各種工具來完成任務：

| 服務/工具名稱 | 功能說明 | 後端比喻 | 
|---|---|---|
| **Mosaic AI Vector Search** | **語意搜尋資料庫 (RAG 核心)**。用於儲存非結構化資料 (如 PDF 文件) 的向量，讓 Agent 能理解問題語意並找到最相關的資料段落。 | 一個為 AI 定制的 Elasticsearch 或 OpenSearch | 
| **Online Tables** | **高效能線上資料庫 (低延遲)**。用於存放需要快速 Key-Value 查詢的結構化資料，如客戶資料、費用表等。 | 一個內建的 Redis 或 DynamoDB | 
| **Unity Catalog** | **統一數據治理中心**。管理所有數據資產 (資料表、模型、向量索引) 的權限，確保 Agent 只能存取它被授權的資料。 | 數據目錄 + IAM 權限控管系統 | 
| **AI Gateway** | **外部 LLM 金鑰保險箱**。集中且安全地管理對外部 LLM (如 OpenAI) 的 API Key，Agent 本身不需持有敏感金鑰。 | 一個專門管理 API Key 的 Secret Manager / Vault | 



#### **5\. 延遲 (Latency) 與資安 (Security) 特別說明**



**針對延遲問題的解決方案：**

1. **高速快取 (Online Tables)：** 這是關鍵。將頻繁查詢的資料放在 Online Tables 中，實現毫秒級的快速查找，避免掃描慢速的資料倉儲。

2. **平行處理 (Parallel Execution)：** Agent 內部邏輯採用 `asyncio`，能**同時**發出多個資料查詢請求 (查保單、查費用、查客戶資料)，大幅縮短了 I/O 等待時間。

3. **簡化邏輯 (Custom PyFunc)：** 採用固定、程式化的工作流程，減少了 LLM 反覆決策的延遲，提升了反應速度。

**針對對外暴露的資安措施：**

1. **網路層防護：** API 端點本身是受管理的 Gateway，可設定 **IP 白名單**來限制來源，或部署為**私有端點**完全不暴露於公網。

2. **身份驗證：** 所有 API 請求都必須攜帶有效的**認證權杖 (Token)**，無權杖者會被直接阻擋。

3. **權限最小化 (核心安全策略)：** Agent 以一個\*\*「服務主體」(Service Principal)\*\* 的身份運行。**Unity Catalog** 會嚴格限制此身份只能存取完成任務所必需的最小數據集。即使 API 被攻破，**安全衝擊範圍也被有效控制**，無法存取到其他未經授權的敏感資料。

4. **全面監控：** 透過 **Inference Tables** 和 **Audit Logs** 記錄所有 API 的請求、回應與平台操作，提供完整的安全審計與異常行為分析能力。

# BreadCards

## A. 主脈絡與個人映射
- **論證骨架**：以 Care Cost Compass（醫療費用 agent）為案例，分四節說明（案例概要 / Databricks 託管特點 / 工具與記憶服務 / 延遲與資安）。重點是把 agent 從研究實驗變成「對外 REST API」需要解決的兩個現實工程問題：延遲與資安。針對延遲提出三招（Online Tables 快取 / asyncio 並行 / 簡化 LLM 決策路徑）；針對資安提出四層（IP 白名單 / Token 驗證 / Service Principal 權限最小化 / Inference Tables + Audit Logs）。
- **挑戰的預設**：「Databricks 是內部分析平台不能對外提供服務」「agent 反應慢沒辦法」「agent 對外暴露無法做嚴格安全控制」。
- **個人映射**：直接命中我關注的「analysis workflow productization」「AWS Shared Responsibility 在 AI workflow 的具體做法」與「RMN agent 對外提供查詢服務」三條主線。Service Principal × Unity Catalog × Inference Tables 是把「最小權限 + 可追溯」這個原則落地到 agent 的具體架構，可遷移到任何 agent-as-service 場景。延遲三招（特別是「簡化 LLM 決策路徑」這個取捨）也可挑戰主流「讓 LLM planning 越多越好」的迷思。

## B. 候選卡（Lite）

序號 1
- 候選標題：Custom PyFunc 取代 LLM 動態 planning — agent 延遲取捨
- 分級：Core
- 類型：Heuristic
- 核心內容：傳統 agent 讓 LLM 反覆決策下一步，導致延遲累積。Care Cost Compass 採用「固定、程式化的工作流程」（custom PyFunc），把任務拆成已知步驟（理解問題 → 多源檢索 → 計算 → 回覆），減少 LLM 反覆決策的延遲。這是一個明確的取捨：放棄 agent 的「自主規劃彈性」換取可預測的延遲與成本。對 production-facing agent 特別重要——使用者對延遲非常敏感。
- 保留理由：罕見的取捨——多數人鼓吹「讓 LLM 規劃」，這篇給出何時該反過來的判準
- 待補強處：何時 custom PyFunc 不夠用、什麼情境必須回到 dynamic planning、混合架構的設計
- 初步知識鉤子：[[Workflow vs Agent]]、[[簡單比聰明可靠]]、Anthropic 「Building Effective Agents」 的 workflow vs agent 分類、[[Harness 是把模型變成 Agent 的關鍵]]

序號 2
- 候選標題：Online Tables + asyncio 並行 — agent 延遲的兩個槓桿點
- 分級：Support
- 類型：Pattern
- 核心內容：agent 對外提供服務時，延遲主要來自 I/O 等待（多次資料查詢）與單一 LLM 推理鏈。解法是兩層：(1) 把熱資料放 Online Tables 做毫秒級 KV 查詢，避免掃描慢速 warehouse；(2) agent 內部用 asyncio 同時發出多個查詢請求（保單 / 費用 / 客戶資料），把序列 I/O 變成並行。這個 pattern 可遷移到任何「多源 RAG + production latency」場景。
- 保留理由：兩個 lever 的組合很實用，可直接套到 RMN 多源資料 agent
- 待補強處：Online Tables 與 Delta Table 的一致性策略、asyncio 在錯誤處理上的複雜度、cache invalidation
- 初步知識鉤子：[[多源 RAG 延遲設計]]、Cache-Aside pattern、Serving layer vs Analytics layer 分離

序號 3
- 候選標題：Service Principal × Unity Catalog — agent-as-service 的權限最小化具體做法
- 分級：Core
- 類型：Pattern
- 核心內容：Agent 對外提供服務時，最大的安全風險不是 LLM 被攻擊，而是 agent 身分能存取的資料範圍過大。Care Cost Compass 用「Service Principal」作為 agent 執行身分，Unity Catalog 嚴格限制此身分只能存取完成任務所必需的最小資料集。即使 API 被攻破，安全衝擊範圍也被有效控制。這是把「權限最小化」原則從理論落地到 agent 的具體架構模式，可遷移到任何 agent-as-service 場景。
- 保留理由：對應「AI workflow 上線責任邊界」主線，是少見的具體可複製做法
- 待補強處：Service Principal 跨 tenant / 跨客戶的隔離設計、權限變更的審批與 audit、與 row-level security 的搭配
- 初步知識鉤子：[[Unity Catalog 作為 AI 控制平面]]、AWS Shared Responsibility、IAM Least Privilege、[[Agent 身分管理]]

序號 4
- 候選標題：對外 agent API 的四層安全模型（網路 / 身分 / 權限 / 監控）
- 分級：Support
- 類型：Pattern
- 核心內容：agent 對外暴露為 REST API 時，需要四層防護：(1) 網路層 — IP 白名單或私有端點；(2) 身分層 — 所有請求必須帶有效 Token；(3) 權限層 — Service Principal + Unity Catalog 強制最小權限；(4) 監控層 — Inference Tables + Audit Logs 記錄請求 / 回應 / 平台操作。四層是縱深防禦（defense in depth），任一層被攻破還有後續層攔截。
- 保留理由：縱深防禦在 agent-as-service 的具體展開，可作為 production agent 的安全 checklist
- 待補強處：每層的真實攻擊向量與失效模式、四層之間的耦合與獨立性、與 OWASP LLM Top 10 對應
- 初步知識鉤子：Defense in Depth、OWASP LLM Top 10、[[Production agent 安全 checklist]]

## C. 建議送 refine 的項目
- 序號 1（Custom PyFunc 取代 LLM 動態 planning）：Core，取捨明確且逆主流
- 序號 3（Service Principal × Unity Catalog 權限最小化）：Core，落地性高
- 序號 2（Online Tables + asyncio）：可保留為延遲 pattern 卡
- 序號 4（四層安全模型）：可保留為 production agent 安全 checklist

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉