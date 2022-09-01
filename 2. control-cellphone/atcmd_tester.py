#!/usr/bin/env python
from bluetooth import *
import sys
import struct
sock = BluetoothSocket(RFCOMM)
sock.connect(('98:52:B1:60:0B:0F', 2))

while 1:
	data = raw_input(' >> ')
	sock.send( data + "\r\n")
	print sock.recv(1024)

sock.close()

