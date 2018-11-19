#!/bin/bash
if [ "$EUID" -ne 0 ];
then
        echo "Please run as root"
	exit
fi

python3 /etc/NSA/script/conf.py
