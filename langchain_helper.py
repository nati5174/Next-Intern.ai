import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI  # Correct import for chat models

from constants import RESUME_TEMPLATE, COVER_LETTER_TEMPLATE

os.environ['OPENAI_API_KEY'] = openai_key

def generate_new_resume(resume, job_description):

    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    prompt = PromptTemplate(input_variables=['resume', 'job_description'], template=RESUME_TEMPLATE)

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run({"resume": resume, "job_description": job_description})
        

    return response