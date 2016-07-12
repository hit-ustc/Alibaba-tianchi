__author__ = 'CC'

import csv
import math

def cal_month():
    f = open("../data/artist_days/artist_train.csv")
    rows = csv.reader(f)

    for row in rows:

        arr_days = []
        aver_days = []
        aver_ratio = []
        for i in xrange(120):
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

cal_month()
