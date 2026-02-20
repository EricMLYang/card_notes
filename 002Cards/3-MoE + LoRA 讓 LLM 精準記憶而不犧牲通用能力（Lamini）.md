# 3-MoE + LoRA 讓 LLM 精準記憶而不犧牲通用能力（Lamini）

**類型**：Model

## 概念

Lamini 挑戰 RAG 和 Fine-tuning 的缺陷：RAG 雖然讓 LLM 閱讀最新資訊，但**LLM 無法「原封不動輸出 Retrieve 到的內容」**——因為閱讀內容的知識、格式、語言可能與 LLM 偏好不一致，導致「幻覺」（融合自己的知識和語言偏好重新敘述）。Lamini 的解法：用**百萬個 LoRA 以 Mixture of Expert 形式學習**，每個 LoRA 記憶一筆知識（Train 30+ epochs），需要回答時選出對應 LoRA。關鍵設計：固定 LLM weight 保留通用能力，每筆 instruction tuning data 用 cross attention 選 32 個 experts 學習，加入 Load Balance loss 直到能精準記憶。適用場景：text-to-SQL（語法必須精準）、產品推薦（精確輸出產品 ID）。

## 重要性

這是判斷「何時用 RAG vs Fine-tuning vs Lamini」的框架——需要精準輸出時，記憶比理解更重要。

## 邊界/反例

通用對話場景不需要精準記憶；百萬 LoRA 的部署成本高；知識更新頻繁的場景 RAG 仍較適合。

## 標籤

#Lamini #MoE #LoRA #RAG #精準記憶 #幻覺
