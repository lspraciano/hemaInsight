import os

from PIL import Image
from numpy import ndarray
from ultralytics import YOLO
from ultralytics.engine.results import Results, Boxes

from machine_learning.cnn.schemas import YoloResultSchema


def load_yolo_model() -> YOLO | None:
    full_ml_model_path: str = "machine_learning/cnn/cnn_models/white_blood_cells_v7_y10.pt"

    if not os.path.exists(full_ml_model_path):
        return None

    model: YOLO = YOLO(full_ml_model_path)

    return model


def parse_yolo_result_to_schema(
        result: Results,
        class_name_dict: dict,
) -> YoloResultSchema:
    boxes_result: Boxes = result.boxes

    return YoloResultSchema(
        detect_class_id_list=boxes_result.cls.tolist(),
        detect_object_confidence_list=boxes_result.conf.tolist(),
        xyxyn=boxes_result.xyxyn.tolist(),
        xywhn=boxes_result.xywhn.tolist(),
        class_name_dict=class_name_dict
    )


def get_plotted_image_from_result(
        result: Results
) -> Image:
    predict_plotted_array: ndarray = result.plot()
    image_from_array: Image = Image.fromarray(predict_plotted_array[..., ::-1])
    return image_from_array


def yolo_predict(
        image: Image,
) -> tuple[Image, YoloResultSchema] | None:
    yolo_model: YOLO = load_yolo_model()
    image_from_array: Image
    class_name_dict: dict = {
        0: "basófilo",
        1: "eosinófilo",
        2: "linfócito",
        3: "monócito",
        4: "neutrófilo",
        5: "verificar"
    }

    predict_result_list: list[Results] = yolo_model.predict(
        source=image,
        verbose=False,
        conf=0.5
    )
    predict_result: Results = next(iter(predict_result_list))

    image_from_array: Image = get_plotted_image_from_result(
        result=predict_result
    )

    result_schema: YoloResultSchema = parse_yolo_result_to_schema(
        result=predict_result,
        class_name_dict=class_name_dict
    )

    image_full_path: str = image.filename
    image_name: str = os.path.basename(p=image_full_path)
    image_from_array.save(f"./images/detections/pred_{image_name}")

    return image_from_array, result_schema
