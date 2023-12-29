from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_response(input, image):
    model = genai.GenerativeModel("gemini-pro-vision")

    if input != '':
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title='Gemini Image Chatbot')

st.header('QnA Text With Image Chatbot Using Gemini LLM Model')



input = st.text_input('Ask your question ....', key='input')


uploaded_file = st.file_uploader('Choose an image', type=['jpg','jpeg','png'])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=False)

submit = st.button('Tell me about the image')
if submit:
    response = get_gemini_response(input,image)
    st.subheader('The response is ....')
    st.success(response)
