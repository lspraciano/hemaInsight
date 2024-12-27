from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from images.images_handler import list_image_paths
from machine_learning.llm.graphs.compiled_graph import compiled_graph

load_dotenv()

path_list: list[str] = list_image_paths(folder="./images/originals")

prompt_input: str = f"""
    Quais leucócitos foram identificados como verificar nos paths: {path_list}? 
    Cite as imagens onde eles estão
    
    """

final_state: dict = compiled_graph.invoke(
    input={
        "messages": [
            HumanMessage(content=prompt_input)
        ]
    },
    config={"configurable": {"thread_id": "3"}}
)

print(final_state["messages"][-1].content)
