from langchain_core.messages import AIMessage


def user_interaction_node(state):
    """
    Handles user answers collected during the 
    resume information gathering phase.
    """

    return {
        "messages": [
            AIMessage(
                content="User information has been collected successfully."
            )
        ]
    }