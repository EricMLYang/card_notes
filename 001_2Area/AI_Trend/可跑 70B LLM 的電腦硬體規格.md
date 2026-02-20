# 可跑 70B LLM 的電腦硬體規格

- Reference: <https://ihower.tw/blog/>



- 主要應用: Inference

- 本地跑 LLM，關鍵就是 GPU RAM 要夠，而且記憶體頻寬速度要夠快。

- 2025年中研究: 個人用的 AI 工作站電腦，在「128 GB RAM + 2TB SSD」的條件下來選

- AMD 的 Ryzen AI Max+395 跑推論好像也很猛，就去找有哪幾家有組裝

   - Framework Desktop

   - GMKtec EVO-X2

   - Bosgame M5 AI

- gpt-oss-20b (GGUF) 超快，可以跑到 60 tok/sec

- gpt-oss-120b 速度則是 30 tok/sec 也很快!!

Context Length 方面，gpt-oss 模型的上限是 131k。但我這個家用硬體，當然是沒辦法開到滿。目前測試到 12k 是沒問題的，需要再進一步研究設定 (還沒開 Flash Attention)。

作為對比，相比我筆電 MacBook Pro M2 Pro (32g)

- gpt-oss-20b (MLX) 也是可以跑 50 tok/sec

- gpt-oss-120b 跑不起來，ram 不夠 

我也嘗試了其他模型例如 Gemma 3 和 Mistral Small 等，但速度都沒有 gpt-oss 來得快，只有 15tok/sec 左右。而 Qwen3 30B 在 LM Studio 裝好就可以跑到 70 tok/sec 超快。要弄好模型 Inference 又是一門大學問了，很多設定在這邊。

## 比較資訊

- **性價比冠軍**: AMD Ryzen AI Max+395: 價格才 USD 2k; 記憶體頻寬 273 GB/s; x86 + Windows; 70B 模型推論 + 玩遊戲都 OK

- **生態優勢**: NVIDIA DGX Spark: 要 USD 4k; 記憶體頻寬也是只有 273 GB/s; ARM + CUDA，適合模型訓練/微調，若只跑推論感覺 C/P 值不如 AMD 啊

- **頻寬極速**: Mac Studio M4 Max: 最貴 USD 4.5k; 546 GB/s 跑推論最快; macOS 生態

- [Mac Studio](https://www.apple.com/tw/mac-studio/) 是很多人推薦的選擇，但是我覺得組 128GB + 2T 硬碟的話，價格太貴了(六位數台幣約14W)

- 2025 年初發表的 [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)，我對這台也很感興趣，後來發現這台有幾個問題:

   - 這台是 ARM 機器是跑 Linux，定位就是機器學習工作站，拿來在 Nvidia CUDA 體系下做機器學習訓練

   - 記憶體頻寬只有 273GB/s，跑推論應該會比 Mac Studio 慢，沒優勢

   - 價格也不便宜，要台幣6位數，而且其實網上你還買不到


