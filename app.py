from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import base64
import io
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
    ## Convert PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        ## Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

## Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell me About the Resume")
submit2 = st.button("How to Improve the Resume")
submit3 = st.button("Percentage Match with Job Description")

input_prompt1 = """
You are an experienced with experience in the field of any one job role from
Data science, Web development, Data engineering, DEVOPS, Data analyst, AI/ML engineer,
Your task is to review the provided resume against the job description for 
this profiles. 
Please share your professional evolution on weather the 
candidates profile aligns with the role.
Highlight strengths and weaknesses of the applicant in relation to the 
specified job requirements."""

input_prompt3 = """
You are a skilled ATS applicant tracking system scanner with a 
deep understanding of any one job role Data science, Web development, big Data engineering, 
Data analyst, AI/ML engineer and ATS functionality, your task is to evaluate the resume 
against the provided job description. 
Give me the percentage of match if the resume matches the job description. 
First the output should come as percentage and then keywords missing 
and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is...")
        st.write(response)
    else:
        st.write("Please upload a Resume file.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Response...")
        st.write(response)
    else:
        st.write("Please upload a Resume file.")