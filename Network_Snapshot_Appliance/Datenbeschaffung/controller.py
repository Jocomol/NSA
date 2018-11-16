#!/usr/bin/python3.5
#Controller

import scriptlib, DBConnector

def run():
    run = scriptlib.runScripts()
    queryarray = scriptlib.getqueryarray()
    DBConnector.DBInsert(queryarray, run)
    print("done")
run()
