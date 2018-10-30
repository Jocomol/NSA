#Version 1.0
#Author: Joel Meier
#Contact: joelmeie08@gmail.com
#!/bin/bash

#prepare
exec 2> /dev/null
mkdir -p /tmp/NSA/dhcp

#scan
echo "scanning..."
for i in {1..10}
do
	nmap --script=broadcast-dns-service-discovery |grep "Address" 2> /dev/null >> /tmp/NSA/dns/dns1
done
echo "Scan complete"

#parsing
while read line;
do
        i=$((i+1))
        if ! [ $i -eq 8 ];
        then
                line=$(echo $line) #better parsing
                echo "$line" >> /tmp/NSA/dns/dns2
        else
                echo "" >> /tmp/NSA/dns/dns2
                i=0
        fi
done < /tmp/NSA/dns/dns1

rm output.txt
cat /tmp/NSA/dns/dns2 >> output.txt

