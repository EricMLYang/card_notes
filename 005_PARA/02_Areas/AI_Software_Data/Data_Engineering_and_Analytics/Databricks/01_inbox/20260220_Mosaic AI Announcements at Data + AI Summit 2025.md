---
tags:
  - databricks
  - llm-application
---
# Mosaic AI Announcements at Data + AI Summit 2025

<https://www.databricks.com/blog/mosaic-ai-announcements-data-ai-summit-2025?hl=en-US>

這篇 **Databricks Data + AI Summit 2025 的 Mosaic AI 新功能公告**，可以歸納成幾個重點方向：



---

### **1\. Agent Bricks（Beta）**

- 只要描述任務 + 連結企業資料，就能自動生成高品質 Agent。

- 支援 **資訊抽取、知識助理、文字轉換、多 Agent 系統**。

- 自動建立測試與優化成本/品質。



---

### **2\. MLflow 3.0（為 GenAI 重構）**

- 新版專為 **生成式 AI 與 Agent 管理**打造。

- **跨平台監控**：能觀測部署在 AWS、GCP、On-Prem 的 Agent。

- **Prompt Registry**：註冊、版本化、測試與部署 LLM Prompt。





---

### **3\. AI Functions in SQL（更快且支援多模態）**

- 效能提升：**速度提升 3 倍，成本降 4 倍**。

- 新增 **文件解析（ai_parse_document）**，從複雜文件中萃取結構化資訊。

- 支援 **跨文字、圖片等多模態數據**。





---





### **4\. Storage-Optimized Vector Search（Public Preview）**

- 架構重寫：**計算與儲存分離**。

- 成本降低 **7 倍**，可支援數十億向量。

- 更適合 **RAG 應用、語義搜尋、文件探索**。





---





### **5\. Serverless GPU Compute（Beta）**

- Databricks Serverless 平台新增 GPU。

- 不需管理基礎設施即可使用 GPU 做 **訓練 / 推理 / 大規模轉換**。

- 支援 **A10g (Beta)**，即將支援 **H100**。





---





### **6\. High-Scale Model Serving**

- 模型服務效能提升：可支援 **25 萬 QPS**。

- 新自研推理引擎，Meta Llama 等模型推理可快 **1\.5 倍**。

- 讓 LLM 部署更快、更便宜、更易於維運。





---





### **7\. MCP Support in Databricks**

- 內建 **Anthropic Model Context Protocol (MCP)** 支援。

- 可在 Databricks App 裡快速部署 **MCP Server**，並在 Playground 測試。

- 已支援 UC Functions、Genie、Vector Search。





---





### **8\. AI Gateway（正式 GA）**

- **AI 服務統一入口**，提供治理、使用監控、安全控制。

- 功能包含 **多供應商自動 fallback、PII 安全防護、Rate Limit 政策**。

- 支援 Databricks 內外部 AI 服務。





---



👉 總結來說，這些更新的方向是：



- **建 Agent 更簡單**（Agent Bricks, MLflow 3.0）

- **AI 效能更快更便宜**（AI Functions, Vector Search, Serverless GPU, Model Serving）

- **跨平台治理與安全更完整**（MLflow observability, AI Gateway, MCP support）

# BreadCards

## A. 主脈絡與個人映射
- **論證骨架**：Databricks Data + AI Summit 2025 的 Mosaic AI 公告整理，列出 8 個產品方向（Agent Bricks / MLflow 3 / AI Functions in SQL / Storage-Optimized Vector Search / Serverless GPU / High-Scale Model Serving / MCP Support / AI Gateway），每項 2-3 行 bullet，最後總結為三條方向（建 agent 更簡單 / 更快更便宜 / 跨平台治理）。
- **挑戰的預設**：未挑戰任何主流預設，整篇是 feature list 摘要。
- **個人映射**：所列方向（MLflow 3、AI Gateway、MCP 支援、ai_parse_document、Vector Search 成本下降）已被其他高訊號文章（MLflow 3 Migration、SiliconAngle、Lakebase）以更具機制與取捨的方式覆蓋。本文作為「事件型新聞」存在，沒有提供取捨、機制、設計理由或失敗模式。

## B. 候選卡（Lite）

**判定：0 卡**

理由（命中多個 blacklist）：
1. **❌ 純產品發表（feature list）**：8 個項目都是 capability claim（「快 3 倍、便宜 4 倍、降 7 倍」「支援 25 萬 QPS」），沒有對比基準、測試條件、適用情境。
2. **❌ 純平台宣傳**：完全圍繞「Databricks 又推出什麼」，沒有回到資料、語意、workflow、商業影響的分析。
3. **❌ 純事件報導**：summit 公告整理，未附帶結構性分析。
4. **❌ 無支撐的結論**：「3x 快、4x 便宜、7x 成本下降」這類數字無 benchmark 條件，無法形成判斷。
5. **❌ 中庸論述**：總結「建 agent 更簡單、更快更便宜、治理更完整」是樣板話，無取捨。

同主題的高訊號內容（MLflow 3 控制平面整合、MCP × Unity Catalog 治理邊界、ai_parse_document 的治理意義）已被本批次其他文章以具體機制覆蓋，本文無增量價值。

## C. 建議送 refine 的項目
- 無

## D. 呼叫 refine-cards
- 不呼叫，0 卡





---