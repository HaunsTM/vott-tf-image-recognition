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

class image_helper:

    def get_vott_csv_headings(self) -> Dict[str, int]:
        vott_csv_headings = {
            "filename": 0,
            "xmin": 1,
            "ymin": 2,
            "xmax": 3,
            "ymax": 4,
            "label": 5
        }

        return vott_csv_headings

    def get_unique_image_labels_dictionary_from_vott_csv(self, vott_csv_file_data_array: array, vott_csv_file_heading_index_label: int) -> Dict[str, int]:
        unique_image_labels_dictionary_from_vott_csv: Dict[str, int] = {}
        index = 1 #Note: label map id should be diffirent to 0 ! https://github.com/EmnamoR/Face-recognition-Tensorflow-object-detection-api/blob/master/README.md

        for row in vott_csv_file_data_array:
            label_at_current_row = row[vott_csv_file_heading_index_label]
            if label_at_current_row not in unique_image_labels_dictionary_from_vott_csv:
                unique_image_labels_dictionary_from_vott_csv[label_at_current_row] = index
                index += 1
                
        return unique_image_labels_dictionary_from_vott_csv

    def get_unique_image_file_names_list_from_vott_csv(self, vott_csv_file_data_array: array, vott_csv_file_heading_index_file_name: int) -> List[str]:
        list_of_string_type = List[str]
        unique_image_file_names_list: list_of_string_type = []

        for row in vott_csv_file_data_array:
            file_name_at_current_row = row[vott_csv_file_heading_index_file_name]
            if file_name_at_current_row not in unique_image_file_names_list:
                unique_image_file_names_list.append(file_name_at_current_row)
                
        return unique_image_file_names_list

    def get_unique_images_with_data_dictionary(self, unique_image_file_names_list: List[str], train_images_folder) -> Dict[str, image_data]:

        unique_images_with_data_dictionary: Dict[str, image_data] = {}

        for unique_image_file_name in unique_image_file_names_list:
            
            unique_image_file_name_with_path = os.path.join(train_images_folder, unique_image_file_name)
            try:
                
                with tf.gfile.GFile( unique_image_file_name_with_path, 'rb') as fid:
                    encoded_jpg = fid.read()
                    with io.BytesIO( encoded_jpg ) as encoded_jpg_io:
                        #encoded_jpg_io = io.BytesIO(encoded_jpg) as encoded_jpg_io
                        with Image.open( encoded_jpg_io ) as unique_image:
                            unique_image = Image.open( encoded_jpg_io )
                            measurement = image_measurement_data( unique_image.height, unique_image.width )
                            image = image_data( train_images_folder, unique_image_file_name, measurement )

                            unique_images_with_data_dictionary[unique_image_file_name] = image
                            print("Closed: " +unique_image_file_name_with_path)
            except Exception as not_found_err:
                print(not_found_err)
        return unique_images_with_data_dictionary

    def get_image_data_and_annotations_from_vott_csv(self, vott_csv_file: str, column_separator: str, train_images_folder: str) -> List[image_data]:
        vott_csv_headings = self.get_vott_csv_headings()
        vott_csv_file_data_frame = pd.read_csv(vott_csv_file, sep = column_separator)
        vott_csv_file_data_array = vott_csv_file_data_frame.to_numpy()

        unique_image_file_names_list  = self.get_unique_image_file_names_list_from_vott_csv(vott_csv_file_data_array, vott_csv_headings["filename"])
        unique_images_with_data_dictionary = self.get_unique_images_with_data_dictionary(unique_image_file_names_list, train_images_folder)
        unique_image_label_list_from_vott_csv = self.get_unique_image_labels_dictionary_from_vott_csv(vott_csv_file_data_array, vott_csv_headings["label"])
                
        for row in vott_csv_file_data_array:
            file_name_at_current_row = row[vott_csv_headings["filename"]]
            x_min_at_current_row = row[vott_csv_headings["xmin"]]
            y_min_at_current_row = row[vott_csv_headings["ymin"]]
            x_max_at_current_row = row[vott_csv_headings["xmax"]]
            y_max_at_current_row = row[vott_csv_headings["ymax"]]
            label_at_current_row = row[vott_csv_headings["label"]]
            label_index = unique_image_label_list_from_vott_csv[label_at_current_row]
            image_data_label = image_label_data( x_min_at_current_row, y_min_at_current_row, x_max_at_current_row, y_max_at_current_row, label_at_current_row, label_index)
            unique_images_with_data_dictionary[file_name_at_current_row].get_labels().append(image_data_label)

        return list(unique_images_with_data_dictionary.values())

    def get_image_dataset_for_model_making(self, vott_csv_file: str, column_separator: str, images_folder: str) -> image_dataset_for_model_making:
            
        dataset = image_dataset_for_model_making()

        image_data_and_annotations_from_vott_csv = self.get_image_data_and_annotations_from_vott_csv(vott_csv_file, column_separator, images_folder)

        for image_data_and_annotation in image_data_and_annotations_from_vott_csv:
            try:
                image_fullpath = os.path.join(image_data_and_annotation.get_image_folder(), image_data_and_annotation.get_image_file_name())
                target_size = (image_data_and_annotation.get_measurement().get_height(), image_data_and_annotation.get_measurement().get_width())
                with keras.preprocessing.image.load_img(image_fullpath,) as image:
                    image_data_array = keras.preprocessing.image.img_to_array(image)

                    for label in image_data_and_annotation.get_labels():
                        dataset.add_image( image_data_array )
                        dataset.add_target( label.get_xmin(), label.get_ymin(), label.get_xmax(), label.get_ymax(), image_data_and_annotation.get_measurement().get_width(), image_data_and_annotation.get_measurement().get_height() )
                        dataset.add_label( label.get_label_index() )
            except Exception as e: 
                print(e)
        return dataset