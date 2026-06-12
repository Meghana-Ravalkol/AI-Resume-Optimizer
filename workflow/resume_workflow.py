from langgraph.graph import StateGraph, END

from state.resume_state import ResumeState

from agents.jd_analyzer import jd_analyzer_node
from agents.resume_analyzer import resume_analyzer_node
from agents.question_planner import question_planner_node
from agents.user_interaction import user_interaction_node
from agents.gap_analyzer import gap_analyzer_node
from agents.skill_recommender import skill_recommender_node
from agents.resume_generator import resume_generator_node
from agents.resume_reviewer import resume_reviewer_node


workflow = StateGraph(ResumeState)


# Add agents
workflow.add_node("jd_analyzer", jd_analyzer_node)
workflow.add_node("resume_analyzer", resume_analyzer_node)
workflow.add_node("question_planner", question_planner_node)
workflow.add_node("user_interaction", user_interaction_node)
workflow.add_node("gap_analyzer", gap_analyzer_node)
workflow.add_node("skill_recommender", skill_recommender_node)
workflow.add_node("resume_generator", resume_generator_node)
workflow.add_node("resume_reviewer", resume_reviewer_node)


# Starting point
workflow.set_entry_point("jd_analyzer")


# Workflow connections
workflow.add_edge("jd_analyzer", "resume_analyzer")
workflow.add_edge("resume_analyzer", "question_planner")
workflow.add_edge("question_planner", "user_interaction")
workflow.add_edge("user_interaction", "gap_analyzer")
workflow.add_edge("gap_analyzer", "skill_recommender")
workflow.add_edge("skill_recommender", "resume_generator")
workflow.add_edge("resume_generator", "resume_reviewer")
workflow.add_edge("resume_reviewer", END)


# Compile the graph
app = workflow.compile()