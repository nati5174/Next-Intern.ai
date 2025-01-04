RESUME_TEMPLATE = """
You are an AI assistant helping a student tailor their resume for a specific internship application.

The student’s original resume is provided below:
{resume}

The job description for the internship is as follows:
{job_description}

Your task is to:
1. Identify the most relevant experiences, skills, and projects from the resume that align with the job description.
2. Tailor the language to emphasize these relevant details.
3. Remove or de-emphasize less relevant information.
4. Format the tailored resume in Jake's Resume format.
"""


COVER_LETTER_TEMPLATE = """
You are an AI assistant helping a student write a tailored cover letter for a specific job application.

The student’s original cover letter or data is provided below:
{cover}

The job description for the job position is as follows:
{job_description}

Your task is to:
1. Craft a compelling introduction that explains the student's interest in the job and company.
2. Highlight the student's most relevant experiences, skills, and projects that align with the job description.
3. Emphasize how the student's qualifications make them an ideal fit for the position.
4. Keep the tone professional and enthusiastic, while maintaining clarity and conciseness.
5. Close with a strong, confident statement of interest, inviting the employer to discuss the student’s qualifications further.
"""
