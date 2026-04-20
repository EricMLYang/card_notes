# AI Agent Guardrails：把 guardrail 當成執行邏輯，而不是事後補丁

> 來源：Arthur AI Blog
> 來源類型：高密度觀點
> 需求層：知識建構
> 發布日期：2026-04-06
> 連結：https://www.arthur.ai/blog/best-practices-for-building-agents-guardrails
> 搜集日期：2026-04-20
> 搜集原因：對應你關注的 AI Agent 工程化、verification、guardrails、memory 與 production reliability；這篇不是空泛談安全，而是把 guardrail 放回 agent loop 的執行設計。

## 摘要
這篇文章把 agent guardrails 拆成兩層：pre-LLM 與 post-LLM。前者處理 PII、敏感資料與 prompt injection，後者處理 hallucination、toxicity、tool/action validation 與 output format。更重要的是，它主張 guardrail 不該只做 blocking，而應該成為 feedback loop 的一部分，讓 agent 在單次執行內自我修正，而不是把錯誤留到事後監控才發現。這很貼近你在意的「如何把 agent 從 demo 推到可上線系統」。

## 為什麼值得看
這篇最有價值的地方，不是列一堆安全名詞，而是把 guardrail 提升成 runtime architecture。對你來說，重點不是「要不要加 guardrail」，而是「哪些 guardrail 必須在 hot path、哪些可以用模型判斷、怎麼把失敗變成 retry 與 correction」。它也呼應你常寫的判準：真正有價值的 agent，不是模型更強，而是 loop、tool use、verification 與 observability 被設計進去。

## 可能偏誤或限制
Arthur AI 本身賣 observability / eval / guardrail 產品，因此會自然強調 guardrail 作為核心控制面。文中案例有實戰感，但仍以供應商敘事為主，沒有提供完整失敗率、成本曲線或和其他架構的量化比較。對於小團隊來說，文中最佳實踐需要再轉譯成較輕量的落地版本。

## 潛在卡片方向
- guardrail 不是 filter，而是 agent execution loop 的一部分
- pre-LLM 與 post-LLM 是兩種不同責任邊界，不應混成同一個「安全層」
- post-LLM guardrail 的高槓桿用法，是把失敗訊號餵回 agent 做 self-correction
- guardrail 事件要進 telemetry，否則只是看似安心的黑盒子

---

## 重點譯摘
- guardrail 的關鍵不是「擋掉錯誤」，而是把錯誤攔在使用者看見之前。
- pre-LLM guardrail 適合做快速、確定性高的檢查，例如 PII、敏感資料與 injection。
- post-LLM guardrail 適合檢查模型輸出是否被 context 支撐、是否選對 tool、是否符合格式。
- 真正高槓桿的模式是：guardrail 發現問題後，不是直接失敗，而是把問題描述回饋給 agent 重新生成，直到通過或達到重試上限。
- 如果 guardrail 沒有被記錄進 tracing / telemetry，你很難知道它何時常常被觸發，甚至無法分辨系統是不是正在退化。

