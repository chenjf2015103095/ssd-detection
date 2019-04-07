# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       陈剑锋
   Date：         2019-03-27 下午5:00
   Description :  Dream it possible!
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import collections
import tensorflow as tf

train='python /home/ubutnu/SSD-Tensorflow/train_ssd_network.py '\
    '--train_dir=/home/ubutnu/SSD-Tensorflow/train_dir '\
    '--dataset_dir=/home/ubutnu/SSD-Tensorflow/tfrecords '\
    '--dataset_name=pascalvoc_2007 '\
    '--dataset_split_name=train '\
    '--model_name=ssd_300_vgg '\
    '--checkpoint_path=/home/ubutnu/SSD-Tensorflow/checkpoints/ssd_300_vgg.ckpt '\
    '--save_summaries_secs=60 '\
    '--save_interval_secs=600 '\
    '--weight_decay=0.0005 '\
    '--optimizer=adam '\
    '--learning_rate=0.001 '\
    '--batch_size=32'
os.system(train)
