. Agentic Engineering

來源：Addy Osmani（Google Cloud AI 工程師）
連結：https://addyosmani.com/blog/agentic-engineering/
發佈日期：2026 年 2 月 4 日
語言：英文
一句話摘要：系統性定義了「Agentic Engineering」的工作流，清晰劃分它與 Vibe Coding 的本質區別。
為什麼值得讀：這是目前對 Agentic Engineering 最清晰、最具實操性的定義文章。Osmani 從實踐出發，給出完整工作流：先寫設計文檔→分解任務→AI 生成代碼→嚴格代碼審查→測試驅動循環。 addyosmani他同時指出這種模式更利於資深工程師，對初級工程師存在技能萎縮風險， AddyOsmani.com並出版了 O'Reilly 新書《Beyond Vibe Coding》。
關鍵洞見預覽：「Agentic Engineering 不是比傳統工程更簡單——而是一種不同的難。你用審查時間替代了寫代碼時間，用編排能力替代了實現能力。基礎功力不是變得不重要，而是更重要了。」 addyosmani


Agentic Engineering
February 4, 2026
A year ago, Andrej Karpathy coined “vibe coding” to describe a gleefully reckless way of programming: you prompt, hand the keyboard to an AI, accept everything it spits out, don’t read the diffs, iterate by pasting error messages back in. It was a great label for a real thing - building quick prototypes or MVPs on pure AI autopilot.

The problem is that “vibe coding” has become a suitcase term. People now use it to describe everything from a weekend hack to a disciplined engineering workflow where AI agents handle implementation under human oversight. These are fundamentally different activities, and conflating them is causing real confusion - and real damage.

What vibe coding actually is
Vibe coding means going with the vibes and not reviewing the code. That’s the defining characteristic. You prompt, you accept, you run it, you see if it works. If it doesn’t, you paste the error back and try again. You keep prompting. The human is a prompt DJ, not an engineer.

This is genuinely useful for:

Greenfield MVPs, prototypes and hackathon demos. You need something working by Sunday. Code quality is irrelevant.
Personal scripts and one-off tools. You’re the only user. If it breaks, you regenerate it.
Learning and exploration. Newcomers can build things they couldn’t otherwise, learning by example from the AI’s output.
Creative brainstorming. Deliberately over-generating to see what approaches the AI suggests, then throwing it away and building properly.
If vibe coding gives millions of people the ability to create custom software who otherwise couldn’t, that’s a genuine win. The technique has a legitimate place in the toolbox.

But the failure modes are well-documented at this point. The pattern is always the same: it demos great, then reality arrives. You try to modify it, scale it, or secure it, and you discover nobody understands what the code is actually doing. As one engineer put it, “This isn’t engineering, it’s hoping.”

We need a better term for the professional version
Here’s the thing: a lot of experienced engineers are now getting massive productivity gains from AI - 2x, 5x, sometimes more - while maintaining code quality. But the way they work looks nothing like vibe coding. They’re writing specs before prompting. They’re reviewing every diff. They’re running test suites. They’re treating the AI like a fast but unreliable junior developer who needs constant oversight. I’ve personally liked “AI-assisted engineering” and have talked about how this describes that end of the spectrum where the human remains in the loop.

Simon Willison (whose work I adore) proposed “vibe engineering” for this - it reclaims “vibe” while adding “engineering” to signal discipline. But after watching the community debate this for months, I think the the word “vibe” carries too much baggage. It signals casualness. When you tell a CTO you’re “vibe engineering” their payment system, you can see the concern on their face.

Andrej Karpathy suggested “agentic engineering” this week and I think I like it.

Here’s perhaps why it works:

It describes what’s actually happening. You’re orchestrating AI agents - coding assistants that can execute, test, and refine code - while you act as architect, reviewer, and decision-maker. You might write only a % of the code by hand. The rest comes from agents working under your direction. That’s agentic. And you’re applying engineering discipline throughout. That’s engineering.

It’s professionally legible. “Agentic engineering” sounds like what it is: a serious engineering discipline involving autonomous agents. You can say it to your VP of Engineering without embarrassment. You can put it in a job description. You can build a team practice around it.

It draws a clean line. Vibe coding = YOLO. Agentic engineering = AI does the implementation, human owns the architecture, quality, and correctness. The terminology itself enforces the distinction.

A spectrum showing vibe coding on one end and agentic engineering on the other, with AI-assisted engineering in the middle.

What agentic engineering looks like in practice, perhaps.
The workflow isn’t complicated, but it requires discipline that vibe coding explicitly abandons:

You start with a plan. Before prompting anything, you write a design doc or spec - sometimes with AI assistance. You break the work into well-defined tasks. You decide on the architecture. This is the part vibe coders skip, and it’s exactly where projects go off the rails.

You direct, then review. You give the AI agent a well-scoped task from your plan. It generates code. You review that code with the same rigor you’d apply to a human teammate’s PR. If you can’t explain what a module does, it doesn’t go in.

You test relentlessly. The single biggest differentiator between agentic engineering and vibe coding is testing. With a solid test suite, an AI agent can iterate in a loop until tests pass, giving you high confidence in the result. Without tests, it’ll cheerfully declare “done” on broken code. Tests are how you turn an unreliable agent into a reliable system.

You own the codebase. You maintain documentation. You use version control and CI. You monitor production. The AI accelerates the work, but you’re responsible for the system.

Teams doing this well often report faster development - and those gains come from augmenting a solid process, not abandoning one. The AI handles boilerplate and grunt work. The human focuses on architecture, correctness, edge cases, and long-term maintainability.

The irony is that AI-assisted development actually rewards good engineering practices more than traditional coding does. The better your specs, the better the AI’s output. The more comprehensive your tests, the more confidently you can delegate. The cleaner your architecture, the less the AI hallucinates weird abstractions. As one analysis noted, “AI didn’t cause the problem; skipping the design thinking did.”

The skill gap we’ve discussed
Here’s an uncomfortable truth from the trenches: agentic engineering disproportionately benefits senior engineers. If you have deep fundamentals - you understand system design, security patterns, performance tradeoffs - you can leverage AI as a massive force multiplier. You know what good code looks like, so you can efficiently review and correct AI output.

But if you’re junior and you lean on AI before building those fundamentals, you risk a dangerous skill atrophy. You can produce code without understanding it. You can ship features without learning why certain patterns exist. Several engineering leaders have flagged this as an emerging crisis: a generation of developers who can prompt but can’t debug, who can generate but can’t reason about what they’ve generated.

This isn’t an argument against AI-assisted development. It’s an argument for being honest about what it demands. Agentic engineering isn’t easier than traditional engineering - it’s a different kind of hard. You’re trading typing time for review time, implementation effort for orchestration skill, writing code for reading and evaluating code. The fundamentals matter more, not less.

Where we go from here
The trajectory is clear: AI agents are getting more capable, and the agentic engineering workflow is becoming default for a growing number of professional developers. This is going to accelerate.

We need:

Honest terminology. Call it agentic engineering when you mean disciplined, agent-assisted development with human oversight. Call it vibe coding when you mean the fun, reckless, prototyping-only version. Stop using one term for both.
Better evaluation frameworks. We need systematic ways to measure whether AI-assisted workflows are actually producing reliable software, not just faster software.
Investment in fundamentals. As AI handles more implementation, the premium on architectural thinking, security awareness, and systems design goes up, not down. Training programs need to adapt.
The rise of AI coding doesn’t replace the craft of software engineering - it raises the bar for it. The developers who’ll thrive aren’t the ones who prompt the fastest. They’re the ones who think the clearest about what they’re building and why, then use every tool available - including AI agents - to build it well.

Vibe coding showed us what’s possible when you drop all conventions.

Now it’s time to bring the engineering back. Let’s call that what it is.

I’ve written a new book with O’Reilly, Beyond Vibe Coding, that goes deeper into practical frameworks for AI-Assisted (and agentic) engineering. If you’ve been figuring this out in your own workflow, I’d love to hear what’s working.
---

# 拆解結果

## A. 主脈絡與個人映射

**論證骨架**：
- Osmani 從術語混亂切入：「Vibe Coding」原本指無審查的快速原型開發，但現已被濫用來描述所有 AI 輅助開發，導致專業實踐與業餘玩票無法區分。
- 論證路徑：定義 Vibe Coding（無審查、純提示型）→ 指出其合理場景（MVP/原型）→ 區分專業做法（有設計、審查、測試）→ 提出新術語 Agentic Engineering → 說明工作流與技能要求 → 警告初級工程師風險。
- **作者挑戰的預設**：「AI 讓開發變簡單了」。他的核心主張是：AI 不是降低門檻，而是改變難度的性質——從「寫代碼」轉向「審查與編排」，基礎功力變得更重要而非更不重要。

**個人映射（對系統建造者的價值）**：
- 這篇文章提供了清晰的**分類框架**，讓「槓桿型系統建造者」能精準定位自己的工作模式：不是 Vibe Coding，而是 Agentic Engineering。
- 核心價值在於**角色重定義**：AI 將你從「實現者」推向「架構師 + 審查者 + 編排者」，這與 MY_PROFILE 中「限制理論：把 90% 可被 AI 壓縮與 10% 高槓桿決策分開管理」直接對應。
- **風險治理視角**：文章指出測試、設計文檔、代碼審查是專業與業餘的分界線，這與 MY_PROFILE 的「AI Coding 風險治理」節點高度契合。
- **技能分化警告**：資深工程師獲得槓桿，初級工程師面臨萎縮風險，這是結構性趨勢，需要在團隊管理與個人發展中納入考量。

---

## B. 卡片（Zettel）

### 序號 1
- **標題**：Vibe Coding vs Agentic Engineering：審查權是唯一分界線
- **類型**：Model
- **概念**：
  Vibe Coding = 提示 + 接受 + 不審查 + 迭代靠錯誤訊息。人類是「prompt DJ」，不是工程師。
  Agentic Engineering = AI 執行 + 人類架構/審查/決策。工作流：設計文檔 → 任務分解 → AI 生成 → 嚴格審查 → 測試驅動循環。
  **唯一分界線**：是否審查代碼。兩者不是「簡單 vs 複雜」，而是根本不同的活動。把它們混用會導致專業實踐被稀釋成業餘玩票。
  Vibe Coding 的合理場景：週末 MVP、個人腳本、學習探索、創意腦暴（Deliberately over-generating then throwing away）。超出這些場景，失敗模式是：demo 很好，修改/擴展/安全加固時發現無人理解代碼實際在做什麼。
- **重要性**：讓你精準定位自己的 AI 協作模式，避免在團隊或提案中被誤判為「不負責任的 Vibe Coder」；同時能識別哪些場景可以降低標準（原型），哪些必須維持工程紀律（生產系統）。
- **邊界/反例**：Agentic Engineering 並非萬能：它要求資深工程師級別的架構與審查能力，對初級工程師反而可能加速技能萎縮（能提示但不能除錯、能生成但無法推理）。若團隊缺乏測試文化或代碼審查習慣，引入 AI 只會加速混亂。
- **知識鉤子**：
  - 可作為 #AI_Coding_風險治理 的頂層分類框架。
  - 與 #Kent_Beck（AI 時代工程角色重估）形成對話：當 AI 承擔實現，人類價值在哪？
  - 與 #限制理論 對應：Vibe Coding 是「局部最佳化」（快速出 demo），Agentic Engineering 是「系統最佳化」（保護長期可維護性）。

---

### 序號 2
- **標題**：AI 協作的核心交易：你用審查時間替代了寫代碼時間
- **類型**：Principle
- **概念**：
  Agentic Engineering 不是「更簡單的開發」，而是「不同性質的難」。
  **核心交易**：
  - 你放棄：寫代碼的掌控感、純實現工作的時間投入。
  - 你獲得：快速產出（2x–5x）、從繁瑣實現中解放。
  - 你必須支付：嚴格審查每行代碼的時間（如同審查 junior developer 的 PR）、編排與架構設計的認知負擔、測試套件的前期投入。
  
  **底層邏輯**：AI 是「快速但不可靠的 junior」。槓桿的前提是你有能力判斷它的輸出（架構、安全、邊界案例），否則速度只會讓你更快撞牆。
  
  越好的規格 → 越好的 AI 輸出。越完整的測試 → 越能放心委派。越乾淨的架構 → 越少 AI 幻覺奇怪抽象。
  
- **重要性**：破除「AI 讓一切變簡單」的幻覺，讓你正視新的技能要求（審查、編排、架構）並刻意訓練；同時能向管理層解釋為何引入 AI 後仍需維持高標準的設計與測試流程。
- **邊界/反例**：若你缺乏深厚的系統設計、安全模式、效能權衡知識，AI 產出的代碼你無法有效審查，速度優勢會變成品質災難。這也是為何 Agentic Engineering「disproportionately benefits senior engineers」。
- **知識鉤子**：
  - 可作為 #Harness_驅動框架視角 的底層邏輯：把「模型能力」與「可交付成果」分開看，中間需要 loop/verification/guard。
  - 與 #納瓦爾「不可壓縮的才是護城河」形成呼應：AI 壓縮了實現，但架構判斷與系統直覺無法壓縮。
  - 與 #複利工作流 對應：前期投入測試與規格，後期複利放大。

---

### 序號 3
- **標題**：測試套件是 Agentic Engineering 的核心槓桿點
- **類型**：Leverage
- **概念**：
  「The single biggest differentiator between agentic engineering and vibe coding is testing.」
  
  **機制**：
  - 有完善測試套件 → AI Agent 可在迴圈中迭代直到測試通過 → 你對結果有高信心 → 你能安心委派更多任務。
  - 無測試套件 → AI 會愉快地宣告「完成」在 broken code 上 → 你只能手動驗證每個輸出 → 速度優勢消失。
  
  測試不只是品質保證，而是「將不可靠 agent 轉成可靠系統」的機制。它讓 AI 從「產生垃圾需要你判斷」變成「自我迭代直到正確」。
  
  **實務建議**：在引入 AI 之前，先建立測試文化與 CI 流程。AI 不是「讓你可以跳過測試」，而是「讓測試變得更重要」。
  
- **重要性**：讓你知道在 AI 協作中，測試不是成本而是槓桿。一個好的測試套件可以讓你放心將重複性實現工作委派給 AI，自己專注於架構與邊界案例。
- **邊界/反例**：測試套件本身的品質至關重要。若你的測試只覆蓋 happy path，AI 會過度自信地通過測試但在 edge case 失敗。若測試寫得太脆弱（過度依賴實現細節），AI 每次重構都會打破測試，反而增加負擔。
- **知識鉤子**：
  - 可作為 #AI_Coding_風險治理 中「測試策略」的核心論述。
  - 與 #TDD（測試驅動開發）形成新的意義：在 AI 時代，TDD 不只是品質保證，更是「AI 的操控介面」。
  - 與 #可觀測性思維 對應：測試是最直接的「判斷 AI 產出是否正確」的訊號。

---

### 序號 4
- **標題**：AI 協作的技能分化：資深工程師獲得槓桿，初級工程師面臨萎縮
- **類型**：Warning / Trend
- **概念**：
  **結構性風險**：Agentic Engineering 不成比例地偏惠資深工程師。
  
  - **資深工程師**：有深厚基本功（系統設計、安全模式、效能權衡）→ 能高效審查與修正 AI 產出 → 知道好代碼長什麼樣 → AI 成為巨大力量倍增器。
  - **初級工程師**：若在建立基本功之前就依賴 AI → 能產出代碼但不理解它 → 能交付功能但不學習為何某些模式存在 → **技能萎縮（skill atrophy）**：會提示但不會除錯、會生成但無法推理。
  
  多位工程領導已將此標記為「emerging crisis」：一整代開發者可能會 prompt 但無法 reason。
  
  **底層邏輯**：AI 壓縮了「學習曲線中的練習環節」。傳統路徑是「寫很多爛代碼 → 被 review 打臉 → 理解為何那樣不好 → 內化模式」。AI 讓初級工程師跳過「寫爛代碼」直接到「產出看起來 OK 的代碼」，但沒有經歷「被打臉」與「內化」，導致判斷力無法成長。
  
- **重要性**：若你在團隊中引入 AI 工具，需要刻意設計「初級工程師的學習路徑」，不能讓他們無限依賴 AI。若你本身是初級/中級工程師，需要警覺自己是否在用 AI 逃避基本功（架構、演算法、系統設計）的刻意練習。
- **邊界/反例**：並非所有初級工程師都會萎縮——關鍵在於他們如何使用 AI。若將 AI 當作「學習工具」（生成後深入研究為何這樣寫、拆解架構邏輯），可以加速學習。若當作「外包工具」（生成後直接交付，不理解內部），則會萎縮。團隊需要建立明確的「AI 使用原則」與「code review 文化」來引導。
- **知識鉤子**：
  - 與 #AI時代的角色轉型 形成系統性分析：不只是「PM 到 Possibility Maker」，工程師也在分化。
  - 與 #複利思維 形成警告：短期生產力提升（用 AI 快速交付）可能是長期能力衰退（判斷力無法成長）的代價。
  - 可作為 #團隊管理 中「AI 時代人才培養策略」的底層風險評估。

---

## C. 連結建議（組裝藍圖）

### 內部組裝
- **卡片 1 + 卡片 3**：可組成「Agentic Engineering 的最小可行工作流」——先建測試套件，再引入 AI，用審查而非接受作為關卡。
- **卡片 2 + 卡片 4**：可組成「AI 協作的能力門檻與風險分析」——不是所有人都能從 AI 獲益，槓桿的前提是你有能力審查與編排。

### 外部對接
- 與現有卡片 **`3-AI 工程兩層拆解：技術實現 vs 需求定義`** 連結：Agentic Engineering 進一步細化了「技術實現層」的分工——AI 負責 coding，人類負責架構與審查。
- 與 **`4-Coding Agent 的三層架構：Harness > Model > Output`** 連結：Agentic Engineering 的工作流（設計 → AI 生成 → 審查 → 測試）就是 Harness 層的實踐。
- 與 **`14-AI 讓某些技能過時，但讓判斷力更有價值`**（若有）連結：本文提供具體證據——寫代碼被壓縮，架構與審查能力成為新槓桿。
- 建議新增到索引 **`Idx_4-AiCoding.md`** 的「AI Coding 工作流」或「角色與技能轉型」段落。

---

## D. 可執行的下一步

1. **團隊層級**：若你正在推動 AI Coding 工具（如 Cursor、GitHub Copilot、Claude Code），先盤點當前的「設計文檔習慣」、「測試覆蓋率」、「Code Review 文化」。若這三者不存在，引入 AI 可能加速混亂而非提升效能。優先投資測試基礎設施。

2. **個人層級**：若你是資深工程師，刻意練習「審查 AI 產出」的速度與準度（辨識安全漏洞、效能瓶頸、架構債）。若你是初級/中級工程師，設定規則「每次接受 AI 產出前，必須能向他人解釋這段代碼的運作機制與權衡」，避免技能萎縮。

3. **語言升級**：在向管理層或團隊提案 AI 工具時，不要用「AI 讓開發更快更簡單」，而是用「AI 讓我們從實現轉向架構與品質把關，但需要更強的基礎能力與測試投入」。這能避免管理層誤判「可以砍人或降低招聘標準」。

