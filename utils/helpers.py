from config.settings import MAX_QUESTIONS


def can_ask_more_questions(state):
    """
    Checks whether the system can ask more questions.
    This will be used by LangGraph conditional edges.
    """

    return state["questions_asked"] < MAX_QUESTIONS


def increment_question_count(state):
    """
    Increases the number of questions asked.
    """

    state["questions_asked"] += 1

    return state


def format_resume_sections(resume_text):
    """
    Basic resume formatting utility.
    More advanced formatting can be added later.
    """

    return resume_text.strip()