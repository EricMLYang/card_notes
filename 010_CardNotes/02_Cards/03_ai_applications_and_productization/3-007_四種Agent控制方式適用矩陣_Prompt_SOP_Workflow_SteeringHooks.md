# 四種 Agent 控制方式適用矩陣 — Prompt / SOP / Workflow / Steering Hooks

- 狀態：KEEP
- 類型：Pattern
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260321_agent控制流程不能只靠長prompt.md（#1，吸收 #3 邊界）

## 核心命題
Agent 控制不是「找一招最強的」，而是按「規則明確度 × 輸入變異度 × 推理彈性需求」三軸分流，且四種方式可疊加使用。

## 卡片內容
Strands 的 600 trial 顯示：Steering 100% / SOP 99.8% / Prompt 82.5% / Workflow 80.8%，且 Steering 的 input token 約是 SOP 的 1/3。但這不代表 Steering 萬用——四種方式的適用條件是：**Prompt** 適合原型與簡單 agent；**SOP** 適合要高可靠但無 hook 能力的環境；**Workflow/Graph** 適合輸入變異小且流程明確；**Steering Hooks** 適合「保留推理彈性但有些規則絕不能違反」。最強組合常是 SOP backbone + Steering Hooks 補強。重要邊界：Steering 只能擋住「你定義的攔截點」，沒攔的還是會漂移——hook 不會自動讓 agent 變聰明。

## 使用情境
- 為新 agent 選擇控制策略時的決策表
- 解釋為什麼「workflow 越完整越穩定」是錯覺
- 設計 agent 治理時的混合策略起點

## 邊界 / 失效條件
- 數據來自 Strands 自家 library renewal benchmark
- Steering 需要可注入 hook 的框架支援
- SOP 在 token 成本敏感場景仍會被 prefix caching + Steering 打敗

## 上游連結
- [[3-006_Harness六層構成_Agent系統工程的解構]]
- [[Agent 產品 95% 在 Production 失敗的原因]]

## 下游連結
- [[10-002_Policy_as_Code護欄要在LLM之外執行]]
- [[當計算轉為純執行，評估標準成了唯一的控制介面]]

## 關聯對照
- [[Opinionated Agent 產品設計原則]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
