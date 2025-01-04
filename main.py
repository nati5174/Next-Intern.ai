import streamlit as st
import llm_agent
import pdf
import time




st.title("Next-Intern")

role  = st.sidebar.selectbox("Pick Something", ("Home","Resume Creatr", "Cover letter creatr"))
