# KaggleX Fellowship Program Cohort 4 Project

## Mathlearn Chatbot Pipeline
Finetuned Gemma model with a custom chain of thought data to solve mathematics problems in step by step approach.

![Mathlearn Project drawio](https://github.com/user-attachments/assets/745926e0-56c5-4403-a0d0-8d8cc37cd088)

This project details how I finetuned a quantized gemma2-9b-instruct model to a finetuned custom mathlearn model for solving mathematical problems in more structured step by step procedure. I first came up with a visual of the model pipeline to get a clear view of what to expect and to plan on methods of execution. I fine tuned the quantized model using QLoRa approach which cost and time effective. This finetuning technique freezes most of the layers in the model making only a small section of the selcted weights are updates during finetuning. Numina provided me with finetuning data where I leveraged their [NuminaMath- CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) data which is a custom data used in previous AIMO competiton where each sample is formated in chain of thought manner. Using a subset of 100k sample from the CoT data, I was able to reach a loss of 0.96 which clearly indicated that the model was learning from the data.


