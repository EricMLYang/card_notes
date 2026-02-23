# 4-Multi-Repo AI Agent 架構

**類型**：Model

## 概念
Multi-repo Agent 架構的核心不是拆 repo，而是拆責任邊界：能力模組、執行流程、環境配置、知識資產各自獨立版本化。這能降低 context 汙染、縮小變更半徑，讓不同 Agent 在明確契約下協作。

## 重要性
它決定 Agent 系統能否從單次 demo 走向可維護產品。

## 邊界/反例
團隊規模小、問題單純時，過早多 repo 會增加協作成本。若沒有明確 interface 契約，多 repo 只會把混亂分散到更多地方。

## 知識鉤子
可與 `#Repo-as-Worker` 連成可維護代理工作流，並對接 `#MCP 工具治理` 的權限與版本策略。

## 標籤
#MultiRepo #Agent架構 #模組化 #版本治理 #Context管理
