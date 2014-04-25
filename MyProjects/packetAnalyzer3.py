#!usr/bin/python

from pcapy import open_offline
from impacket import ImpactDecoder
from impacket.ImpactPacket import IP, TCP, UDP, ICMP






def Process(header, data):
	decoder = ImpactDecoder.EthDecoder()
	packet = decoder.decode(data)
	l2 = packet.child()
	l3=l2.child()

	if l3.protocol == 6:
	
		if l3.get_th_dport()==80 or l3.get_th_sport()==80:
	     	    payload = GetPayload(l3)
	     	    return payload




def GetPayload(l3):
	payload_decimal=l3.child().get_bytes().tolist()
	ascii = []

	for decByte in payload_decimal:
		if decByte in range(9,14) or decByte in range(32,127):
			hexByte = str(hex(decByte)).lstrip("0x")
			if len(hexByte)==1:
				hexByte="0" + hexByte
			asciiByte=hexByte.decode('hex')
			ascii.append(asciiByte)
	
	payload_ascii=''.join(ascii)

	return payload_ascii

	
	




packetReader = open_offline('sansholiday2')
packetReader.loop(0,Process)


print "Done"






	
