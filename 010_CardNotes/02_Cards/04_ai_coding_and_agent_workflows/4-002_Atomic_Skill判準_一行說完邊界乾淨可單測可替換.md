# Atomic Skill 判準 — 一行說完、邊界乾淨、可單測可替換

- 狀態：WEAK KEEP
- 類型：Heuristic
- 分類：4-
- 索引：010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Coding/01_inbox/20260401_從HarnessEng看skills的原子性.md（#3+#4，合併）

## 核心命題
Atomic skill 的形狀像 `fetch_page_text(url)`、`evaluate_task_completion(task,result)`——進去什麼、出來什麼，邊界乾乾淨淨；但原子化是手段不是目的。

## 卡片內容
好的 skill 像 Unix tool：單一職責、明確 I/O、可組合呼叫、可單測替換。反例：在一支 skill 裡塞五件事的詳細流程＝塞滿冰箱的 monolith prompt。**對沖警告**：目標不是把系統拆到最小單位，是拆到「有意義的邊界」。兩件事如果總是一起發生從不分開，硬拆只是徒增煩惱（一雙襪子不能拆成左右手分別洗）。判準：「總是一起發生」可量化為——三次以上、跨多個 use case 都同時出現，才考慮合併。

## 使用情境
- 設計新的 agent skill 時的形狀檢查
- 重構 monolith prompt 時的邊界判準
- 解釋為什麼「skill 越多越好」是錯的

## 邊界 / 失效條件
- 與既有 [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]] 概念重疊，差異化在「判準 + 反例」
- 拆得太細會讓組合成本爆炸

## 上游連結
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]

## 下游連結
- [[8-001_Tool合約設計_工具是帶驗證的類型化API]]

## 關聯對照
- [[8-002_Harnessability與Ambient_Affordances_AI友善環境的新架構競爭力]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
