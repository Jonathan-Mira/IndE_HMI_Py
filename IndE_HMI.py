import sys
import DataLog
import csv


Datalog_ = DataLog._Datalog()
Datalog_._DateTimeUpdate()

Datalog_._FileOpen('IndE_HMI.csv')
Datalog_._FileWrite()
Datalog_._DateTimeUpdate()
Datalog_._FileWrite()
Datalog_._FileClose()
