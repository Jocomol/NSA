/* Insert Query*/
INSERT INTO query (date, wanconnection, domainname, match) 
VALUES
("30.10.2018",1,"domain.local",1);

/*Insert all ips*/
INSERT INTO ip (ip, hostname, devicetype, deviceos, dhcp_id, dns_id, query_id)
VALUES
("192.168.1.1","router.local",NULL,NULL,NULL,NULL,1),
("192.168.1.2","client.local","DELL","windows 10",NULL,NULL,1),
("192.168.1.3","dns.local","Mainframe","UBUNTU 18.1",NULL,NULL,1),
("192.168.1.4","dhcp.local","Mainframe","Ubuntu 18.1",NULL,NULL,1),
("192.168.1.69","intruder.local","HP","Kali Linux",NULL,NULL,1);

/* Insert ROles */
INSERT INTO ip_role (ip_id, role_id)
VALUES
(1,1),
(3,2),
(4,3);

/* Insert DHCP entry */
INSERT INTO dhcp (leastime, ip_offered, subnetmask, router, domainname)
VALUES
(0800,"192.168.1.50","255.255.255.0","192.168.1.1","domain.local");

UPDATE ip SET dhcp_id = 1 WHERE ip = "192.168.1.4";

/*Insert DNS entry*/
INSERT INTO DNS (working)
VALUES
(1);

UPDATE ip SET dns_id = 1 WHERE ip = "192.168.1.3";
