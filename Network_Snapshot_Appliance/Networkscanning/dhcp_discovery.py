#!/usr/bin/python3.5
#DHCP-Discovery
import subprocess
def run(repe):
    dhcpList=[]
    OneDHCP=[]
    parsedDHCP=[]

    #Execute Nmap script
    for i in range(repe):
        output = subprocess.check_output(["nmap", "--script=broadcast-dhcp-discover"])
        for c in range(0, 14):
            if c != 0 and c != 1 and c != 2 and c!=3  and c!= 4 and c!=6 and c!= 13 and c!=14 and len(str(output).split("\\n")) >= 10:
                parsedOutput = (str(output).split("\\n")[c].split(":")[1].strip())
                OneDHCP.append(parsedOutput)
            elif len(str(output).split("\\n")) <= 10:
                parsedOutput = None
                OneDHCP.append(parsedOutput)
        parsedDHCP.append(OneDHCP[1])

        #Check if DHCP works and fill in array
        try:
            domainname = subprocess.check_output(['nslookup', OneDHCP[1]])
            domainname = str(domainname).split(".\\n")[0].split("=")[1]
        except Exception:
            parsedDHCP.append(None)
        else:
            parsedDHCP.append(domainname)
        parsedDHCP.append(None)
        parsedDHCP.append(None)
        parsedDHCP.append(OneDHCP[2])
        parsedDHCP.append(OneDHCP[0])
        parsedDHCP.append(OneDHCP[3])
        parsedDHCP.append(OneDHCP[4])
        parsedDHCP.append(OneDHCP[6])
        parsedDHCP.append(None)
        dhcpList.append(parsedDHCP)
        OneDHCP=[]
        parsedDHCP=[]
    returnarray = []
    inreturn = ["dummy"]

    #Delete Duplicats and output
    for j in range(len(dhcpList)):
        if dhcpList[j][0] == None:
            x = 0
        elif dhcpList[j][0] in str(inreturn):
            x = 0
        else:
            returnarray.append(dhcpList[j])
            inreturn.append(dhcpList[j][0])
    return returnarray
