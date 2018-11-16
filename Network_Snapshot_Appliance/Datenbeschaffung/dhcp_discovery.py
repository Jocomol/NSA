#!/usr/bin/python3.5
import subprocess
import re
def run():
    dhcpList=[]
    OneDHCP=[]
    parsedDHCP=[]
    for i in range(0, 10):
        output = subprocess.check_output(["nmap", "--script=broadcast-dhcp-discover"])
        for c in range(0, 14):
            if c != 0 and c != 1 and c != 2 and c!=3  and c!= 4 and c!=6 and c!= 13 and c!=14:
                helpme = (str(output).split("\\n")[c].split(":")[1].strip())
                OneDHCP.append(helpme)
        parsedDHCP.append(OneDHCP[1])                   #0
        try:
            domainname = subprocess.check_output(['nslookup', OneDHCP[1]]) #1
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            parsedDHCP.append(None)
        else:
            parsedDHCP.append(domainname)
        parsedDHCP.append(None)                         #2
        parsedDHCP.append(None)                         #3
        parsedDHCP.append(OneDHCP[2])                   #4
        parsedDHCP.append(OneDHCP[0])                   #5
        parsedDHCP.append(OneDHCP[3])                   #6
        parsedDHCP.append(OneDHCP[4])                   #7
        parsedDHCP.append(OneDHCP[6])                   #8
        parsedDHCP.append(None)                         #9

        dhcpList.append(parsedDHCP)
        OneDHCP=[]
        parsedDHCP=[]
    returnarray = []
    inreturn = ["dummy"]

    for j in range(len(dhcpList)):
        if dhcpList[j][0] in str(inreturn):
            x = 0
        else:
            returnarray.append(dhcpList[j])
            inreturn.append(dhcpList[j][0])
    return returnarray
