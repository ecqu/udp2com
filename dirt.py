#! /usr/bin/env python
#Â encoding: utf-8
#
# Res andy


import os, re, serial, socket, struct

DIRT_IP = "127.0.0.1"
DIRT_PORT = 20777

serport = "COM3"
serspeed = 115200

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((DIRT_IP, DIRT_PORT))

ser = serial.Serial(serport, serspeed, timeout=0)

while True:
	data, addr = sock.recvfrom(512)

	outsim_pack = struct.unpack('64f', data[0:256])
	output = "%s %s %s %s %s %s\n" %(outsim_pack[11:17])
	ser.write(output)

	# this is just to empty input buffer so it won't overflow; we don't need any response from duino, right?
	while (ser.inWaiting() > 0):
		ser.read(1)



#	print "%s %s %s %s %s %s" %(outsim_pack[11:17])
#	for id, value in enumerate(outsim_pack):
#		print "%d : %s" % (id, value)

