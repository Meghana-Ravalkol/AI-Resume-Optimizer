from vector_db.retriever import retrieve_knowledge


query = "How can I improve ATS score?"


response = retrieve_knowledge(
    query,
    sources=[
        "ats_rules.txt",
        "action_verbs.txt"
    ]
)


print("\nRetrieved Knowledge:\n")
print(response)