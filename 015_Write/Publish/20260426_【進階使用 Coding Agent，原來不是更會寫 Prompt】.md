【 進階使用 Coding Agent，原來不是更會寫 Prompt 】
——看完 Tonyq 的 Better Agent Terminal，我發現自己一直把它當聊天工具在用

長期潛水 Tonyq Wang 的 FB，
ㅤ
最近一直觀察他在做的 Better Agent Terminal，還有他對 Codex、Claude Code、context management 的一些討論。
ㅤ
我一邊看一邊冒汗。
ㅤ
不是因為他講的東西多難，

而是我發現——我用 Coding Agent 已經一年多了，但他談的那些東西，我從來沒想過要管。
ㅤ
ㅤ
▋ 我以為的進階，其實只是換更強的模型
ㅤ
我以前對「會用 Coding Agent」的想像很簡單。
ㅤ
打開 terminal，叫它讀 repo、改 bug、加功能、跑測試。

哪天 Claude Opus 4.6 出來，換新的就會更好用。哪天 Codex GPT-5.5 上來了再換 Codex。
ㅤ
看到 Tonyq 的東西之後，我才意識到一件事，

我以為的進階是「升級工具」，他在做的事是「重新設計工作流」。
ㅤ
他關心的不是哪個模型寫 code 比較強，他關心的是：
ㅤ
我下的每個 message、每次 tool call，到底怎麼變成 context？
ㅤ
要怎麼壓縮、怎麼放、什麼時候該扔掉？
ㅤ
這個問題我以前想都沒想過。
ㅤ
ㅤ
▋ 一般人用 Agent，他在管理 Agent
ㅤ
這個差別讓我卡了一下。
ㅤ
我以前的用法大概是這樣，我把想法直接打給 Claude Code 或 Codex，它幫我寫程式，我看結果。
ㅤ
Tonyq 的方向不太一樣。

他做的 Better Agent Terminal 是把 workspace、agent panel、file browser、git viewer、permission、worktree 隔離整合在一起。
ㅤ
換句話說，他不是只在「用 Agent」，而是在「管 Agent」。
ㅤ
我看完之後想——這個差距其實不在工具，在心態。
ㅤ
進階使用 Coding Agent，可能根本不是讓 prompt 變得更精煉，而是把 Agent 的工作流程變成可管理的東西。
ㅤ
ㅤ
▋ Context 不是越多越好，是該不該進來
ㅤ
Tonyq 提到 context management 那段我反覆讀了幾次。
ㅤ
以前我覺得 context 就是「把相關檔案丟進去」。但他在問的問題更細：
ㅤ
哪些訊息要進？
工具回傳的結果要完整保留還是摘要？
plan 要一直留著嗎？
context 要爆掉的時候怎麼 compact？
ㅤ
這些問題以前我都交給 Claude Code 自己處理。它有自己的壓縮策略，我也沒去管它怎麼決定的。
ㅤ
但仔細想——我自己做 data platform 的時候，不就是在管這個嗎？
ㅤ
資料不是越多越好，重點是正確的資料、在正確的時候、用正確的格式，進入正確的決策流程。
ㅤ
原來這套思維可以套到 Agent 身上。我之前一直沒接起來，是因為我把 Agent 當「對話對象」在用，沒把它當成一個有工作記憶的系統來管。
ㅤ
ㅤ
▋ Plan mode 是進階使用者的安全帶
ㅤ
Tonyq 對 plan mode 看得很重。他甚至說沒有 plan mode 是重傷。
ㅤ
我一開始覺得有點誇張。直到我回想我自己平常用 Coding Agent 的尷尬時刻——
ㅤ
它太快開始做。
還沒理解完整就改檔。
直接改錯地方。
改出一大包 diff，我得花很多時間才看得完。
ㅤ
這些不是模型不夠強，而是它太積極了。
ㅤ
Better Agent Terminal 的 permission modes 把 plan 寫進工具流程：Agent 要先提一份 plan file，人通過後才執行。
ㅤ
這比口頭叮嚀「請你先 plan」可靠很多。因為靠 prompt 提醒，agent 看心情；寫進工具流程，它沒選擇。
ㅤ
這件事我大概是現在最能立刻學起來的。
ㅤ
我打算之後固定加一段：
ㅤ
請先進入 planning 模式。不要修改任何檔案。先讀專案結構與相關檔案。提出修改計畫、風險與驗收方式。等我確認後再實作。
ㅤ
不是因為這段話多神奇，而是因為我終於把「人類確認」這件事，從口頭變成了流程。
ㅤ
ㅤ
▋ Worktree 隔離，是給 Agent 一個沙盒
ㅤ
Better Agent Terminal 還有一個我覺得很關鍵的功能是 git worktree isolation。

Agent 在隔離的 worktree 裡執行，不會污染主工作區。
ㅤ
這個觀念我很慚愧，

我以前都讓 Agent 直接在主分支或主工作區改東西。改得不好就 git stash，改得很糟就 git checkout 還原。
ㅤ
但說實話，我有幾次差點就把不該交出去的東西交出去了。

原因是 Agent 是 diff 太大、我看不完，就在 review 時失了焦。
ㅤ
換成 worktree 隔離的思維，事情就乾淨很多：
ㅤ
任務分支或 worktree → Agent 實作 → 我看 diff → 跑測試 → 確認後再 merge。
ㅤ
不滿意就丟掉。
ㅤ
這聽起來只是 git 的標準做法，但用在 Agent 身上，意義變了——它從「我跟 Agent 共用工作區」變成「我給 Agent 一個沙盒」。
ㅤ
這條我會放進自己的下一個案子裡試試看。
ㅤ
ㅤ
▋ CLI 是給人用的，不一定給程式用的
ㅤ
Tonyq 還說了一句：如果走 CLI 層，很多 hook 都要自己來。
ㅤ
我反芻了一下這句話。
ㅤ
CLI 是給人操作的介面。畫面格式可能改、中斷流程不好控、tool call 狀態不好抓、plan 跟 diff 解析全部要自己補。
ㅤ
我們一般用 Coding Agent，CLI 已經很好。但如果要打造一個自己的 Agent 工作台，CLI 就會不夠結構化。
ㅤ
所以 Better Agent Terminal 對 Claude Code 不是去包 CLI，

而是直接用 Claude Agent SDK——管 session、訊息、工具、狀態，而不是只看 terminal 畫面。
ㅤ
這是一般使用者跟工具開發者的差距。
ㅤ
我目前還在使用者那一端。

但我至少看清楚了——我現在 CLI 用得順手，不代表我有能力把 Agent 變成穩定的工作系統。這兩件事是兩個層次。
ㅤ
ㅤ
▋ 我不打算做工作台，但我想學他的工作法
ㅤ
看完之後我問自己一個問題——我要不要也去做一個 Better Agent Terminal？
ㅤ
答案是不要。
ㅤ
我目前的本業重心在 MI 2.0、廣告平台、Databricks 數據工程、Text2SQL 這些東西。我自己做工作台，會分散焦點。
ㅤ
但我可以學 Tonyq 背後的觀念，把它套到我自己現有的工作流上。
ㅤ
我目前能想到的具體動作是這幾個：
ㅤ
第一，把 AGENTS.md 寫得更清楚。
ㅤ
裡面寫死幾條規則：改檔前要先 plan、不要直接動 schema、不要隨便加大套件、做完要列改了哪些檔案、要附驗收方式。把口頭規矩變成 repo 裡的紀律。
ㅤ
第二，把 prompt 改成 plan-first。
ㅤ
不要再只說「幫我做這個功能」。改成「先讀 repo、先列檔案、先提 plan、先標風險，等我確認」。
ㅤ
第三，重要任務用 branch 或 worktree 隔離。
ㅤ
不要再直接讓 Agent 在主工作區動。給它一個沙盒，做完看 diff，再決定收不收。
ㅤ
第四，開始留任務紀錄。
ㅤ
每次跑完簡單記：目標是什麼、用了哪些工具、改了哪些檔、什麼 prompt 有效、什麼地方失控、下次要改什麼。
ㅤ
這樣我才會越用越進步，而不是每次都重新摸索。
ㅤ
ㅤ
▋ 最後
ㅤ
看完 Tonyq 的東西，我心裡有個想法很清楚——
ㅤ
我以前一直在問「哪個 Agent 比較強」，他在問「怎麼讓 Agent 穩定產出」。
ㅤ
這兩個問題的層次不一樣。
ㅤ
模型會一直變強。但工作環境如果不可控，再強的模型也只是放大失控。
ㅤ
我目前還沒能力做到他那個層次。但這次至少看清楚一件事：

進階使用 Coding Agent，不是更會寫 prompt，是把它從聊天工具升級成可管理的工程流程。
ㅤ
我會先從 plan-first 跟 worktree 隔離兩件事開始試。
ㅤ
不確定我做得到，但這個方向我看起來是對的。
ㅤ
ㅤ
參考：Tonyq 的 Better Agent Terminal — github.com/Tonyq1223/better-agent-terminal
