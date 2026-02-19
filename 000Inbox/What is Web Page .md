---
tags:
  - frontend
---
# What is Web Page 

- Resource:

   - [SoftwareArchitect](https://github.com/justinamiller/SoftwareArchitect#4-code)

   - [Learn Programming For Free (All Free Resources)](https://dev.to/nerdjfpb/learn-programming-for-free-all-free-resources-2b3j)

   - [Learn to code in 2020, get hired, and have fun along the way](https://zerotomastery.io/blog/learn-to-code-in-2020-get-hired-and-have-fun-along-the-way/)

   - [Roadmap to becoming a web developer in 2020](https://github.com/kamranahmedse/developer-roadmap)

   - [Web Development In 2020 - A Practical Guide Course List](https://github.com/andrews1022/web-development-2020-course-list)

   - [Lidemy 鋰學院](https://www.lidemy.com/)

   - [Learn how to design large-scale systems.](https://github.com/donnemartin/system-design-primer)



## WWW(World wile Web)

- Basic Introduction:

   - 全球資訊網（Web、WWW、W3），最初只是希望可以透過網絡分享彼此的資訊，目前已經演變成所有互相聯結的超文字文檔系統，以下幾個關鍵字介紹。

   - 資源:ＷＷＷ中，每個有用的事物都稱為資源(Resource)。

   - HTML:資源是以超文字標示語言(Hypertext Markup Language)是W3系統主要檔案格式。

   - HTTP:超文本傳輸安全協定（HTTP,Hypertext Transfer Protocol)，是W3主要通訊協議，一般來說只要將資源放置到伺服器(Server)，使用者可以透過瀏覽器輸入 URI 去訪問。

- Web Application:

   - 大部分 Web 應用程式都是由 **客戶端-Client** 和**伺服器端-Server**所組成：

   - 客戶端(Client):

      - 又稱為前端(Front-End)

      - 主要就是**瀏覽器**

      - 使用者透過**瀏覽器**去請求 Web 資源

      - 收到相關資源後(HTML...等)，瀏覽器進行解析，最後呈現畫面

   - 伺服器端(Server):

      - 又稱後端（Back-end)

      - 主要是 HTTP Server 以及運行在上面的相關資源

      - 所謂 HTTP Server 就是裝有相關軟體的主機，並且有連結上 www

      - Server 收到瀏覽器請求後，會進行相關處理，並回傳所需資源

      - 常見 Server Software:

         - Apache HTTP Server

         - Ngnix

         - Internet Information Servers(IIS)

   - 重點:兩端是在不同記憶體的機器上透過通訊協議溝通，無法直接的互動

   - 使用者透過瀏覽器輸入URI(Uniform Resource Identifier),其會備解析後透過網路找到正確的網域名稱&IP及連結到對應的www伺服器(主機)。連結到主機後，瀏覽器會發出一個HTTP請求，通常會將HTML/CSS/JavaScript檔案,連同所需的圖片/文字...等資源回傳。最終瀏覽器會把所有資源解析成使用者能看到的網頁。

- Web Page：

   - 網站本質上是由 **HTML, CSS, JaveScript** 文件所組成，瀏覽器看到的是這些格式文字，再渲染成使用者所看到的畫面:
      

      ![](https://i.imgur.com/pDVIYQw.jpg)

      

   - HTML(HyperText Markup Language)：就是 WWW這系統上主要的共用資料格式，瀏覽器會針對HTML文件主體內容作解析，以便進行畫面呈現與定義行為，可以說其存放網頁的內容與架構

   - CSS(Cascading Style Sheets)：是疊層樣式表，主要目的是制定 HTML 標記內容的靜態呈現樣式; CSS 選擇器用於選擇 HTML 元素的一種語法，可以分為:

   - JavaScript：如果我們要讓網站可以根據使用者行為做出一些「反應」，例如點下按鈕後顏色改變、按下 enter 時發出聲音,那就需要像　JavaScript 這種具備「邏輯」的程式語言來幫忙了 。
      

      ![](https://i.imgur.com/tEXYmij.jpg)

- WWW Server：

   - 架設網站最簡單的方法就是把相關檔案放在裝有伺服器軟體的主機上，讓伺服器軟體來回應相關請求，而一般常見的 Web 網站伺服器軟體主要有 Apache、Nginx以及 Windows Server上的 IIS。

   - 以 Linux Apache 為例，只要以下指令安裝即可：

   - Web Service Architecture

      - [\[筆記\] REST 到底是什麼](https://medium.com/@jinghua.shih/%E7%AD%86%E8%A8%98-rest-%E5%88%B0%E5%BA%95%E6%98%AF%E4%BB%80%E9%BA%BC-170ad2b45836)

      - [SOAP vs. REST: Differences in Performance, APIs, and More](https://dzone.com/articles/differences-in-performance-apis-amp-more)

      - SOAP

      - REST

- HTTP (HyperText Transfer Protocol)

   - [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

   - HTTP is a protocol which allows the fetching of resources, such as HTML documents. 

   - HTTP is the foundation of any data exchange on the Web and it is a **client-server** protocol.

   - Clients and servers communicate by exchanging individual messages. 

      - requests: messages sent by the client, usually a Web browser 

      - responses: messages sent by the server as an answer

   - 使用者在瀏覽器輸入web網頁的URI後，就會開始進行HTTP的處理，HTTP一般使用 80 port 與伺服器建立TCP連接。HTTP 最大特點就是基於請求「Request」與回應「Response」的傳輸方式，沒請求就不會有回應，而最基本的幾個指令分別是:

   - OPTIONS: 設定選項

   - GET: 取得指定URI資源

   - HEAD: 只取得表頭訊息

   - POST: 在指定的URI登錄資料

   - PUT: 在指定的URI儲存資料

   - DELETE: 刪除指定URI的資料

   - TRACE: 請求訊息回到使用者端
      

      ![](https://i.imgur.com/h2AqWwT.jpg)

# Front-End

- Resource：

   - [CodePen：Online Front End Code Editor](https://codepen.io/)

   - [Web 界非常實用的線上編譯：jsFiddle - Online Editor for the Web](https://jsfiddle.net/)

   - [紮實的網頁前端學習路線與資源推薦](https://medium.com/@hulitw/front-end-learning-path-55201571ecfe)

   - [MATERIAL DESIGN - Data visualization](https://material.io/design/communication/data-visualization.html#principles)

   - [Qhmit.com](https://www.qhmit.com/)

   - HTML/CSS:

      - [CSS Terms and Definitions](https://www.impressivewebs.com/css-terms-definitions/)

      - [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/)

      - [html & css is hard](https://internetingishard.com/html-and-css/)

      - [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

      - [A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

   - Bootstrap:

      - [Bootstrap 4 Tutorial](https://www.w3schools.com/bootstrap4/default.asp)

   - Responsive Design Web:

      - [Responsive Media Designs: Setting CSS Breakpoints](https://www.bitdegree.org/learn/responsive-media)

      - [How to build a Complete Responsive Website from scratch | Html5 CSS3 Website Design Tutorial](https://www.youtube.com/watch?v=X8NFkUQNeek&list=LL4a5i79DSM5EOraX1iamrjQ)

   - Design Inspiration:

      - [Dribbble](https://dribbble.com/)

      - [Pattern Tap](https://zurb.com/patterntap)

      - [Mashup Template](http://www.mashup-template.com/)

      - [Free Bootstrap Templates](https://bootstrapmade.com/)

   - Other:

      - [2020🔥 New and Hand-Picked Free Web Resources, Every developer should bookmark it!](https://dev.to/gadhiyaravi/2020-new-and-hand-picked-free-web-resources-every-developer-should-bookmark-it-mn7)

      - [Frontend free resource](https://zerotomastery.io/resources/)

   - Advantage:

      - [A Really, Really, Really Good Introduction to XML](https://www.sitepoint.com/really-good-introduction-xml/)

## DOM(Document Object Model)

- [主要參考書籍: AI時代在網頁上資料視覺化：D3.js實作寶典](https://www.books.com.tw/products/0010803892)

- [Day03-深入理解網頁架構：DOM](https://ithelp.ithome.com.tw/articles/10202689)

- HTML 本質是是由一堆預定義好的元素組成階層式架構的文件，而這就是由「文件物件模型」 DOM (Document Object Model )樹決定架構，加上元素的標籤來決定段落用途， 

- Why DOM?

   - DOM 是一種針對結構化文件的介面，其允許程式和指令搞動態的存取和修改文件，當需要動態修改網頁元素時，會需要用DOM 

   - 網頁都是在瀏覽器上運行，瀏覽器本質就是一種編譯器，負責編譯網頁程式，不統一格式的話各瀏覽器會各自為政不利網路發展，而　WWW　就定義各種基準來讓大家參與，DOM　就是其中一個協定結構，

- 結構:

   - DOM : DOM 其實就是把一份 HTML 文件內的各個標籤，包括文字、圖片等等都定義成物件，而這些物件最終會形成一個**樹狀結構**，每個元素都是樹的節點，其關係如下圖:
      

      ![](https://i.imgur.com/tAlYrOl.png)

      

   - 在 DOM 中，每個 element 、 文字(text) 等等都是一個節點，而節點通常分成以下四種：

      - Document: 是指本文件，也就是這份 HTML 檔的開端

      - Element: 文件內的各種 tag 標籤

      - Text: 標籤包起來的文字

      - Attribute: 標籤內的屬性

- 存取和修改 HTML 元素:

   - DOM 物件儲存在 document 中，呼叫其方法或屬性，即可存取 HTML 檔案中的任意元素

   ```javascript
   document.getElementById("an_id");
   document.getElementsByTagName("p");
   document.getElementsByClassName("an_class");
   ```

   - an example:

      - 抓取所有 `<P> </P>` 元素，並以陣列儲存

      - 取出 `innerHTML` 屬性，印出後，進行文字內容修改

   ```htmlembedded
   <p>Apple</p>
   <p>Banana</p>
   <script>
     var para = document.getElementsByTagName("p");
     for (var i=0; i<para.length; i++){
         console.log(para[i].innerHTML);
         para[i].innerHTML = "New Text";
     }
   </script>
   ```

   - HTML DOM 常用屬性:

      - innerHTML: 元素標籤內部文字，包含 HTML 標籤

      - innerText: 元素標籤內部文字，不包含 HTML標籤

      - outerHTML: 包含元素標籤本身在內文字，包含內部 HTML 標籤

      - outerText: 包含元素標籤本身在內文字，不包含內部 HTML 標籤

      - nodeName: 節點名稱

      - parentNode: 父節點

      - childNodes: 子節點

      - nextSibling: 下一個兄弟節點

      - previousSibling: 上一個兄弟節點

      - style: 元素樣式

   - 修改元素樣式: 將 body 元素的背景顏色修改成藍色

   ```javascript
   var body = document.getElementsByTagName("body");
   console.log(body);
   body[0].style.backgroundColor = "blue";
   ```

   - 增加節點: 使用 `appendChild()`方法增加子節點

   ```javaseript
   // create a new node first
   var para = document.createElement("p");
   para.innerHTML = "Hello";
   //get a body node
   var body = document.getElementById("mybody");
   //add a child node to body node
   body.appendChild(para);
   ```

   - 刪除節點: `removeChild` method

   ```htmlembedded
   <body id="mybody">
    <p id="mypara">Apple</p>
    <p>Banana</p>
    <script>
      var para = document.getElementById("mypara");
      var body = document.getElementById("mybody");
      body.removeChild(para)
    </script>
   </body>
   ```

   - 事件:

      - HTML DOM 透過事件能夠與使用者進行互動(Ex:點擊滑鼠, 滑鼠移入, 頁面載入...等)

      - an example: 點擊 "Click Here" 後，變成 "Thank you!"

      ```htmlembedded
      <p id="mypara">Click Here</p>
      <script>
        var para = docment.getElementById("mypara");
        para.onclick = function(){
            this.innerHTML = "Thank you";
        }
      </script>
      ```

      - 個人解讀： 

         - let`para.onclick`binding a function 

         - after user click, produce`para.onclick` and call function immediately

      - 其他事件:

         - onload: 頁面或圖片載入完成

         - onclick: 滑鼠點擊

         - ondblclick: 滑鼠雙擊

         - onkeydown: 鍵盤某鍵按下

         - onkeypress: 鍵盤某鍵按下並鬆開

         - onkeyup: 鍵盤某個案件鬆開

         - onmousedown: 滑鼠按鈕按下

         - onmousemove: 滑鼠移動

         - onmouseout: 滑鼠從某元素移開

         - onmouseover: 滑鼠移到某元素上

         - onmouseup: 滑鼠鬆開

## HTML

- Introduction :

   - HTML is the standard markup language for creating web page.

   - HTML tags are elements names surrounded by angle brackets.

   - `<tag_name>content</tag_name>` 

- First look:

   ```htmlembedded
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <title>Hello World</title>
   </head>
   <body>
     <h1>Hello World</h1>
     <p>This is a web page.</p>
   </body>
   </html>
   ```

   - `<!DOCTYPE html>` a declaration that document is HTML5

   - `<html>` the root element of an HTML page

   - `<head>` element contains meta info.

   - `<body>` elements contains the visible page content 

      ![](https://i.imgur.com/V011hQt.png)

      

      ![](https://i.imgur.com/W3U8jPT.png)

- Semantics Overview: 

   - Semantics within HTML is the practice of giving content on the page meaning and structure by using the proper element.

   - [Semantic code: What? Why? How?](https://boagworld.com/dev/semantic-code-what-why-how/)

   - Block vs. Inline Elements:

      - Block-level elements begin on a new line, stacking one on top of the other, and occupy any available width. We’ll most commonly see block-level elements used for larger pieces of content, such as paragraphs.

      - Inline-level elements do not begin on a new line. They fall into the normal flow of a document, lining up one after the other, and only maintain the width of their content.Inline-level elements may be nested inside one another; however, they cannot wrap block-level elements. We’ll usually see inline-level elements with smaller pieces of content, such as a few words.

   - A `<div>` is a block-level element that is commonly used to identify large groupings of content, and which helps to build a web page’s layout and design.

   - A `<span>`, on the other hand, is an inline-level element commonly used to identify smaller groupings of text within a block-level element.

   - For the longest time the structure of a web page was built using divisions. The problem was that divisions provide no semantic value, and it was fairly difficult to determine the intention of these divisions. Fortunately HTML5 introduced new structurally based elements, including the `<header>`, `<nav>`, `<article>`, `<section>`, `<aside>`, and `<footer>` elements.
      

      ![](https://i.imgur.com/hRuiztU.png)

   - The `<nav>` element identifies a section of major navigational links on a page. The `<nav>` element should be reserved for primary navigation sections only, such as global navigation, a table of contents, previous/next links, or other noteworthy groups of navigational links.

   - Both the `<article>` and `<section>` elements contribute to a document’s structure and help to outline a document. If the content is being grouped solely for styling purposes and doesn’t provide value to the outline of a document, use the `<div>` element.

### Basic Tag

- `<div>` tag: defines a division or a section in an HTML document

   - often used as a container for other HTML elements to style them with CSS or to perform certain tasks with JavaScript

   - try:

   ```htmlembedded
   <!DOCTYPE html>
   <html>
   <body>
   <p>This is some text.</p>
   
   <div style="background-color:lightblue">
     <h3>This is a heading in a div element</h3>
     <p>This is some text in a div element.</p>
   </div>
   
   <p>This is some text.</p>
   </body>
   </html>
   ```

- `<span>` tag:span 標籤可以用來標示一個行元素，並做出一些顏色修改...等效果，與 DIV 區塊的用法有點類似，但瀏覽器會將 span 標籤包起來的元素視為一行

- Link `<a></a>`: `<a href="https://www.w3schools.com">This is a link</a>`

- image`<img>`：`<img src="img_girl.jpg" width="500" height="600" alt="image describe">`

- `<a href="#">`: to the top of the page

### SVG:

- [主要參考書籍: AI時代在網頁上資料視覺化：D3.js實作寶典](https://www.books.com.tw/products/0010803892)

- [How can I convert a shapely Polygon to an SVG?](https://stackoverflow.com/questions/49147707/how-can-i-convert-a-shapely-polygon-to-an-svg)

- Basic Introduction:

   - 可縮放向量圖(Scalable Vector Graphics)

   - 用於描述二維向量圖形的一種圖形格式

   - 使用 **XML** 格式來定義圖形

   - 大部分瀏覽器支援 SVG ，可直接嵌入 HTML 中顯示

- 點陣圖和向量圖:

   - 解析度：向量圖與解析度無關，可自由縮放；向量圖與解析度相依，會有馬賽克情況

   - 色彩：向量圖基於數學圖形，表達上較簡單；點陣圖表達較豐富

   - 空間：向量圖占用空間較小；點陣圖佔用空間較大

   - 轉換：向量可以輕鬆轉乘點陣；點陣轉向量較麻煩

- 使用方式：

   - Inline: HTML 中嵌入`<svg></svg>` 中，成為 DOM 的一部分，後續可用 JS 和 CSS 操作

   ```htmlembedded
   <!DOCTYPE html>
   <html>
   <head></head>
   <body>
   <svg
     id="mysvg"
     xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 800 600"
     preserveAspectRatio="xMidYMid meet">
     <circle id="mycircle" cx="400" cy="300" r="50" />
   <svg>
   </body>
   </html
   ```

   - SVG 寫成獨立文件，再用`<img>、<object>、<embed>、<iframe>`等 tag 插入

   ```htmlembedded
   <img src="circle.svg">
   <object id="object" data="circle.svg" type="image/svg+xml"></object>
   <embed id="embed" src="icon.svg" type="image/svg+xml">
   <iframe id="iframe" src="icon.svg"></iframe>
   ```

- SVG 基本形狀元素:

   - 矩形(rect):

   ```htmlembedded
   <rect x="10" y="10" width="200" height="200"
         style="fill:steelblue; stroke:blue; stroke-width:4; opacity:0.5"/>
         
   <rect x="0" y="0" width="50" height="50" rx="10" ry="10" 
         style="fill:steelblue; stroke:blue; stroke-width:2; opacity:0.5"/>
   ```

   - 圓形(circle):

   ```htmlembedded
   <circle cx="50" cy="50" r="25"
           style="fill:yellow; stroke:blue; stroke-width:2"/>
   ```

   - 橢圓(ellipse):

   ```htmlembedded
   <ellipse cx="50" cy="50" rx="50" ry="5" 
            style="fill:#33FF33; stroke:red; stroke-width:2"/>    
   ```

   - 線段(line):

   ```htmlembedded
   <line x1="20" y1="20" x2="100" y2="100"
         style="stroke:black; stroke-width:4"/>
   ```

   - 多邊形(polygon):

   ```htmlembedded
   <polygon points="130,20 50,90 90,160 170,160 210,90"
            style="fill:pink; stroke:black; stroke-width:3"/>
   ```

   - 聚合線(polyline):

   ```htmlembedded
   <polyline points="130,20 50,90 90,160 170,160 210,90"
             style="fill:white; stroke:black; stroke-width:3"
             transform="translate(80,50)"/>
   ```

   - 路徑(path):

      - 用法:列出一個座標點，座標前增加一個大寫字母代表操作參數。

      - 操作參數說明:

         - 移動:

            - M：move to, 將畫筆移到指定座標

         - 直線:

            - L：line to, 畫直線到指定點

            - H：畫水平線到指定點

            - V：畫垂直線到指定點

            ```htmlembedded
            <path d="M10,10 L50,50
                     M10,10 H50
                     M10,10 V50"
                  style="stroke:black; stroke-width:3"/>
            ```

         - 3次貝茲曲線:

            - C：接3個座標，控制點1 控制點2 最終點

            - S：接2個座標，控制點 最終點

            ```htmlembedded
            <path d="M60,50 
                     C90,20 150,90 200,60 
                     S250,100 300,60"
                  style="fill:white; stroke:black; stroke-width:3"/>
            ```

         - 2次貝茲曲線:

            - Q：接2個座標，控制點 最終點

            - T：最終點

            ```htmlembedded
            <path d="M50,100 
                     Q150,50 200,100
                     T300,100"
                  style="fill:white; stroke:red; stroke-width:3"/>
            ```

         - 弧線 A: 畫橢圓曲線到指定座標，參數較多

            - A(rx, ry, x-axis-rotation, large-arc-flag, sweep-flag, x, y)

               - rx, ry:橢圓半徑

               - x-axis-rotation: 橢圓x軸水平夾角

               - large-arc-flag: 1(大角度弧線)，0(小角度弧線)

               - sweep-flag: 1(順時鐘走)，0(逆時鐘走)

               - x,y: 終點

         - Z 閉合

         ```htmlembedded
         <path d="M80,100
                  A40,10 0 1,1 50,200
                  Z" 
         fill="white" stroke="blue" stroke-width="3"/>
         </svg>
         ```

   - 文字(text)：`<text>x="" y="" dx="" dy="" rotate="" textLength=""</text>`

      - x, y: 起始點

      - dx, dy: 與起始點偏移量

      - rotate: 選轉角

      - textLength: 文字長度

      - `<tspan></tspan>tspan>`: 部分文字單獨定義

   ```htmlembedded
   <text x="150" y="150" dx="-5" dy="10" textLength="60" rotate="0">
     I love <tspan fill="red">D3</tspan>
   </text>
   ```

## CSS

- The type selector has the lowest specificity weight and holds a point value of 0-0-1. The class selector has a medium specificity weight and holds a point value of 0-1-0. Lastly, the ID selector has a high specificity weight and holds a point value of 1-0-0.

- Currently there are four primary ways to represent sRGB colors within CSS: 

   - keywords

   - hexadecimal notation:

      - [Adobe Kuler, a free application that provides a color wheel to help us find any color we want and its corresponding hexadecimal value.](https://color.adobe.com/create)

   - RGB values

      - RGB color values may also include an alpha, or transparency, channel by using the `rgba(255, 102, 0, .5)`

   - HSL values (percentage)

      - The first value, the hue, is a unitless number from 0 to 360.

      - The second and third values, the saturation and lightness, are percentage values from 0 to 100%.

      - HSL color values, like RGBa, may also include an alpha, or transparency, channel with the use of the `hsla(24, 100%, 50%, .5).` function.
         

         ![](https://i.imgur.com/sOfU20L.png)

         

         ![](https://i.imgur.com/r657uio.png)

- Lengths

   - Absolute Lengths

      - pixel: pixel is equal to 1/96th of an inch; thus there are 96 pixels in an inch.

   - Relative Lengths

      - percentage: set the width of an element to 50%, we have to know the width of its parent element

      - em: its length is calculated based on an element’s font size

- Display Property:

   - Exactly how elements are displayed—as block-level elements, inline elements, or something else—is determined by the display property.

   - display of an element has implications on how the box model is rendered.

   - There are four main value:

      - block

      - inline

      - inline-block

      - and none

- Box Model:

   - Every element on a page is a **rectangular** box.
      

      ![](https://i.imgur.com/cuLSAuO.png)

   - total width of an element:

      - margin-right + border-right + padding-right + width + padding-left + border-left + margin-left

      - The default width of an element depends on its display value. 

         - Block-level elements have a default width of 100%,

         - inline-block elements expand and contract horizontally to accommodate their content.

         - Inline-level elements cannot have a fixed size, thus the width and height properties are only relevant to non-inline elements 

   - total heigh of an element:

      - margin-top + border-top + padding-top + height + padding-bottom + border-bottom + margin-bottom

      - The default height of an element is determined by its content. An element will expand and contract vertically as necessary to accommodate its content

   - Margin: 

      - The margin property allows us to set the amount of space that surrounds an element.

      - top and bottom, are not accepted by inline-level elements

      - These vertical margins are, however, accepted by block-level and inline-block elements.

   - Padding:

      - works vertically on inline-level elements.

   - Borders:

      - fall between the padding and margin, providing an outline around an element.

      - Shorthand values for the border property are stated in that order—**width**, **style**, **color**, `border: 6px solid #949599;`

      - In longhand, these three values can be broken up into the **border-width**, **border-style**, and **border-color** properties.

      - The most common style values are **solid**, **double**, **dashed**, **dotted**, and **none**, but there are several others to choose from.

      - **border-radius** property, which enables us to round the corners of an element

         - `border-radius: 5px;`

         - `border-radius: 50%; /* a circle*/`

   - Box Sizing:

      - `content-box`

      - `padding-box`

      - ` border-box` Good

- Positioning Content

   - `float` property：

      - [CSS Float Theory: Things You Should Know](https://www.smashingmagazine.com/2007/05/css-float-theory-things-you-should-know/)

      - float property allows us to take an element, remove it from the normal flow of a page, and position it to the left or right of its parent element

      - When you float an element it becomes a block box. This box can then be shifted to the left or right on the current line. The markup options are float: left, float: right or float: none.

      - when an element is floated, it will float all the way to the edge of its parent element. If there isn’t a parent element, the floated element will then float all the way to the edge of the page

      - if we use the `clear` property with the value of both on the `<footer>` element, we are able to clear the floats

      - It is important that this clear be applied to an element appearing after the floated elements, not before, to return the page to its normal flow.

- web typography

   - A **typeface** is what we see. It is the artistic impression of how text looks, feels, and reads.

   - A **font** is a file that contains a typeface. Using a font on a computer allows the computer to access the typeface.

   - color property: `color: #555;`

   - `font-family` property is used to declare which font—as well as which fallback or substitute fonts—should be used to display text. 

      - `font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;`

   - `font-size: 14px;`

   - `font-style: italic;`

   - `font-variant: small-caps;`

   - `font-weight: bold;`: Occasionally, we’ll want to style text as bold or to change the specific weight of a typeface. 

      - Keyword values include `normal, bold, bolder, lighter, and inherit`

      - `font-weight: 600;`

   - `line-height: 22px;`

      - Line height, the distance between two lines of text (often referred to as leading) is declared using the line-height property.

- Setting Backgrounds & Gradients:

   - `background-color: #b2b2b2;`

   - `background-color: rgba(0, 0, 0, .3);`

   - `background-image: url("alert.png");`

   - `background-repeat: no-repeat;  or repeat, repeat-x, repeat-y, and no-repeat`

   - `background-position: 20px 10px; or 0% 0%`
      

      ![](https://i.imgur.com/BACrj9l.png)

   - Linear Gradient Background

      - `background:         linear-gradient(#648880, #293f50);`

      - `background: linear-gradient(to right bottom, #648880, #293f50);`

      - `background: radial-gradient(#648880, #293f50);`

      - `background: linear-gradient(to right, #f6f1d3, #648880, #293f50);`

- Building Forms

   - Forms provide a way for websites to capture information from users and to process requests, and they offer controls for nearly every imaginable use of an application.

   - submit: After a user inputs the requested information, buttons allow the user to put that information into action.

      - Users click the submit button to process data after filling out a form. The submit button is created using the `<input>` element with a type attribute value of submit. The value attribute is used to specify the text that appears within the button.

      - `<input type="submit" name="submit" value="Send">`

      - As an `<input>` element, the submit button is self-contained and cannot wrap any other content.

   - `<button>`:

      - The `<button>` element performs the same way as the `<input>` element with the type attribute value of submit; however, it includes opening and closing tags, which may wrap other elements.

   - file input:

      - `<input type="file" name="file">`

      - To allow users to add a file to a form, much like attaching a file to an email, use the file value for the type attribute.

      - Unfortunately, styling an <input> element that has a type attribute value of file is a tough task with CSS. Each browser has its own default input style, and none provide much control to override the default styling. JavaScript and other solutions can be employed to allow for file input, but they are slightly more difficult to construct.

   - lable tag:

   - fieldset tag:

      - Fieldsets group form controls and labels into organized sections. 

      - Much like a `<section>` or other structural element, the `<fieldset>` is a block-level element that wraps related elements, specifically within a `<form>` element, for better organization. 

      - Fieldsets, by default, also include a border outline, which can be modified using CSS.

## [JavaScript Language](https://hackmd.io/@L_VGP_ZqS2WG30NvJnde1g/B1UJvl0CH)

## Frontend Framework

### React:

- Javascript user-interface library written and maintained by Facebook.

# Back-End

## [Database](https://hackmd.io/@L_VGP_ZqS2WG30NvJnde1g/rkV_FQ7zS)

## [Web API](https://hackmd.io/@EricMLYang/B1H_Af1aI)

## Server Software

### apache2 in Ubuntu18.04

- Basic Operation：

   - start Apache：`sudo systemctl start apache2`

   - check status：`sudo systemctl status apache2`
      

      ![](https://i.imgur.com/Mgkr5gu.png)

   - stop Apache：`sudo systemctl stop apache2`

   - restart Apache：`sudo systemctl restart apache2`

- directory structure:

   - default document root: `/var/www/html`

      - search document root: `grep -R "DocumentRoot" /etc/apache2/sites-enabled`

   - config: /etc/apache2/apache2.conf

## [Container](https://hackmd.io/@L_VGP_ZqS2WG30NvJnde1g/HkhsVb2KE)

## [The Node.js best practices list ](https://github.com/goldbergyoni/nodebestpractices#readme)

## Framework

### Django

- 主要參考:[Python新手使用Django架站技術實作：活用Django 2.0 Web Framework建構動態網站的16堂課](https://www.books.com.tw/products/0010790747)

- Basic Instruction:

   - `django-admin help` : list basic command

   - `django-admin startproject project_name`

      - will create a directory with your project name

      - Basic file:

      ```
      Main_Directory  #Project name
      |----- manage.py # 
      |_____ Same_name_with_Main_Directory #put global setting file
      |      |----- __init__.py
      |      |----- settings.py
      |      |----- urls.py
      |      |_____ wsgi.py
      ```

   - `python manage.py startapp app_name`

   - `mkdir media template static`

   - 檔案架構:

      ```
      Main_Directory  #Project name
          |----- manage.py # 
          |_____ Same_name_with_Main_Directory #put global setting file
          |      |----- __init__.py
          |      |----- settings.py
          |      |----- urls.py  # match page with function (logical)
          |      |_____ wsgi.py
          |      |
          |----- APP_Directory #one of many APP
          |      |----- __init__.py
          |      |----- admin.py
          |      |----- apps.py
          |      |----- migrations
          |      |      |----- __init__.py
          |      |      |----- 0001_initial.py
          |      |----- models.py # 
          |      |----- tests.py
          |      |----- views.py
          |      |
          |----- template # .html
          |----- static # .css .js img...
          |----- media # some file
      ```

   - `python manage.py runserver 127.0.0.1:8000`

   - `python manage.py migrate`: default SQLite

   - `python manage.py createsuperuser`

- 一般 MVC 架構把軟體專案區分為：

   - 資料(模型, Model)：包含系統中的資料內容，通常是以資料庫形式儲存，資料變動的話會通知 View 變更，一些處理程式的邏輯也會放這。

   - 顯示(視圖, View)：建立和使用者之間的介面，傳遞使用者的請求給 Controller,並負責依照 Controller 的要求呈現出來自於 Model 中的資源。

   - 控制(Controller)：透過 View 傳來的使用者請求，派發這些請求，並依這些請求進行處理資料內容以及設定要呈現的資料。

- Django MTV：網頁伺服器本身在派發工作時就隱含了控制邏輯，而且網站框架中 Template 的模板文件套用是最常被使用的網頁渲染技巧，因此發展出：

   - Model:

      - 對應到 APP 資料夾中的 [models.py](http://models.py) 檔

      - 以建立 python class 的方式來操作資料庫 

   - Template: 

      - template 放置 \*.html, .js, .css 檔

      - 建立網頁外觀框架，並接資料後呈現最終頁面

      - 資料基本上盡量是可直接顯示的簡單形式

      - 不要在 template 檔案中用複雜方法處理送進來的變量(頂多簡單邏輯判斷)

      - template 保持在前端人員可以獨立處理的狀態

   - View:

      - 對應到 APP 資料夾中的 [view.py](http://view.py) 檔

      - 負責控制如何處理資料城式邏輯

      - 常以 class 或是 funciton 形式與網頁位址一一對應
         

         ![](https://i.imgur.com/WpLU1hL.jpg)

# DevOps

- Resource

   - [The Cathedral and the Bazaar](http://www.catb.org/\~esr/writings/cathedral-bazaar/)

   - [The Phoenix Project](https://school.soft-arch.net/p/on-the-phoenix-project)

   - [Automating Every Aspect of Your Python Project](https://dev.to/martinheinz/automating-every-aspect-of-your-python-project-f5f)

DevOps is the practice of operations and development engineers participating together in the entire service lifecycle, from design through the development process to production support.
...

# Full Stack

A full stack web developer is a person who can develop both client and server software.

## Dash

- Reference:

   - [Bokeh vs Dash — Which is the Best Dashboard Framework for Python?](https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f)

   - [Dash User Guide](https://dash.plot.ly/)

- What is Dash?

   - Dash is a Python framework for building analytical web applications. No JavaScript required.

   - Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python.

   - Underlying frameworks? 

      - Frontend

         - React.js

         - [Plotly.js](https://plot.ly/)

      - Backend: Flask

         - communicating JSON packets over HTTP requests

   - Dash components are Python classes that encode the properties and values of a specific React component and that serialize as JSON. 

### Dash Tutorial:

- Dash apps are composed of two parts. 

   - The first part is the "`layout`".

#### Dash Layout:

- [Dash Layout](https://dash.plot.ly/getting-started)

- imaging `dash.layout` just like a three with some kinds of components

- the python classes for dash layout is in two library:

   - `the dash_html_components` library： has a component for every HTML tag

   - `dash_core_components`library：

      - describe higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library.

      - `Graph` component renders interactive data visualizations using the open source `plotly.js`

- a quikt view:

   ```python
   # -*- coding: utf-8 -*-
   import dash
   import dash_core_components as dcc 
   import dash_html_components as html
   
   external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
   
   app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
   
   app.layout = html.Div(children=[
       html.H1(children='Hello Dash'), #<h1>Hello Dash</h1>
   
       html.Div(children='''
           Dash: A web application framework for Python.
       '''),
   
       dcc.Graph(
           id='example-graph',
           figure={
               'data': [
                   {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                   {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
               ],
               'layout': {
                   'title': 'Dash Data Visualization'
               }
           }
       )
   ])
   
   if __name__ == '__main__':
       app.run_server(debug=True)
   ```

   - The layout is composed of a tree of "components" like `html.Div` and `dcc.Graph`.

   - This application is using a custom CSS stylesheet to modify the default styles of the elements. More detail is in [css tutorial](https://dash.plot.ly/external-resources).

- some style modify about above example:

   ```python
   # -*- coding: utf-8 -*-
   import dash
   import dash_core_components as dcc
   import dash_html_components as html
   
   external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
   
   app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
   
   # a dict to match colors
   colors = {
       'background': '#111111',
       'text': '#7FDBFF'
   }
   
   app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
       html.H1(
           children='Hello Dash',
           # add some style
           style={
               'textAlign': 'center',
               'color': colors['text']
           }
       ),
   
       html.Div(children='Dash: A web application framework for Python.', 
       # add some style 
       style={
           'textAlign': 'center',
           'color': colors['text']
       }),
   
       dcc.Graph(
           id='example-graph-2',
           figure={
               'data': [
                   {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                   {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
               ],
               'layout': { # modify colors
                   'plot_bgcolor': colors['background'],
                   'paper_bgcolor': colors['background'],
                   'font': {
                       'color': colors['text']
                   }
               }
           }
       )
   ])
   
   if __name__ == '__main__':
       app.run_server(debug=True)
   ```

## Django REST API + React(consume the API by HTTP requests)

- [Django/Flask with React.js](https://medium.com/@timmykko/django-flask-with-react-js-3c6da2d47b52)

- REST API

   - [The definitive guide for building REST APIs](https://medium.com/clebertech-en/the-definitive-guide-for-building-rest-apis-f70d37b1d656)

   - [Django REST Framework](https://www.django-rest-framework.org/)

   - [Flask API](http://www.flaskapi.org/)

- [React](https://reactjs.org/):

   - How does React make HTTP Requests?

      - HTTP Requests in JS：JQuery, $.ajax, Fetch, Axios, Superagent, and so on

      - Recommend : **Fetch API** is standardized and uses Promises! 

```python
from __future__ import division

import os
import sys
import time
import json
import datetime
import argparse

import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template, send_file
from werkzeug.utils import secure_filename

from models import *
from utils.utils import *
from utils.datasets import *

from PIL import Image, ImageFont, ImageDraw
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def MockResponse():
	#this_file_path = os.path.abspath(__file__)
	#here = os.path.dirname(this_file_path)
	here = "/var/www/flaskApp"
	model_def =  os.path.join(here, "config/yolov3.cfg")
	img_size = 416
	weights_path = os.path.join(here, "weights/yolov3.weights")
	image_folder = os.path.join(here, "data/samples/")
	batch_size = 1
	n_cpu = 0
	class_path = os.path.join(here, "data/coco.names")


	#os.makedirs("output", exist_ok=True)
	# Set up model
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
	model = Darknet(model_def, img_size=img_size).to(device)
	if weights_path.endswith(".weights"):
		# Load darknet weights
		model.load_darknet_weights(weights_path)
	else:
		# Load checkpoint weights
		model.load_state_dict(torch.load(weights_path))


	model.eval()  # Set in evaluation mode
	dataloader = DataLoader(
		ImageFolder(image_folder, img_size=img_size),
		batch_size=batch_size,
		shuffle=False,
		num_workers=n_cpu,
	)
	classes = load_classes(class_path)  # Extracts class labels from file
	Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

	imgs = []  # Stores image paths
	img_detections = []  # Stores detections for each image index

	prev_time = time.time()
	for batch_i, (img_paths, input_imgs) in enumerate(dataloader):
		# Configure input
		input_imgs = Variable(input_imgs.type(Tensor))

		# Get detections
		with torch.no_grad():
			detections = model(input_imgs)
			detections = non_max_suppression(detections, 0.8, 0.4)

		# Log progress
		current_time = time.time()
		inference_time = datetime.timedelta(seconds=current_time - prev_time)
		prev_time = current_time
		#print("\t+ Batch %d, Inference Time: %s" % (batch_i, inference_time))

		# Save image and detections
		imgs.extend(img_paths)
		img_detections.extend(detections)

	# Bounding-box colors
	cmap = plt.get_cmap("tab20b")
	colors = [cmap(i) for i in np.linspace(0, 1, 20)]

	# Iterate through images and save plot of detections
	for img_i, (path, detections) in enumerate(zip(imgs, img_detections)):
		# Draw bounding boxes and labels of detections
		# Create plot
		img = Image.open(path).convert("RGB")
		draw = ImageDraw.Draw(img)

		if detections is not None:
			# Rescale boxes to original image
			detections = rescale_boxes(detections, img_size, np.array(img).shape[:2])
			unique_labels = detections[:, -1].cpu().unique()
			n_cls_preds = len(unique_labels)
			bbox_colors = random.sample(colors, n_cls_preds)
			for idx, (x1, y1, x2, y2, conf, cls_conf, cls_pred) in enumerate(detections):
				x1 = x1.data
				y1 = y1.data
				x2 = x2.data
				y2 = y2.data
				draw.rectangle(((x1, y1), (x2, y2)), outline='red')
				draw.text((x1, y1), classes[int(cls_pred)], fill=(255,255,255,128))
		filename = path.split("/")[-1].split(".")[0]
		img.save(f"/var/www/flaskApp/output/{filename}.jpg", "JPEG")

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
            
            #將檔案儲存至磁碟，在這裡請指定其他程式可以抓到的地方
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			MockResponse()
			refilename = filename.split("/")[-1].split(".")[0]
            #將結果的 JSON 回傳
			#response = app.response_class(response=result, status=200, mimetype="application/json")
			return send_file("/var/www/flaskApp/output/" + refilename +".jpg", mimetype='image/jpg')
                        #return response
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)
    
if __name__ == "__main__":
	app.run()
```