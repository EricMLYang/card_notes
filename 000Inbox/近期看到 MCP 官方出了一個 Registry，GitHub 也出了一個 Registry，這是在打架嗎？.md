近期看到 MCP 官方出了一個 Registry，GitHub 也出了一個 Registry，這是在打架嗎？

不是的，讓我解釋一下 MCP Registry 的架構。

 為什麼需要官方 Registry？

官方 MCP Registry 是一個統一的 metadata service，解決了幾個關鍵問題:

1\. Server Discovery: 各種 MCP servers 散落在各個 GitHub repo、社群討論串，很難找。現在有了中央目錄，方便找到合適的 MCP server。更重要的是，它提供標準 API，未來 AI agents 可以自動發現和選擇需要的工具。

2\. 信任與安全性: 你可以知道這個 MCP server 是誰建立的，是不是官方認證的。這能大幅減少安全風險，避免安裝到惡意或釣魚的 MCP server。Registry 還有社群回報機制，可以標記和移除有問題的 servers。

3\. 版本追蹤: 清楚知道你正在使用哪個版本的 MCP server，有沒有更新可用，避免版本混亂的問題。

 兩層 Registry 的分工

官方的 Registry 和 Github 的 Registry 的關係就像「中央資料庫」和「使用者介面」的差別。

1\. MCP 官方 Registry 是個純粹的 metaregistry，它的工作很單純: 當作所有公開 MCP servers 的「single source of truth 單一事實來源」。它只提供 API 和標準化的 metadata，沒有漂亮的 UI，就像一個中央資料庫。

2\. GitHub 的 MCP Registry 則是一個 subregistry，專門做使用者體驗。它會從上游的官方 Registry 自動同步資料，加上 GitHub 特有的功能: 漂亮的瀏覽介面、用 GitHub stars 排序、VS Code 一鍵安裝等等。

 Metaregistry 的設計

有個關鍵概念是 MCP Registry 只有做 metaregistry，沒有存真正的程式碼檔案。

這是因為開源軟體圈早就有成熟的套件管理系統: JavaScript 有 npm、Python 有 PyPI、容器化應用有 Docker Hub。這些都是各社群花了十幾年建立的基礎建設。

因此 MCP 就不重新發明輪子了:

\* MCP server 的程式碼檔案，還是發布到 npm 或 PyPI 等等 (就像平常發布套件一樣)

\* MCP Registry 只記錄: 「weather-server v1.2.0 在 npm:weather-mcp」這種索引資訊

於是這形成了架構分工:

1\. 既有套件系統 (npm, PyPI, Docker Hub): 存真正的程式碼檔案

2\. 官方 MCP Official Registry: 新增的索引層，告訴你哪個 MCP server 在哪裡

3\. 各家 Subregistries (GitHub, Smithery 等): 加值服務層，提供好用的 UI 和額外功能

開發者的工作流程是:

1\. 把 MCP server  程式碼發布到 npm/PyPI (不用學新東西)

2\. 在 MCP Registry 註冊一筆 metadata

3\. MCP server 自動出現在所有 subregistries

當你在 GitHub Registry 點「安裝」時，它會查詢 MCP Registry 的 metadata，然後導向 npm 或 PyPI 下載真正的程式碼。

 結語

這種設計比再做一個 MCP servers awesome list 聰明多了，建立了一個分層協作的生態系: 既有套件系統管程式碼、MCP Registry 做索引和信任層、各家 subregistry 專注使用者體驗。開發者只需要發布一次，使用者就能在任何地方找到。開源社群太有智慧啦。

\> 架構圖片出自官方文件 Ecosystem Vision，也推薦一看。


