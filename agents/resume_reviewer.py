from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def resume_reviewer_node(state):
    """
    Reviews the optimized resume for ATS compatibility
    and overall job suitability.
    """

    knowledge = retrieve_knowledge(
        query=state["jd_analysis"],
        sources=[
            "ats_rules.txt",
            "action_verbs.txt"
        ],
        limit=5
    )


    prompt = f"""
    You are an Expert ATS Resume Reviewer.

    Use the ATS knowledge and resume best practices
    to evaluate the resume.


    ATS KNOWLEDGE:
    {knowledge}


    JOB DESCRIPTION ANALYSIS:
    {state["jd_analysis"]}


    GENERATED RESUME:
    {state["optimized_resume"]}


    Evaluate the following:


    1. ATS compatibility score out of 100

    2. Job match score out of 100

    3. Resume strengths

    4. Weak sections needing improvement

    5. Missing keywords

    6. Better action verbs or wording improvements

    7. Final recommendations


    Instructions:
    - Consider ATS readability and keyword matching.
    - Suggest stronger action verbs where necessary.
    - Give practical, professional feedback.
    - Be specific rather than generic.


    Provide a detailed structured review.
    """


    response = llm.invoke(prompt)


    return {
        "resume_score": 0,
        "improvement_feedback": response.content,

        "messages": [
            AIMessage(
                content=f"Resume Review Completed\n\n{response.content}"
            )
        ]
    }