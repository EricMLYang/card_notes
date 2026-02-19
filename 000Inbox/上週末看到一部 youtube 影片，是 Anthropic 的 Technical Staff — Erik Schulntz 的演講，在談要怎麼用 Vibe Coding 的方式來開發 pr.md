上週末看到一部 youtube 影片，是 Anthropic 的 Technical Staff — Erik Schulntz 的演講，在談要怎麼用 Vibe Coding 的方式來開發 production 的產品，他提到的方法也有在 Claude 內部使用。

影片內容不長，但概念卻很實用，也再次提醒我使用 AI 工具來開發軟體時，必須以「負責任」的態度來實作。

https://youtu.be/fHWFF_pnqDk?si=\_-0ELiJANqpku_GX

他提到的核心概念是，為了避免 Vibe Coding 產生的技術債，我們應該讓 Agent 專注在開發屬於葉節點（leaf node）的程式碼，而核心節點（core node）則仍需要工程師完全理解寫出來的程式碼。

什麼是 葉節點（leaf node） 跟 核心節點（core node）？