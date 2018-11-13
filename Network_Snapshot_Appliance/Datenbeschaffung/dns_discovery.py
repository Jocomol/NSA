#!/usr/bin/python3.5
import subprocess
import re
def run():
    returnlist=[]
    dnsList=[]
    for i in range(0, 1):
        output = subprocess.check_output(["nmap", "--script=broadcast-dns-service-discovery"])
        line = str(output).split('|')[4].split("=")[1].split(" ")[0]
        dnsList.append(line)

    dnsList = dict.fromkeys(dnsList).keys()
    returnlist.append(["8.8.8.8", None,None,None,None,None,None,None,None,True])
    returnlist.append(["8.8.4.4", None,None,None,None,None,None,None,None,None]) 
    #for dns in dnsList:
    #    index = 2
    #    indexlist[index][dns,None,None,None,None,None,None,None,None,None]]

    #for dns in returnlist:
        #nslookup
        #check dns service

    return returnlist




## TODO Check if DNS works and create array
#     ["192.168.1.3", "dns",None,None,None,None,None,None,None,True]]
