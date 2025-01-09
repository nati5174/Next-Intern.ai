import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI  # Correct import for chat models
from langchain.chains.question_answering import load_qa_chain
import vectordb

from constants import RESUME_TEMPLATE, COVER_LETTER_TEMPLATE

import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()


open_ai_key= os.getenv('openai_key')
pinecone_key= os.getenv('pinecone_key')

class LangchiainHelper():
    openai_key = open_ai_key

    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_key)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
    

    os.environ['OPENAI_API_KEY'] = openai_key

    def generate_new_resume(self,resume, job_description):

        prompt = PromptTemplate(input_variables=['resume', 'job_description'], template=RESUME_TEMPLATE)

        chain = LLMChain(llm=self.llm,prompt=prompt)

        response = chain.run({"resume": resume, "job_description": job_description})
            

        return response


    def generate_new_cover_letter(self,cover, job_description):

        prompt = PromptTemplate(input_variables=['cover', 'job_description'], template=COVER_LETTER_TEMPLATE)

        chain = LLMChain(llm=self.llm, prompt=prompt)

        response = chain.run({"cover": cover, "job_description": job_description})
            

        return response

    def mock_interview(self):
        chain = load_qa_chain(self.llm, chain_type="stuff")
        return chain
    
    def retrieve_query(self, query, index, k=3):
        #chain = self.mock_interview(llm)
        result = index.similarity_search(query, k)
        return result
    
    def retrieve_answer(self, query, chain, index):
        result = self.retrieve_query(query, index)
        answer = chain.run(input_documents=result, question=query)
        return answer
    
    



    

#if __name__ == "__main__":