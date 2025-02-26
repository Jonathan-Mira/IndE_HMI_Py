import sys
import DataLog
import csv


Datalog_ = DataLog._Datalog()
Datalog_._DateTimeUpdate()


while True:
    Datalog_._DateTimeUpdate()
    print(Datalog_._DateTime.strftime("%H:%M:%S.%f"))
