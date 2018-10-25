#!/bin/bash
touch NSA_DB.db
sqlite3 NSA_DB.db < createDB.sql
