---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-11
---

## [重點]
agent-browser  去控制任何 Electron based 的 App，也可以 agent 操作瀏覽器做驗測

## [摘要]


## [詮釋]


---
agent-browser 一定要學！它能控制你任何桌面上的 Electron 應用，包括 slack ！ 

agent-browser 可控制任何 Electron 應用，有人用它讓 Claude Code 控制 Slack 自動發送訊息，打通桌面應用自動化。


https://x.com/pahudnet/status/2028349701402099885
才发现原来可以使用前几天我推荐的 agent-browser  去控制任何 Electron based 的 App，OP 就用 agent-browser 让 Claude Code 去控制了 Slack，自动化的发送信息。

用的是这两个 skills，一个是 Slack 专属的：

https://
skills.sh/vercel-labs/ag
ent-browser/slack

一个是通用的 Electron 应用的：

https://
skills.sh/vercel-labs/ag
ent-browser/electron


其实原理很简单：
几乎所有的 Electron 应用都会暴露 Chrome DevTools Protocol (CDP) 端口，通常是 --remote-debugging-port=9222 或类似端口，然后使用 CDP  协议進行控制，一旦連上，就跟控制普通 headless Chrome 幾乎一樣。

所以任何瀏覽器自動化工具都是可以控制的，比如 Playwright 或者  Puppeteer。

但是還是一個很棒自動化的思路。 

The "holy shit" moment when I realized agent-browser can control Slack

npx skills add vercel-labs/agent-browser --skill slack 


## 補充
該段文字說明一項結合 AI 代理（AI Agent）與自動化工具的技術實作。具體意義可拆解為以下四點機制與邏輯：

**1. agent-browser 的技術定位**
`agent-browser` 是由 Vercel Labs 開發的命令列（CLI）瀏覽器自動化工具。其專為 AI 代理設計，運作方式是提取介面快照，並為可互動元素生成簡短的參照碼（如 `@e1`、`@e2`）來取代複雜的 DOM 結構或 CSS 選擇器，使 AI 能夠準確且低 token 消耗地辨識並操作介面。

**2. 控制 Electron 應用的底層邏輯**
Slack、VS Code 等桌面應用程式是基於 Electron 框架開發，其底層依賴 Chromium 引擎，因此原生支援 Chrome 開發者工具協定（Chrome DevTools Protocol, CDP）。只要該應用程式在啟動時開啟遠端除錯連接埠（`--remote-debugging-port`），`agent-browser` 就能透過 CDP 連線，將該桌面軟體視為一般網頁，執行讀取 DOM、截圖、點擊與輸入文字等操作。

**3. Claude Code 的自動化整合**
Claude Code 是 Anthropic 推出的 AI 程式碼助手。透過為 Claude Code 安裝 `agent-browser` 的技能模組（Skill），系統會建立連動。運作流程為：使用者下達自然語言指令（如「透過 Slack 發訊息」） -> Claude Code 呼叫 `agent-browser` 檢視 Slack 介面 -> 取得元素參照碼 -> Claude Code 產生對應的點擊與輸入指令並執行。這達成了由 AI 完全自主操作介面的流程。

**4. 錯誤前提拆解與限制**
文字敘述提及「能控制你任何桌面上的 Electron 應用」，此說法在實務上受限於以下條件，並非毫無限制：

* **限定技術棧**：這套自動化機制僅對基於網頁技術打包的 Electron 或 WebView 應用有效。無法控制以 Swift、C++ 或 .NET 等技術開發的純原生桌面應用程式。
* **安全性與連接埠限制**：必須能夠修改該應用程式的啟動參數以開啟 CDP 除錯埠。在部分企業資安管控嚴格或鎖定啟動程序的環境下，應用程式會拒絕開啟除錯模式，此時 `agent-browser` 無法連線與控制。提供的 X (Twitter) 連結即為展示上述技術成功串接的實例來源。