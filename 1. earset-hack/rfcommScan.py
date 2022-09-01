#!/usr/bin/python
from bluetooth import *
import sys

def chanel_detect(addr, port):
	sock = BluetoothSocket(RFCOMM)
	try:
		sock.connect((addr, port))
		print ' [+] RFCOMM Port ' + str(port) + ' open'
		sock.close
	except Exception, e:
		print ' [-] RFCOMM Port ' + str(port) + ' closed'
		print '   ',e

def main():
	if len(sys.argv) < 2:
		print 'usage : %s [bdaddr]' %sys.argv[0]
		exit(-1)
	for port in range (1, 5):
		chanel_detect(sys.argv[1], port)


if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print e


