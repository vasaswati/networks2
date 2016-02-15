#!/usr/bin/env python

from sys import argv
import queue
import time
import threading
from threading import Thread

script, in_file1, in_file2, in_file3 = argv

# Packet Size (in bytes)
packet_size = 50

# Define a Queue
queueList = [ queue.Queue() for i in range(3) ]

# Define delay between each packet
delay1 = 1
delay2 = 3
delay3 = 2

class RouterThread (Thread):
    def __init__(self, threadID, name, in_file, delay, queue):
        "Init code for Thread class"
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.in_file = in_file
        self.delay = delay
        self.queue = queue
        return

    def run(self):
        "Run code for Thread class"        
        print("Starting " + self.name)
       
        # Get lock to synchronize threads
        #threadLock.acquire()

        # Fetch data from data link
        data_link( self.name, self.delay, self.in_file, self.queue )
        
        # Free lock to release next thread
        #threadLock.release()
        return

# Define a function for the thread (Fetch from data link)
def data_link( threadName, delay, in_file, queue):
    "Fetch data from a particular data link"

    # Open and read file
    ifile = open(in_file,'rb')

    # Read data (get packets)
    data = ifile.read(packet_size)
    
    while data:

        # Push bytes into Queue
        queue.put(data)

        # Sleep the thread
        time.sleep(delay)

        # Read data (get packets)
        data = ifile.read(packet_size)

        print("Fetching from %s" % threadName)

    # Close file
    ifile.close()
    return

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = RouterThread(1, "Data Link 1", in_file1, delay1, queueList[0])
thread2 = RouterThread(2, "Data Link 2", in_file2, delay2, queueList[1])
thread3 = RouterThread(3, "Data Link 3", in_file3, delay3, queueList[2])

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")

# Print output - Get bytes from Queue
print("Printing items from each queue -");
for queue in queueList:
    while not queue.empty():
        print(queue.get().decode("utf-8"))
