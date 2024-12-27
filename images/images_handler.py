import os


def list_image_paths(
        folder: str,
        extensions: tuple[str, ...] = ("jpg", "png", "jpeg", "gif")
) -> list[str]:
    image_paths: list[str] = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):
                image_paths.append(os.path.join(root, file))
    return image_paths
