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
		print e

def rfcomm_connect(bdaddr, chanel):
	sock = BluetoothSocket( RFCOMM )
	if sock.bind(( "", chanel )) < 0:
		sock.close()	
		exit(-1)
	print 'ko'
	sock.connect(( bdaddr, chanel ))
		

def main( bt_mac ):
	for port in range (1, 5):
		#chanel_detect('9c:3a:af:a7:40:65', port)
    chanel_detect( bt_mac, port )


if __name__ == "__main__":
	try:
		main( sys.argv[1] )
	except Exception as e:
		print e


