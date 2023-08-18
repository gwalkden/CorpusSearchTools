#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import re

tokencount = 0

def process_file(data_path):
    global tokencount
    print 'Numbering tokens…'
    f1 = open(data_path, 'r')
    f = f1.read()
    lines = re.findall('(.+)',f)
    for w in lines:
	if re.match('^(.+)\.[0-9]+\.(.+)', w):
        	tokencount += 1
		part1a = re.findall('^(.+)\.[0-9]+\.',w)
		part1 = '%s' % part1a[0]
		part2a = re.findall('\.[0-9]+\.(.+)$',w)
		part2 = '%s' % part2a[0]
		f2.write(part1)
		f2.write('.')
		f2.write(str(tokencount))
		f2.write('.')
		f2.write(part2)
		f2.write('\n')
		if tokencount % 100 == 0:
			print tokencount, 'tokens numbered.'
	else:
		f2.write(w)
	f2.write('\n')
    print 'Done. Numbered', tokencount, 'tokens.'

def main(data_path):
    tagged_list = process_file(data_path)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\tokenno.py <data_file>'
        sys.exit(0)
    f2 = open('tokenno', 'w')
    main(sys.argv[1])
