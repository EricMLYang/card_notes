# API 是能力來源，CLI 是能力入口——Agent 時代的介面分層

- 狀態：KEEP
- 類型：Principle
- 分類：8-
- 索引：010_CardNotes/01_Index/08_system_architecture.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260327_CoreNote_CLI是Agent重要溝通介面.md

## 核心命題
在 Agent 時代，系統的「能力入口」（CLI）比「能力來源」（API）更決定 Agent 能否低摩擦地操作系統。

## 卡片內容
API 提供系統能力（Drive、Databricks、各種雲端服務），CLI 則是操作這些能力的介面封裝。大多數 CLI 本質上就是 API 上層的一層。但對 Agent 而言，兩者的操作成本結構截然不同：直接走 API 需要理解 SDK、處理驗證、組裝 request、解析 response，每一步都是出錯點；而 CLI 路徑是「呼叫指令 → 拿到結構化輸出（JSON）→ 繼續決策」，是 Agent 擅長的線性流。因此，系統是否能被 Agent 高效操作，瓶頸往往不在 API 的能力有多強，而在 CLI（或等價的工具介面）的設計品質——包括輸出是否結構化、指令是否可被探索、錯誤是否可機器理解。

## 使用情境
- 設計新系統時，判斷要先投資 API 還是 CLI/Tool 層
- 評估現有平台「Agent-readiness」的架構審查
- 決定 Agent 該用 SDK 串接還是 CLI 方式操作系統

## 邊界 / 失效條件
- 當 API 本身就有優秀的 SDK 封裝（如 OpenAI Python SDK），CLI 的成本壓縮優勢會縮小
- 對需要長連線、streaming、複雜狀態管理的場景，CLI 的指令式互動模型有天然限制
- CLI 的「可組合性」仰賴每個指令的 input/output 契約穩定，若契約常變動，維護成本反而上升

## 上游連結
- [[好 API 設計可以維持很久——Stripe V2 的穩定抽象哲學]]
- [[Agent 時代 CPU 從配角變指令層：工具處理佔總延遲 50%-90%]]

## 下游連結
- [[Skill是可編碼的判斷力_從Prompt到Skill的典範轉移]]
- [[非同步 Agent 工作模式是必然趨勢]]

## 關聯對照
- [[Agent-friendly CLI五大設計原則]]
- MCP 協議（另一種讓能力變成 Agent 工具的標準化路徑）
- Unix 哲學（小工具 + pipe 的可組合設計，CLI 的思想源頭）

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
