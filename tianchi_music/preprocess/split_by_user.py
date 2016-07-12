__author__ = 'CC'


import csv
import os

data_dictionary = {}


def writeByUser(user, words):
    file_name = user+".csv"
    os.chdir('../data/users')
    if not data_dictionary.has_key(user):
        data_dictionary[user] = True
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

def splitByUsers():
    os.mkdir('../data/users')
    f = open("../data/source_data/mars_tianchi_user_actions.csv")
    rows = csv.reader(f)
    for row in rows:
        user = row[0]
        words = row[0:-1]
        writeByUser(user, words)

splitByUsers()