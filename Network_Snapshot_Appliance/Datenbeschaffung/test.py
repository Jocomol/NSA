#!/usr/bin/python3.5
#Testfile

import subprocess, ipaddress
from subprocess import Popen, PIPE

#TODO test if it has somethign relevant, else delete

def getIP():
    
    ##TODO, Adresse von Host erhalten z.B. 192.168.220.0/255.255.255.0
    
    output = subprocess.check_output(["ifconfig"]).decode()

    array = output.split('\n')

    for item in array:
        if "inet addr" in item:
            if "addr:127" not in item:
                line = item.split(" ")

    for part in line:
        if "addr" in part:
            ip = part.split(":")[1]
        if "Mask" in part:
            mask = part.split(":")[1]
            
    netid = getNetID(ip, mask)
    
    combined = netid + "/" + mask

    return combined

def getNetID():
    
    
    return netid

def pingHosts(ip):
    #Code von: https://topnetworkguide.com/how-to-use-python-to-ping-all-ip-addresses-on-a-network/ vom 13.11.2018
    #Wurde modifiziert
    ips = []
    network = ipaddress.ip_network(ip)
    for i in network.hosts():
        i = str(i)
        toping = Popen(['ping','-c', '1', i], stdout=PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            #reachable
            #2D-Array
            #[["192.168.1.1", "client",None,None,None,None,None,None,None,None],["192.168.1.2", "client",None,None,None,None,None,None,None,None]]
            try:
                #Domainname herausfinden
                domainname = subprocess.check_output(["nslookup", i]) #1
                domainname = str(domainname).split(".\\n")[0].split("=")[1]
            except subprocess.CalledProcessError:
                domainname = ""
            ip = [str(i),domainname,None,None,None,None,None,None,None,None]
            ips.append(ip)
    return ips


#print(pingHosts("192.168.210.5/255.255.255.0"))

print(getIP())