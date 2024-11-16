# KaggleX Fellowship Program Cohort 4 Project

## Mathlearn Chatbot Pipeline
Finetuned Gemma model with a custom chain of thought data to solve mathematics problems in step by step approach.

![Mathlearn Project drawio](https://github.com/user-attachments/assets/745926e0-56c5-4403-a0d0-8d8cc37cd088)

### Project Outline
This project details how I finetuned a `quantized gemma2-9b-instruct model` to a finetuned custom mathlearn model for solving mathematical problems in more structured step by step procedure. I first came up with a visual of the model pipeline to get a clear view of what to expect and to plan on methods of execution. I fine tuned the quantized model using `QLoRa `approach which cost and time effective. This finetuning technique freezes most of the layers in the model making only a small section of the selcted weights are updates during finetuning. Numina provided me with finetuning data where I leveraged their <a href='https://huggingface.co/datasets/AI-MO/NuminaMath-CoT'>`NuminaMath- CoT`<a/> data which is a custom data used in previous `AIMO` competiton where each sample is formated in chain of thought manner. Using a subset of 100k sample from the CoT data, I was able to reach a loss of 0.96 which clearly indicated that the model was learning from the data.

<b> RAG System </b>

I also added contextual data in a retrieval system to provide more context to the model when prompted with a problem. The most challenging part of implementing the RAG was getting the retiever to extract relevant data related to the query especially in math domain where main concepts interrelated. 
I used Microsofts's <a href='https://huggingface.co/datasets/microsoft/orca-math-word-problems-200k'>`Orca-math-word-problems`<a/> to provide contexr to the user prompts where I used a `recursive text character splitter` to split the data into smaller chunks then passed the chunked data in an index for semantic retrieval. This is among the existing research am working on to find better ways to improve retrieval system in mathematics domain.

<b> Streamlit App</b>

I was able to create a user interface to interat with the model using streamlit which `abstracts` the inner components of the model and allows users to easy use the model. Though not efficient interms of the time it takes to respond to user queries, It clearly provide key steps it uses to a reach at the final solution and the formulas used. 



https://github.com/user-attachments/assets/dd8ffc19-1237-4b94-9548-51abbef38e27



### Usage
To use the chatbot, fork this repoistory and run the app.py script using the following code

First create a secure tunnel to run the streamlit app

```bash
wget -q -O - ipv4.icanhazip.com
```
This provides an IP address that autheticates you to access the app in your browser

```bash
streamlit run app.y & npx localtunnel --port 8501
```
This code runs the app.y in the secure tunnel and provides the link to acess it in your browser

```plaintext
Mathlearn model only runs on CUDA devices
```

## Acknowledgements

I would like to thank my mentor Engineer Uzordinma Nwokeaka for the continous guidance throughout this project and the KaggleX community for an opportunity of self and career development. Special thanks to the organizers of the fellowship program for such an exposure in generative AI and providing computing resources to that made this project a reality.

