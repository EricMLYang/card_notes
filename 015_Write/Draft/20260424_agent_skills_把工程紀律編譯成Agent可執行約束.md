---
pipeline_stage: "DONE"
topic: "agent-skills 如何把人類工程紀律編譯成 Agent 可執行約束"
target_reader: "A｜寫 Code 也兼做 PM 的中階軟體工程師"
scenario: "insight"
personal_angle: "針對 Vibe coding 看了很多流程資訊，沒想到 agent-skills 一組包含完整開發週期。以一個讀這份 skills 來更理解軟體開發週期的人，分享自己的理解；謙虛、自問自答、不說教、沒有要互動"
selected_cards:
  - "Skill是可編碼的判斷力_從Prompt到Skill的典範轉移"
  - "Agent 開發的典範轉移：80% 時間從工程問題搬到領域問題"
  - "TDD 在 AI 時代的角色轉變：從開發者自律工具到 Agent 的控制介面"
  - "測試套件是 Agentic Engineering 的核心槓桿點"
  - "AI Coding 的骨架策略：用 Interface + Test 鎖住頭尾，中間放給 Agent 跑"
  - "軟體開發價值遷移：從生成程式碼到定義驗收條件，人才市場面臨結構性錯配"
  - "Vibe Coding：80% 規劃 20% 執行的工作流"
  - "AI Coding 的控制能力差距：新手 5x vs 有經驗者 20x，差別在骨架品質"
  - "AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性"
  - "Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單"
  - "當工具夠強，你需要更少的流程：Codex 團隊 40 人 1 PM 的運作模式"
  - "Agent組織化原則——專門context處理專門事情"
  - "組織設計是context管理——人類集中昂貴Agent輕量可分切"
  - "Jevons悖論在AI時代_效率提升擴大總需求"
  - "Prototype as Spec：架構師用原型代替規格文件的新工作模式"
chosen_title: "讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄"
chosen_hook: "H4 — Rationalizations 是資深工程師對自己偷懶的內心獨白"
chosen_framework: "universal_writing"
created: 2026-04-24
last_updated: 2026-04-24
published_to: "015_Write/Publish/20260424_【讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄】.md"
status: "published"
---

# agent-skills：把工程紀律編譯成 Agent 可執行約束（暫訂）

## 原始素材

### 來源
- Capture：`003_Capture/20260424_google_agent_skills_fro_coding.md`
- 外部專案：`addyosmani/agent-skills`（20 skills + 3 personas + 7 slash commands + hooks，非 Google 官方，但由 Google Cloud AI Director Addy Osmani 開源，受 Google SWE 實務啟發）

### 素材重點摘要

1. **本質判斷**：這不是 prompt pack，是 **workflow-as-code** 框架——把人類工程紀律包成 agent 可讀的「有限狀態機 + 驗收證據 + 反理性化抗辯」。
2. **三層正交抽象**：
   - **Skills**（*how*）：流程 + 退場條件
   - **Personas**（*who*）：角色視角 + 輸出格式
   - **Slash Commands**（*when*）：orchestrator 入口
3. **核心轉化手法（值得偷學）**：
   - 「先寫 spec」→ Frontmatter intent 觸發 + gated workflow
   - 「先寫失敗測試」→ 明文 `A test that passes immediately proves nothing.`
   - 「每 PR ~100 行」→ 100 行寫進 Process 步驟主動觸發 split
   - 「不要事後合理化」→ 每個 skill 有 **Rationalizations 反駁表**
   - 「看到異常先停下來」→ Stop-the-Line Rule
   - 「證據本位決定 done」→ 每個 skill 末節強制 Verification（tests passing、build output、runtime data）
   - 「資深工程師 review」→ 3 personas parallel fan-out（code-reviewer / security-auditor / test-engineer）
4. **覆蓋完整 SDLC**：DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP，20 個 skills 對應六階段 + 一個 META 層。
5. **適用邊界**：綠地/棕地、L0/L1/L2 風險分層；Hackathon 和 Legacy 無測試 codebase 不適用。
6. **反例警示**：Reddit 有使用者認為自己本來就會給 agent 長 spec，skill tree 價值取決於工作流成熟度；issue 區有 skill 路由、`/review` 命令衝突等問題。

---

## 核心卡片（直接相關）

| 卡片 | 角色 | 關鍵摘錄 |
|---|---|---|
| [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]] | 框架 | Skill 與 prompt 的關鍵差異在於**可系統化迭代、可轉移、可交易**。它是把隱性知識變成可複利資產的核心機制。 |
| [[Agent 開發的典範轉移：80% 時間從工程問題搬到領域問題]] | 論據 | 用 Coding Agent + SKILLs + MCP 後，80% 時間花在評估「該準備什麼 SKILL」「該配什麼 Tools/MCP」——工程問題轉領域問題。 |
| [[TDD 在 AI 時代的角色轉變：從開發者自律工具到 Agent 的控制介面]] | 框架 | 傳統 TDD 是開發者自律工具；Agent 執行實作時，TDD 變成「控制介面」——測試是你跟 AI 溝通「我到底要什麼」的唯一精確語言。 |
| [[測試套件是 Agentic Engineering 的核心槓桿點]] | 論據 | The single biggest differentiator between agentic engineering and vibe coding is testing. |
| [[AI Coding 的骨架策略：用 Interface + Test 鎖住頭尾，中間放給 Agent 跑]] | 框架 | 用 code 定義規格（Interface）+ 用 code 定義驗收（Test），這兩層親自 review；中間實作交給 Agent 跑到通過為止。 |
| [[軟體開發價值遷移：從生成程式碼到定義驗收條件，人才市場面臨結構性錯配]] | 論據 | 價值鏈從「寫程式」遷到「寫規格」；稀缺人才是能把「老闆模糊的話」翻譯成精確、完備、邊界條件清晰的測試案例的人。 |
| [[Vibe Coding：80% 規劃 20% 執行的工作流]] | 對照 | Lovable 的 Vibe Coding 正確工作流：80% 規劃、20% 執行——概念上與 agent-skills 同方向，但 agent-skills 把「規劃」編碼成可審計流程。 |
| [[AI Coding 的控制能力差距：新手 5x vs 有經驗者 20x，差別在骨架品質]] | 論據 | AI 可 100x 開發，但控制能力有限；新手加速到 5x 就失控，有經驗者到 20x，差別在骨架品質。 |
| [[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]] | 反面/前提 | 沒有完整測試、沒有可複製環境，Agent 自主工作就會幻覺型產出——正好解釋 agent-skills 為何在 Legacy 無測試 codebase 失效。 |

## 跨域卡片（意外連結）

| 卡片 | 連結理由 | 關鍵摘錄 |
|---|---|---|
| [[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]] | 反面警示 | 精心設計 workflow = 做空模型進步的單子——模型跳升時固化架構會成技術負債；agent-skills 作為 workflow-as-code 同樣面臨這個風險。 |
| [[當工具夠強，你需要更少的流程：Codex 團隊 40 人 1 PM 的運作模式]] | 對照張力 | OpenAI Codex 團隊：更強工具不是加流程而是減流程。與 agent-skills「加紀律」方向相反——但兩者其實互補：skills 是紀律的載體，而不是紀律本身。 |
| [[Agent組織化原則——專門context處理專門事情]] | 前提 | agent-skills 的三層抽象（Skill × Persona × Command）正是「專門 context 處理專門事情」的實作。 |
| [[組織設計是context管理——人類集中昂貴Agent輕量可分切]] | 類比 | 人類組織貴在 context 集中；Agent 則要輕量可切。Skills 作為可切片的 context 載體，正好順應 agent 的成本結構。 |
| [[Jevons悖論在AI時代_效率提升擴大總需求]] | 類比 | AI 降成本 → 工作內容從「執行」轉向「判斷與指揮」——agent-skills 的價值不在寫更快，而在讓判斷可編碼、可審計。 |
| [[Prototype as Spec：架構師用原型代替規格文件的新工作模式]] | 對照 | 一派用 Prototype 當 Spec；agent-skills 則把 Spec 本身編碼成 gated workflow。兩種路徑、同一個目的：讓規格變成可執行契約。 |

## 素材缺口

- ❌ **個人第一手使用經驗**：目前只讀過 skills 的說明文字，未實際整套跑過，文章需如實標示這點（剛好符合寫作人設：謙虛的學習者）。
- ❌ **實際團隊 rollout 數據**：缺少第三方團隊導入 agent-skills 後的量化成效（DORA、缺陷率）。
- ❌ **跨 agent 相容性實測**：Claude Code / Cursor / Copilot 實際觸發率差異，只有零散 issue 回報。

## 搜尋摘要

- 掃描索引：3/15 個主分類（04 AI Coding / 03 AI Applications / 01 Mental Models）+ 旁支
- 候選卡片：30+ 張
- 精選輸出：15 張（核心 9 + 跨域 6）

---

## 素材地圖（W2_01 CardWeaver 角色化整理）

> 文章軸：**人類工程紀律如何編譯成 Agent 可執行約束**；假想讀者：寫 Code 兼做 PM 的中階軟工；人設：謙虛的學習者，自問自答、不說教。

### (a) 開場鉤子素材（為什麼值得看？）
- **Vibe Coding 的「80/20 規劃」已是共識**（[[Vibe Coding：80% 規劃 20% 執行的工作流]]）——但「規劃」這件事本身仍是口頭藝術。agent-skills 把它變成**可以被 agent 讀、被 CI 檢查、被 audit 的狀態機**。
- 個人觸發點：「針對 Vibe coding 看了很多流程資訊，沒想到這個 agent-skills 一組包含完整開發週期」。

### (b) 核心主張素材（文章要論證什麼？）
**主張**：agent-skills 的真正突破不是「教 agent 寫 code」，而是**把隱性工程紀律編譯成 agent 可執行的顯性約束**——讓資深工程師的判斷從「口頭傳承」變成「可版本控制的制度」。

論據卡：
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]——Skill 的本質是**可系統化迭代 / 可轉移 / 可交易**。
- [[軟體開發價值遷移：從生成程式碼到定義驗收條件，人才市場面臨結構性錯配]]——價值遷移到「定義驗收」。
- [[Agent 開發的典範轉移：80% 時間從工程問題搬到領域問題]]——80% 時間搬到 SKILL / MCP 準備。

### (c) 骨架素材（文章結構用什麼？）
以軟體開發週期（SDLC）六階段為骨架，把 agent-skills 做的事對照到傳統工程紀律的「口頭版 vs 編碼版」：

| SDLC 階段 | 傳統口頭紀律 | agent-skills 的編碼手法 | 我的理解卡片 |
|---|---|---|---|
| DEFINE | 「先 spec 後 code」 | Frontmatter intent + gated workflow，未完成 Specify 不得進 Plan | [[Prototype as Spec]] 的對照 |
| PLAN | 「拆小任務」 | Plan Mode 禁寫 code；Vertical / Risk-First Slicing | [[AI Coding 的骨架策略]] |
| BUILD | 「先寫失敗測試」 | `A test that passes immediately proves nothing` + Prove-It Pattern | [[TDD 在 AI 時代的角色轉變]]、[[測試套件是 Agentic Engineering 的核心槓桿點]] |
| VERIFY | 「看到異常先停下來」 | Stop-the-Line Rule 寫進 debugging skill 第一步 | [[AI Coding Agent 自主工作的兩個硬前提]] |
| REVIEW | 「每 PR ~100 行」「Nit/Optional/FYI」 | 100 行寫進 Process；嚴重度三級標籤 | [[AI Coding 的控制能力差距]] |
| SHIP | 「灰度發布」「feature flag 有期限」 | Staged Rollout 5→25→50→100 + 每 flag 有 owner 與到期日 | — |

### (d) 類比與跨域素材
- **類比 1：workflow-as-code ↔ infrastructure-as-code**——從 Terraform 的角度看，agent-skills 是把「工程流程」當成 Terraform 要管的資源。
- **類比 2：三層抽象 ↔ 菜單結構**——Slash Command（顧客下單「我要吃什麼」）× Persona（廚師「誰來做」）× Skill（食譜「怎麼做」）。
- **反面張力**：[[當工具夠強，你需要更少的流程]] vs agent-skills「加流程」。答案可能是——**流程不是越多越好，但「可視」比「口頭」好**；agent-skills 真正在做的是把流程從「無形」變「有形」，至於要不要用那麼多，交給 L0/L1/L2 分層決定。
- **做空檢驗**（[[Agent 架構的做空檢驗]]）：模型進步時 agent-skills 會不會自動變簡單？答：**如果 skills 只是「描述期望行為」應該會自動變好；但如果把過多業務邏輯固化到 skill 內，就會變技術負債。**

### (e) 收尾素材
- [[Jevons悖論在AI時代_效率提升擴大總需求]]——AI 降成本 → 需求爆炸 → 人類的工作從「執行」搬到「判斷與指揮」。
- [[組織設計是context管理]]——真正的組織設計瓶頸是 context 管理；agent-skills 正是在做「可共享的 context 模組化」。
- 個人反思：身為讀者，我學到的不是「快點安裝這包 skill」，而是**「資深工程師的紀律本來就可以被寫下來；過去只是沒人肯花時間」**。

---

## 發想筆記（W2_04 價值 × 乾貨）

### 外部價值定位
| 維度 | 對假想讀者（寫 Code 兼 PM 中階軟工）的價值 |
|---|---|
| **教育** | 🟢 高：用 SDLC 六階段當骨架，把 agent-skills 的結構講清楚 |
| **啟發** | 🟢 高：「workflow-as-code」這個視角重構了對 AI 工具的想像——不是用更好的 prompt，而是用更好的**流程基礎設施** |
| **共感** | 🟡 中：讀者會認同「vibe coding 很潮但品質不穩」的痛點 |
| **娛樂** | 🟡 低：偏硬核知識分享 |

→ **主打**：啟發 + 教育；用「我剛讀完它的感想」切入，避免說教感。

### 內部乾貨盤點
- ✅ **知識**：對 agent-skills 20 skills 的結構性理解（來自原始 capture）
- ✅ **框架**：SDLC 對照表 + Skill × Persona × Command 三層抽象
- ✅ **類比**：workflow-as-code、菜單結構、做空檢驗
- ⚠️ **經驗缺口**：我本人還沒跑完一整套 skills，只能誠實說「讀完後的理解」而非「實戰後的心得」
- ⚠️ **案例缺口**：沒有具體團隊 rollout 的親身案例可引

→ **對應寫作人設**：剛好符合「謙虛學習者」的定位；**把知識差當作敘事優勢**，用「我讀完後發現...」作為開場口吻。

### 觀點深化（W2_09 五種視角重新發想）

我要避免的寫法：「agent-skills 有 20 個 skills，讓我介紹給你」——這會變工具推薦文。

五種視角換位思考：

1. **歷史視角**：prompt → system prompt → rules file → skill，這是「把工程師隱性知識逐步顯性化」的連續過程，agent-skills 是這條線的最新一站。
2. **經濟視角**：agent-skills 的核心是**把 review 的成本前置**——與其在 PR 階段被資深 engineer 擋下，不如在 agent 執行時就被流程擋下。
3. **PM 視角**（貼合讀者）：agent-skills 提供的最稀有東西是**「Acceptance Criteria 可執行」**——把 PM 最痛的「模糊需求」變成 agent 看得懂的契約。
4. **學徒視角**：讀這份 skills 像在讀一本**資深工程師的備忘錄**——每條「Rationalizations 反駁表」都是「我跟自己過去的偷懶對話」。
5. **做空視角**：如果模型在半年後大跳級，agent-skills 這包會怎麼樣？答：**結構無恙，細節會鬆**（例如 100 行上限會被放寬）；但三層抽象（Skill × Persona × Command）會留下。

→ **主文章要用的視角**：**學徒視角 + PM 視角**，符合讀者角色（寫 Code 兼做 PM）。

### 非顯然的判斷（這是洞察文的關鍵）

列出 3 個**讀者不會馬上想到的**判斷：

1. **「流程多寡」不是重點，「流程可視」才是**——`當工具夠強你需要更少的流程` vs `agent-skills 加紀律` 看似矛盾，其實互補：skills 不是叫你加流程，而是把本來就有的隱性流程寫下來變成可審計物件。
2. **agent-skills 最大的價值不在 agent 變強，而在「資深工程師的判斷可被版本控制」**——這是第一次，一個人可以把自己對「好 code 長什麼樣」的品味，放進 git、diff、PR。
3. **這包 skills 在 legacy 無測試 codebase 會反向產生危害**——它預設「有測試基礎建設」，沒有時會產出幻覺型測試，這是工具/紀律的**前置依賴條件**，不是工具本身的鍋。

---

## 標題鉤子選項

> 8 種策略產出標題（W3_01），每個標題配一個鉤子（W4_01）。依切入角度分類。

### 🏷️ 標題候選（推薦 5 個）

#### T1｜具體化 + 反差
**看了一整年 Vibe Coding，我才發現這包 agent-skills 做的是完全不同的事**

- **鉤子 H1**：
> 以為 Vibe Coding 的極致就是「花 80% 時間規劃、20% 時間執行」。
> 直到讀完 addyosmani/agent-skills 的 20 個 skills，我才意識到：
> 那個 80% 的「規劃」，過去始終是口頭藝術，從來沒人把它變成 agent 看得懂的東西。
> 這包 skills 不是把 agent 教得更聰明，它是把資深工程師的紀律，**編譯成可被 agent 執行、被 CI 檢查、被 diff 出來的約束**。

---

#### T2｜核心洞察直球
**把工程紀律編譯成 Agent 的狀態機：我從 agent-skills 學到的一件事**

- **鉤子 H2**：
> 軟體開發的紀律我一直以為只能靠文化、師徒、code review 傳下去。
> 但讀完這 20 個 skills 後，一個之前沒有認真想過的問題浮上來：
> 「資深工程師的判斷力，有沒有可能被寫成一份可執行的契約？」
> 看來是可以的——而且已經有人把整套 SDLC 都編完了。

---

#### T3｜SDLC 對照法
**從 DEFINE 到 SHIP，agent-skills 幫我補完了 Vibe Coding 少掉的那一半**

- **鉤子 H3**：
> 過去我理解的 AI Coding 工作流大概就是：先對話規劃、丟給 agent 跑、跑完自己 review。
> 聽起來沒毛病，但卡住的永遠是同一件事——**「什麼叫做完」？**
> 這 20 個 skills 用 SDLC 六階段（Define → Plan → Build → Verify → Review → Ship）把整條路補起來，
> 每一階都告訴你：觸發條件是什麼、什麼時候才算 done、agent 偷懶時的藉口怎麼反駁。

---

#### T4｜學徒視角
**讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄**

- **鉤子 H4**：
> 每個 skill 的最後一節叫做 Rationalizations（合理化辯詞）。
> 裡面列的不是 agent 的話，是**資深工程師過去對自己偷懶時的內心獨白**：
> 「之後再補測試啦」「這太小不值得開 skill」「先做完這個 sprint 再說」。
> 讀這份備忘錄的體感，就像在看一個資深 engineer 把自己跟過去自己對話的紀錄全部公開出來，讓 agent 拿去用。

---

#### T5｜反直覺判斷
**Agent 不會自動變資深——得有人把資深的判斷寫成 code**

- **鉤子 H5**：
> 一直以為等模型再強一點，agent 就會自動寫出資深工程師水準的 code。
> 看完 agent-skills 才發現：**模型再強也不會突然懂「為什麼一個 PR 不該超過 100 行」**，
> 因為這不是知識問題，是紀律問題。
> 紀律沒被寫下來之前，agent 只會無視；寫下來之後，它就變成了一條可被觸發、被驗證、被違反時反駁的規則。

---

### 鉤子風格差異摘要

| 鉤子 | 開場策略 | 情緒 | 與主題連結方式 |
|------|----------|------|----------------|
| H1 | 自我顛覆（「以為 A，其實 B」） | 反差 | 用 Vibe Coding 當對照 |
| H2 | 拋問題 + 自答 | 思辨 | 從「紀律能否被編譯」切入 |
| H3 | 場景痛點（「什麼叫做完」） | 共感 | 用 SDLC 補完口頭流程 |
| H4 | 畫面感（偷看備忘錄） | 畫面 | 用 Rationalizations 當鉤子 |
| H5 | 反直覺命題 | 認知衝擊 | 把「模型強 vs 紀律」對立起來 |

---

### 文章角度摘要（待 CP1 確認）

- **主軸**：agent-skills 的真正價值不是讓 agent 寫得更快，而是**把人類工程紀律編譯成 agent 可執行的顯性約束**。
- **骨架**：SDLC 六階段對照表 + 「口頭紀律 → 編碼紀律」的轉化手法。
- **非顯然判斷三條**：(1) 流程可視比流程多寡重要；(2) 資深工程師判斷首次可被版控；(3) legacy 無測試時反而有害。
- **人設**：謙虛的學習者，自問自答，不說教，不要求互動。
- **避雷**：不要寫成「工具推薦文」或「20 skills 介紹」。

---

## Draft v1

### 選定
- **標題**：讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄
- **鉤子**：H4（畫面感 — Rationalizations 當切入點）
- **框架**：萬能寫作法（W5_03 Universal Writing）——*鉤子 → 我的困惑 → 一個意外發現 → 展開理解 → 非顯然判斷 × 3 → 收在自己身上*

---

# 讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄

每個 skill 的最後一節叫做 Rationalizations（合理化辯詞）。

裡面列的不是 agent 的話，是**資深工程師過去對自己偷懶時的內心獨白**：「之後再補測試啦」「這太小不值得開 skill」「先做完這個 sprint 再說」。

讀這份備忘錄的體感，就像看一個資深 engineer 把自己跟過去自己對話的紀錄全部公開出來，讓 agent 拿去用。

---

## 我先說一下我是怎麼遇到它的

這一整年我花了很多時間在看各種 Vibe Coding 的流程資訊。

Lovable 的 Lazar 說要「80% 規劃、20% 執行」；Kent Beck 和幾位架構師說要「Prototype as Spec」；Karpathy 說 Claude Code 才是正確的 Agent 典範；Anthropic 團隊示範了截圖除錯、非技術人員操作數據的協作模式。

這些東西我都讀得很開心，因為它們回答了「AI Coding 時代到底要怎麼工作」這個我一直放在心上的問題。

但有一個地方始終沒被填滿——**那個被強調到爛的「80% 規劃」，到底長什麼樣？**

這件事沒人真正寫清楚過。大家講的規劃都是口頭的、文化的、靠感覺的。你看了十篇文章，得到的是「規劃很重要」這個結論，但如果要你明天早上就把規劃寫下來給 agent 看，你還是不知道要寫什麼。

直到我讀到 `addyosmani/agent-skills`（Addy Osmani 是 Google Cloud AI Director，這是他的個人開源專案，受 Google 工程實務啟發，但不是 Google 官方產品）。

一打開 repo，我愣了一下：

**它沒有在教 agent 怎麼寫 code，它在教 agent 怎麼走完一整輪軟體開發週期。**

從 DEFINE（定義要做什麼）、PLAN（拆任務）、BUILD（動手寫）、VERIFY（驗證能動）、REVIEW（合併前把關）、到 SHIP（安全出貨），每一階段都有對應的 skill，每個 skill 都寫著觸發條件、步驟、常見偷懶藉口、red flags、驗收證據。

那一刻我意識到：我一年來在看的那些 Vibe Coding 流程資訊，只是拼圖的一小塊，而這包 skills 把整張拼圖攤在桌上。

---

## 我原本對它有的偏見

坦白說，我第一眼看到「20 個 skills、3 個 personas、7 個 slash commands」這種數字，會下意識覺得這又是一個 prompt pack——把一堆 prompt 打包起來賣 hype，跟我之前看過的很多 AI Coding 模板沒兩樣。

但往下讀的時候，有幾個細節讓我停下來想了很久。

**第一個**，每個 skill 的格式不是「你要這樣做」，而是「何時觸發 → 步驟 → Red Flags → Verification」。它寫的不是給人看的建議，是給 agent 走的流程圖。

**第二個**，每個 skill 最後都有一節 Rationalizations，列出 agent 很可能會用的藉口，然後逐條配好反駁話術。第一次看到的時候我真的笑出來——這根本是資深工程師在跟自己內心那個「懶惰版的自己」對話啊。

**第三個**，它用 Skill × Persona × Slash Command 這三層抽象把「怎麼做」「誰來做」「什麼時候做」拆開，三件事可以獨立演進、獨立審計、獨立替換。

看到這裡我慢慢收回偏見，開始覺得：這不是 prompt pack，是把資深工程師的紀律**編譯成 agent 看得懂的狀態機**。

它解決的不是「agent 懂不懂怎麼寫程式」（知識層），而是「agent 肯不肯照流程走」（流程層）——這兩個層次，過去從來沒有被這樣清楚地分開處理過。

---

## 然後我想通了幾件事

### 一、那個被講了很多年的「80% 規劃」，第一次有了可寫下來的形狀

以前讀「先 spec 後 code」，我知道它是對的，但我始終不知道「把 spec 寫到什麼程度才算完」。

agent-skills 的 `spec-driven-development` 把 spec 拆成六大面向：Objective、Commands、Structure、Code Style、Testing、Boundaries。而且規定一件很硬的事——**未完成 Specify 階段，不得進入 Plan 階段**。人類必須審核才能推進。

這叫 gated workflow。聽起來很像以前那種繁瑣流程，但差別在於：過去的流程是寫在 Wiki 上沒人讀，現在這個流程被 agent 自己持續讀、持續驗收、持續反問你有沒有跳步。

[[AI Coding 的骨架策略：用 Interface + Test 鎖住頭尾，中間放給 Agent 跑]]這張卡說的是同一件事——用 code 定義規格、用 code 定義驗收，中間放給 agent 跑。差別只在：agent-skills 把「用 code 定義規格」這件事本身，也變成了可以被 agent 遵守的流程。

我原本以為這會疊床架屋，但靜下來想，這其實是**把隱性的工程師直覺顯性化**。直覺寫不下來，agent 就看不到；agent 看不到，你就永遠只能靠 review 事後擋——而 review 是最貴的人力。

### 二、Rationalizations 這東西，是第一次有人把「工程師的良心」寫進規格裡

TDD 的 skill 裡有一句話我看完印象很深：

> A test that passes immediately proves nothing.

意思是，如果你寫了一個測試，它第一次跑就直接 pass，那它根本沒證明任何東西——因為你不知道它是在驗證邏輯，還是在驗證空白。

TDD 的 Red-Green-Refactor 裡，RED 那一步要求測試必須先失敗。這件事每個資深工程師都知道，但你會看到很多 agent 寫完 code 就配一個空測試交差。

agent-skills 是怎麼處理的？它直接把這句話寫進 skill，並且列出 agent 可能會說的所有藉口：「我等下再補測試」「這個 edge case 不太可能發生」「現在時間不夠」。每條藉口後面配好反駁話術。

這段東西我讀了三遍，因為我一直在想：**資深工程師心裡本來就有這些對話，只是從來沒人把它寫下來。**

過去這些內心對話只能靠 code review 一次一次地傳給新人：你這個 PR 沒測試，我要擋；你這個測試沒失敗過，我要擋；你這邊偷偷 catch 例外，我要擋。

agent-skills 做的事是——把這些 review 當下才會出現的話，搬到 agent 執行當下就出現。

這不是 review 消失，是 review 被提前了。用另一張卡的說法：[[軟體開發價值遷移：從生成程式碼到定義驗收條件]]——當 review 成本從「PR 當下」前移到「工具內建」，工程師的稀缺價值就從寫 code 轉到「寫驗收標準」了。

### 三、三層抽象比 20 個 skills 本身更重要

如果有一天我要把這包 skills 介紹給同事，我不會從 skills 清單講起，我會從**三層抽象**講起：

| 層次 | 回答的問題 | 例子 |
|---|---|---|
| **Slash Commands** | 什麼時候做？（when） | `/spec`、`/plan`、`/build`、`/review`、`/ship` |
| **Personas** | 誰來做？（who） | code-reviewer、security-auditor、test-engineer |
| **Skills** | 怎麼做？（how） | spec-driven-development、TDD、code-review-and-quality |

這三層可以獨立演進。Persona 的角色可以加可以換、skill 的步驟可以改版、slash command 的觸發時機可以調整，彼此不強耦合。

為什麼這件事重要？因為過去所有「AI Coding 最佳實踐」的建議都是一坨——一坨 system prompt、一坨 rules file、一坨 CLAUDE.md。當你想改其中一條，你就要重讀整份、重新思考，很容易改出意料外的副作用。

三層拆開之後，**行為治理從藝術變成工程**。你可以 diff 一個 skill 的改動、可以 A/B 測試兩個 persona 的 review 風格、可以觀察某個 slash command 的觸發率是不是掉了。

這件事呼應了 [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]] 這張卡的核心主張——Skill 和 prompt 的本質差異在於**可系統化迭代、可轉移、可交易**。三層抽象讓 iterate、transfer、trade 這三件事第一次真的能做。

---

## 但我還是有三個沒想通的地方

寫到這裡我應該要給結論了，但誠實一點講，我對這包 skills 還有三個疑惑。如果看到這篇的人剛好有答案，歡迎告訴我。

### 疑惑一：流程多 vs 流程少，到底哪個對？

我有另一張卡[[當工具夠強，你需要更少的流程：Codex 團隊 40 人 1 PM 的運作模式]]，講 OpenAI Codex 團隊 40 人只配 1 個 PM，靠工具夠強所以流程可以砍。

但 agent-skills 做的看起來剛好相反——它是在加流程。

我目前給自己的和解方案是：**流程多寡其實不是重點，「流程可視」才是重點**。agent-skills 不是叫你加新流程，是把本來就有（但寫在資深工程師腦子裡）的流程搬出來變成可審計物件。至於每個情境要用多少，它自己也說了——Hackathon / typo / 一行改動不該觸發 `/spec`。

但這個和解方案對不對，我還不確定。

### 疑惑二：模型大跳級以後，這包 skills 會變成技術負債嗎？

[[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]] 這張卡讓我很警覺——精心設計的 workflow 本質上是「做空模型進步」的單子。模型跳級時，你之前固化的流程就會變技術負債。

agent-skills 會嗎？我目前的猜測是：**三層抽象應該能活下來；細節規則會鬆**。例如「每 PR 不超過 100 行」這條未來可能會放寬，但「PR 要有大小限制」這件事不會消失。「寫失敗測試」的硬性 RED 步驟可能會被簡化，但「先定義驗收條件」不會。

不過這只是猜測。要真的驗證，只能等半年後回來看。

### 疑惑三：它在我手上的 codebase 會不會反而有害？

這是我最後一個、也最大的一個擔憂。

[[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]] 說得很清楚——沒完善測試的 codebase，agent 自主工作會幻覺型產出。

agent-skills 的 TDD / code-review 等 skill 預設「測試基礎建設存在」。如果你拿這包去一個 legacy 沒測試、沒 CI 的 codebase 跑，agent 不會變資深，反而會產出一堆你以為在驗證什麼、實際根本跑不起來的假測試。

這是工具/紀律的**前置依賴條件**問題。不是 agent-skills 的鍋，但如果我沒注意到，就會是我的鍋。

---

## 所以我打算怎麼用它

寫了這麼多，我其實還沒真的在自己的案子上跑過整套 skills。這篇不是實戰心得，是讀完之後的理解整理。

但我對自己下一步想嘗試的事情已經有個清單：

1. **先在個人小案子上試 5 個 skills**：`spec-driven-development`、`planning-and-task-breakdown`、`incremental-implementation`、`test-driven-development`、`code-review-and-quality`——先不引入 Persona fan-out，只跑 happy path。
2. **觀察 Rationalizations 在哪些時刻被觸發**：我自己的心裡也會冒出那些藉口——「之後再補測試」「這太小不值得開 spec」——看看當 agent 照著反駁話術回我時，我是會照做、還是會找新藉口。
3. **判斷它適不適合帶到團隊**：如果在個人案子上都覺得「開銷 > 收益」，那拿到團隊也救不了。這件事我想先自己走過再說。

---

## 最後

讀完這包 skills，我的想法很簡單：

**資深工程師的紀律，過去只能靠師徒制傳。現在第一次，這些紀律可以被寫下來、可以放進 git、可以讓 agent 照著走。**

它不會讓 agent 自動變資深。但它讓資深工程師的判斷，第一次有了可分享、可複製、可累積的形狀。

我會先挑 5 個 skills 在自己的案子上試看看——spec、plan、incremental、TDD、code-review。跑完之後再決定要不要帶到團隊。

如果我自己都做不到這些紀律，我也不會期待 agent 做到。

---

## Draft v2（POLISH 後）

> Polish 處理：W7_05 平實直述 → W7_01 Humanizer（經驗感/判斷感）→ W7_02 NotButReducer（去辯證句）→ W7_formatting（標題與段落）。
> 主要調整：（1）降低「不是 A 而是 B」這類辯證句密度；（2）把幾處太工整的總結句改得更口語；（3）尾段保留你指定的直白版本。

---

# 讀完這份 Skills，我像是偷到了一本資深工程師的備忘錄

每個 skill 的最後一節叫做 Rationalizations（合理化辯詞）。

這段裡面列的不是 agent 的話，是**資深工程師過去對自己偷懶時的內心獨白**：「之後再補測試啦」「這太小不值得開 skill」「先做完這個 sprint 再說」。

讀這份備忘錄的體感，像看一個資深 engineer 把自己跟過去自己對話的紀錄全部公開出來，讓 agent 拿去用。

---

## 我先說一下是怎麼遇到它的

這一整年我花了不少時間看各種 Vibe Coding 的流程資訊。

Lovable 的 Lazar 說要「80% 規劃、20% 執行」；Kent Beck 和幾位架構師主張「Prototype as Spec」；Karpathy 說 Claude Code 才是正確的 Agent 典範；Anthropic 團隊示範了截圖除錯、非技術人員操作數據的協作模式。

這些我讀得很開心，因為它們回答了「AI Coding 時代到底要怎麼工作」這個問題——我心裡一直放著這個問題。

但有一個地方始終沒被填滿。那個被強調到爛的「80% 規劃」，到底長什麼樣？

我看了十篇文章，得到的結論都是「規劃很重要」。但如果你要我明天早上就把規劃寫下來給 agent 看，我其實還是不知道要寫什麼。

直到我讀到 `addyosmani/agent-skills`。順帶說明——Addy Osmani 是 Google Cloud AI Director，這是他的個人開源專案，受 Google 工程實務啟發，但不是 Google 官方產品。

一打開 repo 我愣了一下。它沒有在教 agent 怎麼寫 code，它在教 agent 怎麼走完一整輪軟體開發週期。

從 DEFINE（定義要做什麼）、PLAN（拆任務）、BUILD（動手寫）、VERIFY（驗證能動）、REVIEW（合併前把關）、到 SHIP（安全出貨），每一階段都有對應的 skill，每個 skill 都寫著觸發條件、步驟、常見偷懶藉口、red flags、驗收證據。

那一刻我意識到：我一年來在看的那些 Vibe Coding 流程資訊，只是拼圖的一小塊。這包 skills 把整張拼圖攤在桌上。

---

## 我原本對它有的偏見

坦白說，第一眼看到「20 個 skills、3 個 personas、7 個 slash commands」這種數字，我下意識覺得——這又是一個 prompt pack。打包一堆 prompt 賣 hype，跟之前看過的很多 AI Coding 模板沒兩樣。

但往下讀的時候，有幾個細節讓我停下來想了很久。

**第一個**，每個 skill 的格式是「何時觸發 → 步驟 → Red Flags → Verification」。它寫的是給 agent 走的流程圖，不是給人看的建議條列。

**第二個**，每個 skill 最後都有一節 Rationalizations，列出 agent 很可能會用的藉口，然後逐條配好反駁話術。第一次看到的時候我真的笑出來——這就是資深工程師在跟自己內心那個「懶惰版的自己」對話。

**第三個**，它用 Skill × Persona × Slash Command 這三層抽象把「怎麼做」「誰來做」「什麼時候做」拆開。三件事可以獨立演進、獨立審計、獨立替換。

看到這裡我慢慢收回偏見。它解決的是 agent 的流程層問題——agent 肯不肯照流程走，不是 agent 懂不懂怎麼寫程式。這兩個層次過去從來沒有被這樣清楚地分開處理過。

---

## 我想通的三件事

### 一、「80% 規劃」這次終於有了可以寫下來的形狀

以前讀「先 spec 後 code」，我知道它是對的，但我始終不知道 spec 要寫到什麼程度才算完。

agent-skills 的 `spec-driven-development` 把 spec 拆成六大面向：Objective、Commands、Structure、Code Style、Testing、Boundaries。而且規定一件很硬的事——未完成 Specify 階段，不得進入 Plan 階段。人類必須審核才能推進。

這叫 gated workflow。聽起來很像以前那種繁瑣的流程文件，但差別很明顯：過去的流程寫在 Wiki 上沒人讀，現在的流程被 agent 持續讀、持續驗收、持續反問你有沒有跳步。

[[AI Coding 的骨架策略：用 Interface + Test 鎖住頭尾，中間放給 Agent 跑]]這張卡講的是同一件事——用 code 定義規格、用 code 定義驗收，中間放給 agent 跑。差別只在：agent-skills 把「用 code 定義規格」這件事本身，也變成了可以被 agent 遵守的流程。

我原本以為這會疊床架屋，靜下來想才發現它在做的是把隱性的工程師直覺顯性化。直覺寫不下來，agent 就看不到；agent 看不到，你就只能靠 review 事後擋——review 是最貴的人力。

### 二、Rationalizations 這東西，第一次把「工程師的良心」寫進規格

TDD 的 skill 裡有一句話我看完印象很深：

> A test that passes immediately proves nothing.

意思是如果你寫了一個測試，它第一次跑就直接 pass，那它根本沒證明任何東西——你不知道它是在驗證邏輯，還是在驗證空白。

TDD 的 Red-Green-Refactor 裡，RED 那一步要求測試必須先失敗。每個資深工程師都知道這件事，但我還是常看到 agent 寫完 code 就配一個空測試交差。

agent-skills 是怎麼處理的？它直接把這句話寫進 skill，並且列出 agent 可能會說的所有藉口：「我等下再補測試」「這個 edge case 不太可能發生」「現在時間不夠」。每條藉口後面配好反駁話術。

這段我讀了三遍，因為我一直在想：資深工程師心裡本來就有這些對話，只是從來沒人把它寫下來。

過去這些內心對話只能靠 code review 一次一次地傳給新人。你這個 PR 沒測試，我要擋；你這個測試沒失敗過，我要擋；你這邊偷偷 catch 例外，我要擋。

agent-skills 做的事是——把這些 review 當下才會出現的話，搬到 agent 執行當下就出現。

用另一張卡的說法：[[軟體開發價值遷移：從生成程式碼到定義驗收條件]]——當 review 成本從「PR 當下」前移到「工具內建」，工程師的稀缺價值就從寫 code 轉到「寫驗收標準」了。

### 三、三層抽象比 20 個 skills 本身更重要

如果有一天我要把這包 skills 介紹給同事，我不會從 skills 清單講起。我會從三層抽象講起。

| 層次 | 回答的問題 | 例子 |
|---|---|---|
| **Slash Commands** | 什麼時候做？（when） | `/spec`、`/plan`、`/build`、`/review`、`/ship` |
| **Personas** | 誰來做？（who） | code-reviewer、security-auditor、test-engineer |
| **Skills** | 怎麼做？（how） | spec-driven-development、TDD、code-review-and-quality |

這三層可以獨立演進。Persona 的角色可以加可以換、skill 的步驟可以改版、slash command 的觸發時機可以調整，彼此不強耦合。

為什麼這件事重要？過去所有「AI Coding 最佳實踐」的建議都是一坨——一坨 system prompt、一坨 rules file、一坨 CLAUDE.md。當你想改其中一條，你就要重讀整份、重新思考，很容易改出意料外的副作用。

三層拆開之後，行為治理從藝術變成工程。你可以 diff 一個 skill 的改動、可以 A/B 測試兩個 persona 的 review 風格、可以觀察某個 slash command 的觸發率是不是掉了。

這件事呼應了 [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]] 這張卡的主張——Skill 和 prompt 的本質差異在於可系統化迭代、可轉移、可交易。三層抽象讓 iterate、transfer、trade 這三件事第一次真的能做。

---

## 但我還沒想通的三個地方

寫到這裡本來要下結論了，但誠實一點講，我對這包 skills 還有三個疑惑。如果看到這篇的人剛好有答案，也可以告訴我。

### 疑惑一：流程多 vs 流程少，到底哪個對？

我手上有另一張卡[[當工具夠強，你需要更少的流程：Codex 團隊 40 人 1 PM 的運作模式]]，講 OpenAI Codex 團隊 40 人只配 1 個 PM，靠工具夠強所以流程可以砍。

但 agent-skills 做的看起來剛好相反——它在加流程。

我目前給自己的和解是：流程多寡本身其實不是重點，「流程可視」才是重點。agent-skills 把本來就有（但寫在資深工程師腦子裡）的流程搬出來變成可審計物件。至於每個情境要用多少，它自己也說了——Hackathon / typo / 一行改動不該觸發 `/spec`。

這個和解方案對不對，我還不確定。

### 疑惑二：模型大跳級以後，這包 skills 會變技術負債嗎？

[[Agent 架構的做空檢驗：模型翻倍時你的系統會不會自動變簡單]] 讓我很警覺——精心設計的 workflow 本質上是「做空模型進步」的單子。模型跳級時，你之前固化的流程就會變技術負債。

agent-skills 會嗎？我目前的猜測是——三層抽象應該能活下來，細節規則會鬆。例如「每 PR 不超過 100 行」這條未來可能會放寬，但「PR 要有大小限制」這件事不會消失。「寫失敗測試」的硬性 RED 步驟可能會被簡化，但「先定義驗收條件」不會。

這是猜測。要真的驗證，只能等半年後回來看。

### 疑惑三：它在我手上的 codebase 會不會反而有害？

這是最後一個、也是我最擔心的一點。

[[AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性]] 說得很清楚——沒完善測試的 codebase，agent 自主工作會幻覺型產出。

agent-skills 的 TDD / code-review 等 skill 預設「測試基礎建設存在」。如果你拿這包去一個 legacy 沒測試、沒 CI 的 codebase 跑，agent 不會變資深，反而會產出一堆你以為在驗證什麼、實際根本跑不起來的假測試。

這是工具/紀律的前置依賴條件問題。不是 agent-skills 的鍋，但如果我沒注意到，就會是我的鍋。

---

## 我打算怎麼用它

寫了這麼多，我其實還沒真的在自己的案子上跑過整套 skills。這篇不是實戰心得，是讀完之後的理解整理。

但下一步想嘗試的事情我已經有清單：

1. **先在個人小案子上試 5 個 skills**：`spec-driven-development`、`planning-and-task-breakdown`、`incremental-implementation`、`test-driven-development`、`code-review-and-quality`——先不引入 Persona fan-out，只跑 happy path。
2. **觀察 Rationalizations 在哪些時刻被觸發**：我心裡也會冒出那些藉口——「之後再補測試」「這太小不值得開 spec」——看看當 agent 照著反駁話術回我時，我會照做、還是會找新藉口。
3. **判斷它適不適合帶到團隊**：如果在個人案子上都覺得「開銷 > 收益」，拿到團隊也救不了。這件事我想先自己走過再說。

---

## 最後

讀完這包 skills，我的想法很簡單。

資深工程師的紀律，過去只能靠師徒制傳。現在第一次，這些紀律可以被寫下來、可以放進 git、可以讓 agent 照著走。

它不會讓 agent 自動變資深。但它讓資深工程師的判斷，第一次有了可分享、可複製、可累積的形狀。

我會先挑 5 個 skills 在自己的案子上試看看——spec、plan、incremental、TDD、code-review。跑完之後再決定要不要帶到團隊。

如果我自己都做不到這些紀律，我也不會期待 agent 做到。

---

## 查證報告

Draft v2 中涉及的**可查證事實**與我目前對它們的信心度：

| # | 陳述 | 來源 | 信心 | 備註 |
|---|---|---|---|---|
| 1 | `addyosmani/agent-skills` repo 有 20 skills + 3 personas + 7 slash commands | Capture 原文 + repo 描述 | 高 | 原文列出 21 個 skills（含 META 層的 using-agent-skills），正文 20 個核心 + 1 個 meta，敘述時用「20 個 skills」較穩妥 |
| 2 | Addy Osmani 是 Google Cloud AI Director | Capture 原文引用 Addy 網站 | 中高 | 原文標註「Google Cloud AI director」。不是 Google 官方專案已清楚說明 |
| 3 | repo 有 22.4k stars、2.8k forks | Capture 原文（截至查詢時） | 中 | 星數會變動；發文時應避免寫死數字，或加「截至 2026/04」字樣 |
| 4 | Lovable 的 Lazar 主張「80% 規劃、20% 執行」 | 個人卡 [[Vibe Coding：80% 規劃 20% 執行的工作流]] | 高 | 已有卡片佐證 |
| 5 | Kent Beck：「AI 讓我 90% 技能價值變 $0，但剩下 10% 放大 1000x」 | 個人卡 [[Prototype as Spec]] | 高 | 已有卡片佐證；文中未直接引用這句，只泛指「Kent Beck 和幾位架構師主張 Prototype as Spec」 |
| 6 | Karpathy：Claude Code 是第一個令人信服的 LLM Agent 展示 | 個人卡 [[Karpathy：Claude Code 典範]] | 高 | 已有卡片佐證 |
| 7 | `A test that passes immediately proves nothing.` | Capture 原文 agent-skills TDD skill | 高 | 引用整個句子為 agent-skills 原文 |
| 8 | spec-driven-development 六大面向：Objective / Commands / Structure / Code Style / Testing / Boundaries | Capture 原文 | 高 | — |
| 9 | 「未完成 Specify 階段，不得進入 Plan 階段」 | Capture 原文（gated workflow） | 高 | — |

### 可能需要修正的小處

- **star 數**：若要發佈，建議把 repo stars 這段改成「截至 2026 年 4 月超過 22k stars」或直接不寫死數字（目前 Draft v2 內文沒寫 star 數，在 Capture 裡而已，**不需修正**）。
- **Skill 總數**：Draft v2 說「20 個 skills」，原 Capture 附錄其實寫 21 個（含 `using-agent-skills` META 層）。可以保留「20 個核心 skills + 1 個 META skill」更精確，或維持 20（較接近官方 README 的強調口徑）。**建議維持 20，注記在心即可**。

整體查證結果——**沒有需要硬改的事實錯誤**。


