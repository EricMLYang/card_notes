---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
# Demystifying evals for AI agents — Anthropic

> 來源：Anthropic Engineering
> 來源類型：官方事實 + 高密度觀點
> 需求層：知識建構
> 連結：https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
> 搜集日期：2026-04-12
> 搜集原因：K4 — AI Agent 工程化落地開始從「比模型」轉成「比 eval harness、grader 設計、回歸控制」

## 摘要

這篇是 Anthropic 在 2026-01-09 發表的 agent eval 方法文，價值不在於單一 benchmark，而在於它把 agent eval 拆成可以工程化執行的零件：task、trial、grader、transcript、outcome、evaluation harness、agent harness。對你最有用的地方是，它明確把「agent 能力」和「agent scaffold / harness」綁在一起評估，而不是只評模型。

文中也把 grader 分成 code-based、model-based、human 三類，並進一步區分 capability eval 與 regression eval，這很適合拿來整理你一直在想的那條主線：AI Agent 一旦進 production，真正稀缺的不只是 prompt 或模型，而是你怎麼定義成功、怎麼抓退步、怎麼讓產品團隊與研究團隊有共同語言。

更關鍵的是，Anthropic 明講早期不用等到幾百筆資料才開始做 eval。從 20-50 個真實失敗案例起步就夠，先把手動測的東西變成測試集，之後再逐步擴大。這和你關注的小團隊落地條件非常一致。

## 為什麼值得看

這篇文章把 eval 從「研究團隊才做的事」拉回產品與工程團隊的日常工作，對資料 Agent、分析 Agent、coding agent 都有直接參考價值。

它也強調一個很重要的判準：當你說在評估「agent」時，實際上是在評估 `模型 + harness + tools + environment` 的組合，而不是孤立模型。這剛好可以支撐你對 harness、context、verification 一直在寫的主張。

另一個值得注意的點是 non-determinism。文中用 `pass@k` 與 `pass^k` 區分「試幾次有一次成功」和「每次都穩定成功」，這對企業內部 agent 尤其重要，因為很多場景真正要的不是偶爾很強，而是每次都不失手。

## 可能偏誤或限制

這是 Anthropic 自家的方法論整理，會偏向 Claude / Claude Code 的實務脈絡，對其他 agent stack 的細節未必完全等價。

文章偏方法框架，不是實測數據報告；它提供的是設計思路，不是直接可搬用的完整模板。實際落地時，還是要依你的 agent 類型補足 domain-specific graders。

另外，文中示例橫跨 coding、support、research、computer use，廣度很高，但也因此不會深入到資料治理、business semantics 或 decision system 的專門問題。

## 潛在卡片方向

- Agent eval 的評估對象其實不是模型，而是 `model + harness + environment`
- Capability eval 與 regression eval 是兩種不同管理問題
- 小團隊做 agent eval 的最小起點：20-50 個真實失敗案例就夠
- `pass@k` 與 `pass^k` 分別對應「找到答案」與「穩定可靠」
- 可連結的現有卡片：[[AI時代評估能力成為關鍵槓桿點]]
- 可連結的現有卡片：[[AI Error Analysis：LLM 應用評估方法]]
- 可連結的現有卡片：[[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]

---

## 全文重點整理

以下為依原文重寫的中文整理，非逐字全文翻譯。

Anthropic 先指出，agent 之所以難評估，是因為它們不是單回合回答問題，而是會多輪互動、呼叫工具、改變環境狀態，錯誤也會沿著流程累積。這使得傳統單輪 prompt-response 的 eval 已經不夠。

文章把評估拆成幾個最重要的元件：

- `task` 是單一測試題與成功條件
- `trial` 是同一題的一次嘗試
- `grader` 是給結果打分的邏輯
- `transcript` 是整段軌跡與中間推理、工具使用紀錄
- `outcome` 是環境最終狀態，而不只是 agent 最後說了什麼
- `evaluation harness` 是整套執行 eval 的基礎設施
- `agent harness` 則是讓模型能作為 agent 行動的 scaffold

這個區分很重要，因為它提醒你：當 agent 表現不好時，問題可能在模型，也可能在 scaffold、tooling、task 設計或 grader 本身。

grader 的部分，Anthropic 建議混用三類：

- code-based grader：快、便宜、可重現，但容易對合理變體太脆弱
- model-based grader：能處理開放式任務與細膩標準，但成本較高，也需要人工校準
- human grader：最準，但最慢最貴，適合校準或抽樣

他們還區分兩種 eval：

- capability eval：看 agent 現在能不能做到某件事，應該故意選比較難、目前通過率不高的題目
- regression eval：看 agent 有沒有退步，應該維持接近 100% 的通過率

一旦 capability eval 的題目變成熟、穩定高通過率，就可以升格成 regression suite。這個想法很適合產品化團隊，因為它讓「新功能探索」和「品質守門」變成同一套系統的不同階段。

對 coding agents，Anthropic 的建議很務實：核心還是穩定測試環境與明確的 pass/fail tests，但如果只看測試是否通過，會漏掉很多工具使用品質、過度工程、互動方式等問題，所以仍應搭配 transcript grading。

對 research agents，文章提醒一個你很會共鳴的點：研究品質往往沒有單一正解，因此 groundedness、coverage、source quality、human calibration 都要一起上，而不是只問「答對了沒」。

最後一段最值得做成操作框架：

1. 越早開始做 eval 越好
2. 先把本來手動驗證的案例收進來
3. 題目要寫得沒有歧義，並準備 reference solution
4. 從真實失敗案例擴充資料集，而不是先追求龐大數量

這篇的真正價值是把 eval 從抽象口號，降成一套產品與工程團隊可以持續執行的工作流。

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Agent eval 難在多輪互動 + 工具呼叫 + 環境狀態變化會讓錯誤累積，傳統單輪 prompt-response eval 不夠。Anthropic 把 eval 拆成可工程化的零件：task / trial / grader / transcript / outcome / evaluation harness / agent harness。Grader 分 code-based / model-based / human 三類；Eval 分 capability eval（看能不能做到、可挑難題）與 regression eval（看有沒有退步、保持高通過率）。最有用的落地原則：從 20-50 個真實失敗案例起步，不必等大資料集。
- 作者挑戰的預設：（1）Eval 是研究團隊才做的事 → Eval 是產品與工程團隊的日常工作；（2）評 Agent 等於評模型 → 評 Agent 是評 model + harness + tools + environment 的組合；（3）需要大量資料才能開始 → 20-50 個真實失敗案例就夠；（4）pass@k 就夠 → 在企業場景需要 pass^k（穩定性）才是真關鍵。
- 個人映射：直接補強你的「AI 時代評估能力是關鍵槓桿點」「Harness 是把模型變成 Agent 的關鍵」主軸；把「20-50 案例起步」這個你之前沒明寫的可操作門檻補上；pass@k vs pass^k 的區分對你關心的「production agent 的可靠性」是關鍵語言工具。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent Eval 的對象是 Model + Harness + Tools + Environment 的組合
- 分級：Core
- 類型：Principle
- 核心內容：當你說在評估 agent 時，實際上在評估「模型 + agent harness + tools + environment」的組合，而不是孤立模型。這個區分很重要，因為 agent 表現不好時，問題可能在模型、scaffold、tooling、task 設計或 grader 本身。任何 eval 報告若沒明說 stack 邊界，都會誤導判斷。
- 保留理由：這是和 Stripe 那篇完全互為佐證的核心命題；對你長期主張的「Harness Engineering」直接 load-bearing。
- 待補強處：當 eval 結果不好時，如何分離歸因到 stack 的哪一層？是否有 ablation 設計範式？
- 初步知識鉤子：[[Harness Engineering]]、[[Stripe Benchmark Stack]]、[[Agent Stack 評估]]

序號 2
- 候選標題：Capability Eval vs Regression Eval：兩種不同的管理問題
- 分級：Core
- 類型：Principle
- 核心內容：Capability eval 看 agent 現在能不能做到某件事，應該故意選比較難、目前通過率不高的題目；Regression eval 看 agent 有沒有退步，應該維持接近 100% 通過率。一旦 capability eval 的題目穩定高通過率，就可以升格成 regression suite。這個設計讓「探索新功能」和「品質守門」變成同一套系統的不同階段。
- 保留理由：把 eval 從「打分工具」抬升到「持續演化的測試資產管理」；對你做 agent product team 的工作流設計很實用。
- 待補強處：升格的觸發門檻（連續多少次達 95%？）？退役機制？
- 初步知識鉤子：[[Eval Suite Lifecycle]]、[[Capability vs Regression]]、[[CI for Agents]]

序號 3
- 候選標題：20-50 個真實失敗案例：小團隊 Agent Eval 的最小起點
- 分級：Core
- 類型：Heuristic
- 核心內容：早期不用等到幾百筆資料才開始做 eval。從 20-50 個真實失敗案例起步就夠——先把手動驗證的東西收進測試集，題目寫得無歧義並準備 reference solution，再從真實失敗逐步擴大。這把「eval 必須先大規模才有意義」的隱性門檻拆掉了。
- 保留理由：直接給出可操作的最小起點；對你關心的「小團隊資源約束下做 BDS / Agent productization」是核心拼圖。
- 待補強處：題目「無歧義」的具體寫法 / 範例？reference solution 的最小規格？什麼算「真實失敗」？
- 初步知識鉤子：[[小團隊資源約束]]、[[手動測試 → 自動化]]、[[Reference Solution 設計]]

序號 4
- 候選標題：Pass@k vs Pass^k：找到答案 vs 穩定可靠的本質差別
- 分級：Core
- 類型：Principle
- 核心內容：`pass@k` 表示試 k 次至少有一次成功；`pass^k` 表示連續 k 次每次都成功。前者衡量「能不能找到答案」，後者衡量「穩定可靠」。研究 benchmark 多用 pass@k，但企業內部 agent 真正要的不是偶爾很強，而是每次都不失手——pass^k 才是 production 場景的真關鍵。
- 保留理由：給出一個非常 sharp 的概念區分，可直接套用到產品決策（什麼任務可接受 pass@k、什麼必須 pass^k）。
- 待補強處：在實作上，pass^k 達到多少 k 才算 production-ready？非確定性壓到多少才算「夠穩」？
- 初步知識鉤子：[[Production Reliability]]、[[Non-determinism]]、[[Decision System 容錯]]

序號 5
- 候選標題：三類 Grader 混搭：Code / Model / Human 各自的取捨
- 分級：Support
- 類型：Heuristic
- 核心內容：Code-based grader 快、便宜、可重現，但對合理變體脆弱；Model-based grader 能處理開放式任務與細膩標準，但成本較高、需人工校準；Human grader 最準但最慢最貴，適合校準或抽樣。生產級 eval 應混用三類，而非選一個。
- 保留理由：是設計 eval 系統的實作判準；可遷移到任何 agent 類型（coding、analysis、research）。
- 待補強處：三類混搭的成本配比？哪些任務應主要用哪一類？
- 初步知識鉤子：[[Grader 設計]]、[[Eval Cost-Quality Tradeoff]]、[[Model-Based Grader 校準]]

序號 6
- 候選標題：Outcome ≠ Final Message：Agent Eval 應看環境最終狀態
- 分級：Support
- 類型：Principle
- 核心內容：Outcome 是環境最終狀態，不只是 agent 最後說了什麼。Agent 可能說「任務完成」但環境裡實際資料沒寫進去；或者口頭說失敗但實際結果是對的。Eval 必須檢查環境狀態而不是 final message，這呼應 Stripe 用「實際建立的 Stripe object」做驗證的設計。
- 保留理由：把一個常被忽略的 eval 設計細節明確化；對你做 BDS / decision system 的 eval 設計很實用（state-based vs message-based 驗證）。
- 待補強處：state 抽取 / 比對的設計範式？環境狀態複雜時如何定義「成功狀態」？
- 初步知識鉤子：[[State-Based Verification]]、[[Stripe Grader Design]]、[[Eval Design Pattern]]

## C. 建議送 refine 的項目
- 序號 1（Core）：Eval 對象是 Stack 組合
- 序號 2（Core）：Capability vs Regression Eval
- 序號 3（Core）：20-50 案例最小起點
- 序號 4（Core）：Pass@k vs Pass^k
- 序號 5（Support）：三類 Grader 混搭
- 序號 6（Support）：Outcome 是環境狀態

## D. 呼叫 refine-cards
- 上述 6 張候選卡交由 refine-cards 精煉；refine 階段重點：序號 1 必須與 Stripe Benchmark 序號 1 合併或互為案例；序號 2、4、5、6 可組成「Agent Eval 工程化四件套」連結串。建議在卡片內互相引用形成主題群。

