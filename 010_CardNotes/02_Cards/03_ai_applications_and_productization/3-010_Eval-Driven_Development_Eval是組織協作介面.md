# Eval-Driven Development — Eval 是組織協作介面，不是研究產物

- 狀態：KEEP
- 類型：Heuristic
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260228_Anthropic_拆解Agent評估的迷霧.md（#7）

## 核心命題
兩個工程師讀同一份 spec 對 edge case 的理解經常不同；eval suite 是「強迫共識的可執行規格」，因此它的真實角色是 PM × Engineer × Researcher 之間最高頻寬的協作介面。

## 卡片內容
在 Anthropic，eval 不是研究團隊獨有的工具，產品 PM、CSM、銷售都可用 Claude Code 提交 eval task PR。這把 eval 從「品質檢查工具」拉高成「組織決策語言」：當需求模糊、判斷邊界不明時，提交一個 eval 比寫一份 spec 更精準也更可驗證。Eval-Driven Development 的意思是先把「什麼叫做對」寫成可執行 case，再去實作 agent。對小團隊也成立——不需要 dedicated eval team，需要的是「任何角色都能新增一條 eval」的儀式與 tooling。

## 使用情境
- 跨部門對 agent 行為有爭議時
- 建立 agent product team 的協作工作流
- 做向上管理/對客戶溝通時把抽象需求轉成可量化承諾

## 邊界 / 失效條件
- 非工程角色提交 eval 的品質需要有 review 機制
- 過早把探索性需求轉成 eval 會壓縮創意空間

## 上游連結
- [[AI 協作時代 - 衡量變重要]]
- [[AI時代評估能力成為關鍵槓桿點]]

## 下游連結
- [[10-005_20-50個真實失敗就能啟動Eval]]
- [[DecisionOps]]

## 關聯對照
- [[先定義驗證標準再動手的倒推思維]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
