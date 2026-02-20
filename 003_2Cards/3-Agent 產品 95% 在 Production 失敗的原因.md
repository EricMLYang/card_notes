# 3-Agent 產品 95% 在 Production 失敗的原因

**類型**：Warning

## 概念

大多數 AI Agent 進到正式環境會失敗，問題不在模型不夠聰明，而在於周邊的工程架構：context 管理、memory 設計、錯誤處理、agent prompt 最佳化、語意檢索、評估回饋機制。「大多數創辦人以為自己在做 AI 產品，其實是在做 context selection 系統。」Context Engineering 不等於 Prompt 技巧——RAG 做得好就夠用，但多數 RAG 系統太天真（索引太多讓模型混亂，太少又缺乏訊號）。

## 重要性

這是 Agent 產品開發的核心認知——避免把精力放在「換模型」而忽略系統工程。

## 邊界/反例

在簡單、低風險的場景（如個人助理、內部工具），可以容忍較高的失敗率。但面向客戶的產品、涉及金錢或合規的場景，95% 失敗率是致命的。成功的 5% agent 都有人機協作設計，讓 AI 當助手而非自主決策者。

## 標籤

#Agent開發 #Context工程 #Production失敗 #系統工程 #RAG
