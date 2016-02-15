#!/usr/bin/env python

from sys import argv
import queue
import threading
from threading import Thread

script, in_file = argv

# Packet Size (in bytes)
packet_size = 512

# Define worker threads
num_worker_threads = 3

# Define a Queue
q = queue.Queue()

# Define worker
def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()
        return

for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

# Open and read file
ifile = open(in_file,'rb')
data = ifile.read(packet_size)
while data:
    # Push bytes into Queue
    q.put(data)
    data = ifile.read(packet_size)
ifile.close()

# Get bytes from Queue
while not q.empty():
    print(q.get().decode("utf-8"))

# block until all tasks are done
q.join()

