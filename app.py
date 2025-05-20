import streamlit as st
from main import recommend_career
from resume_parser import extract_text_from_pdf

st.title("AI Career Recommender")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
user_input = st.text_area("Or describe your interests and skills")

if st.button("Get Recommendations"):
    if uploaded_file:
        user_text = extract_text_from_pdf(uploaded_file)
    elif user_input:
        user_text = user_input
    else:
        st.warning("Please provide input via text or upload.")
        user_text = ""

    if user_text:
        results = recommend_career(user_text)
        for role, score in results:
            st.success(f"{role} - {round(score*100, 2)}% match")
