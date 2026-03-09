---
tags:
  - charging-master
---
# CGM - PM



- Algorithm

   - Adjustment The Weight

   - Change Priority Take Method

      - Now: Order by priority and dynamic modify contract limit

      - Then: Original Flow but just take enough car to ch

- Data Analysis (Charging Data & T-Box Data)

   - charging efficient data

   - 





## Business Expending Direction

Charge Pile + Energy Save is Good Business

AD ( Display ) on E-Bus

# 系統承接與維運計畫

## \[ 理解分工 \]

- 大原則：Eric, Cindy, 國豪 原則都要了解，其他人理解必要的部分

- 分工：

   - ebus-internalservice + EventHub + 演算法相關業務邏輯: Eric, 妙珊(演算法）

   - Container (Repo.),  Azure Devops Flow:  Eric, Cindy, 國豪

   - ebus-webhookservice + ebus-backend + 充電流程 : Cindy, 國豪 

   - ebus-adminportal + WAF +  使用者相關流程與頁面： 國豪、Jing

   - ebus-dashboard  + Phase 2 分析用到的數據理解: 妙珊、Eric



- 技術 - 前端: React.js Code

- 技術 - 後端 : Java 17 + Srpint Boot 3







## Communication

- Product Team 絕對是既定政策，老實說以目前狀況來說利多於弊(減少溝通成本+避免資源互卡+深化累積經驗), 建議的方法就是依據產品團隊發展流程，把缺的東西、要調整的東西、多的(無價值的)東西逐一盤點出來，然後把時間軸拉出來，讓S看的到目標，有時程去展望，才能依著你的步調走。

- 簡報太多思考不周，例如突然想到大南因為換車已經沒 T-Box 了，但整體方向的確是我自己真實想法，但那也是之後的是- 對實際在戰場打滾的我們來說，思考越接近實際，才能讓我們好好活下來(請參考諾曼第大空降BOB)，我們越浮，老闆們會更浮，大家最後就去雲端做仙了。

- 大南換車我們還是可以接 T-box資料，之後AUO 合作的車廠總瑩，也適用寶路的 T-box，先接有益無害。

- 充電樁未來，我可能還是會傾向目前系統歸獨立系統，後續把資料過到分析的環境去產生數據價值相關測試，類似之前資料倉儲收各個系統資料的做法，會比較單純

- 如果你是從資料倉儲的角度來看系統，是的，應該要分開，未來龐大的基礎分析資料有可能會拖垮系統本身效能，但 ETL要做扎實(質變、量變、時變)

- 雖然我對 Databricks 沒那摸了解，好歹我也拿著微軟執照的 SQL Server 專家，對於實時資料處理，Databricks 可能未必是強項，它的對外應用性，我也有很大的疑慮。

- 如果沒有商業或集團政策考量，我建議還是讓技術團隊做技術選型，以加快開發速率與保證開發品質。(不然我Day1就踢掉 MySQL，因為我以前被它處理資料binary code的問題搞死過 XD)



## 




