

【前言：Agent 時代的商業數據分析—技術演進與現實檢驗】

**核心結論**

Agent 架構的核心商業價值，並非推翻既有演算法或解決企業內部的資料治理問題，而是大幅降低「Time-to-Insight」以及「將分析結果對接業務行動」的摩擦成本。Agent 成功跨越了人機互動與分析交付的最後一哩路，但同時對底層資料工程（第一哩路）的容錯率降至極低。

**一、 過去數據願景的現實比對與 Agent 的介入作用**

過去 5–10 年圍繞現代資料堆疊（Modern Data Stack）所建立的願景，在 Agent 導入後呈現以下驗證結果：

1. **數據民主化與自助式分析：實質落地**
    
    - **過去瓶頸：** 傳統 BI 工具仍需使用者理解表結構與維度度量，資料素養（Data Literacy）門檻導致普及失敗。
        
    - **現狀事實：** 透過語意層（Semantic Layer）與 Text-to-SQL，自然語言正式取代圖形化拖拉介面。Agent 擴大了資料的取用性（Access/Delivery），這是目前最易量化、降本增效最明顯的商業落地點（如 Dentsu 縮短 80% 分析時間的案例）。
        
2. **公民資料科學家（Citizen Data Scientist）：遭降維打擊並被取代**
    
    - **過去瓶頸：** 企圖讓無技術背景的業務人員透過 AutoML 建構預測模型，實務上因無法處理特徵工程與防範資料外洩而難以商用。
        
    - **現狀事實：** LLM 內建的程式碼執行環境（如 Code Interpreter）使「建立模型」的需求轉移為「定義問題」。Agent 可依據自然語言自動編寫腳本並輸出檢驗結果，此舊有概念已無獨立存在的必要。
        
3. **數據驅動決策（DDDM）：部分推進，受限於不可解釋性**
    
    - **過去瓶頸：** 儀表板僅提供描述性分析（發生什麼事），極度依賴人類推導行動，導致儀表板疲勞。
        
    - **現狀事實：** 結合 Action Layer（API/Webhook），Agent 具備將數據指標轉化為自動化流程的能力（如客服分流、行銷觸發）。但因大型語言模型缺乏嚴謹的因果推論（Causal Inference）能力且具黑箱特性，在高風險或高價值決策場景中，仍無法完全授權 Agent 執行，需人類介入。
        
4. **單一事實來源（SSOT）：未被解決，且成為最大技術死穴**
    
    - **錯誤前提拆解：** 誤以為導入 AI Agent 即可解決企業異質系統的資料孤島與髒數據問題。
        
    - **現狀事實：** Agent 毫無資料清洗能力。若缺乏嚴謹的 Data Catalog、中繼資料（Metadata）與統一業務邏輯定義，Agent 強大的自然語言生成能力，只會加速產出具高度說服力的錯誤結論（數據幻覺）。嚴格的資料治理是 Agent 上線的絕對前置條件。
        


# Business Data Science × Agent：案例、分類與我的判斷筆記

## 核心判斷

目前看到的趨勢很明確：**Agent 的價值，通常不在於取代 forecasting、optimization、causal inference 或 ML 模型本身，而在於把這些能力從「產出分析結果」推進到「更快被取得、被理解、被接上流程與行動」**。因此，企業公開強調的成果，常常不是模型準確率，而是分析時間、time-to-insight、比較分析速度、resolution rate、ROAS、工時節省這類更靠近交付與執行面的指標。([Microsoft](https://www.microsoft.com/en/customers/story/19582-dentsu-azure-kubernetes-service?utm_source=chatgpt.com "Dentsu reduces time to media insights by 90% using Azure AI"))

---

## 幾家公司與案例的簡單定位

### Dentsu

Dentsu 是全球性的行銷、媒體與轉型服務集團，官方定位自己為全球企業的 growth and transformation partner。它用 Azure AI Foundry 與 Azure OpenAI 做出 predictive analytics copilot，讓 media insights 更容易被員工與客戶取得；公開成果包括 **analysis time 減少 80%**、**time-to-insight 減少 90%**，並且降低分析成本。這個案例最像「把原本分析能力包成更容易取用的產品介面」。([dentsu](https://www.dentsu.com/?utm_source=chatgpt.com "Integrated Marketing Solutions & Agency Services | dentsu USA"))

### causaLens

causaLens 是做 Causal AI / decision intelligence 的公司，近年的主軸已經擴展到以 causal reasoning 為基礎的 digital workers，官方也把自己定位成可建立、部署、治理 AI-powered Digital Workers 的平台，並強調在 regulated environment 與 enterprise decision-making 場景的可用性；其官方內容也明確主打 data science workflow acceleration，以及金融服務等高決策價值場景。這家公司代表的不是單純問答型 agent，而是更接近「進階分析引擎 + Agent 調用」的方向。([causaLens](https://causalens.com/?utm_source=chatgpt.com "causaLens: Reliable Digital Workers"))

### Salesforce

Salesforce 官方現在把自己定位為 AI CRM，並以 Agentforce、Customer 360、Data 360、Slack 等能力組成同一個平台。它自家案例最值得看的是：統一數據之後，Agent 不只回答問題，而是直接接進 sales、marketing、service 流程。官方公開的成果包括 **60% increase in marketing lead revenue and contract value per lead**、**85% resolution rate**、**98,000 fewer support cases projected**，以及透過 AI-powered Slack notifications 發現 **2300 萬美元潛在續約收入機會**。這是典型的「分析結果變成實際行動」。([Salesforce](https://www.salesforce.com/ap/?utm_source=chatgpt.com "Salesforce: The Customer Company | Salesforce AP"))

### S&P Global

S&P Global 是大型市場資訊與分析公司，旗下能源與商品資料服務本來就以高價值市場 intelligence 為核心。它把資料接到 Microsoft 365 Copilot 後，官方公布客戶平均可達到 **95% faster data extraction**、**98% faster comparative analysis**、**96% faster customer insights**。這很適合拿來當「高價值資料產品被 Agent 化交付」的代表。([S&P Global](https://www.spglobal.com/en/who-we-are/about-sp-global?utm_source=chatgpt.com "About Us"))

### Shell

Shell 是全球能源與石化公司。它公開的 AI 應用案例更接近工業與工程決策：例如管線腐蝕模擬比傳統 CFD 方法 **快 106 倍**，而某些 CCS storage site assessment 流程也可 **speed up by more than 60%**。這類案例展示的是：Agent / AI 價值不只在報表與客服，也可以進入實體流程、工程評估與 operational workflow。([Shell](https://www.shell.com/?utm_source=chatgpt.com "Shell Global"))

---

## 我對整體市場的整理：先分成兩張圖來看

## 一、這是「商業模式分類」，不是系統能力路線圖

### 類型 A：內部自助分析

重點是把原本 analyst / data scientist 才能做的事，變成更多內部使用者可直接取得的分析能力。Dentsu 就很典型。這一型最常對應的成果指標是 analysis time、time-to-insight、分析成本。([Microsoft](https://www.microsoft.com/en/customers/story/19582-dentsu-azure-kubernetes-service?utm_source=chatgpt.com "Dentsu reduces time to media insights by 90% using Azure AI"))

### 類型 B：外部資料產品 / 洞察產品

本質上和 A 類很像，底層都常是 NL-to-query、RAG、semantic retrieval、summary generation，但商業模式不同。A 類是內部降本增效，B 類是把高價值資料更好地商品化與交付。S&P Global 是代表。([Microsoft](https://www.microsoft.com/en/customers/story/25029-s-and-p-global-microsoft-365?utm_source=chatgpt.com "S&P Global Commodity Insights unlocks 95% faster data ..."))

### 類型 C：流程最佳化 / 工業流程自動化

這一型更靠近排程、監控、工程計算、風險判斷、physical system optimization。重點是讓模型與規則真的影響機器、工程、後台系統的流程。Shell 這類案例最接近。([Shell](https://www.shell.com/what-we-do/technology-and-innovation/shell-techxplorer-digest/2024-shell-techxplorer-digest--powering-energy-innovation-houst/_jcr_content/root/main/section/list_306812369/list_item_copy_copy__1604387742/links/item0.stream/1705305780621/9cb7af9c4d8c69e6fb24cd86b3c3c43c698622c1/STCH%20Digest_2024_Advancements%20in%20utilising%20AI%20to%20solve%20business%20problems_Lu.pdf?utm_source=chatgpt.com "Advancements in utilising AI - to solve business problems"))

### 類型 D：驅動業務行動 / 前台流程自動化

這一型是把數據、分群、預測、規則與 CRM / service / sales / marketing action 直接接起來。Salesforce 是代表。它不是只做 insight，而是直接推進 outreach、resolution、campaign、opportunity follow-up。([Salesforce](https://www.salesforce.com/ap/agentforce/?utm_source=chatgpt.com "Agentforce: The AI Agent Platform"))

---

## 二、這是「系統能力分類」，比較接近實作與架構

### 1. Access / Delivery Layer

這層解決的是：分析結果怎麼更快被取得、理解、比較、消費。  
代表案例是 Dentsu、S&P Global。  
常見技術核心通常是：metadata、data catalog、semantic layer、NL-to-query、RAG、檢索與摘要。  
常見成果指標是：analysis time、time-to-insight、faster data extraction、faster comparative analysis。([Microsoft](https://www.microsoft.com/en/customers/story/19582-dentsu-azure-kubernetes-service?utm_source=chatgpt.com "Dentsu reduces time to media insights by 90% using Azure AI"))

### 2. Analytical Engine Layer

這層解決的是：怎麼做更高階的判斷、what-if、counterfactual、decision intelligence。  
causaLens 比較像這一層的代表。它不是 Action Layer 的前置必經步驟，而是一個獨立的進階分析能力模組；Agent 比較像去調用它，而不是自己自然演化成 Causal AI。([causaLens](https://causalens.com/?utm_source=chatgpt.com "causaLens: Reliable Digital Workers"))

### 3. Action Layer

這層解決的是：分析結果怎麼真的去觸發流程、回寫系統、呼叫 API、通知人、推動下一步。  
這裡又可以分成兩種落地面：

- 工業 / 後台系統：偏 C 類，像工程評估、監控、最佳化流程。
    
- 商業 / 前台系統：偏 D 類，像 CRM、service、sales、marketing。  
    核心關鍵通常不是 causal inference，而是 orchestration、權限、事件驅動、系統整合、write-back。Shell 和 Salesforce 都屬於這一層，但面向不同。([Shell](https://www.shell.com/what-we-do/technology-and-innovation/shell-techxplorer-digest/2024-shell-techxplorer-digest--powering-energy-innovation-houst/_jcr_content/root/main/section/list_306812369/list_item_copy_copy__1604387742/links/item0.stream/1705305780621/9cb7af9c4d8c69e6fb24cd86b3c3c43c698622c1/STCH%20Digest_2024_Advancements%20in%20utilising%20AI%20to%20solve%20business%20problems_Lu.pdf?utm_source=chatgpt.com "Advancements in utilising AI - to solve business problems"))
    

---

## 我自己的判斷與偏好

### 1. Dentsu 型，是最適合先做的

原因不是它最終最強，而是它最容易先產生可見價值。  
它直接解決一個很常見的痛點：分析結果明明存在，但取得太慢、太靠專家、太難被業務端消費。  
如果目標是先做出有感成果，Dentsu 型通常是最快的切入點。([Microsoft](https://www.microsoft.com/en/customers/story/19582-dentsu-azure-kubernetes-service?utm_source=chatgpt.com "Dentsu reduces time to media insights by 90% using Azure AI"))

### 2. causaLens 型，是我最想達到的分析理想

這一型吸引人的地方，是它往 decision intelligence 靠近：不只回答發生了什麼，還逼近「為什麼」與「改什麼最有用」。  
但這不是從 Dentsu 型自然升級而來的下一站，而是另一條更高要求的分析能力線。它更依賴結構化資料、因果設計、評估機制與高品質業務建模。([causaLens | Pioneer of Causal AI](https://causalai.causalens.com/why-causal-ai/?utm_source=chatgpt.com "Why Causal AI?"))

### 3. Salesforce 型，是系統目標

這代表的是：分析結果最後要能接到行動。  
如果系統最後要有真正的商業影響，終局通常不是停在更好的分析介面，而是走到能夠推動 sales、marketing、service 或其他 workflow 的 Action Layer。Salesforce 的案例很適合當這個終局參考。([Salesforce](https://www.salesforce.com/ap/agentforce/?utm_source=chatgpt.com "Agentforce: The AI Agent Platform"))

---

## 指標與 Agent 角色的對應

### 當指標是速度、時間、比較效率

例如：

- 80% analysis time reduction
    
- 90% time-to-insight reduction
    
- 95% faster extraction
    
- 98% faster comparative analysis
    

這通常表示 Agent 的角色是：

- 分析入口
    
- 結果交付加速器
    
- 檢索、比較、摘要的互動介面
    

這一類比較屬於 **Access / Delivery Layer**。([Microsoft](https://www.microsoft.com/en/customers/story/19582-dentsu-azure-kubernetes-service?utm_source=chatgpt.com "Dentsu reduces time to media insights by 90% using Azure AI"))

### 當指標是 resolution、營收、ROAS、案件減少

例如：

- 85% resolution rate
    
- 98,000 fewer support cases
    
- 60% increase in lead revenue
    
- 2300 萬美元潛在續約收入機會
    

這通常表示 Agent 的角色已經變成：

- 決策輔助者
    
- 流程推進者
    
- 行動執行者
    

這一類比較屬於 **Decision / Action Layer**。([Salesforce](https://www.salesforce.com/ap/blog/salesforce-on-salesforce-unlocking-transformative-growth-and-roi-with-data-360-and-agentforce/?utm_source=chatgpt.com "How We Unlock Growth and ROI With Data 360 ..."))

### 當指標是模擬與評估流程本身被大幅加速

例如：

- 106 倍 simulation speed
    
- 60%+ assessment speedup
    

這通常表示 Agent / AI 已經進入：

- 專業分析工作流
    
- 工程決策流程
    
- operational workflow
    

這類屬於 **工業型 Action Layer / 流程最佳化層**。([Shell](https://www.shell.com/what-we-do/technology-and-innovation/shell-techxplorer-digest/2024-shell-techxplorer-digest--powering-energy-innovation-houst/_jcr_content/root/main/section/list_306812369/list_item_copy_copy__1604387742/links/item0.stream/1705305780621/9cb7af9c4d8c69e6fb24cd86b3c3c43c698622c1/STCH%20Digest_2024_Advancements%20in%20utilising%20AI%20to%20solve%20business%20problems_Lu.pdf?utm_source=chatgpt.com "Advancements in utilising AI - to solve business problems"))

---

## 最後的整理

我目前會把整件事記成下面這樣：

- **Dentsu 型**：先把分析結果變得更容易被拿到。
    
- **causaLens 型**：把進階分析能力做成獨立 analytical engine，讓 Agent 去調用。
    
- **Salesforce 型**：把分析結果接到真正的業務行動。
    

所以它們不是一條單一路徑的先後升級，而是三種不同層次的能力焦點：

- Dentsu 偏 **Access / Delivery**
    
- causaLens 偏 **Analytical Engine**
    
- Salesforce 偏 **Action Layer**
    

而我自己的偏好也很清楚：

- **近期最適合落地的，是 Dentsu 型。**
    
- **最想達到的分析理想，是 causaLens 型。**
    
- **系統最後真正想走到的，是 Salesforce 型。**