import streamlit as st
import langchain_helper
import pdf
import pinecone
import vectordb
from langchain.schema import AIMessage,HumanMessage,SystemMessage
from langchain.vectorstores import Pinecone as LangchainPinecone
from constants import QUERY


# Initialize session state if not already initialized
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""


pdf_instance = pdf.PDF()
lang_instance = langchain_helper.LangchiainHelper()

st.title("Next-Intern")

role  = st.sidebar.selectbox("Pick Something", ("Home","Resume Creatr", "Cover letter creatr", "testing"))

if role == "Home":
    st.write("Next Intern is a web-app which helps students in getting their next internship. The app provides, users with a oppurtunity to find internships based on location and desired position, a resume generator based on job your applying to, and a cover letter generator based off of the job your applying to.")
elif role == "Resume Creatr":
    st.subheader("Resume")
    uploaded_file = st.file_uploader("Upload your Resume or data about yourself!")
    job_description = st.text_area("Enter Job Description")

    if uploaded_file and job_description:
        if st.button("Generate Resume"):
            with st.spinner('Generating...'):
                resume =pdf_instance.extract_pdf_info(uploaded_file)
                new_resume = lang_instance.generate_new_resume(resume, job_description)
                
            st.success("Done!")
            st.write(new_resume)
            #pdf_new = pdf.generate_pdf(new_resume)
            #st.download_button(label ="Download PDF", data=pdf_new, file_name="tailered_resume.pdf", mime="application/pdf")

elif role == "Cover letter creatr":
    st.subheader("Cover Letter")
    uploaded_file = st.file_uploader("Upload your Cover Letter or data about yourself!")
    job_description = st.text_area("Enter Job Description")

    if uploaded_file and job_description:
        if st.button("Generate Cover-letter"):
            with st.spinner('Generating...'):
                cover = pdf_instance.extract_pdf_info(uploaded_file)
                new_cover = lang_instance.generate_new_resume(cover, job_description)
                
            st.success("Done!")
            st.write(new_cover)

elif role == "testing":
    job = st.selectbox("Pick Role", ("Software", "Machine Learning", "Deep Learning", "Front-End", "Back-end")) 
    level = st.selectbox("Pick level", ("Moderate", "Difficult"))  
                       
    if job and level:
        db = vectordb.VectorDB()
        pinecone_client = db.pinecone_client
        index = pinecone_client.Index("interview-questions3")
        embedding= db.embedding
        index = LangchainPinecone(index=index, embedding=embedding, text_key="text")

        chain = langchain_helper.LangchiainHelper().mock_interview()
        messages = [SystemMessage(QUERY),]

        s=f"Give me a list of 5 random {job} related questions, which are off dificulty {level}"
        ai_response = langchain_helper.LangchiainHelper().retrieve_answer(s, chain, index)
        st.write(ai_response)

        you = st.text_input("input question for answer")
        if you:
             you = "Find out how" + you
             ai_response1 = langchain_helper.LangchiainHelper().retrieve_answer(you, chain, index)
             st.write(ai_response1)

