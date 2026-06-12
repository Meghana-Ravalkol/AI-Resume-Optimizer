from config.settings import llm


response = llm.invoke(
    "Say exactly: OpenRouter connection successful"
)

print(response.content)