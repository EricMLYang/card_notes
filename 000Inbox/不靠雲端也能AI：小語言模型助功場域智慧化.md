---
tags:
  - edge-ai
---
# 不靠雲端也能AI：小語言模型助功場域智慧化

- 雲端、終端是我們目前技術造成的限制

- NPU 可以把模型包的比較小

- 2022 才是生成式 AI 的拐點

- CNN 是局部化的辨識機率再拼湊的，比較難看整體

- Transform 更能看連續的全局

- 目前自駕還是 CNN base，所以容易撞到大片卡車…等

- 作者心中認為 GPT 不是 AI 的主流，太耗電？

- 2037 年端 AI 會很快速的增長

- 小語言模型約在 10B 以下

- GPU 很難做到省電

- 莫爾定律爭論：

   - 系統層面來講，的確無法應付算力增長，是靠 CoWars 3D技術達到

   - 用 NPU 來看，莫爾定律沒變

- 1年內可能每一家的 LLM 差異化都不大，會專注在 inference 

- 2、3年前大廠都開始講 NPU

- 









- 模型的範疇還會變嗎？變的化 NPU需要做大調整嗎？



## 問題

- 端側代理 (On-Device Agent)

- Edge LLM 的甜蜜點是以 7B左右的模型當標準

- 「NPU ≥ 30 TOPS / ≤ 5 W」成為端側 LLM 甜蜜點；雲端 GPU 價格 12 個月內上漲 \~14 %，推動終端自給自足 

   - NPU性能甜蜜點

      - 「NPU ≥ 30 TOPS / ≤ 5W」 指的是：

      - TOPS：每秒萬億次運算（Tera Operations Per Second），衡量AI運算能力

      - ≥ 30 TOPS：AI運算能力要達到每秒30萬億次以上

      - ≤ 5W：功耗控制在5瓦以下

- 為什麼是30 TOPS？因為這個算力大概能：

   - 流暢運行7B參數的量化LLM

   - 支持實時多模態推理

   - 滿足大部分日常AI應用需求

- 為什麼是5W？因為：

   - 手機、筆電等移動設備的功耗限制

   - 散熱和電池續航的考量

   - 成本控制的需要







目前（截至 2025 年中）在 7B 左右的模型中，Google 的 Gemma 確實是非常優秀的一員，



🔝 現役 7B 級 LLM 比較（截至 2025）



- Gemma 7B	Google DeepMind	7B	高品質資料 + RLHF + 多語	Apache 2.0	泛用性強、效能優秀、合規性高

- LLaMA 3 8B	Meta	8B	高品質 pretraining + 大語料	自由授權（需註冊）	強推理能力、社群活躍

- Mistral 7B	Mistral AI	7B	Dense Transformer 訓練	Apache 2.0	執行速度快、推理效能優異

- Phi-3 mini (3.8B)	Microsoft	3.8B	微型大腦、訓練資料高品質	MIT	體積小、效能優於常規 7B 模型

- Qwen 7B	阿里巴巴	7B	中文能力強，泛用性佳	開源商用授權	中文表現好、RAG 整合方便




