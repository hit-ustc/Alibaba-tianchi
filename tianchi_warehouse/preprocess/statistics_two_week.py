__author__ = 'CC'
import csv

data_dictionary = {}

data1 = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}
data6 = {}
data7 = {}
data8 = {}


def StatisticsItem():
    f = open("../data/source_data/item_feature2.csv")
    rows = csv.reader(f)
    for row in rows:
        if not data_dictionary.has_key(row[1]):
            data_dictionary[row[1]] = True
            data1[row[1]] = 0
            data2[row[1]] = 0
            data3[row[1]] = 0
            data4[row[1]] = 0
            data5[row[1]] = 0
            data6[row[1]] = 0
            data7[row[1]] = 0
            data8[row[1]] = 0

def StatisticsTwoWeek():

    StatisticsItem()

    f = open("../data/source_data/item_feature2.csv")
    # f = open("../data/test.csv")
    rows = csv.reader(f)
    for row in rows:
        if row[0] > "20151213" and row[0] < "20151228":
            data1[row[1]] = data1[row[1]] + int(row[17])
            continue

        if row[0] > "20151129" and row[0] < "20151214":     # 12.12
            data2[row[1]] = data2[row[1]] + int(row[17])
            continue

        if row[0] > "20151115" and row[0] < "20151130":
            data3[row[1]] = data3[row[1]] + int(row[17])
            continue

        if row[0] > "20151101" and row[0] < "20151116":     # 11.11
            data4[row[1]] = data4[row[1]] + int(row[17])
            continue

        if row[0] > "20151018" and row[0] < "20151102":     # 11.01
            data5[row[1]] = data5[row[1]] + int(row[17])
            continue

        if row[0] > "20151004" and row[0] < "20151019":
            data6[row[1]] = data6[row[1]] + int(row[17])
            continue

        if row[0] > "20150920" and row[0] < "20151005":     # 10.01
            data7[row[1]] = data7[row[1]] + int(row[17])
            continue

        if row[0] > "20150906" and row[0] < "20150921":
            data8[row[1]] = data8[row[1]] + int(row[17])
            continue

    for key in data1:
        w = open("../data/trainset2/all_two_week.csv", 'ab')
        write = csv.writer(w)
        write.writerow((key, data1[key], data2[key], data3[key], data4[key], data5[key], data6[key], data7[key], data8[key]))
        w.close()


StatisticsTwoWeek()
