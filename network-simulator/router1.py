#!/usr/bin/env python

from sys import argv
import queue
import time
import threading
from threading import Thread
from struct import *
import binascii

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
        self._totalLength = ""
        self._identification = ""
        self._flags = ""
        self._fragmentOffset = ""
        self._timeToLive = ""
        self._protocol = ""
        self._headerChecksum = ""
        self._sourceAddress = ""
        self._destinationAddress = ""
        self._options = ""

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

    @totalLength.deleter
    def totalLength(self):
        del self._totalLength

    @property
    def identification(self):
        return self._identification

    @identification.setter
    def identification(self, value):
        self._identification = value

    @identification.deleter
    def identification(self):
        del self._identification

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, value):
        self._flags = value

    @flags.deleter
    def flags(self):
        del self._flags

    @property
    def fragmentOffset(self):
        return self._fragmentOffset

    @fragmentOffset.setter
    def fragmentOffset(self, value):
        self._fragmentOffset = value

    @fragmentOffset.deleter
    def fragmentOffset(self):
        del self._fragmentOffset

    @property
    def timeToLive(self):
        return self._timeToLive

    @timeToLive.setter
    def timeToLive(self, value):
        self._timeToLive = value

    @timeToLive.deleter
    def timeToLive(self):
        del self._timeToLive

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value

    @protocol.deleter
    def protocol(self):
        del self._protocol

    @property
    def headerChecksum(self):
        return self._headerChecksum

    @headerChecksum.setter
    def headerChecksum(self, value):
        self._headerChecksum = value

    @headerChecksum.deleter
    def headerChecksum(self):
        del self._headerChecksum

    @property
    def sourceAddress(self):
        return self._sourceAddress

    @sourceAddress.setter
    def sourceAddress(self, value):
        self._sourceAddress = value

    @sourceAddress.deleter
    def sourceAddress(self):
        del self._sourceAddress

    @property
    def destinationAddress(self):
        return self._destinationAddress

    @destinationAddress.setter
    def destinationAddress(self, value):
        self._destinationAddress = value

    @destinationAddress.deleter
    def destinationAddress(self):
        del self._destinationAddress

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    @options.deleter
    def options(self):
        del self._options 

def ByteToHex( byteStr ):
    return [ "%02X " % ord( x ) for x in byteStr ]

def HexToBin( hexArr ):
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8

    return ''.join( [  bin( int( x , scale ) )[2:].zfill( num_of_bits ) for x in hexArr ] ).strip()

def BinToInt( binStr  ):
    return int( binStr, 2 )

def DecToHex( decimal ):
    return hex( decimal )

def HexToDec( hexadecimal ):
    return int( hexadecimal, 16 )

def IPFormatter( decimal ):
    h1 = DecToHex( decimal )
    h2 = h1.split('x')[1]
    octet1 = HexToDec( '0x' + h2[0:2] )
    octet2 = HexToDec( '0x' + h2[2:4] )
    octet3 = HexToDec( '0x' + h2[4:6] )
    octet4 = HexToDec( '0x' + h2[6:8] )
    ip = str(octet1) + '.' + str(octet2) + '.' + str(octet3) + '.' + str(octet4)
    return ip

# Packet Parser - Parser that parses string data and gives datagram object
# Takes Input as protocol, Outputs packet object
class PacketParser(Packet):
    def __init__( self ):
        "Initialization method for Packet Parser"
        
    def parsePacket( self , data ):
        "Parse a Packet"
        
        packet = Packet()

        sliced_str = str(data[:60])[2:-1]

        #print(sliced_str)

        pkt_str = HexToBin(ByteToHex(sliced_str))
    
        #print(pkt_str[16:32])
        

        ## IP4 Datagram structure
        packet.version = BinToInt( pkt_str[0:4] )
        packet.ihl = BinToInt( pkt_str[4:8] )
        packet.dscp = BinToInt( pkt_str[8:14] )
        packet.ecn = BinToInt( pkt_str[14:16] )
        packet.totalLength = BinToInt( pkt_str[16:32]  )
        packet.identification = BinToInt( pkt_str[32:48] )
        packet.flags = BinToInt( pkt_str[64:66] )
        packet.fragmentOffset = BinToInt( pkt_str[66:80] )
        packet.timeToLive = BinToInt( pkt_str[80:88] )
        packet.protocol = BinToInt( pkt_str[88:104] )
        packet.headerChecksum = BinToInt( pkt_str[104:130] )
        packet.sourceAddress = BinToInt( pkt_str[130:162] )
        packet.destinationAddress = BinToInt( pkt_str[162:194] )
        packet.options = BinToInt( pkt_str[194:226] )

        print('Version : ' + str(packet.version) + ' source address : ' + IPFormatter(packet.sourceAddress) + ' destination address : ' + IPFormatter(packet.destinationAddress))

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
