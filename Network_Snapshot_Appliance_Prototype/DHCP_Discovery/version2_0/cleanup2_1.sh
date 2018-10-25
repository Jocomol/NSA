
#Version 2.1
#Author: Joel Meier
#contact: joelmeier08@gmail.com

#!/bin/bash

###Arguments
##r: Make the files for adding a fictional IP to the DHCP-IP list.
##Used to test if the Script allows 2 DHCP IPs if there is only one DHCP-Server present in the Network.

exec 2> /dev/null
##Delete
rm -r /tmp/NSA

##Redo
if [ "$1" == "r" ];then
        mkdir /tmp/NSA/dhcp
        mkdir /tmp/NSA/dhcp
        touch /tmp/NSA/dhcp/dhcp
        echo "Server Identifier: 111.111.111.0" >> /tmp/NSA/dhcp/dhcp1
fi

##End
echo "Done"
