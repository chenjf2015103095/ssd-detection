# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       陈剑锋
   Date：         2019-03-29 下午3:07
   Description :  Dream it possible!
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import collections
import tensorflow as tf
#读取train.txt和test.txt文将SSD目标检测中的train和test数据集分开
#便于更好的统计训练和测试的图片数目以及没个类别的bounding box数目
import shutil
classes_list=[]
count=0
with open('/home/ubutnu/SSD-Tensorflow/VOC2007/ImageSets/Main/train.txt','r') as f :
    line = f.read().strip()
    print(line)
    classes_list = re.split(r"[\n]", line)  #将txt文件的每行数据转换为一个大列表
    print(classes_list)
    for content in classes_list:
        count+=1
    print(count)

xml_dir='/home/ubutnu/SSD-Tensorflow/VOC2007/Annotations'
train='/home/ubutnu/下载/train'
for root, dirs, files in os.walk(xml_dir):
    for file in files:
        name,ext=file.split('.xml')
        if name in classes_list:
            name=name+str('.xml')
            path=os.path.join(root,name)
            print(path)
            shutil.copy(path,train)

