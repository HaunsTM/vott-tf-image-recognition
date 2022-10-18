from helper.image_data import image_data
from helper.image_label_data import image_label_data
from helper.image_measurement_data import image_measurement_data
from helper.image_dataset_for_model_making import image_dataset_for_model_making

from typing import List, Dict

import os
import io
import pandas as pd

from array import array
from xml.dom import NotFoundErr

from PIL import Image
import tensorflow.compat.v1 as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential

class model_maker:


    
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width