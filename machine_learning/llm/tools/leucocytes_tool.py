import os

from PIL import Image
from langchain_core.tools import tool

from machine_learning.cnn.schemas import YoloResultSchema
from machine_learning.cnn.yolo_handler import yolo_predict


@tool
def leucocytes_detect(
        image_path: str
) -> str:
    """
    Detects leukocytes in images by their path.
    """
    result_image: Image
    result_schema: YoloResultSchema

    image_full_path: str = image_path
    image_name: str = os.path.basename(image_full_path)
    image: Image = Image.open(image_path)
    result_image, result_schema = yolo_predict(image)
    output_text: str = f"Image Name: {image_name}\n"

    for index, class_id in enumerate(result_schema.detect_class_id_list):
        output_text += f"""
        Cell #{index} in the image
            Class {result_schema.class_name_dict[int(class_id)]}
            Normalized Coordinates XYWH: {result_schema.xywhn[int(index)]}
                    
        """

    return output_text
