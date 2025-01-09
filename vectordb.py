import pinecone
from pinecone import Pinecone
import os
import vectordb
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.embeddings.openai import OpenAIEmbeddings


os.environ["PINECONE_API_KEY"] = ""  # Replace with your Pinecone API key

class VectorDB():

    pinecone_key=""  # Replace with your Pinecone API key
    open_api_key = '-'
    dimension = 1536
    #index_name = "langchain"
    embedding = OpenAIEmbeddings(api_key =open_api_key )
    pinecone_client = Pinecone(api_key = pinecone_key)


    def index_init(self, doc, index_name):
        index = LangchainPinecone.from_documents(doc, self.embedding, index_name= index_name)
        return index
    
    def create_index(self, name):
        self.pinecone_client.create_index(name= name, dimension=1536, spec=pinecone.ServerlessSpec(cloud='aws', region='us-east-1'))




