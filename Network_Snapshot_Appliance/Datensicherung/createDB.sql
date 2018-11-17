CREATE TABLE dns(
id INTEGER PRIMARY KEY AUTOINCREMENT,
working INTEGER
);

CREATE TABLE dhcp(
id INTEGER PRIMARY KEY AUTOINCREMENT,
leastime INTEGER,
ip_offered TEXT,
subnetmask TEXT,
router TEXT,
domainname TEXT
);

CREATE TABLE role(
id INTEGER PRIMARY KEY AUTOINCREMENT,
role TEXT
);

CREATE TABLE query(
id INTEGER PRIMARY KEY NOT NULL,
date TEXT NOT NULL,
wanconnection INTEGER NOT NULL,
domainname TEXT NOT NULL,
subnetmask TEXT NOT NULL
);

CREATE TABLE ip(
id INTEGER PRIMARY KEY NOT NULL,
ip TEXT,
hostname TEXT,
devicetype TEXT,
deviceos TEXT,
dhcp_id INTEGER,
dns_id INTEGER,
query_id INTEGER,
FOREIGN KEY (query_id) REFERENCES query(id),
FOREIGN KEY (dhcp_id) REFERENCES dhcp(id),
FOREIGN KEY (dns_id) REFERENCES dns(id)
);

CREATE TABLE ip_role(
id INTEGER PRIMARY KEY,
ip_id INTEGER,
role_id INTEGER,
FOREIGN KEY (ip_id) REFERENCES ip(id),
FOREIGN KEY (role_id) REFERENCES role(id)
);

CREATE TABLE configuration(
id INTEGER PRIMARY KEY NOT NULL,
interface TEXT NOT NULL,
dnsrepetation INTEGER NOT NULL,
dhcprepetation INTEGER NOT NULL
);

INSERT INTO role (id, role)
VALUES
(1,"DNS"),
(2,"DHCP");
