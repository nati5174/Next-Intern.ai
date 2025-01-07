import streamlit as st
import langchain_helper
import pdf
import vectordb
from langchain.schema import AIMessage,HumanMessage,SystemMessage
from constants import QUERY

pdf_instance = pdf.PDF()

st.title("Next-Intern")

role  = st.sidebar.selectbox("Pick Something", ("Home","Resume Creatr", "Cover letter creatr", "Practise Interview"))

if role == "Home":
    st.write("Next Intern is a web-app which helps students in getting their next internship. The app provides, users with a oppurtunity to find internships based on location and desired position, a resume generator based on job your applying to, and a cover letter generator based off of the job your applying to.")
elif role == "Resume Creatr":
    st.subheader("Resume")
    uploaded_file = st.file_uploader("Upload your Resume or data about yourself!")
    job_description = st.text_area("Enter Job Description")

    if uploaded_file and job_description:
        if st.button("Generate Resume"):
            with st.spinner('Generating...'):
                resume = pdf.extract_pdf_info(uploaded_file)
                new_resume = langchain_helper.generate_new_resume(resume, job_description)
                
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
                cover = pdf.extract_pdf_info(uploaded_file)
                new_cover = langchain_helper.generate_new_resume(cover, job_description)
                
            st.success("Done!")
            st.write(new_cover)



elif role == "Practise Interview":
    st.subheader("Mock Interview")
    upload_resume = st.file_uploader("Upload you resume")
    #upload_job = st.file_uploader("Upload job info")

    if upload_resume:
        chain = langchain_helper.LangchiainHelper().mock_interview()
        doc = pdf_instance.read_pdf_as_list(upload_resume)
        docs = pdf_instance.chunk_data(doc)
        db = vectordb.VectorDB()
        index = db.index_init(docs)

        if st.button("Start inerview"):
            #stores in documents into databse as vectors
            messages = [SystemMessage(QUERY),]
            s = "Based off of my resume give me potential inerview questions, only 1 at a time. Once I've replied and you feel satisifed with the question, go to the next question. Dont go to next question unless a good reply"
            ai_response = langchain_helper.LangchiainHelper().retrieve_answer(s, chain, index)
            print("ai: ",ai_response)


            while True:
                user_input = input("you: ")
                messages.append(HumanMessage(content=user_input))
                ai_response = langchain_helper.LangchiainHelper().retrieve_answer(user_input, chain, index)
                print("ai: ",ai_response)
                messages.append(AIMessage(content=ai_response))            

