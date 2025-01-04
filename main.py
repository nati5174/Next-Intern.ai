import streamlit as st
import llm_agent
import pdf
import time




st.title("Next-Intern")

role  = st.sidebar.selectbox("Pick Something", ("Home","Resume Creatr", "Cover letter creatr"))

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
                new_resume = llm_agent.generate_new_resume(resume, job_description)
                
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
                new_cover = llm_agent.generate_new_resume(cover, job_description)
                
            st.success("Done!")
            st.write(new_cover)
