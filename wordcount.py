#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Approximate word count of Penn parsed .psd files.
# Created by George Walkden in August 2023.

import sys
import os
import re

def process_file(data_path):
    global tokencount
    print 'Counting words...'
    f1 = open(data_path, 'r')
    f = f1.read()
    terminals = re.findall('([^\s\(\)]+ [^\s\(\)]+)',f)
    # print(terminals)
    codecomments = re.findall('(CODE [^\s\(\)]+)',f)
    ids = re.findall('(ID [^\s\(\)]+)',f)
    nulls = re.findall('([^\s\(\)]+ \*[^\s\(\)]+)',f) + re.findall('([^\s\(\)]+ 0)',f)
    punct = re.findall('([^\w\s] [^\s\(\)]+)',f)
    lemmwordsplus = re.findall('([\w\$\+\^]+ [^\s\(\)\-\*]+\-[^\s\(\)\-\*]+)',f)
    lemmwords = [i for i in lemmwordsplus if i not in ids]
    # print(lemmwords)
    words = len(terminals) - len(codecomments) - len(ids) - len(nulls) - len(punct)
    notwords = codecomments + ids + nulls + punct
    wordlist = [i for i in terminals if i not in notwords]
    # overlap = [i for i in wordlist if i not in lemmwords]
    print 'Done. Found', len(terminals), 'terminals, of which', len(codecomments), 'were CODE,', len(ids), 'were token IDs,', len(punct), 'were punctuation, and', len(nulls), 'were null, leaving', words, 'words. We also found', len(lemmwords), 'lemmatized words.'
    # print len(overlap), 'terminals not in any other category:', terminals1

def main(data_path):
    tagged_list = process_file(data_path)

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print 'usage:\wordcount.py <data_file>'
        sys.exit(0)
    main(sys.argv[1])
