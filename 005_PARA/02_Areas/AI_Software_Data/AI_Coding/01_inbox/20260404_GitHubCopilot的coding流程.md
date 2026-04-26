---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

GitHub Copilot 公開了他們的 AI Coding 流程

幾個他們踩出來的原則：

1. 先 /plan 再動手
不要直接叫 agent 寫 code
先用 planning mode 對齊方向

2. 重構和文件比寫新功能重要
乾淨的架構和完整的文件
是 agent 能不能有效工作的前提

3. 出錯時怪流程不怪 agent
agent 寫出爛 code 代表你的 linting、
typing、測試不夠嚴格

5 個人、不到 3 天
就產出 11 個 agent、4 個 skill
改了 345 個檔案、+28,858 行 code

他們的開發循環：
plan → autopilot → agent code review → 人工 review
每週再跑一次自動化檢查
抓測試缺漏、重複 code、文件落差

結論很直白：
讓 agent 寫好 code 的能力
跟讓人寫好 code 的能力相同
都是架構、文件、測試、設計
沒有捷徑

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：GitHub Copilot 自家流程：先 /plan 再動手、重構文件比寫新功能重要、出錯怪流程不怪 agent。5 人 3 天產出 11 個 agent + 4 個 skill + 改 345 檔案 + 28,858 行。完整循環：plan→autopilot→agent code review→人工 review→每週自動化檢查。結論：讓 agent 寫好 code 與讓人寫好 code 同樣需要架構/文件/測試/設計，沒有捷徑。
- 作者挑戰的預設：挑戰「AI Coding 加 agent 就能繞過工程基本功」「agent 出錯是模型問題」兩個慣性。
- 個人映射：高度濃縮版的「harness > 模型」結論，與 20260401、20260407、20260414 形成共識；「出錯怪流程不怪 agent」是個人友善的判斷口訣。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent 出錯時，怪流程不怪 agent——歸因方向決定改善路徑
- 分級：Core
- 類型：Heuristic
- 核心內容：當 agent 寫出爛 code，正確歸因不是「模型不夠強」，而是「你的 linting / typing / 測試不夠嚴格」。這個歸因方向決定了改善資源放在哪——不是換更貴的模型，而是補 harness。是組織心智模型的關鍵切換。
- 保留理由：一句口訣型 heuristic，可直接用在 team retrospective 與技術決策會議。
- 待補強處：邊界——是否有「真的就是模型問題」的情境？例如模型對某語言陌生？
- 初步知識鉤子：與 20260401「外圍系統不夠透明」、20260407 feedback controls、ToC 限制理論

序號 2
- 候選標題：重構與文件比寫新功能重要——AI 時代的優先級重排
- 分級：Core
- 類型：Principle
- 核心內容：在 AI Coding 時代，乾淨的架構與完整的文件是 agent 能否有效工作的「前提」而非「奢侈」。把工程實踐中常被擠壓的「重構/文件」拉到 P0，因為 agent 無法在混亂的程式碼上有效運作。對應 capture profile 的 ambient affordances / harnessability。
- 保留理由：與 20260327 Stripe 的 DX 飛輪、20260407 harnessability 完整對應，可形成主軸卡。
- 待補強處：在「資源有限的小團隊」情境下，如何拿捏「先建架構/文件 vs 先做產品」的順序？
- 初步知識鉤子：harnessability、與 20260327 Stripe DX 投資、與 20260414 Pang monorepo「為了 agent 可讀性」

序號 3
- 候選標題：完整循環：plan → autopilot → agent code review → 人工 review → 每週自動化檢查
- 分級：Core
- 類型：Pattern
- 核心內容：GitHub Copilot 內部的完整 AI 開發循環。每週再跑一次自動化檢查抓「測試缺漏、重複 code、文件落差」——這是把「品質債」從事件驅動轉為週期性巡檢的關鍵設計。多數團隊只做事件驅動 review，缺週期性巡檢。
- 保留理由：把 harness 從「事中控制」延伸到「週期性自我健康檢查」，補完 20260407 Fowler 的「持續迭代 harness」實作。
- 待補強處：每週檢查發現的問題如何回流？是否自動建工單？人類介入比例？
- 初步知識鉤子：與 20260414 Pang 的「每天 9:00 自動健康檢查 + 自動建 Linear 工單」、與 20260412 OpenAI 30 分鐘審查窗口

序號 4
- 候選標題：5 人 3 天產出 11 agent / 4 skill / 28,858 行——小團隊高槓桿產能基準
- 分級：Support
- 類型：Pattern
- 核心內容：當 harness 與流程到位，5 人團隊在 3 天內可產出 11 個 agent、4 個 skill、改 345 個檔案、+28,858 行。可作為「AI 優先團隊」產能的參考錨點。
- 保留理由：具體數字可作為向客戶/領導說服的素材；與 20260414 Pang「25 人 14 天每天 3-8 次部署」、20260327 Stripe「每週 1300 PR」形成數據群。
- 待補強處：產出物的品質、技術債、後續維護成本未交代；單看數字會誤導。
- 初步知識鉤子：與 20260327 Stripe、20260414 Pang 的產能數據群；需配 20260403 Junior Grit 危機作為對沖

## C. 建議送 refine 的項目
- 序號 1、2、3（Core，可獨立成卡）
- 序號 4 為 Support，建議與 20260327、20260414 合併成「AI 優先產能基準」對照卡

## D. 呼叫 refine-cards
- 將 4 張候選卡交由 refine-cards 精煉；序號 1、2 是高密度短卡的好範例；序號 3 與 20260414 高度相似需去重。
