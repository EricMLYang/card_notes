# 4-AI Coding 的骨架策略：用 Interface + Test 鎖住頭尾，中間放給 Agent 跑

**類型**：Heuristic

## 概念

AI Coding 的核心挑戰是需求不清和品質不可控。解法：(1) 用 code 定義規格（Interface）；(2) 用 code 定義驗收條件（Test）；(3) 這兩層親自逐行 review 並保護起來（不讓 AI 改）；(4) 中間的實作全交給 Agent 跑到通過為止。直接 Review Interface + Test（代表你的設計意圖和品味），間接 Review 靠編譯器和測試自動驗證其餘 code。骨架打好了，肉再長也歪不到哪裡去。Unit Test 還兼任 AI 的 Sample Code——告訴 AI 你期待怎麼使用它，比文件更精準。Code 修改也比 Docs 容易（重構工具 + 測試保護），在設計未定案階段尤其有優勢。

## 重要性

這是目前最實用的 AI Coding 品質控制方法——用最少的人工投入（Interface + Test）獲得最大的品質保證。

## 邊界/反例

前提是開發者有足夠的抽象化能力來定義好 Interface；對於 UI/UX 密集型或探索性原型開發，Interface 定義成本可能過高。

## 標籤

#Interface #Test #骨架策略 #AICoding #品質控制
