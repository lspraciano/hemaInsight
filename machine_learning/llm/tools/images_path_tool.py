import os

from langchain_core.tools import tool


@tool
def list_image_paths(
        folder_path: str,
        extensions: tuple[str, ...] = ("jpg", "png", "jpeg", "gif")
) -> list[str]:
    """
    Lists all image files in the specified folder and its subfolders, returning their full paths.
    """
    image_paths: list[str] = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(extensions):
                image_paths.append(os.path.join(root, file))
    return image_paths
