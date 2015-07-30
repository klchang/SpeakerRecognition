#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import numpy
import scipy.io.wavfile as wav

def load_data():
    train_set = ([], [])
    test_set = ([], [])

    label = 0
    for sex in ('male',):
        dir = os.path.join('.', 'audio_data', sex+'_audio')
        for subdir in os.listdir(dir):
            if subdir[0] == sex[0].upper():
                id = subdir.split('_')[-1]
                for i in (1,2,3,4):
                    filename = os.path.join(dir, subdir, "{0}_{1}.wav".format(id,i))
                    train_set[0].append(wav.read(filename))
                    train_set[1].append(label)
                for i in (5,):
                    filename = os.path.join(dir, subdir, "{0}_{1}.wav".format(id,i))
                    test_set[0].append(wav.read(filename))
                    test_set[1].append(label)
                label = label+1

    return (train_set, test_set), label

if __name__ == '__main__':
    (train_data, test_data), n_classes = load_data()
    print len(train_data[0]) + len(test_data[0])