import google.generativeai as genai
import os
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
genai.configure(api_key="AIzaSyBcBNW3moG8nFwpqCe7IiPAWqzMJx3WNK0")
llm_model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
def string_to_dict(json_string):
        # Convert string to JSON (which is also a dictionary in Python)
        json_dict = json.loads(json_string)
        return json_dict
def transform_string(input_string):
    # Replace spaces with hyphens
    replaced_string = input_string.replace(' ', '-')
    # Convert to lowercase
    lowercased_string = replaced_string.lower()
    return lowercased_string
def find_api(model):
   driver = webdriver.Chrome(options=options)

   # Navigate to the URL
   url = f"https://huggingface.co/{model}?inference_api=true"
   driver.get(url)

   try:
      # Wait for up to 10 seconds for the <pre> tag to appear
      pre_tag = WebDriverWait(driver, 2).until(
         EC.presence_of_element_located((By.TAG_NAME, "pre"))
      )

      # Print the content of the <pre> tag
      prompt = pre_tag.text+"""
           convert  this code for javascript 
           and the bearer key for Authorization is  : Bearer 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
           also use axios using require syntax
           Using this JSON schema:
           code = {"code": str}
         """
      response = llm_model.generate_content(prompt)
      return response.text
      
   except Exception as e:
      print("Element not found or error occurred:", e)
   finally:
      # Clean up and close the browser
      driver.quit()
def give_models(type):
   uri = f"https://huggingface.co/models?pipeline_tag={type}&sort=trending"
   response = requests.get(uri)
   soup = BeautifulSoup(response.text, 'html.parser')
   h4_tags = soup.find_all("h4")
   model_names = [tag.text for tag in h4_tags]
   return model_names
types = """
'Graph Machine Learning',
 'Robotics',
 'Reinforcement Learning',
 'Time Series Forecasting',
 'Tabular Regression',
 'Tabular Classification',
 'Voice Activity Detection',
 'Audio Classification',
 'Audio-to-Audio',
 'Automatic Speech Recognition',
 'Text-to-Audio',
 'Text-to-Speech',
 'Sentence Similarity',
 'Fill-Mask',
 'Text2Text Generation',
 'Text Generation',
 'Feature Extraction',
 'Summarization',
 'Translation',
 'Zero-Shot Classification',
 'Question Answering',
 'Table Question Answering',
 'Token Classification',
 'Text Classification',
 'Image Feature Extraction',
 'Image-to-3D',
 'Text-to-3D',
 'Zero-Shot Object Detection',
 'Mask Generation',
 'Zero-Shot Image Classification',
 'Text-to-Video',
 'Video Classification',
 'Unconditional Image Generation',
 'Image-to-Video',
 'Image-to-Image',
 'Image-to-Text',
 'Text-to-Image',
 'Image Segmentation',
 'Object Detection',
 'Image Classification',
 'Depth Estimation',
 'Document Question Answering',
 'Visual Question Answering',
 'Image-Text-to-Text'
 """
def query_api(query) : 
   schema = """
   model = { "model" : str }
   """
   prompt = f"""
   for the following query {query}
   which of the following types of ai model is preferable to use 

   types = {types}

   give response Using the JSON schema :
   model = {schema}
   """

   response = llm_model.generate_content(prompt)
   type = transform_string(string_to_dict(response.text)["model"])
   models = give_models(type)
   api = find_api(models[0])
   print(api)
   return string_to_dict(api)["code"]
