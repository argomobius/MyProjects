import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error, msg:
	print "Failed to create socket. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
	sys.exit();

print 'Socket Created'

host = 'www.cnn.com'
port = 80

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