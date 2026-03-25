# AI Agents 101：最清晰的 Agent 入門指南

**來源**：Greg Isenberg（@gregisenberg）
**連結**：https://x.com/gregisenberg/status/2034052610664116550
**日期**：2026-03-18
**主題**：AI Agents / Claude Skills / MCP / 實務應用
**互動**：359.7K 瀏覽 · 116 留言 · 318 轉發 · 2.4K 喜歡

---

## 正文

**AI AGENTS 101（58 分鐘免費大師課）**

send this to anyone who wants to understand ai agents, claude skills, md files, how to get the most out of AI etc in plain english:

1. **chat vs agents**
   chat models answer questions in a back and forth while agents take a goal, figure out the steps, and deliver a result

2. **agents don't stop after one response**
   they keep running until the task is actually finished — no babysitting required

3. **everything runs on a loop**
   they gather context, decide what to do, take an action, then repeat until done

4. **the loop is the system**
   they look at files, tools, and the internet. decide the next step. execute and then feed that back into the next step. over and over until completion

5. **the model is just one piece**
   gpt, claude, gemini are the reasoning layer. the key is model + loop + tools + context

6. **mcp is how agents use tools**
   it connects things like browser, code, apis, and your internal software. once connected, the agent decides when to use them to get the job done

7. **context beats prompt all day**
   you don't need to write perfect prompts. load your agent with context about your business, style, and goals and then simple instructions work

8. **claude.md or agents.md is the onboarding doc**
   it tells the agent who it is, how to behave, what it knows, and what tools it can use. this gets loaded every time before it starts

9. **memory.md is how it improves**
   agents don't remember by default. this file stores preferences, corrections, and patterns you tell the agent to update it, and it gets better over time

10. **skills + harnesses make it usable**
    skills are reusable tasks like writing, research, analysis
    the harness is the environment like claude code or openclaw that runs everything
    basically, different interfaces, same system underneath

this episode with remy on @startupideaspod was one of the clearest ways of understanding a lot of the core concepts of ai agents — could be the best beginners course for ai agents

58 mins. all free. no advertisers. i just want to see you build cool stuff. im rooting for you. send to a friend

---

## 重點摘要

- **Chat vs Agent 的關鍵差異**：Chat 是問答對話；Agent 是設定目標後自動執行到完成
- **Agent 的核心架構**：Loop（循環）= 蒐集 context → 決策 → 執行 → 回饋 → 重複
- **Model 只是一個零件**：完整的 agent = model + loop + tools + context
- **MCP 的角色**：讓 agent 連接到外部工具（瀏覽器、API、內部軟體）
- **關鍵文件**：
  - `claude.md` / `agents.md`：agent 的「入職文件」，定義身份、行為、工具
  - `memory.md`：讓 agent 累積學習，隨時間改善
- **Context > Prompt**：與其寫完美提示詞，不如給 agent 豐富的業務背景資訊
