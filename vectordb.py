import pinecone
from pinecone import Pinecone
import os
import vectordb
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.embeddings.openai import OpenAIEmbeddings

import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


open_ai_key= os.getenv('openai_key')
pinecone_key= os.getenv('pinecone_key')

class VectorDB():

    pinecone_key= pinecone_key
    open_api_key = open_ai_key

    dimension = 1536
    #index_name = "langchain"
    embedding = OpenAIEmbeddings(api_key =open_api_key )
    pinecone_client = Pinecone(api_key = pinecone_key)


    def index_init(self, doc, index_name):
        index = LangchainPinecone.from_documents(doc, self.embedding, index_name= index_name)
        return index
    
    def create_index(self, name):
        self.pinecone_client.create_index(name= name, dimension=1536, spec=pinecone.ServerlessSpec(cloud='aws', region='us-east-1'))




