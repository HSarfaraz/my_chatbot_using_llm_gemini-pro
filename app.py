import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')

def main():
  st.set_page_config(page_title="My Chatbot")
  st.markdown("<h1 style='text-align: center; color: #FFF;'>My Chatbot</h1>", unsafe_allow_html=True)
  
  text_input=st.text_area(label="Enter your query here in plain english", label_visibility="hidden", placeholder="Enter your query here in plain english")
 
  submit=st.button("Ask AI")
  if submit:
    response=model.generate_content(text_input)
    st.write(response.text)

main()