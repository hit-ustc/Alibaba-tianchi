__author__ = 'CC'

import csv
import os
import time

dates = {}
musicians = {}

days = {}


def init():
    # f = open("../data/source_data/mars_tianchi_user_actions_unix.csv")
    # rows = csv.reader(f)
    # for row in rows:
    #     # if(row[4] > "20150630" and row[4] < "20150831" and row[4] != "20150731"):
    #     if(row[4] > "20150228" and row[4] < "20150901"):
    #         dates[row[4]] = 0
    for i in xrange(9):
        dates["2015030" + str(i+1)] = 0
        dates["2015040" + str(i+1)] = 0
        dates["2015050" + str(i+1)] = 0
        dates["2015060" + str(i+1)] = 0
        dates["2015070" + str(i+1)] = 0
        dates["2015080" + str(i+1)] = 0

    for y in xrange(21):
        dates["201503" + str(y+10)] = 0
        dates["201504" + str(y+10)] = 0
        dates["201505" + str(y+10)] = 0
        dates["201506" + str(y+10)] = 0
        dates["201507" + str(y+10)] = 0
        dates["201508" + str(y+10)] = 0

    dates["20150331"] = 0
    dates["20150531"] = 0
    dates["20150731"] = 0
    dates["20150831"] = 0


def SongsByMusician():

    f = open("../data/source_data/mars_tianchi_songs.csv")
    rows = csv.reader(f)
    for row in rows:
        musicians[row[1]] = 0


def staticticsArtistsDay():

    init()
    SongsByMusician()
    print "************************************"

    dates_sort = sorted(dates.iteritems(), key=lambda e:e[0], reverse=False)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0

    f = open("../data/source_data/mars_tianchi_user_artist_actions.csv")
    rows = csv.reader(f)

    for row in rows:

        # if(row[4] > "20150630" and row[4] < "20150831" and row[4] != "20150731"):
        if(row[4] > "20150228" and row[4] < "20150901"):
            if(row[3] == "1"):
                days[(str(row[2]), str(row[4]))] = days[(str(row[2]), str(row[4]))] + 1

    w = open("../data/artist_days/artist_everyday2.csv", 'ab')
    write = csv.writer(w)


    for musician in musicians:
        # if(i < 10):
        #     w = open("../data/EachHour60Days/0"+ str(i) +"hour60days.csv", 'ab')
        # else:
        #     w = open("../data/EachHour60Days/"+ str(i) +"hour60days.csv", 'ab')

        word = []
        word.append(musician)
        for date in dates_sort:
            word.append(days[(musician, date[0])])
        write.writerow(word)



staticticsArtistsDay()