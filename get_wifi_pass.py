#!/usr/bin/python3

# Author : @reharish
# Credits : ubuntu,@davidbombal and opensource projects
# Description : Script used to collect passwords from Linux system,
#	        which gives wifi names and passwords as a result.


import subprocess
import re

try:
	# collecting info's
	wifiname = subprocess.getoutput("(ls /etc/NetworkManager/system-connections )").split("\n")
	wifinames = subprocess.getoutput("(ls /etc/NetworkManager/system-connections  | cut -d '.' -f 1)")
	wifis = wifinames.split("\n")
	max_len=len(max(wifis))+3
	
	# filler
	print("+---------------+")
	print("+ Network Found +")
	print("+---------------+")
	print()
	print(" ","SSID".ljust(max_len)," PASSWORDS")
	print()
	
	# grepping out passwords i,e psk keys
	for i in range(len(wifis)):
		connection_type = subprocess.getoutput("sudo cat '/etc/NetworkManager/system-connections/"+wifiname[i]+"' | grep type= | cut -d '=' -f 2")
		if connection_type == 'wifi':
			passwd = subprocess.getoutput("sudo cat '/etc/NetworkManager/system-connections/"+wifiname[i]+"' | grep psk= | cut -d '=' -f 2")
			#print(passwd)
			if re.search("Permission denied",passwd):
				print("make sure you run as Root")
				break
			else:
				if passwd == "":
					
					print("+",wifis[i].ljust(max_len),"=> NONE")
				else:
					print("+",wifis[i].ljust(max_len),"=>",passwd)
		
	# filler
	print()

except :
	print ("Something went Wrong !!")
