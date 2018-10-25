#!/bin/bash
sudo touch testDB_DHCP.db
sqlite3 testDB_DHCP.db < createTestDatabaseDHCP.sql

