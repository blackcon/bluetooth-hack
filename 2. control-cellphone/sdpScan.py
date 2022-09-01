#!/usr/bin/python
from bluetooth import *
import sys

def sdpBrowse(addr):
	services = find_service(address = addr)
	for service in services:
		name = service['name']
		proto = service['protocol']
		port = str(service['port'])
		print '[+] Found ' + str(name) + ' on ' + str(proto) + ':' + port
sdpBrowse(sys.argv[1])
