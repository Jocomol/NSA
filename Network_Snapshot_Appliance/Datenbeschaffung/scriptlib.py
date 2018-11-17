#!/usr/bin/python3.5
#Scriptlibrary
import subprocess, dhcp_discovery, dns_discovery, ipaddress
from subprocess import Popen, PIPE
import datetime
from netaddr import IPNetwork

queryarray = ["",False,"",""] #Date, wanconnection, domainname, subnetmask
queryarray

def runScripts(conf):
    dhcpData = dhcpDiscovery(conf[3])
    dnsData = dnsDiscovery(conf[2])
    ips = ipDiscovery(conf[1])
    output = createOutput(dhcpData, dnsData, ips)

    return output

def createOutput(dhcp, dns, ips):
    for i in range (len(ips)):
        for k in range (len(dns)):
            if ips[i-1][0] == dns[k-1][0]:
                if ips[i-1][1] == None:
                    ips[i-1][1] = dns[k-1][1]
                ips[i-1][9] = dns[k-1][9]
                del dns[k-1]
        for g in range(len(dhcp)):
            if ips[i-1][0] == dhcp[g-1][0]:
                if ips[i-1][1] == None:
                    ips[i-1][1] = dhcp[g-1][1]
                ips[i-1][4] = dhcp[g-1][4]
                ips[i-1][5]= dhcp[g-1][5]
                ips[i-1][6]= dhcp[g-1][6]
                ips[i-1][7]= dhcp[g-1][7]
                ips[i-1][8]= dhcp[g-1][8]
                del dhcp[g-1]
    for k in range (len(dns)):
        ips.append(dns[k-1])
    for g in range (len(dhcp)):
        ips.append(dhcp[g-1])
    return ips




def ipDiscovery(repe):

    ip = getIP(repe)
    data = pingHosts(ip)

    return data


def dhcpDiscovery(conf):
    ##funktioniert
    #cmd = "['bash', 'bashscripts/dhcp_discovery.sh]"
    #data = execScpt(cmd)

    data = dhcp_discovery.run(conf)

    return data


def dnsDiscovery(conf):
    ##funktioniert
    #cmd = "['bash', 'bashscripts/dns_discovery.sh]"
    #data = execScpt(cmd)

    data = dns_discovery.run(conf)

    return data


def getIP(repe):
    output = subprocess.check_output(["ifconfig", repe]).decode() #TODO diese Zeile liest nur von der schnittstelle ens33 (von testcomputer) könnte eth0 sein
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
            queryarray[3] = mask
            mask = str(sum([bin(int(x)).count("1") for x in mask.split(".")])) #Diese Linie wandelt 255.255.255.0 in 24 um usw.
    combined = ip + "/" + mask

    return combined


def pingHosts(ip):
    output = subprocess.check_output(["nmap", "-sP", ip]).decode().split("\n")
    counter2 = 0
    allIp= []
    oneip = [None,None,None,None,None,None,None,None,None,None]
    for i in range(len(output)):
        if i != 0 and i !=1 and i != 2 and i != len(output)-1 and i != len(output)-2:
            if counter2 == 0:
                line1 = output[i-1].split(" ")
                if len(line1) == 6:
                    oneip[1] = line1[4]
                    step1 = line1[5].strip("(")
                    oneip[0] = step1.strip(")")
                else:
                    oneip[1] = None
                    step1 = line1[4].strip("(")
                    oneip[0] = step1.strip(")")
                counter2 = 1
            elif counter2 == 1:
                counter2 = 2
            elif counter2 == 2:
                passed = True
                if "MAC" in output[i-1]:
                    passed = False
                    line32 = output[i-1].split("(")[1]
                    line32 = line32.strip(")")
                    oneip[2] = line32
                allIp.append(oneip)
                oneip = [None,None,None,None,None,None,None,None,None,None]
                counter2 = 0
                if passed:
                    line1 = output[i].split(" ")
                    if len(line1) == 6:
                        oneip[1] = line1[4]
                        step1 = line1[5].strip("(")
                        oneip[0] = step1.strip(")")
                    else:
                        oneip[1] = None
                        step1 = line1[4].strip("(")
                        oneip[0] = step1.strip(")")
                    counter2 += 1
            else:
                print ("An Error happened")
                exit()
        #TODO OS Detection
    return allIp

def getqueryarray():
		#TODO Fill the Domainname index [2]
        queryarray[2] = "dummydomain.local"
        queryarray[0] = str(datetime.datetime.now())
        queryarray[1] = checkWanconnection()
        return queryarray


def checkWanconnection():
    toping = Popen(['ping','-c', '1', '8.8.8.8'], stdout=PIPE)
    output = toping.communicate()[0]
    wanconnection = toping.returncode
    return wanconnection == 0
