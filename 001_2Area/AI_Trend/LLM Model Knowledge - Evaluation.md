---
tags:
  - llm-application
---
# **LLM Model Knowledge - Evaluation**

- Purpose:

   - In the business domain, it's important to understand the capabilities of LLMs to determine how we can effectively integrate them into product design.



## GAIA, which stands for "General AI Assistant,

- What:

   - GAIA: General AI Assistant, designed to evaluate the capabilities of AI systems in performing tasks that are straightforward for humans but challenging for machines

   - primary objective: **evaluate everyday human challenges**

   - **Not** for specialized or expert-level problems

   - Introduced by researchers from institutions like Meta AI and Hugging Face

- How:

   - a public leaderboard is available on Hugging Face's platform

   - Comprises 466 real-world questions requiring abilities such as reasoning, multimodal understanding, web browsing, and tool use. ​

   - Be structured into 3 levels of difficulty, reflecting the complexity and number of steps needed to arrive at a solution.

   - human success rate:  92% 

   - advanced AI systems like GPT-4: 15%



## Other Benchmark

- **OpenCompass LLM Leaderboard:** 

   - Focuses on open-source Chinese LLMs

   - Evaluates them on various tasks like text classification, question answering, and text generation

   - provides detailed comparisons of model performance across different tasks and datasets. 

   - <https://opencompass.org.cn/leaderboard-llm>

- **C-Eval Benchmark:** This benchmark is a comprehensive evaluation suite for Chinese LLMs, covering a wide range of tasks including natural language understanding, reasoning, and knowledge. It provides a standardized way to compare different models and track progress in Chinese language AI. You can find the leaderboard here: <https://cevalbenchmark.com/static/leaderboard.html>

- **ModelScope:** This is a Chinese platform for sharing and discovering AI models. It hosts various LLM leaderboards and evaluations, including some specifically focused on Chinese language understanding. You can explore the different leaderboards and model rankings on their website: <https://modelscope.cn/home>

- You can view the leaderboard for Chinese language understanding benchmarks on the CLUE (Chinese Language Understanding Evaluation) website. The leaderboard includes scores from models like BERT, RoBERTa, and ALBERT on various tasks such as reading comprehension and idiom classification. Each model's score is calculated as an average across multiple datasets. For more detailed information and to view the current standings, you can visit the CLUE GitHub repository [here](https://github.com/CLUEbenchmark/CLUE). <https://github.com/CLUEbenchmark/CLUE>



## How to compared

- Llama3-70B到底是甚麼水平？LMSYS詳細分析chatbot arena告訴你真相

   - <https://lmsys.org/blog/2024-05-08-llama3/>

   - Benchmark evaluation其實現在有各種作弊或是汙染的情形，每一個模型出來的時候都claim說超過GPT4-turbo，但真正使用上幾乎找不到比GPT4-turbo穩定、更好用的

   - 為了避免Benchmark data的汙染以及跟現實情況脫節，LMSYS在一年前就推出了chatbot arena，藉由真是用戶評價、比較模型，來對模型排名，

   - 此chatbot arena的分數一直以來都有幾個不確定的點：

      - 難度不確定：chatbot arena裡面有各種難度的題目，因為大多都是user一時興起想出來的考題，並沒有完整的規劃，有些題目可能測試7b模型很適合，但對於top tierA模型就太簡單了

      - 領域不確定：chatbot arena不像是GSM8k, MMLU這種類型，我們其實不知道chatbot arena中不同模型在每個領域的能力，因此也很難從chatbot arena的score直接回饋到具體使用上要選哪一個模型。

      - Format不確定：chatbot arena不像一般學術dataset，會有較一致的instruction格式，因此也無法深入理解模型到底對於哪些format的instruction是有效的。

​

- LMSYS為了讓大家能夠更好解讀chatbot arena的score，針對Llama3在chatbot arena上的表現進行了大規模的分析，針對Llama3-70B跟其他Top tier model比較（GPT4turbo, gemini1.5pro, claude3），並發現Llama3的幾個特點

   - Llama3-70B的強項在creative writing，弱點在closed end math reasoning問題

   - LMSYS針對chatbot arena的問題領域進行分類，發現Llama3 70B其實在像是Brainstorming, Poetry這種Creative writing的能力上明顯較其他top tier model更好，有60%以上的win rate

   - 但是針對有正確答案的像是math reasoning跟coding，以及reading comprehension、Logic reasoning都顯著較其他top tier model弱，只有40%以下的win rate

   - Llama3-70B在簡單的prompt反應較好，當prompt複雜度變高時表現顯著下降

   - 接著LMSYS針對user input的prompt進行分析，對prompt的難易度從簡單到難標為0\~7分（具體方法可以參考<https://lmsys.org/blog/2024-04-19-arena-hard/），發現Llama3-70B在簡單的prompt反應非常好，超過所有top> tier model，但是在複雜的prompt（4分以上），就會顯著弱於其他top tier model，只有45%以下的win rate。