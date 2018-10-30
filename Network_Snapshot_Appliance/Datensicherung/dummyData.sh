#!/bin/bash
echo "starting database creation"
touch NSA-DB.db
sqlite3 NSA_DB.db < createDB.sql
sqlite3 NSA_DB.db < testing/insertDB.sql
sqlite3 NSA_DB.db < testing/selectDB.sql
echo "Database creation finished"
