__author__ = 'CC'

import csv
import os
import time

dates = {}
musicians = {}

days = {}


def init():
    # f = open("../data/source_data/p2_mars_tianchi_user_actions_unix.csv")
    # rows = csv.reader(f)
    # for row in rows:
    #     if(row[4] > "20150630" and row[4] < "20150831" and row[4] != "20150731"):
    #     # if(row[4] > "20150430" and row[4] < "20150831"):
    #         dates[row[4]] = 0
    for i in xrange(9):
        dates["2015070" + str(i+1)] = 0
        dates["2015080" + str(i+1)] = 0

    for i in xrange(21):
        dates["201507" + str(i+10)] = 0
        dates["201508" + str(i+10)] = 0

def SongsByMusician():

    f = open("../data/source_data/p2_mars_tianchi_songs.csv")
    rows = csv.reader(f)
    for row in rows:
        musicians[row[1]] = 0

def writeFile(i, dates_sort):
    if(i < 10):
        f = open("../data/p2_hours_arts/0"+ str(i) +".csv")
    else:
        f = open("../data/p2_hours_arts/"+ str(i) +".csv")
    rows = csv.reader(f)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0

    for row in rows:

        if(row[4] > "20150630" and row[4] < "20150831" and row[4] != "20150731"):
        # if(row[4] > "20150430" and row[4] < "20150831"):
            if(row[3] == "1"):
                days[(row[2], row[4])] = days[(row[2], row[4])] + 1

    for musician in musicians:
        # if(i < 10):
        #     w = open("../data/EachHour60Days/0"+ str(i) +"hour60days.csv", 'ab')
        # else:
        #     w = open("../data/EachHour60Days/"+ str(i) +"hour60days.csv", 'ab')
        w = open("../data/p2_EachHour60Days/hour60days.csv", 'ab')
        write = csv.writer(w)
        word = []
        word.append(musician)
        for date in dates_sort:
            word.append(days[(musician, date[0])])
        write.writerow(word)
        w.close()

def staticticsArtistsHour():

    init()
    SongsByMusician()

    dates_sort = sorted(dates.iteritems(), key=lambda e:e[0], reverse=False)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0

    for i in xrange(0, 24):
        writeFile(i, dates_sort)



staticticsArtistsHour()