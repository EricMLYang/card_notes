---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-20
---

## [重點]
**編碼代理的瓶頸不在模型智能，而在缺乏結構化工作流程**。強制 AI 遵循紀律化流程比追求更強大的模型更有效。透過 chardet 7.0.0 重寫案例（41x 速度提升、96.8% 準確度），證明單一開發者透過結構化流程能完成完整現代化專案。

## [摘要]


## [詮釋]


---

# Teaching Your Coding Agent to Think Before It Types

> 來源：EMSI
> 連結：https://www.emsi.me/tech/ai-ml/teaching-your-coding-agent-to-think-before-it-types/2026-03-12/143a54
> 搜集日期：2026-03-16
> 搜集原因：AI Coding Agent 工程實踐

## 摘要

作者 Jesse Vincent 開發了 Superpowers 插件，核心論點是：**編碼代理的瓶頸不在模型智能，而在缺乏結構化工作流程**。強制 AI 遵循紀律化流程比追求更強大的模型更有效。透過 chardet 7.0.0 重寫案例（41x 速度提升、96.8% 準確度），證明單一開發者透過結構化流程能完成完整現代化專案。

## 關鍵段落

**Superpowers 三階段工作流：**

> "設計階段（蘇格拉底式頭腦風暴，在寫任何代碼前探索替代方案）→ 規劃階段（將工作分解為 2-5 分鐘的微任務，附帶具體規範）→ 執行階段（實施紅綠重構 TDD 循環，強制測試優先於代碼）"

> "這些技能在任務相關時自動啟動，代理必須遵循匹配的工作流程"

**核心洞察：**
> "與其給代理更多能力，不如給它紀律。Vincent 指出開發人員已知這對人類團隊有效（代碼審查、TDD、設計文檔），問題是未曾為代理編碼這些實踐。"

## 潛在卡片方向

- AI Agent 效率的關鍵不是模型能力，是工作流程紀律（discipline > capability）
- Coding Agent 三階段框架：設計（探索）→ 規劃（分解微任務）→ 執行（TDD 強制）
- 將人類工程最佳實踐「編碼」給 Agent 的設計思路
- 與現有卡片連結：[[AI Coding Agent 判斷力框架]]、[[TDD 作為 AI 操控介面]]

---
*由 scout-news 自動搜集，待 process-inbox 處理*
AI / MLProgramming
Teaching Your Coding Agent to Think Before It Types
2026-03-12  Mariusz Woloszyn
Most coding agents are eager. Too eager. You ask for a feature, and within seconds they’re spitting out code — no questions about what you actually need, no discussion of trade-offs, no plan. Just code barreling in a direction that might be completely wrong. When it inevitably goes sideways, you’ve burned tokens, time, and patience on work that needs to be thrown away.

Jesse Vincent got tired of this. A veteran open-source developer, Vincent spent months in late 2025 observing how he worked with AI coding agents and extracting patterns from that collaboration. What he noticed was that the best results came not from better models, but from better process — from forcing the agent to slow down, ask questions, and commit to a plan before writing a single line of code.

The result was Superpowers, a plugin for Claude Code that doesn’t give the AI new capabilities so much as it gives it discipline.

Skills, Not Prompts
The core idea is that agents work better when they follow structured workflows rather than freestyling from a single prompt. Superpowers encodes those workflows as composable “skills” — markdown files containing instructions that the agent must follow when they apply to the current task. The key word is must. These aren’t suggestions. When a skill exists for an activity, the agent is required to use it.

The workflow starts before any code gets written. When the agent detects you’re building something, it activates the brainstorming skill — a Socratic design session where it asks you targeted questions, explores alternatives, and presents the design in digestible chunks for your approval. Only after you’ve signed off does it move on.

Next comes planning. The agent breaks work into bite-sized tasks — typically two to five minutes each — with exact file paths, complete code expectations, and verification steps. Vincent describes the target audience for these plans as “an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing.” If the plan is clear enough for that imaginary person, it’s clear enough for a subagent.

Then implementation begins. Superpowers dispatches a fresh subagent for each task, reviews their work in two stages — first for spec compliance, then for code quality — and continues forward. The entire process enforces strict red-green-refactor TDD: write a failing test, watch it fail, write the minimum code to make it pass, refactor. If the agent writes code before tests, Superpowers deletes it and forces a restart.

It’s not uncommon for Claude to work autonomously for a couple of hours at a stretch without deviating from the agreed plan.

How It Actually Feels
The shift is immediately noticeable. Instead of chasing a runaway agent through bad code, you spend your time in design conversations and plan reviews — the parts where human judgment matters most. The agent handles the mechanical execution, but within guardrails you’ve approved.

Simon Willison, one of the most widely-read voices in AI tooling, called Vincent “one of the most creative users of coding agents” he knows. By January 2026, Superpowers had been accepted into Anthropic’s official Claude Code plugin marketplace. It has accumulated over 143,000 installs and the GitHub repository has drawn over 29,000 stars — remarkable traction for what is essentially a collection of well-crafted markdown files and shell scripts.

And the overhead is lighter than you’d think. The core bootstrap pulls in fewer than 2,000 tokens. Additional skills get loaded on demand as the agent searches for relevant ones. Vincent has shared full transcripts of end-to-end sessions — brainstorming, planning, implementing a small application — that stayed within 100k tokens total.

The plugin also supports extending itself. One of the earliest skills Vincent wrote was “how to create skills,” which means Claude can author new workflow documents following the same patterns. You can teach it your team’s conventions, your preferred architecture decisions, your code review checklist — and the agent will enforce them going forward.

The Skills Library
Superpowers ships with a library covering the core software development cycle. There’s a brainstorming skill for Socratic design refinement, a planning skill that produces detailed implementation roadmaps, and an execution skill that works through tasks in batches with human checkpoints. A subagent-driven development skill handles fast iteration with two-stage code review. The TDD skill enforces the red-green-refactor cycle and includes an anti-patterns reference. A systematic debugging skill walks through a four-phase root cause process. There are skills for git worktree management, code review (both requesting and receiving), and finishing a development branch — verifying tests, presenting merge options, cleaning up.

These skills trigger automatically based on context. You don’t invoke them manually. The agent checks for relevant skills before any task and follows the matching workflow. The result is that every session adheres to the same disciplined process, regardless of whether you remembered to type “use TDD” at the start.

A Full-Scale Rewrite as Proof
Perhaps the most dramatic demonstration of what Superpowers can deliver happened in early 2026, when Dan Blanchard — the long-time maintainer of chardet, Python’s widely-used character encoding detection library — used the plugin to orchestrate a ground-up rewrite of the entire project.

Blanchard had maintained chardet solo and unpaid for over twelve years. He’d long wanted to modernize it — improve speed, expand encoding support, boost accuracy — but the scope of the work was prohibitive for one person working in spare time. With Superpowers guiding Claude Code, Blanchard used the brainstorming skill to produce a detailed design document specifying the architecture he wanted. The agent then worked through a structured implementation plan, building a new 12-stage detection pipeline, training bigram frequency models on multilingual corpus data, and producing a comprehensive test suite covering 2,161 test files across 99 encodings and 48 languages.

The result, chardet 7.0.0, shipped on March 4, 2026. It was 41x faster than the previous version with mypyc compilation, achieved 96.8% accuracy (up 2.3 percentage points), and fixed dozens of longstanding issues that had lingered in the tracker for years. It closed more open issues in one release than the project had resolved in the prior decade.

Because the entire process ran through Claude Code, the repository contains an unusually transparent trail — design documents, rewrite plans, and commit histories with Claude listed as co-author. The design document alone runs to 330 lines, stepping through each stage of the rewrite from tests through to the detection pipeline architecture.

This wasn’t vibe coding. It was a structured, plan-driven rewrite of a complex, mature library — exactly the kind of project that would normally take a team months — executed by one developer and an agent working within a disciplined methodology.

A Licensing Footnote Worth Watching
The chardet rewrite did generate controversy, though not about its quality. Blanchard released the new version under the MIT license, replacing the original LGPL — arguing that a complete rewrite constitutes a new work. Mark Pilgrim, chardet’s original author, disagreed publicly, contending that the maintainers’ deep familiarity with the original code means the rewrite can’t be considered a clean-room implementation.

The debate — which drew commentary from Armin Ronacher (who coined the term “slopfork” for AI-assisted rewrites that shed licensing obligations), the Free Software Foundation, and even the Linux kernel mailing list — remains unresolved. No court has tested whether AI-mediated code rewrites count as derivative works. It’s a question the industry will need to answer, and chardet may end up being the case that forces it. But that’s a story about copyright law catching up with technology, not about the tool that happened to be in the room.

Why Process Beats Power
The deeper lesson from Superpowers isn’t about any single project. It’s that the bottleneck in AI-assisted development was never the model’s intelligence — it was the absence of structure around how that intelligence gets applied.

Developers have known this about human teams for decades. Code reviews, TDD, design documents, sprint planning — these exist not because individual engineers can’t code, but because unstructured work drifts. The same turns out to be true for coding agents, only more so, because they drift faster and with more confidence.

What Vincent built is, in some sense, the obvious thing: take the engineering practices that already work for humans and encode them so that agents follow them too. The non-obvious part was figuring out how to do it with minimal overhead, making skills composable and self-extending, and proving that a disciplined agent can sustain autonomous work on complex projects for hours at a time.

Superpowers is open source under the MIT license and designed for contributions — anyone can write and share new skills. It works with Claude Code natively and supports Cursor, Codex, and OpenCode with varying levels of setup. Installation is two commands:

/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
After that, your coding agent just has Superpowers. It asks better questions, makes plans you can actually review, tests before it builds, and stays on track. It’s what happens when someone decides that the problem with coding agents isn’t that they can’t code — it’s that nobody taught them how to work.

Related
