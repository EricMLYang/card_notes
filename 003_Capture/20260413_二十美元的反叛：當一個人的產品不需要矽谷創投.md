【二十美元的反叛：當一個人的 SaaS 不再需要矽谷】

Steve Hanov 被創投拒絕了。不是因為產品不好，不是因為沒有用戶，不是因為沒有營收。他同時經營多個月營收破萬美元的 SaaS，每一個都有付費用戶每天在用。

創投的回覆是：「你到底需要錢幹嘛？」

這句話本身就是答案。

▋ 一台五美元的伺服器，做完了所有事

Hanov 的技術棧可以寫在一張便條紙上。

一台 Linode VPS，月費五到十美元。Go 語言寫的後端，編譯成一個 binary，scp 上去就跑。SQLite 當資料庫，開 WAL mode 之後讀寫不互鎖，撐幾千個併發用戶不是問題。一張二手 RTX 3090 跑 VLLM 做批次 AI 推理，九百美元一次性投資。OpenRouter 接雲端模型當備援。VS Code 加 Copilot 寫程式碼。

全部加起來，月費大概二十美元。

這不是 side project 的窮酸架構。這是能跑多個 $10K MRR 產品的生產環境。他的 websequencediagrams.com 你很可能用過。他的 eh-trade.ca 用本地 LLM 批次分析上千份上市公司季報，產出股票研究。

他每一層的選擇都不是隨便挑的，而是算過帳的。

▋ 每一層都是一個反直覺的決策

Go，不是 Rust。 Rust 更快、記憶體安全由編譯器保證，社群聲量更大。但 Hanov 一個人維護多個產品，他需要的不是極致效能，而是最低的認知負擔。Go 的學習曲線是一到兩週，Rust 是三到六個月。Go 編譯秒級，Rust 分鐘級。而且——這點在 2026 年格外重要——LLM 生成 Go 程式碼幾乎不出錯，但生成 Rust 遇到記憶體生命週期的問題就很容易生成失敗、無法執行。當你的「同事」是 AI，你得選一個 AI 也寫得好的語言。

SQLite，不是 Postgres。 業界的條件反射是「生產環境要用真正的資料庫伺服器」。但 SQLite 透過 C 介面直接讀記憶體，比 TCP 連線到遠端 Postgres 快一個數量級。「PRAGMA journal_mode=WAL」 一行指令解決併發問題。沒有 connection pool 要管，沒有 migration 工具鏈要維護，備份就是複製一個檔案。

$5 VPS，不是 AWS。 原話：「AWS 控制台是設計來榨取升級費用的迷宮。」一台機器意味著你知道 log 在哪、知道為什麼 crash、知道怎麼重啟。不需要 EKS、不需要 NAT Gateway、不需要在還沒有任何用戶之前就月花三百美元。

本地 GPU，不是 API。 九百美元買一張二手 3090（24GB VRAM），跑 VLLM 做批次推理。Ollama 拿來原型開發，VLLM 上生產——它用 PagedAttention 把 GPU 記憶體壓到極致，16 個並行請求的總時間跟處理 1 個差不多。他再也不需要為批次任務付 API 費用。

▋ 這不只是省錢。這是軟體市場的結構性轉變。

先看底層。VPS 是商品，五美元一台，到處都有。SQLite 是公共財，不要錢。Go compiler 是公共財，不要錢。開源模型——Qwen3、DeepSeek R1、MiniMax M2.7——是公共財，不要錢。這一層已經完全競爭了：大量供應商、同質化產品、自由進出、價格透明。基礎設施變成了水電。

當基礎設施完全競爭化，應用層的進入門檻就消失了。

過去，「造一個能用的產品」需要一個團隊、一輪融資、幾個月的開發時間。現在，一個人用 AI 就能開發、部署、運維一個完整的 SaaS——「軟體公司」的最小可行規模從一個團隊縮小到一個人。

但真正的重點是：低維護成本比低製作成本更重要。

製作成本降低，你會看到更多產品出現。但維護成本降低，你會看到這些產品存活下來。Hanov 的架構不是為了 scale to millions 而設計的——它是為了讓一個人輕鬆維護 100 個客戶以下的產品而設計的。SQLite 不是在「不夠好」的前提下的妥協，而是在「我不需要 scale」的前提下的最優解。一個檔案、零運維、備份就是 cp。

當軟體的生產和維護都降到一個人能承受的程度，市場會發生什麼？

垂直領域會被切得極碎。不是「給餐廳用的 SaaS」，而是「給台北日式居酒屋用的排班工具」。不是「給會計師用的 SaaS」，而是「給跨境電商會計處理巴西稅務的工具」。過去這些 niche 太小，養不活一個團隊。但一個人、一台 $5 VPS、一個 SQLite 檔案——養得活。

這跟過去所有的技術革命都不一樣。印刷術普及了知識的傳播，但沒有普及知識的生產。網路普及了資訊的取得，但沒有普及軟體的製作。語言模型和 AI Agent 做的事情是人類歷史上從來沒出現過的：它普及了智力本身。

當智力不再稀缺，軟體的生產就像夜市擺攤——門檻低、各賣各的、誰都可以來。大公司是百貨公司，micro-SaaS 是夜市攤販。百貨不會跟你搶一個月一萬美元的生意，但一千個攤販加起來，就是一個新的經濟體。每一攤都小、都快、而且老闆就站在攤位後面——你有問題，直接跟他說。

SaaS Apocalypse 的投資端在蒸發 $2T 市值。Hanov 的建設端在證明：替代品的成本已經低到荒謬。

▋ 更極端的路線：Cloudflare 的 Edge Stack

如果 Hanov 的 VPS 架構是反雲端的第一步，那 Cloudflare 的 edge stack 就是把這件事推到邏輯盡頭。

Workers + Durable Objects + D1 + R2。起步價五美元。

Hanov Stack → Cloudflare Edge Stack：

  運算：Go binary on VPS → Workers (V8 isolates, edge 部署)
  資料庫：SQLite（本地檔案） → D1（SQLite 跑在 edge）
  儲存：本地磁碟 → R2（S3 相容，零 egress 費用）
  狀態管理：Go + 記憶體 → Durable Objects（全球分散的有狀態運算）
  延遲：依伺服器位置 → 全球 edge，使用者最近的節點
  月費：~$20 → ~$5 起步

Cloudflare 的做法更極端：你連伺服器都不需要管。D1 本質上就是 SQLite 跑在 edge，所以 Hanov「SQLite 就夠了」的判斷在 edge 架構裡同樣成立——甚至更合理，因為 D1 本身就是基於 SQLite 的 edge 資料庫。

Workers 的冷啟動是毫秒級，不是 Lambda 的秒級。Durable Objects 給你全球分散的有狀態運算。R2 的零 egress 費用直接消除了 AWS S3 最惡名昭彰的成本陷阱。

如果你的產品面向全球用戶、需要低延遲、但規模仍然是 100 客戶以下——Cloudflare 的 edge stack 可能比 Hanov 的單機 VPS 更合適。代價是 vendor lock-in：你的程式碼跟 Cloudflare 的 runtime 綁定了。Hanov 的 Go binary 可以 scp 到任何一台 Linux 機器上跑；你的 Worker 只能跑在 Cloudflare 上。

這就是自由度跟便利性的取捨。兩條路都通往同一個結論：軟體基礎設施的成本已經不再是門檻。

基礎設施的成本解決了。但 AI 推理的成本呢？

▋ 本地 AI：二萬台幣的推理引擎

Hanov 用 $900 的 3090 跑 VLLM。這是 NVIDIA GPU 的路線，強大但吵、耗電、需要一台 PC 當 host。

還有另一條路：一台兩萬台幣以內的 Mac Mini M4（16GB），跑 MLX。

Apple Silicon 的統一記憶體架構意味著 CPU 和 GPU 共用記憶體，不需要把模型權重從系統記憶體搬到 GPU 記憶體。MLX 是 Apple 自家的機器學習框架，針對這個架構做了深度優化。16GB 的 M4 可以跑 Qwen3 8B、Llama 3.3 8B、甚至量化後的 14B 模型，推理速度足以應付批次任務和輕量級即時服務。

跟 Hanov 的 3090 比較：

RTX 3090 + VLLM vs Mac Mini M4 + MLX：

  成本：$900（二手） vs $600（新品）
  功耗：350W vs 15-25W
  噪音：風扇直升機 vs 幾乎無聲
  記憶體：24GB VRAM（獨立） vs 16GB 統一記憶體
  吞吐量：高（PagedAttention） vs 中（單用戶批次夠用）
  生態：CUDA + PyTorch（最成熟） vs MLX + llama.cpp（成長中）
  運維：需要 Linux host vs macOS 當桌機用

3090 在高併發批次推理上仍然勝出。但如果你是 solo developer，一天跑幾十到幾百次推理——Mac Mini 安靜地坐在桌上就夠了。功耗差了十倍以上，7/24 開著跑的電費成本完全不同。

MiniMax M2.7 這週剛開源權重，Qwen3 系列持續更新，DeepSeek R1 的推理能力越來越強——開源模型的品質已經到了「本地跑就夠好」的水準，不是每個任務都需要打 API 給 Claude 或 GPT。Hanov 的 laconic（為 8K context window 設計的 agentic researcher）就是一個具體案例：它像作業系統的虛擬記憶體管理器一樣管理 LLM context，把不相關的對話「page out」，只保留最關鍵的事實在 active context 裡。小模型配合好的 harness，能做的事情比你以為的多很多。

▋ 五個你可以偷的決策框架

➊ 先問「我需要 scale 嗎？」 如果答案是「不，我服務 100 個以下的客戶」——SQLite、單台伺服器、甚至 Cloudflare 的免費 tier 就是正確答案。不要為了假設性的百萬用戶去設計架構。

➋ 選 AI 寫得好的語言。 你的下一個隊友是 LLM。Go 和 TypeScript 目前是 LLM 程式碼生成品質最穩定的語言。Rust 很好，但你會花更多時間修 AI 的 lifetime 錯誤。

➌ 批次推理自己跑。 API 適合即時、低量、高品質的請求。批次分析幾百份文件？本地跑。二手 3090 或 Mac Mini M4 都行，六到十二個月回本。

➍ 用 OpenRouter 或類似的 aggregator 當雲端 AI 入口。 一個介面、多個 provider、自動 fallback。不要直接綁定任何一家 AI 公司的 API——看看 Anthropic 這週偷偷降了 cache TTL（210 分）、Pro Max 額度 1.5 小時就用完（224 分），兩個 issue 同時上 HN 首頁，開發者有多不爽一目瞭然。

➎ 把 VC 的錢當成最後手段，不是第一步。 Hanov 被拒絕不是失敗，是驗證。如果你的產品能在 $20/月的基礎設施上跑出 $10K MRR，你已經證明了產品市場適配——而且你擁有 100% 的股權。

━━━━━━━━━━
Steve Hanov 的 460 分不只是 Hacker News 上的一個好帖子。它是一個訊號：當基礎設施變成水電，當 AI 把智力從稀缺資源變成公共財，當一個人就能做出過去一個團隊才能做的東西——軟體產業的結構正在根本性地改變。

不是更多的獨角獸。是更多的夜市攤販，每一攤都小、都快、都不值得大公司來搶。但一千個這樣的攤販加起來，就是一個新的經濟物種。

這個物種的基礎設施成本是二十美元。它的競爭優勢是老闆就站在攤位後面。