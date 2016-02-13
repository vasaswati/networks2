#!/usr/bin/env python

from sys import argv
import queue

script, in_file = argv

# Define a Queue
q = queue.Queue()

# Packet Size (in bytes)
piece_size = 512

ifile = open(in_file,'rb')
data = ifile.read(piece_size)
while data:
    # Push bytes into Queue
    q.put(data)
    data = ifile.read(piece_size)
ifile.close()

# Get bytes from Queue
while not q.empty():
    print(q.get().decode("utf-8"))

