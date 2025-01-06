from pypdf import PdfReader
from typing import List
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz 

class PDF():

    def extract_pdf_info(pdf):

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
    def read_pdf_as_list(directory: str):
        doc = fitz.open(directory)
        documents = []
        for i, page in enumerate(doc):
            text = page.get_text()
            # Create a Document object for each page
            documents.append(Document(
                page_content=text,
                metadata={"page": i + 1, "source": directory}
            ))
        return documents  


    #for splitting the data when preparing for stored pdf sata in Vector DB
    def chunk_data(doc, chunk_size, chunk_overlap):
        splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
        new_doc = splitter.split_document(doc)
        return new_doc




    