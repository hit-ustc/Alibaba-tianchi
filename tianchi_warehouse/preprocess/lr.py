__author__ = 'CC'

import csv
import numpy as np
import sklearn.linear_model as lm

# def multivar_linear_regression():
#     clf = lm.LinearRegression()
#     x = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
#     #x = np.array([[1], [2], [3], [4], [5]])
#     y = np.array([4.83, 4.27, 3.59, 3.53, 3.46])
#     print 'x:', len(x)
#     print 'y:', len(y)
#     clf.fit(x, y)
#     for xx, yy in zip(x, y):
#         print yy, clf.predict(xx)
#     print 'x=[6, 6, 6], y =', clf.predict([6, 6, 6])
#     return

def predict():

    trainX = []
    trainY = []

    testX = []
    testY = []

    y = []
    f = open("../data/trainset/no_store_two_week.csv")
    rows = csv.reader(f)
    for row in rows:
        xx = []

        y.append(row[1])
        xx.append(row[2])
        xx.append(row[3])
        xx.append(row[4])
        xx.append(row[5])
        xx.append(row[6])
        xx.append(row[7])
        xx.append(row[8])
        trainX.append(xx)

    trainY = np.array(y)
    clt = lm.LinearRegression()
    clt1 = lm.LogisticRegression()
    clt.fit(trainX, trainY)
    clt1.fit(trainX. trainY)

    for row in rows:
        xx = []

        xx.append(row[2])
        xx.append(row[3])
        xx.append(row[4])
        xx.append(row[5])
        xx.append(row[6])
        xx.append(row[7])
        xx.append(row[8])
        testX.append(xx)

        value = clt.predict(testX)
        print testX,value


predict()





