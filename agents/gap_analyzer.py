from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def gap_analyzer_node(state):
    """
    Compare the candidate resume with job requirements
    and identify missing skills and experiences.
    """

    knowledge = retrieve_knowledge(
        query=state["jd_analysis"],
        sources=[
            "job_skills.txt",
            "industry_keywords.txt"
        ],
        limit=5
    )


    prompt = f"""
    You are an expert Resume Gap Analysis Agent.

    Use the industry knowledge to compare the candidate's
    resume against the job requirements.


    INDUSTRY KNOWLEDGE:
    {knowledge}


    JOB REQUIREMENTS:
    {state["jd_analysis"]}


    CANDIDATE RESUME:
    {state["current_resume"]}


    ADDITIONAL USER INFORMATION:
    {state["user_answers"]}


    Identify:

    1. Missing technical skills
    2. Missing soft skills
    3. Missing projects or work experience
    4. Missing certifications
    5. Weak areas in the resume
    6. Skills that should be emphasized


    Instructions:
    - Compare only against the job requirements.
    - Use industry knowledge for better recommendations.
    - Do not suggest irrelevant technologies.
    - Give practical suggestions.


    Provide a clear structured gap analysis.
    """


    response = llm.invoke(prompt)


    return {
        "skill_gap_analysis": response.content,

        "messages": [
            AIMessage(
                content=f"Gap Analysis Completed\n\n{response.content}"
            )
        ]
    }