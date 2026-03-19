---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-20
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---

# Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl

> 來源：Martin Fowler Blog
> 連結：https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
> 搜集日期：2026-03-16
> 搜集原因：AI Coding Agent 工程實踐（SDD 規格驅動開發）

## 摘要

Martin Fowler 的文章比較三種 Spec-Driven Development（SDD）工具的設計哲學與實作層次。核心發現是：SDD 目前缺乏統一定義，工具成熟度差距極大。文章也提出批判性觀點，警告 SDD 可能重蹈 Model-Driven Development（MDD）失敗的覆轍。

## 關鍵段落

**三種 SDD 成熟度層級：**
> "Spec-first（規格先於代碼，完成後丟棄）→ Spec-anchored（規格持續維護貫穿功能演化）→ Spec-as-source（規格為主要製品，人類只編輯規格，不碰生成的代碼）"

目前 Kiro、spec-kit 都只實踐 spec-first；只有 Tessl 嘗試 spec-as-source。

**工具規模不匹配問題：**
> "嘗試用 Kiro 修復小 bug，結果被轉化為四個 user story 和十六個驗收標準。spec-kit 對中等功能同樣過度冗長，製造審查疲勞而沒有等比的價值。"

**歷史警告：**
> "Model-Driven Development（MDD）在過去數十年嘗試類似的規格到代碼自動化，最終因不靈活和高開銷失敗。Spec-as-source 的風險在於結合 MDD 的限制與 LLM 的不確定性——以一個問題換另一個問題。"

## 潛在卡片方向

- SDD 三層成熟度模型：spec-first / spec-anchored / spec-as-source（清楚定義邊界）
- SDD 工具選擇的反直覺建議：工具複雜度應與問題規模匹配，不要用大型框架做小任務
- AI 工程歷史類比：MDD 失敗的警示如何應用到 SDD 設計決策
- 與現有卡片連結：[[規格作為 AI 的控制介面]]、[[Coding Agent 20x vs 5x 差距]]

---
*由 scout-news 自動搜集，待 process-inbox 處理*
