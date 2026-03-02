AI 寫的 code 越來越多，怎麼確保不會把架構搞爛？

Pragmatic Engineer 的 Gergely Orosz 深度拆解了 OpenAI Codex 團隊的做法：Harness Engineering

核心概念：用機械式規則強制架構一致性，而不是靠 code review 或人的紀律

具體做法是定義嚴格的單向依賴鏈：
Types → Config → Repo → Service → Runtime → UI
每一層只能依賴上一層，違反就自動擋掉

這樣不管是人寫的還是 AI 寫的 code，都不可能破壞架構

另一個有趣的點：Codex 團隊分成 CLI 團隊和 Web 團隊雙軌並行，各自獨立迭代但共用底層協議

當 AI agent 每天產出上千行 code，架構守護不能靠人，要靠 harness

🔗 newsletter.pragmaticengineer.com/p/how-codex-is-built

#SoftwareArchitecture #HarnessEngineering #AI #Codex