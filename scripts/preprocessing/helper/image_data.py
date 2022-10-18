from helper.image_label_data import image_label_data
from helper.image_measurement_data import image_measurement_data
from typing import List

class image_data:

    def __init__(self, image_folder: str, image_file_name: str, measurement: image_measurement_data):

        self._image_folder = image_folder
        self._image_file_name = image_file_name
        self._measurement = measurement
        self._labels:List[image_label_data] = []

    def get_image_folder(self) -> str:
        return self._image_folder

    def get_image_file_name(self) -> str:
        return self._image_file_name

    def get_measurement(self) -> image_measurement_data:
        return self._measurement

    def get_labels(self) -> List[image_label_data]:
        return self._labels
