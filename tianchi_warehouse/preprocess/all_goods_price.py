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
            data7[row[1]] = 0
            data8[row[1]] = 0

def StatisticsPrice():

    StatisticsItem()

    f = open("../data/source_data/item_feature1.csv")
    # f = open("../data/test.csv")
    rows = csv.reader(f)
    for row in rows:
        if row[0] == "20151227" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data1[row[1]] = str(round(temp, 1)) + "-" +  row[15] + "-" + row[17]
            continue

        if row[0] == "20151226" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data2[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151225" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data3[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151224" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data4[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151223" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data5[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151222" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data6[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151221" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data7[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

        if row[0] == "20151220" and int(row[17]) != 0:
            temp = float(row[15])/int(row[17])
            data8[row[1]] = str(round(temp, 1)) + "-" + row[15] + "-" + row[17]
            continue

    for key in data1:
        w = open("../data/trainset/all_item_price.csv", 'ab')
        write = csv.writer(w)
        write.writerow((key, data1[key], data2[key], data3[key], data4[key], data5[key], data6[key], data7[key], data8[key]))
        w.close()


StatisticsPrice()
