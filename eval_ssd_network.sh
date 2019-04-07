#EVAL_DIR=/home/ubutnu/SSD-Tensorflow/train_dir/eval
python eval_ssd_network.py \
    --eval_dir=/home/ubutnu/SSD-Tensorflow/train_dir/eval \
    --dataset_dir=/home/ubutnu/SSD-Tensorflow/tfrecords \
    --dataset_name=pascalvoc_2007 \
    --dataset_split_name=train \
    --model_name=ssd_300_vgg \
    --checkpoint_path=/home/ubutnu/SSD-Tensorflow/checkpoints/ssd_300_vgg.ckpt \
    --wait_for_checkpoints=False \
    --batch_size=1 \
    --max_num_batches=2000
