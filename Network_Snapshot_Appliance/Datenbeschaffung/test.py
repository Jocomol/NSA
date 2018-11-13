#!/usr/bin/python3.5
#Testfile

#import ipaddress

#def getNetmask():
#    ipaddress.ipnetwork


#text = getNetmask()
#print(text)

##wenn response == 0 ist IP erreichbar
#Quelle: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
#import os

#ip = "8.8.8.8"
#response = os.system("ping -c 1 " + ip)
#print(str(response))



#parsing

#import subprocess


#output = subprocess.check_output(["ifconfig"]).decode()

#array = output.split('\n')

#for item in array:
    #if "inet addr" in item:
        #if "addr:127" not in item:
            #line = item.split(" ")

#for part in line:
    #if "addr" in part:
        #ip = part.split(":")[1]
    #if "Mask" in part:
        #mask = part.split(":")[1]

    
#combined = ip + "/" + mask

#return combined


import scriptlib

print(scriptlib.ipDiscovery())