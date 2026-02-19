---
tags:
  - llm-application
---
# LLM Application - AUO GenAI Strategy

- 針對模型 Finetuning 應該是未來進行 AI 產品的必備能力，甚至要像蘋果一樣可以針對清楚的任務跟環境去進行自家 LLM 模型策略

- RAG 部分，光是詳細研究、實驗這兩個部份，就超越台灣大部分企業的 RAG 流程了，是一個必須要投入的方向。



- My Question:

   - 2025 不只是面板公司，沒有 AI 會變嗎? 有 AI 會變嗎?

   - 如果目標不變， AI 可以加值什麼?

   - AI 伺服器買貨的是誰?都在做什麼?

   - 場域解決方案很貼近人，人是不是已經很習慣 AI 了? AI 特點不夠會賣不出去嗎?要納入 AI 是我們的事嗎?

- George’s Question

   - 是否有需要訓練自己的模型?

   - 如果不要?要選哪個?大的選甚麼?小的選甚麼?

   - 如果要?要訓練甚麼類型的?

   - LLM是否需要落地?落地要做什麼?

   - 長文本的問題要怎麼解決?

   - AUO內外場域有甚麼是需要LLM解決的?



## <生成式 AI 如果變產品標配，不跟上會喪失產品競爭力嗎？>

    當汽車智慧座艙因為體驗好而變成購買汽車重要因素，你沒好的座艙將喪失市場，當手機筆電都開始納入 AI ，蘋果不得不加大速度跟上，不然產品極有可能漸漸喪失吸引力，而對 AUO 而言，車用 或 NB 導入 LLM 的主戰場也許不在面板，但在AUO 極力拉升營收占比的外場域解決方案可能有機會面臨 AI 沒跟上就落隊的問題．







## <邊緣運算持續成長，讓場域 AI 應用變普及>

外場域 AI 可能變成產品標配主要原因有: 

1\. 生成式 AI 是目前最廣泛被一般消費者接觸的 AI，因為大家可打開網頁就透過聊天機器人直接體驗，並且也有很多 AI 產品應用，像是生成圖片、自動簡報…等，更不用說後續 AI 大量進入手機跟筆電趨勢滿確定的，至少科技大頭目前都很積極推動，這樣廣泛接觸下，沒 AI 的體驗的產品確會處於劣勢．



2. 邊緣運算變成新顯學，研華說 2025 年有機會是原深度學習在 Edge 的爆發年，而生成式 AI 在 Edge 會慢一點，但包含 Nvidia 在內的企業也都積極在推動生成式 AI Edge 化，這讓之前大家期待萬物聯網所能帶來的效率、體驗…等，又重新燃起，而所謂場域解決方案中，場域智慧化本來就是很重要的一塊，因此現在不是 LLM 在場域能做什麼的問題，而是當 AI in Edge 趨勢沒錯， 到時候是變成為什麼你產品沒 AI 的時候，要追都來不及



3. 簡立峰老師說過，雲的業者其實很希望運算可以邊緣化，因為雲端算實在太貴了，而其他應用業者也有很大的成本、隱私、低延遲誘因讓 AI 就在 Edge 端算就好，基於者實質的誘因加上硬體、Edge 模型越來越成熟，雲 和  Edge 的 AI 應用體驗會越來越好，這就像大腦(雲)和其他四肢(端)，很多事件是等不及腦袋細想就要趕快反應的，但當需要那腦時，四肢可以只傳遞必要資訊(痛)，讓大腦決定後續要怎麼處理



以上是剛好呼應 LLM 落地問題，假設未來 3 年 LLM 在 Edge 只會越來越成熟，那麼基於 Edge 端優勢的話落不落地不會是問題，而是落地的模型能力越來越強的速率多快，有限的能力在場域能做什麼







## <有哪些場域是需要 LLM 解決的>

這題我倒是比較想用另一個角度切入，試想當現場的 ”四肢“ 都做的不錯了，也就是現場有感應器可收數據、有相關文件資料可供終端使用者使用、有好的語音模型可用，而所有數據都可以串在一起了，這時候如果導入 LLM，將可以很有彈性、極大化這些數據的應用，這時場景又很需要一個大面板來顯示資訊，那應該就是 AUO 要積極投入的方向．

EX: 會議室、餐廳廚房備料管理、試衣間入口、零售商店展示櫥窗…等

當場景有個輪廓，這時落地能做什麼就比較好討論，例如試衣間出入口可以讓顧客掃一下條碼，快速針對該產品去做一些資訊回覆，或推薦其他類似產品…等







## <是否需要訓練自己模型>

- 重新建構大型語言模型可以說是最冒險的舉動，這個就像重新蓋水電設施一樣，沒有巨頭的生態系就不太可能發生

- 根據現有模型 re-training 的話，我倒覺得未來某個時間點有機會，畢竟現在有很多研究在努力把現有模型縮小(表現不變)，或是能力面向限縮一點，但是變得很強，基於這前提下：

   - 當之前提到的某場域，也許有一定規模，而且也收了一些數據，評估後很值得導入 LLM 服務來升級產品，在相對小的規模針對特定數據 re-training 

   - 或是有些場域嘗試用現有 LLM API 導入後發現有市場，可考慮 re-training 模型來強化特定表現，提升體驗，甚至可以減少後續每月經營成本

- Fine Turing: 我認為 Fine Turing、RAG、Prompt Engineering 都是必備基礎能力







## <模型選哪一個>

只要你不是領頭羊，你又有不能落隊太多的追趕壓力，你就有誘因持續把模型開源，畢竟開源可以靠社群力量來快速理解應用上的缺陷，甚至有人會幫你補強，某種程度也在間接培養自己 User 和生態系，而且開源又可以持續搗亂一下領頭羊，

而我們可預期一段時間就會有不錯的開源 LLM，像阿里近期 Qwen2 開源模型號稱贏 llama 3，而且中文聽說很不錯，因此我覺得不用太深入糾結選哪一個，根據場景選一個大小合適，當時表現最好的幾個，重點是後續有新的出來我們可以快速反應（決定要用新的還是不用）







## <長文本怎麼解決>

- 這問題可能還不是很理解，如果是針對局部做彙整 QA， 那麼問題都會是 RAG 的搜尋能力，如果是長文直接做類似摘要的處理，那麼切完後分段可能還是最有機會的解法

- 但後續模型有個 Long Memory 和 Long context LLM 的研究趨勢，

   - **Long Memory LLM** 更側重於在多輪交互中記住和利用過去的信息，Open AI 努力實現超長的 Memory 技術讓 ChatGPT 更個人化，可以想像是另一種版本的 RAG，其搜尋內容是你之前的資訊

   -  **Long Context LLM** 則側重於在單次處理中能夠理解和生成長段文字，Google 有打算推出付費的 1百萬長 token 模型，

以上都還可以持續理解

- 



- Resource

   - <https://www.edge-ai-vision.com/>

   - Qualcomm Edge AI

## **The AI opportunity: Sequoia Capital's AI Ascent 2024 opening remarks**

![image 1.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%201.png)

![image 2.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%202.png)

![image 3.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%203.png)

![image 4.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%204.png)

### Two Part: 

- For Business: Base on ( Display+ GenAI +  Entention Algorithm) to think the Architecture

   - Self-Service Ordering Kiosk

   - Car

   - Smart Mobile

   - Kiosk: <https://kiosk.com/>

      - <https://www.isg.dev/wp-content/uploads/2020/04/software_for_kiosks.pdf>

- For Company Operation

   - SaaS AI

### Retail use case:

- 1\.Enhance Search and Upselling

- 2\.Social Media Customer Sentiment

- 5\.Conversational Chat Interface

- 3\.Supply Chain Optimization

- 4\.Customer Order Substitution

- 9\.customer-centric merchandising

![image 5.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%205.png)

![image 6.png](./LLM%20Application%20-%20AUO%20GenAI%20Strategy-assets/image%206.png)





1\. Enhanced Search and Upselling Prompts and interactions during search improve customers’ abilities to find what they are looking for during a shopping process. Upselling is a sales technique where AI can be leveraged to encourage more-expensive purchases or add-ons. Crossselling is selling a different product or service to an existing customer. Increased revenue (4): It helps customers and associates find the right products, based on the customer’s natural language and contextual inferences. Increased efficiency (4): It eliminates errors from current categorizations and filtering. Managed risk (4): Good execution should improve retention. It is possible that the retailer may have to admit to the customer that it does not have exactly what the customer is looking for. Nonfinancial value (4): It helps consumers achieve their highest levels of personal satisfaction through validation and availability. Technical feasibility (3): AI in retail has been progressing over the past five years. Now, there is greater ability to identify product attributes, as well as to leverage chat interfaces to improve use of natural language. Internal readiness (3): Digital commerce has improved the focus on master data management for products and customers. External readiness (3): Customers want better search options.





2\. Social Media Customer Sentiment Content discovery analysis is leveraged to quickly monitor customer and influencer social media content, spot trends and sentiments, and predict outcomes and inform future decisions. Increased revenue (3): Customer sentiment changes quickly, and if the retailer is more in line with customer sentiments, revenue will increase. Increased efficiency (4): This is a difficult process to continually update today. Managed risk (4): This is a way to catch early risks from shifting social media impacts seen in many retail and consumer goods companies. Nonfinancial value (4): It helps with environmental, social and governance (ESG). Technical feasibility (3): Predictive elements from GenAI will make it easier to prevent possible errors. Internal readiness (4): Retailers are struggling with current tools to keep abreast of the speed of change in social sentiment. External readiness (3): Consumers, governments and organizations are holding retailers more accountable for what they are saying and doing.



3\. Supply Chain Optimization GenAI content discovery in a globalized, data-driven business world enables efficient and sustainable flow of goods, components and materials. This improves predictions for sourcing and procurement, logistics, transportation, and collaboration with suppliers. Increased revenue (3): Execution of the basics, including in-stock availability, is a primary core competency and the foundation of sales. Increased efficiency (4): New models are required to ensure efficiency is achieved in the complex marketplace. Managed risk (3): Derisking the global supply chain is a significant risk avoidance tactic. Nonfinancial value (3): It enables better customer perception through inventory availability. Technical feasibility (3): Supply chains have available information and signals that can be leveraged to improve performance. Internal readiness (4): Retailers are hungry for optimization of supply chains. External readiness (3): Global uncertainty and legislative reactions across North America, European Union and Asia/Pacific are lingering.



5\. Conversational Chat Interface Conversational AI and virtual assistant interfaces interact with customers and associates, which may include facilitating a transaction. A key aspect is the enablement of human customers to converse in their platform of choice — whether that is the messaging platform, SMS, advanced virtual assistants (VPAs), social media or voice. Increased revenue (4): There are some early examples (Zappos), and customers are hungry for more accuracy from chat. Increased efficiency (4): Well-developed and wellcontrolled solutions that are trained on the retailer’s specific operations and products will create efficiency. Managed risk (1): This exposes the retailer to risk and must be closely monitored in the early stages. Nonfinancial value (4): It builds stronger perceived relationships with the customers. Technical feasibility (3): GenAI will help these solutions evolve to greater accuracy and flexibility to respond to more-complex chats. Internal readiness (2): There should be no major impact, but human associates must be prepared for customers who ask about previous chat interactions. External readiness (3): Customers are ready for better chat options.



6\. Associate Hiring, Onboarding It leverages content creation and discovery, large language models (LLMs), and natural language technologies to enhance associate recruiting and training through interactive experiences for individual associates. Increased revenue (4): Well-trained associates instore are a major contributing factor to sales success. Increased efficiency (3): Onboarding in the retail store is challenging, haphazard and timeconsuming. Turnover is high, and lack of training exacerbates the turnover issues. Managed risk (3): Knowledgeable associates operate at a significantly higher standard and will do a greater job of protecting assets. Nonfinancial value (2): It can improve retention and associate satisfaction. Technical feasibility (3): There are active use cases, including Walmart. But presently, this may be out of reach for many retailers. Internal readiness (3): Associates will quickly adopt this approach. External readiness (3): New associates expect more from employers



7\. Automated Text Creation GenAI language models create content for digital and physical marketing and merchandising activities, such as ad copy, product descriptions, product attribute identification and management of product information. Increased revenue (3): More-frequent and moreaccurate communications improve the customer response to offers and communications outreach. Increased efficiency (4): Retailers should expect significant impact from automation on the workforce, as human effort plunges and volume of content rises. Managed risk (1): This may increase risk in certain ways — for example, using copywritten material or accidentally making a mistake that will have an impact on the consumer. Nonfinancial value (1): This enables formation of stronger relationships, based on values and alignment with key customer groups. Technical feasibility (4): LLMs and interfaces like ChatGPT make this highly feasible in the near future. Internal readiness (2): There is potential for significant disruption in process and workforce that retailers must prepare for to make this a successful transition. External readiness (3): Customers are ready to receive these communications.



8\. Social Commerce Conversational commerce speeds up and improves success rates of social engagement in generating purchases as a result of a consumer-to-brand interaction on social media platforms. Increased revenue (3): Revenue from social media channels is increasing. Increased efficiency (3): More tools result in greater productivity. Managed risk (1): It increases risk exposure. Nonfinancial value (4): It improves relevance to customer lifestyles. Technical feasibility (3): Interfaces like ChatGPT have already shown better predictive capabilities for chat. Internal readiness (3): Retailers are hungry to grow social commerce. External readiness (4): Consumers are adopting social commerce at an accelerated rate, particularly in fashion, beauty and apparel categories.



10\. Personalization for Customers It improves the accuracy of the personalization process by leveraging content discovery and creation and helping LLMs and interfaces create relevant, individualized interactions between a company and its audiences to enhance the recipient’s experience. It uses insight based on unique recipient behavioral data. Increased revenue (3): Benefit will vary significantly across industry segments, as well as digital selling versus physical selling. Increased efficiency (3): GenAI will make personalization more possible by enabling translation, natural language and context. Managed risk (1): This may increase risk. For example, the level of personalization may feel inappropriate for some customers, and it will be very difficult to predetermine what may offend any one person. Nonfinancial value (3): It helps meet higher-level customer needs of loving, belonging and esteem. Technical feasibility (3): ChatGPT and similar interfaces have already presented ways to accomplish this. Internal readiness (3): Retailers already employ personalization techniques with limited success. There will be challenges with obtaining and consolidating accurate customer data from many sources. Retailers will also have to adhere to data security and privacy regulations and legislation. External readiness (4): Customers want personalized offers.



11\. Best-Fit Apparel Technology GenAI image search and generation models further improve the customer’s decision-making capability to select accurate products, based on shape, drape, fit and size, that enable satisfaction and reduce return rates. Increased revenue (4): Apparel returns are a major drain on profits. Customers appreciate the ability to see how things will look on their body types. Increased efficiency (3): The large return rates are a productivity issue in the store and warehouse. Inventory is shifted around to locations that it may not have been intended for and often isn’t placed back on sale. Managed risk (3): It varies from a risk perspective. If not successful, it could cause customer dissatisfaction. Nonfinancial value (2): Customers can feel more empowered and connected with the retailer. Technical feasibility (3): There are vendors today, and GenAI technology should improve the ability to customize models. Internal readiness (3): It’s not difficult from an internal perspective. External readiness (2): There are many concerns from customers who are reluctant to share pictures of themselves in undergarments or other forms of personal information. GenAI should help to alleviate some concerns.



9\. Customer-Centric Merchandising Content discovery and virtual assistants aid merchandising associates in determining products, services and experiences to be offered to customers, including substitutions and deletions at touchpoint, to maximize sales, margin, inventory and customer satisfaction. Increased revenue (4): Aligning merchandise assortments to customers through planning across channels and locations is, first and foremost, the preeminent way to improve inventory productivity, sales and profits. Increased efficiency (4): Merchandising and planning staff members typically require nearly the entire workweek to identify problems and opportunities, yet often only a small portion of those opportunities are addressed through some type of execution. Managed risk (3): Merchandising based on customer behavior models lowers the risk of inaccurate planning. Nonfinancial value (2): There is better alignment with customer behaviors. Technical feasibility (2): Many solutions attempt to do this today. There is a disconnect between business process and technology, as most retailers still use Microsoft Excel to manage planning and analysis within the category hierarchy. Internal readiness (2): Extensive process reengineering is required, as well as new skills, tools and so on. External readiness (3): Customers are ready for more-curated assortment planning that meets their needs.



12\. Product Development, Selection GenAI is applied to simulation, discovery and content generation for selecting and developing products for sale that align with customer needs and organizational sustainability goals. It includes processes such as digital prototyping, attributing and testing for products, and life cycle development. Increased revenue (4): All retailers select products to include in their assortment, while some develop products internally or with suppliers. Improving success rates for new products has direct sales and profitability implications. Increased efficiency (3): Speed is a top priority. Reduction of costs with digital prototypes can be a major time and money saver. Managed risk (4): Improved success rates for new products reduce risk. Nonfinancial value (3): Improved success for product development, less sampling and transportation, and greater production accuracy are all part of sustainability. Technical feasibility (2): Retailers have already been accelerating the use of digital product life cycle management (PLM) software and are seeking to improve performance in this area. Internal readiness (2): There may be resistance from creative resources. Retailers will need to improve collaboration with suppliers. External readiness (3): There is generally accepted opportunity across the supply chain.



13\. Automated Image Creation Image and video content creation is used for improved digital and physical marketing and merchandising activities, such as product development, display, messaging, signage and management of product information. Increased revenue (3): Conversion rates typically improve significantly when images are more realistic representations of products in various situations. Increased efficiency (4): Traditional means of image creation are very expensive and timeconsuming. Leveraging this ability will save production costs and labor. Managed risk (1): There is a low-level risk of copyright violation, but it is not significantly increased over traditional means of image capture. Nonfinancial value (3): Speed and flexibility of product and service offerings are greater. Technical feasibility (3): DALL-E and others are making this increasingly possible. Internal readiness (2): This will impact the process. But it’s not overwhelmingly disruptive, as it’s more about extending existing image management. External readiness (2): Customers are ready for this.



14\. Skills Management for Associates GenAI techniques evaluate and predict associate performance and track skills data. When applied to workforce management (WFM), it is used to automate skills-based workforce scheduling and generating operational and personalized training programs. Increased revenue (3): Retail requires a skilled workforce to effectively execute most required operational tasks. Labor is one of the largest expense areas for retailers, but an effective workforce is also one of the greatest drivers of revenue. Increased efficiency (4): By considering a worker’s complete skill set, organizations can align talent to work, while considering how the work will be completed, improving effectiveness and ensuring the right employee is doing the right task at the right time. This approach will enable workforce planning, inform worker skills development, and help to navigate talent shortages and changes to the nature of work. Managed risk (2): There are risks of training bias and potential litigation if it is not carefully administered. Nonfinancial value (4): It directly contributes to associates’ work-life balance and feeling of control. Technical feasibility (2): There are several uses in the market today. Internal readiness (2): Retailers require process change and face some legacy lack of trust. External readiness (2): It will feel natural for associates. Some labor law changes may be coming that impact how this use case is applied.



15\. Customer Behavior Modeling It deploys content discovery and knowledge management to improve predictive models about customers from internal and external data sources, for marketing, merchandising, digital commerce, supply chain and customer service. Behavior models provide a view of customers’ browsing and purchase activities, taking advantage of natural language prompts used by customers and associates. Increased revenue (4): Customer behavior models are pivotal for the future of retailing and, therefore, will provide tremendous business value when applied across many business use cases. Increased efficiency (3): Deployment of inventory, associates and other assets can be more highly targeted, leading to less waste. Managed risk (4): The accurate understanding of customer behavior improves sales and efficiency and will reduce business risk through early warning and ability to shift focus more quickly. Nonfinancial value (4): Loyalty has an indirect but vital impact on business value, and can be enhanced through better understanding and use. Technical feasibility (2): Data availability is still an issue and will be for quite some time. Internal readiness (1): Back-office processes today are not designed to be customer-centric, so much work will be required to achieve benefits. External readiness (2): Laws and regulations are shifting continually, and use of customers’ identifiable data is an ongoing question.



4\. Customer Order Substitution It uses content discovery and knowledge management, as well as simulation and prediction, to improve substitution satisfaction for customers when the desired or requested item is unavailable at the time of order fulfillment. Predicting and selecting the next best alternative items will satisfy customer expectations and save the sale. Increased revenue (2): Substitution should never be relied on as an operational mode. But when the requested item is not available, a likely substitution may save the sale, retaining revenue. Increased efficiency (3): Accurate and predetermined substitutions speed the fulfillment process. Managed risk (2): Customers have less dissatisfaction and less dissonance with what is substituted or with the lack of any alternative presented. When better managed, a substitution can change from a negative event to a positive event for the customer. Nonfinancial value (2): It leads to better customer satisfaction and a feeling of well-being. Technical feasibility (4): It is highly possible and is already implemented in some retailers, but GenAI will help make it more successful through better prediction. Internal readiness (4): It is not difficult to implement. External readiness (4): As long as required rates of substitution remain relatively low, customers prefer to have an alternative rather than nothing.



17\. Dynamic Pricing of Products Content discovery, knowledge management, simulation and prediction for experiences and related products identify the optimal price, based on real-time supply and demand, promotional cadence, competitors’ pricing, and customers’ behavioral profiles. Pricing for services, experiences and related products is dynamic, as it leverages inventory availability in the calculation. Increased revenue (2): Only a portion of items offered by most retailers will be priced dynamically. Increased efficiency (2): By leveraging inventory in the pricing decisions, it will make elimination of undesired inventory more possible. But present processes make this very inefficient. Managed risk (3): It reduces excess inventory. Nonfinancial value (2): It offers a faster response to the marketplace. Technical feasibility (2): In-store execution is a problem due to in-flux customer interactions, signage and shelf edge label requirements. Internal readiness (2): Presently, this is not part of the regular business process for most retailers. External readiness (2): There are many varied jurisdictional legal requirements around pricing.



18\. Immersive Retail Experiences GenAI creates immersive shopping for customers in physical, virtual or combined environments. It includes the physical store and digital touchpoints or emerging virtual realms. Increased revenue (2): The impact varies substantially by industry segment. Home furnishings and improvement are major categories today. Its application in food or consumables is less clear. Significant changes in revenue are unlikely in the next few years. Increased efficiency (1): Immersive experiences are likely a drain on efficiency at least in the short run. Managed risk (2): As a new channel, it represents significant potential risk. Nonfinancial value (2): It moves retailers toward co-creation, which provides the customer with greater ability to self-actualize. Technical feasibility (2): It is improving, but still has some way to go. Internal readiness (1): Process change, associate readiness and skills are in question. External readiness (3): Recent research from Klarna indicates that 81% of Gen Z and millennial consumers believe augmented reality (AR) will enhance the physical shopping experience.



19\. Real-Time Pricing GenAI simulation and digital twins will enhance retailers’ abilities to manage and adjust item pricing, personalized for customers in real time, across all channels, leveraging the customer’s mobile device. Increased revenue (3): Customers expect pricing consistency across channels, but changing physical store prices at the same frequency as digital prices is impractical and creates a dilemma. Increased efficiency (2): At least initially, this may seem more difficult. But by removing manual price overrides, it is more efficient. Some customers are still having issues with use of mobile devices in stores (for example, Kroger struggling with mobileonly offers). Managed risk (2): This has to be carefully managed, as profitability can be negatively impacted. Policies must be revised. Nonfinancial value (2): It improves customer trust. Technical feasibility (1): It will require more instore use of the customer’s mobile device during check-out. Internal readiness (1): More pricing changes have implications on business processes and profitability. External readiness (1): There are some legal compliance issues that vary by jurisdiction. Some customers are comfortable using mobile devices in the store for coupons and transactions, but many are still not ready.



20\. Co-creation of Products Content creation, simulation and design alternatives enable customers to share personal preferences through co-creation of products, services and experiences in physical and digital realms, including the metaverse. Increased revenue (2): Custom products can usually enable retailers to demand a premium price. There is an opportunity to create new sales touchpoints for digital immersive experiences and non-fungible tokens (NFTs). Significant revenue opportunities are limited for the next several years. Increased efficiency (1): It is very difficult for the retailer to execute at any scale. Managed risk (3): There is a risk to brand integrity. Nonfinancial value (3): It helps meet customers’ needs for self-actualization through co-creation. Technical feasibility (2): GenAI is required to make this a real possibility. Internal readiness (1): Retailers generally approach customers as a mass opportunity, and this will be difficult to absorb in the current business processes. External readiness (1): Klarna recently reported that 43% of Gen Z customers believe that virtual shopping will surpass physical shopping in the next two decades. Ownership of intellectual property is an issue.



## 錢哥問題

如果是以這一波 LLM （大模型）為主軸的話，這一波的特性是

- 基礎設施：

   - 模型偏大，需要一定的基礎設施，通常會在雲端，並且要配合一些搜尋引擎…等基礎設施，但私有雲或是地端方案持續在演進中

   - 內部數據(資料）整合很重要，應該也是最耗時的基礎工作，有數據 LLM RAG 才能發揮作用，但牽扯到數據就會有內外部雲和資安隱私問題，這個規矩大家還在訂

- 易用性 ：

   - 只要一個 API 就可以用到很多面向，讓終端 User 很快比以前有感

   - 代理人的相關工具高速演進中，後續會看到更多替你完成任務的工具

- 實際用途：基本上針對企業現有流程，找到 LLM 應用點，去優化他是後面很多企業努力的方向，你就把 LLM 想像成人力，把任務拆解後，針對這個人的特性去找到他可以作用的，並且可以取代員工作低價值工作的時間，或是加速原本費時耗人的動作



根據以上特性，你的問題：



**Q1  AI部門的組織架構**

**開發模式(集中/分散)以及選擇原因**

- **要有資安相關案 Infra 相關的集中 team 來引入或建構一些基礎設施，並制定一些資安規則**

- **其他逐漸分散式開發模式**：找幾個指標試點團隊，放入一些人來做 DEMO, 內部比較熟了就開始採用個團隊都埋一些人的方式



**為了發揮AI部門的價值和執行策略分工，如何確保不同功能單位能夠有效合作？**

**應該包括哪些角色支持公司數位轉型的推動？**

- **企業流程優化會涉及跨部門(光整合資料就要了), 基本上高層不先支持，玩不下去**

- 部門主管

- AI Infra 要先有好的工具出來，流程優化 DEMO 要看見一點效益，大家看到有用就會比較願意投入

---





**Q2  如何制定企業AI管理章程的參考法規及準則？**

**尋求有關企業如何依循外部法規、標準及內部政策**

- 還沒有標準，大家都還在訂

**AI管理章程制定是否參考國際標準？由哪個單位負責制定執行？**

- **負責單位**：資安 Team，還沒有標準，大家都還在訂

- 

---

**Q3  AI部門的職掌範疇**

**長春此部門的核心職責範疇，哪些具體的業務領域和流程需要此部門的參與？**

要對 LLM 怎麼用以及配套工具要熟,有能力聽完需求後，用現有工具快速讓部門試用，確認應用點後才找相關開發資源





---

**Q4  AI部門需求核心能力與人力配置**

**想了解該部門所需的技術、管理及業務知識等核心能力**

- **技術能力**：

   - 數據工程師比以前重要一點

   - LLM 應用工具包(API, Prompt, Search, Embedding …)

**是否有特定技能需要特別培養？**

- **有一點 NLP 或建模概念比較好，但基本上數據工程或是雲端工具的知識會更重要**

**每個團隊的規模、專業背景和人員分佈，是否引進外部專家支援？**

- **看狀況，但數據工程師和懂 LLM 的人都要有，最好搭配一個可以建構 DEMO 系統的 Team**



---

**Q5  AI部門與其他單位協作模式、扮演角色**

**了解該部門與其他業務單位如何協作，如何在跨部門專案中發揮橋樑作用？具體扮演什麼樣的角色來協助其他部門推進數位轉型目標？**

- **快速協助 DEMO 試用，不斷‘嘗試找到真正效益點**

- 

---

**Q6  部門績效與KPI**

**如何訂立這個部門的KPI？**

**這個部門的績效該如何評定？**

- **初期使用率，後期流程優化效益指標要出來**

- 

---

**Q7  如何讓此組織保持對新技術的敏銳度與適應性**

**如何確保數位轉型部門能夠持續關注並快速適應最新的技術發展，並將其有效整合進現有的業務流程？**

**應該採取哪些策略來促進技術的創新和更新，以保持企業在競爭中的優勢？**

- **工具演變非常快，中心 Infra Team 的目的也是持續演進工具**



---

**Q8  中鼎對於AI新技術策略與未來Roadmap**

*中鼎不是顧問工師嗎，你跑去我土木的領域喔*







應該這麼說，我還是假設目前講的 AI 就是 LLM, 以下我自己覺得比較合適：

1. 模型和工具變動很快, 要有人持續理解並引入新的工具( 應該會越來越好用，雲端工具很多）

2. 一個理解公司資安重點的人，持續滾動公司的應用安全

3. 懂得下 prompt, 知道怎麼用 LLM 效果比較好的人

4. 一個知道 search, 向量 DB, 數據處理的工程師 (應用上很重要）

5. 可以快速建構整個應用的軟體工程人員, 尤其前端，因為要有基本的體驗效果

以上規模小可以一人多功，規模大看要怎麼分工，3,4,5 應該可以慢慢讓各自團隊去培養人，整個目標就是產出完整的 DEMO 應用，確定有用就想辦法技轉到負責單位，中心保持 1,2 3 的研究



內部應用的話，就由單位相關 IT 來跟中心接洽，可以讓單位 IT 出一些 4,5 的人+ 理解業務的人，來把應用建構出來，初期速度看效果為主，有用再考慮建構比較大的系統



隸屬那單位，就至少要有一點話語權，如果是全公司要發展，掛數位長比較合適



但以上是我自己的看法啦，不一定是對的







有幾個組織面的問題再請教啦！ 大大有空再說！

1. Ai中心的人員組成是有 資安 ，應用開發（網頁 app)，數據工程，模型算法，infra (熟網路 雲端服務）嗎？

2. Ai中心隸屬 數位長轄下？

3\.需求單位提出後交由試點團隊與ai 中心合作嗎？例如：製造單位的製程系統要加入llm 功能，由製造向mes 提出，再由mes 跟ai 中心合作完成嗎？

1. ai 中心職責為尋找適合模型或解決方案，並提供落地的方法（api 或整體解決方案輸出）？