#!/bin/bash

if [ "$EUID" -ne 0 ];
then
        echo "Please run as root"
	exit
fi

apt update
apt install python3 sqlite3 php7.2 python3-pip php7.2-sqlite3
pip install pip
pip install netaddr
a2dismod mpm_event
a2dismod mpm_worker
a2enmod mpm_prefork
a2enmod php7.2

mkdir /etc/NSA
mkdir /etc/NSA/data
mkdir /etc/NSA/script
mkdir /etc/NSA/frontend

cp ./conf.py /etc/NSA/script
cp ../Datenbeschaffung/* /etc/NSA/script
cp ../Frontend/NSA/* /var/www/html
ln -s /var/www/html /etc/NSA/frontend
chmod +x nsaconf.sh
cp ./nsaconf.sh /usr/bin/nsaconf

cp ../Datensicherung/createDB.sql /etc/NSA/data
touch /etc/NSA/data/NSA_DB.db
sqlite3 /etc/NSA/data/NSA_DB.db < /etc/NSA/data/createDB.sql
rm /etc/NSA/data/createDB.sql

#user info
echo "Please execute the command sudo nsaconf to configure the appliance"
