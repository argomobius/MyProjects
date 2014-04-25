import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, msg:
	print "Failed to create socket. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
	sys.exit();

print 'Socket Created'

host = 'localhost'
port = 8895

try:
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	#could not resolve
	print 'Hostname could not be resolved.'	
	sys.exit()

print 'IP address of ' + host + ' is ' + remote_ip	

#connect to IP, port

try:

	s.connect((remote_ip, port))

except socket.error, msg:
	print "Failed to create socket. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
	sys.exit();

print 'Socket Connected to ' + host + ' on IP ' + remote_ip	

#Message to be sent

message = "GET / HTTP/1.1\r\n\r\n"

#send the whole message


try: 
	s.sendall(message)

except socket.error:
	print 'Send failed'
	sys.exit();

print 'Message sent'	

try: 
	reply = s.recv(4096)

except socket.error:
	print 'Receive failed'
	sys.exit();	

print reply	




