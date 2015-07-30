#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import numpy
from features import mfcc, fbank

def extract_features(datasets):
    def get_features(sample):
        rate, sig = sample
        mfcc_feats = mfcc(sig, rate)

        def diff(feats):
            feats_diff = numpy.zeros(feats.shape)
            for i in range(2, feats.shape[0]-2):
                feats_diff[i,:] = 2*feats[i-2,:] - feats[i-2,:] + feats[i+1,:] + 2*feats[i+2,:]
            return feats_diff

        mfcc_diff_feats = diff(mfcc_feats)
        mfcc_diff2_feats = diff(mfcc_diff_feats)

        _, energy_feat = fbank(sig, rate)
        log_energy_feat = numpy.log(energy_feat).reshape(energy_feat.shape[0],1)

        return numpy.concatenate((mfcc_feats, mfcc_diff_feats, mfcc_diff2_feats, log_energy_feat), axis=1)[2:-2]

    new_datasets = []
    for dataset in datasets:
        new_datasets.append(([get_features(sample) for sample in dataset[0]], dataset[1]))

    return tuple(new_datasets)

if __name__ == '__main__':
    from loader import load_data
    datasets, n_classes = load_data()

    new_datasets = extract_features(datasets)
    for data in new_datasets[0][0]:
        print data.shape

