#!/bin/bash

###Arguments
##r: Make the files for adding a fictional IP to the DHCP-IP list.
##Used to test if the Script allows 2 DHCP IPs if there is only one DHCP-Server present in the Network.

exec 2> /dev/null
##Delete
rm -r /tmp/dhcp

##Redo
if [ "$1" == "r" ];then
	mkdir /tmp/dhcp
	mkdir /tmp/dhcp
	touch /tmp/dhcp/dhcp.txt
	echo "Server Identifier: 111.111.111.0" >> /tmp/dhcp/dhcp.txt
fi

##End
echo "Done"
