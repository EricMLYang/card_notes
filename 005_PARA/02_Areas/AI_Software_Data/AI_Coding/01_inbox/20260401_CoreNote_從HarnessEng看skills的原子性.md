---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

【從 Harness Engineering 看 Skills 的原子性】

大家應該看過這種狀況。花了三個月精心調校一個 AI Agent 自動化流程。模型選了最貴的，context 開到最大，四十支 skills 一支一支接上去。Prompt 寫到三千字，每個字都經過反覆推敲。Demo 的時候，大家都很驚豔。

然後上 production 就慢慢失靈了。

那是一種沒有爆炸聲的失靈，沒有引擎蓋冒煙的失靈。只是默默的，在某個沒人注意的交流道，失去了動力。儀表板沒有警告燈，或是有，但沒有人看到。四十支工具安靜地躺在那裡，像一把再也沒被打開的瑞士刀。

大家嘗試修復，很快的又好了，但然後，又會不知道為什麼，某個工具突然連不上，edge case 一再發生。升級了模型，反而行為又跑掉。就像換了新的收音機，同樣一首歌的節奏卻悄悄偏移了。到了 Q3，原本號稱可以幫團隊每週省下 20 小時的 agent 沒有人再提起，就像夏天結束後再也沒有人去的那座海水浴場。售票亭還立著，海浪還在拍打，但沙灘上只剩下風。

▋關於 Harness Engineering

最近這個詞反覆出現，像一張張被風吹到腳邊的傳單。

每個人都太想讓 Agent 長時間跑下去了。持續地、安靜地、大規模地運轉，還不能偏離軌道。這種期望說起來理所當然，就像期待一台洗衣機按下去就能安安穩穩地把衣服洗好。但事實上這件事難得多。

人們試過各種方法。Stop hook、ralph wiggum、oh my opencode，還有 /loop。每一種都像是在深夜廚房裡嘗試不同的食譜，加一點這個，調一點那個，打開烤箱看一眼，關上，再等。

然後某一天，它真的跑起來了。長時間、穩穩地，產出了符合預期的東西。那個瞬間，你會像中了彩券一樣急忙按下截圖鍵，把螢幕畫面發到社群平台上。因為你知道這可能只是幸運。

要能達到這個目標，目前大家認為最主要關鍵在於模型外面的那一層控管機制。大概是三塊。

第一塊是評估迴圈。

它處理的問題很簡單，你不能讓一個人自己幫自己打分數。就好像一個剛進公司的實習生交出了一份年度報告，你問他寫得怎麼樣，他一定會說還可以。每個人都會說還可以。所以你需要一個獨立的人來驗收。Harness 做的事情就是這樣：先把「什麼叫做好」這件事定義清楚，像在牆上畫好一條線，然後讓 agent 去做，做完了，有人拿著尺去量。

第二塊是架構約束。

你不能讓 agent 隨心所欲地呼叫工具。就像你不能讓一個廚師在廚房裡愛開哪個瓦斯爐就開哪個。OpenAI Codex 團隊的做法是在工具裡寫死分層規則，用 linter 強制執行，像鐵軌上的柵欄。Types 只能依賴 Types，Service 只能依賴 Types。誰違反了就直接被擋下來。規則不是寫在什麼「團隊規範文件」裡等人自覺遵守的。那種東西，說穿了就像貼在冰箱上的節食宣言，三天以後就沒有人再看一眼了。

第三塊是記憶治理。

這個問題比較微妙。想像一間圖書館，好幾個人在裡面寫筆記，放在同一個書架上。Agent A 寫了什麼，Agent B 翻開就當真了。但如果 A 寫的是錯的呢？一個幻覺就這樣安安靜靜地傳播開來，像一個不實的傳言在小鎮裡擴散。PrismerCloud 的做法是把每一次經驗先當作一個未經證實的耳語。驗證通過了，才把它提煉成基因。沒通過的，就讓它留在風裡。

三塊東西加在一起，撐起了所謂 Harness Engineering 這個詞。

▋Skill 的原子性

Harness Engineering 很重要。但我最近注意到還有一個東西比較少人提，那就是 Skill 的原子性。

每個 Skill 要做到可以獨立運作，而不是變成另一個版本的 monolith。

一支 skill 如果在裡面塞了五件事的詳細流程，那它就不叫 skill 了。那只是一個被塞得滿滿的 prompt，像一個什麼都往裡面丟的冰箱。剩菜、過期的醬油、不知道誰買的奇異果。你沒辦法只拿出其中一樣來測試，出了問題也搞不清楚是哪一樣壞了。而且這個冰箱只會越來越滿，直到有一天門關不起來，也沒有人願意打開它。

Atomic Skill 的樣子大概是這樣的：

• fetch_page_text(url)，吃一個網址，吐出結構化的內容
• write_to_memory(key, value)，寫進去，拿到確認
• evaluate_task_completion(task, result)，吃任務與結果，吐出 pass 或 fail
• route_by_intent(input)，吃分類，吐出路由決定

每一個都是一行就能說完的東西。進來什麼，出去什麼。邊界乾乾淨淨，像剛洗好的玻璃杯。

Skill 可以被其他 Skill 呼叫。但不是說每支 skill 都要獨立對外服務，而是說每支 skill 有明確的 input 和 output，可以被組合，可以被替換，可以被單獨測試。一支大的 skill 內部如果是由幾個 atomic 子 skill 組成的，那就像一個樂團，每個人負責自己的聲部，同樣是乾淨的架構。

但也不是所有東西都要原子性。

這點很重要，不然你會陷入 over-engineer 的泥沼。目標不是把系統拆到最小單位，是拆到有意義的邊界。兩件事如果總是一起發生，從來不分開，硬拆開只是徒增煩惱。就像你不能把一雙襪子拆成左手一隻右手一隻來分別洗。Atomic skill 是手段，不是目的。

Terminal Bench 2.0 把同一個 agent 從一本厚厚的、充滿指令的 harness，換成精實的、有結構的 harness。模型完全沒換。任務完成率多了十四個百分點。十四個百分點。

CORE-Bench 更放寬了 Opus 4.5 的 scaffold 限制，修了一個 eval 的 bug，分數從 42% 跳到 95%。從四十二到九十五。這不是換了一個更聰明的腦袋。這只是把眼鏡擦乾淨了，讓它終於可以看清楚東西。

▋充滿架構美感的 Skill Graph

大部分 Agent Framework 會卡住，是因為它們試著變成 monolith。把 Memory、工具、eval、編排全部包在一個系統裡，像一間什麼都賣的百貨公司。你只透過一個櫃檯跟它互動，而那個櫃檯後面是一團你永遠看不見的混亂。把所有東西抽象進一個地方，複雜度並沒有消失。它只是被推到了你看不見的角落，像把雜物塞進衣櫃裡然後把門關上。衣櫃還是滿的。

另一條路是最小表面積。Skills 獨立定義、獨立運作，像抽屜裡各自裝著不同工具的隔間。Harness 提供的是組合的規則，而不是實作本身。Eval 是外部的、自動化的。Memory 是基礎設施，不是什麼神秘的黑魔法。

這才是 Claude Code 實際運作的方式。CLI、VS Code 擴充套件、Slack 整合、GitHub Actions Bot，這些都是同一張 skill graph 的不同入口。就像同一棟建築有好幾扇門，走進去是同一個大廳，底下共享同一套 evaluation 的紀律。最後會贏的 framework，不是功能最多的那個。是最不強迫你接受一堆你不需要的結構的那個。就像最好的旅館，不是設施最多的，是你走進去覺得什麼都剛剛好的。

▋試想：生產級 Agent 的判斷標準

接下來，一個 production agent 好不好，不會再用工具數量或 context window 的大小來衡量。就像你不能用一口袋裡裝了幾把鑰匙來判斷一個人會不會開鎖。

會用這些東西來衡量。

第一，eval 精準度。你能不能明確地指出，是哪一個 skill 失敗了，原因又是什麼。就像一個好的醫生，不是給你一個籠統的「身體有點不對勁」，而是告訴你哪裡出了問題，為什麼。

第二，skill graph 的可讀性。你能不能在一張白紙上，把整個系統畫出來。不需要投影機，不需要三小時的簡報。就一張白紙，一支筆。如果畫不出來，那表示系統已經複雜到沒有人真正理解它
了。

第三，當某一個 skill 吐出了一個壞掉的輸出，那個問題會不會一路燒到其他 skill。這叫 memory 有沒有邊界。就像一間公寓的防火牆，一戶失火，不該把整棟樓都燒了。

第四，你能不能把一個 skill 抽換成更好的版本，而不需要把整個 agent 重寫。這叫可升級性。就像換一條琴弦，不需要把整把吉他丟掉。

這些決定了你的 agent 會真的走出大門，還是在半路上就停下來，像一台拋錨在路邊的車，閃著黃燈，等著有人來拖走。

Harness Engineering 加 Atomic Skill 能讓系統足夠乾淨，乾淨到每個問題都可以被正確地測量到，每個 skill 都可以被單獨替換。沒有這個哲學在背後支撐的 agent，會一直堆在 2025 年的亂葬崗旁邊，不是因為模型不夠好，是因為系統本身不夠透明。

Model 是原料。Skill 是工具。Harness 是讓工具湊在一起幹活的系統。先把系統架構建立，也許才是好的開始。

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：作者把 production agent 失敗的根因從「模型不夠強」拉到「外圍系統不夠透明」。Harness Engineering（評估迴圈、架構約束、記憶治理）+ Atomic Skill（一卡一事、可單測可替換）= 讓 agent 真的能跑下去的兩根支柱。並用 Terminal Bench 2.0、CORE-Bench 數字佐證 harness 改良比換模型更有效。
- 作者挑戰的預設：挑戰「工具數量 / context window 大小 = agent 強度」「framework 越大越完整」這兩個慣性，主張「最小表面積」「skill graph 可讀性」才是新判準。
- 個人映射：高度補強 capture profile 的「Harness / 驅動框架視角」「Repo-as-Worker / Agent-as-Repo」「卡片化標準」三條主軸；尤其「skill graph 一張白紙畫得出來」可直接遷移到知識管理 / 卡片系統設計。

## B. 候選卡（Lite）

序號 1
- 候選標題：Production Agent 失靈是慢性失能而非急性故障
- 分級：Core
- 類型：Pattern
- 核心內容：production agent 不會「爆炸式」失敗，而是默默失去動力——某工具突然連不上、edge case 一再發生、升級模型反而行為跑掉。這種失靈不會觸發 alarm，最後變成「沒人再提的 agent」。識別這種失敗模式比單次故障處理更重要。
- 保留理由：把「agent 上線後緩慢退化」具象化，是建立監控與生命週期管理的觸發點。
- 待補強處：缺乏可量化的「退化訊號」（例如成功率、token 浪費率的時間序列）。
- 初步知識鉤子：與 20260412 OpenAI misalignment monitoring（事中監控+事後分級）對接、可觀測性、agent SLO

序號 2
- 候選標題：Harness Engineering 三支柱：評估迴圈、架構約束、記憶治理
- 分級：Core
- 類型：Principle
- 核心內容：(1) 評估迴圈：自己不能評自己，需要外部裁判先把「好」定義清楚再量；(2) 架構約束：用 linter 強制分層規則，規則寫在工具裡而非團隊規範文件，因為「冰箱貼紙三天就沒人看」；(3) 記憶治理：A 寫的 B 別當真，先當未經證實的耳語，驗證通過才提煉成基因。三者共同撐起 harness。
- 保留理由：高密度 framework，三點皆有具體機制與生活化比喻，可作為設計 agent 系統的 checklist。
- 待補強處：三支柱在小團隊資源約束下，哪一塊優先投資？缺取捨指引。
- 初步知識鉤子：與 20260407 Fowler 的 feedforward/feedback、computational/inferential controls 對應；與 20260414 Pang 的「自我修復回饋迴圈」對應

序號 3
- 候選標題：Atomic Skill 的判準：一行說完、邊界乾淨、可單測可替換
- 分級：Core
- 類型：Heuristic
- 核心內容：Atomic skill 的樣子像 fetch_page_text(url)、write_to_memory(key,value)、evaluate_task_completion(task,result)、route_by_intent(input)——進來什麼出去什麼，邊界乾乾淨淨。Skill 之間可被組合呼叫，但每個都有明確 I/O。反例：在一支 skill 裡塞五件事的詳細流程＝塞滿冰箱的 monolith prompt。
- 保留理由：直接呼應個人 capture profile 的「卡片化標準」與「平台化能力模組（Adapter Pattern）」，可遷移到知識卡片設計與 skill 庫管理。
- 待補強處：與「不是所有東西都要原子性」的邊界判準（兩件事總是一起發生就不該拆）需要更明確的識別法。
- 初步知識鉤子：Unix philosophy、單一職責原則、與 20260328 gstack（13 個 slash command）對照、Adapter Pattern

序號 4
- 候選標題：原子化是手段不是目的——over-engineer 的反向警告
- 分級：Core
- 類型：Warning
- 核心內容：目標不是把系統拆到最小單位，是拆到「有意義的邊界」。兩件事如果總是一起發生從不分開，硬拆只是徒增煩惱（一雙襪子不能拆成左右手分別洗）。Atomic 是手段，能力組合的清晰度才是目的。
- 保留理由：是序號 3 的對沖護欄，避免把「原子化」變成新的教條；對「框架信徒」是必要的反例。
- 待補強處：缺判準——「總是一起發生」如何量化？三次以上？跨多少 use case？
- 初步知識鉤子：YAGNI、premature abstraction、與 20260328 gstack（複合 slash command）的取捨對照

序號 5
- 候選標題：Harness 改良的 ROI 可能高於換模型——Terminal Bench / CORE-Bench 的證據
- 分級：Support
- 類型：Pattern
- 核心內容：Terminal Bench 2.0 同 agent 換成「精實有結構的 harness」（模型沒換），任務完成率提升 14 個百分點。CORE-Bench 放寬 Opus 4.5 scaffold 限制並修一個 eval bug，分數從 42% 跳到 95%。佐證「擦乾淨眼鏡」比「換更聰明的腦袋」回報更高。
- 保留理由：用具體數字支撐 harness 投資的策略性，可作為向團隊說服的素材。
- 待補強處：缺乏「同模型不同 harness」「同 harness 不同模型」的對照矩陣，難判斷 harness 與模型升級的邊際報酬。
- 初步知識鉤子：bench 數字的 framing、與 20260414 Pang「Opus 4.6 才做得到」的模型依賴形成對話張力

序號 6
- 候選標題：Production Agent 的四個新判準：eval 精準度、skill graph 可讀性、memory 邊界、可升級性
- 分級：Core
- 類型：Heuristic
- 核心內容：(1) eval 精準度：能指出哪個 skill 失敗、原因；(2) skill graph 可讀性：能在白紙畫出整個系統；(3) memory 邊界：壞輸出不會燒到其他 skill，像公寓防火牆；(4) 可升級性：抽換 skill 不需要重寫整個 agent。這四項取代「工具數 / context window」成為新判準。
- 保留理由：直接形成 production-readiness checklist，可拿來評估自家或客戶 agent 系統。
- 待補強處：每項判準該如何量測？eval 精準度有公式嗎？memory 邊界如何測試？
- 初步知識鉤子：可遷移到知識卡片系統的健康度評估、與 20260407 Fowler 的 harnessability、與 20260414 Pang 的 CI/CD 六階段對接

序號 7
- 候選標題：最小表面積 framework 會贏，不是功能最多的會贏
- 分級：Support
- 類型：Principle
- 核心內容：Monolith framework（Memory、工具、eval、編排全包）的複雜度沒消失，只是被推到看不見的角落。最小表面積路線把 skills 獨立、harness 提供組合規則、eval 外部化、memory 是基礎設施。Claude Code 的 CLI / VS Code / Slack / GitHub Actions 是同一張 skill graph 的不同入口（同棟建築不同門）。
- 保留理由：對 framework 選型的取捨原則，可遷移到自家 repo / agent 平台設計。
- 待補強處：何時最小表面積反而成為負擔？小團隊缺人時是否需要 monolith 的便利性？
- 初步知識鉤子：API 設計哲學、與 20260409 Anthropic Managed Agents（包山包海平台）的取捨張力

## C. 建議送 refine 的項目
- 序號 1、2、3、4、6（Core，皆可獨立成卡）
- 序號 5、7 為 Support，與序號 2、3 有合併潛力

## D. 呼叫 refine-cards
- 將 7 張候選卡交由 refine-cards 精煉；高度需注意與 20260407 Fowler、20260414 Pang 兩篇 harness 文章的概念去重，可能形成「harness 三部曲」的合併卡組。
