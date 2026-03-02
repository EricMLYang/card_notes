---
tags:
  - llm-application
---
# LLM Framework -  LangChain

### LLM Model Problem: 

- **stochastic parrots**: the deficiencies in models that produce fluent but meaningless language

- **Outdated knowledge**: LLMs rely solely on their training data. Without external integration, they cannot provide recent real-world information.

- **Inability to take action**: LLMs cannot perform interactive actions like searches, calculations, or lookups. This severely limits functionality.

- **Hallucination risks**: Insufficient knowledge on certain topics can lead to the generation of incorrect or nonsensical content by LLMs if not properly grounded.

- **Biases and discrimination**: Depending on the data they were trained on, LLMs can exhibit biases that can be religious, ideological, or political in nature.

- **Lack of transparency**: The behavior of large, complex models can be opaque and difficult to interpret, posing challenges to alignment with human values.

- **Lack of context**: LLMs may struggle to understand and incorporate context from previous prompts or conversations. They may not remember previously mentioned details or may fail to provide additional relevant information beyond the given prompt.



### Mitigating these limitations includes techniques like:

- **Retrieval augmentation**: This technique accesses knowledge bases to supplement an LLM’s outdated training data, providing external context and reducing hallucination risk.

- **Chaining**: This technique integrates actions like searches and calculations.

- **Prompt engineering**: This involves the careful crafting of prompts by providing critical context that guides appropriate responses.

- **Monitoring, filtering, and reviews**: This involves ongoing and effective oversight of emerging issues regarding the application’s input and output to detect issues. Both manual reviews and automated filters then correct potential problems with the output. This includes the following:

   1. **Filters**, like block lists, sensitivity classifiers, and banned word filters, can automatically flag issues.

   2. **Constitutional principles** monitor and filter unethical or inappropriate content.

   3. **Human reviews** provide insight into model behavior and output.

- **Memory**: Retains conversation context by persisting conversation data and context across interactions.

- **Fine-tuning**: Training and tuning the LLM on more appropriate data for the application domain and principles. This adapts the model’s behavior for its specific purpose



### LLM API

- **A client layer to collect user input as text queries or decisions.**

- **A prompt engineering layer to construct prompts that guide the LLM.**

- **An LLM backend to analyze prompts and produce relevant text responses.**

- **An output parsing layer to interpret LLM responses for the application interface.**

- **Optional integration with external services via function APIs, knowledge bases, and reasoning algorithms to augment the LLM’s capabilities.**

### LangChain

- Creater: Harrison Chase

#### The key benefits LangChain offers developers are:

- **Modular architecture** for flexible and adaptable LLM integrations.

- **Chaining together** multiple services beyond just LLMs.

- **Goal-driven agent interactions instead of isolated calls.**

- **Memory and persistence** for statefulness across executions.

- **Open-source** **access** and community support.

#### Some Ecosystem tools

- LlamaHub is a library of data loaders, readers, and tools created by the LlamaIndex community. 

- **LangChainHub** is a central repository for sharing artifacts like prompts, chains, and agents used in LangChain

- LangSmith is a platform that complements LangChain by providing robust debugging, testing, and monitoring capabilities for LLM applications.

- LangFlow and Flowise are UIs that allow chaining LangChain components in an executable flowchart by dragging sidebar components onto the canvas and connecting them together to create your pipeline.

#### Key Component:

- Chain: a critical concept in LangChain for composing modular components into reusable pipelines.

   - **Prompt chaining** is a technique that can be used to improve the performance of LangChain applications, which involves chaining together multiple prompts to autocomplete a more complex response.

- Agants: 

   - Agents are a key concept in LangChain for creating systems that interact dynamically with users and environments over time.

   - While chains define reusable logic by sequencing components, agents leverage chains to take goal-driven actions. Agents combine and orchestrate chains.

- Memory:

   - memory refers to the persisting state between executions of a chain or agent

- Tools:

   - Tools provide modular interfaces for agents to integrate external services like databases and APIs.

### A LLM Flow Example:

- These components can be combined into pipelines also called chains that sequence the following actions:

   - Loading documents

   - Embedding for retrieval

   - Querying LLMs

   - Parsing outputs

   - Writing memory

#### Mitigating hallucinations through fact-checking

- Fact-checking involves three main stages:

   1. **Claim detection**: Identify parts needing verification

   2. **Evidence retrieval**: Find sources supporting or refuting the claim

   3. **Verdict prediction**: Assess claim veracity based on evidence

- Chain of Density: incrementally increase the information density of GPT-4 generated summaries while controlling length.

   ```plain
   template = """Article: { text }
   You will generate increasingly concise, entity-dense summaries of the above article.
   Repeat the following 2 steps 5 times.
   Step 1. Identify 1-3 informative entities (";" delimited) from the article which are missing from the previously generated summary.
   Step 2. Write a new, denser summary of identical length which covers every entity and detail from the previous summary plus the missing entities.
   A missing entity is:
   - relevant to the main story,
   - specific yet concise (5 words or fewer),
   - novel (not in the previous summary),
   - faithful (present in the article),
   - anywhere (can be located anywhere in the article).
   Guidelines:
   - The first summary should be long (4-5 sentences, ~80 words) yet highly non-specific, containing little information beyond the entities marked as missing. Use overly verbose language and fillers (e.g., "this article discusses") to reach ~80 words.
   - Make every word count: rewrite the previous summary to improve flow and make space for additional entities.
   - Make space with fusion, compression, and removal of uninformative phrases like "the article discusses".
   - The summaries should become highly dense and concise yet self-contained, i.e., easily understood without the article.
   - Missing entities can appear anywhere in the new summary.
   - Never drop entities from the previous summary. If space cannot be made, add fewer new entities.
   Remember, use the exact same number of words for each summary.
   Answer in JSON. The JSON should be a list (length 5) of dictionaries whose keys are "Missing_Entities" and "Denser_Summary".
   """
   ```

### others

- tackles turning LLMs into reliable assistants by weaving in fact-checking to reduce misinformation, employing sophisticated prompting strategies for summarization, and integrating external tools for enhanced knowledge.

- map-reduce in LangChain for handling long documents

- Two distinct agent paradigms, plan-and-solve and zero-shot, are implemented to demonstrate decision-making strategies.

- Retrieval-Augmented generation: a method that provides LLMs with access to external knowledge, improving their accuracy and domain-specific proficiency.

- document vectorization, efficient indexing, and the use of vector databases like Milvus and Pinecone for semantic search

- *Chapter 6*, *Developing Software with Generative AI*,

- *Chapter 7*, *LLMs for Data Science*

- *Chapter 9*, *Generative AI in Production*

- **Retrieval-augmented generation** (**RAG**) is a technique that enhances text generation by retrieving and incorporating external knowledge.


