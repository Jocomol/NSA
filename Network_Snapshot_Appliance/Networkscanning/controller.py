#!/usr/bin/python3.5
#Controller
import scriptlib, DBConnector

#Run the Scriptlib
def run():
    configuration = DBConnector.getConfiguration()
    run = scriptlib.runScripts(configuration)
    queryarray = scriptlib.getqueryarray()
    DBConnector.DBInsert(queryarray, run)
run()
