---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
# Agent Harness in 2026 — Phil Schmid

> 來源：philschmid.de（Phil Schmid 個人技術部落格）
> 來源類型：高密度觀點
> 需求層：知識建構
> 連結：https://www.philschmid.de/agent-harness-2026
> 搜集日期：2026-04-12
> 搜集原因：K1 — AI Agent 工程化與 harness 設計

## 摘要
作者把 Agent Harness 類比成「Operating System」：Model 是 CPU、Context Window 是 RAM、Agent 是 Application，而 Harness 才是真正讓 Agent 從 demo 走到上線的那層作業系統。文章核心論點是「benchmark 上 1% 的差距，看不出模型在 50 步之後會不會崩」，要靠 harness 才能把多步驟、多日的 workstream 變成可被 log、可被 grade 的結構化資料。

## 為什麼值得看
這篇是少數把 harness 講成「OS 級抽象」的長文，而且舉的案例很實在：Manus 在 6 個月內把 harness 重構 5 次、LangChain 一年內把 Open Deep Research agent 重新架構 3 次、Vercel 把 agent 工具刪掉 80% 之後反而更快。對應到 Eric 自己「decision system 不是模型而是 harness」的主軸，這篇是直接的彈藥庫，特別適合拿來寫「為什麼 Agent 上不了線，問題不在模型」的判準文。

## 可能偏誤或限制
- 作者立場偏「open-source harness」與工程實作派，對於企業治理、權限邊界、人工 checkpoint 的著墨較少
- 案例都是面向「Coding Agent / Research Agent」這類技術型 Agent，未直接談垂直領域 business decision agent 的差異
- 沒有討論 harness 與 Unity Catalog / MCP / 治理層如何接合，需要自己補

## 潛在卡片方向
- Agent Harness = OS 的類比卡（CPU/RAM/OS/App 對應 Model/Context/Harness/Agent）
- 「Build to Delete」原則：harness 要模組化，因為下一代模型會讓現有控制流失效
- Harness as Dataset：競爭優勢從 prompt 移到 trajectory 資料
- 可串連卡片：[[Harness Engineering 是 Agent 上線的關鍵]]、[[Coding Agent 工作流的 verification 設計]]

---

## 全文翻譯（重點摘錄）

### 為什麼需要 Agent Harness
- 傳統 model benchmark 會錯過最關鍵的「可靠性」問題：「leaderboard 上 1% 的差距，無法偵測模型在 50 步之後會不會偏離軌道。」
- Harness 讓多日的 workstream 變得可靠，這是模型 benchmark 看不到的能力。

### 計算機類比
- **Model = CPU**：原始運算能力
- **Context Window = RAM**：有限的揮發性記憶
- **Agent Harness = OS**：管理 context、boot sequence、tool 處理
- **Agent = Application**：使用者特定的邏輯
- Harness 提供「prompt presets、tool call 的意見化處理、lifecycle hooks，以及 planning、filesystem access、sub-agent management 等開箱即用能力」

### Harness 為什麼重要的三個理由
1. 用真實 use case 驗證實際進度（而不是 leaderboard）
2. 用驗證過的 pattern 提供一致的使用者體驗
3. 建立 feedback loop：「Harness 把模糊的多步驟 agent workflow 變成可以 log、可以打分的結構化資料」

### 真實案例
- **Manus**：在 6 個月內把 harness 重構 5 次
- **LangChain**：一年內把 Open Deep Research agent 重新架構 3 次
- **Vercel**：把 agent 工具刪掉 80%，回應速度反而更快

### 三條給團隊的行動建議
1. **Start Simple**：避免巨大的控制流，讓模型自己 plan
2. **Build to Delete**：保持架構模組化，因為新模型會讓現有邏輯過時
3. **Harness as Dataset**：競爭優勢從 prompt 轉移到「Harness 捕捉的 trajectory」

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Phil Schmid 主張「模型 benchmark 的 1% 差距」無法揭露 Agent 在 50 步以後的可靠性，因此真正決勝點是 Harness 這層 OS-like 抽象。他用 CPU/RAM/OS/App 類比 Model/Context/Harness/Agent，再以 Manus、LangChain、Vercel 三個重構案例佐證 harness 是會被反覆推翻的演進產物，最後給出 Start Simple / Build to Delete / Harness as Dataset 三條行動原則。
- 作者挑戰的預設：「模型升級＝產品升級」、「Agent 競爭力＝prompt engineering」、「框架抽象越多越好」這三個業內常見假設。
- 個人映射：直接補強 Eric「decision system 不是模型，而是 harness」的主軸；把 K1（AI Agent 工程化）從泛論推向「OS 級抽象 + trajectory 是新護城河」的工程語言。Build to Delete 同時打到知識系統建造者偏好的「模組化 / 可重組 / 抗結構性過時」原則，可作為跨領域類比（Agent Harness ↔ Repo-as-Worker ↔ Card System）。
- 個人挑戰：作者偏 open-source / 工程派，沒談治理層、權限邊界、人工 checkpoint，這正好是 Eric 在 RMN / business decision agent 場景需要自行補上的空白。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent Harness 是 OS 級抽象，不是框架糖衣
- 分級：Core
- 類型：Principle
- 核心內容：把 Model 視為 CPU、Context Window 視為 RAM、Agent 視為 Application，那麼 Harness 就是負責 boot sequence、context 管理、tool 處理、lifecycle hooks 的 OS。它提供 prompt presets、planning、filesystem access、sub-agent management 等開箱即用能力，使多步驟、多日 workstream 從「demo」變成「可上線系統」。沒有這層抽象，Agent 等於跑在裸機上的 app，無法處理長期運作的不確定性。
- 保留理由：把 harness 從「工程細節」抬升到「架構決策」層級，是 decision system 對外溝通的高槓桿語言。
- 待補強處：OS 類比的失效邊界（哪些 Agent 場景反而不該有重 harness？）
- 初步知識鉤子：[[Harness Engineering 是 Agent 上線的關鍵]]、Repo-as-Worker、Decision System 架構分層

序號 2
- 候選標題：Benchmark 的 1% 差距看不出 50 步後的崩潰
- 分級：Core
- 類型：Heuristic
- 核心內容：模型 leaderboard 比較的是單步表現，但 Agent 真正的失效模式是長 horizon 的軌跡偏離。當任務需要 50 步以上連續決策，1% 的單步差距會放大成完全不同的可靠性曲線。判準應該換成「在真實 use case 連跑 N 步後是否還在軌道上」，而不是 leaderboard 排名。這也是為什麼模型升級不等於產品升級。
- 保留理由：直接挑戰「選最強模型就好」的常識，是寫「為什麼 Agent 上不了線」判準文的核心彈藥。
- 待補強處：N 該怎麼設？有沒有可量化的 trajectory drift 指標？
- 初步知識鉤子：可觀測性思維、Evaluation harness、Decision Loop、AI Coding 風險治理

序號 3
- 候選標題：Build to Delete — Harness 必須假設下一代模型會推翻自己
- 分級：Core
- 類型：Principle
- 核心內容：Manus 6 個月重構 5 次、LangChain 一年重構 Open Deep Research 3 次、Vercel 刪掉 80% 工具反而更快。這些案例指向同一條原則：harness 的最佳設計不是「未來相容」，而是「容易被刪」。每一代模型的能力邊界會直接讓現有控制流過時，因此架構應保持模組化、低耦合、可拋棄。把工程資產押在 prompt / 控制流上會被模型升級洗掉。
- 保留理由：跨域可遷移的反脆弱原則，能直接接到知識系統 / repo 設計 / data product 平台化決策。
- 待補強處：哪些模組屬於「不能刪」的長期資產（trajectory data？eval set？）？刪除節奏的判準是什麼？
- 初步知識鉤子：模組化抽象、Adapter Pattern、卡片系統的「可重組原則」、平台化能力模組

序號 4
- 候選標題：Harness as Dataset — 護城河從 Prompt 移到 Trajectory
- 分級：Core
- 類型：Pattern
- 核心內容：當 prompt 與 tool 設計都會被下一代模型抹平，真正能複利的是 harness 在執行過程中捕捉的 trajectory：每一步的決策、tool call、verification、失敗與回補。這份結構化資料能拿去做 fine-tuning、eval、failure analysis，形成持續放大的回饋迴路。Agent 競爭力從「誰寫得出好 prompt」轉成「誰累積得出高品質軌跡資料集」。
- 保留理由：直接定義新一輪 AI 護城河，與 data moat / decision moat 主軸高度交叉。
- 待補強處：Trajectory 的資料治理（隱私、語意穩定性、權限邊界）如何設計？跟 Unity Catalog / lineage 怎麼接？
- 初步知識鉤子：Data Moat、Decision Loop、評估資料集設計、資料契約、Trace as Spec

序號 5
- 候選標題：Start Simple — 讓模型自己 plan，避免巨大控制流
- 分級：Support
- 類型：Heuristic
- 核心內容：Vercel 把 80% 工具刪掉後反而變快，背後是「過度工程化的控制流會搶走模型的 planning 能力」。當 harness 試圖用條件分支與 routing 規則涵蓋所有狀況時，反而限制了模型在不確定情境下的彈性。預設應該是「最少控制流 + 讓模型 plan」，只有當 plan 失效時才補上控制流。這條與「Build to Delete」互為表裏：少寫，才好刪。
- 保留理由：可重複套用的工程判準，能直接寫進 agent 設計 checklist。
- 待補強處：什麼時候「最小控制流」會失效？哪些場景必須先寫死 deterministic flow（如金流、權限）？
- 初步知識鉤子：Less is more 工程原則、TOC 瓶頸思維、Agent 設計 checklist

序號 6
- 候選標題：技術型 Agent 的 Harness 設計，不能直接套到 Business Decision Agent
- 分級：Question
- 類型：Question
- 核心內容：[Inference] Phil Schmid 引用的案例（Manus、LangChain Open Deep Research、Vercel）都是 Coding Agent 或 Research Agent，這類 Agent 的失效成本相對可控（重跑、回滾、人工接手）。但垂直領域的 business decision agent（如 RMN 廣告投放決策、庫存補貨、產線停機判斷），失效會直接打到營收與責任歸屬。harness 的設計重點可能要從「彈性 / 速度」轉向「人工 checkpoint / 可審計 trace / 權限邊界」。這條尚無定論，但值得追蹤對比案例。
- 保留理由：補上原文未談的治理 / 責任邊界視角，是 Eric 自己的差異化切入點。
- 待補強處：需要找到 1–2 個 business decision agent 的實作案例對照（保險核保、零售決策、醫療輔助）。
- 初步知識鉤子：人工 checkpoint 設計、AWS Shared Responsibility、Unity Catalog 治理、AI Coding 風險治理

序號 7
- 候選標題：Harness 把模糊 workflow 變成可 log、可 grade 的結構化資料
- 分級：Support
- 類型：Pattern
- 核心內容：Harness 的第三個價值（在「驗證進度」「一致 UX」之外）是把多步驟 agent workflow 從黑盒變成結構化 trace。每一步都被記錄成可查詢、可標註、可打分的事件，feedback loop 才得以建立。這條與「Harness as Dataset」互補：前者談「為什麼要記」，這條談「記下來之後 evaluation / debugging 會怎麼長」。沒有結構化 trace，eval 只能停在「整體成功率」這種粗顆粒指標。
- 保留理由：connect 到 evaluation harness、可觀測性、business data science 的事件定義主軸。
- 待補強處：trace 的事件 schema 該怎麼設計？哪些欄位是長期穩定、哪些會隨模型演進？
- 初步知識鉤子：事件定義、語意層、可觀測性、Evaluation Pipeline、Trace Schema 設計

## C. 建議送 refine 的項目
- 必送：序號 1（OS 類比）、序號 2（Benchmark 失效）、序號 3（Build to Delete）、序號 4（Harness as Dataset）
- 次送：序號 5（Start Simple，可能與序號 3 合併或作為附帶推論）、序號 7（結構化 trace，可能與序號 4 合併）
- Question 類保留：序號 6（business decision agent 差異）— 作為長期追蹤問題卡

## D. 呼叫 refine-cards
- 將上述候選卡（序號 1–7）交由 refine-cards 精煉；重點處理：序號 3 vs 5 的合併取捨、序號 4 vs 7 的層級關係、序號 6 是否獨立成 Question 卡。
