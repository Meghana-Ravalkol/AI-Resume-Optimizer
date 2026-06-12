from langchain_core.messages import AIMessage

from config.settings import llm, MAX_QUESTIONS
from vector_db.retriever import retrieve_knowledge


def question_planner_node(state):
    """
    Generates intelligent follow-up questions
    to gather missing candidate information.
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
    You are a Smart Resume Interview Agent.

    Use the industry knowledge, job requirements,
    and candidate gaps to ask the most useful
    questions required to improve the resume.


    INDUSTRY KNOWLEDGE:
    {knowledge}


    JOB DESCRIPTION ANALYSIS:
    {state["jd_analysis"]}


    CURRENT GAP ANALYSIS:
    {state["skill_gap_analysis"]}


    PREVIOUS QUESTIONS:
    {state["generated_questions"]}


    PREVIOUS ANSWERS:
    {state["user_answers"]}


    Maximum number of questions allowed:
    {MAX_QUESTIONS}


    Rules:

    - Ask only one question at a time.
    - Do not repeat previous questions.
    - Prioritize missing projects, achievements,
      measurable results, certifications,
      responsibilities, and skills.
    - Ask questions that will improve the final resume.
    - Keep the question clear and professional.


    Generate only the next best question.
    """


    response = llm.invoke(prompt)


    return {
        "generated_questions": [
            response.content
        ],

        "questions_asked": (
            state["questions_asked"] + 1
        ),

        "messages": [
            AIMessage(
                content=f"Question Generated:\n{response.content}"
            )
        ]
    }