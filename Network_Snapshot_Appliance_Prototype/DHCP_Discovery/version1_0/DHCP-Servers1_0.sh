#!/bin/bash

##prepare
exec 2> /dev/null
mkdir /tmp/dhcp
if ! [ -x "$(command -v nmap)" ]; then
        echo "nmap is not installed."
        echo "nmap will be installed now."
        apt-get update
        apt-get install nmap
fi

##Search for DHCP-Servers in the Network
echo "scanning..."
for i in {1..10}
do
        nmap --script broadcast-dhcp-discover >> /tmp/dhcp/dhcp.txt
done
echo "scan complete!"

##parsing
grep "Server Ident" /tmp/dhcp/dhcp.txt | cut -d: -f2 >> /tmp/dhcp/dhcp2.txt
while read line;
do
        line=$
(echo $line | tr -d '[:space:]')
        echo "$line" >> /tmp/dhcp/dhcp3.txt
done < /tmp/dhcp/dhcp2.txt

#Sort out the Duplicate IPs
awk '!seen[$0]++' /tmp/dhcp/dhcp3.txt >> /tmp/dhcp/dhcp4.txt

#Fill all the IPs into an Array
IFS=$'\r\n' GLOBIGNORE='*' command eval  'XYZ=($(cat /tmp/dhcp/dhcp4.txt))'

##cleanup
rm -r /tmp/dhcp

##testing
rm output.txt
touch output.txt
for element in "${XYZ[@]}"
do
    echo "IP = $element" >> output.txt
done
echo "output.txt has been created in the local folder. Consult it for the results of the scan"
