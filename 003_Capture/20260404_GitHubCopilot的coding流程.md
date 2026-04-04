GitHub Copilot 公開了他們的 AI Coding 流程

幾個他們踩出來的原則：

1. 先 /plan 再動手
不要直接叫 agent 寫 code
先用 planning mode 對齊方向

2. 重構和文件比寫新功能重要
乾淨的架構和完整的文件
是 agent 能不能有效工作的前提

3. 出錯時怪流程不怪 agent
agent 寫出爛 code 代表你的 linting、
typing、測試不夠嚴格

5 個人、不到 3 天
就產出 11 個 agent、4 個 skill
改了 345 個檔案、+28,858 行 code

他們的開發循環：
plan → autopilot → agent code review → 人工 review
每週再跑一次自動化檢查
抓測試缺漏、重複 code、文件落差

結論很直白：
讓 agent 寫好 code 的能力
跟讓人寫好 code 的能力相同
都是架構、文件、測試、設計
沒有捷徑