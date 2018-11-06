#!/usr/bin/python3.5
#Scriptlibrary

import subprocess


def runScripts():
    #TODO, run all scripts
    
    allIPs = ipDiscovery()
    #dhcpData = dhcpDiscovery()
    #dnsData = dnsDiscovery()
    
    output = createOutput(allIPs, dhcpData, dnsData)
    
    return output



def ipDiscovery():
    
    netmask = getNetmask()
    ##TODO, Sven: Scan network
    
    return data



def dhcpDiscovery():
    
    cmd = "['bash', 'bashscripts/dhcp_discovery.sh]"
    data = execScpt(cmd)
    
    return data
    


def dnsDiscovery():
    
    
    return data


def getNetmask():
    
    
    return netmask

def createOutput(allIPs, dhcpData, dnsData):
     
    
    return output

#Needs cmd like cmd = "['bash', 'bashscripts/test.sh]"
def execScpt(cmd):
    
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')
    
    return retVal