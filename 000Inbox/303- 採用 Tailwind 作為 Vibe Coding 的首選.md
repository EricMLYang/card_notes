---
tags:
  - permanent-note
---
# 303- 採用 Tailwind 作為 Vibe Coding 的首選

- 重新審視傳統 CSS 最佳實踐。過去那些針對人類開發者和網路效能優化的做法，在 AI coding 的場景下可能不再是最佳解。



- Vibe Coding 的想法是，未來我會儘量採用 tailwind 那種 utility first 的做法，然後捨棄過去的一些 Web 在 CSS 處理上的 Best practice。



為什麼要選擇 Tailwind。

▌ AI 沒辦法精準判斷 CSS

css 可橫跨多檔案，有覆蓋狀況，且必須要去尋找樣式檔案，特別是除了有外部的 css 檔案，也可能有寫在 html 裡面的 inline css，透過 AI 開發時就可能會有樣式打架的狀況發生。



▌ 檔案可能太大

傳統 external css，為了降低 html 的檔案大小，然後利用 caching 避免檔案多次下載，所以集中在幾個 stylesheet 的做法，最終可能導致的是 css 檔案太大，超出 context window，讓 AI 難以讀取。 



▌ 樣式衝突

集中式的 external css 很容易造成改 A 壞 B 的狀況，這個在專案變大的時候，這個問題就會更容易浮現，Vibe Coding 更是如此。



▌ tailwind 提供了精準的 context

explicit is better thant implicit, 這句話是 python 重要的原則。

而 tailwind 在 html 裡面明確的定義了所有的設計樣式，而過去的 external css 的做法則是留下了語意式的 class, 但卻無關設計，對於 AI 來說， context 至關重要，Framework 是 context、架構是 context, 檔案結構也是 context，AI 時代，提供精準的 context 絕對是最重要的事情。

根據上述的想法，我覺得精準，並且直接提供完整設計樣式的 context 才是比較適合 AI，並且能夠加速 Vibe Coding 的做法。




