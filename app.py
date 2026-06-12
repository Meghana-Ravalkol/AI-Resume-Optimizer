from workflow.resume_workflow import app


initial_state = {
    "messages": [],

    "job_description": """
    Looking for an AI Engineer with experience in Python,
    LangChain, LangGraph, RAG, vector databases, and LLM applications.
    """,

    "current_resume": """
    Computer Science student with Python experience.
    Built machine learning projects and worked on basic AI applications.
    """,
    "candidate_information": "",

    "jd_analysis": "",

    "generated_questions": [],

    "user_answers": [],

    "questions_asked": 0,

    "skill_gap_analysis": "",
    "missing_skills": [],

    "suggested_skills": [],

    "optimized_resume": "",

    "resume_score": 0,
    "improvement_feedback": "",
    "completed": False
}


result = app.invoke(initial_state)


print("\n" + "="*60)
print("FINAL OPTIMIZED RESUME")
print("="*60)
print(result["optimized_resume"])


print("\n" + "="*60)
print("FINAL RESUME REVIEW")
print("="*60)
print(result["improvement_feedback"])