---
tags:
  - llm-application
---
# **LLM Model Knowledge - [Introducing Apple’s On-Device and Server Foundation Models](https://machinelearning.apple.com/research/introducing-apple-foundation-models)**

- Apple Intelligence is comprised of multiple highly-capable generative models that are specialized for our users’ everyday tasks, and can adapt on the fly for their current activity

- a \~3 billion parameter on-device language model, and a larger server-based language model available with [Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/) and running on Apple silicon servers — have been built and adapted to perform specialized tasks efficiently, accurately, and responsibly.

- .These two foundation models are part of a larger family of generative models created by Apple to support users and developers; this includes a coding model to build intelligence into Xcode, as well as a diffusion model to help users express themselves visually, for example, in the Messages app.

![image 47.png](./LLM%20Model%20Knowledge%20-%20Introducing%20Apple’s%20On-Device%20and%20Server%20Foundation%20Models-assets/image%2047.png)



## Tool

- Our foundation models are trained on [Apple's AXLearn framework](https://github.com/apple/axlearn), an open-source project we released in 2023. It builds on top of JAX and XLA, and allows us to train the models with high efficiency and scalability on various training hardware and cloud platforms, including TPUs and both cloud and on-premise GPUs.

   - **JAX: High-Performance Array Computing:** JAX is a Python library for accelerator-oriented array computation and program transformation, designed for high-performance numerical computing and large-scale machine learning.

   - XLA (Accelerated Linear Algebra) is an open-source compiler for machine learning. The XLA compiler takes models from popular frameworks such as PyTorch, TensorFlow, and JAX, and optimizes the models for high-performance execution across different hardware platforms including GPUs, CPUs, and ML accelerators.

- We used a combination of data parallelism, tensor parallelism, sequence parallelism, and Fully Sharded Data Parallel (FSDP) to scale training along multiple dimensions such as data, model, and sequence length.

## Post-Training

- data quality is essential to model success

- hybrid data strategy in our training pipeline, incorporating both human-annotated and synthetic data

- conduct thorough data curation and filtering procedures

- two novel algorithms in post-training:

   - (1) a rejection sampling fine-tuning algorithm with teacher committee

   - (2) a reinforcement learning from human feedback (RLHF) algorithm with mirror descent policy optimization and a leave-one-out advantage estimator.

## Model Adaptation

- small neural network modules that can be plugged into various layers of the pre-trained model, to fine-tune our models for specific tasks.

- we developed a new framework using LoRA adapters that incorporates a mixed 2-bit and 4-bit configuration strategy — averaging 3.5 bits-per-weight — to achieve the same accuracy as the uncompressed models.

- For our models we adapt the attention matrices, the attention projection matrix, and the fully connected layers in the point-wise feedforward networks for a suitable set of the decoding layers of the transformer architecture.

![image 48.png](./LLM%20Model%20Knowledge%20-%20Introducing%20Apple’s%20On-Device%20and%20Server%20Foundation%20Models-assets/image%2048.png)

- the values of the adapter parameters using 16 bits, and for the \~3 billion parameter on-device model, the parameters for a rank 16 adapter typically require 10s of megabytes. The adapter models can be dynamically loaded, temporarily cached in memory, and swapped — giving our foundation model the ability to specialize itself on the fly for the task at hand while efficiently managing memory and guaranteeing the operating system's responsiveness.



## LoRA Adapter

- LoRA Adapters are, to me, one of the smartest strategies used in Machine Learning in recent years! It is one of those things where I think, "Wait! How didn't we think about that before?"

- The idea is to realize that 

   - any matrix of model parameters in a neural network of a trained model 

      - is just a sum of the initial values and

      - the following gradient descent updates learned on the training data mini-batches:

   - 𝜃(trained model) = 𝜃(initial value) + gradient descent updates

   - 𝜃(fine-tuned) = 𝜃(trained model) + ΔW

- we understand that we don't need that decomposition to happen into the same matrix; we could sum the output of 2 different matrices instead. That is the idea behind LoRA: we allocate new weight parameters that will specialize in learning the fine-tuning data, and we freeze the original weights.

- As such, it is not very interesting because new matrices of model parameters would just double the required memory allocated to the model. So, the trick is to use a low-rank matrix approximation to reduce the number of operations and required memory. We introduce 2 new matrices A and B to approximate ΔW:

   ΔW \~ BA

- It is important to realize that, typically, the amount of training data used for fine-tuning is much smaller than the data used for pretraining.



![image 49.png](./LLM%20Model%20Knowledge%20-%20Introducing%20Apple’s%20On-Device%20and%20Server%20Foundation%20Models-assets/image%2049.png)


