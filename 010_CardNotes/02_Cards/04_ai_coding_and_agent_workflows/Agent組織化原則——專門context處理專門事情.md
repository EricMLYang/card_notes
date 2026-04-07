# Agent 組織化原則——專門 context 處理專門事情

- 狀態：KEEP
- 類型：Heuristic
- 分類：4-
- 索引：010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260324_CoreNote_用Context看組織管理.md

## 核心命題
Agent 最高效的組織方式是「專門的 context 處理專門的事情，不確定的部分靠 model 基礎能力支撐」。

## 卡片內容
基於 Agent context 可輕量分切的特性，最高效的做法是讓每個 Agent 只承載一件事的 context，職責極清晰、context 極輕。不確定的知識缺口靠大型模型的基礎能力補位。這樣做的好處：(1) 每個 Agent 的行為可預測、可量化；(2) job queue 管理變簡單，一個任務對應一個 context 實例；(3) 出錯時隔離範圍小。反之，若一個 Agent 塞很多 context（模仿人類多工），會讓 Agent 行為難以預測，debug 困難，且浪費了 context 可分切的結構性優勢。

## 使用情境
- 設計 Skill / Agent 的粒度時，判斷該切多細
- 規劃 Agent job queue 與排程架構
- 評估現有 Agent 是否承載過多 context（過度「擬人化」）

## 邊界 / 失效條件
- Model 基礎能力不足時（如特定領域知識），純靠 model 補位會導致錯誤率上升，需要顯式注入 context
- 過度分切可能導致 Agent 數量爆炸，orchestration 本身成為瓶頸
- 某些任務天然需要跨步驟的持續 context（如長對話、多輪決策），強制分切會破壞任務完整性

## 上游連結
- [[組織設計是context管理——人類集中昂貴Agent輕量可分切]]

## 下游連結
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]
- Single Responsibility Principle 在 Agent 架構的實踐

## 關聯對照
- Unix 哲學（Do One Thing Well）
- [[Agent 開發的典範轉移：80% 時間從工程問題搬到領域問題]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
