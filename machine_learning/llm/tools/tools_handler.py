from machine_learning.llm.tools.display_image_tool import display_image_tool
from machine_learning.llm.tools.images_path_tool import list_image_paths
from machine_learning.llm.tools.leucocytes_tool import leucocytes_detect

tools: list = [
    list_image_paths,
    leucocytes_detect,
    display_image_tool
]
