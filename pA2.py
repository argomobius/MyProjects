#!usr/bin/python

from pcapy import open_offline
from impacket import ImpactDecoder
from impacket.ImpactPacket import IP, TCP, UDP, ICMP


packetReader = open_offline('sansholiday2')


def Process(header, data):
	decoder = ImpactDecoder.EthDecoder()
	ether = decoder.decode(data)
	ipHeader = ether.child()
	l3 = ipHeader.child()

	try:

		if l3.protocol == 6:
	    	    payload = GetPayload(l3)

	except:
    	   pass	


	print payload



def GetPayload(l3):
	payload_decimal=l3.child().get_bytes().tolist()
	return payload_decimal



	



	    
packetReader.loop(0, Process)

print "Done"
