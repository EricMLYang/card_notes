---
tags:
  - general-ad-play-platform
---
# PM - Family Digital Signage AD

## \[Main Question\]

- AD Business: What factors lead ad channels and advertisers to select our ad mediation services, rather than establishing direct agreements?

- Channel: Data Really Value

- Some Data:

   - 遠傳<https://www.fetnet.net/content/cbu/tw/digital-services/media-biz-service/index.html#product_02>

   - 中華電信<https://www.cht.com.tw/home/enterprise/businessapplication/bigdata/856>

   - 台灣大哥大<https://www.tamedia.com.tw/>

   

   **統計數據：** 例如特定區域的人口密度、年齡分佈、性別比例等。這些數據經過彙總處理，無法追溯到個別用戶。

   **趨勢分析：** 例如特定時間段內的人潮移動模式、特定事件對人流的影響等。這些分析著重於群體行為的變化，而非個人軌跡。

   **地理空間資訊：** 以匿名化的方式呈現特定區域的用戶密度或移動熱點，例如以網格或熱力圖展示。

   **行為特徵群組：** 將具有相似行為模式的用戶劃分為不同的群組，例如具有相似App使用習慣、網站瀏覽偏好或消費能力的群體。這些群組不包含任何可識別個人的資訊。

## \[ Task \]

- [x] Digital Signage - System

   - Databricks & Local Solution

   - Dashboard: Current System, Databricks Dashboard,  Plotly Dash 

- [x] Digital Signage - Analysis Plan 

   - pySpark Repo.

   - Schema Design

   - Analysis Flow: Auto Parser Information

- [x] AI Tiger Team Topic - Story ( PPT ): 

   - AI Agent Protocol 

   - Take AD video content → get AD feature 

![image 112.png](./PM%20-%20Family%20Digital%20Signage%20AD-assets/image%20112.png)



## \[ Project Management \]

- New Milestone

   - 目的：驗證廣告對商品轉換率的影響

   - 方式 ：給定廣告，每月分享數據，與全家數據 Team 交流成效

- Further Milestone:

   - 合約, 會員分析 Team 合作

## \[Analysis Meeting Record\]

1. 跟 4 位行銷部開會(部長不在)，討論滿順利的 客戶對我們 Dashboard 認同，對我們後面開始畫圖、找insight 也認為有感覺，是對的方向， 因為客戶看懂我們分析(特徵)想做什麼，所以後續會提供他們自己的標籤當作特徵

2. 下次 Milestone:  

- 3/26 想給部長定版分析方向

- 給一個修改後的Demo Dashboard

- 分析部分希望看到不同廣告自己特別的觀看 Pattern

- S4M 業務會針對 3/26 討論結果開始推進合約討論

1. 重點:

- 客戶盡快給我們 Dashboard 後續討論的回饋

- 客戶希望有觀看率 ( 觀看/人流)，下周跟 S4M 討論一下，我們要有一周開人流模式(當人流基準)

- 認定是人流或觀看的秒數重 3秒改成 1 秒，對廣告而言認定寬鬆是可以的
   ( 請S4M 幫我們跟 AMC 約個會， 確認一下 1. 重複抓取會不會變很嚴重   2.為什麼現在還是有 3 秒以下的數據?)

- 討論後續數據撈取規劃

1. 分析 & 報表:

- 指標先以: 觀看數、觀看率( 觀看/人流)、觀看秒數  為主 (完成率先不用 )

- 全家會提供的店標籤: 正副商圈、地標(200公尺內有什麼設施)、店來客跟客單標籤

- 廣告平均觀看幾秒、那些狀況高於平均資訊他們很喜歡

- 希望看到不同廣告的指標明顯差異

1. 進階課題: 要有一個 400 家觀看指標怎麼回推所有母體觀看數的評估方法 ( 給區間 )

2. 客戶 End Game: 未來可以針對廣告特性建議播放排程



## \[ Business Record \]

- Stakeholders

   - Client: Taiwan 全家便利商店 ( 母公司 is 日本 伊藤忠商事 )

      - 廣告銷部門

      - 數據單位是: 會員數據創研部

   - Supplier: S4M, 賣螢幕, AI 影像偵測設備, CMS 播放系統, Beacon

   - ABS: Analysis Support Team 

-  分析相關

   - 全家接受觀看指標、廣告標籤、受眾分群、店的觀看輪廓 

   - 較重視廣告提升店內商品銷售效果，賣廣告次之

      - EX:  某些店受眾比較會看健康食品，後續挖掘店的會員年齡偏高，健康食品消費也確實偏高 

      - EX:  年前年貨賣較好的跟賣不好的的店，會看年貨廣告的差異

   - 廣告標籤 Q3 才有機會正式上，只能先用預設類別標籤，請 ChatGPT 靠廣告名稱判斷

   - 期望 400 台 Camera 數據可推測，其他要再多裝幾台，分析效益提升較多

      - 備註:  全家母公司是裝 1/3  ( 1 萬家裝  3000 家)

## \[ Question \]

### AI Demo 方案建議

基於以下情境，請提出 AI 功能演示的 20 個可行方案，並仔細評估後，幫我挑出 5 個，每個簡短說明跟提出建議原因，挑選的優先順序是:

1. 目前 Demo 紹不要太過即時，因為 Mac Mini + LLM 無法非常快回覆

2. 有機會 2個月內 Demo，6個月內有機會在客戶店家 PoC

3. 應用價值: 可增加銷售、推薦...等價值都很高

4. 隨著軟體應更成熟，服務會越來越好，生態圈會越來越穩固



### AI 長期技術發展

根據以下情境，如果我希望能讓客戶很直覺的知道我們 透過  更個人化的內容推薦 的技術發展，達到讓客戶 獲得 Enhance Search and Upselling  的好處，我該怎麼用一頁 PPT 說明? 是用一個商店顧客的角度來舉例我們能做到什麼事嗎?

## \[ Background \]

### 基本情境

- 我們原本是 CMS 播放系統服務商，近期在測試 AI Camera 觀看分析服務，我們想持續增加我們對於客戶場域的解決方案價值

- 客戶場域: 台灣全家連鎖便利商店

- 超過 2700 店有裝設 Digital Signage，目前都安裝在結帳櫃台的正上方，可以看到顧客結帳

-  選 400 店 安裝 AI Camera 於 電子看板下方，可偵測多少人走進到框選範圍，多少人正面對螢幕

- AI Camera 只偵測人臉和五官，目前用SORT 演算法計算人流，用五官角度判斷正對螢幕

- 目標: 

   - 讓客戶滿意我們的 AI Camera 效果，跟我們訂閱數據分析服務，並持續安裝新 AI Camera

   - 以解決方案角度，持續提供現場有價值的新軟硬體服務，如 Beacon、LLM 應用、其他 AI 應用



### AI 功能演示

- 目標: 

   - 提供零售客戶更多有價值的方案

   - 建構我們自己的 AI 服務生態圈，於 AI 應用不落後

   - Demo 是基於目前硬體限制去測試可能應用，未來產品應該會用更產品導向的軟硬體

- 目前可用元素:

1. LLM:  Qwen 2.5-Omni-7B Model in Mac Mini

   - 程式流程:  抓現場影像讓 LLM 進行描述

2. 廣告分析系統，可給予某店家的廣告觀看輪廓

   - ( EX: 觀看率  20%，集中早上觀看， 常看咖啡廣告...等)

3. CMS 廣告影像預處理: 把廣告進行各種標籤與描述，未來可以跟觀看輪廓、現場描述進行聯合分析



### 長期技術願景

Gartner 報告，在零售領域，Enhance Search and Upselling 是最有價值的應用方向，我們期望以此主軸發展技術

我們暫定以 "更個人化的內容推薦" 為主軸，來發展技術，因為:

- Enhance Search and Upselling 有賴於此技術，例如辨識顧客身分、輪廓..等資訊後，推薦合適的商品、廣告...等資訊 

- 因為我們有廣告觀看分析的 PoC 在進行，我們認為針對受眾觀看輪廓去推薦廣告，本質上是 更個人化的內容推薦 的應用

- 未來可以衍伸到商品推薦

\-目前我們是透過 AI Camera 理解顧客、電子螢幕讓顧客看到廣告或資訊，未來我們的方案可以納入 Beacon、其他影像 AI ...等來更了解顧客，加裝聲音播放...等來跟顧客接觸



### Inference Population, Similar Store:

連鎖商店中，所有店都有安裝電子看板播放廣告，挑選其中 N% 安裝 AI Camera 進行人流、觀看行為統計，期望給予一個價值明確的提案，讓連鎖商店主管知道，隨著安裝的 N% 越多，整體數據的利用價值越高，例如:

1. 樣本回推所有店的觀看、人流，樣本越多誤差區間可以縮小，越來越明確

      例如：**FPC (Finite Population Correction)** 或稱為**有限母體校正因子**

2. 建構人流觀看行為特徵，與所有店都有的特徵關係，進行分群或相似性建構

       例如:  觀看行為特徵( N% 才有)，與商圈位置特徵(全部都有)，讓 AI Camera 數據最大化


