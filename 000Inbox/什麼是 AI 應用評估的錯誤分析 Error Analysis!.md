# 什麼是 AI 應用評估的錯誤分析 Error Analysis?

[ihower](https://ihower.tw/blog/): 

<https://ihower.tw/blog/12960-ai-evals-and-error-analysis>



最近在上 [Hamel + Shreya 的 AI Evals For Engineers & PMs 課程](https://maven.com/parlance-labs/evals)，這應該是市面上最深入探討 AI 應用評估的課程了。以下根據網上有公開的內容，整理一篇精華內容(大約是課程的前1/4內容)。





## **為什麼 LLM 評估這麼難？**

傳統的機器學習評估方法在 LLM 時代面臨全新挑戰：

1. **輸出的非結構化特性**：不像傳統 ML 有明確的數值指標（如準確率、召回率），LLM 輸出的是開放式文本，難以用簡單的指標衡量

2. **主觀性問題**：什麼是「好的」回應往往高度依賴具體情境和使用者期望

3. **邊緣案例層出不窮**：你測試了 100 種情況，使用者偏偏會用第 101 種方式來問

4. **持續對話的複雜性**：不像一問一答就結束，真實對話可能持續幾天甚至幾個月





## **什麼是改進循環? 分析、測量、改進**

LLM 應用改進的核心是一個三步驟循環：

1. **分析（Analyze）**：進行錯誤分析

2. **測量（Measure）**：大規模測量

3. **改進（Improve）**：基於測量結果進行改進

![Pasted 2025-11-02-08-00-43.png](./什麼是%20AI%20應用評估的錯誤分析%20Error%20Analysis!-assets/Pasted%202025-11-02-08-00-43.png)



## **什麼是錯誤分析 Error Analysis ?**

第一步的錯誤分析是整個流程的關鍵。重點就是透過分析找到有哪些失敗模式，後續步驟直接針對這些失敗模式來進行量測及改進。

> 編按: 針對沒有標準答案的問答評估(對比有標準答案的是指單選、多選等有固定答案)，這裏不同於常見的 [G-Eval ](https://arxiv.org/abs/2303.16634)評估方式採用正面表列，根據你的 Criteria 做評估量測打分(例如1\~5分有多符合)。這裏教的方法是先做錯誤分析，拿到具體的負面表列後，後續再針對 “每一種” 失敗模式都來做評估量測和改進。



![Pasted 2025-11-02-08-00-43 1.png](./什麼是%20AI%20應用評估的錯誤分析%20Error%20Analysis!-assets/Pasted%202025-11-02-08-00-43%201.png)

### **1\. 創建初始數據集：100 個樣本**

目標是得到 100 個跨越不同使用維度的輸入。為什麼是 100 個？「沒什麼特別原因，就是個不多不少的數字，足夠讓你開始了。」

具體執行步驟：

- **維度思考**：在你的應用可能期望經歷的維度進行採樣，想出至少三個維度。可以從功能、角色、查詢複雜性或使用場景的角度來思考

- **組合生成**：生成這三個維度的 50 個組合，過濾掉不合理的

- **查詢生成**：手寫或使用 LLM 幫助生成完整的 100 個現實查詢

### **2\. 檢視資料**

查看追蹤記錄，並在記錄上寫筆記。查看 100 個數據項目中的每一個，並對你在數據中觀察到的失敗模式進行觀察。

關鍵原則：

- 讓類別從數據中自然浮現，而不是帶著預設想法

- 不需要做根本原因分析(why 發生)，只需關注觀察到的行為和模式

- 預計花費時間：「這是你將花費 80% 時間的地方，對於 100 個追蹤記錄可能需要大約一個小時」

另外，NurtureBoss 的經驗顯示，如果自己開發的檢視工具更能大幅提升效率:

- 能清楚顯示對話全貌：用戶說了這個，AI 說了那個，AI 呼叫了工具。這是 AI 從工具得到的回應

- 快速標記和註解：標記這個對話是好是壞，然後快速輸入註解解釋原因

- 快速分類失敗模式：分類這是 看房安排錯誤、未觸發轉接、重複詢問…，然後系統統計哪類錯誤最常發生

### **3\. 分群歸類**

看完所有案例後，把類似的問題放在一起。你可以用 AI 幫忙，但最後一定要自己檢查。Eugene 說「我把所有東西都先讓 AI 跑一遍當草稿。AI 會給出不錯的分類，但最後總是需要 5-10% 的人工調整。」

通過將相似的失敗模式分組，建構和合併出你應用的失敗分類法，統計每種錯誤出現的頻率，識別最常見的失敗模式。

實用建議：

- 嘗試創建二元的失敗模式（可觀察到的 True 或 False ），這樣更容易有明確的定義，比較簡單

- 始終手動審查、改進和自行定義這些失敗模式

### **4\. 標記更多追蹤記錄並迭代**

在這個過程中，不要擔心你的失敗模式命名或定義可能會演變。這是標註數據時常見的現象，隨著你檢查新的輸出，標準會漂移。實際上你應該更高興，因為這反映了你對數據理解的加深。

那要持續標註多少資料? 當新的資料都沒發現新的失敗模式時，就可以停下來迭代了。





## **總結**

**必須人工查看數據**，引用 Greg Brockman 推文:「手動檢查數據是機器學習中價值與聲望比最高的活動」。Hamel 更進一步強調：「我會說這是機器學習中投資報酬率最高的活動，而且是建立任何 AI 產品時投資報酬率最高的活動。」雖然查看數據感覺像枯燥的苦工，但實際上「當你查看數據時，會非常快速地獲得大量價值」。

[https://platform.twitter.com/embed/Tweet.html?dnt=true&embedId=twitter-widget-0&features=eyJ0ZndfdGltZWxpbmVfbGlzdCI6eyJidWNrZXQiOltdLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2ZvbGxvd2VyX2NvdW50X3N1bnNldCI6eyJidWNrZXQiOnRydWUsInZlcnNpb24iOm51bGx9LCJ0ZndfdHdlZXRfZWRpdF9iYWNrZW5kIjp7ImJ1Y2tldCI6Im9uIiwidmVyc2lvbiI6bnVsbH0sInRmd19yZWZzcmNfc2Vzc2lvbiI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfZm9zbnJfc29mdF9pbnRlcnZlbnRpb25zX2VuYWJsZWQiOnsiYnVja2V0Ijoib24iLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X21peGVkX21lZGlhXzE1ODk3Ijp7ImJ1Y2tldCI6InRyZWF0bWVudCIsInZlcnNpb24iOm51bGx9LCJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3Nob3dfYmlyZHdhdGNoX3Bpdm90c19lbmFibGVkIjp7ImJ1Y2tldCI6Im9uIiwidmVyc2lvbiI6bnVsbH0sInRmd19kdXBsaWNhdGVfc2NyaWJlc190b19zZXR0aW5ncyI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfdXNlX3Byb2ZpbGVfaW1hZ2Vfc2hhcGVfZW5hYmxlZCI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfdmlkZW9faGxzX2R5bmFtaWNfbWFuaWZlc3RzXzE1MDgyIjp7ImJ1Y2tldCI6InRydWVfYml0cmF0ZSIsInZlcnNpb24iOm51bGx9LCJ0ZndfbGVnYWN5X3RpbWVsaW5lX3N1bnNldCI6eyJidWNrZXQiOnRydWUsInZlcnNpb24iOm51bGx9LCJ0ZndfdHdlZXRfZWRpdF9mcm9udGVuZCI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9fQ%3D%3D&frame=false&hideCard=false&hideThread=false&id=1622683988736479232&lang=zh-tw&origin=https%3A%2F%2Fihower.tw%2Fblog%2F12960-ai-evals-and-error-analysis&sessionId=9b3d182e6cd82e178ff28c0f5907f0603035769f&theme=light&widgetsVersion=2615f7e52b7e0%3A1702314776716&width=550px](https://platform.twitter.com/embed/Tweet.html?dnt=true&embedId=twitter-widget-0&features=eyJ0ZndfdGltZWxpbmVfbGlzdCI6eyJidWNrZXQiOltdLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2ZvbGxvd2VyX2NvdW50X3N1bnNldCI6eyJidWNrZXQiOnRydWUsInZlcnNpb24iOm51bGx9LCJ0ZndfdHdlZXRfZWRpdF9iYWNrZW5kIjp7ImJ1Y2tldCI6Im9uIiwidmVyc2lvbiI6bnVsbH0sInRmd19yZWZzcmNfc2Vzc2lvbiI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfZm9zbnJfc29mdF9pbnRlcnZlbnRpb25zX2VuYWJsZWQiOnsiYnVja2V0Ijoib24iLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X21peGVkX21lZGlhXzE1ODk3Ijp7ImJ1Y2tldCI6InRyZWF0bWVudCIsInZlcnNpb24iOm51bGx9LCJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3Nob3dfYmlyZHdhdGNoX3Bpdm90c19lbmFibGVkIjp7ImJ1Y2tldCI6Im9uIiwidmVyc2lvbiI6bnVsbH0sInRmd19kdXBsaWNhdGVfc2NyaWJlc190b19zZXR0aW5ncyI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfdXNlX3Byb2ZpbGVfaW1hZ2Vfc2hhcGVfZW5hYmxlZCI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9LCJ0ZndfdmlkZW9faGxzX2R5bmFtaWNfbWFuaWZlc3RzXzE1MDgyIjp7ImJ1Y2tldCI6InRydWVfYml0cmF0ZSIsInZlcnNpb24iOm51bGx9LCJ0ZndfbGVnYWN5X3RpbWVsaW5lX3N1bnNldCI6eyJidWNrZXQiOnRydWUsInZlcnNpb24iOm51bGx9LCJ0ZndfdHdlZXRfZWRpdF9mcm9udGVuZCI6eyJidWNrZXQiOiJvbiIsInZlcnNpb24iOm51bGx9fQ%3D%3D&frame=false&hideCard=false&hideThread=false&id=1622683988736479232&lang=zh-tw&origin=https%3A%2F%2Fihower.tw%2Fblog%2F12960-ai-evals-and-error-analysis&sessionId=9b3d182e6cd82e178ff28c0f5907f0603035769f&theme=light&widgetsVersion=2615f7e52b7e0%3A1702314776716&width=550px)

**不要迷信通用的評估指標**，例如簡潔性評分、幻覺評分等通用指標，那些都是無意義的學術練習。Jacob 的經驗證實了這點，他們透過錯誤分析，將日期處理的成功率從 33% 提升到 100%，這種具體、可測量的改進才是真正有價值的。 你的系統有其獨特性，通用工具和指標往往無法完美適用。專注於你的實際痛點，而不是追求漂亮的通用分數。

**不要一開始就用 LLM 做初步標註**，這是很多人會犯的錯誤。不要讓 LLM 幫你做初步標註再調整，因為 LLM 會把你帶偏，你會被它的判斷影響，你需要親自看數據，建立自己對資料的直覺理解，LLM 抓不到你在意的「vibes」氛圍! 花一個小時標註絕對值得。你正在基於這評估來建立整個產品，百分之百值得親自查看你的數據。

LLM 應用的評估和錯誤分析不僅是技術問題，更是一種思維方式的轉變。成功的關鍵不在於使用什麼工具或框架，而在於建立一個持續學習和改進的文化。透過系統化的方法、正確的心態和持續的努力，可以將你的 LLM 應用從概念驗證推進到真正改變用戶生活的產品。