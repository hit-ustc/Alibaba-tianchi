__author__ = 'CC'

import csv

musicians = {}
dates = {}

days = {}

def SongsByMusician():

    f = open("../data/source_data/p2_mars_tianchi_songs.csv")
    rows = csv.reader(f)
    for row in rows:
        musicians[row[1]] = 0


def init():

    for i in xrange(9):
        dates["2015090" + str(i+1)] = 0
        dates["2015100" + str(i+1)] = 0

    for i in xrange(21):
        dates["201509" + str(i+10)] = 0
        dates["201510" + str(i+10)] = 0


def result():

    SongsByMusician()
    init()
    dates_sort = sorted(dates.iteritems(), key=lambda e:e[0], reverse=False)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0

    f = open("../data/p2_EachHour60Days/hour60days.csv")
    rows = csv.reader(f)
    for row in rows:
        sum = 0
        for i in xrange(len(row)-1):
            sum = sum + int(row[i+1])
        sum = sum / 60

        for date in dates_sort:
            days[(row[0], date[0])] = days[(row[0], date[0])] + sum

        # i = 1
        # for date in dates_sort:
        #     days[(row[0], date[0])] = days[(row[0], date[0])] + int(row[i])
        #     i = i + 1


    for musician in musicians:
        for date in dates_sort:
            w = open("../data/result/20160613/mars_tianchi_artist_plays_predict.csv", 'ab')
            write = csv.writer(w)
            write.writerow((str(musician), str(days[(musician, date[0])]), str(date[0])))


result()