__author__ = 'CC'

import csv
import os
import time

def timestamp_datetime(value):
    format = '%Y%m%d %H:%M:%S'

    value = time.localtime(value)

    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)

    dt = time.strftime(format, value)
    return dt


def splitByMusician():

    f = open("../data/source_data/p2_mars_tianchi_user_actions.csv")
    rows = csv.reader(f)
    for row in rows:
        dt = timestamp_datetime(int(row[2]))
        w = open("../data/source_data/p2_mars_tianchi_user_actions_unix.csv", 'ab')
        write = csv.writer(w)
        write.writerow((row[0], row[1], dt, row[3], row[4]))
        w.close()


splitByMusician()