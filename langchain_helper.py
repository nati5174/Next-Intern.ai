import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI  # Correct import for chat models
from langchain.chains.question_answering import load_qa_chain
import vectordb
from constants import RESUME_TEMPLATE, COVER_LETTER_TEMPLATE


class LangchiainHelper():

    llm = ChatOpenAI(model="gpt-4", temperature=0.7, openai_api_key=openai_key)
    pineconedb = vectordb.VectorDB()
    os.environ['OPENAI_API_KEY'] = openai_key

    def generate_new_resume(resume, job_description, llm):

        prompt = PromptTemplate(input_variables=['resume', 'job_description'], template=RESUME_TEMPLATE)

        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.run({"resume": resume, "job_description": job_description})
            

        return response


    def generate_new_cover_letter(cover, job_description, llm):

        prompt = PromptTemplate(input_variables=['cover', 'job_description'], template=COVER_LETTER_TEMPLATE)

        chain = LLMChain(llm=llm, prompt=prompt)

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