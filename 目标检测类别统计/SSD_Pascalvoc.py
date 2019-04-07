# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       陈剑锋
   Date：         2019-03-29 下午1:52
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

import re
import os
import xml.etree.ElementTree as ET


'''
    'QianYiZiBan-Z': (6125, 6126),
    'HouFengDangBoLiJuShengMenBoLi': (5178, 5178),
    'NeiWeiDeng-Z': (3411, 5156),
    'GangQuan': (13699, 14532),
    'HouBaoXianGangPi': (6026, 6026),
    'DaoCheJingZongCheng-Z': (11453, 12584),
    'ZhongWang': (8054, 8054),
    'HouMen-Z': (6413, 6414),
    'XingLiXiangGai': (6173, 6173),
    'HouYeZiBan-Z': (4974, 4975),
    'FaDongJiZhao': (7747, 7748),
    'HouMenBoLiZuo': (7796, 7799),
    'QianMenBoLiZuo': (6627, 6630),
    'QianMen-Z':(6231,6234),
    'QianFenDangBoLi': (6131, 6131),
    'QianDaDeng-Z': (10261, 12144),
    'QianBaoXianGangPi': (7595, 7595),
    'WaiWeiDeng-Z': (6968, 7681),
'''

class1 = 'aeroplane'
class2 = 'bicycle'
class3 = 'bird'
class4 = 'boat'
class5 = 'bottle'
class6 = 'bus'
class7 = 'car'
class8 = 'cat'
class9 = 'chair'
class10 = 'cow'
class11 = 'diningtable'
class12 = 'dog'
class13 = 'horse'
class14 = 'motorbike'
class15 = 'person'
class16 = 'pottedplant'
class17 = 'sheep'
class18 = 'sofa'
class19 = 'train'
class20 = 'tvmonitor'


#
# class1 = 'QianYiZiBan-Z'
# class2 = 'HouFengDangBoLiJuShengMenBoLi'
# class3 = 'NeiWeiDeng-Z'
# class4 = 'GangQuan'
# class5 = 'HouBaoXianGangPi'
# class6 = 'DaoCheJingZongCheng-Z'
# class7 = 'ZhongWang'
# class8 = 'HouMen-Z'
# class9 = 'XingLiXiangGai'
# class10 = 'HouYeZiBan-Z'
# class11 = 'diningtable'
# class12 = 'FaDongJiZhao'
# class13 = 'HouMenBoLiZuo'
# class14 = 'QianMenBoLiZuo'
# class15 = 'QianMen-Z'
# class16 = 'pottedplant'
# class17 = 'QianFenDangBoLi'
# class18 = 'QianDaDeng-Z'
# class19 = 'QianBaoXianGangPi'
# class20 = 'WaiWeiDeng-Z'

annotation_folder = '/home/ubutnu/下载/train'  # 改为自己标签文件夹的路径
list = os.listdir(annotation_folder)


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                L.append(os.path.join(root, file))
    return L


total_number1 = 0
total_number2 = 0
total_number3 = 0
total_number4 = 0
total_number5 = 0
total_number6 = 0
total_number7 = 0
total_number8 = 0
total_number9 = 0
total_number10 = 0
total_number11 = 0
total_number12 = 0
total_number13 = 0
total_number14 = 0
total_number15 = 0
total_number16 = 0
total_number17 = 0
total_number18 = 0
total_number19 = 0
total_number20 = 0
total = 0
total_pic = 0

pic_num1 = 0
pic_num2 = 0
pic_num3 = 0
pic_num4 = 0
pic_num5 = 0
pic_num6 = 0
pic_num7 = 0
pic_num8 = 0
pic_num9 = 0
pic_num10 = 0
pic_num11 = 0
pic_num12 = 0
pic_num13 = 0
pic_num14 = 0
pic_num15 = 0
pic_num16 = 0
pic_num17 = 0
pic_num18 = 0
pic_num19 = 0
pic_num20 = 0

flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
flag7 = 0
flag8 = 0
flag9 = 0
flag10 = 0
flag11 = 0
flag12 = 0
flag13 = 0
flag14 = 0
flag15 = 0
flag16 = 0
flag17 = 0
flag18 = 0
flag19 = 0
flag20 = 0

xml_dirs = file_name(annotation_folder)

for i in range(0, len(xml_dirs)):
    print(xml_dirs[i])
    # path = os.path.join(annotation_folder,list[i])
    # print(path)

    annotation_file = open(xml_dirs[i]).read()

    root = ET.fromstring(annotation_file)
    # tree = ET.parse(annotation_file)
    # root = tree.getroot()

    total_pic = total_pic + 1
    for obj in root.findall('object'):
        label = obj.find('name').text
        if label == class1:
            total_number1 = total_number1 + 1
            flag1 = 1
            total = total + 1
        # print("bounding box number:", total_number1)
        if label == class2:
            total_number2 = total_number2 + 1
            flag2 = 1
            total = total + 1
        if label == class3:
            total_number3 = total_number3 + 1
            flag3 = 1
            total = total + 1
        if label == class4:
            total_number4 = total_number4 + 1
            flag4 = 1
            total = total + 1
        if label == class5:
            total_number5 = total_number5 + 1
            flag5 = 1
            total = total + 1
        if label == class6:
            total_number6 = total_number6 + 1
            flag6 = 1
            total = total + 1
        if label == class7:
            total_number7 = total_number7 + 1
            flag7 = 1
            total = total + 1
        if label == class8:
            total_number8 = total_number8 + 1
            flag8 = 1
            total = total + 1
        if label == class9:
            total_number9 = total_number9 + 1
            flag9 = 1
            total = total + 1
        if label == class10:
            total_number10 = total_number10 + 1
            flag10 = 1
            total = total + 1
        if label == class11:
            total_number11 = total_number11 + 1
            flag11 = 1
            total = total + 1
        if label == class12:
            total_number12 = total_number12 + 1
            flag12 = 1
            total = total + 1
        if label == class13:
            total_number13 = total_number13 + 1
            flag13 = 1
            total = total + 1
        if label == class14:
            total_number14 = total_number14 + 1
            flag14 = 1
            total = total + 1
        if label == class15:
            total_number15 = total_number15 + 1
            flag15 = 1
            total = total + 1
        if label == class16:
            total_number16 = total_number16 + 1
            flag16 = 1
            total = total + 1
        if label == class17:
            total_number17 = total_number17 + 1
            flag17 = 1
            total = total + 1
        if label == class18:
            total_number18 = total_number18 + 1
            flag18 = 1
            total = total + 1
        if label == class19:
            total_number19 = total_number19 + 1
            flag19 = 1
            total = total + 1
        if label == class20:
            total_number20 = total_number20 + 1
            flag20 = 1
            total = total + 1

    if flag1 == 1:
        pic_num1 = pic_num1 + 1
        # print("pic number:", pic_num1)
        flag1 = 0
    if flag2 == 1:
        pic_num2 = pic_num2 + 1
        flag2 = 0
    if flag3 == 1:
        pic_num3 = pic_num3 + 1
        flag3 = 0
    if flag4 == 1:
        pic_num4 = pic_num4 + 1
        flag4 = 0
    if flag5 == 1:
        pic_num5 = pic_num5 + 1
        flag5 = 0
    if flag6 == 1:
        pic_num6 = pic_num6 + 1
        flag6 = 0
    if flag7 == 1:
        pic_num7 = pic_num7 + 1
        flag7 = 0
    if flag8 == 1:
        pic_num8 = pic_num8 + 1
        flag8 = 0
    if flag9 == 1:
        pic_num9 = pic_num9 + 1
        flag9 = 0
    if flag10 == 1:
        pic_num10 = pic_num10 + 1
        flag10 = 0
    if flag11 == 1:
        pic_num11 = pic_num11 + 1
        flag11 = 0
    if flag12 == 1:
        pic_num12 = pic_num12 + 1
        flag12 = 0
    if flag13 == 1:
        pic_num13 = pic_num13 + 1
        flag13 = 0
    if flag14 == 1:
        pic_num14 = pic_num14 + 1
        flag14 = 0
    if flag15 == 1:
        pic_num15 = pic_num15 + 1
        flag15 = 0
    if flag16 == 1:
        pic_num16 = pic_num16 + 1
        flag16 = 0
    if flag17 == 1:
        pic_num17 = pic_num17 + 1
        flag17 = 0
    if flag18 == 1:
        pic_num18 = pic_num18 + 1
        flag18 = 0
    if flag19 == 1:
        pic_num19 = pic_num19 + 1
        flag19 = 0
    if flag20 == 1:
        pic_num20 = pic_num20 + 1
        flag20 = 0

print(class1, pic_num1, total_number1)
print(class2, pic_num2, total_number2)
print(class3, pic_num3, total_number3)
print(class4, pic_num4, total_number4)
print(class5, pic_num5, total_number5)
print(class6, pic_num6, total_number6)
print(class7, pic_num7, total_number7)
print(class8, pic_num8, total_number8)
print(class9, pic_num9, total_number9)
print(class10, pic_num10, total_number10)
print(class11, pic_num11, total_number11)
print(class12, pic_num12, total_number12)
print(class13, pic_num13, total_number13)
print(class14, pic_num14, total_number14)
print(class15, pic_num15, total_number15)
print(class16, pic_num16, total_number16)
print(class17, pic_num17, total_number17)
print(class18, pic_num18, total_number18)
print(class19, pic_num19, total_number19)
print(class20, pic_num20, total_number20)

print("total", total_pic, total)


