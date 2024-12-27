from typing import TypedDict

from PIL import Image
from pydantic import BaseModel


class YoloResultSchema(BaseModel):
    detect_class_id_list: list[int] = []
    detect_object_confidence_list: list[float] = []
    xyxyn: list[list[float]] = []
    xywhn: list[list[float]] = []
    class_name_dict: dict = []


class ImagePredictedSchema(TypedDict):
    image: Image.Image
    image_path: str
