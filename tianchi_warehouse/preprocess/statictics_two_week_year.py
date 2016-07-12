__author__ = 'CC'
import csv

data_dictionary = {}

data1 = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}
data6 = {}


def StatisticsItem():
    f = open("../data/source_data/item_feature1.csv")
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




def StatisticsTwoWeekYear():

    StatisticsItem()

    f = open("../data/source_data/item_feature1.csv")
    # f = open("../data/test.csv")
    rows = csv.reader(f)
    for row in rows:
        if row[0] > "20141227" and row[0] < "20150111":
            data1[row[1]] = data1[row[1]] + int(row[17])
            continue

        if row[0] > "20141213" and row[0] < "20141228":
            data2[row[1]] = data2[row[1]] + int(row[17])
            continue

        if row[0] > "20141129" and row[0] < "20141214":     # 12.12
            data3[row[1]] = data3[row[1]] + int(row[17])
            continue

        if row[0] > "20141115" and row[0] < "20141130":
            data4[row[1]] = data4[row[1]] + int(row[17])
            continue

        if row[0] > "20141101" and row[0] < "20141116":     #11.11
            data5[row[1]] = data5[row[1]] + int(row[17])
            continue

        if row[0] > "20141018" and row[0] < "20141102":     # 11.01
            data6[row[1]] = data6[row[1]] + int(row[17])
            continue

    for key in data1:
        w = open("../data/no_store_year/two_week.csv", 'ab')
        write = csv.writer(w)
        write.writerow((key, data1[key], data2[key], data3[key], data4[key], data5[key], data6[key]))
        w.close()


StatisticsTwoWeekYear()

