---
tags:
  - llm-application
---
# LLM Model Knowledge - Online / offline RLHF

## 05/13\~05/19 一週LLM論文整理

​#AI #LLM #學習資源 #語言模型 #deeplearning #machinelearning 

Crazy week，原本從OpenAI發布會、GoogleIO後一天，還想說這週論文有點少，好像可以好好思考一些問題，粉專的更新頻率也跟著下降，結果週四、五大量有趣的新論文出現，小編週末苦讀還是有點讀不完，挑選一些值得深入的論文之後幾天會用【論文速讀】介紹，weekly還是一樣先列出大量值得參考的論文，以及挑幾篇可以快速理解的讓各位朋友可以先讀。

​

RLHF Workflow: From Reward Modeling to Online RLHF

<https://arxiv.org/abs/2405.07863>

這週其實最讓我感興趣且食用性較高的就是這篇與下一篇討論online & offline RLHF的差異的，這篇Salesforce更注重在整個pipeline的介紹，因為是technical report，所以裡面有很多操作性的技巧與分析，具體在教會每個人，怎麼使用online RLHF。

​

Understanding the performance gap between online and offline alignment algorithms

<https://arxiv.org/abs/2405.08448>

DeepMind這篇則注重在分析，online & offline RLHF具體差別在哪裡，同時分析了performance跟reward model的behavior，其中我比較感興趣的就是論文中發現online跟offline RLHF的reward model behavior很不一樣，offline RLHF的reward model有更好的pairwise comparison能力，但是online RLHF的reward model較差，但同時online RLHF的reward model卻能維持一定的generation能力，顯示出一個好的reward model跟一個好的RLHF結果有複雜的聯繫，我們原本的直覺（reward model就要把comparison做好）可能不可靠。

BEHAVIOR Vision Suite: Customizable Dataset Generation via Simulation

<https://arxiv.org/abs/2405.09546>

Li Fei-Fei團隊的大作，提供給每個CV project一個大規模進行data synthesize的Toolkit。

​

MambaOut: Do We Really Need Mamba for Vision?

<https://arxiv.org/abs/2405.07992>

這篇有趣的點就在現在這個時間點，因為今年各種CV的會議包含接下來要開的CVPR，其實都有很多Vision Mamba相關的work，這篇論文大膽挑戰Vision Mamba的核心假設，並發現Mamba其實對於Vision task不見得是必要的module。

​

Chameleon: Mixed-Modal Early-Fusion Foundation Models

<https://arxiv.org/abs/2405.09818>

Meta提出的新的MLLM架構，並提出在output端也要具備interleaving output image & text的能力，提出新的可能性，原有Llava相關架構都是藉由一些tool才能做到output image，像是retrieval或是DallE，而Chameleon主打讓MLLM自行生成，並得到跟傳統VLM一樣甚至更好的performance。

​

\-——————————-

​

Many-Shot In-Context Learning in Multimodal Foundation Models

<https://arxiv.org/abs/2405.09798>

​

MS MARCO Web Search: a Large-scale Information-rich Web Dataset with Millions of Real Click Labels

<https://arxiv.org/abs/2405.07526>

​

SynthesizRR: Generating Diverse Datasets with Retrieval Augmentation

<https://arxiv.org/abs/2405.10040>

​

Beyond Scaling Laws: Understanding Transformer Performance with Associative Memory

<https://arxiv.org/abs/2405.08707>

​

ALPINE: Unveiling the Planning Capability of Autoregressive Learning in Language Models

<https://arxiv.org/abs/2405.09220>

​

SambaNova SN40L: Scaling the AI Memory Wall with Dataflow and Composition of Experts

<https://arxiv.org/abs/2405.07518>

​

Linearizing Large Language Models

<https://arxiv.org/abs/2405.06147>

​

What Can Natural Language Processing Do for Peer Review?

<https://arxiv.org/abs/2405.06563>

​

UniRAG: Universal Retrieval Augmentation for Multi-Modal Large Language Models

<https://arxiv.org/abs/2405.10311>

​

Xmodel-VLM: A Simple Baseline for Multimodal Vision Language Model

<https://arxiv.org/abs/2405.09215>

​

Benchmarking Retrieval-Augmented Large Language Models in Biomedical NLP: Application, Robustness, and Self-Awareness 

<https://arxiv.org/abs/2405.08151>

​

State-Free Inference of State-Space Models: The Transfer Function Approach

<https://arxiv.org/abs/2405.06147>

​

Kolmogorov-Arnold Networks (KANs) for Time Series Analysis

<https://arxiv.org/abs/2405.06147>

​

——————-

​

Survey & reviews:

​

Risks and Opportunities of Open-Source Generative AI

<https://arxiv.org/abs/2405.08597>

​

How Far Are We From AGI

<https://arxiv.org/abs/2405.10313>

​

A Survey on RAG Meets LLMs: Towards Retrieval-Augmented Large Language Models

<https://arxiv.org/abs/2405.06211>

​

Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems

<https://arxiv.org/abs/2405.06211>