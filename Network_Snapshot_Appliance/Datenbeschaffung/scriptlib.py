#!/usr/bin/python3.5
#Scriptlibrary

import subprocess, dhcp_discovery, dns_discovery, ipaddress
from subprocess import Popen, PIPE


def runScripts():
    #TODO, run all scripts
    
    #allIPs = ipDiscovery()
    #dhcpData = dhcpDiscovery()
    #dnsData = dnsDiscovery()
    
    #output = createOutput(allIPs, dhcpData, dnsData)
    
    return output


def ipDiscovery():
    
    ip = getIP()
    data = pingHosts(ip)
    
    return data


def dhcpDiscovery():
    ##geht noch nicht
    #cmd = "['bash', 'bashscripts/dhcp_discovery.sh]"
    #data = execScpt(cmd)
    
    data = dns_discovery.run()
    
    return data
    

def dnsDiscovery():
    ##funktioniert
    #cmd = "['bash', 'bashscripts/dns_discovery.sh]"
    #data = execScpt(cmd)
    
    data = dhcp_discovery.run()
    
    return data


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
    
    combined = ip + "/" + mask

    return combined



def createOutput(allIPs, dhcpData, dnsData):
     
     ##TODO, create Arrays gemäss Vorlage Joel
     
    
    return output


def pingHosts(ip):
    #Code von: https://topnetworkguide.com/how-to-use-python-to-ping-all-ip-addresses-on-a-network/
    network = ipaddress.ip_network(ip)
    for i in network.hosts():
        i = str(i)
        toping = Popen(['ping','-c', '1', i], stdout=PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            #reachable
            print("reachable")
        else:
            #unreachable
            print("unreachable")


#Needs cmd like cmd = "['bash', 'bashscripts/test.sh]"
def execScpt(cmd):
    
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')
    
    return retVal