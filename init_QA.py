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
file1 = st.file_uploader("ADD NEW QUESTIONS, IF ALREADY PROVIDE QUESTIONS BEFORE")
db = vectordb.VectorDB()
name = "interview-questions3"

if file:
    doc = pdf_instance.read_pdf_as_list(file)
    docs = pdf_instance.chunk_data(doc)
    db.create_index(name)
    index = db.index_init(docs, name)

if file1:
    doc = pdf_instance.read_pdf_as_list(file1)
    docs = pdf_instance.chunk_data(doc)
   #embedding_model = db.embedding
   #pinecone_client = db.pinecone_client
   #index = pinecone_client.Index("interview-questions3")
    index = db.index_init(docs, name)