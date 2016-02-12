#!/usr/bin/env python

from sys import argv

script, in_file = argv

# Packet Size (in bytes)
piece_size = 512

ifile = open(in_file,'rb')
data = ifile.read(piece_size)
while data:
    print data
    data = ifile.read(piece_size)
ifile.close()
