from langchain_openai import ChatOpenAI


def get_llm_model(
        model_name: str = "gpt-4o"
) -> ChatOpenAI:
    if model_name == "gpt-4o":
        return ChatOpenAI(
            model="gpt-4o",
            temperature=0,
        )
