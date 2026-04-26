---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-04-16
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
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


<心得文>
# 當評估變成 Agent 工程的護城河：從 Databricks MLflow 3 看數據分析 Agent 該怎麼自學

## 引言：一份 migration guide，卻洩漏了產業方向

最近看到 Databricks 在 2026 年 3 月更新的一份文件，標題是《Migrate to MLflow 3 from Agent Evaluation》。表面上是 API 搬家指南，告訴你舊的 `mlflow.evaluate()` 要改成 `mlflow.genai.evaluate()`、`@metric` 要改成 `@scorer`。

但真正值得看的不是改名，而是它洩漏了 Databricks 對 agent 工程的整體佈局——把原本獨立的 Agent Evaluation 收進 MLflow 3，和 tracing、human feedback、dataset 綁成同一個控制平面。

這個動作背後，是一個我認為未來兩年對資料團隊最關鍵的趨勢：

**Agent 品質的瓶頸，已經從「模型能力」轉移到「評估能力」。**

模型會持續變強，但換一個更強的模型，你的 agent 可能只好一點點。真正拉開團隊差距的，是你有沒有能力定義「什麼叫做好」、有沒有辦法快速發現它壞在哪、有沒有機制讓 production 錯誤持續回餵改進。

對我這種想做數據分析 agent 的人來說，這個訊號很明確：**如果我只會寫 prompt、串 API，一年後市場上會遍地都是這種人；但如果我能把 agent 當成可工程化的產品來做，這套能力差距是複利的。**

這篇心得整理我從這份文件延伸出去的學習路線，重點不是 Databricks 的 API，而是 **做數據分析 agent 該補的基本功**。

---

## 一、先把幾個容易被跳過的詞搞懂

我發現自己過去一年讀 agent 相關文章時，有幾個詞會被反覆提到，但從沒被真正解釋過。補完這幾個詞，後面整套思考才接得起來。

### MLflow 是什麼

可以想成 **模型和 AI 系統的版本控制 + 建置紀錄系統**。

寫程式用 Git 記 commit、用 CI/CD 記 build log，但訓練模型或跑 agent 光靠 Git 不夠——你還想知道這次用什麼參數、跑出什麼 metric、產出的 artifact 存在哪。MLflow 就是做這件事的開源工具。

MLflow 2 時代主要服務傳統 ML（訓練分類器那類），MLflow 3 加了 `mlflow.genai` 這個專門給 LLM 和 agent 的命名空間，核心是兩件事：**tracing（記錄 agent 每一步做了什麼）** 和 **evaluation（評估做得好不好）**。

Databricks 賣的是「Managed MLflow」，概念類似 GitHub 之於 Git——開源版你可以自己架，但 Databricks 幫你 host 並加額外功能。

### Scorer 是什麼

**一個會回傳「這次 agent 表現好不好」的 function。**

最簡單的 scorer 長這樣：

```python
@scorer
def response_length_check(inputs, outputs, expectations=None, traces=None):
    length = len(outputs.get("response", ""))
    return "yes" if 50 <= length <= 500 else "no"
```

四個固定參數：使用者問了什麼（inputs）、agent 回了什麼（outputs）、正確答案是什麼如果有的話（expectations）、agent 中間做了哪些事（traces）。

Scorer 有兩種：

- **程式邏輯 scorer**：用 if-else 判斷，例如「回答有沒有引用 table 名」。便宜、快、確定。
- **LLM-as-judge scorer**：呼叫另一個 LLM 當裁判。貴、慢，但能處理主觀判斷。Databricks 內建的 `Correctness()`、`Safety()` 都屬於這種。

最直觀的類比：**scorer 是 unit test 的進化版**。Unit test 回傳 pass/fail，scorer 也一樣；差別是 scorer 可以評估「沒有唯一正確答案」的輸出。

### Trace-level vs Span-level

這兩個詞是 debug 功力的分水嶺，但其實你每天都在用同樣的思維——只是用在 PySpark job 上。

一個 PySpark job 會分成好幾個 stage，每個 stage 又有好幾個 task。Job 失敗時你會先看整體 fail 了沒，再點進去看是哪個 task 出問題。

Agent 的 trace 結構一模一樣：

```
Trace: 使用者問「上週店 A impression 比店 B 高多少？」
├── Span 1: 理解問題（LLM call）
├── Span 2: Retrieval（查 Delta table）
├── Span 3: 產生 SQL
├── Span 4: 執行 SQL
└── Span 5: 產生最終回答（LLM call）
```

- **Trace-level 評估**：整條跑完後，最終答案對不對？
- **Span-level 評估**：每一步單獨看，retrieval 有沒有抓到對的 table？SQL 有沒有寫對？

為什麼要分兩層？因為只看 trace-level，你知道答案錯了但不知道錯在哪。Span-level 才能 pinpoint 是 retrieval 壞了、還是 retrieval 對了但 LLM 算錯數字。如果 retrieval 根本沒找到對的資料，那 prompt 再怎麼調都沒用——**你要修的東西不一樣**。

### Binary pass/fail 為什麼重要

想像我叫你給每個 PR 打 1-10 分，你會卡住：「這個該給 6 還是 7？」同一個你隔天看可能還打不同分。但如果我只問「這個 PR 該 merge 嗎？yes/no」，你反而很快能答。

LLM judge 一樣。研究和實務都發現：

- 問它「1-5 分」→ 分數飄移嚴重，同一個答案今天 3 分明天 4 分。
- 問它「可接受嗎？yes/no」→ 穩定很多。

所以最佳實務是 **先用 binary 建立及格線，等團隊對「什麼叫可接受」有共識後，再細分 excellent / acceptable / poor**。

這和帶團隊一樣：新規範先訂「能不能過」，不要一開始就訂 A/B/C/D 級。

### Evaluation 與 Observability 合流

先分清楚這兩個詞：

- **Evaluation**：上線前跑的。你有 golden dataset（幾十筆已知問題+正確答案），每次改 prompt 或換模型跑過這組看有沒有退步。像 unit test。
- **Observability**：上線後跑的。使用者真實在問什麼、哪些 query 讓 agent 崩、latency 多少。像 Datadog。

過去這兩件事用完全不同的工具、不同的資料格式、不同的團隊在管。Eval 產出離線表格，observability 產出 time-series 和 log。

**MLflow 3 做了一個關鍵設計：evaluation 的結果不存表格，存成 trace。** 這意味著：

1. Production trace 和 eval trace 是同一種格式，同一個 query 可以撈兩邊。
2. 同一組 scorer 可以跑在兩邊：`Correctness()` 上線前跑 golden set，上線後抽樣跑 production。
3. Production 發現的 bad case 可以直接變 golden case。使用者問了一個答錯的問題 → human 標記 → 寫回 eval dataset → 下次 regression test 測到。

用我們熟的 Medallion 思維：**production traces 是 Bronze、human labeling 是 Silver、curated golden dataset 是 Gold**。過去這三層是三套工具、三種格式；現在 trace-based 資料模型讓它們在同一條 pipeline 裡流動。

---

## 二、從這個趨勢看，數據分析 Agent 該怎麼自學

把上面幾個詞串起來，我重新整理了自己的學習路線。核心思路是：**別再只練「怎麼讓 agent 跑起來」，要練「怎麼持續知道它跑得好不好」。**

### 學習路線一：先建立 eval-first 的思維習慣

傳統開發流程是「寫 code → 看結果 → 覺得 OK 就交」。Agent 開發的正確流程應該是：

1. 先寫 10-20 筆 golden case（使用者問什麼、期望回什麼）
2. 再寫 scorer 定義什麼叫「可接受」
3. 才動手實作 agent
4. 每次改 prompt / 換模型 / 換檢索邏輯，都跑過這組 eval

這個順序逆過來很重要。先寫 eval，你會被逼著想清楚「這個 agent 到底要達到什麼」——這個問題在只寫 prompt 的流程裡經常被跳過。

### 學習路線二：把 scorer 當成核心資產，不是附屬品

Scorer 不是寫完 agent 之後的額外工作，它本身就是產品定義。

對數據分析 agent，我會先練這幾種 scorer：

- **Correctness**：數字對不對（需要 ground truth）
- **RetrievalGroundedness**：回答有沒有基於真實資料，還是幻覺
- **Guidelines 類**：domain-specific 規則，例如「不能跨 tenant 取數」「必須標明資料來源 table」
- **自訂 `@scorer`**：硬規則，例如「SQL 必須包含 WHERE 條件避免全表掃描」

注意這幾個 scorer 涵蓋了三個層次：**事實正確性、資料基礎、商業約束**。好的數據分析 agent 這三層都要過。

### 學習路線三：Trace 是 debug 的起點，不是 log

過去看 agent 出錯，很容易陷入「再改一次 prompt 試試」的死循環。正確姿勢是先看 trace：

- Retrieval span 抓到什麼 context？如果 context 就錯，prompt 再好也沒用。
- SQL 生成 span 產出什麼 query？如果 SQL 錯了，generation 才是要修的點。
- 最終 LLM 拿到什麼輸入？如果輸入對了輸出還錯，才是 prompt 或模型問題。

**這個習慣能把 debug 時間從「一下午」壓到「十分鐘」，因為你知道該修哪一層。**

### 學習路線四：把 production 變成最大的 dataset 來源

這是 eval 和 observability 合流帶來的最大紅利。

具體做法：

1. 所有 production trace 都收集起來
2. 抽樣讓 scorer 跑過（例如 5% 的 traffic）
3. scorer 標為「疑似有問題」的 trace 丟到 labeling queue
4. Human reviewer 確認後，把這些 case 寫回 golden dataset
5. 下次 regression test 就會測到這類情境

這個 loop 運作起來之後，你的 agent 品質會是複利成長——**每一個使用者遇到的 bug 都在幫你變更強**。

### 學習路線五：把這套做法寫進 code review 規範

我們團隊正在定義 L1/L2/L3 code review。我的想法是：**scorer 的定義和修改要歸為 L2 以上**。

原因是 scorer 一旦上線，會影響整個 agent 的迭代訊號。錯的 scorer 會讓團隊優化錯方向——就像 metric 定義錯了，整個團隊 KPI 都在衝錯目標。這個風險比單次 prompt 改動大得多。

---

## 三、為什麼我選擇在這個時間點押這件事

產業現在處在一個微妙的點：

- 模型層的差距正在縮小（GPT / Claude / Gemini 拉不開）
- Agent 進 production 的比例快速拉高（2025 年已 40%）
- 但 eval 和 observability 工具還碎片化（Langfuse / Arize / Opik / W&B 各做一塊）

這個狀態很像 2015 年前後微服務大爆炸、observability 工具（Datadog、Honeycomb）還沒成熟的時期。**誰先把一套整合的工程實踐建立起來，誰就拿到未來兩年的 agent 開發紅利。**

對我個人來說，選擇在這個時間點投入 eval infrastructure 的學習，有三個理由：

1. **我的團隊已經在 Databricks 上**，MLflow 3 直接可用，學習成本攤在日常工作裡。
2. **MI 2.0 正要嵌 AI agent**，這正好是把這套方法論落地的場域。
3. **這是複利型能力**，不是「學一個新 framework」那種一次性投入——scorer 定義、golden dataset、trace debugging 習慣，都會在未來每個 agent 專案裡累積複用。

---

## 四、三個可以立刻開始的小實驗

寫完這篇心得，我給自己列了三個下週就能動手的小實驗：

**實驗一：挑一個現有的 agent，補上 5 個 scorer**。不用多，先有就好。跑一次看看 pass rate 是多少，找到第一個真正會 fail 的 case。

**實驗二：挑一個已知的 bad case，從 trace 開始 debug**。練習先看 retrieval span、再看 generation span 的思維習慣，而不是直接跳到 prompt。

**實驗三：把一筆 production 真實 query 變成 golden case**。走完「觀察 → 標記 → 寫回 dataset → regression test」這個 loop 一次，感受完整的閉環。

這三個實驗都很小，但它們覆蓋的是 **從 eval-first 思維、到 span-level debug、到 production-to-dataset 閉環** 的核心動作。做完一輪，整套方法論就從概念變成肌肉記憶了。

---

## 結語

這篇心得的起點是一份看起來很技術的 Databricks migration guide，但真正的主題不是 MLflow 3 怎麼用，而是：**agent 工程正在從手工業變成工程學科**。

如果你和我一樣在做數據分析 agent，我認為現在最值得投入的，不是再學一個新的 LLM framework，而是 **把評估能力變成團隊的肌肉記憶**。模型會變，framework 會換，但「怎麼定義好、怎麼發現壞、怎麼持續改進」這套思維框架不會過時。

這也是為什麼我會說，這份文件不是一份 migration guide——它是一份 **產業方向的訊號文件**。看懂它的人，下一步就知道該投資什麼。

# BreadCards

## A. 主脈絡與個人映射
- **論證骨架**：表面是 API migration guide，但作者把它讀成「Databricks 把 trace + eval + labeling + scorer 收斂為單一 GenAI / agent 控制平面」的訊號文件，並推出五個關鍵設計轉變：統一 UI、統一 API、production-scale tracing backend、streamlined human feedback、顯性 scorer 指定。同時心得文延伸出「Agent 品質瓶頸已從模型能力轉到評估能力」的判斷與五條學習路線。
- **挑戰的預設**：「evaluation 是離線一次性工作」「judge 是黑箱自動跑」「observability 與 evaluation 是兩個工具兩種資料模型」。
- **個人映射**：直接命中我關注的 Harness 視角、AI 評估能力作為複利槓桿、以及「analysis workflow productization」三條主線。trace-based 統一資料模型的論點特別有用——把 production traces / human labeling / golden dataset 對應成 Bronze / Silver / Gold，是把 Medallion 思維遷移到 agent eval 的精彩類比。也補強我對 RMN 場景的應用思考：agent 出錯時必須能 span-level 拆解 retrieval / generation / SQL，否則 debug 會死循環。

## B. 候選卡（Lite）

序號 1
- 候選標題：Agent 品質瓶頸正從「模型能力」轉移到「評估能力」
- 分級：Core
- 類型：Principle
- 核心內容：模型會持續變強，但換模型對 agent 整體品質提升有限；真正拉開團隊差距的是「能否定義什麼叫好、能否快速發現它壞在哪、能否讓 production 錯誤持續回餵」。這個判斷把投資焦點從「追新模型」轉到「建評估基礎設施」，是面對「LLM 排名變動快」時的穩定錨點。
- 保留理由：明確的視角翻轉與投資判準，可作為個人 / 團隊技能投資的指南針
- 待補強處：何時這個論點會失效（例如真的有跨代模型躍升時）、評估能力的具體量化指標
- 初步知識鉤子：[[AI時代評估能力成為關鍵槓桿點]]、[[Harness 是把模型變成 Agent 的關鍵（不是模型本身）]]、複利能力 vs 一次性能力

序號 2
- 候選標題：顯性 scorer 取代自動 judge — 從「自動評」到「自己定義要評什麼」的產品哲學轉變
- 分級：Core
- 類型：Principle
- 核心內容：MLflow 2 時代只要欄位對得上就自動跑一批 judge；MLflow 3 強制顯性指定 Correctness() / Safety() / Guidelines() / RetrievalGroundedness() 等 scorer。這背後是哲學轉變：評估標準不再是黑箱預設，而是團隊責任；scorer 與 judge 變成可治理資產，而非 evaluator_config 的副作用。對有治理要求的資料團隊，這種顯性化反而提升信任。
- 保留理由：把「顯性化」視為治理升級的具體做法，可遷移到其他評估 / 監控場景
- 待補強處：對 onboarding 友善度的衝擊、預設 scorer 模板的最佳實務、scorer 演進的 backward compatibility
- 初步知識鉤子：[[顯性化是治理的基礎]]、Configuration as Code、[[scorer 作為團隊資產]]

序號 3
- 候選標題：Trace + Scorer + Labeling + Dataset 是同一個閉環（不該分開想）
- 分級：Core
- 類型：Pattern
- 核心內容：MLflow 3 把 evaluation 結果存成 trace + assessment，意味著 production trace 和 eval trace 共用資料模型，同一組 scorer 可同時跑離線 golden set 與線上抽樣。Production 發現的 bad case 可直接變 golden case（觀察 → 標記 → 寫回 dataset → regression test）。這個閉環讓 agent 品質呈複利成長，每個使用者 bug 都在訓練系統。
- 保留理由：把 evaluation 與 observability 合流的趨勢說清楚，且帶具體 loop
- 待補強處：抽樣策略、trace 儲存成本、跨團隊共用 dataset 的權限模型
- 初步知識鉤子：[[Evaluation 與 Observability 合流]]、CI/CD × Production Monitoring、[[DecisionOps]]

序號 4
- 候選標題：Production Traces / Human Labeling / Golden Dataset = Bronze / Silver / Gold（Medallion 思維遷移到 agent eval）
- 分級：Core
- 類型：Pattern
- 核心內容：用 Medallion 架構類比 agent eval 資料層次：production traces 是 Bronze（原始且大量）、human labeling 是 Silver（清洗過、有判斷）、curated golden dataset 是 Gold（高信任、可重複測試）。過去這三層是三套工具三種格式，現在 trace-based 資料模型讓它們在同一條 pipeline 流動。這個類比對熟悉 lakehouse 的工程師遷移認知極有效。
- 保留理由：跨領域類比，從資料工程遷移到 agent eval，遷移性極高
- 待補強處：Bronze → Silver → Gold 的具體升級規則與 SLA、各層的 schema 設計
- 初步知識鉤子：[[Medallion Architecture]]、Data Engineering 思維遷移到 AI Eval、[[Lakehouse for AI]]

序號 5
- 候選標題：Span-level Debug 是 agent 工程的分水嶺（不是看 trace 就好）
- 分級：Core
- 類型：Heuristic
- 核心內容：agent 出錯時，先看 retrieval span 抓到什麼 context（context 錯，prompt 再好也沒用）；再看 SQL 生成 span 產出什麼 query（SQL 錯，generation 才是要修的點）；最後看最終 LLM 拿到什麼輸入（輸入對輸出錯，才是 prompt 或模型問題）。這個習慣能把 debug 時間從一下午壓到十分鐘，因為知道該修哪一層。直接對應 PySpark 的 stage / task 拆解思維。
- 保留理由：高度可執行的工作習慣卡，對日常 agent debug 立即有用
- 待補強處：自動化 span-level 異常檢測規則、span 命名與 schema 一致性
- 初步知識鉤子：[[分層 debug 思維]]、PySpark stage debug、Distributed Tracing、[[Harness × Observability]]

序號 6
- 候選標題：Binary pass/fail 比 1-5 評分穩定（先及格線、後分等級）
- 分級：Support
- 類型：Heuristic
- 核心內容：LLM judge 用 1-5 分時分數飄移嚴重，同一答案今天 3 分明天 4 分；改成 binary 「可接受嗎？yes/no」反而穩定。最佳實務是先用 binary 建立及格線，等團隊對「什麼叫可接受」有共識後再細分 excellent / acceptable / poor。這個原則和帶團隊訂規範一樣——新規範先訂能不能過，不要一開始就訂 ABCD。
- 保留理由：罕見但重要的設計 heuristic，可遷移到其他人類 / AI 評估場景
- 待補強處：何時可從 binary 升級到多級、「可接受」標準的 calibration 方法
- 初步知識鉤子：[[評估設計 heuristic]]、Likert scale 限制、漸進式標準化

序號 7
- 候選標題：Eval-first 開發流程（先寫 golden case → 寫 scorer → 才動手實作）
- 分級：Support
- 類型：Heuristic
- 核心內容：傳統「寫 code → 看結果 → 覺得 OK 就交」要逆轉成：先寫 10-20 筆 golden case → 寫 scorer 定義「可接受」→ 才實作 agent → 每次改動都跑 eval。先寫 eval 會逼你想清楚「這個 agent 到底要達到什麼」，這個問題在只寫 prompt 的流程裡經常被跳過。對應 TDD 思維但放在 agent 場景。
- 保留理由：可立即套用的工作流程改變，與 TDD 的類比有遷移性
- 待補強處：早期不確定情境下 golden case 的界定、eval 與探索性開發的取捨
- 初步知識鉤子：TDD vs Eval-Driven Development、[[先寫驗收條件再寫程式]]

## C. 建議送 refine 的項目
- 序號 1（評估能力 = 真正瓶頸）：Core，主線投資判準
- 序號 2（顯性 scorer 取代自動 judge）：Core，治理升級的具體做法
- 序號 3（Trace + Scorer + Labeling + Dataset 閉環）：Core，與 4 相關但角度不同
- 序號 4（Medallion 類比 agent eval）：Core，跨領域遷移性高
- 序號 5（Span-level debug 分水嶺）：Core，立即可用工作習慣
- 序號 6（Binary pass/fail）：可保留為設計 heuristic
- 序號 7（Eval-first 流程）：可保留為流程 heuristic

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉
