__author__ = 'CC'

import csv
import math

musicians = {}
dates = {}

days = {}

artist_start = {}
cal_month_ratio = {}
def SongsByMusician():
    f = open("../data/source_data/mars_tianchi_songs.csv")
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

    # dates["20150731"] = 0

def linefit(x , y):
    N = float(len(x))
    sx,sy,sxx,syy,sxy=0,0,0,0,0
    for i in range(0,int(N)):
        sx  += x[i]
        sy  += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    a = (sy*sx/N -sxy)/( sx*sx/N -sxx)
    b = (sy - a*sx)/N
    r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b,r


def cal_month():
    f = open("../data/artist_days/artist_train.csv")
    rows = csv.reader(f)

    for row in rows:

        arr_days = []
        aver_days = []
        aver_ratio = []
        for i in xrange(180):
           arr_days.append(int(row[i+1]))

        aver_month = []
        aver_ratio_month = []
        for month_y in xrange(len(arr_days) - 29):
            sum = 0.0
            for i in xrange(30):
                sum = sum + arr_days[month_y+i]
            sum = sum / 30
            sum = round(sum, 1)
            aver_month.append(sum)

        for month_z in xrange(len(aver_month)):
            temp = arr_days[month_z+14]/aver_month[month_z]
            temp = round(temp, 1)
            aver_ratio_month.append(temp)

        eve_ratio = {}
        count = {}
        old = {}
        new = {}
        for i in xrange(30):
            eve_ratio[i] = 0
            count[i] = 0
        for k in xrange(len(aver_ratio_month)):
            eve_ratio[(k%30+14)%30] = eve_ratio[(k%30+14)%30] + aver_ratio_month[k]
            count[(k%30+14)%30] = count[(k%30+14)%30] + 1

        for i in xrange(30):
            old[i] = eve_ratio[i]/count[i]
            old[i] = round(old[i], 1)

        old_sum = 0.0
        for i in xrange(30):
            old_sum = old_sum + old[i]
        diff = (old_sum - 30.0)/30.0
        diff = round(diff, 1)

        for i in xrange(30):
            new[i] = old[i] - diff

    return new

def result():
    SongsByMusician()
    init()

    dates_sort = sorted(dates.iteritems(), key=lambda e:e[0], reverse=False)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0.0

    # for musician in musicians:
    #     for date in dates_sort:
    #         artist_start[(musician, date[0])] = 0.0
    f = open("../data/artist_days/artist_everyday.csv")
    rows = csv.reader(f)

    w = open("../data/result/20160601/mars_tianchi_artist_plays_predict.csv", 'ab')
    write = csv.writer(w)

    for row in rows:

        re = open("../data/result/20160517/mars_tianchi_artist_plays_predict.csv")
        lines = csv.reader(re)
        for line in lines:
            artist_start[(str(line[0]), str(line[2]))] = int(line[1])

        # for i in xrange(30):
        #     value = int(row[i+1]) + int(row[i+31+1]) + int(row[i+61+1]) + int(row[i+92+1])
        #     value = value/4.0
        #     value = round(value, 1)
        #     if(i < 9):
        #         artist_start[(row[0], "2015070" + str(i+1))] = value
        #         artist_start[(row[0], "2015080" + str(i+1))] = value
        #     else:
        #         artist_start[(row[0], "201507" + str(i+1))] = value
        #         artist_start[(row[0], "201508" + str(i+1))] = value
        #
        # artist_start[(row[0], "20150731")] = (int(row[31]) + int(row[92]))/2
        # print artist_start


        # X = []
        # Y = []
        # for i in xrange(30):
        #     X.append(i+1)
        #     Y.append(int(row[i+93]))
        # fit_a, fit_b, fit_r = linefit(X, Y)
        # fit_aa = round(fit_a, 1)
        # fit_bb = round(fit_b, 1)
        # fit_rr = round(fit_r, 1)
        # print "--------fit_rr---------"
        # print row[0]
        # print fit_aa, fit_bb, fit_rr
        #
        # for i in xrange(31):
        #     value = fit_aa * (i+31) + fit_bb
        #     if(i < 9):
        #         artist_start[(row[0], "2015070" + str(i+1))] = value
        #     else:
        #         artist_start[(row[0], "201507" + str(i+1))] = value
        #
        # for i in xrange(30):
        #     value = fit_aa * (i+31) + fit_bb
        #     if(i < 9):
        #         artist_start[(row[0], "2015080" + str(i+1))] = value
        #     else:
        #         artist_start[(row[0], "201508" + str(i+1))] = value


        arr_days = []
        aver_days = []
        aver_ratio = []
        for i in xrange(183):
           arr_days.append(int(row[i+1]))

        for y in xrange(len(arr_days)-6):
            temp = (arr_days[y] + arr_days[y+1] + arr_days[y+2] + arr_days[y+3] + arr_days[y+4] + arr_days[y+5] + arr_days[y+6])/7.0
            temp = round(temp, 1)
            aver_days.append(temp)

        for z in xrange(len(aver_days)):
            temp = arr_days[z+3]/aver_days[z]
            temp = round(temp, 1)
            aver_ratio.append(temp)

        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        for k in xrange(len(aver_ratio)):
            if k % 7 == 0:
                a3.append(aver_ratio[k])
            if k % 7 == 1:
                a4.append(aver_ratio[k])
            if k % 7 == 2:
                a5.append(aver_ratio[k])
            if k % 7 == 3:
                a6.append(aver_ratio[k])
            if k % 7 == 4:
                a7.append(aver_ratio[k])
            if k % 7 == 5:
                a1.append(aver_ratio[k])
            if k % 7 == 6:
                a2.append(aver_ratio[k])

        aver_a1 = sum(a1)/len(a1)
        aver_a1 = round(aver_a1, 1)

        aver_a2 = sum(a2)/len(a2)
        aver_a2 = round(aver_a2, 1)

        aver_a3 = sum(a3)/len(a3)
        aver_a3 = round(aver_a3, 1)

        aver_a4 = sum(a4)/len(a4)
        aver_a4 = round(aver_a4, 1)

        aver_a5 = sum(a5)/len(a5)
        aver_a5 = round(aver_a5, 1)

        aver_a6 = sum(a6)/len(a6)
        aver_a6 = round(aver_a6, 1)

        aver_a7 = sum(a7)/len(a7)
        aver_a7 = round(aver_a7, 1)
        # print aver_a1, aver_a2, aver_a3, aver_a4, aver_a5, aver_a6, aver_a7

        diff = ((aver_a1 + aver_a2 + aver_a3 + aver_a4 + aver_a5 + aver_a6 + aver_a7) - 7.0)/7.0
        seven = round(diff, 1)

        new_aver_a1 = aver_a1 - diff
        new_aver_a2 = aver_a2 - diff
        new_aver_a3 = aver_a3 - diff
        new_aver_a4 = aver_a4 - diff
        new_aver_a5 = aver_a5 - diff
        new_aver_a6 = aver_a6 - diff
        new_aver_a7 = aver_a7 - diff
        # print new_aver_a1, new_aver_a2, new_aver_a3, new_aver_a4, new_aver_a5, new_aver_a6
        # print "*******************************"

        cal_month_ratio = cal_month()

        for i in xrange(30):
            if(i < 9):
                artist_start[(row[0], "2015090" + str(i+1))] = artist_start[(row[0], "2015090" + str(i+1))] * cal_month_ratio[i]
                artist_start[(row[0], "2015100" + str(i+1))] = artist_start[(row[0], "2015100" + str(i+1))] * cal_month_ratio[i]
            else:
                artist_start[(row[0], "201509" + str(i+1))] = artist_start[(row[0], "201509" + str(i+1))] * cal_month_ratio[i]
                artist_start[(row[0], "201510" + str(i+1))] = artist_start[(row[0], "201510" + str(i+1))] * cal_month_ratio[i]

        # artist_start[(row[0], "20150731")] = artist_start[(row[0], "20150731")] * cal_month_ratio[29]

        date_day = 0
        for date in dates_sort:
            if(date_day%7 == 1):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a3)

            elif(date_day%7 == 2):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a4)

            elif(date_day%7 == 3):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a5)

            elif(date_day%7 == 4):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a6)

            elif(date_day%7 == 5):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a7)

            elif(date_day%7 == 6):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a1)

            elif(date_day%7 == 0):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a2)
            date_day = date_day + 1

            write.writerow((str(row[0]), str(days[(row[0], date[0])]), str(date[0])))


result()


