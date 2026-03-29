---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-29
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
這幾天 Claude Code 社群最紅的東西大概就是 gstack 了
Y Combinator CEO Garry Tan 開源的 Claude Code skill 包
48 小時破萬星，現在已經 4 萬多了

今天就來聊聊好了，我也用了一陣子有一些心得
剛被燒到的時候有用了幾個裡面的 skill，
目前最常用的就是 plan-ceo-review

我自己也蠻常將跑過的流程寫成 skill 的
花了點時間研究它的設計，蠻有東西的

簡單說 gstack 就是把 Claude Code 變成一個虛擬工程團隊
13 個 slash command 涵蓋從產品規劃到 QA 到發佈的完整流程
最狠的是它內建 Playwright 瀏覽器引擎
讓 AI 有了「眼睛」，可以真的開瀏覽器、點按鈕、截圖找 bug

下面聊聊我的觀察