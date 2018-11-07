#!/usr/bin/env python

import sys
import urllib
import chardet2
import os

orig = sys.argv[1]
rawdata = urllib.urlopen(orig).read()
enc = chardet.detect(rawdata)['encoding']
if enc.startswith('UTF-16'):
    enc = 'UTF-16'

if enc != 'utf-8' and enc != 'ascii':
    print("{0}: {1}".format(enc, orig))
    utf8 = orig + '.utf8'
    os.system("iconv -f {0} -t UTF-8 '{1}' > '{2}'".format(enc, orig, utf8))
    os.system("mv '{0}' '{1}'".format(utf8, orig))
