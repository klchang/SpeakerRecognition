#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD

from keras.utils import np_utils

def MLP(n_classes):
    model = Sequential()
    model.add(Dense(10*40, 350, init='glorot_uniform', activation='tanh'))
    model.add(Dense(350, n_classes, init='glorot_uniform', activation='softmax'))

    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mse', optimizer=sgd)

    return model

def CNNwithPooling(n_classes):
    model = Sequential()
    model.add(Convolution2D(4, 1, 10, 5, border_mode='valid'))
    model.add(Activation('tanh'))
    model.add(MaxPooling2D(poolsize=(1, 2)))
    model.add(Flatten())
    model.add(Dense(4*1*18, 50, init='glorot_normal'))
    model.add(Activation('tanh'))
    model.add(Dense(50, n_classes, init='glorot_normal'))
    model.add(Activation('softmax'))

    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mse', optimizer=sgd)

    return model


def CNNwithoutPooling(n_classes):
    model = Sequential()
    model.add(Convolution2D(4, 1, 10, 5, border_mode='valid'))
    model.add(Activation('tanh'))
    model.add(Flatten())
    model.add(Dense(4*1*36, 100, init='glorot_normal'))
    model.add(Activation('tanh'))
    model.add(Dense(100, n_classes, init='glorot_normal'))
    model.add(Activation('softmax'))

    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='mse', optimizer=sgd)

    return model

from loader import load_data
from feature_extractor import extract_features
from utils import reform

if __name__ == '__main__':
    print "... loading data"
    datasets, n_classes = load_data()

    print "... extracting features"
    datasets = extract_features(datasets)

    print "... reforming data"
    train_set, test_set = reform(datasets)

    print "*********************"
    print "    Model 1 - MLP"
    print "*********************"

    print "... building MLP"
    mlp = MLP(n_classes)

    print "... training MLP"
    mlp.fit(train_set[0], np_utils.to_categorical(train_set[1], n_classes), batch_size=10, nb_epoch=5, show_accuracy=True)

    print "... evaluating MLP"
    loss, accuracy = mlp.evaluate(test_set[0], np_utils.to_categorical(test_set[1], n_classes), batch_size=50, show_accuracy=True)

    print "MLP loss: {0}".format(loss)
    print "MLP accuracy: {0}".format(accuracy)

    print "***********************************"
    print "    Model 2 - CNN with Pooling"
    print "***********************************"

    print "... building CNN"
    cnn = CNNwithPooling(n_classes)

    print "... reshaping data"
    train_set_x = train_set[0].reshape((train_set[1].shape[0], 1, 10, 40))
    test_set_x = test_set[0].reshape((test_set[1].shape[0], 1, 10, 40))

    print "... traing CNN"
    cnn.fit(train_set_x, np_utils.to_categorical(train_set[1], n_classes), batch_size=10, nb_epoch=5, show_accuracy=True)

    print "... evaluating CNN"
    loss, accuracy = cnn.evaluate(test_set_x, np_utils.to_categorical(test_set[1], n_classes), batch_size=50, show_accuracy=True)

    print "CNN loss: {0}".format(loss)
    print "CNN accuracy: {0}".format(accuracy)

    print "***********************************"
    print "    Model 3 - CNN without Pooling"
    print "***********************************"

    print "... building CNN"
    cnn = CNNwithoutPooling(n_classes)

    print "... reshaping data"
    train_set_x = train_set[0].reshape((train_set[1].shape[0], 1, 10, 40))
    test_set_x = test_set[0].reshape((test_set[1].shape[0], 1, 10, 40))

    print "... traing CNN"
    cnn.fit(train_set_x, np_utils.to_categorical(train_set[1], n_classes), batch_size=10, nb_epoch=5, show_accuracy=True)

    print "... evaluating CNN"
    loss, accuracy = cnn.evaluate(test_set_x, np_utils.to_categorical(test_set[1], n_classes), batch_size=50, show_accuracy=True)

    print "CNN loss: {0}".format(loss)
    print "CNN accuracy: {0}".format(accuracy)