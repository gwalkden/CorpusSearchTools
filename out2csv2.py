#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import re

filecount = 0

def process_file(data_path):
    global filecount
    print 'Getting results…'
    f1 = open(data_path, 'r')
    f = f1.read()
    head, sep, tail = f.partition('SUMMARY:')
    newfile = str(data_path[:-4]) + '.csv'
    f2 = open(newfile, 'w')
    f2.write('File,Hits,Tokens,Total\n')
    files = re.findall('  [\w\.\+\-]+\t+\d+/\d+/\d+',tail)
    for w in files:
	source1 = re.findall('^  ([\w\.\+\-]+)\t',w)
        source = '%s' % source1[0]
	hits1 = re.findall('\t(\d+)/\d+/\d+$',w)
        hits = '%s' % hits1[0]
	tokens1 = re.findall('\t\d+/(\d+)/\d+$',w)
        tokens = '%s' % tokens1[0]
	total1 = re.findall('\t\d+/\d+/(\d+)$',w)
        total = '%s' % total1[0]
	f2.write(source)
	f2.write(',')
	f2.write(hits)
	f2.write(',')
	f2.write(tokens)
	f2.write(',')
	f2.write(total)
	f2.write('\n')
        filecount += 1
	if filecount % 10 == 0:
	    print filecount, 'files added to results.'
    print 'Done. Found', filecount, 'files.'

def main(data_path):
    tagged_list = process_file(data_path)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\out2csv.py <output_file.out>'
        sys.exit(0)
    main(sys.argv[1])
