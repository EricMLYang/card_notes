---
tags:
  - ai-application
  - evaluation
---
# AI Error Analysis：LLM 應用評估方法

## 類型
AI 應用方法論

## 概念
來自 Hamel + Shreya 的 AI Evals 課程。LLM 評估核心是「分析→測量→改進」三步驟循環。關鍵在第一步：錯誤分析 (Error Analysis)。方法：(1) 建立 100 個跨維度的測試輸入；(2) 逐一檢視，記錄失敗模式（約花 80% 時間）；(3) 讓類別自然浮現，不做根本原因分析，只關注觀察到的行為模式。不同於 G-Eval 正面評分法，此法用負面表列針對每種失敗模式做量測和改進。

## 重要性
LLM 輸出難以用傳統指標衡量，此方法提供系統化改進流程。

## 邊界
需要約 1 小時完成 100 個樣本分析；對持續對話場景仍有挑戰。

## 標籤
#ai-application #evaluation #llm #error-analysis
