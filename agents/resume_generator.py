from langchain_core.messages import AIMessage

from config.settings import llm
from vector_db.retriever import retrieve_knowledge


def resume_generator_node(state):
    """
    Generates an ATS-optimized resume using
    templates, examples, and candidate information.
    """

    knowledge = retrieve_knowledge(
        query=state["jd_analysis"],
        sources=[
            "resume_templates.txt",
            "resume_examples.txt"
        ],
        limit=8
    )


    prompt = f"""
    You are an Expert Resume Writer.

    Use the provided resume templates and examples
    as guidance for formatting, structure, and writing style.


    RESUME KNOWLEDGE:
    {knowledge}


    JOB DESCRIPTION ANALYSIS:
    {state["jd_analysis"]}


    CURRENT RESUME:
    {state["current_resume"]}


    GAP ANALYSIS:
    {state["skill_gap_analysis"]}


    USER ADDITIONAL INFORMATION:
    {state["user_answers"]}


    SKILL RECOMMENDATIONS:
    {state["suggested_skills"]}


    Create an ATS-optimized professional resume.


    Include these sections when relevant:

    1. Professional Summary

    2. Technical Skills

    3. Work Experience

    4. Projects

    5. Education

    6. Certifications

    7. Achievements


    Instructions:

    - Maintain truthful information only.
    - Do not invent fake experience, projects, or certifications.
    - Emphasize the candidate's existing strengths.
    - Improve wording using professional resume language.
    - Include relevant keywords from the job description.
    - Use measurable achievements when the candidate provides them.
    - Keep formatting clean and ATS-friendly.


    Generate the final polished resume.
    """


    response = llm.invoke(prompt)


    return {
        "optimized_resume": response.content,

        "messages": [
            AIMessage(
                content=(
                    "Resume Generated Successfully\n\n"
                    f"{response.content}"
                )
            )
        ]
    }