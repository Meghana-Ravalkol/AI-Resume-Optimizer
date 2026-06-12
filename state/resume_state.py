from typing import TypedDict, Annotated, List, Dict, Any
import operator


class ResumeState(TypedDict):
    # Conversation history between user and agents
    messages: Annotated[list, operator.add]

    # User inputs
    job_description: str
    current_resume: str
    candidate_information: str

    # Questioning phase
    questions_asked: int
    generated_questions: List[str]
    user_answers: List[str]

    # Analysis phase
    jd_analysis: str
    skill_gap_analysis: str
    missing_skills: List[str]
    suggested_skills: List[str]

    # Resume generation phase
    optimized_resume: str

    # Evaluation phase
    resume_score: int
    improvement_feedback: str

    # Metadata
    completed: bool