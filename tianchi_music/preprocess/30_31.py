__author__ = 'CC'

import csv

def No31():
    f = open("../data/artist_days/artist_everyday2.csv")
    rows = csv.reader(f)

    w = open("../data/artist_days/artist_train.csv", 'ab')
    write = csv.writer(w)

    for row in rows:
        sum = 0
        arr = []
        for i in xrange(len(row)-1):
            if(i == 30 or i == 91 or i == 152):
                arr.append(str((int(row[i]) + int(row[i+1]))/2))
            elif(i == 31 or i == 92 or i == 153):
                continue
            else:
                arr.append(row[i])

        write.writerow(arr)


No31()