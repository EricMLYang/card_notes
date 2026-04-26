# pass@k vs pass^k — 能上線 vs 只能 demo 的最尖銳判準

- 狀態：KEEP
- 類型：Heuristic
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260228_Anthropic_拆解Agent評估的迷霧.md（#2）

## 核心命題
研究 benchmark 多用 pass@k（試 k 次至少一次成功），但 production customer-facing agent 真正要過的是 pass^k（連續 k 次每次都成功）；這兩個指標的差距，就是 demo 與上線的距離。

## 卡片內容
同一個 75% 成功率的 agent，pass@10 趨近 100%（看起來無敵），pass^10 趨近 0%（生產上幾乎必崩）。Coding 類「找到一次解就贏」的場景用 pass@k 合理；客戶端/自動化決策「每次都不能錯」的場景必須用 pass^k。指標選錯，評估會讓人誤以為 agent 已準備好上線。pass^k 也是把 SLA 與 outcome-based pricing 落到可驗證的最關鍵橋樑——沒有穩定性指標，就沒有可賣的 outcome。

## 使用情境
- 寫 agent 產品的 SLA 與 acceptance criteria
- 評估一個 demo 影片是否代表生產可用度
- 為 customer-facing agent 設計監控指標

## 邊界 / 失效條件
- 多步驟任務的 step-level pass^k 怎麼算尚未有定論
- 對純探索類/創意類任務 pass@k 仍是合適語言

## 上游連結
- [[AI時代評估能力成為關鍵槓桿點]]

## 下游連結
- [[兩階段判斷設計_AI自動化的安全模式]]
- [[Trust Gap 就是產品機會：AI 能做 5 小時，人類只敢讓它跑 42 分鐘]]

## 關聯對照
- [[7-005_Outcome-based_Pricing不是趨勢全勝]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
