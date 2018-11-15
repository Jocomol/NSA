#!/usr/bin/python3.5
#Testfile2

#TODO test if it has somethign relevant, else delete

##IP + netmask zu netID
import subprocess, ipaddress
from subprocess import Popen, PIPE


ip = "192.168.210.20"
netmask = "255.255.255.240"

desired_array = [int(numeric_string) for numeric_string in current_array]



ip = ip.split(".")
netmask = netmask.split(".")

ip = [int(num) for num in ip]
mask = [int(num) for num in netmask]

net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])
    
print(str(net))