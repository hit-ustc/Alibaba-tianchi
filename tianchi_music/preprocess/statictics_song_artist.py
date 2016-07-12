__author__ = 'CC'

import csv
import os
import time

hours = {}

musicians = {}

def countMusicians():
    art = open("../data/source_data/mars_tianchi_songs.csv")
    lines = csv.reader(art)
    for line in lines:
        musicians[line[0]] = line[1]


def staticticsSongsHour():

    countMusicians()

    f = open("../data/source_data/mars_tianchi_user_actions_unix.csv")
    rows = csv.reader(f)

    w = open("../data/source_data/mars_tianchi_user_artist_actions.csv", 'ab')
    write =  csv.writer(w)

    for row in rows:
        date = row[2].split(' ')[1]
        hour = date.split(':')[0]
        words = []

        words.append(row[0])
        words.append(row[1])
        words.append(musicians[row[1]])
        words.append(row[3])
        words.append(row[4])

        write.writerow(words)

staticticsSongsHour()
