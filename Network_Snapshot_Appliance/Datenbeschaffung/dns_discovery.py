#!/usr/bin/python3.5
import subprocess
import re
import os
from subprocess import Popen, PIPE
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
    for dns in dnsList:
        index = 2
        returnlist.append([dns,None,None,None,None,None,None,None,None,None])
        try:
            domainname = subprocess.check_output(["nslookup", dns]) #1
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            returnlist.append(None)
        else:
            returnlist.append(domainname)


    for i in range(len(returnlist)):
        try:
            domainname = subprocess.check_output(["nslookup","switch.ch", returnlist[i][0]])
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            return1 = 0
        else:
            return1 = 1
        try:
            domainname = subprocess.check_output(["nslookup", "20min.ch", returnlist[i][0]])
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            return2 = 0
        else:
            return2 = 1
        try:
            domainname = subprocess.check_output(["nslookup", "8.8.8.8", returnlist[i][0]])
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            return3 = 0
        else:
            return3 = 1

        print (return1, return2, return3)
        if (return1 + return2 + return3 >= 2):
            returnlist[i][9] = True

    return returnlist




## TODO Check if DNS works

print(run())
