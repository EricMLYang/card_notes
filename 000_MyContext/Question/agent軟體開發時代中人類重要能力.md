# 有經驗的人用 Coding Agent 可以發揮 20x，新手只能 5x，中間的差距是什麼？

> AI 其實可以用 100x 速度開發，但你的控制能力有限，加速到 5x 就無法再快了。有經驗的人就能發揮到 20x，差別就在這裡。
> — Andrew Chen

---

## 資深者提到的關鍵差距

### 1. 定義規格的能力（Interface / SKILL）
- 用 code 寫規格，定義 interface — *Andrew Chen*
- 設計 SKILL，讓 Agent 理解任務邊界 — *Andrew（Agent SDK）*
- 把模糊商業需求翻譯成可執行規格 — *TDD 文章*

### 2. 定義驗收標準的能力（Test / Eval）
- 用 test case 定義「什麼叫做對」 — *Andrew Chen*
- 測試是與 AI 溝通的「唯一精確語言」 — *TDD 文章*
- 資料合約 + 商業常識斷言（數據分析的 TDD） — *我的觀點文*
- 軌跡評估 + LLM-as-a-Judge（Agent 的 Eval） — *我的觀點文*

### 3. 準備執行脈絡的能力（Context / Tools）
- CLAUDE.md 建立專案 context — *Vincent Quigley*
- MCP 整合外部工具（Linear, Notion, DB, GitHub） — *Vincent Quigley*
- 選擇配給 Agent 哪些 Tools — *Andrew（Agent SDK）*

### 4. 迭代與 Review 的心法
- 預期三次迭代：95% 垃圾 → 50% 垃圾 → 可用起點 — *Vincent Quigley*
- 直接 Review（Interface + Test）+ 間接 Review（讓編譯器幫你驗） — *Andrew Chen*
- 把 AI 當「永遠不會學習的 Junior Developer」 — *Vincent Quigley*

### 5. 設計判斷與品味
- 親自寫部分 interface/test，這是「品味」 — *Andrew Chen*
- 骨架打好了，肉再長也歪不到哪裡去 — *Andrew Chen*
- 抽象化能力：能快速寫出定義邊界的 code — *Andrew Chen*

---

## 來源文章
- 20260226_用 Interface + Test 驯服 AI Coding 的不确定性（Andrew Chen）
- 20260226_當TDD不再是品質保證，而是AI的操控介面
- 20260226_Agent SDK開發心得：從工程問題到領域問題
- 20260221_StaffEngineer的ClaudeCode六週實戰（Vincent Quigley）
- 20260227_當計算轉為純執行，評估標準成了唯一的控制介面（我的觀點文）
