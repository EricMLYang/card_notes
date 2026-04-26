# 三類 Grader 是分層防線，不是替代選項（Swiss Cheese Model）

- 狀態：KEEP
- 類型：Pattern
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260228_Anthropic_拆解Agent評估的迷霧.md（#4）

## 核心命題
Code-based / Model-based / Human grader 不是「該選哪個」的單選題，而是「如何分層搭配」的縱深防禦設計。

## 卡片內容
Code-based grader 快、便宜、客觀但對合理變體脆弱；Model-based grader 處理開放輸出但需與人類校準、會被 prompt injection 攻擊；Human grader 是 gold standard 但慢且貴。實務上要混搭：deterministic 為主擋掉確定性錯誤、必要時加 LLM rubric 處理開放任務、用 human 偶發抽樣校準 LLM judge。Swiss Cheese Model 思維——任何單層都會有洞，多層錯位才能擋住大部分問題。Cost-quality tradeoff 的關鍵不是「哪個最好」，而是「哪些層必須有，分別承擔哪種錯誤」。

## 使用情境
- 為 agent 產品設計 eval pipeline 時的層級規劃
- 說服老闆 LLM judge 不能完全取代 human review
- 發現某類失敗一直漏網時，問「我缺了哪一層 grader」

## 邊界 / 失效條件
- 每多一層成本與延遲都上升
- LLM judge 若被 prompt injection / grader hacking 攻破反而會給錯誤的安心感

## 上游連結
- [[AI Error Analysis：LLM 應用評估方法]]

## 下游連結
- [[兩階段判斷設計_AI自動化的安全模式]]

## 關聯對照
- [[10-002_Policy_as_Code護欄要在LLM之外執行]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
