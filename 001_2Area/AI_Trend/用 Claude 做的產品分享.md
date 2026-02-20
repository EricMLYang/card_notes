用 Claude 做的產品分享

<https://www.facebook.com/share/1TkZihVd6b/>

在 Anthropic 開發者活動的錄影中，還有好幾場是客戶公司來展示他們用 Claude 做的產品，包括:

- Canva: 推出 Canva Code，讓非技術用戶也能建立互動式網頁原型

- Databricks: 整合 Claude 到他們的資料平台，用於處理企業級 AI 應用的治理和評估問題

- Manus AI: 建立通用 AI Agent，可以在雲端虛擬機器中執行長時間任務（如找辦公室、規劃行程）

- Shopify: 下述

- Tempo Labs: 打造「給 PM 和設計師用的 Cursor」，讓非工程師也能協作寫程式碼

- Zencoder: 推出 ZAN agents，支援 MCP 的自訂 Agent，可部署在整個軟體開發生命週期

- Gamma: 用 Claude 生成簡報和文件

- Biddo: AI 程式碼審查平台

- Refusion: 音樂生成平台，用 Claude 的 Ghost Writer 幫助創作歌詞

- Create: AI Text-to-App 建構器，讓任何人都能用自然語言建立行動應用程式

- Stanford 學生用 Claude 建立核武偵測模擬系統

- UC Berkeley 學生 7 個月從零學會寫程式，建立多個實用工具
   但最讓我感興趣的是 Shopify 首席工程師 Obie Fernandez 的分享，這場我認為比較特別是在講內部工程工具，不是講產品。
   Shopify 是全球最大的 Ruby on Rails 應用，開發近 20 年，有數百萬行程式碼。在這種規模下，他們怎麼善用 AI 提升開發效率?
   他們的關鍵洞察是: 確定性 vs 非確定性工作流程的結合，他認為 AI 工具有兩種截然不同的使用方式:

1. Agentic 工具 (如 Claude Code): 適合探索性、模糊的任務，需要適應性決策和迭代

2. 結構化工作流程: 適合有明確步驟、需要一致性和可重複性的任務
   他們發現，像花生醬配巧克力一樣，可以將這兩種方式結合起來。他們除了大量使用 Claude Code，同時也開發了 Roast <https://github.com/Shopify/roast> 一套用 Ruby 寫的結構化 AI 工作流程框架。
   實際應用案例:

- 自動化測試生成和優化

- 程式碼遷移 

- 類型檢查改進
   最巧妙的是可以雙向整合:

- 可以在 Claude Code 中呼叫 Roast 工作流程

- 也可以在 Roast 工作流程中呼叫 Claude Code SDK
   實務好處:

- 可以快取 function 呼叫結果，不用每次重跑

- 可以從特定步驟重新開始，不用從頭跑