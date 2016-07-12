__author__ = 'CC'

import csv
from numpy import *
from LogRegression import *
import time

def loadData():
    train_x = []
    train_y = []
    count = 0
    f = open('../data/trainset/no_store_two_week.csv')
    lines = csv.reader(f)
    for line in lines:
        count = count + 1
        if(count <= 80):
            # float(lineArr[0]),float(lineArr[1]), float(lineArr[2]),float(lineArr[3]), float(lineArr[4]),float(lineArr[5]), float(lineArr[6]), float(lineArr[7])
            # train_x.append([1.0,float(lineArr[3]), float(lineArr[4]), float(lineArr[5]), float(lineArr[6])])
            train_x.append([1.0, float(line[2]), float(line[3]), float(line[4]),float(line[5]), float(line[6]), float(line[7]), float(line[8])])
            train_y.append(float(line[1]))

    return mat(train_x), mat(train_y).transpose()

def loadTestData():
    test_x = []
    test_y = []
    count = 0
    f = open('../data/trainset/no_store_two_week.csv')
    lines = csv.reader(f)
    for line in lines:
        count = count + 1
        if(count > 80):
            # test_x.append([1.0,float(lineArr[3]), float(lineArr[4]),float(lineArr[5]), float(lineArr[6])])
            test_x.append([1.0, float(line[2]), float(line[3]), float(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[8])])
            test_y.append(float(line[1]))
    return mat(test_x), mat(test_y).transpose()


## step 1: load data
print "step 1: load data..."
train_x, train_y = loadData()
test_x, test_y = loadTestData()

## step 2: training...
print "step 2: training..."
opts = {'alpha': 0.01, 'maxIter':100, 'optimizeType': 'gradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)

## step 3: testing
print "step 3: testing..."
testLogRegres(optimalWeights, test_x, test_y)
