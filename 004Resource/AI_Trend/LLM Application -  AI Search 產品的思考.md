---
tags:
  - llm-application
---
# LLM Application -  AI Search 產品的思考

- Search + LLM其實80%的功勞是在 Search

   - 網路上的 content 量超大，大機率有一堆用戶曾出現一樣的需求、並分享過一樣的經歷，因此不太需要深入理解用戶需求，只需要靠網路內容來滿足，

   - 因此Search + LLM其實只要套用足夠好的Search ，大多可以打造成一個不錯的產品，而LLM只需要做內容的歸類、總結以及移除不相關的內容

   - 文章：The Many Ways that Digital Minds Can Know



- 越來越多 open source 的 Search + LLM 的 project ，每一個都可以達到perplexity 70\~80%的效果，因此Search + LLM在2023年底到2024年，明顯走向更專業化以及更滿足特定需求的方向，具體有幾種方向：

   - [Perplexity.ai](Perplexity.ai)的UIUX，[個人認為大部分LLM產品的UX問題都可以在Perplexity.ai](個人認為大部分LLM產品的UX問題都可以在Perplexity.ai)的介面中找到答案。

   - [Perplexity.ai](Perplexity.ai)的copilot mode，可以反問，來更好的跟user互動、最簡化找到正確content的flow

   - [You.com](You.com)的Research mode（秘塔AI搜索的研究模式也是），滿足大家搜索網路的時候會「大量蒐集參考資料、並且總結各種資料變成一個完整的研究、分析報告」這個需求。

   - Google Gemini的Audit with Google的設計，可以讓user更好驗證答案。

   - 領域專業化，針對領域的所有可能性的任務把服務、介面做好，<http://xn--devv-4h0gy4d.xn--aireportify-os86a.cc/>



- 值得參考的產品，LLM+search Product:

   - [Perplexity.ai](Perplexity.ai)[:](https://l.facebook.com/l.php?u=http%3A%2F%2FPerplexity.ai%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR0vzwxsFlOX-eht3avK4H2EVc0DvXNA074REZp4fYFvt17_uJCMh7T1tNI_aem_AePppulPNbKjUhRwwUl2de_cqBs2lP1zN9eu-j29HfERXLHuvuUQQkbVZIWkzR4G_1CWrH3ZoIG9YMDoh55cPpz6&h=AT1z9Ot3jLnC_0J8vS-ezjWMFOvRWFHrNFvXIPY6loXzUtTo-yl7MkpTqTPXgxRGF7NNHdldEAlrjhyBoMbqgLY_Pw4WxWSU4HZuyd4WBVJqIMh4F0QQAgMstxWC-FenENzz5blbdw&\__tn_\_=-UK-y-R&c\[0\]=AT3gjetHCqlPuKiJihB33hkMC8PHJ0Ig9PeQL6fw9EfXjA1CHxuj1RdGZQqpc7j-dv_0nj65UyYCuKU4jzzRsXa1LSgQCTfQ-RmWsWgh-AOPVqS4_QD-rcLbNt3PAwd-\_QXfYwoOXFpwQDSwSryoOD4K10lodVbZsBMdm06nI7pHomFcMQUCfV5xRKYY8hVsR8cylzKVTIBLW6oASMWmKJYaf_KFXd2rO24OEHqpF4CsBu-NEGKI3PxEuwsiTw) <https://www.perplexity.ai/>（尤其值得參考copilot mode）

   - [You.com](You.com)[:](https://l.facebook.com/l.php?u=http%3A%2F%2FYou.com%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR2IYQ95h_TORbXSPBP6SO-xk5qez9IuuN_N4Tn4WvPFA66CoZJg1KyiZ3M_aem_AeO3oxDwljis64T76jXYn_AVnylpiKVC0wUVujImu4fmZ0Wjc0TVdly3TWcTHdrvrIFVgm6P5ZMNk6BYgJw52EDS&h=AT1wyqQoq6e6aaHbCsPumojHc6_7FJmNZbL1JtnrQO6O3CWIwVboOPQke7PuynAw0m1o_EZItAr46ZCjZWWKbkIqr1pcyDve72SQ94RGcA_8doQ5o9NvSP1pIUY_zqyuRH1CiTNB_w&\__tn_\_=-UK-y-R&c\[0\]=AT3gjetHCqlPuKiJihB33hkMC8PHJ0Ig9PeQL6fw9EfXjA1CHxuj1RdGZQqpc7j-dv_0nj65UyYCuKU4jzzRsXa1LSgQCTfQ-RmWsWgh-AOPVqS4_QD-rcLbNt3PAwd-\_QXfYwoOXFpwQDSwSryoOD4K10lodVbZsBMdm06nI7pHomFcMQUCfV5xRKYY8hVsR8cylzKVTIBLW6oASMWmKJYaf_KFXd2rO24OEHqpF4CsBu-NEGKI3PxEuwsiTw) \[[You.com](You.com)\](<https://you.com/>)（尤其值得參考Research mode）

   - Bing Chat: <https://www.bing.com/chat>

   - Google Gemini: <https://gemini.google.com/app>（值得參考Audit with Google的設計）

   - 秘塔AI搜索: <https://metaso.cn/>

   - 工程師專用Search服務，[devv.ai](devv.ai)[:](https://l.facebook.com/l.php?u=https%3A%2F%2Fdevv.ai%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR0NrczMwvhUkgBjr4VpcC41lJbfQc6JpwDZr6jb8pmBH3jvuQdYoxsB_w4_aem_AeNWMaR1telT8SDnBFdOZHBt9xl3CamHjrqJ8Qq0mlWR2gLWVfOrzGC4YOQDz3JeGDdeRzpnKK8C1A0gT6OQq39J&h=AT3sj92Foq4anT_PD-ES-2lYSn6ZqMzYHAVJRjoIsVjeMK9QWb31RhkhYXtiwB_Y_6E0pIrTp9iXQS2aZU1YRTPuKmCgUDqBH8BySjThGUe3Z7pN8JfvpqUx_6J-la89uUl_hRAxWw&\__tn_\_=-UK-y-R&c\[0\]=AT3gjetHCqlPuKiJihB33hkMC8PHJ0Ig9PeQL6fw9EfXjA1CHxuj1RdGZQqpc7j-dv_0nj65UyYCuKU4jzzRsXa1LSgQCTfQ-RmWsWgh-AOPVqS4_QD-rcLbNt3PAwd-\_QXfYwoOXFpwQDSwSryoOD4K10lodVbZsBMdm06nI7pHomFcMQUCfV5xRKYY8hVsR8cylzKVTIBLW6oASMWmKJYaf_KFXd2rO24OEHqpF4CsBu-NEGKI3PxEuwsiTw) <https://devv.ai/>

   - 財務專用Search服務，[reportify.ai](reportify.ai)[:](https://l.facebook.com/l.php?u=http%3A%2F%2Freportify.ai%2F%3Ffbclid%3DIwZXh0bgNhZW0CMTAAAR2PP-DJrWkY0j6V4nRwoFxKu8i8KwETjOCvzpS5X71F9yu2Rp75aHKxsVA_aem_AeMNsXFvmCaVYUrCVRws9nXPzlGwmY0P5ElE21XzZn8Us_mQuBRsySXWIjDX1bxs78TKsnSC-rUruDOV95csrqoF&h=AT3KJ06AHfzhmrYMyQAfz6pOHt5_N7Ysx_85OSjUjdWNAJxBdQitduOVPKJRxcWNzanfiqC7I9LPvMTneLSTvxzxiGz-5VM9EBrZZT-uoDZipgVG3VrWzfh5Eb9R9cnQdvgmjOEaug&\__tn_\_=-UK-y-R&c\[0\]=AT3gjetHCqlPuKiJihB33hkMC8PHJ0Ig9PeQL6fw9EfXjA1CHxuj1RdGZQqpc7j-dv_0nj65UyYCuKU4jzzRsXa1LSgQCTfQ-RmWsWgh-AOPVqS4_QD-rcLbNt3PAwd-\_QXfYwoOXFpwQDSwSryoOD4K10lodVbZsBMdm06nI7pHomFcMQUCfV5xRKYY8hVsR8cylzKVTIBLW6oASMWmKJYaf_KFXd2rO24OEHqpF4CsBu-NEGKI3PxEuwsiTw) <https://reportify.cc/>



- Open source project:

   - <https://github.com/ItzCrazyKns/Perplexica>

   - <https://github.com/nashsu/FreeAskInternet>

   - <https://github.com/fatwang2/search4all>

   - <https://github.com/miurla/morphic>

   

- 參考資料:

   - How does AI chat change search behaviors?: <https://arxiv.org/abs/2307.03826>，研究者分析傳統search跟search+LLM對user behavior的影響，可以藉此來更理解我們設計相關產品需要解決的問題及建立對用戶基礎的認識。

   - The Many Ways that Digital Minds Can Know: <https://moultano.wordpress.com/.../the-many-ways-that.../>，可以看到網路內容的coverage的大小，帶來顯著的優勢，能夠cover住大部分人大多數時候的需求。

   - Perplexity founder 採訪: <https://www.youtube.com/watch?v=e5utruJd6Gk>

   - Comparison: <https://blog.glarity.app/.../ai-search-engine>[...](https://blog.glarity.app/blog/ai-search-engine-multilingual-evaluation-report-v1.0?fbclid=IwZXh0bgNhZW0CMTAAAR2vdimL5-qa4PQiqpXopvLop3OtzAQdl8KrVKWOtRwzbiopL80v0KivCfU_aem_AeM_yPIYvdE3f3eCSfuSikc_ha7V3Prohn1gJcJLb1bcxrRPXFMAJ-ddQq3E1AF2HUyVsKkE4yvCu_1lh9wjxfN6)，雖然結論跟小編使用經驗有點不一樣，但是還是很值得參考的分析報告。

- 
