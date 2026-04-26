為什麼 Claude Design Agent 嚴禁使用 `scrollIntoView`（我猜的）

在 Claude Design Agent 的執行環境裡，你產出的 HTML 跑在 Claude.ai 的 iframe 預覽窗格內，這個 iframe 又坐落在整個聊天介面之中。問題的核心在於，`scrollIntoView` 並不只捲動最近的卷軸容器，它會沿著 DOM 樹往上冒泡，把所有具有 `overflow: auto` 或 `overflow: scroll` 的祖先元素一併捲動。一旦呼叫，這道捲動指令會穿過 iframe 邊界，把使用者的聊天視窗、訊息列、甚至外層整個 App 的捲軸都拉走。換句話說，你以為自己只是在捲動原型裡的某個元素，實際上你把使用者「正在閱讀的對話」整個甩走了。

從技術原理來看，瀏覽器的 `scrollIntoView` 規格本來就是這樣設計的。當你呼叫這個方法時，瀏覽器會先計算目標元素到 viewport 的距離，接著沿著 `offsetParent` 鏈往上找，每一個可捲動的祖先（包含 `<html>`、`<body>`，以及外層 iframe 的父視窗）都會被調整 `scrollTop`。在 iframe 場景下，瀏覽器會嘗試讓 iframe 內的元素「對使用者可見」，這意味著它會通知父頁面也跟著捲動，結果是整個 Claude.ai 的 UI 跟著震一下。`scrollIntoViewIfNeeded`（非標準 API）與帶 `block: 'nearest'` 選項的版本表現稍好，但跨 iframe 邊界的傳播風險依然存在，而且各家瀏覽器實作不一致，根本無法可靠地預測行為。

具體會壞掉什麼？常見的災情是這樣的場景：使用者正在預覽你做的簡報原型，按了某個按鈕觸發 `scrollIntoView`，結果整個 Claude.ai 的對話列表瞬間跳到頁面頂端，使用者看不到原本在讀的訊息。或者，自動播放動畫到某個段落呼叫 `scrollIntoView`，主視窗的右側面板被推開、原本浮動的工具列消失，使用者一頭霧水。更糟的情況是，iframe 內的捲動會洩漏到工具列、Tweak 面板、甚至評論氣泡的定位錨點，造成 `<mentioned-element>` 抓到的 DOM 座標跟使用者看到的完全錯位。這些問題不是程式有 bug，而是 `scrollIntoView` 本來就會這樣運作，只是在一般獨立網頁開發時你看不出來。

正確的替代方案是明確指定要捲動哪一個容器，把捲動行為鎖死在你自己的設計範圍內。最直接的做法是對特定容器設定 `scrollTop`，這種方式不會牽動任何祖先。若需要平滑捲動效果，可以改用 `scrollTo` 搭配 `behavior: 'smooth'`，這個 API 同樣只作用於你指定的容器。橫向幻燈片切換常用的模式則是對容器設定水平方向的 `scrollLeft`。若需要計算精確位移，可以搭配 `getBoundingClientRect` 取得目標相對容器的偏移量，再呼叫 `scrollTo`。這些方法的共同特點是直接操作你指定的那一個容器，捲動效果不會冒泡到祖先，更不會穿透 iframe 邊界。

從設計準則的角度來看，這條規則背後的精神，跟 Nielsen 第三條可用性啟發「使用者控制與自由」是同一脈絡：你做的 Artifact `不應該綁架使用者的視窗控制權`。Claude.ai 是一個多面板的 IDE 風格介面，原型只是其中一塊磚，磚塊不該擅自移動整面牆。所以這條鐵律可以這樣記：你設計的捲動，永遠只能發生在你畫的那個框框裡。如果想深入了解 iframe 與 scroll 行為的交互，可以查 MDN 上 `Element.scrollIntoView()` 文件中的「Scrolling ancestors」章節，Chrome DevTools 的 Performance 面板也能看到 `scrollIntoView` 觸發的多重 layout 計算，跟單純 `scrollTop` 賦值的差距相當明顯。