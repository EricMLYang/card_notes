# 燒 CPU 比燒 GPU 省：Sonnet 4.6 的 Programmatic Tool Calling 加速又省錢

> Claude Sonnet 4.6 新功能：Programmatic Tool Calling（程式化工具呼叫）
> 核心突破：將資料處理從 GPU 轉移到 CPU，大幅提升效率與準確率

## 為何這項功能重要？

Sonnet 4.6 剛推出，鎂光燈似乎馬上就被 Gemini 3.1 Pro 的新聞給蓋了過去。但 Sonnet 4.6 的一項新功能立刻引起了我的注意，那就是 **Programmatic Tool Calling（程式化工具呼叫）**。

記不記得前一陣子 Claude Code 推出了 MCP Tool Search 的新功能，取代了傳統必須完整預載所有 MCP 工具集的做法，號稱能省下大量的 Token？然而，這終究只是在小地方省錢、省時間，LLM 運作的本質並沒有改變。

## 傳統 Tool Use 的痛點

現在主流 LLM 的 Tool Use，幾乎都是基於生成 JSON 的能力。當 LLM 發現自己需要呼叫工具時，它會自動生成一段 JSON 格式的文字，包含工具名稱、描述、參數及傳回值等。當外部的 Orchestrator（協調器）收到 LLM 的「呼救」後，就會接收這個 JSON，接著由外部 Runtime 執行工具，再把執行結果丟回給 LLM 的 Context Window。這個循環會不斷持續，直到 LLM 吐出 EOS（結束標記），最後才將結果呈現給使用者。

### Web Search 的例子

舉個最簡單的例子：Web Search。當你詢問 Agent 知識截止日之後的問題時，LLM 會聰明地啟動搜尋工具。接著你會發現，工具去爬了約 10 個網頁，然後**把所有撈到的原始資料全部塞回 Context Window 繼續處理**。這時你的 Token 消耗大概就爆增了，但也無可奈何。

就算你使用了各種 Skill 或是 MCP Tool Search，這個循環依舊不變——海量資料被硬塞進 Context Window 交給 LLM 處理。而**讓 LLM 處理資料就是在燒 GPU，燒 GPU 當然就是在燒錢。**

## 核心問題：為何要用 LLM 做 CPU 的工作？

但冷靜想想，有些純粹的資料整理工作，為何非得交給 LLM 處理不可？像是排序 (Sort)、過濾 (Filter)、尋找與取代，這讓 Python 來做不是更好嗎？**學過資料結構與演算法的都知道，這些運算的代價極低，是標準的 CPU 操作。**

既然能用省錢又快速的方法解決，幹嘛什麼任務都要拿 LLM 這把牛刀來殺雞？就像你在 Linux 下要排序 1,000 萬行資料，你是會直接下 sort 指令，還是打開 Claude Code 把這 1,000 萬行全貼給 LLM 處理呢？（當然，現在的 Claude Code 會聰明到自動幫你下 sort 指令啦）。

## Programmatic Tool Calling 的解決方案

這正是 Programmatic Tool Calling 閃亮登場的時刻。

**LLM 最擅長的事情之一就是寫程式，只叫它產生死板的 JSON 實在是大材小用。** 如果我們只是要處理資料，何不讓它直接寫一段程式？事實上，早期的 Tool Use 就有這種直接讓 LLM 寫程式的流派，只是後來 JSON 成為了業界標準。當然，當初不讓它寫程式的另一個痛點是：沒有一個安全的環境可以執行。

**既然如此，給它一個 Container（沙盒）不就得了？**

沒錯，現在就是這麼做的。

## 運作流程

在 Programmatic Tool Calling 的架構下，當使用者提出 Query 時，開發者會提供給 LLM 一個「程式碼執行（Code Execution）」工具，並將其他外部 API 設定為「允許程式碼呼叫（allowed_callers）」。運作流程就變成了這樣：

### 1. 編寫腳本
AI 不再進行單次、死板的 JSON 工具呼叫，而是寫出一段包含邏輯（如 for 迴圈、if 判斷式、陣列排序）的 Python 程式碼。

### 2. 沙盒內執行
這段程式碼會被送到一個獨立、安全的沙盒環境中執行。程式碼會在沙盒裡自動呼叫需要的 API、撈取資料。

### 3. 動態過濾 (Dynamic Filtering)
程式碼會在沙盒內部直接對龐大的資料進行運算、篩選與摘要。

### 4. 只回傳精華
最後，只有 print() 出來的簡短結果（例如：「最高營收的地區是西區，金額為 500 萬」）才會被傳回 AI 的 Context Window 中。

## 成果：準確率大幅提升

採用這種新方法後，LLM 的準確率迎來了大幅提升：

### BrowserComp 基準測試（網頁隱藏資訊）
- Sonnet 4.6：33% → **46%**
- Opus 4.6：45% → **61%**

### Deep Search QA（多答案尋找）
分數也有顯著的進步。

## 成果：Token 消耗顯著減少

另一個極有感的改變是 Token 消耗量顯著減少。由於大量無用的雜訊資料在沙盒階段就被 CPU 過濾掉了，根本不需要輸入給模型看：

- 平均減少 **24% 的輸入 Token**
- 極端資料密集型任務：節省 **80% 以上的 Context 空間**

### 注意事項

不過要注意的是，雖然最終「輸入」的 Token 變少了，總花費卻不一定會絕對下降。例如 Opus 4.6 就曾因為在過濾資料時「寫了非常多、非常複雜的程式碼」，導致它在生成程式碼這一步驟消耗的 Token 成本反而上升。

但整體而言，換取到的任務執行效率與絕對準確度，依然是極度划算的巨大升級。

## 核心價值：CPU vs GPU 的正確分工

**最核心的重點在於：我們終於將真正複雜且繁瑣的資料邏輯，轉移到了能效更高、更省電的 CPU 上，只把真正需要「語意推理」的精華資料留給 GPU (LLM)。** 不管怎麼算，這絕對是更省電、更省錢，也更省時間的做法。

總結來說，這項技術把 AI 從一個「被動接收海量資料的閱讀者」，轉變成了「主動派遣腳本去處理資料的系統工程師」。所有的髒活、累活都在沙盒裡用明確的 Python 邏輯解決完畢，AI 的大腦（Context Window）就能保持乾乾淨淨，專注於最終的決策與回答。

## 未來展望

這項突破極有可能會跟去年的 MCP 協定一樣，迅速成為全業界開發 AI Agent 的新標準。在 Sonnet 4.6 大放異彩之後，Opus 4.6 也已支援，相信其他科技巨頭很快就會跟上腳步。

這也讓我們再次看到 Anthropic 這家公司濃厚的工程師哲學：**不斷在底層細節著力，把大量運算的工作交給 CPU，真正需要 LLM 智慧的推理再留給 GPU。** 讓程式碼活在該活的地方，Context Window 也清爽無比，這絕對是 AI 發展上又一個非常大的突破！

---

## 待萃取重點

- [ ] Programmatic Tool Calling：讓 LLM 寫 Python 程式而非 JSON
- [ ] 傳統 Tool Use 痛點：海量原始資料塞進 Context Window（燒 GPU = 燒錢）
- [ ] 核心問題：為何要用 LLM 做 CPU 的工作？（排序、過濾、尋找取代）
- [ ] 解決方案：沙盒環境執行 Python 程式碼
- [ ] 四步流程：編寫腳本 → 沙盒執行 → 動態過濾 → 只回傳精華
- [ ] 準確率提升：Sonnet 4.6 (33%→46%)、Opus 4.6 (45%→61%)
- [ ] Token 節省：平均 24%，極端情況 80%+
- [ ] 注意：生成複雜程式碼可能增加輸出 Token 成本
- [ ] 核心價值：將資料邏輯轉移到 CPU，語意推理留給 GPU
- [ ] AI 角色轉變：從「被動閱讀者」到「主動系統工程師」
- [ ] Anthropic 工程師哲學：CPU 做運算，GPU 做推理
- [ ] 未來預測：可能成為業界新標準（如同 MCP）
- [ ] 金句：用 LLM 這把牛刀殺雞 vs Linux sort 指令
- [ ] 對比前篇 CPU 瓶頸文章：呼應 CPU 在 Agent 工作負載中的關鍵性

---

# 拆解結果

## A. 主脈絡與個人映射
- **論證骨架**：傳統 Tool Use 痛點（海量資料塞進 Context Window = 燒 GPU = 燒錢）→ 核心問題（排序過濾為何要用 LLM？）→ Programmatic Tool Calling 解法（LLM 寫 Python 在沙盒執行）→ 四步流程 → 準確率和 Token 節省的量化成果 → 收束到 CPU vs GPU 正確分工的架構原則。
- **個人映射**：對系統建造者最重要的洞見是架構原則——把資料邏輯歸 CPU、語意推理歸 GPU。這不只是 Anthropic 的產品功能，更是 Agent 系統設計的通用分工原則。

## B. 卡片（Zettel）

序號 1
- 標題：Programmatic Tool Calling：讓 LLM 寫 Python 取代生成 JSON，CPU 做髒活 GPU 做推理
- 類型：Pattern
- 概念（50–300 字）：傳統 Tool Use 的痛點：LLM 生成 JSON 呼叫工具，工具撈回海量原始資料全塞進 Context Window（如 Web Search 爬 10 個網頁全灌回去），處理這些資料就是在燒 GPU。Programmatic Tool Calling 翻轉了這個流程：LLM 不再生成死板 JSON，而是直接寫一段含邏輯（for 迴圈、if 判斷、排序）的 Python 程式碼，在沙盒（Container）內執行、呼叫 API、對資料做運算篩選，最後只有 print() 出來的精華結果回到 Context Window。排序、過濾、尋找取代是標準 CPU 操作，LLM 最擅長的是寫程式而非生成 JSON。成果：平均減少 24% 輸入 Token，極端情況節省 80%+；BrowserComp 準確率 Sonnet 33%→46%、Opus 45%→61%。
- 重要性（1 句）：這是 Agent 系統設計的通用分工原則——資料邏輯歸 CPU（沙盒），語意推理歸 GPU（LLM），兩者各歸其位。
- 邊界/反例（1–2 句）：Opus 有時寫過度複雜的程式碼，輸出 Token 成本反而上升——總花費不一定絕對下降。需要安全的沙盒環境，對內網或高安全要求場景有額外部署成本。
- 知識鉤子：是 #CPU成為Agent指令層 的解法之一——把更多有意義的工作交給 CPU；與 #Agent架構做空檢驗 呼應——這是一種「讓模型做它最擅長的事」的設計，符合 Bitter Lesson 精神。

## C. 連結建議（組裝藍圖）
- 內部組裝：此卡片 + CPU 指令層 + 能源戰爭 可組成「AI Agent 成本優化三層架構」（硬體層、系統層、應用層）
- 外部對接：與 Idx_3 的 AI 應用卡片對接（產品功能）；與 Idx_8 的系統架構卡片對接（CPU/GPU 分工原則）
