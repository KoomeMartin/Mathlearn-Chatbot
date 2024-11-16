from transformers import AutoModelForCausalLM , BitsAndBytesConfig , AutoTokenizer
from peft import PeftModel, PeftConfig

from time import time
from IPython.display import Markdown, display

import streamlit as st

class ModelInterface():

  def __init__(self):
      self.path_to_model = "unsloth/gemma-2-9b-bnb-4bit"
      self.max_new_tokens = 1024
      self.initialize_model()

  def initialize_model(self):
      start_time = time()
      self.tokenizer = AutoTokenizer.from_pretrained(self.path_to_model)
      tok_time = time()
      print(f"Load tokenizer: {round(tok_time-start_time, 1)} sec.")
      self.config = PeftConfig.from_pretrained("Koomemartin/unsloth-gemma2-9b-version3-100k")
      self.base_model = AutoModelForCausalLM.from_pretrained(
          self.path_to_model,
          
          low_cpu_mem_usage=True,
          device_map="cuda",
      )
      self.model = PeftModel.from_pretrained(self.base_model, "Koomemartin/unsloth-gemma2-9b-version3-100k",)
      mod_time = time()
      print(f"Load model: {round(mod_time-tok_time, 1)} sec.")


  def get_message_response(self, input_text):
      start_time = time()
      
      prompt_template='''
        <start_of_turn> user \n 
        You are a math assistant. Answer the following math problem with a detailed, step-by-step solution. Be clear and concise in each step. If there are multiple approaches, select the most efficient method. Include any formulas or key concepts used, and provide the final answer at the end.

        Instruction: {problem} \n  <end_of_turn>  \n
        <start_of_turn> model \n
        Response:
           '''

      inputs=self.tokenizer(
        [
          prompt_template.format(problem=input_text)
        ] ,return_tensors='pt'
      ).to('cuda')


      outputs = self.model.generate(
              **inputs,
              max_new_tokens=self.max_new_tokens,
              eos_token_id=self.tokenizer.eos_token_id,
              )
      end_time = time()

      answer=self.tokenizer.decode(outputs[0])

      cleaned_response = answer.split("Response:")[1].strip() 

      return cleaned_response
              



@st.cache_resource # if the model is loaded the cached version is used to avoid memory wastage
def load_model_interface():
    return ModelInterface()


model_interface = load_model_interface()

st.title('🦜🔗 Welcome to  MathLearn ') 

# Streamlit session state to manage chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
      st.markdown(message["content"])

# Accept user input and process response
if user_input := st.chat_input():
  st.session_state.messages.append({"role": "user", "content": user_input})
  with st.chat_message("user"):
      st.markdown(user_input)

  with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
          response_text = model_interface.get_message_response(user_input)
          st.write(response_text)

  # Save assistant's response to chat history
  st.session_state.messages.append({"role": "assistant", "content": response_text})

