Agent Sandbox 沙箱架構: 論兩種設計模式與七種隔離方式
2026-04-20
AIAgentSecurity
Agent Sandbox 沙箱架構: 論兩種設計模式與七種隔離方式
最近 Agent Sandbox 這個話題蠻熱的，Simon Willison 在年初就預測「2026 會是解決 sandbox 的一年」。從他列出的名單看來這個預測蠻準: Claude Cowork 內建完整 Linux VM、Fly.io 推出 Sprites.dev、Docker 上線 Docker Sandboxes、Anthropic 在 Claude Code 加上 OS 層 sandbox、連 OpenAI Agents SDK 最近也補上相關支援。

這篇小編想整理一下: 什麼是 Agent Sandbox?為什麼 AI Agent 需要沙盒?以及目前有哪些做法、各自的優缺點是什麼。

什麼是 Agent Sandbox
講白話就是給 AI Agent 跑指令和程式碼的「隔離環境」。這個環境要能限制 agent 能碰到的檔案、能連的網路、能呼叫的系統資源，讓 agent 放手去做事的時候不會把本機或伺服器搞爛。

為什麼 Agent 需要 Sandbox
有幾個核心動機:

1. 防 Prompt Injection 攻擊
這是最硬的理由。只要 agent 會讀外部內容(網頁、Email、文件、別人給的 repo)，就可能被注入惡意指令。沒有 sandbox 擋著，一個被勾引的 agent 可能順手就把 ~/.ssh/id_rsa 上傳出去了。

2. 保護本機不被破壞
Agent 會錯、會亂寫、會跑錯指令。沒有隔離，一個 rm -rf 或誤改 .bashrc 就掛了。

3. 減少授權疲勞 (Approval Fatigue)
Claude Code 的經驗很有代表性: 如果每個 bash 指令都要使用者按「同意」，最後大家會下意識連點 Y。Anthropic 有個數據蠻驚人——加上 sandbox 之後，權限詢問次數減少 84%。預先劃出清楚的邊界，反而比一直問還安全。

4. 平行執行、乾淨重現
每個 agent 一個乾淨的 sandbox，不會互相污染、依賴衝突也沒了，一次跑十個也沒問題。團隊之間要重現別人的執行環境也容易。

編按: Fly.io CEO Kurt Mackey 講過一句蠻經典的話 ——「Agent 不想要 container，不想要 sandbox，它們要的是『電腦』」。意思是 agent 需要有狀態、可以累積的工作環境，不是每次用完就丟。這點後面會看到，不同做法對這件事的回應很不一樣。

Agent 跟 Sandbox 怎麼組合: 兩種整合模式
在講技術做法之前，先看 LangChain 最近一篇文章整理的兩種 pattern，這是更上位的架構選擇:

Pattern 1: Agent IN Sandbox
Agent 本身跑在 sandbox 內，要跟外面溝通走網路 API。E2B、Runloop、OpenCode 都支援這種模式。

優點: 最像本機開發環境，agent 有完整的檔案系統、記憶體、上下文，緊密耦合好寫。
缺點: API 金鑰必須放進 sandbox (多一層風險);agent 邏輯改一點就得重建映像、重新部署;prompt 跟 agent 的設計細節也比較容易外洩;不同工具之間的權限隔離比較弱。

Pattern 2: Sandbox as Tool
Agent 跑在本地或自己的 server，要執行程式碼時才遠端呼叫 sandbox API。Daytona、Modal、E2B、Runloop 都支援這種用法。

優點: Agent 邏輯改了立刻生效，不用重新部署;API 金鑰留在 agent 這端;狀態跟執行環境乾淨切開;容易平行多個 sandbox;按次計費成本攤得開。
缺點: 每次執行都有網路延遲，細碎操作累積起來會慢。

OpenAI 官方的兩張對照圖
OpenAI 在 Agents SDK 文件裡剛好用兩張圖把這兩個 pattern 對照出來，視覺上非常清楚，小編拿來當本文的主要參考。

圖 1: Harness in compute (= Pattern 1)

Harness in compute

Harness、Agent Loop、MCPs/Tools 全都跑在 sandbox 裡面;外部的 Server 用 API 呼叫把 coding agent「踢進」sandbox 啟動;sandbox 要存取外部資料時，透過一個 Gateway Service (握有 secrets) 代打，Gateway 會攔截請求防止 sandbox 亂連外網。OpenAI 原文對這個做法的評語翻成中文大意是:「適合原型，但會把編排邏輯跟模型指揮的執行擠在同一個 compute 邊界裡」——違反信任隔離原則。

圖 2: Harness separate from compute (= Pattern 2)

Harness separate from compute

Harness、Agent Loop、MCPs/Tools 跑在 trusted 環境裡 (可以是 Temporal、AWS、Azure 等，圖上 “Runs anywhere” 那排);Secrets 也留在這個 trusted 環境。Sandbox 只剩 filesystem 加上供應商支援的執行環境 (OpenAI Hosted Containers、Modal、E2B、Vercel、Daytona、Cloudflare 等 logo 直接列在圖裡)。Server 要存 Data/APIs/Web 是從 trusted 環境過去，不是從 untrusted 的 coding sandbox 過去。OpenAI 原文強調: Server 存資料庫和網路是從 trusted 環境出去，不是從不受信任的 coding sandbox 出去。

兩張圖連起來看: OpenAI 用這兩張圖做觀念對照，圖 1 不是 SDK 的實作，而是當作反例: 展示「prototype 常見的把 harness 塞進 sandbox」的做法，方便但犧牲信任隔離。SDK 實際走的是圖 2 (Pattern 2)，Cookbook 的範例也都是圖 2。前面 Browser Use 那套技術上落在圖 1 的 pattern —— 但他們沒用 OpenAI SDK，而是自建 control plane 加強化三件套 (bytecode-only、setuid 降權、env var 刪除) 加 Unikraft micro-VM，把圖 1 的安全缺陷補起來。這是可行但工程量大的做法。

小編覺得大部分新專案 Pattern 2 是比較好的起點，開發迭代快、憑證比較安全，跟 OpenAI 的建議一致。但 Browser Use 的經驗顯示，當規模拉大、要跑百萬級 agent 的時候，Pattern 1 配上控制平面 (control plane) 反而會變成更好的選擇 —— 下一段小編把他們的架構拆開來講。

實戰案例: Browser Use 的 Control Plane 架構
Browser Use 在 X 上分享過他們的 agent sandbox 架構，蠻值得拆開來看。他們跑百萬級的 web agent，走過的路是「先用 Pattern 2 (Sandbox as Tool)，後來搬到 Pattern 1 (Agent in Sandbox)」，跟前面直覺可能相反。

編按: Browser Use 原文把兩個 pattern 的編號對調了 —— 他們的 Pattern 1「Isolate the tool」對應 LangChain 的 Pattern 2，Pattern 2「Isolate the agent」對應 LangChain 的 Pattern 1。本文為了一致性統一用 LangChain 的編號。

為什麼要換? 他們一開始 agent 主循環跟 REST API 跑在同一個後端，結果「重新部署就殺掉所有執行中的 agent」「記憶體吃很多的 agent 會拖慢 API」。兩種工作負載 (長時間 agent vs. 短促 API 請求) 本來就不該擠在同一個行程。

控制平面是關鍵: Agent 跑在 sandbox 裡，但 sandbox 裡沒有任何憑證 —— 只有三個環境變數: SESSION_TOKEN、CONTROL_PLANE_URL、SESSION_ID。要打 LLM、存 S3、算帳單，全都透過控制平面代理。控制平面握真憑證、維護對話歷史、做權限控管和計費。

幾個小編覺得蠻巧妙的設計:

LLM 代理: Sandbox 只送新訊息，控制平面從資料庫重組完整對話上下文再打給 LLM 廠商。Sandbox 完全無狀態，隨時可以殺掉重開，對話接得回來。
檔案同步用預簽 URL: Sandbox 要傳檔去 S3 不用拿 AWS 金鑰，而是跟控制平面要一次性的預簽 URL。
強化三件套: Docker 建置時把 Python 編譯成位元碼再刪掉 .py 原始碼;啟動入口跑起來後立刻 setuid 降權到 sandbox 使用者;讀完環境變數立刻從 os.environ 刪掉。
Unikraft micro-VM: 生產環境每個 agent 一個 Unikraft micro-VM，啟動時間一秒內、閒置時歸零;開發和評估環境同一個映像改跑 Docker，sandbox_mode 一個設定切換就好。
作者 Larsen 收尾一句話小編蠻喜歡: 「讓你的 agent 沒東西可偷，也沒東西要保留」。這就是 Agent in Sandbox 配控制平面做到極致的樣子 —— sandbox 被偷走也沒差，裡面根本沒東西值得偷，被殺掉也沒差，因為狀態全在控制平面的資料庫裡。

這個案例也呼應了 Mackey 那句「agent 要的是電腦」的觀察: 後面要講的七種技術實作裡，Unikraft micro-VM 剛好踩在「MicroVM」那條線上，同時提供了「像電腦」的持久化體驗跟強隔離。

技術實作的七種路線
如果從「怎麼做隔離」這層看，目前有七種主流做法，各自有各自的甜蜜點:

1. OS 層 Process 隔離 (Seatbelt / Bubblewrap)
Claude Code 2026 年加的 sandbox 就是這條路。macOS 用 Seatbelt、Linux 用 Bubblewrap，靠作業系統原生的隔離機制限制子行程能讀寫的路徑和能連的網域。Anthropic 甚至把這個執行環境開源成 @anthropic-ai/sandbox-runtime npm 套件。

OpenAI Codex CLI 也是同一條路，macOS 一樣用 Seatbelt (sandbox-exec 加上動態產生的 SBPL profile)，Linux 則是 Bubblewrap 加 Landlock 做 LSM 層補強、再搭配命名空間隔離 (--unshare-user/pid/net)，Windows 則用 Restricted Tokens。小編覺得蠻有意思的是，兩家主流的 CLI coding agent (Claude Code 跟 Codex) 最後都收斂到同一個技術選擇，看來 Seatbelt + Bubblewrap 已經是「本機 coding agent」的事實標準了。

優點: 輕量、啟動快、跟本機開發無縫接軌，不用另外拉機器。
缺點: 綁作業系統 (macOS 和 Linux 要各寫一套，Windows 原生還沒支援);隔離強度比 VM 弱，理論上還是可能被突破;在 Docker 裡跑 Linux 版還要退回弱化模式。適合單人本機用。

2. 容器 (Docker Container)
最傳統的做法，用 Docker 映像包起來。很多雲端 sandbox 服務底層其實都是容器。

優點: 生態成熟、可重現、部署簡單、大家都會用。
缺點: 共享主機核心，隔離強度對「真正不信任的程式碼」來說其實有點不夠;啟動稍慢 (秒級);狀態管理要另外處理。

3. MicroVM / 完整 VM
Claude Cowork 的 macOS 應用用 Apple Virtualization Framework 開一個完整 Linux VM 來跑 agent。Docker 推出的 Docker Sandboxes 每個都是 microVM，有自己的 Docker daemon、檔案系統、網路。Fly.io 的 Sprites.dev 也是這條路，主打「整個硬碟狀態的快照和還原」。

優點: 隔離最強、硬體級別的分離;持久化狀態方便 (完美對上 Mackey 說的「他們要電腦」);快照跟還原做得好的話體驗很好。
缺點: 資源用得多一點;設定相對複雜。這是目前「本機跑高強度 agent」的主流方向。

4. 遠端雲端沙盒服務 (Sandbox-as-a-Service)
E2B、Modal、Daytona、Runloop、Fly Sprites 這一掛。LangChain 的 Deep Agents 最近也加了 Runloop、Daytona、Modal 三家支援。

優點: 不用自己架，直接打 API 就好;天生支援平行、擴展、長時間任務;按次計費，成本攤得開。
缺點: 網路延遲;憑證管理要小心 (LangChain 建議用短期憑證搭配人工介入);會鎖定平台。

5. WebAssembly Runtime
Simon Willison 最看好的一條路。他自己做了實驗性的 Denobox (用 Deno 子行程跑 JS + Wasm)，另外 Python 生態還有 amla-sandbox、eryx、localsandbox 三個新專案，目標都是「讓 Python 可以方便地用 Wasm 跑不信任的程式碼」。

優點: 真·語言層沙盒、啟動毫秒級、跨平台、不需要作業系統特權。非常適合「agent 要執行一小段 LLM 生的程式碼」的場景。
缺點: 能跑的語言或執行環境有限 (主流是 Python、JS、Rust);要用到系統工具 (docker、git CLI 等等) 就不行;生態還年輕。

6. 瀏覽器就是沙盒
Paul Kinlan 的觀點蠻有趣: 瀏覽器是一個被打磨 30 年、專門設計用來跑「來自網路的不可信程式碼」的 sandbox，幹嘛不直接用?他做的 Co-do 就是示範 —— 用 File System Access API 拿資料夾權限、CSP 管網路請求、Web Worker + Wasm 跑程式碼，整個 agent 在瀏覽器分頁裡面跑完。

優點: 零安裝、零後端、天然跨平台、安全模型現成而且打磨多年。
缺點: 能做的事被瀏覽器 API 限制住 (沒有 shell、沒有任意執行檔);適合輕量型應用，要碰系統工具就不行。

7. 語言層解譯器沙盒 (Capability-based)
Pydantic 最近出的 Monty 蠻有意思。他們用 Rust 從頭寫了一個 Python 位元碼虛擬機，預設「什麼都不能做」——沒檔案、沒網路、沒環境變數，要讓它做什麼就得自己審核過再開放對應的函式。

優點: 微秒級啟動、狀態只有幾 KB 可以輕易做快照、每次執行零成本、允許清單 (allowlist) 比拒絕清單 (denylist) 安全得多。
缺點: 只能跑 Python 子集;不適合需要整套系統工具的場景。定位比較偏「讓 LLM 寫 Python 取代一連串工具呼叫」這個用法。

Pattern 跟技術做法的對照
前面談了「兩種整合 pattern」跟「七種技術實作」，這兩個其實是不同維度 —— pattern 講 agent 和 sandbox 怎麼組合，技術實作講 sandbox 靠什麼機制做隔離。實務上會「挑一個 pattern，再挑一個技術來落地」。小編整理了一張對照表:

技術做法	最常見的 Pattern	典型代表
OS 層 (Seatbelt / Bubblewrap)	Pattern 2	Claude Code、Codex CLI
Container (Docker)	兩者皆可	多數 SaaS 底層、本機開發環境
MicroVM / 完整 VM	Pattern 1 居多	Claude Cowork、Browser Use (Unikraft)、Fly Sprites、Docker Sandboxes
雲端 SaaS	Pattern 2 為主，也支援 Pattern 1	E2B、Modal、Daytona、Runloop、Blaxel、Vercel
WebAssembly	Pattern 2	Denobox、amla-sandbox、eryx、localsandbox
瀏覽器	Pattern 1	Co-do
語言層解譯器	Pattern 2	Pydantic Monty
幾個值得注意的搭配:

CLI coding agent 都是 OS 層 + Pattern 2: Claude Code 和 Codex CLI 的主循環跑在你本機，但每個 bash 指令被 Seatbelt/Bubblewrap 包住。Agent 本身其實在 sandbox 外面。
Pattern 1 配 MicroVM 是「大規模 agent 服務」的主流: Browser Use 的 Unikraft、Claude Cowork 的 Apple Virtualization 都是這個組合。隔離強、啟動夠快、持久化狀態方便，適合「agent 當作可拋棄運算單元」的場景。
Wasm 跟 Monty 只走 Pattern 2: 因為它們不是「完整電腦」，只是一個受限的執行引擎，主要任務是安全地跑一段程式碼。
SDK 層的整合: OpenAI Agents SDK
2026 年 4 月 OpenAI 在 Agents SDK 加上原生 sandbox 支援。小編覺得這次更新的重點不是做新的隔離技術 (底下就是用現成的 sandbox 服務)，而是把「agent 工作站」的合約標準化。下面幾段試著用白話把它的設計拆開講，不用熟 SDK 的程式碼也能看懂。

走哪個 pattern、綁什麼技術? OpenAI Agents SDK 走 Pattern 2 (Sandbox as Tool) —— agent 主循環跑在你控制的 trusted 環境，要執行 shell 指令或改檔案時才遠端呼叫 sandbox，沒事不佔資源。官方用前面那兩張對照圖解釋為什麼選這個 pattern (不是說 SDK 兩種都支援，而是在說為什麼不走圖 1 那條路)。底層技術則完全不綁定: 同一套 agent 邏輯，本地開發可以跑 Docker 容器，生產環境換成 E2B (容器) / Vercel (MicroVM) / Cloudflare (Workers isolate) 等，換供應商只改一行設定、不用改 agent 程式碼。這也是 OpenAI 把 SDK 定位在「合約層」而不是「隔離層」的關鍵。

SDK 新加了兩層合約: 一層叫「環境合約」，描述 sandbox 開起來是什麼樣 —— 要掛哪些檔案、哪些目錄、要從哪個 git repo clone、要掛載哪些 S3 / R2 / GCS / Azure Blob 儲存 (SDK 裡這叫 Manifest)。另一層叫「操作合約」，把 agent 在 sandbox 裡能做的事拆成可組合的能力: 執行指令、編輯檔案/檢視圖片、載入技能包、跨次執行累積經驗、長對話壓縮 (SDK 裡這叫 Capabilities，對應的能力名稱是 Shell / Filesystem / Skills / Memory / Compaction)。環境合約定義「agent 進到什麼環境」，操作合約定義「agent 在環境裡能做什麼」，兩個合起來就是 OpenAI 想標準化的「agent 跟 sandbox 之間的介面」。

內建九家供應商: Blaxel、Cloudflare、Daytona、E2B、Modal、Runloop、Vercel 七家雲端，加上本地的 Docker 跟 Unix 行程共九家，全部共用同一組合約介面。

題外話 — OpenAI 自己的 Hosted Containers 竟然不在清單裡: OpenAI 其實有自家的 sandbox 即服務，叫 Hosted Containers (走 Responses API 的 container_auto 旗標)，OpenAI 預先幫你開好 Debian 12 容器、裝好 Python / Node / Ruby / Go 等環境，可以跨 request 存活 20 分鐘閒置時間。但這個服務目前不在 Agents SDK 的 9 家內建供應商清單裡，兩條路是分開的。Hosted Containers 目前的定位看起來是「只用 OpenAI 模型、只需要跑段程式碼或簡單 shell、不想管 sandbox 基礎設施」的輕量場景 —— 一個 flag 就能用。至於會不會被收進 Agents SDK 當第十家?小編猜應該會啦，畢竟 OpenAI 把 SDK 定位成合約層、自家又有現成供應商，兩邊打通是自然的事，就看時機。

Host 跟 sandbox 的分工: 這裡有個容易誤會的點 —— SDK 裡有個類別叫 SandboxAgent，聽起來像「住在 sandbox 裡的 agent」(Pattern 1)，但它不是。官方 Cookbook 白紙黑字寫「harness outside the sandbox」。實際分工:

Host 端跑的: Agent 主循環、LLM 呼叫、操作合約的 handler、MCP server、憑證
Sandbox 裡跑的: 只有「操作合約被呼叫時觸發的實際動作」—— 執行中的 shell 指令 (例如 pytest)、正在被編輯的檔案、agent 啟動的子行程 (test runner、dev server 之類)
操作合約底層就是註冊給 LLM 的 function calling 工具。LLM 吐出「執行 pytest」這樣的 tool call，host 上的 handler 攔下來、把指令送進 sandbox 跑、結果再回到 host 塞進對話。所以「Sandbox as Tool」這個名字剛好兩層意思都對上: 架構上 sandbox 是 agent 從外部呼叫的能力，技術上就是 function call 工具。

狀態切成三類分別管: Host 跟 sandbox 分離之後，狀態也自然分開。SDK 把 run 的狀態切三類:

執行狀態: 模型訊息 (也就是對話訊息)、工具狀態、核准流程 —— 存在 host
Sandbox session 狀態: 可序列化的連線描述，拿來重連同一個 sandbox —— 存在 host
工作區快照: Sandbox 裡檔案的備份，拿來初始化一個新 sandbox —— 存在 host 或外部儲存
好處有三個: 憑證不會暴露在 LLM 生成程式碼跑的環境裡;sandbox 容器死掉不等於整個 run 掛掉，三類狀態可以分別還原;容易平行跑多個 sandbox 或把子 agent 路由到獨立環境。前面 Browser Use 手工打造的那條控制平面路線，這裡直接變成 SDK 的預設。

對話紀錄放在哪? 三類狀態裡的「執行狀態」就包含對話訊息 —— 預設跑在 host。但這只是其中一種做法，對話歷史其實有三個可能的存放位置:

存放位置	機制	適合場景
Host 本機	SDK 內建的 session 物件 (例如 SQLite 版)	單機、小規模、開發測試
OpenAI 伺服器端	Responses API 的 previous_response_id / Conversations API	只用 OpenAI 模型、不想自己存狀態
自建後端	像 Browser Use 的控制平面資料庫	多供應商、要自己控管計費跟稽核
不管選哪個，原則不變: sandbox 一律不碰對話紀錄，對話收束在哪一層是上游的選擇題。用 OpenAI 伺服器端 conversation 時，host 只握一個對話 ID 當指標、LLM 狀態由 OpenAI 後端管，host 本身可以薄到幾乎只剩轉發層 —— 這對做 SaaS agent 服務特別有吸引力。

一個具體案例: OpenAI Cookbook 有一份 legacy codebase 遷移 agent 教學，做的是把程式碼從 Chat Completions 搬到 Responses API。做法是把大遷移拆成「一個服務一個 task」，每個 task 開一個獨立 sandbox、agent 跑完產出一個 patch 就把 sandbox 拆掉，天然對應到一個獨立 PR 的 review 流程。Agent 只拿 Shell 跟 ApplyPatch 兩個 Capabilities，其他東西全部留在 host 端。這個例子還順便示範一個蠻漂亮的延伸: MCP server 也掛在 host 端 —— agent 要查 OpenAI 官方文件時，透過 host 的 MCP 代查，sandbox 自己根本不用拿 MCP 憑證、也不用開對外網權限。憑證、工具、文件通通留在 host，sandbox 真的就乾淨只有當下這個 task 的檔案跟指令。

2026 的 agent 基礎設施不只在卷 sandbox 本身，也在卷「agent 跟 sandbox 之間的合約」長什麼樣，OpenAI 這步就是在定義那個合約。

怎麼選?
每條路線都有各自的甜蜜點，小編簡單收斂一下選擇建議:

本機單人用 Claude Code 這類 coding agent → OS 層 sandbox 最無痛
要讓 agent 自己建環境、裝套件、長期工作 → MicroVM (Docker Sandboxes、Fly Sprites、Claude Cowork 這類)
產品要讓使用者帶自己的 agent 跑程式碼 → 遠端雲端 sandbox (E2B、Modal、Daytona、Runloop)
只需要安全地跑一小段 LLM 生的程式碼 → Wasm sandbox 或 Pydantic Monty
做純前端/客戶端 agent → 瀏覽器 sandbox
一些觀察
Agent 這件事最後還是會收斂到「信任邊界」的工程問題。Anthropic 把 sandbox-runtime 開源、OpenAI 在 Agents SDK 裡把 Manifest 跟工作區標準化、Pydantic 用 Monty 做能力制 (capability-based) 解譯器、Luis Cardoso 寫了 Field Guide…這個方向確實是 2026 年 agent 基礎設施最值得盯的區塊之一。

過去一兩年大家在 agent 層堆各種 prompt 技巧、規劃器、記憶、工具，這些都很重要。但真的要讓 agent「放手去做」，底下這層隔離才是那個決定「膽子能放多大」的前提 —— 沒有 sandbox 撐著，再好的工具你也不敢給它自動核准。這兩件事是互補的: 工具決定 agent 能做什麼，sandbox 決定我們敢讓它做到哪。