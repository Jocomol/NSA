#!/usr/bin/python3.5
#Testfile

#import ipaddress

#def getNetmask():
#    ipaddress.ipnetwork


#text = getNetmask()
#print(text)

##wenn response == 0 ist IP erreichbar
#Quelle: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
import os

ip = "8.8.8.8"
response = os.system("ping -c 1 " + ip)
print(str(response))
