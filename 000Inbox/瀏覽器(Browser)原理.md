---
tags:
  - frontend
---
# **瀏覽器(Browser)原理**

- <https://developer.chrome.com/blog>

- [Inside look at modern web browser](https://developers.google.com/web/updates/2018/09/inside-browser-part1)

- [How Browsers Work: Behind the scenes of modern web browsers](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/#The_browsers_we_will_talk_about)

- [How the Puffin Browser Works](https://medium.com/coding-neutrino-blog/how-the-puffin-browser-works-440c91cece8f)

## 前導：進程(Process) & 線程(Thread):

程式常常會被劃分為幾個獨立又彼此配合的模組，瀏覽器也不利外，以Chrome為例，其是由多個進程組成，每個進程有自己核心功能，互相配合完成整體瀏覽器工作，每個進程又包含多個線程一起協同運作，以下簡單解釋進程與線程。

- 進程：
   一個任務可以稱為一個程序，一個在運行中的程序就叫做進程,進程就像工廠的獨立產線，一次只能進行一個任務。程式一般是放置在實體磁碟中，然後透過使用者的執行來觸發。觸發後會載入到記憶體中成為一個個體，那就是程序,所以,**進程可以看做是作業系統進行資源分配與調度的獨立單位**。  

   在 Linux 系統當中：『觸發任何一個事件時，系統都會將他定義成為一個程序，並且給予這個程序一個 ID ，稱為 PID，同時依據啟發這個程序的使用者與相關屬性關係，給予這個 PID 一組有效的權限設定。』以便作業系統可管理這個程序。

   在執行一個 Process 大概會有 Memory Space 和 Thread 這二個部份， Memory Space 用來進行變數的存取， Thread 就是屬於 CPU 運算的部份。Process 和 Process 之間的變數不能互相共享使用。

   但一個進程可以要求系統生成另一個進程來執行不同任務，系統會為新進程分配不同內存，而兩個進程間可以使用 IPC（Inter Process Communication）進行通訊。
   

   ![](https://i.imgur.com/p9msEbU.jpg)

   

   ![](https://i.imgur.com/6DRbmVB.png)

- 線程（執行緒）：
   當一個程序在跑得時候，可能有好幾個程序執行流程，這些執行流就叫做線程，可以想成是產線上的多個工人，一起在執行同一個PID的任務，每個工作在動作的時候就會佔據一些資源，但資源原則上是進程所擁有，因此每個線程都會有個父進行，因此線程可以想像成輕量級的進程。

    線程是獨自進行的，其不會知道有其他線程存在，對於進程的資源也是先搶先贏。

- 多線程：
   一個 Process 可以啟動多個 Thread 的 CPU 資源，Thread 和 Thread 之間的變數可以互相共享使用，多執行緒使用場景：\
   當遇到很多的 IO 處理時：例如要把一個很大的資料寫入到資料庫或是 File System 時，如果只用一個 main 程式去做的話，就會阻礙到後面程式的執行，所以應該要另外去開一個 Thread 去做寫入資料的動作，才能增加程式的執行效率。

- Concurrent 和 Parallel 之間的差異：

   - Concurrent 主要是一個 CPU 交叉排程去做多件事，雖然同一個時間點一樣只會做一件事，但避免一個線程完全結束後才進行下一個線程。

   - Parallel 主要是會有多個 CPU 在同一個時間點內會去做多件事，而這關係到CPU的核心數量。

## 瀏覽器架構:

瀏覽器的製作可以是單進程多線程，或是多進程再用 IPC 進行溝通，以Chrome 為例，其是多進程架構，最頂層有一個 Browser process 協調其他進程，Chrome 主要進程如下:

- Browser Process：

   - 地址欄、書籤、前進後退按鈕...等部分工作；

   - 一些瀏覽器底層操作，例如網路請求和文件訪問；

- Renderer Process（渲染）：

   - 負責一個tab內關於網頁呈現的所有工作;

- Plugin Process：

   - 控制一個網頁用到的所有插件,如 flashGPU Process

   - 處理GPU相關事情
      

      ![](https://i.imgur.com/1x9XVHz.jpg)

多進程好處是單一進程運行失敗的話，並不影響其他進程，但因為記憶體不能共用，所以進程如果要處理一樣的東西的話，其沒辦法共享。
此外，Chrome 把瀏覽器不同程序的功能看做服務，這些服務可以方便的分割為不同的進程或者合併為一個進程。
以Broswer Process 為例，如果Chrome 運行在強大的硬件上，它會分割不同的服務到不同的進程，這樣Chrome 整體的運行會更加穩定，但是如果Chrome 運行在資源貧瘠的設備上，這些服務又會合併到同一個進程中運行，這樣可以節省內存。

另外，Chrome 與許同一tab下利用獨立進程開啟 Subframe，這樣同tab下跨站資訊可以獨立渲染以增加穩定性。

![](https://i.imgur.com/PavBWpY.jpg)

## 網頁搜尋過程

瀏覽器 Tab 外的工作主要由 Browser Process 掌控，Browser Process 又對這些工作進一步劃分，使用不同線程進行處理：

- UI thread ： 控制瀏覽器上的按鈕及輸入框；

- network thread: 處理網絡請求，從網上獲取數據；

- storage thread: 控製文件等的訪問；

步驟：

1. 處理輸入：
   UI thread 需要判斷用戶輸入的是 URL 還是 query；

2. 開始搜尋：
   network thread 會執行 DNS 查詢，隨後為請求建立 TLS 連接。

3. 讀取回應：
   network thread 會依據 Content-Type 及 MIME Type sniffing 判斷回應內容的格式，如果回應內容的格式是 HTML ，下一步將會把這些數據傳遞給 renderer process，如果是 zip 文件或者其它文件，會把相關數據傳輸給下載管理器。

4. 查找渲染進程：
   當上述所有檢查完成，network thread 確信瀏覽器可以導航到請求網頁，network thread 會通知 UI thread 數據已經準備好，UI thread 會查找到一個 renderer process 進行網頁的渲染。

5. 確認搜尋：
   進過了上述過程，數據以及渲染進程都可用了， Browser Process 會給 renderer process 發送 IPC 消息來確認導航，一旦 Browser Process 收到 renderer process 的渲染確認消息，導航過程結束，頁面加載過程開始。此時，地址欄會更新，展示出新頁面的網頁信息。 history tab 會更新，可通過返回鍵返回導航來的頁面，為了讓關閉 tab 或者窗口後便於恢復，這些信息會存放在硬盤中。

## 渲染流程:

### 1\. 主線程解析 HTML 和構建 DOM

渲染的第一步是由主線程解析 HTML 文本，逐步構建 DOM（Document Object Model）樹。DOM 是一個表示頁面結構的樹形數據結構，代表 HTML 文檔的內容和結構。

### 2\. 資源加載

在解析 HTML 的過程中，主線程會識別出需要加載的外部資源，如圖片、CSS 文件、JavaScript 腳本等。這些資源會被主線程逐一發出請求，並在接收到這些資源後進行處理。CSS 影響到樣式計算，JavaScript 可能會改變 DOM 結構，因此需要特別處理。

### 3\. JavaScript 執行

JavaScript 的執行是渲染流程中的一個關鍵點，因為它可能會改變 DOM 結構或樣式。當瀏覽器遇到 `<script>` 標籤時，如果沒有 `async` 或 `defer` 屬性，瀏覽器會暫停 HTML 解析，先加載並執行 JavaScript。  

- `async` 屬性允許 JavaScript 非同步加載並立即執行，無需等待 DOM 完全構建。

- `defer` 屬性則在 DOM 解析完成後再執行 JavaScript，確保腳本按順序執行。

### 4\. 樣式計算

主線程使用 CSS 選擇器和規則來計算每個 DOM 元素的最終樣式，這一過程稱為樣式計算（style calculation）。計算結果會應用到 DOM 樹中的各個元素上。

### 5\. 佈局

在樣式計算完成後，主線程會基於 DOM 和樣式信息構建佈局樹（layout tree），並確定每個元素在頁面上的位置和大小。這個階段也被稱為回流（reflow）或佈局（layout）。

### 6\. 繪製

主線程接著會根據佈局樹生成繪製指令，這些指令確定元素如何在螢幕上繪製出來。這些繪製指令會記錄每個元素的顏色、邊框、陰影等細節。

### 7\. 合成和光柵化

現代瀏覽器會將頁面分成多個層（layer），每個層可以單獨進行光柵化處理（即將向量圖形轉換為像素）。光柵化後，合成器線程（compositor thread）負責將這些層合成（compose）成最終的畫面。這種分層處理有助於提高渲染性能，特別是在頁面部分內容發生變化時，只需重新光柵化和合成受影響的層。

### 8\. 渲染流水線

現代瀏覽器採用更複雜的渲染流水線，包含樣式計算、佈局、繪製和合成等階段。這些階段在某些情況下可能會並行執行，以提高效率。如果樣式或佈局發生變化，渲染流程可能會重複執行相關階段。

### 9\. Worker 線程

為了減少主線程的負擔，現代瀏覽器還會使用 Worker 線程來執行一些 JavaScript 任務。Worker 線程運行在主線程之外，可以進行密集計算而不會阻塞主線程的執行，從而提高整體渲染性能。

這些步驟共同構成了網頁從 HTML 解析到最終呈現在用戶螢幕上的完整渲染流程。每個步驟都扮演著關鍵角色，確保網頁可以高效且正確地呈現。