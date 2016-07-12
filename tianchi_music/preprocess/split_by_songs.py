__author__ = 'CC'


import csv
import os

data_dictionary = {}


def writeBySong(song, words):
    file_name = song+".csv"
    os.chdir('../data/songs')
    if not data_dictionary.has_key(song):
        data_dictionary[song] = True
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

def splitBySongs():
    os.mkdir('../data/songs')
    f = open("../data/source_data/mars_tianchi_user_actions.csv")
    rows = csv.reader(f)
    for row in rows:
        song = row[1]
        words = row[0:-1]
        writeBySong(song, words)

splitBySongs()