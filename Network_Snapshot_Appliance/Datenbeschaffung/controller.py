#!/usr/bin/python3.5
#Controller

import scriptlib, DBConnector

#TODO lets jsut cut the idea of twice execution
def run():
    #scripts 2mal aufrufen und in vars speichern
    run = scriptlib.runScripts()
    queryarray = scriptlib.getqueryarray()
    #run2 = sriptlib.runScripts()

    #vars vergleichen & logeinträge schreiben
    #goodRun = compareRuns(run1, run2)

    #in DB schreiben
    DBConnector.DBInsert(queryarray, run)
    print("done")


    #def compareRuns(run1, run2):

     #   return goodRun

run()
