# 4-AI Coding Agent 自主工作的兩個硬前提：測試覆蓋率 + 環境可複製性

**類型**：Heuristic

## 概念

AI Coding Agent 能否從「人類盯著跑」升級到「放著讓它做」，取決於兩個不可妥協的前提：(1) 測試覆蓋率夠高，Agent 改壞能自己跑測試發現並修復，人只需 review 最終結果；(2) 環境可複製，Agent 能在獨立 sandbox 中把服務跑起來驗證。Stripe Minions 成功因為本來就有大量測試，Cloudflare 一人一週遷移 Next.js → Vite 靠的是完整 AI 文件 + 全面測試案例。反面：沒測試的公司只能工程師硬 review 或「勇敢按 merge」。

## 重要性

這是判斷「組織是否具備 AI Coding 槓桿基礎」的快速檢驗標準。

## 邊界/反例

測試覆蓋率高但測試品質差（只測 happy path）一樣無效。探索性開發、UI 互動密集型任務目前仍難以自動化驗證。

## 標籤

#AICoding #測試覆蓋率 #環境可複製 #Stripe #自主工作
