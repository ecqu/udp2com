#! /usr/bin/env python
#Â encoding: utf-8
#
# Res andy


import os, re, socket, struct

DIRT_IP = "127.0.0.1"
DIRT_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((DIRT_IP, DIRT_PORT))

#print "UDP MON RDY @", DIRT_IP, ":", DIRT_PORT


#filek = open("dump.txt","r").read().split("\n")


while True:
	data, addr = sock.recvfrom(512)

	outsim_pack = struct.unpack('64f', data[0:256])
	print "%s %s %s %s %s %s" %(otsim_pack[11-17])
#	for id, value in enumerate(outsim_pack):
#		print "%d : %s" % (id, value)

