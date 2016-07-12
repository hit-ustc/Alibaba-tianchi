__author__ = 'CC'

import csv
import os

data_dictionary = {}


def writeByStoreItems(item, words):
    file_name = item+".csv"
    os.chdir('../data/stores2')
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

def splitByStores():
    os.mkdir('../data/stores2')
    f = open("../data/source_data/item_store_feature2.csv")
    rows = csv.reader(f)
    for row in rows:

        item = row[2]
        # words = row[0:-1]
        words = []
        for rec in row:
            words.append(rec)

        writeByStoreItems(item, words)


splitByStores()