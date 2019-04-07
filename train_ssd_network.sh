DATASET_DIR=/home/ubutnu/SSD-Tensorflow/tfrecords
TRAIN_DIR=/home/ubutnu/SSD-Tensorflow/train_dir
CHECKPOINT_PATH=/home/ubutnu/SSD-Tensorflow/checkpoints/ssd_300_vgg.ckpt
#mkdir -p $"{TRAIN_DIR}"
python train_ssd_network.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=pascalvoc_2007 \
    --dataset_split_name=train \
    --model_name=ssd_300_vgg \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --save_summaries_secs=60 \
    --save_interval_secs=600 \
    --weight_decay=0.0005 \
    --optimizer=adam \
    --learning_rate=0.001 \
    --batch_size=32



