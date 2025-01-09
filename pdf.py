from pypdf import PdfReader
from typing import List
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz 

class PDF():


    def extract_pdf_info(self, pdf):

        reader = PdfReader(pdf)
        pages = len(reader.pages)

        if pages > 1:
            text = []
            for i in range(pages):
                page = reader.pages[i]
                text.append(page.extract_text())
            return " ".join(text) 

        else:
            return reader.pages[0].extract_text()

     #needed for mock interview   
     #not my code nor implementation
    def read_pdf_as_list(self, file):
    # Ensure the uploaded file is read as bytes
        file_data = file.read()
        doc = fitz.open(stream=file_data, filetype="pdf")
        documents = []
        for i, page in enumerate(doc):
            text = page.get_text()
            documents.append(Document(
                page_content=text,
                metadata={"page": i + 1, "source": "Uploaded File"}
            ))
        return documents


    #for splitting the data when preparing for stored pdf sata in Vector DB
    def chunk_data(self, doc, chunk_size=500, chunk_overlap=50):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        new_doc = splitter.split_documents(doc)
        return new_doc




    