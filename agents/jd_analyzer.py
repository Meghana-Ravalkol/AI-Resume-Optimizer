from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def jd_analyzer_node(state):
    """
    Analyzes the Job Description and extracts
    important information for resume optimization.
    """

    # Retrieve relevant job skill knowledge
    knowledge = retrieve_knowledge(
        query=state["job_description"],
        sources=[
            "job_skills.txt",
            "industry_keywords.txt"
        ],
        limit=5
    )


    prompt = f"""
    You are an expert Job Description Analyst.

    Analyze the job description using the provided
    industry knowledge.

    INDUSTRY KNOWLEDGE:
    {knowledge}


    JOB DESCRIPTION:
    {state["job_description"]}


    Extract the following:

    1. Job Role / Title

    2. Required Technical Skills

    3. Preferred Skills

    4. Required Experience Level

    5. Key Responsibilities

    6. Important ATS Keywords

    7. What the resume should emphasize


    Instructions:
    - Prioritize skills explicitly mentioned in the job description.
    - Use industry knowledge to identify related skills and keywords.
    - Do not add irrelevant technologies.
    - Keep the analysis structured and concise.


    Provide a well-structured analysis.
    """

    response = llm.invoke(prompt)


    return {
        "jd_analysis": response.content,

        "messages": [
            AIMessage(
                content=f"JD Analysis Completed\n\n{response.content}"
            )
        ]
    }