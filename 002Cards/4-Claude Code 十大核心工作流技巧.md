# 4-Claude Code 十大核心工作流技巧

**類型**：Model

## 概念

Boris 分享的 Claude Code 高效工作系統：(1) **平行處理**：3-5 個 git worktrees 同時跑功能、bug、重構、分析；(2) **計畫模式優先**：複雜任務先寫計畫，用另一個 Claude 審查漏洞；(3) **CLAUDE.md 累積經驗**：每次糾正後要求 Claude 更新自己規則，讓錯誤不再重複；(4) **高頻工作封裝成 skill/command**：如 /techdebt 清理、上下文彙整指令；(5) **讓 Claude 自己修 bug**：只說「修」，讓它自己讀上下文找重現步驟；(6) **用 Claude 當 reviewer**：要求嚴格審查、證明正確性、砍掉重練；(7) **語音輸入加速**：說比打字快且完整；(8) **Subagent 分工**：把掃描、整理、列清單交給 subagent，主 agent 保持精簡；(9) **資料分析整合**：bq CLI + BigQuery skill commit 到 codebase；(10) **學習模式**：啟用 Explanatory 輸出，把「改好了」變成「知道為什麼」。

## 重要性

這是把 Claude Code 從聊天工具變成系統的完整框架——定義了「一天做超過一次就封裝」的標準。

## 邊界/反例

這套系統需要一定上手成本，小專案可能過度複雜。平行任務太多時上下文切換仍有成本。

## 標籤

#ClaudeCode #AI工作流 #平行開發 #計畫模式 #開發效率
