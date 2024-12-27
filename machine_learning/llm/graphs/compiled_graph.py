from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.graph.state import CompiledStateGraph

from database.sqlite import sqlite_connection
from machine_learning.llm.edges.conditionals.should_call_tools import should_call_tools
from machine_learning.llm.nodes.agent_node import call_llm_model
from machine_learning.llm.nodes.tools_node import tool_node

checkpointer: SqliteSaver = SqliteSaver(conn=sqlite_connection)
workflow: StateGraph = StateGraph(state_schema=MessagesState)

workflow.add_node(node="agent", action=call_llm_model)
workflow.add_node(node="tools", action=tool_node)

workflow.add_edge(start_key=START, end_key="agent")
workflow.add_conditional_edges(source="agent", path=should_call_tools)
workflow.add_edge(start_key="tools", end_key="agent")

compiled_graph: CompiledStateGraph = workflow.compile(checkpointer=checkpointer)
compiled_graph.get_graph().draw_mermaid_png(output_file_path="compiled_graph.png")
