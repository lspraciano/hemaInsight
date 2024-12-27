from langgraph.prebuilt import ToolNode

from machine_learning.llm.tools.leucocytes_tool import leucocytes_detect

tools: list = [leucocytes_detect]
tool_node: ToolNode = ToolNode(tools)
