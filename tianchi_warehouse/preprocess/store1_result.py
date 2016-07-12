__author__ = 'CC'
import csv



def writeResult(result):
    w = open("../data/20160514result/store1_result.csv", 'ab')
    write = csv.writer(w)
    write.writerow(result)
    w.close()

def store1Result():
    f = open("../data/trainset2/1_two_week.csv")
    rows = csv.reader(f)
    for row in rows:
        data = []
        # arrs = []
        # arrs.append(int(row[1]))
        # arrs.append(int(row[2]))
        # arrs.append(int(row[3]))
        # arrs.append(int(row[4]))
        # arrs.append(int(row[5]))
        # arrs.append(int(row[6]))
        # arrs.append(int(row[7]))
        # arrs.append(int(row[8]))
        # arrs.sort()

        temp = (int(row[1]) - int(row[7]))/6.0
        temp = round(temp, 1)
        data.append(row[0])
        data.append("1")
        data.append(int(row[1]) + temp)
        writeResult(data)


# def store1Result():
#     f = open("../data/trainset/store1_two_week.csv")
#     rows = csv.reader(f)
#     for row in rows:
#
#         data = []
#         value = 3.218 + 0.253 * int(row[2]) + 0.177 * int(row[3]) - 0.013 * int(row[4]) + 0.512 * int(row[5]) - 0.246 * int(row[6])
#         value = round(value, 1)
#         data.append(row[0])
#         data.append("1")
#         data.append(value)
#         writeResult(data)


store1Result()

