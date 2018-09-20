#!/bin/bash
echo "Offered IP:"
read OIP
echo "ServerIden"
read SI
echo "Latency"
read LC
echo "Netmask"
read NM
echo "DNS"
read DNS
echo "Router"
read RT
echo "Domain"
read DM

sqlite3 testDB_DHCP.db "INSERT INTO Messwerte(OfferedIP, ServerIdentifier, Latency, Netmask, DNS, Router, Domainname) VALUES ('$OIP','$SI','$LC','$NM','$DNS','$RT','$DM');"

echo "Done"
