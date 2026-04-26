---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-18
---

## [重點]
核心週期：讀取狀態 → 規劃 → 執行工具呼叫 → 觀察結果 → 確定性更新狀態。將 LLM 決策（機率性）與狀態轉換（確定性）分離，顯著提升可靠性

## [摘要]


## [詮釋]


---

# AI Agents in 2026: Practical Architecture for Tools, Memory, Evals, and Guardrails

> 來源：andriifurmanets.com
> 連結：https://andriifurmanets.com/blogs/ai-agents-2026-practical-architecture-tools-memory-evals-guardrails
> 搜集日期：2026-03-16
> 搜集原因：AI 24/7 自動化運作設計（Guardrails / 判斷權）

## 摘要

這篇文章是 2026 年 production AI Agent 架構的實戰指南。核心框架是將 agent 理解為「控制迴路」而非增強版聊天機器人，將 LLM 決策（機率性）與狀態轉換（確定性）分離。提供從原型到生產的 1-2 週實作序列，對工具合約、分層記憶、護欄設計都有具體規範。

## 關鍵段落

**控制迴路框架：**
> "核心週期：讀取狀態 → 規劃 → 執行工具呼叫 → 觀察結果 → 確定性更新狀態。將 LLM 決策（機率性）與狀態轉換（確定性）分離，顯著提升可靠性。"

**工具合約設計：**
> "工具應作為帶有驗證輸入/輸出的類型化 API，而非建議。每個工具呼叫應包括超時限制、重試預算和成本上限。結果格式：`{ ok, data, error, meta }`"

**分層記憶架構（反向量資料庫建議）：**
> "四層記憶：工作記憶（短暫狀態）、對話摘要（滾動有損記錄）、任務製品（結構化輸出）、長期偏好。向量檢索適用特定場景，不應作為基礎。"

**護欄設計哲學：**
> "最被低估的護欄是『政策即代碼』——在機器可讀格式中定義允許的工具和審批要求，在 LLM 外部強制執行。安全來自讓失敗變得安全、可觀察且可恢復，而非追求完美。"

**1-2 週生產就緒路徑：**
> "Step 1：工具合約和驗證 → Step 2：狀態 reducer → Step 3：追蹤基礎設施 → Step 4：評估數據集（20-50 個真實測試案例）→ Step 5：政策門控和審批 UX → Step 6：記憶層"

**2026 關鍵洞察：**
> "模型能力已足夠。真正的差異化在於系統是否能可靠選擇正確行動、尊重邊界、實現可觀察性並建立用戶信任。agent 本身很直接；支撐基礎設施才是產品。"

## 潛在卡片方向

- Production AI Agent = 控制迴路（probabilistic decision + deterministic state）
- 工具合約設計原則：API 合約而非建議，統一結果格式
- 分層記憶 4 層架構（不要預設用向量 DB）
- 護欄設計：Policy as Code 比模型層過濾更可靠
- 1-2 週原型到生產的實作序列（可做 checklist）
- 與現有卡片連結：[[AI 24/7 判斷權控制點分類]]、[[Agent 系統設計核心機制]]

---
*由 scout-news 自動搜集，待 process-inbox 處理*

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：把生產級 Agent 理解為「控制迴路」而非增強版聊天機器人——LLM 決策（機率性）必須與狀態轉換（確定性）分離。圍繞這條主軸給出工具合約、分層記憶、護欄、評估的具體規範，並提供 1–2 週從原型到生產的實作序列。
- 挑戰的預設：「Agent = LLM + tools」「分層記憶 = 向量資料庫」「護欄 = LLM 自我審查」。指出向量檢索是特定場景方案不該作為基礎，護欄應該是 Policy as Code 在 LLM 外執行。
- 個人映射：對 D2D Architect / DecisionOps 主軸——這是把 decision system 的「決策」與「執行」明確劃線的工程藍圖，可直接對應到 Vertical AI 的 production checklist。

## B. 候選卡（Lite）

序號 1
- 候選標題：Production Agent ＝ 控制迴路 — 機率性決策 × 確定性狀態轉換的明確分離
- 分級：Core
- 類型：Principle
- 核心內容：核心週期：讀取狀態 → 規劃 → 執行工具呼叫 → 觀察結果 → 確定性更新狀態。LLM 只做「該做什麼」的機率性判斷；狀態變更走純程式碼的 reducer。混在一起做（例如直接相信 LLM 說「已更新」）就會吃到 hallucination 與不可追溯。
- 保留理由：是把 Agent 從 demo 推到 production 的根本架構分割。
- 待補強處：當 LLM 同時要產生「決策」與「副作用 payload」時的邊界處理。
- 初步知識鉤子：Transcript ≠ Outcome、State Reducer Pattern、Event Sourcing。

序號 2
- 候選標題：工具合約設計 — 工具是帶驗證的類型化 API，不是建議
- 分級：Core
- 類型：Pattern
- 核心內容：每個工具呼叫應有：型別化 input/output、超時、重試預算、成本上限、統一結果格式 `{ ok, data, error, meta }`。把工具當合約而非「魔法函數」，讓上游 LLM 與下游 reducer 都能預期失敗模式。沒有合約的工具會在規模化時變成最大的不穩定來源。
- 保留理由：可直接寫進工具開發 SOP；對 Vertical Data Agent 特別關鍵。
- 待補強處：unified result format 在 streaming / partial result 場景的擴展。
- 初步知識鉤子：API Contract、Anthropic Tool Use 設計、UC Functions 的工具註冊。

序號 3
- 候選標題：分層記憶 4 層 — 工作記憶 / 對話摘要 / 任務製品 / 長期偏好；不要預設用向量 DB
- 分級：Core
- 類型：Pattern
- 核心內容：四層記憶：工作記憶（短暫狀態）、對話摘要（rolling 有損）、任務製品（結構化輸出）、長期偏好。向量檢索適合特定場景（語意搜尋大量文件），不應作為記憶基礎。多數團隊預設「分層記憶 = vector DB」是錯的——大部分情境用結構化儲存與摘要更可靠。
- 保留理由：直接打掉「先架 vector DB」的常見預設，給出更務實的記憶分層藍圖。
- 待補強處：每層記憶的儲存技術選型（Redis / Delta / KV store）對應；多用戶隔離。
- 初步知識鉤子：OpenCloud 三檔記憶（swell/user/memory.md）、Memory Hierarchy、Repo-as-Worker。

序號 4
- 候選標題：Policy as Code — 最被低估的護欄，在 LLM 之外執行
- 分級：Core
- 類型：Principle
- 核心內容：在機器可讀格式中定義「允許的工具、審批要求、權限邊界」，在 LLM 外部強制執行（不是丟進 system prompt 求模型遵守）。護欄哲學：安全來自讓失敗變得安全、可觀察且可恢復，而非追求完美。對應 AWS Bedrock AgentCore 用 Cedar policy 在 gateway 層做工具許可。
- 保留理由：把護欄從「prompt 提醒」升級到「可稽核、可單元測試的程式」。
- 待補強處：policy 與 prompt 之間的分工邊界（哪些必須是 policy、哪些可以留 prompt）。
- 初步知識鉤子：Steering Hooks、Defense in Depth、Cedar / OPA。

序號 5
- 候選標題：1–2 週原型到生產的實作序列 — 6 步 checklist
- 分級：Support
- 類型：Heuristic
- 核心內容：Step 1 工具合約與驗證 → Step 2 狀態 reducer → Step 3 追蹤基礎設施 → Step 4 評估資料集（20–50 個真實案例）→ Step 5 政策門控與審批 UX → Step 6 記憶層。順序很重要——先有合約與 reducer 才能談 trace；先有 trace 才能建 eval；先有 eval 才能做 policy gate。
- 保留理由：給「Agent 該怎麼從 PoC 上線」一個明確順序，可直接做 sprint plan。
- 待補強處：團隊規模與時間預算對應的步驟取捨。
- 初步知識鉤子：Anthropic 20–50 真實失敗、Eval-Driven Development、Production Readiness Checklist。

序號 6
- 候選標題：2026 差異化 — 模型能力已足夠，差異化在「支撐基礎設施」是不是產品
- 分級：Core
- 類型：Heuristic
- 核心內容：作者 thesis：「Agent 本身很直接；支撐基礎設施才是產品。」差異化在系統能否可靠選對行動、尊重邊界、實現可觀察性、建立用戶信任。模型能力的進步不會自動補完這些——這正是 harness is key 的另一個版本，但更聚焦在 production 護城河。
- 保留理由：把「投資哪一層」的命題拉到產品策略高度，對 Vertical AI 特別關鍵。
- 待補強處：當 frontier model 又跳一階，這個 thesis 是否仍成立。
- 初步知識鉤子：harness is key、Opinionated AI、Selling the Work / RaaS。

## C. 建議送 refine 的項目
- 序號 1, 2, 3, 4（最高優先：production 架構四支柱）
- 序號 5, 6（中優先：實作序列 + 策略 thesis）

## D. 呼叫 refine-cards
- 將上述 6 張候選卡交由 refine-cards 精煉。
