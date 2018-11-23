#!/usr/bin/python3.5
import subprocess, os
def run(repe):
    returnlist=[]
    dnsList=[]
    for i in range(repe):
        output = subprocess.check_output(["nmap", "--script=broadcast-dns-service-discovery"])
        try:
            line = str(output).split('|')[4].split("=")[1].split(" ")[0]
            if line[-1:] == "n":
                line = line.strip("n")
                line = line.strip("\\")
        except IndexError:
            line = None
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
        firstcheck = subprocess.run(['nslookup', 'switch.ch'])
        secondcheck = subprocess.run(['nslookup', '8.8.8.8'])
        thirtchek = subprocess.run(['nslookup', '20min.ch'])
        if (int(str(secondcheck).split("=")[2].split(")")[0]) + int(str(firstcheck).split("=")[2].split(")")[0]) + int(str(thirtchek).split("=")[2].split(")")[0]) <= 1):
            returnlist[i][9] = True
    returnarray = []
    inreturn = ["dummy"]
    for j in range(len(returnlist)):
        if returnlist[j][0] in str(inreturn):
            x = 0
        else:
            returnarray.append(returnlist[j])
            inreturn.append(returnlist[j][0])
    return returnarray
