The newest Version is in this Folder (Version2_X), the older Versions are in theyr respective Folders.

Changelog DHCP-Servers.sh
1.0 - 1.5:
	+ Script can read out every DHCP in the Network.
2.0:
	+ Rewrote the whole File
	+ Changed all the files no non *.txt files.
	+ The Script now filters following infos:
		> IP of the DHCP
		> Offered IP
		> Subnet IP
		> Router IP
		> Domain Name
		> Domain Name Servers
	- Sorting out Duplicate addresses. This will be implemented in the upcoming SQL script
	- Less Files are Created
	+ /tmp/NSA folder wich holds all temporary files.

2.1: 
	+ Script now saves the time
	

Changelog cleanup.sh
1.0:
	+ Script cleans up /tmp/dhcp/*
	+ Whit the Argument "r" its possible to write a fictional IP in the /tmp/dhcp/dhcp1.txt
2.0:
	+ added folder /tmp/NAS/. DHCP and all the Other Folders will be in /tmp/NAS/*
2.1:
	+ Fixed bugs wich made the Script useless
2.2:
	- Removed the Argument "r" and its function since it wasnt used or functional anymore. 
	  For the function "r" use version 2.1 
	