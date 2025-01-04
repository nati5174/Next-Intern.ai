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


def generate_new_cover_letter(cover, job_description):

    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    prompt = PromptTemplate(input_variables=['cover', 'job_description'], template=COVER_LETTER_TEMPLATE)

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run({"cover": cover, "job_description": job_description})
        

    return response


if __name__ == "__main__":
    print(generate_new_cover_letter("Nethanel Reta 647-740-6403 | nethanel.reta@mail.utoronto.ca | https://github.com/nati5174 | https://www.linkedin.com/in/nethanel-reta Education University of Toronto Toronto, ON Bachelor of Science in Statistics - Minor in Computer Science June 2027 • Relevant Coursework: Software Design (Java), Computer Science II (Data Structures, Algorithms), Calculus II, Linear Algebra II Experience Data Processing Member / Remote Sensing Analyst May 2024 – Oct 2024 University of Toronto Toronto, ON • Enhanced reflectance data by adding noise to simulate real-world signal-to-noise ratios (SNR). • Employed numpy to generate and scale Gaussian noise, integrating it with original data to improve robustness in data analysis. Front-End Engineer Sep 2024 – Present University of Toronto Formula Racing Team Toronto, ON • Developed and maintained the team’s web portal using React.js, ensuring a user-friendly interface for displaying real-time race data, team statistics, and performance metrics. • Collaborated with back-end engineers to integrate the front-end with real-time data from the racing sensors, utilizing Django for API communication. Projects CodeLens AI | Python, OpenCV, Flask ∗ Developed a web application using Flask and PyTorch to capture code snippets from physical media (whiteboards, blackboards, paper) and convert them into annotated digital code files. ∗ Implemented computer vision algorithms to recognize and convert handwritten code into editable text. ∗ Designed an interactive user interface with HTML and CSS to facilitate seamless code uploading and annotation. AI-Powered Resume Builder | Python, Streamlit, OpenAI API, PyPDF2 ∗ Built a web app to tailor resumes using AI by analyzing resumes and job postings. ∗ Enabled PDF upload and text extraction for resumes and job descriptions. ∗ Developed a mock interview tool with AI feedback based on user input. Planteeze | Java, SQLite, Agile, Stripe API, JUnit, Jira Jun. 2024 - Aug. 2024 ∗ Collaborated in an Agile (Scrum) environment with a team of 4, managing 20+ user stories on Jira and conducting daily stand-up meetings. ∗ Developed an Android app on Android Studio with version control through Git. ∗ Integrated a Stripe payment feature within the app, enabling secure payment processing for 50+ users. ∗ Implemented SQLite database to store and manage user payment transactions and app data efficiently.", "Programming Languages: Python (with libraries like NumPy, pandas, TensorFlow, Keras, PyTorch) R JavaScript (for web-based ML models) Java (for large-scale machine learning systems) C++ (for high-performance applications) SQL (for data manipulation and querying) MATLAB (for prototyping and research) Machine Learning & AI Techniques: Supervised Learning (e.g., Regression, Classification) Unsupervised Learning (e.g., Clustering, Dimensionality Reduction) Reinforcement Learning Neural Networks (Feedforward, CNNs, RNNs) Deep Learning Natural Language Processing (NLP) Computer Vision Time Series Analysis Data Analysis & Preprocessing: Data wrangling and cleaning Feature engineering and feature selection Handling missing data Data normalization and standardization Exploratory Data Analysis (EDA) Outlier detection and handling Statistical Knowledge: Probability and Statistics Hypothesis testing Statistical inference A/B testing Bayesian methods Modeling & Evaluation: Cross-validation techniques (e.g., K-fold, leave-one-out) Hyperparameter tuning (e.g., GridSearch, RandomizedSearchCV) Model selection (e.g., Choosing between Random Forest, SVM, etc.) Metrics for evaluating models (Accuracy, Precision, Recall, F1-Score, AUC-ROC) Loss functions (e.g., Mean Squared Error, Cross-Entropy) Deployment & Production: Docker and containerization Model deployment frameworks (e.g., Flask, FastAPI) Cloud platforms (AWS, Azure, GCP) CI/CD pipelines for machine learning Model monitoring and maintenance Software Engineering & Systems Design: Version control (Git) REST APIs for interacting with models Multithreading and parallelism Distributed computing (e.g., Hadoop, Spark) Scalability and optimization of ML models Big Data Technologies: Hadoop Spark SQL and NoSQL Databases (e.g., MongoDB, Cassandra) Data Lakes Tools & Libraries: Scikit-learn (for traditional ML models) TensorFlow and PyTorch (for deep learning models) XGBoost, LightGBM (for gradient boosting) OpenCV (for computer vision) NLTK, spaCy, transformers (for NLP tasks) Plotly, Matplotlib, Seaborn (for data visualization) Soft Skills: Problem-solving mindset Communication (ability to explain complex models to non-technical teams) Collaboration and teamwork (working with Data Scientists, Product Managers) Time management and prioritization Adaptability to new tools, technologies, and challenges This list contains a mix of technical skills, programming expertise, and soft skills that are highly valued in the field of machine learning engineering. You can use these in your job descriptions or resume-building processes."))