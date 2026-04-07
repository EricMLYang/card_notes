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
