#!/usr/bin/python3.5
#Controller

##TODO Array-Format bestimmen wie Daten übergeben werdne sollen

import scriptlib, dbcommands

#scripts 2mal aufrufen und in vars speichern
run1 = scriptlib.runScripts()
run2 = sriptlib.runScripts()

#vars vergleichen & logeinträge schreiben
goodRun = compareRuns(run1, run2)

#in DB schreiben
dbcommands.insertRun(goodRun)


def compareRuns(run1, run2):
    
    return goodRun