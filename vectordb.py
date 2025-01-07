import pinecone
from pinecone import Pinecone
import os
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.embeddings.openai import OpenAIEmbeddings


os.environ["PINECONE_API_KEY"] = ""  # Replace with your actual Pinecone API key
class VectorDB():

    pinecone_key=""  # Replace with your Pinecone API key
    open_api_key = ""
    dimension = 1536
    index_name = "langchain"
    embedding = OpenAIEmbeddings(api_key =open_api_key )
    pinecone_client = Pinecone(api_key = pinecone_key)

    def index_init(self, doc):
        index = LangchainPinecone.from_documents(doc, self.embedding, index_name= self.index_name)
        return index



