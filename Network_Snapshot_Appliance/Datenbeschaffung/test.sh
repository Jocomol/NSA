#!/bin/bash


grep -i "Address" /tmp/NSA/dns/dns1 | cut -f2 -d"=" >> /tmp/NSA/dns/dns3


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

#rm output.txt
cat /tmp/NSA/dns/dns2 > output.txt

