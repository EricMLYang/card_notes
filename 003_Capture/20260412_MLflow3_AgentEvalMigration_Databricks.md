# Migrate to MLflow 3 from Agent Evaluation — Databricks

> 來源：Databricks Docs
> 來源類型：官方事實
> 需求層：知識建構
> 連結：https://docs.databricks.com/aws/en/mlflow3/genai/agent-eval-migration
> 搜集日期：2026-04-12
> 搜集原因：K6 — Databricks 正把 agent evaluation、trace、human feedback 與 judge/scorer 收斂成同一個控制平面

## 摘要

這份 Databricks 文件在 2026-03-18 更新，表面上是 migration guide，實際上透露了 Databricks 對 agent eval control plane 的方向：原本獨立的 Agent Evaluation，已被整合進 MLflow 3，並放到 `mlflow.genai` 命名空間下。

最值得注意的不是 API 改名，而是這次整合帶來的五個訊號：統一 UI、統一評估 API、real-time observability 的 tracing backend、streamlined human feedback、以及內建的 improved LLM judges/scorers。這代表 Databricks 想把「trace + eval + labeling + scorer」變成同一套 GenAI / agent lifecycle 的基礎設施。

對你關心的 data / analysis agent 很有價值，因為這不只是模型評測，而是把 evaluation、trace search、dataset、人工標記與治理一起拉進 lakehouse 工作流。

## 為什麼值得看

這篇文件的價值在於，它讓 agent evaluation 從「外掛工具」變成平台內建能力。Databricks 明確要求你改用 `mlflow.genai.evaluate()`、`@scorer`、`search_traces()`，也要求你明確指定 scorers，而不是像舊版那樣自動跑 judges。

這背後透露一個產品哲學轉變：從「幫你自動評」轉向「你自己定義要評什麼」。對有治理要求的資料團隊來說，這種顯性化控制反而更重要。

如果把這篇和你今天已有的 Databricks agent governance 新聞一起看，訊號很清楚：Databricks 不是只想做 agent authoring，而是想把 agent 的 tracing、grading、human review、production monitoring 都吸進自己的控制平面。

## 可能偏誤或限制

這是 Databricks 平台文件，目的是協助既有使用者遷移，因此偏重平台內工作流，不是中立比較文。

文中也明說 MLflow 3 的 Agent Evaluation 只支援 Managed MLflow，不支援 open source MLflow。也就是說，這條路線較適合已深度押注 Databricks 的團隊，不是普遍適用的開放標準。

另外，這份文件本質仍是 API / migration guide，不會直接回答 business semantics、decision correctness 或 domain eval 設計等更高層問題。

## 潛在卡片方向

- Agent evaluation 正從獨立工具變成平台控制面
- `trace + scorer + labeling + dataset` 是同一個閉環，不該分開想
- Databricks 的顯性 scorer 選擇，代表從自動 judge 走向可治理評估
- Evaluation 結果存成 traces，意味著「觀測」和「評估」正在合流
- 可連結的現有卡片：[[DecisionOps]]
- 可連結的現有卡片：[[AI時代評估能力成為關鍵槓桿點]]
- 可連結的現有卡片：[[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]

---

## 全文重點整理

以下為依原文重寫的中文整理，非逐字全文翻譯。

Databricks 在這份文件一開頭就講得很明白：`Agent Evaluation` 已經整合到 `MLflow 3 on Databricks`，未來 SDK 方法都會透過 `mlflow[databricks]>=3.1` 的 `mlflow.genai` 命名空間暴露。

這次升級引入的核心能力包括：

- 更新後的 UI，與 SDK 功能對齊
- 新的 `mlflow.genai` API，可跑 evaluation、human labeling、evaluation datasets 管理
- 強化 tracing，並有 production-scale trace ingestion backend，支援 real-time observability
- 更順的 human feedback 收集流程
- 改善過的內建 LLM judges / scorers

如果用你的語言來翻，這表示 Databricks 正在把 agent 的「可觀測性、可評估性、可人工校準性」一起包進基礎平台，而不是把它留在模型外部。

文件裡還有幾個值得注意的遷移方向：

1. `mlflow.evaluate()` 要改成 `mlflow.genai.evaluate()`
2. `@metric` 要改成 `@scorer`
3. `request / response / expected_response` 這類欄位，統一改成 `inputs / outputs / expectations`
4. 不再自動選 judge，而是必須顯性指定 scorers
5. 結果不再用舊的 result table 思路去看，而是透過 `search_traces()` 查 traces 與 assessments

這些改動看似技術細節，實際上是一個更大的設計訊號：Databricks 想把每次 agent 執行視為可追蹤的 trace，再在 trace 上掛 assessment、feedback、human labeling，形成統一資料模型。

文件也指出，舊版 MLflow 2.x 的 judge 運行方式比較偏「只要資料欄位符合，就自動替你跑一批 judge」。到了 MLflow 3，Databricks 要求你顯性列出想跑的 `Correctness()`、`Safety()`、`Guidelines()`、`RetrievalGroundedness()` 等 scorers。

這種改法意味著兩件事：

- 評估標準不再是黑箱預設，而是產品 / 團隊要自己負責定義
- scorer 與 judge 變成可治理資產，而不是隱藏在 evaluator_config 裡的副作用

另外一個你會有感的點，是 evaluation results 現在被存成 traces with assessments。這讓 evaluation 不只是離線表格，而是可以和 production traces 接在一起。也就是說，同一套 trace-based infrastructure 可以同時服務 debug、monitoring、offline eval、human review。

這篇文件真正值得記住的不是哪個 import 改名，而是它背後的方向：**資料平台開始把 agent 的評估與觀測，正式拉進平台級控制面。**
