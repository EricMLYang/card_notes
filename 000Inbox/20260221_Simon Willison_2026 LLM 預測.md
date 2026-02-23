# LLM predictions for 2026

> 來源：Simon Willison's Blog
> 連結：https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/
> 搜集日期：2026-02-21
> 搜集原因：LLM 產業分析、AI 對工作角色的衝擊

## 摘要
Simon Willison（Django 共同創辦人、LLM 領域最受敬重的獨立聲音之一）分享他對 LLM 未來的預測，分三個時間尺度。觀點犀利且具體，特別是對編碼代理安全風險的警告值得關注。

## 關鍵段落

### 一年內預測
- **LLM 編程能力已不可否認**：2025 年的推理模型透過強化學習訓練，大幅提升代碼生成品質
- **沙箱隔離技術將成熟**：開發者終於能安全執行 AI 生成的程式碼
- **編碼代理安全危機**：可能出現「挑戰者號災難」級別的安全事件，因為許多人執行編碼代理時缺乏防護

### 三年內預測
- **傑文斯悖論的解答**：編碼成本下降是否讓工程師貶值，或因需求增加而更值錢？答案將在三年內明確
- **AI 協助建構完整瀏覽器**：將成為常態而非特例

### 六年內預測
- **手寫程式碼淘汰**：工程師將不再花工作時間在文字編輯器中手動輸入程式碼，如同打孔卡已消亡

## 潛在卡片方向
- 編碼代理的「挑戰者號時刻」：安全風險的臨界點預測
- 傑文斯悖論在軟體工程的應用：成本下降 → 需求增加 or 價值貶值？
- 與現有卡片連結：[[AI 時代應該轉變成槓桿思維]]

---
*由 scout-news 流程搜集，待 process-inbox 處理*

Simon Willison’s Weblog
Subscribe
Sponsored by: Teleport — Secure, Govern, and Operate AI at Engineering Scale. Learn more
LLM predictions for 2026, shared with Oxide and Friends
I joined a recording of the Oxide and Friends podcast on Tuesday to talk about 1, 3 and 6 year predictions for the tech industry. This is my second appearance on their annual predictions episode, you can see my predictions from January 2025 here. Here’s the page for this year’s episode, with options to listen in all of your favorite podcast apps or directly on YouTube.

Bryan Cantrill started the episode by declaring that he’s never been so unsure about what’s coming in the next year. I share that uncertainty—the significant advances in coding agents just in the last two months have left me certain that things will change significantly, but unclear as to what those changes will be.

Here are the predictions I shared in the episode.

1 year: It will become undeniable that LLMs write good code
1 year: We’re finally going to solve sandboxing
1 year: A “Challenger disaster” for coding agent security
1 year: Kākāpō parrots will have an outstanding breeding season
3 years: the coding agents Jevons paradox for software engineering will resolve, one way or the other
3 years: Someone will build a new browser using mainly AI-assisted coding and it won’t even be a surprise
6 years: Typing code by hand will go the way of punch cards
1 year: It will become undeniable that LLMs write good code ▶ 19:27 #
I think that there are still people out there who are convinced that LLMs cannot write good code. Those people are in for a very nasty shock in 2026. I do not think it will be possible to get to the end of even the next three months while still holding on to that idea that the code they write is all junk and it’s it’s likely any decent human programmer will write better code than they will.

In 2023, saying that LLMs write garbage code was entirely correct. For most of 2024 that stayed true. In 2025 that changed, but you could be forgiven for continuing to hold out. In 2026 the quality of LLM-generated code will become impossible to deny.

I base this on my own experience—I’ve spent more time exploring AI-assisted programming than most.

The key change in 2025 (see my overview for the year) was the introduction of “reasoning models” trained specifically against code using Reinforcement Learning. The major labs spent a full year competing with each other on who could get the best code capabilities from their models, and that problem turns out to be perfectly attuned to RL since code challenges come with built-in verifiable success conditions.

Since Claude Opus 4.5 and GPT-5.2 came out in November and December respectively the amount of code I’ve written by hand has dropped to a single digit percentage of my overall output. The same is true for many other expert programmers I know.

At this point if you continue to argue that LLMs write useless code you’re damaging your own credibility.

1 year: We’re finally going to solve sandboxing ▶ 20:05 #
I think this year is the year we’re going to solve sandboxing. I want to run code other people have written on my computing devices without it destroying my computing devices if it’s malicious or has bugs. [...] It’s crazy that it’s 2026 and I still pip install random code and then execute it in a way that it can steal all of my data and delete all my files. [...] I don’t want to run a piece of code on any of my devices that somebody else wrote outside of sandbox ever again.

This isn’t just about LLMs, but it becomes even more important now there are so many more people writing code often without knowing what they’re doing. Sandboxing is also a key part of the battle against prompt injection.

We have a lot of promising technologies in play already for this—containers and WebAssembly being the two I’m most optimistic about. There’s real commercial value involved in solving this problem. The pieces are there, what’s needed is UX work to reduce the friction in using them productively and securely.

1 year: A “Challenger disaster” for coding agent security ▶ 21:21 #
I think we’re due a Challenger disaster with respect to coding agent security[...] I think so many people, myself included, are running these coding agents practically as root, right? We’re letting them do all of this stuff. And every time I do it, my computer doesn’t get wiped. I’m like, “oh, it’s fine”.

I used this as an opportunity to promote my favourite recent essay about AI security, the Normalization of Deviance in AI by Johann Rehberger.

The Normalization of Deviance describes the phenomenon where people and organizations get used to operating in an unsafe manner because nothing bad has happened to them yet, which can result in enormous problems (like the 1986 Challenger disaster) when their luck runs out.

Every six months I predict that a headline-grabbing prompt injection attack is coming soon, and every six months it doesn’t happen. This is my most recent version of that prediction!

1 year: Kākāpō parrots will have an outstanding breeding season ▶ 50:06 #
(I dropped this one to lighten the mood after a discussion of the deep sense of existential dread that many programmers are feeling right now!)

I think that Kākāpō parrots in New Zealand are going to have an outstanding breeding season. The reason I think this is that the Rimu trees are in fruit right now. There’s only 250 of them, and they only breed if the Rimu trees have a good fruiting. The Rimu trees have been terrible since 2019, but this year the Rimu trees were all blooming. There are researchers saying that all 87 females of breeding age might lay an egg. And for a species with only 250 remaining parrots that’s great news.

(I just checked Wikipedia and I was right with the parrot numbers but wrong about the last good breeding season, apparently 2022 was a good year too.)

In a year with precious little in the form of good news I am utterly delighted to share this story. Here’s more:

Kākāpō breeding season 2026 introduction from the Department of Conservation from June 2025 .
Bumper breeding season for kākāpō on the cards—3rd December 2025, University of Auckland.
I don’t often use AI-generated images on this blog, but the Kākāpō image the Oxide team created for this episode is just perfect:

A beautiful green Kākāpō surrounded by candles gazes into a crystal ball

3 years: the coding agents Jevons paradox for software engineering will resolve, one way or the other ▶ 54:37 #
We will find out if the Jevons paradox saves our careers or not. This is a big question that anyone who’s a software engineer has right now: we are driving the cost of actually producing working code down to a fraction of what it used to cost. Does that mean that our careers are completely devalued and we all have to learn to live on a tenth of our incomes, or does it mean that the demand for software, for custom software goes up by a factor of 10 and now our skills are even more valuable because you can hire me and I can build you 10 times the software I used to be able to? I think by three years we will know for sure which way that one went.

The quote says it all. There are two ways this coding agents thing could go: it could turn out software engineering skills are devalued, or it could turn out we’re more valuable and effective than ever before.

I’m crossing my fingers for the latter! So far it feels to me like it’s working out that way.

3 years: Someone will build a new browser using mainly AI-assisted coding and it won’t even be a surprise ▶ 65:13 #
I think somebody will have built a full web browser mostly using AI assistance, and it won’t even be surprising. Rolling a new web browser is one of the most complicated software projects I can imagine[...] the cheat code is the conformance suites. If there are existing tests that it’ll get so much easier.

A common complaint today from AI coding skeptics is that LLMs are fine for toy projects but can’t be used for anything large and serious.

I think within 3 years that will be comprehensively proven incorrect, to the point that it won’t even be controversial anymore.

I picked a web browser here because so much of the work building a browser involves writing code that has to conform to an enormous and daunting selection of both formal tests and informal websites-in-the-wild.

Coding agents are really good at tasks where you can define a concrete goal and then set them to work iterating in that direction.

A web browser is the most ambitious project I can think of that leans into those capabilities.

6 years: Typing code by hand will go the way of punch cards ▶ 80:39 #
I think the job of being paid money to type code into a computer will go the same way as punching punch cards [...] in six years time, I do not think anyone will be paid to just to do the thing where you type the code. I think software engineering will still be an enormous career. I just think the software engineers won’t be spending multiple hours of their day in a text editor typing out syntax.

The more time I spend on AI-assisted programming the less afraid I am for my job, because it turns out building software—especially at the rate it’s now possible to build—still requires enormous skill, experience and depth of understanding.

The skills are changing though! Being able to read a detailed specification and transform it into lines of code is the thing that’s being automated away. What’s left is everything else, and the more time I spend working with coding agents the larger that “everything else” becomes.

Posted 8th January 2026 at 7:42 pm · Follow me on Mastodon, Bluesky, Twitter or subscribe to my newsletter
More recent articles
Adding TILs, releases, museums, tools and research to my blog - 20th February 2026
Two new Showboat tools: Chartroom and datasette-showboat - 17th February 2026
Deep Blue - 15th February 2026