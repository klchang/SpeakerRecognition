#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy
from sklearn import preprocessing

def reform(datasets):
    new_datasets = []
    scaler = None
    for dataset in datasets:
        new_dataset_x = []
        new_dataset_y = []
        for x, y in zip(dataset[0],dataset[1]):
            for i in range(0, len(x)/10*10, 10):
                new_dataset_x.append(x[i:i+10,:].flatten())
                new_dataset_y.append(y)
        new_dataset_x = numpy.asarray(new_dataset_x)
        new_dataset_y = numpy.asarray(new_dataset_y)

        new_datasets.append((new_dataset_x, new_dataset_y))

    return tuple(new_datasets)

if __name__ == '__main__':
    from loader import load_data
    from feature_extractor import extract_features

    datasets = extract_features(load_data()[0])

    new_datasets = reform(datasets)

    print new_datasets[0][0][0].shape