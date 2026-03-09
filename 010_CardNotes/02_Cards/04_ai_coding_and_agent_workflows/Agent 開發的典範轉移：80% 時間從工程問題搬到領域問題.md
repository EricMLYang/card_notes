# 3-Agent 開發的典範轉移：80% 時間從工程問題搬到領域問題

**類型**：Leverage

## 概念

作者經歷 GPTs → Semantic Kernel → Google ADK/A2A → Coding Agent SDK 的完整路徑後，最大感想是：用 Coding Agent + SKILLs + MCP 做法後，80% 時間花在評估「該準備什麼 SKILL」和「該配什麼 Tools/MCP」——這些都是領域問題，不是工程問題。工作流程變成：先用 Coding Agent 當通用 Agent 寫 SKILL/MCP 驗證 MVP → 確認可行後用 SDK 整合到既有服務。SDK 只負責「把功能整併」，工程量極小。核心呼應 Anthropic 理念：Don't Build Agents, Build Skills Instead。軟體開發的分析/設計/驗證/部署典範全部翻轉。

## 重要性

對系統建造者的關鍵提醒——如果你還在花大量時間寫 Agent 的工程 code，你可能正在用舊範式解決新問題。

## 邊界/反例

前提是通用 Coding Agent 的能力已經夠強；對於需要極致延遲或特殊安全要求的場景，仍可能需要手刻 Agent 核心。

## 標籤

#Agent開發 #SKILL #MCP #典範轉移 #領域問題
