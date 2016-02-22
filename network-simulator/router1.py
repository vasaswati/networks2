#!/usr/bin/env python

from sys import argv
import queue
import time
import threading
from threading import Thread
from struct import *

script, in_file1, in_file2, in_file3 = argv

# Packet Size (in bytes)
packet_size = 500

# Define a Queue
queueList = [ queue.Queue() for i in range(3) ]

# Define delay between each packet
delay1 = 1
delay2 = 3
delay3 = 2

# Multithreading - Data Links receive data in parallel
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
        data_link( self, self.name, self.delay, self.in_file, self.queue )
        
        # Free lock to release next thread
        #threadLock.release()
        return

# Define a function for the thread (Fetch from data link)
def data_link( self, threadName, delay, in_file, queue):
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

class Packet(object):
    def __init__(self):
        "Init for Packet Object"
        self._version = ""
        self._ihl = ""
        self._dscp__ = ""
        self._ecn__ = ""
        self._totalLength = 0

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @version.deleter
    def version(self):
        del self._version

    @property
    def ihl(self):
        return self._ihl

    @ihl.setter
    def ihl(self, value):
        self._ihl = value

    @ihl.deleter
    def ihl(self):
        del self._ihl

    @property
    def dscp(self):
        return self._dscp

    @dscp.setter
    def dscp(self, value):
        self._dscp = value

    @dscp.deleter
    def dscp(self):
        del self._dscp

    @property
    def ecn(self):
        return self._ecn

    @ecn.setter
    def ecn(self, value):
        self._ecn = value

    @ecn.deleter
    def ecn(self):
        del self._ecn

    @property
    def totalLength(self):
        return self._totalLength

    @totalLength.setter
    def totalLength(self, value):
        self._totalLength = value

    @ihl.deleter
    def totalLength(self):
        del self._totalLength


def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (a[0] , a[1] , a[2], a[3], a[4] , a[5])
  return b


# Packet Parser - Parser that parses string data and gives datagram object
# Takes Input as protocol, Outputs packet object
class PacketParser(Packet):
    def __init__( self ):
        "Initialization method for Packet Parser"
        
    def parsePacket( self , data ):
        "Parse a Packet"

        #print("Packet Data in string : " + binascii.unhexlify(data[1:60]))
        #print(data[96:127].decode("utf-8"))

        #parse ethernet header
        eth_length = 14
     
        eth_header = data[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        
        print('Destination MAC : ' + eth_addr(data[0:6]) + ' Source MAC : ' + eth_addr(data[6:12]))

# Receiver Module - Takes data from data links
class ReceiverModule(PacketParser):
    def __init__(self):
        "Init method for the class"
        self.PacketParser = PacketParser
        self.threadLock = threading.Lock()
        self.threads = []

    def start(self):
        "Start module to start reading files"
        # Create new threads
        thread1 = RouterThread(1, "Data Link 1", in_file1, delay1, queueList[0])
        thread2 = RouterThread(2, "Data Link 2", in_file2, delay2, queueList[1])
        thread3 = RouterThread(3, "Data Link 3", in_file3, delay3, queueList[2])

        # Start new Threads
        thread1.start()
        thread2.start()
        thread3.start()

        # Add threads to thread list
        self.threads.append(thread1)
        self.threads.append(thread2)
        self.threads.append(thread3)

        # Wait for all threads to complete
        for t in self.threads:
            t.join()
        print("Exiting Main Thread")

        packetParser = self.PacketParser()

        # Print output - Get bytes from Queue
        print("Printing items from each queue -");
        for queue in queueList:
            while not queue.empty():
                print("***********************************************************************************************************")
                packetParser.parsePacket( queue.get() )

# Router
class Router(ReceiverModule):
    def __init__( self ):
        "Init method"
        return
    
    def start( self ):
        "Start method"
        self.receiverModule = ReceiverModule()
        self.receiverModule.start();
        return

router = Router()
router.start()
