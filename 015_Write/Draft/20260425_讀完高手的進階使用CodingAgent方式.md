---
pipeline_stage: "DONE"
topic: "讀完 Tony 的 Better Agent Terminal — 進階使用 Coding Agent"
target_reader: "想變得更會使用 Coding Agent 的自己"
scenario: "insight"
chosen_title: "進階使用 Coding Agent，原來不是更會寫 Prompt"
chosen_hook: "我以為的進階是換更強的模型，他在做的是重新設計工作流"
chosen_framework: "universal_writing"
created: 2026-04-25
last_updated: 2026-04-26
status: "published"
publish_path: "015_Write/Publish/20260426_【進階使用 Coding Agent，原來不是更會寫 Prompt】.md"
---

# 從 Tony 使用 Coding Agent 的方式，看見進階玩法的差距

最近看到 Tony 對 Codex、Claude Code、OpenCode、context management 的一些討論，再對照他做的工具 **Better Agent Terminal**，我覺得這已經不是一般「會用 Coding Agent」的層次，而是進到下一階段：

> 不只是叫 Agent 幫我寫 code，而是開始設計一個更可控、更安全、更有效率的 Agent 工作環境。

我自己目前比較熟的是 Codex CLI、Claude Code 這類工具。平常用法大概是打開 terminal，請 Agent 看 repo、改 bug、加功能、跑測試。這已經很有幫助，但 Tony 的思考更往前一步：他在關心 Agent 背後的運作流程。

---

## 1. 一般人用 Agent，他在管理 Agent

一般使用者大多是這樣：

```text
我 → Claude Code / Codex CLI → Agent 幫我改程式
```

Tony 的方向比較像這樣：

```text
我 → 自己做的 Agent 工作台
   → 控制 workspace / terminal / git / file / plan / permission / context
   → 再去驅動 Claude Code / Codex / terminal
```

Better Agent Terminal 的 README 也明確寫到，它不是只有 terminal，而是整合了 multi-workspace、Claude Code agent panel、file browser、git viewer、snippet manager、remote access 等功能。它本質上比較像一個「Agent 工作台」，不是單純 terminal 美化工具。([GitHub][1])

這讓我意識到一件事：

> 進階使用 Coding Agent，不是一直換更強的模型，而是讓 Agent 的工作流程變得可管理。

---

## 2. 他最在意的不是 prompt，而是 context management

Tony 提到一個很關鍵的問題：

> 你想過你下的每個 message / tool call 怎麼變成 context 的嗎？怎麼壓縮、怎麼放，怎麼產生效果？

這句話對我很有啟發。

以前我會以為使用 Agent 的能力差距主要來自 prompt 寫得好不好。但實際上，更進階的差距可能是：

```text
哪些資訊要給 Agent？
哪些檔案要放進 context？
工具執行結果要怎麼回填？
錯誤訊息要完整保留還是摘要？
plan 要不要一直保留？
context 快爆掉時要怎麼 compact？
```

所以所謂 context management，不只是「把資料丟給 AI」，而是要管理 Agent 的工作記憶。

這跟我做 PM / SA / Data Platform 其實很像：
資料不是越多越好，重點是**正確的資料，在正確的時候，用正確的格式，進入正確的決策流程**。

---

## 3. Plan mode 是進階使用者的安全帶

Tony 對 plan mode 很重視。他甚至說，沒有 plan mode 會是重傷。

我現在比較能理解為什麼。

因為 Coding Agent 最大的問題，不一定是不會寫 code，而是：

```text
它太快開始做
它可能沒理解完整
它可能直接改錯地方
它可能改出一大包 diff
它可能在我還沒確認前就動手
```

所以進階用法應該是：

```text
先讀 repo
先理解需求
先找相關檔案
先提出 plan
先標風險
人確認後再實作
```

Better Agent Terminal 也有 permission modes，其中包含 Plan mode：Agent 會先提出 plan file，通過後才自動執行。這代表 Tony 不是只靠口頭提醒 Agent「請你先 plan」，而是把 plan 變成工具流程的一部分。([GitHub][1])

這點我覺得很值得學。

我自己之後用 Codex / Claude Code，也應該固定要求：

```text
請先進入 planning 模式。
不要修改任何檔案。
先讀專案結構與相關檔案。
提出修改計畫、風險與驗收方式。
等我確認後再開始實作。
```

這是我目前最可以馬上學起來的進階習慣。

---

## 4. 他在做的是「可控的 Agent 工作環境」

Better Agent Terminal 的功能裡，有幾個我覺得特別值得注意：

```text
multi-workspace
agent presets
permission modes
session resume / fork
auto-compact
context usage
token / cost / cache efficiency
git viewer
file browser
worktree isolation
```

這些功能的共通點是：
它們都不是讓模型「更聰明」，而是讓 Agent 的工作過程**更可控、更可追蹤、更安全**。

README 裡提到，它可以顯示 session ID、token count、context percentage、cost、cache efficiency、prompt history 等狀態。([GitHub][1])

這讓我想到：
一般人只看 Agent 最後有沒有寫出 code；進階使用者會看：

```text
這次用了多少 context？
context 快滿了嗎？
成本多少？
cache 有沒有命中？
session 能不能 resume？
這次改了哪些檔案？
有沒有可以 fork 出另一條路線？
```

這其實已經接近「Agent operating system」的思維。

---

## 5. Worktree isolation 是很重要的安全設計

我以前使用 Claude Code / Codex，比較常見的風險是 Agent 直接在原本 repo 裡改東西。
如果改得不好，就要靠 git diff 慢慢看，甚至可能污染目前工作區。

Tony 的工具有一個很重要的概念：Git worktree isolation。README 說可以讓 Claude agent 在 isolated worktree 裡執行，避免破壞 main working tree。([GitHub][1])

我用自己的話理解就是：

```text
不要讓 Agent 直接在我的主工作區亂改。
先開一個隔離分身給它做。
做完我看 diff。
滿意再 merge。
不滿意就丟掉。
```

這個思維很值得放進我自己的 Agent 工作流。

尤其未來如果我要讓 Agent 幫忙做比較大的功能、PPT 自動化、MI 2.0 模組、Databricks pipeline、前後端整合，就不應該直接讓它在主線亂改。
更合理的是：

```text
任務分支 / worktree
→ Agent 實作
→ diff review
→ 測試
→ 人確認
→ merge
```

這跟我常講的 spec + quality gate 是同一件事。

---

## 6. CLI 好用，但 CLI 不是最穩的整合層

Tony 提到，如果走 CLI 層，很多 hook 都要自己來。

我理解這句話的意思是：

CLI 是給人操作的，不是一定設計給程式穩定控制的。
如果我只是用程式去包 CLI，就會遇到很多問題：

```text
CLI 畫面格式改了，自動化可能壞掉
中斷流程不好控制
tool call 狀態不好抓
plan / diff / permission 不一定好解析
hook 要自己補
```

所以如果只是一般人使用，CLI 很好。
但如果要打造自己的 Agent 工作台，CLI 就會不夠結構化。

這也是為什麼 Better Agent Terminal 對 Claude Code 不是單純開 CLI，而是使用 Claude Agent SDK。README 明確寫到它 built-in Claude Code via SDK，不需要另外開 terminal。([GitHub][1])

這代表它更接近：

```text
用 SDK 管 session、訊息、工具、狀態
而不是只看 terminal 畫面輸出
```

這就是一般使用者和工具開發者的差距。

---

## 7. 我目前不用急著做 SDK，但要學他的工作流觀念

看完之後，我覺得自己不需要一開始就跳去做 Agent SDK 或 App Server。

我現在最該學的是 Tony 背後的使用邏輯：

```text
1. 不要讓 Agent 太快動手
2. 先 plan，再執行
3. 把 context 管好
4. 把權限分級
5. 把修改隔離
6. 把 diff / cost / token / session 狀態看清楚
7. 把常用流程變成可重複的工具
```

也就是說，我現階段不一定要自己打造 Better Agent Terminal。
但我可以先把自己的使用流程升級成：

```text
AGENTS.md / CLAUDE.md
+ plan-first prompt
+ worktree / branch 隔離
+ 明確驗收條件
+ 測試 / lint / diff review
+ 任務紀錄
+ 常用 prompt / skills / scripts
```

這對我會比較務實。

---

## 8. 我對 Tony 這種玩法的理解

我現在會這樣看 Tony 的玩法：

他不是單純在追新工具，而是在解一個更根本的問題：

> Coding Agent 很強，但如果工作環境不可控，就很難穩定放大它的能力。

所以他做 Better Agent Terminal，本質上是在補這些能力：

```text
workspace 管理
terminal 管理
Agent session 管理
permission 管理
context 可視化
cost 可視化
git diff 管理
worktree 隔離
plan 審核流程
snippet / file / git 整合
```

這些東西合在一起，就讓 Agent 從「一個會寫 code 的聊天工具」，變成「一個可以被管理的數位工程師」。

---

## 9. 對我自己的啟發

這件事對我最大的啟發是：

> 我不應該只問「哪個 Agent 比較強」，而應該問「我有沒有建立一套讓 Agent 穩定產出的工作環境」。

對我目前的工作，例如 MI 2.0、廣告平台、Databricks 數據工程、PPT Agent、Text2SQL / Text2Chart，我其實都可以套用同一個想法：

```text
先定義任務
先給 context
先要求 plan
再允許實作
實作要隔離
結果要驗收
過程要可追蹤
常用能力要沉澱成 skills / scripts / prompts
```

這才是真正的進階使用。

不是「我會用 Claude Code」而已。
而是我開始建立一套自己的 Agent 工作法。

---

## 10. 我接下來可以做的具體行動

我覺得可以先從幾個簡單動作開始：

### 第一，建立自己的 Agent 使用規則

例如在 repo 放：

```text
AGENTS.md
CLAUDE.md
GEMINI.md
.github/copilot-instructions.md
```

裡面寫清楚：

```text
改檔前要先 plan
不要直接動 database schema
不要新增大型套件
要遵守現有架構
做完要列 changed files
要提供測試或手動驗收方式
```

### 第二，把 prompt 改成 plan-first

不要再只說：

```text
幫我做這個功能
```

要改成：

```text
請先讀 repo。
不要修改檔案。
先提出 plan、相關檔案、風險、驗收方式。
等我確認後再實作。
```

### 第三，重要任務用 branch / worktree 隔離

至少做到：

```text
每個 Agent 任務開一個 branch
大改動不要直接在 main working tree 做
做完先看 diff
再決定 merge
```

### 第四，開始記錄 Agent 任務結果

每次任務簡單記：

```text
任務目標
Agent 使用工具
改了哪些檔案
遇到什麼問題
哪些 prompt 有效
哪些地方失控
下次怎麼改進
```

這樣我才會越用越進步，而不是每次都重新摸索。

---

# 總結

Tony 的做法讓我看到，進階 Coding Agent 使用者的核心能力，不只是 prompt 寫得好，也不是只會用 Claude Code / Codex CLI。

真正進階的是：

```text
理解 Agent 怎麼吃 context
理解 tool call 怎麼影響結果
知道 plan mode 的重要性
知道 CLI 層的限制
知道什麼時候需要 SDK / 工作台
知道怎麼用 permission、worktree、diff、session 管理風險
```

對我來說，現階段不用急著重做一個 Better Agent Terminal。
但我應該開始學它背後的思想：

> 把 Coding Agent 從「聊天式使用」升級成「可管理的工程流程」。

這會比單純追新模型更有價值。

[1]: https://github.com/tony1223/better-agent-terminal?utm_source=chatgpt.com "tony1223/better-agent-terminal: Multi-workspace ..."
