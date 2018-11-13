#!/usr/bin/python3.5
#Scriptlibrary

import subprocess, dhcp_discovery, dns_discovery, ipaddress
from subprocess import Popen, PIPE


def runScripts():
    #TODO, run all scripts

    allIPs = ipDiscovery()
    dhcpData = dhcpDiscovery()
    dnsData = dnsDiscovery()
    print (dnsData)
    output = createOutput(dhcpData, dnsData, ips)

    return output

def createOutput(dhcp, dns, ips):
    output = []
    merged = []
    for i in range(len(dhcp) -1 ):
        for k in range(len(dns) -1):
            if dhcp[i][0] == dns[k][0]:
                merged = dhcp[i]
                merged[9] == dns[k][9]
                dns.pop(k)
                output.append(merged)

    for k in range(len(dns)):
        output.append(dns[k])

    for k in range(len(ips)):
        output.append(ips[k])


    return output



def ipDiscovery():

    ip = getIP()
    data = pingHosts(ip)

    return data


def dhcpDiscovery():
    ##geht noch nicht
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

    ##TODO, Adresse von Host erhalten z.B. 192.168.220.0/255.255.255.0

    output = subprocess.check_output(["ifconfig"]).decode()

    array = output.split('\n')

    for item in array:
        if "inet addr" in item:
            if "addr:127" not in item:
                line = item.split(" ")

    for part in line:
        if "addr" in part:
            ip = part.split(":")[1]
        if "Mask" in part:
            mask = part.split(":")[1]

    combined = ip + "/" + mask

    return combined




def pingHosts(ip):
    #Code von: https://topnetworkguide.com/how-to-use-python-to-ping-all-ip-addresses-on-a-network/
    network = ipaddress.ip_network(ip)
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



        else:
            #unreachable
            #wird nicht benötigt
            print("unreachable")

    return ips


#Needs cmd like cmd = "['bash', 'bashscripts/test.sh]"
def execScpt(cmd):

    result = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    retVal = result.stdout.decode('utf-8')

    return retVal
