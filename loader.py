#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import numpy
import scipy.io.wavfile as wav

def load_data():
    train_set = ([], [])
    test_set = ([], [])
    valid_set = ([], [])

    label = 0
    for sex in ('male','female'):
        dir = os.path.join('.', 'audio_data', sex+'_audio')
        for subdir in os.listdir(dir):
            if subdir[0] == sex[0].upper():
                id = subdir.split('_')[-1]
                label = label+1
                for i in range(1,3):
                    filename = os.path.join(dir, subdir, "{0}_{1}.wav".format(id,i))
                    train_set[0].append(wav.read(filename))
                    train_set[1].append(label)
                for i in range(3,5):
                    filename = os.path.join(dir, subdir, "{0}_{1}.wav".format(id,i))
                    test_set[0].append(wav.read(filename))
                    test_set[1].append(label)
                filename = os.path.join(dir, subdir, "{0}_5.wav".format(id))
                valid_set[0].append(wav.read(filename))
                valid_set[1].append(label)

    return train_set, test_set, valid_set

if __name__ == '__main__':
    train_data, test_data, valid_data = load_data()
    print len(train_data) + len(test_data) + len(valid_data)