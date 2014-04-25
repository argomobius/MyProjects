import socket
import sys
import time

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, msg:
	print "Failed to create socket. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
	sys.exit();

print 'Socket Created'

host = '' #All available interfaces
port = 8908 #arbitrary port

try: 
	s.bind((host, port))

except socket.error, msg:
	print "Failed to bind socket. Error code: " + str(msg[0]) + " Error message: " + str(msg[1])
	sys.exit();

print 'Socket bind complete'	

s.listen(10)

print 'Socket now listening'


def clientthread(conn):

	conn.send('Welcome to the echo server. Type something and hit enter \n')

	data = ''

	while True:

		data += conn.recv(1096)
		
		conn.send(data)	

	conn.close()


while 1:	

	conn, addr = s.accept()

	print 'Connected with ' + addr[0] + ':' + str(addr[1])  

	clientthread(conn)

s.close()






