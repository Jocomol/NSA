#!/usr/bin/python3.5
#Scriptlibrary
import subprocess, dhcp_discovery, dns_discovery, ipaddress
from subprocess import Popen, PIPE

querryarray = ["",False,"",True] #Date, wanconnection, domainname, match

def runScripts():
    allIPs = ipDiscovery()
    dhcpData = dhcpDiscovery()
    dnsData = dnsDiscovery()
    output = createOutput(dhcpData, dnsData, ips)

    return output

def createOutput(dhcp, dns, ips):
    output = []
    merged = []
    for i in range(len(dhcp)):
        for k in range(len(dns)):
            if dhcp[i-1][0] == dns[k-1][0]:
                merged = dhcp[i-1]
                merged[9] = dns[k-1][9]
                del dns[k - 1]
                del dhcp[i - 1]
                output.append(merged)
    for k in range(len(dhcp)):
        output.append(dhcp[k-1])

    for k in range(len(dns)):
        output.append(dns[k-1])

    return output
    for k in range (len(ips)):
        for i in range (len(output)):
            if output[i-1][0] == ips[k-1][0]:
                ips.pop(k)


def ipDiscovery():
	#TODO make this work
    ip = getIP()
    data = pingHosts(ip)

    return data


def dhcpDiscovery():
    ##funktioniert
    #cmd = "['bash', 'bashscripts/dhcp_discovery.sh]"
    #data = execScpt(cmd)

    data = dns_discovery.run()

    return data


def dnsDiscovery():
    ##funktioniert
    #cmd = "['bash', 'bashscripts/dns_discovery.sh]"
    #data = execScpt(cmd)

    data = dhcp_discovery.run()

    return data


def getIP():
    output = subprocess.check_output(["ifconfig", "ens33"]).decode() #TODO diese Zeile liest nur von der schnittstelle ens33 (von testcomputer) könnte eth0 sein
    print(output)
    array = output.split('\n')
    line = ""
    ip = ""
    mask = ""
    for item in array:
        if "inet" in item:
            if "127" not in item:
                if "::" not in item:
                    ip = item.split(" ")[9]
                    print (line)
        if "netmask" in item:
            mask = item.split(" ")[12]
            mask = str(sum([bin(int(x)).count("1") for x in mask.split(".")])) #Diese Linie wandelt 255.255.255.0 in 24 um usw.
    combined = ip + "/" + mask

    return combined




def pingHosts(ip):
	#TODO make this work
    #Code von: https://topnetworkguide.com/how-to-use-python-to-ping-all-ip-addresses-on-a-network/
    network = ipaddress.ip_network(ip) #TODO Funktioniert nicht da man die Netzwerk addresse Bnötigt, mit zb dem modul netaddr könnte man dies umwandeln
    for i in network.hosts():
        i = str(i)
        toping = Popen(['ping','-c', '1', i], stdout=PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            #reachable
            print("reachable")

            #TODO, 2D-Array
            #[["192.168.1.1", "client",None,None,None,None,None,None,None,None],["192.168.1.2", "client",None,None,None,None,None,None,None,None]]

    return ips


def getQuerryarray():
		
		#TODO Fill out the date index [0]
		#TODO Fill the Domainname index [2]
		querryarray[1] = checkWanconnection
		return querryarray
	
#TODO Needs cmd like cmd = "['bash', 'bashscripts/test.sh]"
def execScpt(cmd):

    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')

    return retVal

	
def checkWanconnection(ip):
	#TODO make this work ping 8.8.8.8 or so
	output = False
	return output

#Dummy Data for testing
'''
a = [["192.168.1.1","dhcp1",None,None,"2","192.681.22.3","255.0.0.0","192.168.1.1","hellow.local",None],
    ["192.168.1.2","dhcp2",None,None,"2","192.681.22.43","255.0.0.0","192.168.1.1","succ.local",None],
    ["192.168.1.3","dhcp3",None,None,"2","192.681.22.53","255.0.0.0","192.168.1.1","kraftwerk.local",None]]

b = [["192.168.1.1", "dhcp1",None,None,None,None,None,None,None,True],
     ["192.168.1.5", "dns",None,None,None,None,None,None,None,True]]

c = [["192.168.1.1", "dhcp1",None,None,None,None,None,None,None,None],
    ["192.168.1.2", "dhcp2",None,None,None,None,None,None,None,None],
    ["192.168.1.3", "dhcp3",None,None,None,None,None,None,None,None],
    ["192.168.1.5", "dns",None,None,None,None,None,None,None,None],
    ["192.168.1.7", "client1",None,None,None,None,None,None,None,None],
    ["192.168.1.6", "client2",None,None,None,None,None,None,None,None]]

print(createOutput(a,b,c)) #dhcp dns all
'''

