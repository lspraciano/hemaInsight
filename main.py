import uuid

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from machine_learning.llm.graphs.compiled_graph import compiled_graph

load_dotenv()


def main():
    thread_id: str = str(uuid.uuid4())
    print(f"Session UUID: {thread_id}")

    while True:
        prompt_input: str = input("Digite sua mensagem (ou 'sair' para encerrar): ")
        if prompt_input.lower() == "sair":
            print("Encerrando o programa.")
            break

        try:
            final_state = compiled_graph.invoke(
                input={
                    "messages": [
                        HumanMessage(content=prompt_input)
                    ]
                },
                config={"configurable": {"thread_id": thread_id}}
            )

            print(final_state["messages"][-1].content)
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")


if __name__ == "__main__":
    main()
