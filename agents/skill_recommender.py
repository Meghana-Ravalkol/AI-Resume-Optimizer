from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def skill_recommender_node(state):
    """
    Recommends skills, projects, and learning paths
    based on candidate gaps and industry requirements.
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
    You are an Expert Career Skill Recommendation Agent.

    Use the industry knowledge to recommend practical
    improvements for the candidate.


    INDUSTRY KNOWLEDGE:
    {knowledge}


    JOB REQUIREMENTS:
    {state["jd_analysis"]}


    GAP ANALYSIS:
    {state["skill_gap_analysis"]}


    Recommend:


    1. Technical skills to learn

    2. Soft skills to improve

    3. Practical projects to build

    4. Certifications or courses to consider

    5. Short-term learning roadmap (1-3 months)

    6. Long-term career growth roadmap (6-12 months)


    Instructions:
    - Prioritize skills relevant to the target job.
    - Do not recommend unrelated technologies.
    - Focus on realistic and practical improvements.
    - Explain why each recommendation is valuable.


    Provide a structured recommendation.
    """


    response = llm.invoke(prompt)


    return {
        "suggested_skills": [
            response.content
        ],

        "messages": [
            AIMessage(
                content=(
                    "Skill Recommendations Completed\n\n"
                    f"{response.content}"
                )
            )
        ]
    }