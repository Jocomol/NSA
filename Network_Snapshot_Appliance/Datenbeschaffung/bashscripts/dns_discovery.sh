#!/bin/bash
#Version 1.0
#Author: Joel Meier
#Contact: joelmeie08@gmail.com


#prepare
exec 2> /dev/null
mkdir -p /tmp/NSA/dhcp

#scan
echo "scanning..."	
    nmap --script=broadcast-dns-service-discovery | grep -i "Address" | cut -f2 -d"=" >> /tmp/NSA/dns/dns3
    #debug
    #grep -i "Address" /tmp/NSA/dns/dns1 | cut -f2 -d"=" >> /tmp/NSA/dns/dns3
echo "Scan complete"

#output
while read line;
do 
    ##TODO, herausfinden ob DNS-Server funktioniert (ob nslookup erfolgreich war)
    result=$(nslookup www.google.ch $line)
    if grep -q "Address" <<< $result; then
        echo $line "True"
    else
        echo $line "False"
    fi

done < /tmp/NSA/dns/dns3

rm output.txt
cat /tmp/NSA/dns/dns2 >> output.txt
