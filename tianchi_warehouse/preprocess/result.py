__author__ = 'CC'
import csv



def writeResult(result):
    w = open("../data/20160514result/result.csv", 'ab')
    write = csv.writer(w)
    write.writerow(result)
    w.close()

def myResult():
    f = open("../data/trainset2/all_two_week.csv")
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
        data.append("all")
        data.append(int(row[1]) + temp)
        writeResult(data)

# def myResult():
#     f = open("../data/trainset/no_store_two_week.csv")
#     rows = csv.reader(f)
#     for row in rows:
#
#         data = []
#         value = 11.557 + 0.227 * int(row[2]) + 0.344 * int(row[3]) - 0.012 * int(row[4]) + 0.522 * int(row[5]) - 0.290 * int(row[6])
#         value = round(value, 1)
#         data.append(row[0])
#         data.append("all")
#         data.append(value)
#         writeResult(data)

myResult()


