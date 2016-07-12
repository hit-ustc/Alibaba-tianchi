__author__ = 'CC'


import csv
import os

data_dictionary = {}


def writeByItems(item, words):
    file_name = item+".csv"
    os.chdir('../data/items')
    if not data_dictionary.has_key(item):
        data_dictionary[item] = True
        f = open(file_name, 'ab')
        write = csv.writer(f)
        write.writerow(words)
        f.close()
    else :
        f = open(file_name, 'ab')
        write = csv.writer(f)
        write.writerow(words)
        f.close()

    os.chdir('../../preprocess')

def splitByItems():
    os.mkdir("../data/items")
    f = open("../data/item_feature1.csv")
    rows = csv.reader(f)
    for row in rows:

        item = row[1]
        # words = row[0:-1]

        words = []
        for rec in row:
            words.append(rec)

        writeByItems(item, words)
