Anthropic 今日宣布Project Glasswing 計畫 - 也展示之前洩漏出來的下一代Mythos模型如何運用在計劃中，文章中也有跟Opus的比較測試結果，這計畫集結了 Amazon Web Services、Anthropic、Apple、Broadcom、Cisco、CrowdStrike、Google、JPMorganChase、Linux 基金會、Microsoft、NVIDIA 與 Palo Alto Networks，共同致力於保護全球最關鍵的軟體基礎設施。

促使 Anthropic 成立 Project Glasswing 的原因，來自一款由 Anthropic 訓練的全新前沿模型所展現的能力-Anthropic 認為這些能力有可能從根本上重塑網路安全的面貌。Claude Mythos Preview 是一款通用型、尚未對外發布的模型，文章中表示：AI 模型的能力已達到一個門檻，在發現和利用軟體漏洞的能力上，除了極少數頂尖人類專家外，已經超越幾乎所有人。

Mythos Preview 已經找到數千個高嚴重性漏洞，其中涵蓋了每一個主流作業系統和網頁瀏覽器。以 AI 目前的進步速度來看，這類能力的擴散只是時間問題，而且可能擴散到不致力於安全部署的行為者手中。其對經濟、公共安全和國家安全造成的衝擊可能極為嚴重。Project Glasswing 是一次緊迫的嘗試，旨在將這些能力率先用於防禦目的。

作為 Project Glasswing 的一部分，上述創始夥伴將使用 Mythos Preview 來強化自身的防禦性安全工作；Anthropic 也會分享從中獲得的經驗，讓整個產業都能受益。此外，Anthropic 還將存取權限擴展給另外超過 40 個組織 - 這些組織負責建構或維護關鍵軟體基礎設施，讓它們能夠使用該模型來掃描並加固自有系統和開源系統。Anthropic 承諾為這些工作提供最高 1 億美元的 Mythos Preview 使用額度，並另外向開源安全組織直接捐贈 400 萬美元。

Project Glasswing 只是一個起點。沒有任何單一組織能獨力解決這些網路安全問題：前沿 AI 開發者、其他軟體公司、安全研究人員、開源維護者以及全球各國政府，都扮演著不可或缺的角色。

━━━━━━━━━━━━━━━━━━━━
▍AI 時代的網路安全
我們每天依賴的軟體，負責運行銀行系統、儲存醫療紀錄、串接物流網路、維持電力系統運作等，一直都存在漏洞。大多數漏洞無關緊要，但有些是嚴重的安全缺陷，一旦被發現，就可能讓攻擊者劫持系統、癱瘓運作或竊取資料。

我們已經親眼目睹網路攻擊對企業網路、醫療系統、能源基礎設施、交通樞紐，以及全球各國政府機構資訊安全所造成的嚴重後果。在國際舞台上，來自中國、伊朗、北韓和俄羅斯等國家支持的攻擊行動，已威脅到支撐民間生活和軍事戰備的基礎設施。即便是較小規模的攻擊，例如針對個別醫院或學校的攻擊，仍然可能造成巨大的經濟損失、洩露敏感資料，甚至危及人命。目前全球網路犯罪的財務成本難以精確估算，但每年可能高達約 5,000 億美元。

許多軟體缺陷之所以多年來未被察覺，是因為發現和利用它們需要極為專業的知識，而擁有這種專業能力的安全專家屈指可數。隨著最新前沿 AI 模型的出現，發現和利用軟體漏洞所需的成本、人力和專業門檻都大幅降低。過去一年間，AI 模型在閱讀和推理程式碼方面的能力大幅提升，尤其在偵測漏洞並設計利用方法方面，展現出驚人的天賦。Claude Mythos Preview 在這些網路安全技能上實現了一次飛躍，它所發現的漏洞，有些在人類數十年的審查和數百萬次自動化安全測試中都未曾被識別，而它開發的攻擊手法也日益精密。

距離首屆 DARPA 網路大挑戰賽（Cyber Grand Challenge）已經過了十年，如今前沿 AI 模型在發現和利用漏洞方面已具備與頂尖人類競爭的實力。如果缺乏必要的安全防護，這些強大的網路攻防能力可能被用來利用全球最重要軟體中存在的眾多缺陷。這將使各類網路攻擊變得更加頻繁、破壞力更強，並賦予美國及其盟友的對手更大的攻擊能力。因此，應對這些問題是民主國家的重要安全優先事項。

儘管 AI 強化網路攻擊的風險確實嚴峻，但仍有理由保持樂觀：同樣使 AI 模型在不當之手中具有危險性的能力，也讓它們在發現和修復重要軟體缺陷方面無比珍貴 - 同時也能產出安全漏洞大幅減少的新軟體。Project Glasswing 正是朝著在即將到來的 AI 驅動網路安全時代中，為防禦方建立持久優勢所邁出的重要一步。

━━━━━━━━━━━━━━━━━━━━
▍以 Claude Mythos Preview 辨識漏洞與攻擊手法
過去幾週，Anthropic 使用 Claude Mythos Preview 辨識出了數千個零日漏洞（即先前軟體開發者未知的缺陷），其中許多屬於關鍵等級，涵蓋每一個主流作業系統和主流網頁瀏覽器，以及一系列其他重要軟體。

在 Anthropic 的 Frontier Red Team 部落格文章中，提供了其中一部分已修補漏洞的技術細節，以及 Mythos Preview 在某些案例中設計出的利用方式。Mythos Preview 幾乎能完全自主地辨識出這些漏洞中的絕大多數，並開發出許多相關的攻擊手法，完全不需要任何人類引導。以下是三個具體案例：

OpenBSD 中一個存在 27 年的漏洞：Mythos Preview 在 OpenBSD 中找到了這個漏洞。OpenBSD 以全球最注重安全加固的作業系統之一著稱，廣泛用於運行防火牆及其他關鍵基礎設施。該漏洞允許攻擊者僅透過連線到目標機器，就能遠端使其當機崩潰。

FFmpeg 中一個存在 16 年的漏洞：FFmpeg 被無數軟體用於編解碼影片。這個漏洞存在於一行自動化測試工具已經命中五百萬次、卻從未捕捉到問題的程式碼中。

Linux 核心中的漏洞鏈：該模型自主發現並串連了 Linux 核心中的多個漏洞，Linux 核心是運行全球絕大多數伺服器的軟體，使攻擊者能從普通使用者權限提升到完全控制整台機器。

上述漏洞已全部回報給相關軟體的維護者，且均已修補完畢。對於其他眾多漏洞，Anthropic 今日提供了相關細節的加密雜湊值（詳見 Red Team 部落格），待修補完成後再公開具體內容。

▍評測基準
CyberGym 等評測基準也印證了 Mythos Preview 與 Anthropic 次強模型 Claude Opus 4.6 之間的顯著差距：

CyberGym（網路安全漏洞重現）：Mythos Preview 83.1%　／　Opus 4.6 66.6%

▍合作夥伴回饋
除了 Anthropic 自身的工作外，許多合作夥伴已在過去數週使用 Claude Mythos Preview，以下是他們的發現與評價：

Cisco — Anthony Grieco，資深副總裁暨首席安全與信任長：
AI 的能力已跨越一個門檻，從根本上改變了保護關鍵基礎設施免受網路威脅所需的急迫性，而這個變化不可逆轉。他們基於這些模型的基礎工作證明，可以以前所未有的速度和規模辨識並修復硬體與軟體的安全漏洞。這是一個深刻的轉變，也是一個明確的信號，舊有的系統加固方式已不再足夠。這就是 Cisco 加入 Project Glasswing 的原因，這項工作太重要、太緊迫，無法獨自完成。

AWS — Amy Herzog，副總裁暨資訊安全長：
AWS 在威脅出現之前就建立防禦，從自研晶片到整個技術堆疊。安全不是一個階段，而是持續且嵌入所有工作中的核心。他們的團隊每天分析超過 400 兆筆網路流量以偵測威脅，AI 是他們大規模防禦的核心。他們已在自身安全運營中測試 Claude Mythos Preview，將其應用於關鍵程式碼庫，且已在協助強化程式碼品質。

Microsoft — Igor Tsyganskiy，網路安全暨 Microsoft Research 執行副總裁：
當我們進入一個網路安全不再受限於純人類能力的階段，負責任地使用 AI 來大規模提升安全和降低風險的機會是前所未有的。加入 Project Glasswing 並取得 Claude Mythos Preview 的存取權限，讓他們能夠及早辨識和緩解風險，強化安全與開發解決方案，更好地保護客戶和 Microsoft。在 Microsoft 的開源安全基準 CTI-REALM 上測試時，Claude Mythos Preview 相較先前的模型展現了大幅改進。

CrowdStrike — Elia Zaitsev，技術長：
從漏洞被發現到被攻擊者利用之間的時間窗口已經坍塌，過去需要數月的過程，現在靠 AI 只需數分鐘。Claude Mythos Preview 展示了防禦者大規模行動的可能，而攻擊者必然也會尋求利用相同的能力。這不是放慢腳步的理由，而是要一起更快行動的理由。如果你想部署 AI，就需要安全，這就是 CrowdStrike 從第一天就參與的原因。

Linux 基金會 — Jim Zemlin，執行長：
過去，安全專業知識是擁有大型安全團隊的組織才有的奢侈品。開源軟體的維護者——他們的軟體支撐著全球大部分關鍵基礎設施，長期以來只能自力更生地處理安全問題。開源軟體構成現代系統中絕大多數的程式碼，包括 AI 代理用來撰寫新軟體的那些系統本身。通過讓這些關鍵開源程式碼庫的維護者使用能夠主動辨識和修復漏洞的新一代 AI 模型，Project Glasswing 提供了一條可行的路徑來改變這個等式。

JPMorganChase — Pat Opet，資訊安全長：
推動金融體系的網路安全與韌性是 JPMorganChase 使命的核心。他們相信，當領先機構攜手應對共同挑戰時，整個產業才會最強大。Project Glasswing 提供了一個獨特的早期機會。

Google — Heather Adkins，安全工程副總裁：
Google 樂見此跨產業網路安全倡議的成形，並透過 Vertex AI 向參與者提供 Mythos Preview。產業在新興安全議題上的合作一向至關重要，無論是後量子密碼學、負責任的零日漏洞揭露、安全開源軟體，還是防禦基於 AI 的攻擊。Google 長期以來相信 AI 在網路防禦方面既帶來新挑戰也開啟新機會，因此打造了 Big Sleep 和 CodeMender 等 AI 驅動工具來發現和修復關鍵軟體缺陷。

Palo Alto Networks — Lee Klarich，首席產品暨技術長：
過去幾週，他們使用 Claude Mythos Preview 辨識出了前一代模型完全遺漏的複雜漏洞。這不僅是發現先前隱藏漏洞的重大突破，也標誌著一個危險的轉折，攻擊者即將能比以往更快地找到更多零日漏洞並開發攻擊手法。這些模型顯然需要交到開源維護者和全球防禦者手中，在攻擊者取得存取之前找到並修復漏洞。

▍編碼與推理能力基準
Claude Mythos Preview 強大的網路安全能力源於其出色的代理式程式碼撰寫與推理技能。以下為多項軟體開發與推理評測的成績：

代理式程式碼撰寫（Agentic Coding）：
SWE-bench Pro　　　　　Mythos 77.8%　／　Opus 4.6 53.4%
Terminal-Bench 2.0　　　Mythos 82.0%　／　Opus 4.6 65.4%
SWE-bench Multimodal　　Mythos 59.0%　／　Opus 4.6 27.1%（內部實作）
SWE-bench Multilingual　 Mythos 87.3%　／　Opus 4.6 77.8%
SWE-bench Verified　　　Mythos 93.9%　／　Opus 4.6 80.8%

推理（Reasoning）：
GPQA Diamond　　　　　　　Mythos 94.6%　／　Opus 4.6 91.3%
Humanity's Last Exam（無工具）Mythos 56.8%　／　Opus 4.6 40.0%
Humanity's Last Exam（有工具）Mythos 64.7%　／　Opus 4.6 53.1%
備註：Humanity's Last Exam 上 Mythos 在低努力程度下仍表現良好，可能暗示一定程度的記憶化。

代理式搜尋與電腦操作（Agentic Search and Computer Use）：
BrowseComp　　　Mythos 86.9%　／　Opus 4.6 83.7%
OSWorld-Verified　Mythos 79.6%　／　Opus 4.6 72.7%
備註：BrowseComp 上 Claude Mythos Preview 分數高於 Opus 4.6，同時使用的 token 數量僅為後者的 4.9 分之一。

Anthropic 不打算將 Claude Mythos Preview 對外公開提供，但最終目標是讓使用者能夠安全地大規模部署 Mythos 級別的模型，不僅用於網路安全，也用於這類高度 capable 模型將帶來的無數其他效益。

━━━━━━━━━━━━━━━━━━━━
▍Project Glasswing 的後續計畫
今日的宣布只是一項長期工作的開端。要取得成功，需要科技產業內外的廣泛參與。
Project Glasswing 的合作夥伴將獲得 Claude Mythos Preview 的存取權限，用於發現和修復其基礎系統中的漏洞或弱點，這些系統代表了全球共享網路攻擊面的極大比例。Anthropic 預期這項工作將聚焦於本地漏洞偵測、二進位檔的黑箱測試、端點安全加固以及系統的滲透測試等任務。

Anthropic 承諾的 1 億美元模型使用額度將涵蓋研究預覽期間的大量使用。之後，Claude Mythos Preview 將以每百萬 token 輸入 25 美元 / 輸出 125 美元的價格提供給參與者（可透過 Claude API、Amazon Bedrock、Google Cloud 的 Vertex AI 以及 Microsoft Foundry 存取）。

除了使用額度的承諾外，Anthropic 還向 Linux 基金會旗下的 Alpha-Omega 和 OpenSSF 捐贈了 250 萬美元，向 Apache 軟體基金會捐贈了 150 萬美元，以幫助開源軟體維護者因應這一變化中的格局（有興趣的維護者可透過 Claude for Open Source 計畫申請存取）。

━━━━━━━━━━━━━━━━━━━━
▍附錄

計畫名稱取自玻璃翼蝶（glasswing butterfly，學名 Greta oto）。這個比喻可從兩個面向理解：蝴蝶的透明翅膀讓牠能隱身於眾目之中，就像本文所討論的那些隱藏漏洞；同時，這些翅膀也讓牠能躲避傷害——這正如同 Anthropic 所倡議的透明作法。

「Mythos」源自古希臘語，意為「話語」或「敘事」：文明藉以理解世界的故事體系。