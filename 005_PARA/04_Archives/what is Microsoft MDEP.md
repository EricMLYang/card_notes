---
tags:
  - smart-space-solution
---
# what is Microsoft MDEP

MDEP stands for **Microsoft Device Ecosystem Platform**. It's essentially Microsoft's own flavor of Android, built on the Android Open Source Project (AOSP). 

Think of it like this: just as there are many different versions of Linux (Ubuntu, Fedora, etc.), MDEP is Microsoft's own distribution of Android.

**Here's a breakdown of what MDEP is all about:**

- **Android-based:**  It's built on AOSP, so it has the core functionalities of Android but with Microsoft's customizations.

- **Focus on devices:**  It's designed for various devices, not just phones. Think of collaboration devices like meeting room systems, smart speakers, and other peripherals.

- **Security and manageability:** Microsoft emphasizes security and easy management for IT administrators in enterprise environments.

- **Customization:** Device manufacturers and developers can customize MDEP to create unique solutions tailored to their needs.

- **Microsoft ecosystem integration:**  MDEP is designed to work seamlessly with Microsoft services and apps like Microsoft Teams, Azure, and Microsoft 365.

**Why did Microsoft create MDEP?**

- **Unified platform:** To offer a consistent platform for building a variety of devices within the Microsoft ecosystem.

- **Security and control:** To provide enhanced security features and management capabilities compared to standard Android.

- **Innovation:** To enable device manufacturers to create innovative solutions with Microsoft's backing.

**Key features of MDEP:**

- **Hardware-based attestation:** Uses Microsoft Public Key Infrastructure (PKI) to verify device identity and integrity.

- **Microsoft Secure Pairing:** Simplifies device pairing and connection to Microsoft services.

- **Customization options:** Allows manufacturers to tailor the platform to their specific hardware and software requirements.

**In a nutshell, MDEP is Microsoft's strategic move to:**

- Expand its presence in the device ecosystem.

- Offer a secure and manageable platform for Android devices.

- Drive innovation in collaboration and productivity tools.

If you're interested in learning more about MDEP, you can check out the official Microsoft documentation and resources:

- **Platform Overview:** <https://learn.microsoft.com/en-us/mdep/overview>

- **MDEP documentation:** <https://learn.microsoft.com/en-us/mdep/>

I hope this explanation is helpful! Let me know if you have any other questions.





MDEP in AUO

謝謝你的快速分析，幾個我看到的重點和兩位分享一下:1.     微軟這個架構開宗明義說，他是為 Video 和 Audio服務設計的，和 AUO 集團產品有強相關2.     架構圖顏色是有意義的，藍色區塊是微軟 MDEP提供的，從硬體底層架構往上慢慢越來越多，表示他主要在作 Platform Services 和 Application，單需要往下先埋入一些未來可以往上和軟體對接的的物件，並把這些’埋入’標準化，作為整合 Ecosystem的標準。這樣的策略和我們目前想要發展產品的方式很像，只是底層我們現在要完全靠外部Partner 來完成。

(當然這也有商務策略的考量，讓外部廠商也有’沉沒成本’，他們才會幫我們努力去推業務 XD)緊接著我們可能很快會面對一件事，就是要拿著友達集團的硬體及供應商的優勢，來作我們自己的 DEP，我暫時稱他為 ADEP (AUO Device Ecosystem Platform)。是不是會由我們來發動我不知道，但這是我近未來很想做的事。(其實可以試著把ABS在做的很多產品放進去看看，你會發現都適用)

3\.     你說的沒錯，架構清楚後，我們可以來找一個題目 POC，看看怎麼把各個位置內容填進去，最近 ADP 找我做透明顯示器的AI雙面翻譯機(他們覺得是新大陸，不過日本一年前就POB了 日本鐵道推出「面對面翻譯機」，提供12語言即時翻譯! - 電腦王阿達 ([kocpc.com.tw](http://kocpc.com.tw)))到時候看有沒有機會運用這個架構。

4\.     這個產品唯一面向的安卓+硬體的解決方案，又有微軟加持(branding)，是 EEBG的最愛(只要加入就能立即享受好處)。不過對 ABS 來說，可能要取代/修正大部分大家現在正在做的事情，老闆可能會有意見，除非有客人買單，否則還是我先自己享用就好。謝謝你的快速分析，幾個我看到的重點和兩位分享一下:1.     微軟這個架構開宗明義說，他是為 Video和Audio服務設計的，和 AUO 集團產品有強相關2.     架構圖顏色是有意義的，藍色區塊是微軟 MDEP提供的，從硬體底層架構往上慢慢越來越多，表示他主要在作 Platform Services 和 Application，單需要往下先埋入一些未來可以往上和軟體對接的的物件，並把這些’埋入’標準化，作為整合 Ecosystem的標準。這樣的策略和我們目前想要發展產品的方式很像，只是底層我們現在要完全靠外部Partner 來完成。(當然這也有商務策略的考量，讓外部廠商也有’沉沒成本’，他們才會幫我們努力去推業務 XD)緊接著我們可能很快會面對一件事，就是要拿著友達集團的硬體及供應商的優勢，來作我們自己的 DEP，我暫時稱他為 ADEP (AUO Device Ecosystem Platform)。是不是會由我們來發動我不知道，但這是我近未來很想做的事。(其實可以試著把ABS在做的很多產品放進去看看，你會發現都適用)3.     你說的沒錯，架構清楚後，我們可以來找一個題目 POC，看看怎麼把各個位置內容填進去，最近 ADP 找我做透明顯示器的AI雙面翻譯機(他們覺得是新大陸，不過日本一年前就POB了 日本鐵道推出「面對面翻譯機」，提供12語言即時翻譯! - 電腦王阿達 ([kocpc.com.tw](http://kocpc.com.tw)))到時候看有沒有機會運用這個架構。4.     這個產品唯一面向的安卓+硬體的解決方案，又有微軟加持(branding)，是 EEBG的最愛(只要加入就能立即享受好處)。不過對 ABS 來說，可能要取代/修正大部分大家現在正在做的事情，老闆可能會有意見，除非有客人買單，否則還是我先自己享用就好。

電腦王阿達

日本鐵道推出「面對面翻譯機」，提供12語言即時翻譯! - 電腦王阿達

全球旅遊業在疫情後全面復甦，日本更是成了國人出國旅遊首選。為服務外國旅客，日本西武鐵道七月份在東京西武鐵道終點新宿站安裝「面對面翻譯機」進行測試，獲得許多國外旅客的好評。日本西武鐵道「面對面翻譯機」是什麼? 以下做一說明:

Aug 6th, 2023 (66 kB)

<https://www.kocpc.com.tw/archives/504041>

Jot something down

想了一下，以 AUO 現況，我自己感覺這個才是需要投入，

我自己直覺想法如下(推理方式)：

1. 查了一下，硬體公司要往軟硬整合發展，有一個不錯個硬體產品應該是基本，
   但我們似乎講不太出哪個硬體很棒(面板以外)，或是說無法肯定的列出哪3個很
   棒的產品要優先 support，因為他們前景光明。

2. 但我們確實有很多硬體產品想發展，因此現況是根據種種原因，把軟體開發資源分配
   再一些項目上，希望他們變成解決方案

3. 但以上撒下去的方式很難抉擇，因為重壓一個硬體不確定性太高(產品失敗率本來就很高)，
   太分散又做不出效果 (幾隻沒絕對豐富經驗的人 support，做出來的東西很難競爭)

4. 以上種種考量下，以 MDEP 為基礎，發展一個多個硬體產品通用的平台，一旦平台是
   支持的，就保證產品有一定的競爭程度可以去攻市場，這樣似乎是最適合我們現在這種
   不斷買公司、發展事業群自己硬體產品、找供應商夥伴的現況

感覺要先盤出目前各事業群 / 子公司 / 關係夠緊密的外部夥伴間還不錯的硬體產品，

再以這些為基礎收斂方向，專注先發展 MDEP 支持這些產品加值應用的功能，

看看我們發展這個是不是能讓:

- 這一範圍產品都提升價值

- 未來找合作夥伴更有說服力(甚至是合作夥伴找我們)

- …

以下是一些小型硬體商或專注於特定產品類別的公司，成功逐步發展應用層或操作系統（OS）層生態系的案例，展示它們如何將硬體與軟體整合以擴大價值：

1. Sonos
   •	產品: 智能音響。
   •	策略: 開發 Sonos App，支持多房間音響控制和串流音樂服務的深度整合（Spotify、Apple Music）。
   •	OS 層生態: 音響內建專屬操作系統，提供高效的音訊處理和互聯能力。
   •	成果: 成為高端智能音響市場的領導者，建立了可與音樂服務商合作的多層次生態系。

2. GoPro
   •	產品: 運動攝影機。
   •	策略: 開發 GoPro Quik App，提供視頻編輯、雲存儲和社交分享功能，並支持訂閱服務。
   •	OS 層生態: 構建專屬固件和軟體套件，提升拍攝性能並支持配件生態。
   •	成果: 成功吸引專業和業餘用戶，延伸了運動攝影機的使用場景。

3. Ring (被 Amazon 收購前)
   •	產品: 智能門鈴和家庭安防設備。
   •	策略: 開發專屬應用，支持即時視頻監控、通知、遠端門鎖控制等功能。
   •	OS 層生態: 以低功耗硬體和專用固件為基礎，確保穩定的長時間運行和智能互聯。
   •	成果: 成為家庭安防領域的重要玩家，吸引 Amazon 收購後進一步擴展生態。

4. Eufy (屬於 Anker 子品牌)
   •	產品: 智能家居設備（掃地機器人、攝影機）。
   •	策略: 開發 Eufy Home App，統一控制旗下所有設備，並與 Alexa、Google Assistant 等智能助理整合。
   •	OS 層生態: 針對不同硬體類型開發高度優化的固件，確保流暢運行和長效電池。
   •	成果: 與其他巨頭產品競爭中找到利基市場，建立品牌忠誠度。

5. Garmin
   •	產品: GPS 裝置與智能手錶。
   •	策略: 開發 Garmin Connect 應用和 Connect IQ 平台，支持用戶活動追蹤、數據分析，以及第三方應用開發。
   •	OS 層生態: 建立專屬操作系統，確保設備高效運行並支持深度定制。
   •	成果: 成功在健康與運動市場占據一席之地，形成獨立生態系。

6. Razer
   •	產品: 遊戲外設（鍵盤、滑鼠、耳機）。
   •	策略: 開發 Razer Synapse 軟體，支持設備同步設定、RGB 燈光效果定制，以及雲端保存配置。
   •	OS 層生態: 通過模組化軟件結構，支持無縫硬體整合和遊戲體驗增強。
   •	成果: 成為遊戲硬體領域的標杆品牌，吸引忠實玩家群體。

7. Nest (被 Google 收購前)
   •	產品: 智能恆溫器和家居設備。
   •	策略: 開發 Nest App，支持遠程控制和能耗分析，並與其他智能家居設備集成。
   •	OS 層生態: 內建專用軟體，確保恆溫器的學習功能（例如自動調節溫度）。
   •	成果: 成為智能家居市場的先驅，為 Google 智能家居生態奠定基礎。

8. Wyze
   •	產品: 廉價智能家居設備（攝影機、燈泡、感應器）。
   •	策略: 開發 Wyze App，統一管理多種類別的智能設備，並提供訂閱服務。
   •	OS 層生態: 將通用硬體與優化的操作系統結合，實現低成本高效能。
   •	成果: 在價格敏感市場中快速崛起，搶占智能家居市場份額。

9. Pocketalk
   •	產品: 手持翻譯器。
   •	策略: 開發專屬翻譯軟體，提供即時翻譯功能，支持多語言數據庫更新。
   •	OS 層生態: 基於專用操作系統和翻譯引擎，確保即時翻譯效果和穩定性。
   •	成果: 成功在跨境商務與旅遊市場建立品牌知名度。

10. Crestron
   •	產品: 高端會議控制系統與智能家居設備。
   •	策略: 開發 Crestron Home 和 Crestron Flex 平台，實現智能設備統一管理與自動化場景設定。
   •	OS 層生態: 內建高效固件，支持設備間的低延遲通信和用戶自定義控制。
   •	成果: 成為商務會議與高端住宅市場的核心供應商。
   總結
   這些公司雖然規模較小，但它們在特定產品類別上逐步發展應用層和 OS 層生態系的成功，主要得益於以下因素：

11. 垂直整合：硬體與軟體的深度結合，解決特定痛點。

12. 細分市場聚焦：專注於小眾或利基市場，建立差異化優勢。

13. 用戶體驗驅動：以軟體提升硬體的價值，增強用戶忠誠度。
   這些案例為 AUO 等硬體公司提供了啟示，尤其是在細分市場中找到契機，逐步擴展軟硬整合的應用層生態系。