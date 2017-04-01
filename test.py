import socket

DIRT_IP = "127.0.0.1"
DIRT_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((DIRT_IP, DIRT_PORT))

print "UDP MON RDY @", DIRT_IP, ":", DIRT_PORT

while True:
	data, addr = sock.recvfrom(512)
	print data
