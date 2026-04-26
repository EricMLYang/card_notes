---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-23
---

## [重點]
用 Claude Code 當主要設計工具一個多月以來，他做出了三層式定價頁面（含比較表、testimonial、FAQ）、Tailwind Labs 內部用的金融 dashboard，而且整個過程沒有用任何 skills 或 CLAUDE.md，就是從空白畫面開始對 Claude 講話。

## [摘要]


## [詮釋]


---
再見了 Figma ? 設計師公開他的 Claude Code 工作流：18 條設計技巧完整拆解

Fox Hsiao
22 3月 2026 — 12 min read

Tailwind CSS 的設計師 Steve Schoger 最近發了一支一小時的影片，展示他怎麼用 Claude Code 從零建出一個金融 App 的行銷首頁。影片開頭他就先打了預防針：「我對命令列還是非常新手，這些東西對我來說都很陌生。Adam Wathan 幫我做了初始設定，現在我就是有一個 Vite 專案模板，每次開新專案就複製一份。」

他說自己大概只會兩件事，換目錄和啟動 Claude。但用 Claude Code 當主要設計工具一個多月以來，他做出了三層式定價頁面（含比較表、testimonial、FAQ）、Tailwind Labs 內部用的金融 dashboard，而且整個過程沒有用任何 skills 或 CLAUDE.md，就是從空白畫面開始對 Claude 講話。

這支影片最有價值的部分，是他在一小時的操作過程中不斷穿插實戰設計技巧，從字型選擇、邊框處理、按鈕細節到整頁裝飾，每一個都是他身為專業設計師多年累積的判斷。以下是完整的 16 條技巧拆解。

Steve Schoger 是誰
Steve Schoger 是 Tailwind Labs 的設計師，跟 Tailwind CSS 的創辦人 Adam Wathan 長期合作。他目前正在開發一款叫 UI.SH 的工具，是給 Claude Code、Cursor、Amp 這些 AI coding agent 使用的 skills 套件，讓 AI 在寫前端程式碼的時候能套用專業級的設計標準。

他的工作流程很簡單，左邊是瀏覽器顯示 localhost 的即時預覽，右邊是 Claude Code 的終端，中間沒有 Figma。他說現在開 Figma 的唯一理由是做向量圖形（SVG logo 之類的），其他全部在 Claude Code 裡完成。他用的技術棧是 Vite + Tailwind CSS + React，但他自己不寫 CSS，所有樣式都是用自然語言告訴 Claude 要什麼效果。

他的起手 prompt 大意是：「幫一個金融 app 設計一個簡單的行銷首頁，這個 app 把所有收入來源整合到一個 dashboard 裡。頁面要包含導覽列、hero 區塊、logo 列、功能介紹、數據統計、使用者推薦、CTA 區塊和頁尾。」Claude 生成初版之後，他花了大約 50 次迭代式的對話，一步步把它從「AI 預設輸出」調整成專業水準的成品。

邊框與陰影：讓元素看起來乾淨的關鍵


1. 用 outer ring 取代 solid border
這是 Schoger 在影片中反覆強調的核心技巧。當一個元素同時有陰影（shadow）和實色邊框（border）的時候，陰影和邊框之間會產生一種「muddy」（混濁）的效果，視覺上很髒。他的做法是完全不用 border，改用 outer ring，顏色設為 gray-950、opacity 10%，放在元素外側。這樣陰影和邊緣之間的過渡更銳利、更乾淨。這個技巧他套用在截圖容器、按鈕、navbar、feature card 上，幾乎所有有陰影的元素都適用。

2. Concentric radius（同心圓角）
當一個圓角容器裡面放了另一個圓角元素（比如截圖放在卡片裡），內層的 border-radius 應該等於外層的 radius 減去 padding。這樣兩層圓角會形成同心圓，視覺上才和諧。如果內外層用同樣的 radius 值，間距小的時候看起來會很彆扭。

3. Inset ring 做邊緣定義
在淡色背景的容器上，用 inset ring（5% opacity）做邊緣定義，取代傳統的 border。這個方式比 border 更微妙，不會搶走容器內容的視覺焦點。

Typography：字型的細節決定專業感


4. 用 Inter variable 的 display 版本
Schoger 推薦從 rsms.me 下載 Inter 的 variable 版本，而非 Google Fonts 上的標準版。variable font 的好處是可以用「中間」字重，比如 550（介於 medium 500 和 semi-bold 600 之間），這在標準版是做不到的。他還特別關閉了一個 OpenType 特性：帶尾巴的小寫 L 變體（stylistic set ss02），因為這個變體在某些情境下會讓字看起來怪怪的。

5. 大字體要收緊 tracking
24px 以上的大字體，字距（tracking / letter-spacing）要比預設值再緊一點。字越大，字母之間的空隙在視覺上會被放大，收緊 tracking 可以讓標題更有衝擊力、更緊湊。他在 Tailwind 裡用 tracking-tight 甚至更緊的值。

6. Eyebrow 文字用 monospace
section 標題上方的小標籤（eyebrow text，像是「你需要的一切」「立即開始」這類），Schoger 有一套固定公式：用 Geist Mono 字型、全大寫（uppercase）、加寬字距（tracking-wider）、小字體（text-xs）、灰色（gray-600）。monospace 字型讓這些短文字看起來更技術感、更精緻。

7. text-pretty vs text-balance
Tailwind CSS 有兩個文字排版 utility：text-pretty 避免段末出現孤字（orphan word），text-balance 讓文字行更均勻分布。兩者效果不同，需要根據具體情況選用。Schoger 在不同的文字區塊之間會來回切換測試哪個效果更好。

8. 小字體行高可以翻倍
14px（text-sm）的文字，行高可以設為 28px（字體大小的兩倍）。這聽起來很誇張，但對於副標題或說明文字來說，更大的行距讓文字有更多呼吸空間，閱讀起來更舒服。

版面佈局：打破 AI 的置中預設


9. 左對齊取代置中
AI 生成的網頁幾乎都是置中對齊，Schoger 第一件事就是把 hero 改成左對齊。他參考的是 Tailwind Plus 網站的 split headline 佈局：標題放左側（約 3/5 寬），副標和描述文字放右側（約 2/5 寬），頂部對齊。這種佈局比全部置中更有設計感，也更容易閱讀。

10. Inline section heading
feature section 的標題，Schoger 不用傳統的「大標題 + 換行 + 副標」結構，而是把標題和副標放在同一行，用不同的顏色和字重區分。標題用深色粗體（neutral-950），副標接在後面用灰色中等字重（neutral-600, medium）。他說這個風格的靈感來自 Apple、Linear、Stripe、Adio，需要比較長的副標文案才能撐起這個效果。

11. max-width 用 ch 單位
控制文字區塊的最大寬度，Schoger 不用固定像素，而是用 ch 單位（基於字型中 0 字元的寬度）。比如 max-w-[40ch] 大約等於 40 個字元寬。好處是不管字體大小怎麼變，閱讀寬度都維持在舒適的範圍。他在調的時候自嘲：「有時候就是要一個一個試，找到剛剛好的那個。」試了 45、40、35，最後選了 40。

元素設計：按鈕、容器、截圖


12. 按鈕的高度和形狀
Schoger 偏好 36 到 38px 的按鈕高度，用 padding 控制而非固定 height。形狀是 pill-shaped（全圓角），字體 14px（text-sm）。他會把 AI 預設加在按鈕裡的 icon 拿掉，保持乾淨。

13. 兩個按鈕高度差 2px 怎麼辦
這是影片裡最令人印象深刻的細節之一，當一個按鈕有 ring（外框），另一個沒有的時候，有 ring 的按鈕會比沒有的高 2px。Schoger 說：「這就是我失眠的原因。」Adam Wathan 的解法是用一個 span 包裹有 border 的按鈕，設定 inline-flex + p-px，再用 calc 計算，讓兩個按鈕視覺上完全等高。Schoger 坦承：「老實說這個我自己想不出來，這是 Adam Wathan 的魔法。」

14. Well-styled container（凹陷容器）
feature section 裡的截圖容器，Schoger 給它一個極淡的背景色（gray-950 at 2.5% 到 5% opacity），移除邊框，讓截圖本身更突出。截圖從底部裁切（底部零 padding、無底部圓角），製造一種截圖「坐在容器底部」的效果。再加上 inset ring（5% opacity）做邊緣定義。

15. 截圖是最好的視覺元素
如果你沒有自訂圖形或插畫，在首頁放一張 app 的高解析度截圖，是讓頁面瞬間有視覺焦點的最簡單方法。Schoger 特別要求 Claude 用 3x 解析度擷取截圖，確保在高 DPI 螢幕上也是清晰的。

裝飾與細節：讓網站看起來不像模板


16. Canvas grid（裝飾性邊框網格）
這是影片最後加的收尾裝飾，在整個網站的各個 section 之間加上裝飾性的線條邊框。水平線延伸到 viewport 全寬，垂直線保持在 page container 寬度內，形成一種精緻的網格框架。Schoger 說靈感來自 Stripe、Adio 和 Tailwind 官網。如果你沒有自訂圖形資源，這是讓網站瞬間脫離「模板感」的好技巧。

17. 背景圖片 testimonial card
testimonial 區塊不用傳統的頭像 + 引言結構，而是用 AI 生成的人像照片當卡片背景，底部加暗色漸層（gradient shim），讓白色引言文字在照片上清晰可讀。這種風格比標準的圓形頭像有視覺衝擊力得多。

18. Logo cloud 處理
partner logo 列不需要標題，直接放 logo 就很清楚。用真實的 SVG logo 而非文字，移除 opacity（直接用 gray-950），佈滿容器寬度。簡單但很多人會過度設計這個區塊。

Claude Code 的 prompt 策略：設計師怎麼跟 AI 說話
Schoger 跟 Claude Code 的對話方式，跟工程師完全不同。他不寫程式碼，不指定 CSS 屬性，他用的是設計語言。

具體的值他會直接說，像是「改成 38 像素」「改成 gray-950」。模糊的方向也能用，像是「再大一點點」「再緊一點」。他甚至自嘲：「我覺得我寫的這些句子根本不太合理，但它每次都聽得懂。」

有幾個特別有效的 prompt 模式，第一個是問「這個是怎麼做的？」，用來檢查 Claude 的實作方式，發現問題再指出修正。第二個是全站同步，叫 Claude「把這個樣式套用到下面所有區塊」，一次統一風格。第三個是建立臨時工具，他要求 Claude 做了一個拖曳定位工具，讓他可以視覺化地調整截圖位置，調好後複製座標值寫進程式碼，再移除工具。

最讓他驚訝的是 Claude 會自己學習風格一致性。「它就是一邊做一邊學，這還蠻好的，我不需要再額外更新。」後面新增的按鈕自動套用了他之前定義的 ring 樣式，不需要額外指示。

整個過程他沒有用任何 skills 或 CLAUDE.md，也沒有寫任何程式碼。他用的是二十年設計經驗累積的眼光，Claude Code 負責把這些設計意圖轉成 Tailwind CSS。

UI.SH 和設計師的下一步
影片最後，Schoger 推廣了他和 Adam Wathan 正在開發的 UI.SH。這是一套給 AI coding agent 用的 skills 套件，目標是把他在影片裡手動教 Claude 的那些設計原則，預先打包成 agent 可以直接引用的設計標準。支援 Claude Code、Cursor、Amp。

這個方向很有意思，Schoger 的影片證明了一件事：AI 生成的初版網頁和專業設計師的成品之間，差距不在程式碼，在設計判斷。AI 會用 indigo 當預設色、會把所有東西置中、會用 solid border 配 shadow 製造混濁效果。設計師知道該把它改成什麼，但以前需要自己動手寫 CSS 或在 Figma 裡畫。現在只需要說出來就好。

Schoger 的 before/after 對比很有說服力。同一個 prompt 生成的初版，經過大約 50 次設計師主導的迭代，變成了一個看起來完全不同的網站。差異不在技術，在眼光。

---

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：Tailwind 設計師 Steve Schoger 用 Claude Code 一個多月當主要設計工具，沒有 skills、沒有 CLAUDE.md，只用設計語言對話 50 輪左右就能把 AI 預設輸出（置中、indigo、solid border + shadow 混濁）調成專業水準。中間穿插 18 條設計技巧，本質上每一條都是 AI 抓不到、必須由設計師補上的「眼光」。最後指出：AI 與專業作品的差距不在 code，在設計判斷。
- 作者挑戰的預設：取代 Figma 需要工程能力或 prompt 工程訓練。實際上需要的是「眼光」——知道哪裡不對、知道用什麼語彙描述。
- 個人映射：強化「AI 把執行門檻降低，把判斷門檻凸顯」的主軸，可串接到 Stitch 削弱 SaaS 護城河、Coding Agent 角色重定義；同時帶出「設計品味作為 AI 時代護城河」的個人定位視角。

## B. 候選卡（Lite）

序號 1
- 候選標題：AI 與專業作品的差距不在 code，在設計判斷
- 分級：Core
- 類型：Principle
- 核心內容：同一個 prompt 生成的初版頁面，經過 50 輪設計師主導迭代，變成完全不同的成品。差異不是技術，而是「知道哪裡不對、知道該改成什麼」。AI 會用 indigo、會置中、會用 solid border 配 shadow（製造 muddy 效果），這些是無人挑就會發生的預設。設計師的價值從「會畫」變成「能挑」與「能描述要什麼」——眼光成為新時代的核心資產。
- 保留理由：高遷移性的「執行 vs 判斷」原則，可套到寫作、資料分析、PM。
- 待補強處：缺乏「眼光如何系統化訓練給新進設計師」的延伸。
- 初步知識鉤子：判斷力 vs 執行力、AI 把執行門檻降低、Vertical AI 護城河、品味作為降噪器。

序號 2
- 候選標題：對 AI 講「設計語言」的三類有效模式：具體值、模糊方向、風格遷移
- 分級：Support
- 類型：Pattern
- 核心內容：Schoger 的 prompt 三種有效模式：① 具體值（「改成 38 像素」「改成 gray-950」）；② 模糊方向（「再大一點點」「再緊一點」）；③ 全站同步（「把這個樣式套用到下面所有區塊」）。第三種特別有意思——AI 會自己學風格一致性，不需要每次重複指示。這把「跟 AI 說設計」從工程語言解放出來，回到設計師原生詞彙。
- 保留理由：把「跟 AI 對話」具體化為三種可遷移模式。
- 待補強處：模糊方向何時會失敗（如品味落差大時）未討論。
- 初步知識鉤子：自然語言介面、Style Transfer、Prompt Vocabulary、AI 與專業協作。

序號 3
- 候選標題：AI 預設輸出的三大反模式：置中、indigo、solid border + shadow
- 分級：Support
- 類型：Warning
- 核心內容：AI 生成 UI 有三個反覆出現的預設反模式：① 所有東西置中（缺乏視覺層次）；② 預設用 indigo 配色（caused by training data 偏誤）；③ solid border + shadow 同時用造成 muddy 邊緣。設計師的第一輪迭代多半在改這三件事。識別這些「AI 預設陷阱」可以快速 raise 整體品質，是 AI 輔助設計的 baseline 修補清單。
- 保留理由：可遷移成「AI 預設反模式清單」這類診斷工具的範本。
- 待補強處：其他領域（寫作、資料分析）的 AI 預設反模式對照未列。
- 初步知識鉤子：AI Default Bias、Diagnostic Checklist、Style Anti-pattern。

序號 4
- 候選標題：AI 一邊做一邊學風格一致性，不需要 CLAUDE.md
- 分級：Support
- 類型：Pattern
- 核心內容：Schoger 全程沒用 skills 或 CLAUDE.md，但 Claude 會自己從前面對話學到「這個專案用 outer ring 不用 border」並套到後面新增的元件。這提示一件事：對於相對短期、單人、單一檔案的設計工作流，session 內 context 已足以維持風格一致性，不一定需要先做完整的 skill / config。在「先把工作做完」與「先把流程系統化」之間，需要根據規模選擇。
- 保留理由：補上「不需要 over-engineering 設定」的反例，與 Superpowers 強紀律形成有意義對照。
- 待補強處：什麼規模、什麼期間後就需要 CLAUDE.md 介入未說。
- 初步知識鉤子：Context Persistence、Skill vs Session、過度工程警示、Methodology Sizing。

## C. 建議送 refine 的項目
- 序號 1（Core Principle）為主軸
- 序號 2、3、4 為補強

## D. 呼叫 refine-cards
- 將上述候選卡交由 refine-cards 精煉。
