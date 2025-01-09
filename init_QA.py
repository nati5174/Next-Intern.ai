# this must be ran in the begening to initlize the database

import streamlit as st
import pinecone
from pinecone import Pinecone
import langchain_helper
import pdf
st.title("Initlize QA here")
pdf_instance = pdf.PDF()
import vectordb

file = st.file_uploader("provide interview questions here")
pinecone_key=""  # Replace with your Pinecone API key


if file:
    name = "kalu2"
    doc = pdf_instance.read_pdf_as_list(file)
    docs = pdf_instance.chunk_data(doc)
    db = vectordb.VectorDB()
    db.create_index(name)
    index = db.index_init(docs, name)


