from langgraph.prebuilt import ToolNode

from machine_learning.llm.tools.tools_handler import tools

tool_node: ToolNode = ToolNode(tools)
