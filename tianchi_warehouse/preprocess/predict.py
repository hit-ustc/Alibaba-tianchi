__author__ = 'CC'

import csv

less = {}
more = {}
less1 = {}
more1 = {}
less2 = {}
more2 = {}
less3 = {}
more3 = {}
less4 = {}
more4 = {}
less5 = {}
more5 = {}

def splitConfig():

    f = open("../data/source_data/config1.csv")
    rows = csv.reader(f)
    for row in rows:
        if row[1] == "all":
            if not less.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less[row[0]] = small
                more[row[0]] = large

        if row[1] == "1":
            if not less1.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less1[row[0]] = small
                more1[row[0]] = large

        if row[1] == "2":
            if not less2.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less2[row[0]] = small
                more2[row[0]] = large

        if row[1] == "3":
            if not less3.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less3[row[0]] = small
                more3[row[0]] = large

        if row[1] == "4":
            if not less4.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less4[row[0]] = small
                more4[row[0]] = large

        if row[1] == "5":
            if not less5.has_key(row[0]):
                small = row[2].split('_')[0]
                large = row[2].split('_')[1]
                less5[row[0]] = small
                more5[row[0]] = large

def predict():
    splitConfig()