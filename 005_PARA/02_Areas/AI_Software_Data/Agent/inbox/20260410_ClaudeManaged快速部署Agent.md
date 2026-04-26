---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

Claude Managed Agents：讓你的產品上線速度快 10 倍，Anthropic 推出 Claude Managed Agents - 一套可組合的 API 套件，用於大規模建構與部署雲端託管的智能代理（Agent）。（可以看看影片Notion 產品經理怎麼說明示範，覺得看起來蠻有潛力的，是Anthorpic 持續弄了幾個月的產品，可以讓非RD人員有機會操作Agent上線）

在此之前，建構 Agent 意味著你必須在安全基礎設施、狀態管理、權限控管以及因每次模型升級而重構 Agent 迴圈上耗費大量開發資源。Managed Agents 將專為效能調校的 Agent 調度引擎與生產級基礎設施結合起來，讓你從原型到上線只需數天，而非數月。

無論你是在建構單一任務執行器，還是複雜的多 Agent 管線，你都可以專注在使用者體驗上，而非營運負擔。Managed Agents 現已在 Claude Platform 上以公開測試版（public beta）提供。

━━━━━━━━━━━━━━━━━━━━
▍建構與部署 Agent，速度快 10 倍
要交付一個生產級 Agent，需要沙箱化程式碼執行、檢查點機制、憑證管理、範圍化權限以及端到端追蹤。這些在你交付任何使用者可見的功能之前，就已經是數月的基礎設施工作。

Managed Agents 替你處理這些複雜性。你只需定義 Agent 的任務、工具和防護欄，我們在我們的基礎設施上運行它。內建的調度引擎會決定何時呼叫工具、如何管理上下文，以及如何從錯誤中恢復。

Managed Agents 包含：
生產級 Agent——安全沙箱、身份驗證和工具執行全部為你處理。
長時間運行的工作階段——可自主運行數小時，進度和輸出即使在斷線後也會持久保存。

多 Agent 協調——Agent 可以啟動並指揮其他 Agent，以平行化處理複雜工作（目前為研究預覽版，可申請存取）。

受信任的治理機制——讓 Agent 以範圍化權限存取真實系統，身份管理和執行追蹤均已內建。

━━━━━━━━━━━━━━━━━━━━
▍專為充分發揮 Claude 潛力而設計
Claude 模型天生就是為 Agent 工作而打造的。Managed Agents 是專門為 Claude 量身定制的，讓你以更少的工作量獲得更好的 Agent 成果。

使用 Managed Agents，你只需定義目標和成功標準，Claude 就會自我評估並反覆迭代直到達成目標（目前為研究預覽版，可申請存取）。在你需要更嚴格控制時，它也支援傳統的提示與回應工作流程。

在結構化檔案生成的內部測試中，Managed Agents 的任務成功率比標準提示迴圈高出多達 10 個百分點，且在最困難的問題上獲得了最大的提升。

工作階段追蹤、整合分析和故障排除指引直接內建於 Claude Console 中，讓你可以檢視每一次工具呼叫、決策和失敗模式。

━━━━━━━━━━━━━━━━━━━━
▍合作夥伴案例
Notion 讓團隊可以直接在其工作空間中將工作委派給 Claude（現已在 Notion Custom Agents 的私人 Alpha 版中提供）。工程師用它來交付程式碼，知識工作者用它來製作網站和簡報。數十項任務可同時平行運行，整個團隊協同處理產出成果。

Rakuten（樂天） 在產品、銷售、行銷和財務各部門部署了企業級 Agent，這些 Agent 可整合到 Slack 和 Teams 中，讓員工分配任務並收回包括試算表、簡報和應用程式在內的交付物。每個專業 Agent 都在一週內完成部署。

Asana 建構了「AI 隊友」（AI Teammates），這是一種在 Asana 專案中與人類協同工作的 AI Agent，能承接任務並草擬交付物。團隊使用 Managed Agents 以遠超以往的速度新增進階功能。

Vibecode 協助客戶從提示到部署應用程式，使用 Managed Agents 作為預設整合，為新一代 AI 原生應用提供動力。使用者現在建立相同基礎設施的速度至少快了 10 倍。

Sentry 將其除錯 Agent「Seer」與一個由 Claude 驅動的 Agent 配對，後者負責撰寫修補程式並提交 Pull Request，讓開發者從一個被標記的 Bug 到可供審閱的修復方案只需一個流程。這項整合在 Managed Agents 上僅花了數週而非數月即上線。

━━━━━━━━━━━━━━━━━━━━
▍合作夥伴評價精選
Vibecode 聯合創辦人 Ansh Nanda：在 Managed Agents 之前，使用者必須手動在沙箱中運行 LLM、管理生命週期、配備工具並監督執行，這個過程可能需要數週甚至數月。現在只需幾行程式碼就能完成，這為開發者和「氛圍編碼者」（vibe coders）打開了全新的可能性。

Sentry AI/ML 工程資深總監 Indragie Karunaratne：客戶現在可以從 Seer 的根因分析直接跳到由 Claude 驅動的 Agent 來撰寫修復並提交 PR。Managed Agents 不僅讓初始整合從數月縮短到數週，還消除了維護自建 Agent 基礎設施的持續營運負擔。

Atlassian 團隊協作產品集團資深副總裁 Sanchan Saxena：透過 Managed Agents，我們能在數週而非數月內將開發者 Agent 直接建構到團隊日常依賴的 Jira 工作流程中。Managed Agents 處理了沙箱、工作階段和範圍化權限等困難部分，讓工程師能專注於為終端使用者打造出色的功能。

某 CTO Javed Qadrud-Din：使用 Managed Agents，我們建構了一個系統，能從使用者的文件和通訊中提取資訊來回答任何查詢，即使我們沒有為此建構特定工具。Managed Agents 能即時編寫所需的任何工具，開發時間縮短了 10 倍。

某聯合創辦人 John Han：Managed Agents 讓我們建構可投入生產的會議準備 Agent 快了 3 倍，從構想到上線只用了幾天。自訂工具讓我們能接入行事曆和通訊錄資料，MCP 簡化了與外部系統的連接，託管引擎處理了沙箱執行和內建網頁搜尋等繁重工作。

Notion 產品經理 Eric Liu：我們希望 Notion 成為團隊與 Agent 協作完成工作的最佳場所。Managed Agents 能處理長時間運行的工作階段、管理記憶體並持續交付高品質的輸出。使用者現在可以委派開放性、複雜的任務而無需離開 Notion。

Rakuten AI 業務總經理 Yusuke Kaji：透過 Managed Agents，進階使用者能跨越單一專業，在工程、產品、銷售、行銷和財務等多個領域貢獻。每個專業 Agent 在一週內部署。隨著 Agent 能力不斷增強，Managed Agents 讓我們能安全地擴展，而不需自行建構 Agent 基礎設施。

Asana CTO Amritansh Raghav：Managed Agents 大幅加速了 Asana AI Teammates 的開發，幫助我們更快地推出進階功能，讓我們能專注於打造企業級的多人協作使用者體驗。

━━━━━━━━━━━━━━━━━━━━
▍開始使用
Managed Agents 採用消費制計費。標準的 Claude Platform token 費率適用，外加每個工作階段每小時 $0.08 的活躍運行時費用。詳細定價請參閱文件。

Managed Agents 現已在 Claude Platform 上提供。你可以閱讀文件了解更多，前往 Claude Console，或使用全新的 CLI 部署你的第一個 Agent。

開發者還可以使用最新版的 Claude Code 及其內建的 claude-api Skill 來使用 Managed Agents 進行開發。只需輸入「start onboarding for managed agents in Claude API」即可開始。

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Anthropic 推出 Claude Managed Agents——把 sandbox、auth、檢查點、scoped permissions、長時程 session、多 agent 協調、execution trace 等基礎設施全部 managed 化，讓開發者只需定義任務、工具、guardrails，從原型到生產從數月縮為數天。Notion、Rakuten、Asana、Sentry 等夥伴案例顯示部署速度提升 10x；Rakuten 一週內完成單個專業 Agent 部署。
- 作者挑戰的預設：（1）做生產級 Agent 必須先做幾個月基礎設施 → 不必，managed 已替你做了；（2）只有 RD 才能部署 Agent → 非 RD 角色（PM、銷售、設計、財務）也可部署；（3）Agent harness 與基礎設施是個別公司各自重造的 → 應該被 commodity 化。但這是平台宣傳文，論證骨架較弱。
- 個人映射：對應你的「Repo as Worker」「Agent harness 工程化」主軸；同時呼應 Rakuten 案例中「進階使用者跨越單一專業在多領域貢獻」與你關心的「分析師 / PM 可獨立部署 Agent」主題。但這篇主要是平台宣傳，需謹慎挑出真有結構性洞察的點。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent Harness 基礎設施正在被 commodity 化
- 分級：Core
- 類型：Pattern
- 核心內容：Anthropic 把 sandbox 程式執行、檢查點、憑證管理、scoped permissions、長時程 session（斷線後可恢復）、多 agent 協調、execution trace 全部 managed 化。這意味「自建 agent infra」這個過去 6-12 個月的工作，正被平台層吸收。對自建 agent stack 的小團隊而言，這是一個架構決策的轉折點。
- 保留理由：把「該不該自建 agent harness」從技術選擇升級為 build vs buy 的策略決策；對你關心的「小團隊資源約束 + 平台化能力」直接相關。
- 待補強處：什麼情況下仍應自建 harness（vendor lock-in 風險、客製需求、隱私）？managed 與 self-hosted 的真實成本對比？
- 初步知識鉤子：[[Harness Engineering]]、[[Build vs Buy]]、[[Vendor Lock-in]]、[[Repo as Worker]]

序號 2
- 候選標題：非 RD 角色（銷售、財務、PM）部署 Agent 的可行性訊號
- 分級：Support
- 類型：Pattern
- 核心內容：Rakuten 在產品、銷售、行銷、財務各部門部署企業級 Agent，整合到 Slack 和 Teams，每個專業 Agent 一週內完成部署。Notion 讓非工程師也能把工作委派給 Claude（製作網站、簡報、知識工作交付）。這是「Agent 操作門檻下降」的具體訊號，呼應 Jenny Wen 那篇的「Cowork 取代 Claude Code 在非 RD 場景」觀察。
- 保留理由：跨來源印證的趨勢觀察；對你關心的「非 RD 操作 Agent」「Solo 顧問如何替小團隊建 Agent」直接相關。
- 待補強處：「一週內部署」的實際工作分工（誰寫 prompt、誰設權限、誰測試）？非 RD 角色可獨立到什麼程度？
- 初步知識鉤子：[[非 RD 操作 Agent]]、[[Anthropic Cowork]]、[[Solo Consultant 服務包裝]]

序號 3
- 候選標題：定義「目標 + 成功標準」讓 Claude 自我評估迭代（vs 傳統 prompt-response）
- 分級：Question
- 類型：Question
- 核心內容：Managed Agents 提供的新模式——只定義 goal + success criteria，Claude 自我評估反覆迭代直到達成（目前 research preview）。這是從「prompt 對話」到「outcome-driven autonomous loop」的範式轉換。Anthropic 內部測試顯示結構化檔案生成任務成功率比標準 prompt loop 高出 10 個百分點。
- 保留理由：值得追蹤的設計範式——把 eval criteria 從 prompt 外圍移進 agent 內部循環；對你寫「Agent 工程化下一步」是重要訊號。
- 待補強處：success criteria 的設計門檻（如何寫得 Claude 能自我評估而不亂解讀）？哪些任務適用、哪些不適用？10 個百分點是哪些任務的什麼 baseline？
- 初步知識鉤子：[[Anthropic Eval]]、[[Plan-Generate-Evaluate Loop]]、[[Outcome-Driven Agent]]

## C. 建議送 refine 的項目
- 序號 1（Core）：Agent Harness 被 commodity 化
- 序號 2（Support）：非 RD 角色部署 Agent 的可行性
- 序號 3（Question）：保留作為追蹤命題（outcome-driven loop）

注：本篇大部分是平台宣傳與案例條列，無太多結構性洞察可萃取；只挑出 3 張具有跨來源 / 結構性意義的候選卡。

## D. 呼叫 refine-cards
- 上述 3 張候選卡交由 refine-cards 精煉；refine 階段需檢查序號 2 是否與 Jenny Wen 那篇的「Cowork 取代 Claude Code」合併；序號 3 是否與「Anthropic Eval」「Stripe Benchmark」串成「Eval-as-Inner-Loop」主題群。
