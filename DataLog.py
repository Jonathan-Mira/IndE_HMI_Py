import csv
import datetime

class _Datalog:
   
    #Data Exporting Variables and Functions
    _filename = -1
    _CSVFile = -1
    _CSVWriter = -1
    def _FileOpen(self, filename): #Opens a new file and put the headers
        _Datalog._filename = filename
        _Datalog._CSVFile = open(_Datalog._filename, 'w', newline='')
        _Datalog._CSVWriter = csv.writer(_Datalog._CSVFile)
        _Datalog._CSVWriter.writerow(['Time',\
                                       'Speed'])
    def _FileWrite(self): #Write the data to the file
        _Datalog._CSVWriter.writerow([_Datalog._Speed\
                                      , _Datalog._Throttle])
    def _FileClose(self): #Close the file
        _Datalog._CSVFile.close()

    #Date and Time Variables
    _DateTime = -1
    def _DateTimeUpdate(self): #Update the date and time
        _Datalog._DateTime = datetime.datetime.now()
        
    #Motor Variables
    _Speed = -1
    _Throttle = -1
