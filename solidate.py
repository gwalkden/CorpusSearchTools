#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Consolidates instances of the same file in the PPCEME. Script by George Walkden, June 2021.

import sys
import os
import csv
import re

def main(data_path):
    f = open (data_path)
    csv_f = csv.reader(f)
    filelist = []
    for row in csv_f:
        filelist.append(row)
    for row in filelist[1:]:
        if re.match('.+-E.-H',row[0]):
            row[0] = row[0][:-2]
        elif re.match('.+-E.-P1',row[0]):
            row[0] = row[0][:-3]
        elif re.match('.+-E.-P2',row[0]):
            row[0] = row[0][:-3]
        entrycount = 0
        for entry in row:
            if 1 <= entrycount <= len(row) + 1:
                entry = int(entry)
            entrycount += 1
    newlist = []
    newlist.append(filelist[0])
    filenames = []
    filenames.append(filelist[0][0])
    for i in filelist[1:]:
        if i[0] not in filenames:
            newlist.append(i)
            filenames.append(i[0])
        else:
            jcount = 1
            fileindex = filenames.index(i[0])
            for j in i[1:]:
                newlist[fileindex][jcount] = int(newlist[fileindex][jcount]) + int(j)
                jcount += 1
    newfile = str(data_path[:-4]) + '-solidate.csv'
    with open(newfile, 'w') as csvfile:
        brandnew = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for k in newlist:
            brandnew.writerow(k)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\solidate.py <file.csv>'
        sys.exit(0)
    main(sys.argv[1])