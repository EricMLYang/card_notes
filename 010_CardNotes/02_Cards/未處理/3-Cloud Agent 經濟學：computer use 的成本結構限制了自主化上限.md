# 3-Cloud Agent 經濟學：computer use 的成本結構限制了自主化上限

**類型**：Warning

## 概念

Cursor Cloud Agent 實測揭露 computer use 模式的成本現實：30 分鐘桌面操作 = 2000 萬 token ≈ $10。Cloud Agent 的價值在於把本地開發環境搬到雲端（自動探索 repo、建置環境、snapshot、發 PR），但 computer use 的 token 消耗遠高於純 CLI Agent。Stripe 模式（Slack → devbox → goose CLI → PR）繞過了 computer use，成本更低但需要更多基礎設施投資。選擇 CLI Agent 還是 Computer Use Agent，本質是「前期基礎設施投資」vs「每次任務的邊際成本」的取捨。

## 重要性

在選擇 Agent 部署模式時，需要區分 CLI-native 路線（低邊際成本、高前期投入）與 computer use 路線（低前期投入、高邊際成本）。

## 邊界/反例

內網環境、資安控管場景下 Cloud Agent 難以部署。模型進步可能快速壓低 computer use 成本，這個取捨會隨時間改變。

## 標籤

#CloudAgent #ComputerUse #成本結構 #Agent部署 #CLI
