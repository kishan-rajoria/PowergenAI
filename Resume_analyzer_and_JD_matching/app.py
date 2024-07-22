from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
# from PIL import Image
# import base64
# import PyPDF2
from PyPDF2 import PdfReader
import google.generativeai as genai
# import io
# Set the environment variable
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read PDF content
        pdf_reader = PdfReader(uploaded_file)
        # Extract text from the first page (you may need to adjust based on your requirements)
        text = pdf_reader.pages[0].extract_text()

        return text
    else:
        raise FileNotFoundError("No file uploaded")

    #     pdf_parts = [
    #         {
    #             "mime_type": "text/plain",
    #             "data": base64.b64encode(text.encode()).decode()  # encode to base64
    #         }
    #     ]
    #     return pdf_parts
    # else:
    #     raise FileNotFoundError("No file uploaded")

# Streamlit app
st.set_page_config(page_title="Resume Analyzer")
st.header("Resume Analyzer Tracking system")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (In PDF only)...", type=["pdf"])
pdf_content = ""

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    pdf_content = input_pdf_setup(uploaded_file)
else:
    st.write("Please upload a valid PDF file.")

submit1 = st.button("Summary About Resume")
submit2 = st.button("How Can I Improvise Skills")
submit3 = st.button("What are the Missing Keywords")
submit4 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager in the field of data science,
full stack web dovelopement, big data engineer, devops data, data analyst, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in data science, 
your role is to scrutinize the resume in light of the job description provided. 
Share your insights on the candidate's suitability for the role from an HR perspective. 
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. As a Human Resource manager,
 assess the compatibility of the resume with the role. Give me what are the keywords that are missing
 Also, provide recommendations for enhancing the candidate's skills and identify which areas require further development.
"""
input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload resume to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload resume to proceed.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload resume to proceed.")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload resume to proceed.")


st.markdown("---")
st.caption("Resume Analyzer - Making resume Evaluation easy -(credit: krish naik)")