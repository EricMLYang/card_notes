---
pipeline_stage: "DONE"
topic: "用 PM Agent 跑了一輪 Discovery，我被自己的 Repo 驚到了"
scenario: "case_study"
selected_cards:
  - "3-Harness 是把模型變成 Agent 的關鍵（不是模型本身）.md"
  - "3-Context Graph 捕獲組織隱性知識.md"
  - "4-Prototype as SPEC：AI 時代的架構心法.md"
  - "1-人機協作設計：建立 AI 與人類分工循環.md"
  - "2-擬人化技巧將概念轉為可互動角色.md"
  - "4-CLAUDE.md 是 AI 助手的腦——投資配置指數回報.md"
  - "3-判斷力與品味的涌現（從工具到決策者）.md"
  - "4-Vibe Coding：80% 規劃 20% 執行的工作流.md"
chosen_title: "產品探索的「模擬器」：如何利用 Repo Context 讓 Agent 產出敢拿去訪談的假設"
chosen_hook: "想像你坐在電腦前，讓 PM 策略師和使用者代表 Agent 坐下來對話，而你只需要在旁邊觀察、判斷、校準。"
chosen_framework: "explosive_formula"
created: 2026-02-23
last_updated: 2026-02-23
status: "published"
---

# 產品探索的「模擬器」：如何利用 Repo Context 讓 Agent 產出敢拿去訪談的假設

▋ 週日下午的 PM Agent 實測

今天我完成了一項測試，驗證 Repo Context 能否驅動 Agent 完成產品探索（Product Discovery）。

我在一個名為 MI_PM 的 Repo 裡，塞進了專案的完整 Context。
同時定義了 PM 策略師、UX 設計師、以及 DSBG 使用者代表等角色。
原本我只是想確認這套由 Markdown 檔案構成的工作流能否運轉。
沒想到在 30 分鐘內，這套系統跑出了完整的工作細節。

這是一次從信號捕獲到 Discovery Brief 的實戰紀錄。

▋ 自動化的視覺化儀表板

Agent 具備讀取結構化文件並產出視覺化結果的能力。

我請 PM 策略師與 UX 設計師協作，讀取 `context/02_dashboard.md` 裡的數據。
系統自動產出了一份 HTML 儀表板。
內容包含 Discovery Pipeline 漏斗圖、風險熱力圖、以及 6 個驗證實驗的雷達圖。
圖表使用 Chart.js 繪製，採用暗色主題。
數據由 Agent 自行從實驗文件中整合，完全不需要手動填寫。

這種方式讓數據更新與圖表產出實現了同步。

▋ 可互動的使用者訪談原型

UX 設計師 Agent 能夠根據產品背景，快速產出具備邏輯的介面原型。

它模擬了一個完整的 MI 2.0 系統介面。
包含導航列、KPI 摘要卡片以及市佔比較趨勢圖。
最實用的細節在於，頁面底部直接嵌入了一份針對 EXP-001 驗證實驗的問卷。
這份原型讓我可以帶著具體的互動邏輯，直接進入使用者訪談現場。

模糊的需求透過原型變成了可對齊的點對點驗證。

▋ 使用者角色的沙盤推演

透過擬人化 Agent 角色，我們可以在開發前完成高品質的需求收斂。

我讓 PM 策略師與使用者代表進行了 5 輪對話。
盤點了 CSV 檢查與資料搬運的痛點。
使用者代表明確提出了「數據正確性」高於「自動化」的判斷標準。
最後系統收斂出 6 項價值需求（VR-001 ~ VR-006）。
並附帶 Cost of Delay (CoD) 的評估與優先權氣泡圖。

模擬對話為真實訪談提供了一份結構化的假設清單。

▋ Context Engineering 是核心關鍵

Agent 的產出品質，主要取決於 Repo 內 Context 的完整度。

我花了很多時間在建構 Context 結構。
包含方法論（00_init）與系統架構（01_product）。
這些文件是 Agent 的「記憶」與「世界觀」，讓它的回應能對齊業務邏輯。
這就是 [[3-Harness 是把模型變成 Agent 的關鍵]]。
環境與背景資訊決定了輸出的天花板。

維護一個「活的」文件系統，是 AI 協作時代的高槓桿投資。

▋ Repo as Brain 實現探索民主化

將專案 Context 結構化地放進 Repo，可以讓 Repo 成為團隊的共享大腦。

任何 Agent 都能讀取這些記憶，並在幾十分鐘內產出高品質的 Discovery Brief。
這降低了產品探索的門檻。
讓 Discovery 能夠成為每個開發任務的標配。
雖然模擬不等於真實，但它能極大地加速我們通往真實的過程。

與其在會議室裡空談需求，現在就開始建構你的 Repo Context，讓 Agent 幫你跑第一輪模擬。
