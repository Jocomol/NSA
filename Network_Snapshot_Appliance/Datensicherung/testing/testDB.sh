#!/bin/bash
sqlite3 NSA_DB.db < insertDB.sql
sqlite3 NSA_DB.db < selectDB.sql
