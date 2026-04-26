# Agent 真正的瓶頸是 Ambiguous Situations 下的驗證與恢復能力，不是 codegen

- 狀態：KEEP
- 類型：Warning
- 分類：4-
- 索引：010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260407_Stripe用真實Benchmark測AI整合能力.md（#2）

## 核心命題
Agent 的典型失敗模式不是不會寫 code，而是缺少「我怎麼知道我做對了」與「失敗了怎麼回到正軌」的能力。

## 卡片內容
Stripe 觀察到 agent 的兩類典型失敗：(a) SDK 升級任務裡用不存在的測試資料打 API、看到 400 error 卻認為任務成功；(b) 瀏覽器操作時一次塞太多動作、焦點移走後失敗、沒有 refresh/refocus 的恢復策略而直接放棄。差別不在生成能力，而在「驗證標準」與「恢復策略」。這把 agent 工程化的真正槓桿從「換更強模型」轉到「設計 plan-generate-evaluate-recover loop」。同時也是 AI Coding 風險治理的核心命題——agent 越自動，越需要它自己會懷疑、會回頭。

## 使用情境
- 診斷 agent 為何在某類任務一直失敗時，先檢查驗證/恢復而非 generation
- 設計 agent harness 時把 verification step 列為一等公民
- 對「換更強模型就好」的提案提出反論

## 邊界 / 失效條件
- 任務本身就無歧義時驗證與恢復價值較低
- 若驗證機制太重會拖慢 happy path

## 上游連結
- [[3-009_Eval的對象是Stack不是模型本身]]

## 下游連結
- [[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]
- [[Agent 產品 95% 在 Production 失敗的原因]]

## 關聯對照
- [[10-007_Transcript≠Outcome_Agent評估必須驗環境狀態]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
