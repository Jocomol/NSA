##WIP
import subprocess
import re
dhcpList=[]
for i in range(0, 1):
    ##output = subprocess.check_output(["nmap", "--script=broadcast-dhcp-discover"])
    output = subprocess.check_output(["cat", "output.txt"])

    for c in range(0, 9):
        if c != 2 and c != 0:
            print (str(output).split("\\n")[c].split(":")[1].strip())

    # TODO fill out arrays
    #for e in range (0,10):
    #    arrayindex = 0
    #    if e != 2 and c != 3 and c != 9:
    #        print
    #offered_ip = str(output).split("\\n")[1].split(":")[1].strip()
    #ip = str(output).split("\\n")[3].split(":")[1].strip()


#Notes  2,3,9 not 
#     ["192.168.1.2","dhcp",None,None,"2","192.681.22.3","255.0.0.0","192.168.1.1","local",None],
#ip offered = 1
#ip dhcp = 3
#leastime = 4
#mask = 5
#router = 6
#dns = 7
#domain name = 8
