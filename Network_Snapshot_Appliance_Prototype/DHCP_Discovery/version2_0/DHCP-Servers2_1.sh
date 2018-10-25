#Version 2.0
#Author: Joel Meier
#Contact: joelmeie08@gmail.com
#Consult the README file for more info and the Changelog

#!/bin/bash

##Prepare
exec 2> /dev/null
datetime=$(date)
mkdir -p /tmp/NSA/dhcp
if ! [ -x "$(command -v nmap)" ]; then
        echo "nmap is not installed."
        echo "nmap will be installed now."
        apt-get update
        apt-get install nmap
fi
echo "scanning..."
for i in {1..10}
do
        nmap --script broadcast-dhcp-discover | grep "Server Ident\|IP\|Subnet\|Router\|Domain" >> /tmp/NSA/dhcp/dhcp1
done
echo "Scan complete!"

##Parsing
i=0
while read line;
do
        i=$((i+1))
        if ! [ $i -eq 8 ];
        then
                line=$(echo $line | cut -d: -f2 | tr -d '[:space:]')
                echo "$line" >> /tmp/NSA/dhcp/dhcp2
        else
                echo "" >> /tmp/NSA/dhcp/dhcp2
                i=0
        fi
done < /tmp/NSA/dhcp/dhcp1

##testing
rm output.txt
cat /tmp/NSA/dhcp/dhcp2 >> output.txt
echo "output.txt has been created in the local folder. Consult it for the results of the scan"
echo $datetime >> output.txt
##Database Acces or starting the Database Script will be here

##cleanup
rm -r /tmp/NSA

#Note: There are Duplicate Entrys in the /tmp/NSA/dhcp/dhcp2 File. The Duplicates are sorted out in the SQL script.
