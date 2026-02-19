---
tags:
  - llm-application
---
# LLM Model Knowledge - GPU Specification

- 估算 LLM 記憶體需求的經驗法則：

   - 載入具有 X 十億個參數的模型，以 32 位元浮點精度 (FP32) 載入，大約需要 4X GB 的記憶體。  

   - 載入具有 X 十億個參數的模型，以 16 位元浮點精度 (FP16) 或 bfloat16 載入，大約需要 2X GB 的記憶體。  

   - 微調 LLM 的記憶體需求通常比推論高 3-4 倍。  

- GPU important Specification

   - VRAM (GB)

   - FP32 算力 (TFLOPS - Tera Floating-point Operations Per Second)

   - 記憶體頻寬 (GB/s): GPU 每秒可以從記憶體中讀取或寫入的數據量

- 量化是一種將模型參數從高精度 (例如 FP32) 轉換為低精度 (例如 INT8 或 INT4) 的技術



## **GPU 之間的連接**

GPU 之間的 **通訊頻寬與延遲** 會嚴重影響多 GPU 配置的效能，主要有以下幾種連接方式：

#### **(a) NVLink**

- NVIDIA 專屬技術，可用於 **高效能 AI 計算與 LLM 訓練**。

- **最新 NVLink 4.0**（H100 使用）有高達 **900GB/s** 的 GPU 互連頻寬，比 PCIe 高出許多。

- 適用於 **H100, A100, RTX 6000 Ada** 等專業級 GPU，不適用於 RTX 4090、4080 等消費級顯卡。

#### **(b) PCIe 介面**

- **PCIe 4.0 vs PCIe 5.0**：

   - PCIe 4.0：**64GB/s（雙向）**

   - PCIe 5.0：**128GB/s（雙向）**（更快，但仍遠低於 NVLink）

- 如果 **GPU 之間的通訊頻寬需求高**（例如大規模 LLM 訓練），NVLink 比 PCIe 更佳。

- **PCIe Lanes（通道數）** 也影響效能：如 **雙 GPU 可能會共享 x8 lanes**，而不是完整的 **x16 lanes**，導致通訊變慢。

[Liger Kernel](https://github.com/linkedin/Liger-Kernel) 是套開放原始碼的 Triton 核心程式框架，專為大型語言模型的訓練設計，藉由核心操作的融合 (operation fusing) 與輸入分塊 (input chunking) 等效能改善機制，Liger Kernel 得以提升約 20% 的訓練吞吐量，並減少約 60% 的 GPU 記憶體使用量




