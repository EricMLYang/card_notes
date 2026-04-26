---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-11
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# Claude Code 實戰評價與「計畫模式」開發流程變革

> 來源：Anthropic 官方、Reddit 社群、實戰開發者評論
> 連結：https://www.anthropic.com/claude-code
> 搜集日期：2026-04-03
> 搜集原因：AI Coding 工具演進與開發流程變革

## 摘要
2026 年初，Claude Code 等 Agentic Coding 工具標誌著開發模式從「AI 輔助（補全）」轉向「AI 指揮（代理）」。核心變革在於工程師角色從「打字員」升級為「導演」。透過 `/plan` 模式進行架構先行、Git Worktrees 進行多代理並發，以及 `CLAUDE.md` 作為「AI 基因庫」，開發效率在實戰中提升了 300% 以上。

## 潛在卡片方向
- **計畫模式 (Plan-First Workflow)**：代碼撰寫前，AI 與人類必須在 `/plan` 模式下達成技術共識。
- **Harness 作為護城河**：2026 年 3 月的泄露事件顯示，Agent 的價值在於「編排與錯誤恢復邏輯」，而非單純的模型。
- **Git Worktrees 的戰略價值**：實現一個工程師同時指揮多個 AI 實例在不同分支工作。
- **與現有卡片連結**：[[20260331_這是我第二次被AI開發方式震撼到——從Claude Code到Genie Code]]、[[20260307_AI_Coding流程設計_公司導入版]]

---

## 核心內容整理

### 1. 開發流程的「三段式」變革
*   **Step 1: Plan (/plan)**：AI 讀取整個 Repo，撰寫詳細技術實作計畫。人類審核計畫中的副作用與架構取捨。
*   **Step 2: Act**：計畫確認後，AI 自主執行代碼撰寫、測試編寫、Lint 修復與環境部署。
*   **Step 3: Validate**：AI 必須運行測試並通過後才提交 PR。

### 2. CLAUDE.md：團隊的 AI 規範守門人
*   不再依賴 Wiki，而是將「專案規範、代碼風格、測試要求」寫入 `CLAUDE.md`。
*   **迭代反饋**：當 Code Review 發現 AI 犯錯時，直接修改 `CLAUDE.md`，AI 下次啟動會立即修正行為。

### 3. 高階技巧：多代理並發 (Agent Teams)
*   工程師透過 **Git Worktrees** 啟動多個 Claude 實例。
*   **角色分配**：可以讓一個 Claude 負責重構，另一個負責功能開發，第三個負責資安掃描，全部並行。

### 4. 2026 年 3 月 Claude Code 泄露事件的洞察
*   泄露的 50 萬行源碼顯示，核心競爭力不在 LLM，而是在於 **Harness (驅動框架)**。
*   **複雜性所在**：處理工具調用的超時、權限分級、複雜的 Regex 匹配、跨檔案的依賴追蹤。這證實了「垂直整合」的重要性。

### 5. 隱憂與挑戰
*   **Junior Grit 危機**：初級工程師過度依賴 AI 導致「AI Slop (代碼垃圾)」，缺乏底層架構理解能力。
*   **技術債積累**：高思考模型傾向於「過度設計」，引入不必要的複雜保護機制。

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Agentic Coding 從「補全」轉向「指揮」，工程師升級為導演。三段式流程（Plan→Act→Validate）+ CLAUDE.md 作為 AI 規範守門人 + Git Worktrees 多代理並發 = 開發效率提升 300%+。2026/3 Claude Code 泄露事件證實核心是 harness 不是 LLM。
- 作者挑戰的預設：挑戰「AI Coding 的價值在模型本身」「AI 寫 code 必降低品質」兩個慣性；用泄露源碼數據佐證 harness 才是垂直整合的護城河。
- 個人映射：把「導演 / 指揮」隱喻具體化為三段式流程；CLAUDE.md 的「迭代反饋」呼應 capture profile 的「持續迭代 harness」「人類從盯人轉向設計控制系統」。但 300% 數字無來源，需 fact-check 標記。

## B. 候選卡（Lite）

序號 1
- 候選標題：/plan 模式：架構先行的硬性流程，不只是 best practice
- 分級：Core
- 類型：Heuristic
- 核心內容：在 Claude Code 工作流中，第一步必須讓 AI 讀取整個 Repo 並產出詳細技術實作計畫，由人類審核副作用與架構取捨後才進入 Act。/plan 把「人類判斷介入點」固定在最高槓桿位置（架構決策前），而不是事後 review code。
- 保留理由：是「AI Coding 流程設計」的關鍵錨點，與 20260404（GitHub Copilot 的「先 /plan 再動手」）形成跨文佐證。
- 待補強處：缺失敗模式——當 plan 本身就錯時，後面 Act 越快錯越大。是否需要 plan 的二次評審？
- 初步知識鉤子：與 20260404 GitHub Copilot 的 plan→autopilot→agent review→人工 review 完整循環、與 20260414 Pang 的 CI 六階段對接

序號 2
- 候選標題：CLAUDE.md 是團隊 AI 規範的「迭代式守門人」
- 分級：Core
- 類型：Pattern
- 核心內容：把專案規範、code style、測試要求寫進 CLAUDE.md。當 code review 發現 AI 犯錯時，直接修 CLAUDE.md，AI 下次啟動立即修正。把「人類隱性 harness」外化成「文件可迭代規則」，避免錯誤重複發生。
- 保留理由：直接呼應 20260407 Fowler 的「human steering loop = 持續迭代 harness」與 capture profile 的「Repo-as-Worker」；可遷移到 AGENTS.md / skills / how-to 文件設計。
- 待補強處：CLAUDE.md 規模上限？太長 AI 是否會忽略？需要分層？
- 初步知識鉤子：與 20260407 feedforward controls、20260401 架構約束（規則寫在工具裡而非規範文件）形成張力——CLAUDE.md 屬於「規範文件」還是「執行工具」？

序號 3
- 候選標題：Git Worktrees + 多代理並發＝把工程師變成多代理 orchestrator
- 分級：Support
- 類型：Pattern
- 核心內容：透過 Git Worktrees 啟動多個 Claude 實例，分別負責重構 / 功能 / 資安掃描並行運作。這是「一人多代理」的具體實作機制，不只是概念。
- 保留理由：是「角色分配 + 並發」的具體架構，可遷移到自家 repo 設計。
- 待補強處：多代理間的衝突解決？merge 順序？人類能同時 review 多少並發 PR？
- 初步知識鉤子：與 20260327 Stripe Minion 並發、20260414 Pang 一天 8 次部署的並發容量

序號 4
- 候選標題：Claude Code 泄露事件揭露：核心競爭力在 Harness 不在 LLM
- 分級：Core
- 類型：Pattern
- 核心內容：2026/3 泄露的 50 萬行源碼顯示，垂直整合難度集中在工具調用超時、權限分級、複雜 Regex 匹配、跨檔案依賴追蹤等 harness 細節。這證實「模型可替換、harness 是壁壘」的策略判斷。
- 保留理由：用泄露事件作為「harness 是護城河」的硬證據，可作為策略簡報素材。
- 待補強處：50 萬行源碼的具體分布？harness 與業務邏輯的比例？需 fact-check。
- 初步知識鉤子：與 20260401 Atomic Skill、20260407 Fowler harness、20260414 Pang「Harness 是產品其他都是馬」三篇形成共識線

序號 5
- 候選標題：Junior Grit 危機 + 過度設計——AI Coding 的兩個隱性技術債
- 分級：Support
- 類型：Warning
- 核心內容：(1) 初級工程師過度依賴 AI 導致 AI Slop（代碼垃圾），缺乏底層架構理解；(2) 高思考模型傾向過度設計，引入不必要的複雜保護機制。兩者都是「看似乾淨、累積有毒」的反例。
- 保留理由：補上失敗模式視角，呼應 20260414 Pang 的「初階人才管線斷裂」與「技術債複利累積」。
- 待補強處：本文僅列名沒展開機制；過度設計的具體例子缺。
- 初步知識鉤子：與 20260414 Pang GitClear/CMU/Apiiro 三項研究、capture profile「AI Coding 風險治理」

## C. 建議送 refine 的項目
- 序號 1、2、4（Core，皆可獨立成卡）
- 序號 3、5 為 Support，可與 20260327、20260414 合併

## D. 呼叫 refine-cards
- 將 5 張候選卡交由 refine-cards 精煉；特別注意「300% 效率提升」「50 萬行源碼」等數字需 fact-check 標記；CLAUDE.md vs 20260401「規則寫在工具裡」的張力值得在 refine 階段保留為對話卡。

