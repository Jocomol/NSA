#!/usr/bin/python3.5
import subprocess
import re
dnsList=[]
for i in range(0, 3):
    output = subprocess.check_output(["nmap", "--script=broadcast-dns-service-discovery"])
    line = str(output).split('|')[4].split("=")[1].split(" ")[0]
    dnsList.append(line)

dnsList = dict.fromkeys(dnsList).keys()
for dns in dnsList:
    print(dns)

##CHECK ALL IPs IN LIST AND DELETE DUPLICATe ONES
