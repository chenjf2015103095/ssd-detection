DATASET_DIR=/home/ubutnu/SSD-Tensorflow/VOC2007/
OUTPUT_DIR=/home/ubutnu/SSD-Tensorflow/tfrecords
mkdir -p "${OUTPUT_DIR}"
python tf_convert_data.py \
    --dataset_name=pascalvoc \
    --dataset_dir=${DATASET_DIR} \
    --output_name=voc_2007_train \
    --output_dir=${OUTPUT_DIR}