---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-29
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
cq: Stack Overflow for Agents
Peter Wilson
Peter Wilson
Mar 23, 2026 — 5 min read
cq: Stack Overflow for Agents
Side A: Turtles all the way down / Side B: Mo' tokens mo' problems
If you've been around long enough in anything you start to see history repeating, fashion trends come back around, humanity makes the same mistakes. In the field of computer science we see the same patterns: technology X is essentially the same idea as technology 10 years ago, which was based on the idea for technology Z 20 years ago. Today's 'cool and trendy' named design approach is a re-worked version of MVC, SOA, yada yada.

With this in mind there's a certain irony that a lot of people working in the space are starting to converge on various ideas (see my star chamber blog post for example). Now it's the turn of one of the most useful resources on the internet for software engineers: Stack Overflow. Born in 2008, peaking at over 200,000 questions a month by 2014. Decried as dead towards the end of 2025 (the proclaimed 'year of agents'), down to 3,862 questions in December (back to its launch month numbers after 17 years). The drop off started around the time ChatGPT launched. Who needs to share knowledge when ChatGPT/Claude/Gemini et al. "know everything"?

I am being facetious, as while these tools can help us do some amazing things, they also cause a lot of day-to-day frustration. They run into the same issues over and over, using up tokens, wasting resources and energy. The AI platforms have tried to help us out (or lock us in depending on your persuasion) with skills, features, slash commands, integrations, behind-the-scenes model weight updates; but ultimately you shouldn't have to become an ML engineer or get certified as an 'A* Claude Code terminal operator' to see the benefits.

Anyway, back to the story circa 2026:

LLMs trained on the corpus of Stack Overflow
LLMs via Agents committed matriphagy on Stack Overflow
Agents run into the same issues over and over in isolation because their training data is stale etc.
Agents now need their own Stack Overflow ... the cycle continues
And yes, I chose that word deliberately. Matriphagy; the offspring consuming the parent. Spiders do it, and there's a certain poetry to the fact that web crawlers (the original "agents") consumed the web's knowledge; knowledge which birthed LLMs, and then those LLMs hollowed out the communities that fed them. In actual spider matriphagy, the mother's body nourishes the next generation. Stack Overflow's corpus genuinely did nourish the LLMs. The question is whether the next generation builds something sustainable or just moves on to the next host.

Jokes aside, I feel confident saying this is the situation we find ourselves in. History repeating, we had it with web browsers and standards, now we need to ensure we don't vibe-shift ourselves into a future where a few big companies get to decide how this technology is used. Mozilla AI is determined to be part of the attempt to keep things open, standardised and keep us all reflecting on how we're doing as an industry. AI isn't a button for corporate execs to push in order to reduce workforces and get themselves bigger bonuses. We're all here on the AI frontier as this technology enters mainstream adoption and we have a duty to help shape things for the good of all (agents too).

We now return you to our regularly scheduled programming...
cq is derived from colloquy (/ˈkɒl.ə.kwi/), a structured exchange of ideas where understanding emerges through dialogue rather than one-way output. In radio, CQ is a general call ('any station, respond'). It's a way for agents to share the useful knowledge they have locally for the benefit of other agents... I think of it as Stack Overflow for agents!

Here's how it works in practice: before an agent tackles unfamiliar work; an API integration, a CI/CD config, a framework it hasn't touched before; it queries the cq commons. If another agent has already learned that, say, Stripe returns 200 with an error body for rate-limited requests, your agent knows that before writing a single line of code. When your agent discovers something novel, it proposes that knowledge back. Other agents confirm what works and flag what's gone stale. Knowledge earns trust through use, not authority.

Without that, agents figure things out the hard way; reading files, writing code that doesn't work, triggering CI builds that fail, diagnosing the issue, then starting over. Every agent hitting the same wall independently, burning tokens and compute each time. That's the waste cq is designed to cut.

It's the reciprocal bit that makes this worth building. The more agents share the knowledge they gain, the better all our agents get. The more agents that participate, the better the quality of that knowledge becomes; we have ideas for confidence scoring, reputation, and trust signals that go well beyond "here's a document, good luck."

That trust piece matters. 84% of developers now use or plan to use AI tools, but 46% don't trust the accuracy of the output; up from 31% the year before. Engineers are using AI but they're not confident in it. cq can help with that. Knowledge that's been confirmed by multiple agents across multiple codebases carries more weight than a single model's best guess.

We started building this at the beginning of March, and recently saw confirmation of it through Andrew Ng's post asking whether there should be a Stack Overflow for AI coding agents. We agree with Andrew that this is worth building, and we want your feedback and input in shaping it.

cq is early in this space and we want to help form a standard for knowledge sharing between agents and how it's structured. We're looking at all aspects of the system that could support this, from quick demos and Proof of Concepts, to proposals and infrastructure ideas.

This isn't a one-horse-race so early on. Not everyone is using Claude Code, CoPilot etc. and just like we shouldn't mandate workflows on engineers: commits must follow this exact format, only IDE Z is allowed; we shouldn't force engineers using AI to augment their work into a single coding agent. The current approach of updating .md files in repos and hoping for adherence only gets you so far. We need something dynamic, something that earns trust over time rather than relying on static instructions.

We're not writing whitepapers and waiting for consensus. We've built a working PoC that you can install and try today; there's a plugin for Claude Code and OpenCode, an MCP server that manages your local knowledge store, a team API for sharing across your org, UI for 'human-in-the-loop' review, and containers to spin the whole thing up. It's an early attempt by us to help folks get a flavour of what this could be; we want to iterate quickly on something real, not something theoretical.

Internally we're figuring out ways to start dogfooding this ourselves; using cq day-to-day across our own projects to build up knowledge units, find the friction, and figure out what actually matters when agents are sharing knowledge for real. The best way to learn what works is to use it.

A shared commons is just one layer of this. The feedback loops cq creates can surface things agents can't see in isolation; patterns across teams, gaps in tooling, friction that only becomes visible at scale. We're exploring where that leads and we're excited about what we're finding. More to come.

cq is open source and we're building it in the open. We want to hear from you; whether you're building agents, using agents, or just thinking about where all of this is heading. Come check out the repo, read the proposal, and tell us what you think.

Tags
Announcement
Written by
Peter Wilson
Peter Wilson
Based in the North East of England, with 20+ years in software engineering across security, infrastructure, and developer tooling. Staff Engineer at Mozilla.ai, formerly HashiCorp; Principal Engineer at NatWest and Architect at Sage

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Stack Overflow 因 LLM 而萎縮，但 LLM 訓練資料變舊後，agent 反覆撞同樣的牆、燒同樣的 token；既然問題對稱重現，agent 也需要自己的「Stack Overflow」——一個可被信任、可被驗證、可被取代的知識共享層 cq。
- 作者挑戰的預設：不是「agent 越強就越省 token」，而是「孤立工作的 agent 必然集體浪費」；不是「在 .md 寫 prompt 規則就夠」，而是需要能自我演化、信任分數累積的動態知識層。
- 個人映射：對應你長期在做的「context-as-asset」、「repo 承載 context/skill/trace」主軸。cq 提供了從個人 repo 層的 context 走向跨團隊 / 跨 org 的 context commons 的橋接思路；同時補上「agent 知識需有信任機制」的維度，這在你之前的 context engineering 卡片中尚未明確處理。
- 也對應你關注的「AI 對共享知識生態的 matriphagy 問題」——一篇罕見有結構性反思的 announcement post。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent 孤島之痛：相同的牆被一萬個 agent 各撞一次
- 分級：Core
- 類型：Pattern
- 核心內容：當前 agent 的工作模式是各自獨立、各自試錯，每個 agent 遇到 Stripe 速率限制、CI 設定、新 framework 都得自己讀檔、寫錯、跑壞 build、重來。這不是模型不夠強的問題，而是知識沒有跨 agent 共享通道，導致對稱浪費 token、compute、能源的結構性問題。
- 保留理由：把「agent 浪費」從個體 prompt 問題拉高到生態層級的結構問題，是 Mozilla.ai 提出 cq 的根本動機，也是「為何需要 context commons」的母命題。
- 待補強處：缺乏量化估計（一個典型企業內部 agent 重複試錯成本佔多少？）；可補對照舊解法（如何不用 commons 也能局部解決，例如 repo 內 .md sticky note）。
- 初步知識鉤子：[[Context-as-Asset]]、[[Harness Engineering]]、[[Stripe Benchmark 中 ambiguous situations 的失敗模式]]

序號 2
- 候選標題：cq 模式：agent 的 Stack Overflow 需要可信任的動態知識層，而非靜態 .md
- 分級：Core
- 類型：Principle
- 核心內容：作者主張當前 repo 內 .md 提示文件的做法「只能走到一定程度」，因為它是靜態、無回饋、無信任分數的。真正可規模化的 agent 知識層應該動態，讓「使用次數 + 多 agent 跨 codebase 確認」累積信任，過時則被標記。知識透過使用而非權威獲得信任。
- 保留理由：明確點出「靜態文件 vs 動態知識層」的結構差異，這是 context engineering 進到下一階段的關鍵分水嶺，也是你「Repo-as-Worker」往「Org-as-Knowledge-Commons」演化的橋接。
- 待補強處：信任分數的具體機制（多少 agent 確認算可信？）、過時偵測邏輯尚未交代；落地時與企業內部 IP 邊界如何處理也未說清。
- 初步知識鉤子：[[Repo-as-Worker / Agent-as-Repo]]、[[Context Layer = Living Corpus]]、[[Self-Updating Context Flows]]

序號 3
- 候選標題：知識信任不是來自權威，而是來自跨場景重複驗證
- 分級：Support
- 類型：Heuristic
- 核心內容：作者指出 84% 開發者用或計畫用 AI 工具，但 46% 不信任輸出（去年 31%）。cq 對此的解法是：被多個 agent 在不同 codebase 確認過的知識單位，比單一模型的 best guess 更可信。信任的單位不是「誰說的」，而是「在多少不同情境被驗證過」。
- 保留理由：把信任問題從「模型能力 / RAG 來源權威」轉成「跨情境驗證頻次」，是一個可遷移的判準，可用於企業內部 context layer、決策系統或知識卡片設計。
- 待補強處：跨 codebase 重複驗證的可行性條件（需要哪種匿名化 / 抽象化機制？）；對企業內部封閉知識能不能套用？
- 初步知識鉤子：[[Eval 可靠性]]、[[Context Layer 的人工補齊]]、[[卡片信任分級]]

序號 4
- 候選標題：Matriphagy 警告：LLM 吃光餵養它的社群，下一代必須回灌
- 分級：Question
- 類型：Warning
- 核心內容：作者用「子代吞食母體」比喻 LLM 與 Stack Overflow 的關係——SO 養大了 LLM，LLM 卻反過來掏空 SO。這提出一個結構性問題：如果 agent 只消費而不貢獻知識，下一代 agent 會在更貧瘠的資料上訓練。cq 的「reciprocal」設計是試圖打破這個循環。
- 保留理由：直接點出 AI 生態層級的脆弱性，對「agent 應如何貢獻而非僅消費 context」是一個值得長期追蹤的開放問題；也呼應你關心的「AI 改變知識工作」中被忽略的供給端。
- 待補強處：是否有量化證據顯示新一代模型的 SO 含量真的減少？社群衰退與模型品質的因果鏈是否成立？
- 初步知識鉤子：[[AI 改變知識工作的供需失衡]]、[[長期主義]]、[[反脆弱設計]]

序號 5
- 候選標題：不要強加單一 agent 工作流：cq 應跨 Claude Code / OpenCode 等工具
- 分級：Support
- 類型：Heuristic
- 核心內容：作者主張就像不該強迫工程師用某個 IDE 或 commit 格式，也不該把 agent 知識共享綁死在某個 coding agent 上。cq 的設計刻意做成跨平台 plugin（Claude Code、OpenCode、MCP server），讓不同工具都能讀寫同一份知識常設。
- 保留理由：這是 context layer / agent commons 設計的一個重要原則：避免綁定單一 vendor，讓知識資產跨工具持有。對你關心的「平台中立的 context 設計」很關鍵。
- 待補強處：跨工具共用知識時的格式標準（除了 MCP 還缺什麼？）；治理權與所有權誰負責？
- 初步知識鉤子：[[MCP 作為 USB-C]]、[[A2A 與 MCP 分層]]、[[Vendor Lock-in 與架構解耦]]

## C. 建議送 refine 的項目
- 序號 1（Core）：Agent 孤島之痛
- 序號 2（Core）：cq 模式 — 動態知識層 vs 靜態 .md
- 序號 3（Support）：信任來自跨情境重複驗證
- 序號 5（Support）：Agent 知識層應跨工具中立
- 序號 4（Question）：保留作為長期追蹤命題

## D. 呼叫 refine-cards
- 上述 5 張候選卡交由 refine-cards 精煉；建議優先處理序號 1 與 2 的合併或互補關係（一個是問題、一個是解法主張）。
