CREATE TABLE dns(
id INTEGER PRIMARY KEY,
working INTEGER
);

CREATE TABLE dhcp(
id INTEGER PRIMARY KEY,
leastime INTEGER,
ip_offered TEXT,
subnetmask TEXT,
router TEXT,
domainname TEXT
);

CREATE TABLE role(
id INTEGER PRIMARY KEY,
role TEXT
);

CREATE TABLE ip(
id INTEGER PRIMARY KEY,
ip TEXT,
hostname TEXT,
devicetype TEXT,
deviceos TEXT,
dhcp_id INTEGER,
dns_id INTEGER,
FOREIGN KEY (dhcp_id) REFERENCES dhcp(id),
FOREIGN KEY (dns_id) REFERENCES dns(id)
);

CREATE TABLE ip_role(
id INTEGER PRIMARY KEY ,
ip_id INTEGER,
role_id INTEGER,
FOREIGN KEY (ip_id) REFERENCES ip(id),
FOREIGN KEY (role_id) REFERENCES role(id)
);

CREATE TABLE query(
id INTEGER PRIMARY KEY,
date INTEGER,
ip_id INTEGER,
wanconnection INTEGER,
domainname TEXT,
match INTEGER,
FOREIGN KEY (ip_id) REFERENCES ip(id)
);
