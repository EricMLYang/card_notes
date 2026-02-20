# AD Audience Viewing Profile

## \[ Goal \]

- Verify/Confirm that in-store advertisements in convenience stores effectively boost product sales

- Main AD:

   - 全家咖啡廣告   ( Let‘s café、單品咖啡)

   - 霜淇淋廣告

   - 義大利麵廣告   ( FamilyMart_UnoPasta )

   - 品牌形象廣告

- Analysis Result:

   - 整理出 AD 有顯著姓的觀看輪廓，讓客戶可以比對內部銷售數據



## \[ Data \]

- Each audience watch record with watch duration ( second )

- convenience store location

- watch date and time



## \[ Method \]

### Cluster:

1\. 階層式分群: 適合在不確定要分幾群的情況下使用

- EX: 觀眾分群

   - 依據行為數據（觀看次數、互動率）

   - 逐步合併相似的觀眾群

- 優點：

   - 可視化樹狀圖，直觀理解分群

   - 彈性決定群數，不用預先設定

   - 呈現資料的層次關係

- 實務建議：

   - 先標準化數據避免尺度影響

   - 觀察樹狀圖決定合適的群數

 3\. PCA

PCA在廣告分析中的主要應用：

特徵降維

將多個相關指標壓縮成少數幾個主成分

例如：觀看時長、點擊率、完播率 → 綜合互動指標

簡化資料，保留關鍵信息

發現潛在模式

找出最能解釋資料變異的方向

理解哪些特徵最具影響力

發現指標間的關聯性

視覺化分析

將高維數據投影到2D/3D空間

直觀觀察觀眾群或廣告的分布

識別異常值和群集

實務應用

建立綜合評分機制

簡化分群分析的輸入

降低模型運算複雜度

需要更詳細了解某個特定應用嗎？例如如何使用PCA結果建立廣告效果的綜合評分？

4\. 关联规则学习 (Association Rule Learning)


