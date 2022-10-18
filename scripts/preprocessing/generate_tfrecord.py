"""
Usage:

# Create train data:
python generate_tfrecord.py --label=<LABEL> --csv_input=<PATH_TO_ANNOTATIONS_FOLDER>/train_labels.csv  --output_path=<PATH_TO_ANNOTATIONS_FOLDER>/train.record

# Create test data:
python generate_tfrecord.py --label=<LABEL> --csv_input=<PATH_TO_ANNOTATIONS_FOLDER>/test_labels.csv  --output_path=<PATH_TO_ANNOTATIONS_FOLDER>/test.record
"""
##https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/tensorflow-1.14/training.html

# -*- coding: utf-8 -*
import argparse


parser = argparse.ArgumentParser(description = 'Usage of tensorflow-script')
parser.add_argument("--csv_input", default = "", type = str, help = "path to the CSV input")
parser.add_argument("--output_path", default = "", type = str, help = "path to output TFRecord")
parser.add_argument("--img_path", default = "", type = str, help = "path to images")


args, unknown = parser.parse_known_args()
from helper.image_helper import image_helper




def start():
    try:
        dh = image_helper()
        #vott_csv_headings = dh.get_vott_csv_headings()
        #image_data_and_annotations_from_vott_csv = dh.get_image_data_and_annotations_from_vott_csv(FLAGS.csv_input, ',', FLAGS.img_path)
        image_dataset_for_model_making = dh.get_image_dataset_for_model_making(args.csv_input, ',', args.img_path)
        
        #image_data_and_annotations_from_vott_csv = get_image_data_and_annotations_from_vott_csv(FLAGS
        # .csv_input, vott_csv_headings, ',', FLAGS.img_path)
        a = 0
    except Exception as e: 
        print(e)

    
    #writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    #path = os.path.join(os.getcwd(), FLAGS.img_path)
    #examples = pd.read_csv(FLAGS.csv_input, sep=',')

    #grouped = split(examples, 'filename')
    #for group in grouped:
    #    tf_example = create_tf_example(group, path)
    #    writer.write(tf_example.SerializeToString())

    #writer.close()
    #output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    #print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    start()