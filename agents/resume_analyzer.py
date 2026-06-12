from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def resume_analyzer_node(state):
    """
    Analyze the candidate's current resume
    against job requirements and resume best practices.
    """

    knowledge = retrieve_knowledge(
        query=state["current_resume"],
        sources=[
            "ats_rules.txt",
            "action_verbs.txt",
            "resume_examples.txt"
        ],
        limit=5
    )


    prompt = f"""
    You are an Expert Resume Analysis Agent.

    Use the resume knowledge provided to evaluate
    the candidate's resume.


    RESUME KNOWLEDGE:
    {knowledge}


    JOB DESCRIPTION ANALYSIS:
    {state["jd_analysis"]}


    CURRENT RESUME:
    {state["current_resume"]}


    Analyze:

    1. Candidate strengths

    2. Matching skills and experiences

    3. Missing information

    4. Weak resume sections

    5. ATS issues

    6. Better wording and action verbs


    Instructions:

    - Compare the resume with the target job.
    - Identify missing keywords.
    - Suggest ATS-friendly improvements.
    - Do not invent fake experience.


    Provide a detailed structured analysis.
    """


    response = llm.invoke(prompt)


    return {
        "skill_gap_analysis": response.content,

        "messages": [
            AIMessage(
                content=f"Resume Analysis Completed\n\n{response.content}"
            )
        ]
    }