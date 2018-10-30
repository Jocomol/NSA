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
    
    cmd = "['bash', 'bashscripts/test.sh]"
    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    data = result.stdout.decode('utf-8')
    
    return data


def dhcpDiscovery():
    
    
    return data


def dnsDiscovery():
    
    
    return data


def createOutput(allIPs, dhcpData, dnsData):
    
    
    return output