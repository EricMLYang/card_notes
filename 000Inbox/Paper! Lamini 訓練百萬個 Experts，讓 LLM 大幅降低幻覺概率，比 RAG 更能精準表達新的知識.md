---
tags:
  - llm-application
---
# Paper: Lamini 訓練百萬個 Experts，讓 LLM 大幅降低幻覺概率，比 RAG 更能精準表達新的知識



- Introducing Lamini Memory Tuning: 95% LLM Accuracy, 10x Fewer

- ++<https://www.lamini.ai/blog/lamini-memory-tunin>++g

- Lamini 挑戰了現在常見的兩個讓 LLM 回答新知識的主流方法，RAG 與 finetuning

- Lamini 先說明了 RAG的缺陷，RAG ​ 雖然可以讓 LLM 隨時閱讀最新資訊，但 LLM 其實無法「原封不動輸出 Retrieve 到的內容」，因為「閱讀的內容」可能「知識、格式、語言」跟 LLM 的偏好不一致，所以就會出現「Hallucination（幻覺）」，LLM 可能融合了自己的知識、自己的語言偏好，來重新敘述參考文件

- Lamini 提出的是我們用 百萬個 Lora，以 Mixture of Expert 的形式來學習，每個 Lora 用來記憶某一筆知識（Train with 30+ epochs），當需要回答這筆知識的時候，我們再選出這個 Lora

- 意思是每個 instruction tuning data 進來，我們就以 cross attention 的方式來挑選其中 32 個 experts 來學習這個知識，固定 LLM 的 weight 讓我們不會忘掉通用能力，而每個 expert 是就是一個 tunable 的 Lora（這部分論文沒有足夠細節判斷具體作法，小編用自己的判斷來理解），並且一樣加入 Load Balance loss，學到我們 loss 足夠低，可以記憶起整筆資料為止

- 藉由Lamini這個方法，他們在多種需要「精準輸出」的場域上都得到了明顯的提升，像是 text to SQL，如果SQL的語法跟他們DB不合，就會失敗，所以需要精準輸出。或是產品推薦，需要精準輸出產品的ID

- 其實這個方法算很聰明，LLM經過訓練可以記憶起任意一筆資料這件事其實大家都知道，原先大眾把這當作缺點，因為記憶（Memorize）通常是通用（General）的捷徑，意思是如果模型都在記憶，反而不會學到新知識，而 Lamini 找到了「需要精準記憶」的使用場景，像是 text to SQL 或是生成產品ID，並用 MoE + Lora 的形式來達成有效的記憶但不劇烈破壞模型通用能力，其實也有點 Model merging 的味道