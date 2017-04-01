#! /usr/bin/env python
#Â encoding: utf-8
#
# Res andy


import os, re, socket

DIRT_IP = "127.0.0.1"
DIRT_PORT = 20777

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((DIRT_IP, DIRT_PORT))

#print "UDP MON RDY @", DIRT_IP, ":", DIRT_PORT


filek = open("dump.txt","r").read().split("\n")


while True:
	data, addr = sock.recvfrom(4096)

	output = ""
	for letter in data:
		output += "%s " % (ord(letter))
	blocs = output.split(" ")
	a = 33
	blob = blocs[(a*4):4+(a*4)]
	print blob

#for line in filek:
#	if len(line) > 20:
#		bloky=line.split(" ")
##		for a in range (0,66):
#		a = 33
#		blob = bloky[(a*4):4+(a*4)]
#		print a, blob
