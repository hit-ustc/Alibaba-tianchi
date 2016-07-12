__author__ = 'CC'


import csv
import os

data_dictionary = {}


def writeByMusician(musician, words):
    file_name = musician+".csv"
    os.chdir('../data/p2_musician')
    if not data_dictionary.has_key(musician):
        data_dictionary[musician] = True
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

def splitByMusician():
    os.mkdir('../data/p2_musician')
    f = open("../data/source_data/p2_mars_tianchi_songs.csv")
    rows = csv.reader(f)
    for row in rows:
        musician = row[1]
        words = row[0:-1]
        writeByMusician(musician, words)

splitByMusician()