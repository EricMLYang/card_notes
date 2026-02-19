---
tags:
  - vibe-code
---
# AI Coding Article Note

## 程式設計本質與 AI 取代論

- 學程式設計是理解計算思維的方法之一，好比做物理和化學實驗來體會和驗證物理學，從基本的四則計算和幾何邏輯開始堆疊數學素養。

- 但如果把程式設計當成是計算機科學或資訊工程的全部，那就實在是太無知了。就像學了E=MC^2，就以為可以去設計製造原子彈，那我也無言了。

- 我一直對於資訊界過度重視程式設計的這件事感到遺憾。把程式競賽得獎者當成神，或者程式題來篩選應徵者，甚至以軟體專案個數、程式行數當成KPI，在某種程度上扭曲的資訊工程專業的樣貌。之所以如此，只能說是便宜行事。

- 記得我小時候還學過珠算，那個時候到親戚家開的會計事務所，看到每張辦公桌上都有算盤，而不懂事的我以為算盤打得快的就是厲害的會計師，殊不知會計師要懂很多東西。幾年之後，桌上都換成計算器了，珠算的技能沒用了，厲害的會計師工作還在，而且效率變高了。到了電腦時代，更是如此，需要的對會計的了解，而不是按計算機的速度。

- 幾年前有人跟我說，資工系的程式設計課應該教Python，不要再教C那種低層次的語言。我說，用C語言的目的是要讓資工系學生有紮實的基礎，要知道作業系統的核心大都是用C寫出來的，能做一些其他語言做不到的操作，效率又高。況且資工系還有演算法、資料結構、機器學習、編譯器等課程，老師可能選用不同的高階語言，學過C語言的學生再學其他語言並不難，反過來就難說了。

- 也有人說，現在一堆Low Code/No Code的東西，輕鬆方便就可以做出想要的東西，何必再學coding？除了重複解說學coding的重點是學習計算思維之外，我得這麼說：No Code很適合那種只想快速獲得解方、沒時間或沒興趣深入計算思維的人，但這種可以很簡單自學起來的東西應該不需要在資工系裡教。

- 社會需要各種人才，打造AI系統需要多方面的人才，我不想評論每類人才的價值，講了傷感情，讀者可以自己去網上查資訊人才的薪情。實際上資訊人才的行情差很大，為什麼一堆公司開出年薪200萬的價碼搶資工系即期畢業生，但某些統計資料顯示資訊從業人員的月薪3-9萬元？要注意那個9萬元是P75，換句話說25%的月薪超過9萬元，因此如果到頂尖公司去的話，月薪90萬都有可能。想拿頂薪的話，不要看這種統計，去看看頂尖公司搶什麼人。

- 然而某些技能，就像珠算和程式設計，會被更好的工具取代，而有些內功心法則可以長長久久。

- 所以與其花大把時間去練外功，學了一堆招式、速度很快，到頭來派不上用場就浪費了。通常大眾化淺碟式的學習成果，比較可能被AI學會，所以我會建議有才能的學生，多涉足一些領域，學到領域的精髓，設法跨領域編織出屬於自己的專業能力，站在AI巨人的肩膀上創新。





## ChatGPT 4o 評論

OpenAI 最新的GPT-4o可說是在多模態語言模型與手機的深度整合上，可以說是到了一個全新領域。

GPT-4o 裡面的 "o" 指的是「omnimodel 」，指的就是可以在同時處理 Text, Vision, Audio 的「全能模型」

跟去年預測的，LLM (Large Language Model )大型語言模型 與 LMM (Large Multimodal Model 大型多模態模型，其實最大的衝擊和應用，在於「人機介面」。而智慧型手機，有著豐富的影音介面，且能隨身攜帶，AI Smartphone會是 LLM/LMM 全面普及應用，初期最重要的戰場。

大家可以注意看，在 OpenAI 這些酷炫且自然的互動中，用的都是智慧型手機! 而不是窩在電腦螢幕前面，狂敲鍵盤看螢幕!

自然的語言和視覺互動才是重點，這會變成新的「人工智慧入口」(AI Portal)，才能繼續導引到未來更多的AI應用。

而更重要的是，只靠手機運算能力不足，一定要智慧型手機與雲端協作，才能創造完美的人機互動效果。而其中, 5G以及未來的 6G、無線網路 WiFi 在裡面的角色也極為重大。這也是智慧型手機會成為 AI Portal 的重要原因。

這也今年初，到 IEEE  ISSCC 的 Forum 演講的主軸，也是三月在 ACM ISPD擔任 Keynote 所講的重點。

很訝異的是，沒想到不到半年，GPT-4o已經展示出年初預言的科技進展!

這個領域真的進步的很快!!

我們也要加緊腳步!

後面回應會放上 OpenAI GPT-4o 的 8個重要示範，可以深入瞭解能力。

也會放上我 ACM ISPD演講投影片的連結，供對技術有興趣的人參考。

.....

最後講一句，目前網路上有些說法，覺得以後寫程式，有 AI代勞即可，Computer Science 不重要了，不要鼓勵學生學 CS。這種說法很有問題。

能開發出 GPT-4o ， 並能利用大量算力來訓練出這麼強的 AI, 靠的就是很強的 CS團隊與功力。

有 AI協助，只是寫程式下命令的方式改變而已，但整體應用架構，處理資訊的方式，還是要學習並研究。就像是早年用機械語言、組合語言寫程式，現在改用 高階語言寫程式，未來有 AI輔助，可能改用自然語言寫程式。但重點不僅在用哪種方式寫程式，而在整體的架構，該如何描述要處理的資訊與架構，並善用已有的資訊工具，包含AI，來完成工作，仍有很多東西需要研究。

CS使用的工具、教學研究方法可以改。但若不去學 CS, 不去研究 CS, 只等著用別人開發好的AI，而那永遠就只能變成最末稍的使用者。只能夠在別人設計好的框架下發揮。但對於 AI 底層更根本、更有價值的部分，卻無能為力。

而台灣其實就靠根本的科技能力，才在前一波的半導體和PC技術進展中，建立其今天的科技地位。但這主要是半導體和資訊硬體的能力。軟體能力仍有很大進步空間。

而現在在更新更大的 AI潮流中，卻說要學生自廢武功不要學CS。等於是AI浪潮還沒開始，就要台灣棄械投降了般。這種論調, 會弱化整個科技的根本，很令人憂心!





## o1-mini 寫程式的心得，結論就是真的超強。

- 寫 code 的話更推薦用 o1-mini

   - Open AI 官方文件有說 o1-mini 比 o1-preview 更適合來寫 code，甚至 o1-mini 在數學和寫 code 這方面，表現幾乎與完全體的 o1 接近

   -  o1-mini 在其他領域的表現就輸了，連 o1-preview 也輸, 所以很顯然地，以後 AI 模型會往專門特化的方向來走，CP 值會比較高

- 主流的框架還是可以回答得比較好

   - 用 Golang 的 beego 框架來寫，可以寫出我要的內容，但是依然有不少 bug，但其實可以看出 o1-mini 真的有理解 beego 了

   - 接著我改用 Golang 的主流 web 框架、Gin 來寫，一次就產出可以動的答案了。

   - 程式語言與其框架馬太效應會更加明顯，因為用主流的程式語言和框架來搭配 AI 輔助開發，可以有更好的表現

- 開局的目標設定就用 o1-mini、或是比較複雜的大問題再用 o1-mini 就好了。

   - 設定開發程式目標時就 o1-mini, 然後改用 4o, 等複雜問題再切換成 o1-mini

- 複雜的商業邏輯可以一次到位。

   - 我試了之前實務上所碰到的商業邏輯，將其描述清楚，出來的程式碼可以一次到

   - 同樣的商業邏輯，我之前使用 gpt-4o 時，必須要拆好幾次、多段來回，才能得到我要的程式碼。

- 用中文和英文來回答，都能得到我要的結果, 但直覺上英文的表現比較好，這尚待驗證



![Pasted 2024-09-21-22-39-00.jpeg](./AI%20Coding%20Article%20Note-assets/Pasted%202024-09-21-22-39-00.jpeg)

# Read: [How I Use "AI"](https://nicholas.carlini.com/writing/2024/how-i-use-ai.html?fbclid=IwY2xjawEu7u1leHRuA2FlbQIxMAABHRXcO20Axp99YvSKFG1yNaYR14uT3x5f2CIQvXHV6AaV01IaJ0OBqxZgcQ_aem_MW4NZWsiw8VzsSFOk2T7qw)

- Main Task:

   - Building entire webapps with technology I've never used before.

   - Teaching me how to use various frameworks having never previously used them.

   - Converting dozens of programs to C or Rust to improve performance 10-100x.

   - Trimming down large codebases to significantly simplify the project.

   - Writing the initial experiment code for nearly every research paper I've written in the last year.

   - Automating nearly every monotonous task or one-off script.

   - Almost entirely replaced web searches for helping me set up and configure new packages or projects.

   - About 50% replaced web searches for helping me debug error messages

- If I were to categorize these examples into two broad categories, they would be “helping me learn” and “automating boring tasks”. Helping me learn is obviously important because it means that I can now do things I previously would have found challenging; but automating boring tasks is (to me) actually equally important because it lets me focus on what I do best, and solve the hard problems.

# AI With Software Engineering

- Github CEO Thomas Dohmke 有場 TED 科普演講: : 透過 AI 任何人都可以成為 Coder (15分鐘、有簡中字幕) 值得一看 ([連結](https://www.ted.com/talks/thomas_dohmke_with_ai_anyone_can_be_a_coder_now?language=en&delay=1m&subtitle=en))

   - 目前可用 Github Copilot 工具協助你完成程式碼，將造福更多人可以輕鬆開始寫程式

   - 透過自然語言與程式碼互動，未來將有更多人可以是 Coder

   - 目前 Github 上有 100M 開發者，預計到 2030 年成長十倍，也就是 1B 的開發者。全球人口 10% 不只會用電腦，還會寫程式!

   - 最後還 demo 了最新預覽版功能 Github Workspace: 只要開票，Github 就可以幫你拆解成文字規格，經過你確認修改後，再幫你寫 code 產生 pull request，最後你再檢查程式碼合併進主程式

   - 最後主持人提問一個關鍵問題:   預測未來是否還需要人類參與? 回答是: 專業軟體設計師不會消失，仍需要人類去理解要打造什麼東西，仍需要人類專業去維護較大的複雜軟體系統。

## Cursor : Lex Fridman Podcast

- <https://www.youtube.com/watch?v=oFfVt3S51T4>

**Section 1: Introduction and the Purpose of Code Editors**

- Introductions of the Cursor team members (Michael, Aman, Suale, Arvid).

- Discussion on the fundamental role of a code editor in software development.

- Emphasis on the importance of user experience and "fun" in code editor design.

**Section 2: The Evolution of Code Editors and the Rise of AI**

- The team's personal journey with code editors, starting with Vim and transitioning to VS Code due to the emergence of GitHub Copilot.

- Acknowledging Copilot as a pioneering AI product in software development.

- The impact of "scaling laws" papers on their perception of AI's potential in coding.

**Section 3: The Genesis of Cursor and its Vision**

- The team's motivation behind creating Cursor, driven by advancements in AI, particularly GPT-4.

- Discussion on the future of code review and the potential for AI-assisted code generation.

- Exploring the role of natural language and other modalities in future programming paradigms.

**Section 4: The Future of AI in Programming**

- Speculation on the future of AI in solving complex problems, including the possibility of AI achieving a Fields Medal.

- Discussion on scaling laws and their implications for AI model development.

- The potential impact of AI on programming practices and the role of human-AI collaboration.

**Section 5: Advice for Aspiring Programmers and Closing Remarks**

- The importance of continuous learning and adaptation in the evolving landscape of programming.

- Discussion on the qualities of successful programmers and the role of passion and curiosity.

- Final thoughts on the future of programming and the potential for AI to enhance human capabilities.

**Additional Sections (potentially):**

- Deep Dive into Specific Cursor Features: The transcript hints at discussions about features like "super tab" which could be a separate section.

- The Role of Reward Models in AI Training: The conversation touches upon reward models, which could be explored in more detail.



### Cursor’s Main Feature

**Overall, Cursor focuses on building an AI-first code editor that understands the context of the code, allows for more natural interaction, and significantly boosts developer productivity.** They achieve this through a combination of AI code generation, codebase understanding, and a strong emphasis on user experience.

**1\. AI-Assisted Code Generation:**

- **"Super Tab" Feature:** This seems to be their flagship feature, allowing users to generate code by pressing tab, with the AI understanding the context and intent. It's described as a more interactive and iterative process than traditional code generation.

- **Focus on Intent Communication:** They aim to move beyond simple code completion to a system where users can communicate their intent at a higher level, and the AI translates that into code.

**2\. Codebase Understanding and Navigation:**

- **Code Indexing:** Cursor indexes the entire codebase, allowing for semantic search and understanding. This enables features like quickly finding where specific functionality is implemented, even with a fuzzy recollection.

**3\. Focus on Developer Experience:**

- **Speed and Efficiency:** They emphasize the importance of speed and responsiveness in the editor, contributing to a "fun" and productive experience.

- **Integration with AI Models:** Cursor is designed to seamlessly integrate with the latest AI models, allowing them to quickly adapt to new advancements in AI code generation.

**Technical Aspects:**

- **Fork of VS Code:** Cursor is built upon VS Code, leveraging its existing foundation while adding their own AI-powered features.

- **Vector Databases and Embeddings:** They utilize vector databases and code embeddings to enable semantic search and code understanding.

- **Emphasis on Scaling:** They discuss the challenges of scaling their solutions, particularly the code indexing system, to handle large codebases and teams efficiently.

- **No Code Storage:** They highlight that they don't store any user code on their servers, only the vector embeddings, addressing privacy concerns.



### **The importance of user experience**

The Cursor team repeatedly emphasizes the importance of user experience and "fun" in their design philosophy. They believe that a code editor should be enjoyable to use and contribute to a sense of flow and productivity for the developer. This focus on user experience is evident in their approach to features like the "super tab" and the diff interface, which are designed to be intuitive and efficient.

To differentiate themselves and provide a superior user experience, Cursor focuses on these key areas:

**1\. Deeper Code Understanding:**

- **Beyond Simple Completion:** While Copilot excels at code completion, Cursor aims for a deeper understanding of the codebase and the developer's intent. This allows for more accurate and contextually relevant suggestions, going beyond simple pattern matching.

- **Semantic Search and Navigation:** Cursor's code indexing enables powerful semantic search and navigation features, allowing developers to quickly find and understand relevant code snippets even with vague queries.

**2\. Enhanced Interactivity:**

- **Iterative Refinement:** Cursor's "super tab" feature encourages an iterative workflow where developers can refine the AI-generated code through interaction and feedback, leading to more accurate and personalized results.

- **Natural Language Interface:** They are working towards a more natural language-based interaction with the AI, allowing developers to express their intent in a more intuitive way.

**3\. Focus on Speed and Efficiency:**

- **Optimized Performance:** Cursor emphasizes speed and responsiveness as core aspects of the user experience. They are investing in efficient algorithms and infrastructure to ensure a smooth and lag-free experience, even with large codebases.

- **Streamlined Workflow:** Features like the "super tab" and the diff interface are designed to streamline the development workflow and reduce friction, allowing developers to stay in the flow and focus on their tasks.

**4\. Tailored AI Models:**

- **Custom Training:** In addition to leveraging powerful LLMs, Cursor invests in training their own AI models specifically for code generation and understanding. This allows them to fine-tune the models to better suit the needs of developers and provide more accurate and relevant suggestions.

- **Ensemble Approach:** They combine the strengths of different AI models, including custom-trained models and frontier models, to achieve optimal performance for various tasks.

**5\. Privacy and Security:**

- **No Code Storage:** Cursor emphasizes that they do not store any user code on their servers, addressing privacy concerns that some developers may have with AI-powered tools.

By focusing on these areas, Cursor aims to provide a user experience that is not only powerful and efficient but also intuitive, enjoyable, and tailored to the specific needs of developers. They are pushing the boundaries of AI-assisted coding beyond simple code completion to create a truly collaborative and empowering experience for programmers.



### challenges in scaling its solutions

The interview mentions that Cursor faces challenges in scaling its solutions, particularly the code indexing system, to handle large codebases and teams efficiently. While they don't discuss specific techniques, they highlight the importance of efficient indexing and query processing to ensure fast and responsive performance for developers working on large projects.

Here are some potential techniques they may be using or considering:

**1\. Distributed Indexing:**

- Partitioning the codebase into smaller chunks and indexing them separately can distribute the workload and improve scalability.

- This approach can also enable faster queries, as the search scope is narrowed down based on the specific chunk of code being accessed.

**2\. Incremental Indexing:**

- Instead of re-indexing the entire codebase every time a change is made, they may use incremental indexing techniques to update only the affected parts.

- This can significantly reduce the computational overhead and improve performance for large codebases.

**3\. Efficient Query Processing:**

- Optimizing the algorithms used for searching and retrieving code can make a significant difference in performance, especially for large codebases with millions of lines of code.

- This may involve techniques like using advanced data structures, caching frequently accessed data, and parallelizing queries.

**4\. Cloud-Based Infrastructure:**

- Utilizing cloud-based infrastructure can provide the necessary scalability and resources to handle large codebases and teams.

- This can involve leveraging cloud storage for storing the indexed data and using cloud-based computing resources for processing queries.

**5\. Collaboration with the Community:**

- Engaging with the open-source community can help them leverage existing tools and libraries that have already been optimized for scalability and performance.

- They may also contribute back to the community by sharing their own techniques and learnings.

Overall, the scaling of their code indexing system is a critical challenge for Cursor, and their success in addressing it will be crucial for providing a seamless and efficient experience for developers working on large projects.



### How Cursor Utilizes LLMs

The Cursor team utilizes LLMs (Large Language Models) and AI in several key ways to enhance their code editor and achieve their goal of boosting developer productivity:

**1\. Code Generation:**

- **"Super Tab" Feature:** This is powered by LLMs that understand the context of the code and generate code snippets based on the user's intent. It goes beyond simple autocompletion by allowing for iterative refinement and interaction with the AI.

- **Focus on Intent Communication:** They aim to enable users to express their desired outcome in natural language or through high-level instructions, and the AI translates that into code.

**2\. Codebase Understanding:**

- **Code Indexing:** LLMs are used to analyze and index the entire codebase, creating semantic representations (embeddings) of the code. This allows for features like semantic search, finding relevant code snippets, and understanding the relationships between different parts of the code.

**3\. Code Editing and Manipulation:**

- **"Apply" Model:** This custom-trained model takes a rough sketch of a code change (potentially generated by an LLM) and accurately applies it to the existing code, handling the intricacies of merging and modifying code.

**4\. Ensemble of Models:**

- **Custom Models alongside Frontier Models:** They combine their own custom-trained models with powerful "frontier" LLMs (likely GPT-4 and similar models). This allows them to leverage the strengths of each type of model for different tasks.

**5\. Speculative Edits:**

- **Efficient Code Generation:** They utilize speculative decoding techniques, where the AI generates multiple possible code edits in parallel and then selects the most suitable one. This improves the speed and efficiency of code generation.

**6\. Reward Models:**

- **Training and Fine-tuning:** They mention the use of reward models to train and fine-tune their AI models, ensuring that the generated code aligns with developer preferences and best practices.

**7\. Continuous Learning and Adaptation:**

- **Staying Updated with AI Advancements:** Cursor is designed to integrate with the latest AI models, allowing them to quickly adapt to new advancements in LLM technology and continuously improve their code generation and understanding capabilities.

Overall, Cursor leverages a combination of LLMs, custom AI models, and innovative techniques to create a code editor that understands code, generates code efficiently, and empowers developers to be more productive.



### The Future of Programmer

This video doesn't explicitly suggest that programmers need to fear being replaced by AI tools. Instead, it paints a picture of AI as a powerful partner that can significantly enhance productivity and creativity. However, it does imply that programmers need to adapt and evolve to thrive in this new era of AI-assisted coding.

Here are some key takeaways for programmers:

**Embrace AI tools:**

- **Increased productivity:** AI tools like Cursor can automate tedious tasks, generate code snippets, and help understand complex codebases, allowing developers to focus on higher-level tasks and problem-solving.

- **Enhanced creativity:** By reducing the cognitive load of writing boilerplate code and navigating complex systems, AI can free up mental space for more creative and innovative solutions.

- **Faster iteration:** AI-powered code generation and editing tools can accelerate the development process, enabling faster iteration and experimentation.

**Adapt and evolve:**

- **Focus on intent communication:** As AI tools become better at understanding intent, developers need to learn how to effectively communicate their desired outcomes to the AI.

- **Develop new skills:** While AI can automate certain tasks, it also creates new opportunities for developers to specialize in areas like AI model training, prompt engineering, and human-AI collaboration.

- **Continuous learning:** The rapid advancements in AI require developers to stay updated with the latest tools and techniques to remain competitive.

**Don't fear replacement (yet):**

- **Human-AI collaboration:** The video emphasizes the importance of human oversight and control in the development process. AI is seen as a tool to augment human capabilities, not replace them entirely.

- **Complex problem-solving:** While AI excels at certain tasks, it still struggles with complex problem-solving, critical thinking, and understanding nuanced requirements, which remain core strengths of human developers.

- **The "fun" factor:** The video highlights the importance of passion and enjoyment in programming. AI can enhance the fun aspects of coding by automating tedious tasks and enabling faster iteration.

**In conclusion:** The video suggests that programmers should embrace AI tools as partners to enhance their productivity and creativity. While adaptation and continuous learning are crucial, there's no immediate threat of replacement. Instead, the future of programming lies in human-AI collaboration, where developers leverage AI to solve complex problems and build innovative solutions.



### Extra interesting points

- **The philosophical side of AI and programming:** The conversation touches upon some interesting philosophical questions, such as the nature of intelligence, the role of intuition in programming, and the potential impact of AI on human creativity. For example, they discuss whether AI can truly understand the meaning of code or if it's simply manipulating symbols based on patterns. They also ponder if AI can ever replicate the intuitive leaps and creative insights that human programmers often experience.

- **The future of code review:** The interview briefly touches upon the potential impact of AI on code review. They suggest that AI could automate certain aspects of code review, such as identifying potential bugs and suggesting improvements. This could free up developers to focus on more high-level aspects of code review, such as ensuring code readability and maintainability.

- **The role of natural language in programming:** The Cursor team envisions a future where natural language plays a more significant role in programming. They believe that AI can bridge the gap between human intention and code by allowing developers to express their ideas in natural language and then translating that into code. This could make programming more accessible to a wider audience and enable more efficient communication between developers and machines.

- **The impact of AI on the programming community:** The conversation also touches upon the potential impact of AI on the programming community. They discuss how AI could democratize access to programming by making it easier for people to learn and contribute to software development. They also speculate on how AI could change the dynamics of collaboration and competition within the programming community.

Overall, the video provides a fascinating glimpse into the future of programming and the potential impact of AI on the field. It's a thought-provoking conversation that raises important questions about the nature of intelligence, the role of creativity, and the future of human-computer interaction.


