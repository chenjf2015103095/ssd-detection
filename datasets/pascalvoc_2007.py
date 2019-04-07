# Copyright 2015 Paul Balanca. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Provides data for the Pascal VOC Dataset (images + annotations).
"""
import tensorflow as tf
from datasets import pascalvoc_common

slim = tf.contrib.slim

FILE_PATTERN = 'voc_2007_%s_*.tfrecord'
ITEMS_TO_DESCRIPTIONS = {
    'image': 'A color image of varying height and width.',
    'shape': 'Shape of the image',
    'object/bbox': 'A list of bounding boxes, one per each object.',
    'object/label': 'A list of labels, one per each object.',
}
# (Images, Objects) statistics on every class.
TRAIN_STATISTICS = {
    'none': (0, 0),
    'aeroplane': (183, 280),
    'bicycle': (230, 349),
    'bird': (257, 513),
    'boat': (155, 360),
    'bottle': (221, 611),
    'bus': (168, 232),
    'car': (668, 1349),
    'cat': (294, 328),
    'chair': (489, 1239),
    'cow': (112, 294),
    'diningtable': (231, 277),
    'dog': (395, 488),
    'horse': (251, 365),
    'motorbike': (210, 341),
    'person': (1906, 4736),
    'pottedplant': (228, 525),
    'sheep': (86, 274),
    'sofa': (323, 359),
    'train': (229, 267),
    'tvmonitor': (233, 327),
    'total': (4456, 13541),
}

TEST_STATISTICS = {
    'none': (0, 0),
    'aeroplane': (22, 31),
    'bicycle': (20, 40),
    'bird': (32, 63),
    'boat': (21, 33),
    'bottle': (19, 46),
    'bus': (15, 22),
    'car': (87, 192),
    'cat': (38, 42),
    'chair': (56, 135),
    'cow': (15, 35),
    'diningtable': (16, 22),
    'dog': (38, 42),
    'horse': (28,30),
    'motorbike': (23, 28),
    'person': (191, 464),
    'pottedplant': (26, 67),
    'sheep': (12, 37),
    'sofa': (30, 37),
    'train': (30, 35),
    'tvmonitor': (22, 34),
    'total': (496, 1435),
}



SPLITS_TO_SIZES = {
    'train': 4456,
    'test': 496,
}
SPLITS_TO_STATISTICS = {
    'train': TRAIN_STATISTICS,
    'test': TEST_STATISTICS,
}
NUM_CLASSES = 20


def get_split(split_name, dataset_dir, file_pattern=None, reader=None):
    """Gets a dataset tuple with instructions for reading ImageNet.

    Args:
      split_name: A train/test split name.
      dataset_dir: The base directory of the dataset sources.
      file_pattern: The file pattern to use when matching the dataset sources.
        It is assumed that the pattern contains a '%s' string so that the split
        name can be inserted.
      reader: The TensorFlow reader type.

    Returns:
      A `Dataset` namedtuple.

    Raises:
        ValueError: if `split_name` is not a valid train/test split.
    """
    if not file_pattern:
        file_pattern = FILE_PATTERN
    return pascalvoc_common.get_split(split_name, dataset_dir,
                                      file_pattern, reader,
                                      SPLITS_TO_SIZES,
                                      ITEMS_TO_DESCRIPTIONS,
                                      NUM_CLASSES)
