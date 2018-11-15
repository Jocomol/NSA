#!/usr/bin/python3.5
#Controller

import scriptlib, dbcommands, DBConnector

#TODO lets jsut cut the idea of twice execution

#scripts 2mal aufrufen und in vars speichern
run = scriptlib.runScripts()
queryarray = scriptlib.getQuerryarray()
#run2 = sriptlib.runScripts()

#vars vergleichen & logeinträge schreiben
#goodRun = compareRuns(run1, run2)

#in DB schreiben
DBConnector.insertRun(queryarray, goodRun)


#def compareRuns(run1, run2):

 #   return goodRun
