import tensorflow as tf 
from tensorflow import keras
from typing import List, Tuple
import numpy as np

class image_dataset_for_model_making:
    
    def __init__(self):
        self._images = []
        self._targets: List[Tuple[int, int, int, int]] = []
        self._labels: List[int] = []

    def add_image(self, image: keras.preprocessing.image):
        self._images.append(image)

    def get_images(self) -> List:
        return self._images

    def get_images_as_ndarray(self) -> np.ndarray:
        ndarray = np.array(self._images)
        return ndarray
    
    def add_target(self, xmin: int, ymin: int, xmax: int, ymax: int, width: int, height: int):
        xmin1 = round(xmin/ width, 2)
        ymin1 = round(ymin/ height, 2)
        xmax1 = round(xmax/ width, 2)
        ymax1 = round(ymax/ height, 2)
        
        self._targets.append((xmin1, ymin1, xmax1, ymax1))

    def get_targets(self) -> List[Tuple[int, int, int, int]]:
        return self._targets

    def get_targets_as_ndarray(self) -> np.ndarray:
        ndarray = np.array(self._targets)
        return ndarray

    def add_label(self, label_index):
        self._labels.append(label_index)

    def get_labels(self) -> List[int]:
        return self._labels
    
    def get_labels_as_ndarray(self) -> np.ndarray:
        ndarray = np.array(self._labels)
        return ndarray