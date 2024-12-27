from langchain_core.messages import (
    AnyMessage,
)
from langgraph.graph import MessagesState, END


def should_call_tools(state: MessagesState):
    messages: list[AnyMessage] = state["messages"]
    last_message: AnyMessage = messages[-1]

    if last_message.tool_calls:
        return "tools"
    return END
