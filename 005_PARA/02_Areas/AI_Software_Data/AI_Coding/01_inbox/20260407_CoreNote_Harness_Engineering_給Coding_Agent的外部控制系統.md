---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# Harness Engineering：給 Coding Agent 的外部控制系統

> 來源：Martin Fowler
> 連結：https://martinfowler.com/articles/harness-engineering.html
> 搜集日期：2026-04-07
> 搜集原因：AI Coding 工程化、Agent 驅動框架、測試與控制介面

## 摘要
Birgitta Böckeler 在 2026-04-02 發表這篇文章，核心不是再談「模型變強」，而是談當 Agent 要少一點人盯、能多做一點事時，工程團隊應該補什麼控制層。她把 coding agent 的可靠性拆成 feedforward guides 與 feedback sensors，並進一步區分 deterministic 的 computational controls 與語意判斷型的 inferential controls。這很貼近你在想的事：真正的槓桿不在 prompt 技巧，而在能不能把 repo、測試、規則、靜態分析與 review 變成一套可持續迭代的 harness。文章還把「harnessability」拉到更高一層，指出有些 codebase 天生更容易被 agent 駕馭，這其實就是 AI 時代的架構競爭力。

## 潛在卡片方向
- Harness 不是模型外圍裝飾，而是讓 Agent 可被信任地工作的外部控制系統。
- Feedforward + feedback 要一起設計，否則不是一直重犯同樣錯，就是寫了一堆規則卻不知道有沒有效。
- 「Keep quality left」在 Agent 時代更重要，因為越晚發現問題，修正成本與 review 負擔越高。
- Ambient affordances 與 harnessability 可以作為評估 repo 是否適合 AI coding 的新判準。
- 可連結的現有卡片：[[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]、[[測試套件是 Agentic Engineering 的核心槓桿點]]、[[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]]

---

## 全文翻譯

作者開場先處理一個很實際的問題：如果我們想讓 coding agent 少一點 supervision，就必須提高自己對輸出的信心。工程師對 AI 產生的程式碼天然有一道 trust barrier，因為 LLM 非決定論、不理解真實脈絡，也不真的「懂」程式，只是在 token 上運作。這篇文章想提供一個心智模型，把 context engineering 與 harness engineering 放進同一張圖裡，幫助團隊建立信任。

她先縮小「harness」這個詞的範圍。廣義上，harness 指的是 Agent 中除了模型本身之外的所有東西；但對 coding agent 的使用者來說，更關鍵的是你能不能在 agent 之外，再搭一層屬於你自己團隊的外部 harness。這層外部 harness 的目標有兩個：第一，提高 agent 第一次就做對的機率；第二，在人看到結果之前，盡可能讓問題透過回饋循環自我修正掉，減少 review toil，也減少浪費 token。

文章接著把控制拆成兩類。第一類是 guides，也就是 feedforward controls，重點在 agent 動手前就先導向正確方向，例如 AGENTS.md、skills、how-to 文件、結構規範、codemods。第二類是 sensors，也就是 feedback controls，重點在 agent 動作之後提供訊號，讓它知道哪裡要修，例如 linters、tests、type checks、review agents、logs、browser-based checks。作者認為這兩者缺一不可。只有 feedback，agent 可能只是反覆犯同樣錯；只有 feedforward，則只是把規則塞進去，卻無法知道它有沒有真的生效。

再往下一層，她把 guides 和 sensors 分成 computational 與 inferential 兩種執行類型。Computational controls 是 CPU 型、快、便宜、可重複、結果穩定的控制，例如 tests、linters、type checkers、結構檢查。Inferential controls 則是 LLM judge、AI code review、語意分析這類偏語意判斷的控制，速度慢、成本高、結果也更不穩定，但能補上 deterministic 工具抓不到的語意品質與上下文適配問題。她的重點不是二選一，而是兩者需要協同：能 deterministic 的就盡量 deterministic，真正需要語意判斷的地方才交給 inferential controls。

在人機分工上，作者把「human steering loop」說得很精準。人類的工作不是每次都重新從頭盯著 agent，而是持續迭代 harness。當同一類錯誤反覆出現時，應該回頭調整 guides 或 sensors，讓這類錯誤未來更不容易再發生。更有意思的是，AI 本身也可以拿來幫忙改善 harness，例如生成結構測試、草擬新規則、補上 custom linter、根據 codebase archaeology 寫出 how-to guides。也就是說，agent 不只是被 harness 控制，它也能幫忙擴建 harness。

在流程配置上，作者延續 continuous integration / continuous delivery 的邏輯，主張把品質檢查盡可能往左移。哪些檢查夠快，可以在 commit 前甚至編碼途中就跑；哪些檢查比較貴，適合放在 integration 後的 pipeline；哪些 drift 會慢慢累積，需要持續在 repo 或 runtime 上長期監測。她把這些 controls 分散到整個 change lifecycle 中，讓 agent 的自我修正不只發生在單次對話裡，而是嵌進整個 delivery flow。

文章中還有一個很有價值的概念叫 harnessability。不是每個 codebase 都一樣適合被 harness。強型別語言天然帶來 type-checking 這種 sensor，清楚的 module boundary 允許你寫 architecture fitness rules，而成熟框架能把很多 agent 不該操心的細節抽掉。這些特性會直接提高 agent 成功率。相反地，legacy system 因為債多、邊界模糊，往往是最需要 harness 的地方，同時也是最難建 harness 的地方。

作者的同事 Ned Letcher 把這類讓環境更可治理的特性稱為 ambient affordances，也就是環境本身的結構特性，讓 agent 能更容易讀懂、導航與操作。這個概念很值得移植到 AI coding 的 repo 設計上：良好的目錄結構、明確的模組邊界、穩定的命名、可執行的測試入口、清楚的 conventions，都是在提高 repo 對 agent 的 legibility。

她還提出 harness templates 的方向。很多企業其實只有幾種常見服務拓樸，例如 CRUD business service、event processor、data dashboard。如果這些拓樸本來就有 service templates，未來很可能會進一步演化成 harness templates，把 guides 與 sensors 一起打包成可複用的控制組件。團隊甚至可能會反過來根據現有 harness 的成熟度來選 tech stack 與結構。

最後一節回到 human role。人類開發者本身其實一直是隱性的 harness：我們吸收過慣例、感受過複雜度、知道技術債什麼時候能忍、也知道團隊現在真正要的是什麼。問題是這些 implicit harness 多半沒被顯性化。作者的觀點並不是把人拿掉，而是把這些隱性判斷逐步外化成 guides、sensors 與環境結構，讓人類能從反覆盯人，轉向持續設計控制系統。

整篇文章最重要的訊號是：對 coding agent 使用者來說，外部 harness 不是一次性設定，而是一項持續的工程實踐。未來真正有競爭力的，不只是誰用到更強的模型，而是誰更快把團隊的品質標準、架構原則、測試能力與 review 判準，變成 agent 能讀、能被約束、能被回饋的工作系統。

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Fowler/Böckeler 把 coding agent 的可靠性問題形式化為一個雙軸 framework：feedforward guides ↔ feedback sensors，computational ↔ inferential controls。提出 harnessability 與 ambient affordances 概念，把 AI Coding 競爭力從「模型能力」推向「環境結構可被治理的程度」。人類角色從盯人轉向持續設計控制系統。
- 作者挑戰的預設：挑戰「prompt 技巧/模型強度=agent 強度」「harness 是一次性設定」兩個慣性；把 harness 提升到產品工程實踐層次。
- 個人映射：本文是 capture profile「Harness / 驅動框架視角」「平台化能力模組」「Repo-as-Worker」的理論骨架；可作為總引用源。harnessability 概念可遷移到評估自家 / 客戶 repo 的 AI-readiness。

## B. 候選卡（Lite）

序號 1
- 候選標題：外部 Harness 雙目標：提高首次正確率 + 在人看到前自我修正
- 分級：Core
- 類型：Principle
- 核心內容：在 agent 之外搭一層屬於團隊的外部 harness，目標有二：(1) 提高 agent 第一次就做對的機率（feedforward）；(2) 在人類看到結果前，讓問題透過回饋循環自我修正（feedback），減少 review toil 與 token 浪費。這是 harness 設計的成本/品質雙重優化目標。
- 保留理由：給 harness 投資一個明確的成本/品質衡量框架，可作為提案 ROI 計算的基礎。
- 待補強處：兩個目標在資源衝突時優先順序？例如增加 feedback 會增加運行成本。
- 初步知識鉤子：與 20260401 評估迴圈、20260404「出錯怪流程」、Toyota Andon Cord

序號 2
- 候選標題：Guides（feedforward）vs Sensors（feedback）——兩者缺一不可
- 分級：Core
- 類型：Principle
- 核心內容：Guides 是動手前的方向控制（AGENTS.md、skills、how-to、結構規範、codemods）；Sensors 是動作後的訊號（linters、tests、type checks、review agents、logs、browser checks）。只有 feedback：反覆犯同樣錯；只有 feedforward：規則塞進去卻不知道生效沒。兩者構成完整控制迴圈。
- 保留理由：是 harness 設計的最高層分類，可遷移到知識管理（卡片寫作 guides + 審查 sensors）、寫作 pipeline 等任何 agentic workflow。
- 待補強處：當 guides 與 sensors 衝突時（例如 guide 要 X，sensor 抓到 X 失敗），如何處理？
- 初步知識鉤子：feedforward / feedback control（控制理論）、與 20260401 評估迴圈、20260403 CLAUDE.md（屬 guides）、20260404 完整循環

序號 3
- 候選標題：Computational vs Inferential Controls——能 deterministic 就盡量 deterministic
- 分級：Core
- 類型：Heuristic
- 核心內容：Computational controls（tests、linters、type checkers、結構檢查）= CPU 型，快、便宜、結果穩定；Inferential controls（LLM judge、AI code review、語意分析）= 慢、貴、結果不穩定，但能補語意品質。判準：能用 deterministic 工具的就用，真正需要語意判斷再交給 inferential。避免「LLM judge everywhere」的誤用。
- 保留理由：對「AI 審 AI」浪潮提供成本/可靠性的取捨判準，是非常實用的工程 heuristic。
- 待補強處：哪些任務天生屬於 inferential（無法 deterministic）？需要邊界清單。
- 初步知識鉤子：cost economics、與 20260403 三道平行 AI 審查（屬 inferential）、與 20260412 OpenAI GPT-5.4 監控（inferential 但近即時）

序號 4
- 候選標題：Harnessability 是 AI 時代的新架構競爭力
- 分級：Core
- 類型：Pattern
- 核心內容：不是每個 codebase 都同樣適合被 harness。強型別語言天然帶來 type-checking sensor；清楚 module boundary 允許 architecture fitness rules；成熟框架抽掉 agent 不該操心的細節。harnessability 高的 repo 直接讓 agent 成功率上升。Legacy 系統最需要 harness 但最難建——典型「窮者越窮」結構。
- 保留理由：把架構決策的長期效益重新定價——選 stack 不只看人類生產力，還看 agent 可治理性。
- 待補強處：如何快速評估一個 repo 的 harnessability 分數？需要 checklist。
- 初步知識鉤子：技術選型、與 20260327 Stripe DX 飛輪、與 20260414 Pang monorepo 為了 agent 可讀性、與 20260401 skill graph 可讀性

序號 5
- 候選標題：Ambient Affordances——環境的隱性可治理性
- 分級：Core
- 類型：Pattern
- 核心內容：Ned Letcher 提出的概念：環境本身的結構特性讓 agent 更容易讀懂、導航與操作。具體包含良好的目錄結構、明確的模組邊界、穩定的命名、可執行的測試入口、清楚的 conventions。重點是「隱性、無需教 agent 的環境訊號」。可遷移到任何 agentic workflow 的環境設計。
- 保留理由：把「對 AI 友善的環境」從直覺變成可設計的概念，呼應 capture profile 的「對開發者好的東西對 AI 也好」。
- 待補強處：與 explicit guides（AGENTS.md）的取捨？什麼時候用 ambient、什麼時候用 explicit？
- 初步知識鉤子：affordance（Don Norman）、與 20260327 Stripe DX、與 20260401 skill graph 可讀性

序號 6
- 候選標題：Human Steering Loop——人類角色從盯人轉向持續設計 harness
- 分級：Core
- 類型：Principle
- 核心內容：人類的工作不是每次重新從頭盯 agent，而是持續迭代 harness。當同一類錯誤反覆出現，回頭調整 guides/sensors，讓這類錯未來不易再發生。AI 本身可幫忙改善 harness（生成結構測試、草擬規則、補 linter、寫 how-to）——agent 不只被 harness 控制，也能擴建 harness。
- 保留理由：是工程師角色重定位的核心 framing，呼應 20260414 Pang「架構師 vs 操作員」、20260403「導演」隱喻。
- 待補強處：個人時間如何分配在「修錯」vs「迭代 harness」？比例參考？
- 初步知識鉤子：與 20260403 CLAUDE.md 迭代、與 20260414 Pang 架構師角色、人類隱性 harness 顯性化

序號 7
- 候選標題：Harness Templates——可複用的服務拓樸控制組件
- 分級：Question
- 類型：Question
- 核心內容：作者預測企業常見的服務拓樸（CRUD business service、event processor、data dashboard）會從 service templates 演化成 harness templates，把 guides 與 sensors 一起打包。團隊甚至會反過來根據 harness 成熟度選 tech stack。值得追蹤這個趨勢。
- 保留理由：未來 1-3 年的趨勢追蹤點，可能影響 data product / decision system 平台化路線。
- 待補強處：目前是否已有早期 harness template 案例？
- 初步知識鉤子：與 capture profile「平台化能力模組」「從專案到產品的演進」、Cookie cutter / Yeoman 類比

## C. 建議送 refine 的項目
- 序號 1、2、3、4、5、6（Core，皆為高密度概念卡）
- 序號 7 為 Question 卡，保留追蹤

## D. 呼叫 refine-cards
- 將 7 張候選卡交由 refine-cards 精煉；本文是 harness 主題的「理論骨架」，refine 時建議優先保留 Fowler 原始命名（feedforward/feedback、computational/inferential、harnessability、ambient affordances）作為連結節點。與 20260401、20260414 必有合併與引用關係。

