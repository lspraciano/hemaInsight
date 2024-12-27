from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState

from machine_learning.llm.llm_models.get_llm_model import get_llm_model
from machine_learning.llm.nodes.tools_node import tools


def call_llm_model(
        state: MessagesState
):
    messages: list[str] = state["messages"]
    llm_model: ChatOpenAI = get_llm_model()
    response: BaseMessage = llm_model.bind_tools(
        tools=tools
    ).invoke(
        input=messages
    )
    return {
        "messages": [response]
    }
