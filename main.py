from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from machine_learning.llm.graphs.compiled_graph import compiled_graph

load_dotenv()


prompt_input: str = f"""
    Quais leucócitos são encontrados nessas imagens?
    
    """

final_state: dict = compiled_graph.invoke(
    input={
        "messages": [
            HumanMessage(content=prompt_input)
        ]
    },
    config={"configurable": {"thread_id": "1"}}
)

print(final_state["messages"][-1].content)
