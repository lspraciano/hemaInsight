import os

from PIL import Image, ImageFile
from langchain_core.tools import tool


@tool
def display_image_tool(
        image_path: str
) -> str:
    """
    Displays an image on the user's screen.
    """
    try:
        if not os.path.exists(image_path):
            return f"Error: The image path '{image_path}' does not exist."

        image: ImageFile = Image.open(image_path)
        image.show()
        return f"Image '{os.path.basename(image_path)}' displayed successfully."
    except Exception as e:
        return f"Error: Failed to display the image. Details: {str(e)}"
