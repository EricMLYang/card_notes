---
tags:
  - llm-application
---
# LLM Application -  Deepseek 心得

最近社群被 DeepSeek 文章洗版了

對於我們只想專注在應用層的 AI Wrapper 來說，這消息帶有幾個重要意義：

1. 對於專注場域應用的業者來說，對於模型的理解不能像以前這麼被動，因為：

   1. 原本認為模型底層研究是白費力氣，因為大資本才玩得起，現在這壟斷的局似乎被打破

   2.  LLM in Edge 的想像空間又更具體一些，這需要對模型有比較深的理解才能用的好

2. 中國正式加入競爭賽局，模型性價比提升的速度應該會很顯著，這是應用層的大福音，但也不能太開心，因為便宜 AI 讓應用層競爭對手變多，且中國在應用層內卷的實力也很驚人



以下分幾個不特別連貫層面來寫心得：



1. AI 應用開發部分：

我個人會更在意 Databricks CEO 所講的，“比起通用的大型語言模型，企業往往更需要能穩定完成特定任務的專門模型，並且是成本上符合效益的，當這件事變成熟，其對企業的發展爆發是可預期的，即使目前模型都不會進步了，以目前的模型的能力來達成專門任務的穩定應用，都足以造成很大的影響。“

”大家都會呼叫 LLM API 時，企業獨特的數據跟客戶關係會變成獨特的優勢跟差異化，因此現有大企業要理解如何結合 AI 並善用自己 Data 會是重要的”

所謂企業獨特的數據，Scale AI CEO Alex 提到，現在 AI 還無法真正解決問題，因為訓練資料還缺少很多人類在特定領域的種種反復嘗試迭代、與客戶互動的過程、在不同工具間來回串接 … 流程數據，這些都是未來 AI 功能差異化的最重要數據源．

以上是應用價值的地板，而因為我有一點產業數據因果分析的背景，我個人認為我自己在應用的天花板會是將 LLM 結合特定領域的因果結構，所謂的因果分析可能就是至少比資料探勘所產生的關聯性分析，又衍伸更多因跟果的確認，這些部分是領域獨有的知識，另一部分是必須透過數據分析的過程中去建構，而數據分析同時也是目前 LLM 尚還難以直接從數據中直接 output 產生(未來一段時間也還看不到他能攻破)

我會認為這部分可行是因為聽到 DeepMind CEO Demis Hassabis 說他們在嘗試建構世界模型，因為多步驟的規劃需要更穩定、正確的連續輸出，而 LLM 自己尚難以達到，需要搭配一個對真實世界有正確理解的額外資訊來輔助，把這 scope 縮小的話，特定產業或領域的因果結構就是類似的概念



2. AGI ？

DeepMind CEO Demis Hassabis 對於 AGI 的非嚴格定義，其認為AGI 重要能力為是能否能自主提出假說，或是能夠提出高層次的抽象目標，

假說的部分在因果推論本身就很重視，因為所有關聯性的分析完成後，通常都要提出各種假說來確認因果關係，因此能夠提出好的假說的確是很多學者或顧問所認同的，

而高層次的抽象目標就不用多說，很多在公司上班的應該都會經歷高層或主管的高層次目標，這些目標會比較模糊就是因為我們就大概知道想去的方向，但具體怎麼走是完全未知，

Hassabis 認為真正的創意需要具備這樣的特性才有機會產生，而其對這樣 AGI 的達成方法，會是目前研究方法的持續演進（Transformer、RAG、推理…等），或是需要再一次類似 Transformer 的這種架構創新，他不是很確定，所以 DeepMind 兩種方式都投資，

如果是目前方法得持續演進就能達到高水準模型，那麼 AI 像電力的世界應該會提早到來，因為中國削價競爭的能力真的很恐怖，加上所有硬體都能配合目前架構去做更極致的優化，但如果再來一次架構上的創新，那麼美國應該又可以再次奪回 AI 龍頭話語權，因為晶片禁令的影響後面應該會越來越大，再加上美國已經有所防備，中國要再次跟上的難度會增加不少，



3. 最後還是回到個人職涯省思，以下兩點是我目前比較有感的：

- 沒有標準答案的業務要持續精進：

目前無論是多厲害的模型，其能夠靠 RL 持續精進的，大多是能夠有標準答案的領域，例如 Coding 編譯、數學解題…等，因此對於沒有標準答案的業務去精進是必然要努力的方向，例如英文，當模型語言翻譯能力已經非常成熟，那麼能夠實際去跟外國人當面交談溝通以便達到目的的語言能力就更顯重要，這個就算即時翻譯機多厲害，某種程度都難以被取代，

而我個人例子就是軟體業，coding 好像是個滿容易被 AI 攻破的領域，但談到架構、功能、體驗、成本、企業目標…等面向，這些需要高度協調或是獨特體驗的業務，也是短時間內難以被 AI 自動化的



- 慎選產業或領域：

因為有獨特的數據或客戶其價值會因為 AI 而被放大，當產業本身價值不高，或是你的數據本身不夠獨特，那這一段 AI 增值能產生的效益有限，因此你獨特經驗的價值當然價值也會有限，以我的年紀講這個似乎有點晚了，但好險我們（應該）還有幾年的時間，而且這世界通常不會是非黑即白的，這樣的工具演進還是會有很多灰色地帶，但我的小孩我就要好好的陪他一起去面對未來世界了





## \[近期所看的參考資訊\]

## **DeepMind CEO Demis Hassabis 預測 5 年內到達超級人工智慧、談 AI 助手、超級智慧與社會變革**

- <https://youtu.be/pfXblrns1_8?si=NvztnRgzlwzx3InX>

- LLM Ability: Reasoning, Hierarchical Planning, Long-Term Memory

- Hassabis 認為 AGI 重要能力是能否自主提出假說，因為這是產生真正創造力的關鍵

- 創造力三個層次：

   - 把所有現有知識做各種組合 - 目前 LLM 在做的

   - 超越現有認知: AlphaGO 第 37 手

      - 這個需要一定程度的搜索比較後才有機會產生

   - 自行提出假設、高層次目標…等全新的原創

- 能一步一步制定計劃，反覆嘗試直到找出最佳方案得能力，需要一定程度的準確穩定性，不然每一步都錯一點，結果會變得非常糟，因此程式或數學等每一步都可驗證的領域比較容易進行多步規劃，其他非這類領域就可能需要一個世界模型，也就是真實世界的運作模式(Gemini Project Astra)

- Hassabis 目前不確定是否需要類似 Transformer 的創新或是目前機制持續演進就可以達到他所謂的原創能力，其認為兩種都有機會，因此兩種都投入



## **Scale AI CEO Alex 談數據在 AI 扮演的重要性以及他看到的機會**

- <https://youtu.be/g3thVrYFA9E?si=o-FHPnzzLFkJpbnU>

- 目前運算能力的擴張是明確的，演算法在各大研究中心也持續被積極演進，而如果拿到或產生更高品質的資料來持續讓模型進化，也將是個重點議題，因為容易取得的資料幾乎都被用來訓練了

- AI Agent 很紅但關於 Agent 的 Data 卻很少，例如目前 AI 工具對於連續工具切換的操作都很差，你可能要查個資料、用 Python 畫個圖表、貼到 PPT 後下標題…等，當涉及當一連串的工具操作，AI 目前表現都很差，而這些紀錄都是最難被記錄下來的 

- 當人類在解決複雜問題時，整個思考脈絡中很自然會用很多工具進行不同動作，其間會思考一下，進行規劃後執行，整個流程在碰到問中後反覆嘗試，這些過程中非常多都沒被紀錄下來

- 數據的生產應該就要像工廠一樣被產出

- 如何更好的評估模型會是比較少被在意但是非常關鍵的議題，我們必須具體知道模型目前缺乏什麼能力

- 大部分企業都還是不知道該如何善用自己獨特的數據，請所謂的顧問公司來很多時候也只是做數據的搬遷動作，如果能善用這些數據並產生價值，會是未來企業的重點，例如銀行業，理專在跟顧客互動過程中的各種數據和內部報告是網路上根本找不到的，這些如果可以用來提升顧客體驗，其價值將非常高



# **我花¥3500评测变态AI编程工具Devin**

- <https://youtu.be/bFDs7HnPIbI?si=i3RlihhBOR7VqnHv>

- 整合了 編輯器、瀏覽器、Terminal、Github…等工具，並配合很不錯的交互 UI 和很好的過程監控紀錄系統，整個 AI Agent 的意圖有到位了

- 人在編程過程涉及到的小工具應用其實比想想中多，看 Lint 訊息、複製貼上、看日誌、前端非編譯的除錯…等，很多我們很習慣地小動作在 Debin 都無法進行，其整合看起來也是大工程

- 生成式 AI 的缺點在基本複製、貼上、增加、刪除…等動作完全顯露，例如我們要在一個大文本修改某幾行文字時，LLM 需要全部生成一次，而容易出錯又是 LLM 特性，這會造成很大的困難

- 用自駕車來比喻自動編程，讓我覺得非常有意思，他認為 Devin 離 L5 還很遠，而我想到的是在汽車整個封閉系統上要整合各種工具或子系統相對單純，而程式涉及到太多不同工具、框架、架構的快速演進，當你要完全自動寫程式時嘗試把這些工具都整合起來，但很快的又有很多新工具產生讓整合好的 AI Agent 又比須作變動，因此在這一方面的標準被制定前，可以被廣泛使用的 AI Code Agent 應該還是要一些時間才能實現

- 作者在產品開發環境，不敢一次讓 AI 生成超過 5 行的程式，因為堆疊起來所產生到問題怕會難以處理，但要快速 Demo 時這類工具就變得很好用



# **吳恩達探討 AI Agent 和代理推理的興起 | BUILD 2024**

- <https://youtu.be/osJuf_X9ibk?si=2Cc-BVj90q9Vmr35>

- AI 應用的 PoC 從以前要 n 個月快速縮短為 10，因為 LLM 不需要你再找數據、Label Data、訓練測試…等，但測試與評估得負擔會變瓶頸，因為很難想像我們要為一個 PoC 開始想 100 個合適的測試案例

- Agentic AI  的反覆迭代工作流程讓 LLM 表現大幅提升，例如 GPT3.5 用 Agentic AI workflow 表現會比 GPT4 還要好

- Agentic Orchestration Layer (EX: LangChain) 會讓 AI 應用變得更簡便

- LLM 目前都是被訓練用來回答人類問題，而未來會有更多模型行被用來針對特定工具的使用更優化

- 數據工程變得越來越重要，因為非結構數據產生價值的難度降低了，因此妥善管理資料重要性提高





## **最新估值 2 兆台幣的 Databricks，CEO 對 AI 產業未來展望**

- <https://youtu.be/oriIvbUwh2I?si=INLeR0TzVOYt1N02> 

- 大家都會呼叫 LLM API 時，企業獨特的數據跟客戶關係會變成獨特的優勢跟差異化，因此現有大企業要理解如何結合 AI 並善用自己 Data 會是重要的，而不是到處去做 PoC

- 複合式的多功智能系統的建立是達成應用品質最後一里路的關鍵，所謂複合可以是各種LLM、Machine Learning Model、Tool 的結合，而其中很關鍵的是我們要能可以評估整個系統的能力跟缺點，否則沒有改進的著手點

- 比起通用的大型語言模型，企業往往更需要能穩定完成特定任務的專門模型，並且是成本上符合效益的，當這件事變成熟，其對企業的發展爆發是可預期的，即使目前模型都不會進步了，以目前的模型的能力來達成專門任務的穩定應用，都足以造成很大的影響



## **++[Raymond Chang](https://www.facebook.com/profile.php?id=100093835564616&\__cft_\_\[0\]=AZW12I0zg13fUuYtymsc8_Oza3xf74-PRpLeAwW7xe1nUMqFO1MBp3UY964wIFGDFvSBLScTyBnAFZEYt-lzh1jyg2gMoFaSHwWG3-fIV5gmYUMbb-8ulPJtdqjc1GPovzEg0sjVnz4dx3spjD6gDxIrZoDO7IAjxiJSCQkuYQa2Kw&\__tn_\_=-UC%2CP-R)++**

- <https://www.facebook.com/share/p/1D3YxcD54Q/>

- DeepSeek為何震撼了OpenAI, Meta一眾大哥, 原因我已經分析過。但最大的貢獻, 是以幾乎不可能的超低成本及優化技術, 顛覆了市場對於算力價格的認知。直接打破壟斷的局面。



- <https://www.facebook.com/share/p/1Q5gZMGBT6/>

- DeepSeek-v3 在工程設計、通信優化、硬體需求分析等方面展現了極高的技術水準，尤其在 MoE 訓練中透過 PXN、IBGDA、Warp Specialization 和 DualPipe 等技術實現了資源的極致利用。

-  DeepSeek-v3 團隊所提出的獨立通信協處理器、統一 ScaleUp 和 ScaleOut 的網絡架構，以及基於簡單原語的通信接口，無疑為未來硬體設計指出了一條清晰的發展方向。這些設計不僅將減少應用程式開發的複雜度，還能讓計算資源得到更加高效的利用，進一步縮小硬體與軟體層面之間的鴻溝。在未來的分散式大模型訓練中，這些技術創新很可能成為新一代硬體設計的標準框架，並為大模型的訓練和推理帶來更高的效率和更低的成本。

- 同時他們對未來硬體的前瞻性需求也展現出對大規模分散式訓練系統演進的深刻理解。

- 未來硬體架構的設計勢必將朝著通信與計算解耦、統一擴展架構、簡單通信接口的方向發展，從而實現真正的計算瓶頸（Compute-Bound）



## **Stratechery - [DeepSeek FAQ](https://stratechery.com/2025/deepseek-faq/)**

- <https://stratechery.com/>

- In the long run, model commoditization and cheaper inference — which DeepSeek has also demonstrated — is great for Big Tech. A world where Microsoft gets to provide inference to its customers for a fraction of the cost means that Microsoft has to spend less on data centers and GPUs, or, just as likely, sees dramatically higher usage given that inference is so much cheaper.

- Another big winner is Amazon: AWS has by-and-large failed to make their own quality model, but that doesn’t matter if there are very high quality open source models that they can serve at far lower costs than expected.

- Apple is also a big winner. Dramatically decreased memory requirements for inference make edge inference much more viable, and Apple has the best hardware for exactly that. Apple Silicon uses unified memory, which means that the CPU, GPU, and NPU (neural processing unit) have access to a shared pool of memory; this means that Apple’s high-end hardware actually has the best consumer chip for inference (Nvidia gaming GPUs max out at 32GB of VRAM, while Apple’s chips go up to 192 GB of RAM).

- Meta, meanwhile, is the biggest winner of all. **[I already laid out last fall](https://stratechery.com/2024/metas-ai-abundance/)** how every aspect of Meta’s business benefits from AI; a big barrier to realizing that vision is the cost of inference, which means that dramatically cheaper inference — and dramatically cheaper training, given the need for Meta to stay on the cutting edge — makes that vision much more achievable.

- Google, meanwhile, is probably in worse shape: a world of decreased hardware requirements lessens the relative advantage they have from TPUs. More importantly, a world of zero-cost inference increases the viability and likelihood of products that displace search; granted, Google gets lower costs as well, but any change from the status quo is probably a net negative.

# **DeepSeek-R1 Paper Explained – A New RL LLMs Era in AI?**

- <https://aipapersacademy.com/deepseek-r1/>

- The paper we’re reviewing today eliminates, or partially eliminates, the supervised fine-tuning stage. Specifically, to train **DeepSeek-R1-Zero**, the first model presented in the paper, we start with a pretrained model called **DeepSeek-V3-Base**, which has 671 billion parameters. The supervised fine-tuning stage is completely omitted. To run reinforcement learning at a large scale, instead of using the standard reinforcement learning with human or AI feedback, a **rule-based reinforcement learning** method is employed.

- A key insight from the paper is the self-evolution process of the model, illustrated in the above figure. The x-axis shows the number of training steps, while the y-axis indicates that as training progresses, the model’s response lengths increase. **Through reinforcement learning, the model naturally learns to allocate more thinking time when solving reasoning tasks**. Amazingly, this occurs without any external adjustments.





## DeepSeek R1解析 — LLMs可以從訓練中自己學出推論能力!!

- **++[陳宜昌](https://www.facebook.com/ai.ycc?\__cft_\_\[0\]=AZWVPhmBOsajY8-OFut6odmNgCrlBznJ2T4nF7jhNsQaqL_tOpp2X8kdzlyY1rk1UsJdv1eDjjhSfjLtnysuUwT5bVA7uGnmoHSCJQHbDVRVAZhQgjkW0i2_0boK-aRl1MgEiGvx0eA_jINCzQCM_x7QB9p6BeRAzh33lMaHbdLmVb5xwb40IHP-wC0SJOle9CzFSW0xf_kpjYb37JxkZNXuyBu0-87V3yKm04KPHbYwrQ&\__tn_\_=-UC%2CP-R)++**

- <https://www.facebook.com/share/15wjMbcqpo/>

- 目前許多研究致力於實現類似 o1 模型的 Meta-CoT。共識上來說，這通常需要使用 RL 來完成。如果能夠在（抽象的）樹狀結構上進行搜尋，就能找到正確答案，同時也能搜尋到錯誤答案。

- 這樣的搜尋機制得以讓我們利用 RL 中的「正向回饋」與「負向回饋」進一步訓練模型：藉由對正確答案進行正向回饋，提升模型找到正確答案的可能性；同時，利用錯誤答案的負向回饋，減少模型生成錯誤答案的機會。這樣的過程能逐步塑造出一個更強大的推理模型。 DeepSeek R1 將這個概念推到極致——完全用 RL 讓 LLMs 自行學出推論能力，其做法簡單到令人髮指：

   -  Step 1 - 使用兩個規則來評價模型輸出：

      - 規則1是最後答案是否正確（如上所述）

      - 規則 2 是回答形式是否遵守 `<think> reasoning process here </think> <answer> answer here </answer>` 的結構。

   - Step 2 - 利用上述規則的評分，在 Pre-training Base Model 上進行大規模 RL 訓練。

   - Step 3 - 收割結果，其成效在多個指標下與o1相近。 研究發現，模型自行學出了 Meta-CoT，能夠產生近乎腦內思維的過程，這相當神奇。這個過程不需要 Process Reward Model ，也不需要 Monte Carlo Tree Search。