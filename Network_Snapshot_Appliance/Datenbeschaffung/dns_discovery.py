#!/usr/bin/python3.5
import subprocess
import re
import os
from subprocess import Popen, PIPE
import socket
def run():
    returnlist=[]
    dnsList=[]
    for i in range(0, 1):
        output = subprocess.check_output(["nmap", "--script=broadcast-dns-service-discovery"])
        line = str(output).split('|')[4].split("=")[1].split(" ")[0]
        dnsList.append(line)

    dnsList = dict.fromkeys(dnsList).keys()
    domainname1 = subprocess.check_output(["nslookup", "8.8.8.8"])
    domainname1 = str(domainname1).split(".\\n")[0].split("=")[1].strip()
    domainname2 = subprocess.check_output(["nslookup", "8.8.4.4"])
    domainname2 = str(domainname2).split(".\\n")[0].split("=")[1].strip()
    returnlist.append(["8.8.8.8", domainname1,None,None,None,None,None,None,None,None])
    returnlist.append(["8.8.4.4", domainname2,None,None,None,None,None,None,None,None])
    for dns in dnsList:
        index = 2
        returnlist.append([dns,None,None,None,None,None,None,None,None,None])
        try:
            domainname = subprocess.check_output(["nslookup", dns])
            domainname = str(domainname).split(".\\n")[0].split("=")[1].strip()
        except Exception:
            returnlist[index][1] = None
        else:
            returnlist[index][1] = domainname
        index += 1


    for i in range(len(returnlist)):
        saali = subprocess.run(['nslookup', 'switch.ch'])
        saali2 = subprocess.run(['nslookup', '8.8.8.8'])
        saali3 = subprocess.run(['nslookup', '20min.ch'])
        if (int(str(saali2).split("=")[2].split(")")[0]) + int(str(saali).split("=")[2].split(")")[0]) + int(str(saali3).split("=")[2].split(")")[0]) <= 1):
            returnlist[i][9] = True
    return returnlist
