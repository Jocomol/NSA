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
    
    
return data



def dhcpDiscovery():
    
    cmd = "['bash', 'bashscripts/test.sh]"
    data = execCommand(cmd)
    
    return data
    


def dnsDiscovery():
    
    
    return data


def createOutput(allIPs, dhcpData, dnsData):
    
    
    return output


def getNetmask():
    
    
    return netmask


#Needs cmd like cmd = "['bash', 'bashscripts/test.sh]"
def execCommand(cmd):
    
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')
    
    return retVal