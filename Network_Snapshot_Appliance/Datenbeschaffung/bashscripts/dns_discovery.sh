#Version 1.0
#Author: Joel Meier
#Contact: joelmeie08@gmail.com
#!/bin/bash

#prepare
exec 2> /dev/null
mkdir -p /tmp/NSA/dhcp

#scan
echo "scanning..."	
nmap --script=broadcast-dns-service-discovery | grep -i "Address" | cut -f2 -d"=" >> /tmp/NSA/dns/dns3
echo "Scan complete"

#output
while read line;
do
    echo $lines
done < /tmp/NSA/dns/dns1

rm output.txt
cat /tmp/NSA/dns/dns2 >> output.txt
