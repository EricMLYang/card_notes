【 1 個 bug → 4 個 user story → 16 個驗收標準 】
——Thoughtworks 工程師的 SDD 工具踩坑紀錄
ㅤ
你大概聽過 Spec-Driven Development。
ㅤ
先寫規格再寫 code，讓 AI 照著規格跑。
聽起來是 AI Coding 的正確方向，對吧？
ㅤ
但 Thoughtworks 的資深工程師 Birgitta Böckeler 實測了三個 SDD 工具後，得出一個反直覺的結論：
她寧可 review code，也不想 review 這些工具生出來的大量 markdown 文件。
ㅤ
更有趣的是她用 Kiro 修一個小 bug 的經歷。
工具把一個簡單的 bug fix 膨脹成 4 個 user story 和 16 個驗收標準。
ㅤ
這不是「規格驅動開發」，這是「規格驅動膨脹」。
ㅤ
我在讀這篇文章時一直想到一件事：
SDD 工具試圖用自然語言寫 spec，但我們在 AI Coding 實務中早就發現——code 本身（Interface + Test）才是表達規格最精準的語言。
ㅤ
SDD 繞了一圈，可能走到了錯誤的方向。
ㅤ
這篇是我消化 Birgitta 的分析後，加上自己的判斷框架寫成的拆解。
幫你看清楚 SDD 到底值不值得入場。
ㅤ
原文：Birgitta Böckeler,《Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl》
Martin Fowler Blog, 2025-10-15
https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
ㅤ
ㅤ
▋ SDD 不是一件事，是三個層次
ㅤ
很多人把 Spec-Driven Development 當成一個簡單的概念。
先寫規格，再讓 AI 寫 code。
ㅤ
但 Birgitta 在文章中拆出了一個分層模型，讓我眼前一亮。
SDD 其實有三個層次，目前大部分工具只做到最淺的那一層。
ㅤ
Spec-first：先寫好規格引導 AI 完成任務，完成後規格就丟了。
Spec-anchored：規格不只用在當下，還持續維護，跟著功能一起演化。活的文件，不是一次性指令。
Spec-as-source：最激進的一層。規格就是主要製品，人類只編輯規格，不碰 code。程式碼頂端標著 // GENERATED FROM SPEC - DO NOT EDIT。
ㅤ
這個分層讓你馬上看出差距。
目前 Kiro 和 spec-kit 都只做到 spec-first。
只有 Tessl 在嘗試 spec-as-source——但那個難度和風險，比 spec-first 高出不只一個數量級。
ㅤ
本質上，spec-first 就是「先定義驗證標準再動手」的倒推思維。
這個思維本身很有價值。
ㅤ
TDD 是它的 code-native 版本，SDD 是它的自然語言版本。
差別在：code 有編譯器保護，自然語言沒有。
ㅤ
ㅤ
▋ 三種工具，三種踩法
ㅤ
Birgitta 實測了三個工具。
每一個都有自己的設計哲學，也各自踩了不同的坑。
ㅤ
Kiro（AWS）是最輕量的。
流程是 Requirements → Design → Tasks，三步走，三個 markdown 文件。
簡潔，但問題出在它的「一體適用」。
ㅤ
Birgitta 拿 Kiro 修一個小 bug。
結果工具把它轉成 4 個 user story，附帶 16 個驗收標準。
其中一條：「As a developer, I want the transformation function to handle edge cases gracefully, so that the system remains robust when new category formats are introduced.」
ㅤ
一個 bug fix，被包裝成企業級需求文件。
殺雞用牛刀。
ㅤ
spec-kit（GitHub）是最完整的，也最重。
先建立「Constitution」作為整個 codebase 的不變規則，然後每個功能走 Specify → Plan → Tasks 流程。
每個 spec 會產生一堆 markdown：data-model、plan、tasks、spec、research、api、component⋯⋯
ㅤ
Birgitta 拿它做一個中等功能（大概 3-5 story points）。
光是 review 這些 markdown 就耗掉大量時間。
文件之間大量重複，有些還直接包含 code。
ㅤ
她的結論很直白：同樣的時間，用普通的 AI 輔助 coding 把功能寫完，掌控感還更強。
ㅤ
Tessl 是最有野心的（目前還在 beta）。
它是唯一嘗試 spec-as-source 的工具。
一個 spec 對應一個 code 檔案，改 spec 就重新生成 code。
ㅤ
聽起來很理想。
但 Birgitta 發現了 LLM 非確定性的問題：同一個 spec，生成多次，每次的 code 都不一樣。
ㅤ
她花了不少時間迭代 spec，讓它越來越精準，來提高一致性。
然後她意識到：這個過程，跟過去寫 MDD 規格的挑戰一模一樣。
ㅤ
要寫出「完整且無歧義的規格」，本身就是一個巨大的工程。
ㅤ
ㅤ
▋ 歷史不會重演，但會押韻
ㅤ
Birgitta 在文章裡提到一段重要的歷史類比。
ㅤ
二十年前，軟體業試過一個很類似的路線：Model-Driven Development（MDD）。
用模型定義規格，用 code generator 自動產生程式碼。
人類只編輯模型，不碰 code。
ㅤ
聽起來是不是很耳熟？
ㅤ
MDD 最終沒有在業界普及。
抽象層級尷尬，靈活性不夠，開銷太大。
ㅤ
Birgitta 的擔憂是：SDD 的 spec-as-source 可能正在結合 MDD 的限制和 LLM 的不確定性。
ㅤ
MDD 的問題是規格語言太死板。
LLM 的問題是輸出不可預測。
兩個加在一起，不是互補——是用一個問題換另一個問題。
ㅤ
她也公平指出：LLM 拿掉了 MDD 的一些硬限制。
你不再需要可解析的規格語言，也不需要寫複雜的 code generator。
代價就是非確定性。
ㅤ
讀到這裡，我想到一個判斷框架：做空檢驗。
每引入一個流程，都問自己：模型能力翻倍時，這個流程會不會自動變簡單？
ㅤ
如果模型夠強，能直接從對話理解需求，那精密的 spec 流程不會變簡單，只會變成技術負債。
ㅤ
ㅤ
▋ 四個結構性問題
ㅤ
讀完 Birgitta 的分析，再拿自己知識庫的筆記做交叉比對。
我歸納出 SDD 工具目前的四個結構性問題。
ㅤ
第一，規模不匹配。
一個流程不可能適配所有問題。
ㅤ
Kiro 用牛刀修 bug，spec-kit 用重型流程做中等功能。
不同問題需要不同的協作模式——從截圖除錯到同步核心開發，至少有五種。
一個工具試圖用單一流程覆蓋所有場景，這本身就是設計上的傲慢。
ㅤ
第二，review 的核心交易被惡化。
ㅤ
AI 協作的本質交易是：你用審查時間替代了寫代碼時間。
越好的規格帶來越好的 AI 輸出，邏輯沒錯。
但 spec-kit 用大量 markdown 替代你寫 code，結果你花更多時間 review 這些 markdown。
ㅤ
markdown 沒有編譯器保護、沒有 type check、沒有測試可以自動驗證。
ㅤ
Birgitta 說得好：「我寧可 review code 也不想 review 這一堆 markdown。」
ㅤ
第三，假控制感。
流程多不代表更安全。
ㅤ
spec-kit 有大量 checklist、template、constitution、research step。
但 Birgitta 發現 agent 經常不遵守這些指示——有時忽略，有時過度執行。
ㅤ
大 context window 不代表 AI 能用好所有 context。
流程多只給了人一種「我已經做了該做的事」的心理安全感。
真正的控制來自可驗證的約束——code 層級的 Interface 和 Test。
ㅤ
第四，自然語言 spec 不如 code spec。
這是我覺得最根本的問題。
ㅤ
SDD 工具用自然語言寫 spec。
但 code 本身就是表達系統設計意圖最精準的語言。
ㅤ
Interface 定義規格，Test 定義驗收條件。
兩者都有編譯器保護，可以自動驗證，可以重構。
ㅤ
自然語言 spec 做不到這些。
它只能靠人類肉眼 review，而人類的注意力是有限資源。
ㅤ
用 Interface + Test 鎖住頭尾、中間放給 Agent 跑，比寫一堆 markdown 來「引導」Agent 更可靠。
ㅤ
TDD 在 AI 時代的角色，已經從開發者自律工具變成 Agent 的控制介面。
SDD 用 markdown 做控制介面，走的是一條更脆弱的路。
ㅤ
ㅤ
▋ 那 SDD 完全沒價值嗎？
ㅤ
不是。
ㅤ
Spec-first 的思維是有價值的。
在 AI 時代，寫 code 的成本趨近於零。
但定義「該寫什麼 code」的成本不會消失。
ㅤ
開發價值正在從「寫程式」遷移到「寫規格」。
能把模糊需求翻譯成精確驗收條件的人，才是稀缺人才。
ㅤ
所以 SDD 的底層邏輯是對的：先想清楚要什麼，再讓 AI 去執行。
這跟「80% 規劃 20% 執行」的工作流是同一件事。
ㅤ
問題不在思維，在工具。
ㅤ
目前的 SDD 工具把一個好思維過度結構化，變成了沉重的流程。
ㅤ
流程產生大量 markdown。
markdown 需要人來 review。
review 消耗注意力。
而注意力，正是這個時代最稀缺的資源。
ㅤ
ㅤ
▋ 帶走思維，放下工具
ㅤ
SDD 的三層模型是一個好的認知框架，值得記住。
ㅤ
但如果你現在要選擇控制 AI Coding Agent 的方式，我的建議是：
ㅤ
先把 spec-first 的習慣融入日常。
每次讓 AI 寫 code 之前，先定義好 Interface 和 Test。
用 code 寫你的 spec，而不是用 markdown。
ㅤ
至於 SDD 工具本身？
等它們解決了規模匹配、review 效率、和可驗證性的問題，再看不遲。
ㅤ
Birgitta 在文章裡用了一個精準的德語詞來形容目前的 SDD 工具：
Verschlimmbesserung。
ㅤ
在試圖改善中，反而把事情弄得更糟。
ㅤ
不過，承認問題存在，本身就是改善的開始。
至少現在我們知道方向在哪裡了。
