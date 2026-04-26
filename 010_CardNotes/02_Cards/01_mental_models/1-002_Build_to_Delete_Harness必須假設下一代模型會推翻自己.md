# Build to Delete — Harness 必須假設下一代模型會推翻自己

- 狀態：KEEP
- 類型：Principle
- 分類：1-
- 索引：010_CardNotes/01_Index/01_mental_models.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260412_AgentHarness2026_PhilSchmid.md（#3+#5）+ 005_PARA/02_Areas/AI_Software_Data/AI_Coding/01_inbox/20260401_從HarnessEng看skills的原子性.md（#7，合併）

## 核心命題
Harness 的最佳設計不是「未來相容」而是「容易被刪」——把工程資產押在 prompt 與控制流上會被模型升級洗掉。

## 卡片內容
Manus 6 個月重構 5 次、LangChain 一年重構 Open Deep Research 3 次、Vercel 刪掉 80% 工具反而更快——同一條原則：harness 必須模組化、低耦合、可拋棄。實作守則：**Start Simple**（預設讓模型自己 plan，避免巨大控制流，因為過度工程化的條件分支會搶走模型的 planning 能力）+ **Build to Delete**（每個模組都假設一年內會被取代）+ **最小表面積 framework**（Monolith framework 把複雜度推到看不見的角落，而不是消除它）。配合 [[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]] 一起用：能在模型翻倍時變更簡單的系統，才是好 harness。

## 使用情境
- 抗拒「精心設計三個月 workflow」的衝動時當煞車
- 評估開源 agent framework 選型
- 設計 harness 模組邊界時的取捨判準

## 邊界 / 失效條件
- 金流、權限、合規等場景仍需 deterministic flow 寫死
- 「容易刪」需要前期投資模組化
- 案例都是 coding/research agent，business decision agent 需重新評估

## 上游連結
- [[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]]
- [[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]

## 下游連結
- [[3-006_Harness六層構成_Agent系統工程的解構]]
- YAGNI / Premature abstraction

## 關聯對照
- [[模型會吸收周邊複雜度（系統結構重要性下降）]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
