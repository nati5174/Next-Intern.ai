# Next-Intern.ai
Next-Intern is a web application designed to assist students in securing their next internship. The platform offers various features that help users prepare for internship applications and interviews. The app leverages AI to generate tailored resumes and cover letters based on the job descriptions provided by users. It also offers a mock interview feature that helps users practice for technical interviews, providing personalized questions based on their desired job role and difficulty level.

Key Features:

Resume Generator: Generates a tailored resume based on the job description a user is applying to.
Cover Letter Generator: Creates a customized cover letter based on the job description.
Mock Interview: Provides random technical interview questions related to a user's chosen role and difficulty level.

Technologies Used:
The following libraries are required to run the project:

  Streamlit: For the interactive user interface.
  Langchain: For language models and prompt handling.
  Pinecone-client: For managing and querying Pinecone vector database.
  Openai: To interact with OpenAI’s GPT models for text generation.
  Pypdf: To extract text from PDF files.
  Fitz: For PDF document manipulation.
  Python-dotenv: To manage environment variables securely.


git clone repo
cd next-intern

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate

pip install -r requirements.txt

You will need API keys for OpenAI and Pinecone.

OpenAI API Key: Sign up for an OpenAI API key at OpenAI's website.
Pinecone API Key: Sign up at Pinecone.io to get your API key.

Create a .env file in the root directory and add the following:

env
Copy code
openai_key=YOUR_OPENAI_API_KEY
pinecone_key=YOUR_PINECONE_API_KEY

streamlit run app.py



