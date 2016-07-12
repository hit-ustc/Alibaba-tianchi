__author__ = 'CC'

import csv
import os
import time

hours = {}

musicians = {}

def countMusicians():
    art = open("../data/source_data/p2_mars_tianchi_songs.csv")
    lines = csv.reader(art)
    for line in lines:
        musicians[line[0]] = line[1]


def writeByHours(hour, words):
    file_name = hour+".csv"
    os.chdir('../data/p2_hours_arts')
    if not hours.has_key(hour):
        hours[hour] = True
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


def staticticsSongsHour():

    countMusicians()
    os.mkdir('../data/p2_hours_arts')
    f = open("../data/source_data/p2_mars_tianchi_user_actions_unix.csv")
    rows = csv.reader(f)
    for row in rows:
        date = row[2].split(' ')[1]
        hour = date.split(':')[0]
        words = []

        words.append(row[0])
        words.append(row[1])
        words.append(musicians[row[1]])
        words.append(row[3])
        words.append(row[4])
        writeByHours(hour, words)

staticticsSongsHour()