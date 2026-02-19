看了 MCP Developer Summit 和 AI Engineer 



MCP Developers Summit: **<https://www.youtube.com/@MCPDevSummit>**

MCP: AI Engineer World's Fair 2025:<https://www.youtube.com/playlist?list=PLcfpQ4tk2k0UqhUyxuMMMmDwyiApd4sDw>



World's Fair 中關於 MCP 的 50+ 場演講(當然只是看逐字稿 AI 摘要啦，不然看錄影會有20+小時)，整理出 MCP 生態系的幾個重要發展趨勢:

 1\. MCP 協定持續進化

MCP 新推出兩個重要新功能:

\* Elicitation: 讓 MCP server 可以向 MCP client 請求用戶的額外資訊

\* Tool Structured Output: 可以定義工具的結構化輸出格式

相關演講:

\- MCP Project Update with Jerome Swannack, Member of Technical Staff at Anthropic

\- MCP Registry: Designing For Server Discovery Tadas A. (PulseMCP) Alex H.(Block), and Toby P.(GitHub) 這場討論官方 MCP Registry 的發展情況

除了新功能，也有一些早就存在但被忽視的規格受到關注。例如 Sampling 功能(我在五月的 MCP talk 有講到，可讓 MCP server 使用 MCP client 的 LLM)

相關演講:

\- MCP201: The Protocol in Depth with David Soria Parra at Anthropic

\- Resources: Building the Next Wave of MCP Apps with Shaun Smith, LLMindset

 2\. 企業級導入案例

\- Block 的全公司導入: 分享全公司導入 MCP 的經驗，最有趣的發現是「非技術人員比工程師更有創意！」甚至有非工程師自己 vibe code 了一個 MCP server (連 GitHub 帳號都沒有)。

\- Bloomberg 的大規模採用: 展示如何用 MCP 連接內部各種系統，讓 AI 能夠安全存取企業資料。他們特別強調資料安全和合規性的重要。

相關演講:

\- From Experiment to Enterprise: How Block Operationalized MCP at Scale - Angie Jones, Block

\- Pragmatic Scaling of Enterprise GenAI with MCP with Sambhav Kothari at Bloomberg

 3\. MCP Gateway 有超高需求

企業一旦開始導入 MCP，馬上就會發現需要 Gateway 來解決各種問題，如何管理內部眾多 MCP server 和工具，特別是安全與授權挑戰。因此希望能有單一的 MCP server 作為 Gateway 角色，統一入口管理。

\- WorkOS 分享從 [localhost](localhost) 到企業級的血淚史。身份驗證只是第一步，更難的是「AI workload 之間的授權傳遞」。還有各家推出 Gateway 方案百花齊放:

\- UCL 把 MCP 包成企業級 Gateway

\- Pomerium 用零信任架構包裝所有服務

\- A16Z 提出 Service Proxy 概念

\- Smithery、Fastn、Natoma 都推出託管方案

\- MCP Defender 的安全方案: 使用 Proxy 攔截所有流量，用 LLM 來保護 LLM

\- ScaleKit 提出 Auth 託管方案

\- Anthropic 工程師也分享了他們內部 MCP gateway 的經驗

相關演講:

\- What MCP Middleware Could Look Like with Yoko Li from A16Z

\- Fastn UCL: Secure & Scalable MCP for Enterprise AI Deployments | Khalid Muaydh, Fastn

\- Agentic Access: OAuth Isn't Enough | Zero Trust for AI Agents w/ Nick Taylor (Pomerium + MCP)

\- Tool Calls Are the New Clicks: Henry Mao on Building Smarter AI Agents with MCP

\- Enterprise-Ready MCP: Hosted Solutions for Scale, Security & Real-World Use | Paresh Bhaya, Natoma

\- How to Add OAuth to MCP Servers in 4 Steps — Ravi Madabhushi, Scalekit

\- Securing AI Apps with MCP Defender — Sundeep Gottipati

\- What does Enterprise Ready MCP mean? — Tobin South, WorkOS

\- Remote MCPs: What we learned from shipping — John Welsh, Anthropic

非常多公司都在做 Gateway 這個題目，顯示這是真實且迫切的需求。

 4\. 工具太多成為核心挑戰

當你有幾百甚至幾千個工具時，AI 會選擇困難。各家提出不同解法:

\- VS Code 的工具管理策略: 動態使用者在每個對話中有不同工具子集，還能自訂工具組合（toolsets）

\- Block 的洋蔥式架構: 把工具分成三層 - 發現層、規劃層、執行層。先用一個工具來探索有哪些 API 可用，再用另一個工具取得詳細參數，最後才執行。有點像是「先問有什麼菜 → 再問怎麼做 → 最後才點菜」的概念。

\- Appify 的動態載入: 他們有 4000+ 個工具！解法是用 MCP 的 toolListChanged 通知機制，根據使用者需求動態載入工具。比如說使用者想爬 LinkedIn，系統才去找相關的爬蟲工具加進來。

\- 向量搜尋方案: 把所有工具描述先做成 embeddings，當使用者輸入 prompt 時，用相似度搜尋找出最相關的工具，再用 reranker 排序。這樣就不用一次載入所有工具。

相關演講:

\- Too Many Tools? How LLMs Struggle at Scale | MCP Talk w/ Matthew Lenhard

\- Full Spec MCP: Hidden Capabilities of the MCP spec — Harald Kirschner, Microsoft / VSCode

 5\. 從工具思維到 Agent 思維

這是重要的開發典範轉移: 不要只是把 API 端點一對一變成 MCP工具！你會有三個用戶: 終端用戶、client app 開發者，還有 AI 本身。要思考使用者會問什麼問題，然後設計適合的工具介面。

MCP-first 開發: 與其先做 REST API 再包裝成 MCP，不如一開始就為 AI 設計。當 AI 成為主要使用者時，系統設計的思維要完全改變。

相關演講:

\- Scaling Enterprise MCP: Best Practices, Nexuses, and Security with Pat White

\- MCP Is Not Good Yet — David Cramer, Sentry

 6\. 標準化之爭

LlamaIndex 的 Laurie Voss 比較了 14 個 Agent 通訊協議。Google 的 A2A (Agent-to-Agent) 已經加入 Linux Foundation，確保技術中立性。

關鍵問題: 「呼叫工具」和「呼叫 Agent」到底有什麼差別？A2A 說差別在於 Agent 可能需要很長時間回應（甚至幾天），所以內建了非同步機制。但講者認為這差異並不大，而且 MCP 也即將支援非同步。

\> 編按: 你可以將 Agent 包在 Tool 裡面，呼叫工具就是傳訊息給裡面的 Agent。我在我之前的 MCP talk 就有提到這招。

現實很殘酷: 這 14 個協議大多「半生不熟」，真正有採用率的只有 MCP。為什麼？因為 MCP 選擇先解決一個小而具體的問題，證明了自己的價值。就像 React 當年征服前端世界一樣。結論是犀利的: 「MCP is all we need」。

相關演講:

\- MCP vs ACP vs A2A: Comparing Agent Protocols with Laurie Voss from LlamaIndex

\- A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench




