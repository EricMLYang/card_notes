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
