import csv
import datetime
import os

class _Data:
    def __init__(self, ID):
        self._ID = ID
    
    _ID = -1
    _value = -1

class _BatteryPair:
    def __init__(self, CapID, V1ID, V2ID, V3ID, V4ID, V5ID, V6ID, V7ID, V8ID):
        self._Capacity = _Data(CapID)
        self._Voltage1 = _Data(V1ID)
        self._Voltage2 = _Data(V2ID)
        self._Voltage3 = _Data(V3ID)
        self._Voltage4 = _Data(V4ID)
        self._Voltage5 = _Data(V5ID)
        self._Voltage6 = _Data(V6ID)
        self._Voltage7 = _Data(V7ID)
        self._Voltage8 = _Data(V8ID)

class _BatteryTemp:
    def __init__(self, T1ID, T2ID, T3ID, T4ID):
        self._Temp1 = _Data(T1ID)
        self._Temp2 = _Data(T2ID)
        self._Temp3 = _Data(T3ID)
        self._Temp4 = _Data(T4ID)

    def _HighestTemp(self):
        return max(self._Temp1._value, self._Temp2._value, self._Temp3._value, self._Temp4._value)
            


class _Datalog:

    def __init__(self):
        self._DateTimeUpdate()

    #Warning values
    ControllerTempCaution = 90
    ControllerTempWarning = 100
    MotorTempCaution = 90
    MotorTempWarning = 100
    BatteryTempCaution = 40
    BatteryTempWarning = 50
    BatteryChargeCaution = 50
    BatteryChargeWarning = 25
   
    #Data Exporting Variables and Functions
    _filename = -1
    _CSVFile = -1
    _CSVWriter = -1
    def _FileOpen(self, filename): #Opens a new file and put the headers
        self._filename = filename + self._DateTime.strftime("_%Y-%m-%d_%H-%M-%S.csv")
        if not os.path.exists("../IndE_Data/"):
            os.mkdir("../IndE_Data/")
        self._CSVFile = open("../IndE_Data/"+self._filename, 'w', newline='')
        self._CSVWriter = csv.writer(self._CSVFile)
        
        #Creates the Headers for the CSV File
        self._CSVWriter.writerow(['Date', 'Time',\
                                    \
                                        'Emergency Stop', 'Windshield Wiper', 'Drive Mode',\
                                        \
                                    \
                                        'Throttle', 'Brake', 'Acceleration', 'RPM', 'Speed', 'Distance',\
                                        \
                                    \
                                        'Controller Temp 1', 'Controller Temp 2', 'Controller Temp 3',\
                                        'Controller Temp 4', 'Controller Temp 5', 'Controller Temp 6',\
                                        'Motor Temp', 'Phase Current A', 'Phase Current B', 'Phase Current C', 'Motor Torque',\
                                        \
                                    \
                                        'Motor Vector 1', 'Motor Vector 2', 'Motor Vector 3',\
                                        'Motor Vector 4', 'Motor Vector 5', 'Motor Vector 6',\
                                        \
                                    \
                                        'Battery Current', 'BMS Status',\
                                        \
                                    \
                                        'Battery Pair 1 Capacity',\
                                        'Battery Pair 1 Voltage 1', 'Battery Pair 1 Voltage 2', 'Battery Pair 1 Voltage 3', 'Battery Pair 1 Voltage 4',\
                                        'Battery Pair 1 Voltage 5', 'Battery Pair 1 Voltage 6', 'Battery Pair 1 Voltage 7', 'Battery Pair 1 Voltage 8',\
                                        \
                                    \
                                        'Battery Pair 2 Capacity',\
                                        'Battery Pair 2 Voltage 1', 'Battery Pair 2 Voltage 2', 'Battery Pair 2 Voltage 3', 'Battery Pair 2 Voltage 4',\
                                        'Battery Pair 2 Voltage 5', 'Battery Pair 2 Voltage 6', 'Battery Pair 2 Voltage 7', 'Battery Pair 2 Voltage 8',\
                                        \
                                    \
                                        'Battery Pair 3 Capacity',\
                                        'Battery Pair 3 Voltage 1', 'Battery Pair 3 Voltage 2', 'Battery Pair 3 Voltage 3', 'Battery Pair 3 Voltage 4',\
                                        'Battery Pair 3 Voltage 5', 'Battery Pair 3 Voltage 6', 'Battery Pair 3 Voltage 7', 'Battery Pair 3 Voltage 8',\
                                        \
                                    \
                                        'Battery A Temp 1', 'Battery A Temp 2', 'Battery A Temp 3', 'Battery A Temp 4',\
                                        'Battery B Temp 1', 'Battery B Temp 2', 'Battery B Temp 3', 'Battery B Temp 4',\
                                        'Battery C Temp 1', 'Battery C Temp 2', 'Battery C Temp 3', 'Battery C Temp 4',\
                                        'Battery D Temp 1', 'Battery D Temp 2', 'Battery D Temp 3', 'Battery D Temp 4',\
                                        'Battery E Temp 1', 'Battery E Temp 2', 'Battery E Temp 3', 'Battery E Temp 4',\
                                        'Battery F Temp 1', 'Battery F Temp 2', 'Battery F Temp 3', 'Battery F Temp 4',\
                                ])
        #Addes the Variable ID to the CSV File
        self._CSVWriter.writerow(['', '',\
                                    \
                                        self._EmergencyStop._ID, self._WindShieldWiper._ID, self._DriveMode._ID,\
                                        \
                                    \
                                        self._Throttle._ID, self._Brake._ID, self._Acceleration._ID, self._RPM._ID, self._Speed._ID, self._Distance._ID,\
                                        \
                                    \
                                        self._ControllerTemp1._ID, self._ControllerTemp2._ID, self._ControllerTemp3._ID,\
                                        self._ControllerTemp4._ID, self._ControllerTemp5._ID, self._ControllerTemp6._ID,\
                                        self._MotorTemp._ID, self._PhaseCurrentA._ID, self._PhaseCurrentB._ID, self._PhaseCurrentC._ID, self._MotorTorque._ID,\
                                        \
                                    \
                                        self._MotorVector1._ID, self._MotorVector2._ID, self._MotorVector3._ID,\
                                        self._MotorVector4._ID, self._MotorVector5._ID, self._MotorVector6._ID,\
                                        \
                                    \
                                        self._BatteryCurrent._ID, self._BMS1Status._ID,\
                                        \
                                    \
                                        self._BatPair1._Capacity._ID,\
                                        self._BatPair1._Voltage1._ID, self._BatPair1._Voltage2._ID, self._BatPair1._Voltage3._ID, self._BatPair1._Voltage4._ID,\
                                        self._BatPair1._Voltage5._ID, self._BatPair1._Voltage6._ID, self._BatPair1._Voltage7._ID, self._BatPair1._Voltage8._ID,\
                                        \
                                    \
                                        self._BatPair2._Capacity._ID,\
                                        self._BatPair2._Voltage1._ID, self._BatPair2._Voltage2._ID, self._BatPair2._Voltage3._ID, self._BatPair2._Voltage4._ID,\
                                        self._BatPair2._Voltage5._ID, self._BatPair2._Voltage6._ID, self._BatPair2._Voltage7._ID, self._BatPair2._Voltage8._ID,\
                                        \
                                    \
                                        self._BatPair3._Capacity._ID,\
                                        self._BatPair3._Voltage1._ID, self._BatPair3._Voltage2._ID, self._BatPair3._Voltage3._ID, self._BatPair3._Voltage4._ID,\
                                        self._BatPair3._Voltage5._ID, self._BatPair3._Voltage6._ID, self._BatPair3._Voltage7._ID, self._BatPair3._Voltage8._ID,\
                                        \
                                    \
                                        self._BatTempA._Temp1._ID, self._BatTempA._Temp2._ID, self._BatTempA._Temp3._ID, self._BatTempA._Temp4._ID,\
                                        self._BatTempB._Temp1._ID, self._BatTempB._Temp2._ID, self._BatTempB._Temp3._ID, self._BatTempB._Temp4._ID,\
                                        self._BatTempC._Temp1._ID, self._BatTempC._Temp2._ID, self._BatTempC._Temp3._ID, self._BatTempC._Temp4._ID,\
                                        self._BatTempD._Temp1._ID, self._BatTempD._Temp2._ID, self._BatTempD._Temp3._ID, self._BatTempD._Temp4._ID,\
                                        self._BatTempE._Temp1._ID, self._BatTempE._Temp2._ID, self._BatTempE._Temp3._ID, self._BatTempE._Temp4._ID,\
                                        self._BatTempF._Temp1._ID, self._BatTempF._Temp2._ID, self._BatTempF._Temp3._ID, self._BatTempF._Temp4._ID,\
                                ])

        

    def _FileWrite(self): #Write the data to the file
        self._CSVWriter.writerow([self._DateTime.strftime('%y/%m/%d'), self._DateTime.strftime('%H:%M:%S.%f'),\
                                    \
                                        self._EmergencyStop._value, self._WindShieldWiper._value, self._DriveMode._value,\
                                        \
                                    \
                                        self._Throttle._value, self._Brake._value, self._Acceleration._value, self._RPM._value, self._Speed._value, self._Distance._value,\
                                        \
                                    \
                                        self._ControllerTemp1._value, self._ControllerTemp2._value, self._ControllerTemp3._value,\
                                        self._ControllerTemp4._value, self._ControllerTemp5._value, self._ControllerTemp6._value,\
                                        self._MotorTemp._value, self._PhaseCurrentA._value, self._PhaseCurrentB._value, self._PhaseCurrentC._value, self._MotorTorque._value,\
                                        \
                                    \
                                        self._MotorVector1._value, self._MotorVector2._value, self._MotorVector3._value,\
                                        self._MotorVector4._value, self._MotorVector5._value, self._MotorVector6._value,\
                                        \
                                    \
                                        self._BatteryCurrent._value, self._BMS1Status._value,\
                                        \
                                    \
                                        self._BatPair1._Capacity._value,\
                                        self._BatPair1._Voltage1._value, self._BatPair1._Voltage2._value, self._BatPair1._Voltage3._value, self._BatPair1._Voltage4._value,\
                                        self._BatPair1._Voltage5._value, self._BatPair1._Voltage6._value, self._BatPair1._Voltage7._value, self._BatPair1._Voltage8._value,\
                                        \
                                    \
                                        self._BatPair2._Capacity._value,\
                                        self._BatPair2._Voltage1._value, self._BatPair2._Voltage2._value, self._BatPair2._Voltage3._value, self._BatPair2._Voltage4._value,\
                                        self._BatPair2._Voltage5._value, self._BatPair2._Voltage6._value, self._BatPair2._Voltage7._value, self._BatPair2._Voltage8._value,\
                                        \
                                    \
                                        self._BatPair3._Capacity._value,\
                                        self._BatPair3._Voltage1._value, self._BatPair3._Voltage2._value, self._BatPair3._Voltage3._value, self._BatPair3._Voltage4._value,\
                                        self._BatPair3._Voltage5._value, self._BatPair3._Voltage6._value, self._BatPair3._Voltage7._value, self._BatPair3._Voltage8._value,\
                                        \
                                    \
                                        self._BatTempA._Temp1._value, self._BatTempA._Temp2._value, self._BatTempA._Temp3._value, self._BatTempA._Temp4._value,\
                                        self._BatTempB._Temp1._value, self._BatTempB._Temp2._value, self._BatTempB._Temp3._value, self._BatTempB._Temp4._value,\
                                        self._BatTempC._Temp1._value, self._BatTempC._Temp2._value, self._BatTempC._Temp3._value, self._BatTempC._Temp4._value,\
                                        self._BatTempD._Temp1._value, self._BatTempD._Temp2._value, self._BatTempD._Temp3._value, self._BatTempD._Temp4._value,\
                                        self._BatTempE._Temp1._value, self._BatTempE._Temp2._value, self._BatTempE._Temp3._value, self._BatTempE._Temp4._value,\
                                        self._BatTempF._Temp1._value, self._BatTempF._Temp2._value, self._BatTempF._Temp3._value, self._BatTempF._Temp4._value,\
                                ])
        
    def _FileClose(self): #Close the file
        self._CSVFile.close()

    #Date and Time Variables
    _DateTime = -1
    def _DateTimeUpdate(self): #Update the date and time
        self._DateTime = datetime.datetime.now()
        
    #General Variables
    _EmergencyStop = _Data(0x010)
    _Distance = _Data(0x100)
    _Acceleration = _Data(0x102)
    _WindShieldWiper = _Data(0x118)

    #Driving Variables
    _Speed = _Data(0x101)
    _Throttle = _Data(0x113)
    _DriveMode = _Data(0x116)
    _Brake = _Data(0x117)
    _RPM = _Data(0x115)

    #Motor Variables
    _ControllerTemp1 = _Data(0x103)
    _ControllerTemp2 = _Data(0x104)
    _ControllerTemp3 = _Data(0x105)
    _ControllerTemp4 = _Data(0x106)
    _ControllerTemp5 = _Data(0x107)
    _ControllerTemp6 = _Data(0x108)
        #Assumes all values are being updated and an -1 is the temp,
        #and not non-updateing from default
    def _OverTemp_Controller(self):
        maxtemp = max(self._ControllerTemp1._value,self._ControllerTemp2._value,self._ControllerTemp3._value,\
                      self._ControllerTemp4._value,self._ControllerTemp5._value,self._ControllerTemp6._value)
        if maxtemp < self.ControllerTempCaution:
            return 0
        elif maxtemp < self.ControllerTempWarning:
            return 1
        else:
            return 2
    _MotorTemp = _Data(0x109)
    def _OverTemp_Motor(self):
        if self._MotorTemp._value < self.MotorTempCaution:
            return 0
        elif self._MotorTemp._value < self.MotorTempWarning:
            return 1
        else:
            return 2
    _PhaseCurrentA = _Data(0x110)
    _PhaseCurrentB = _Data(0x111)
    _PhaseCurrentC = _Data(0x112)
    _MotorTorque = _Data(0x114)
        #Motor Vector Variables Maybe not used
    _MotorVector1 = _Data(0x3B0)
    _MotorVector2 = _Data(0x3C0)
    _MotorVector3 = _Data(0x3D0)
    _MotorVector4 = _Data(0x3E0)
    _MotorVector5 = _Data(0x3F0)
    _MotorVector6 = _Data(0x400)
    
    #Battery Variables
    _BatteryCurrent = _Data(0x121)
    _BMS1Status = _Data(0x188)
    #ID Refferance          (CapID, V1ID,  V2ID,  V3ID,  V4ID,  V5ID,  V6ID,  V7ID,  V8ID,  T1ID,  T2ID,  T3ID,  T4ID,  T5ID,  T6ID,  T7ID,  T8ID):
    _BatPair1 = _BatteryPair(0x134, 0x135, 0x136, 0x137, 0x138, 0x139, 0x140, 0x141, 0x142)
    _BatPair2 = _BatteryPair(0x143, 0x144, 0x145, 0x146, 0x147, 0x148, 0x149, 0x150, 0x151)
    _BatPair3 = _BatteryPair(0x152, 0x153, 0x154, 0x155, 0x156, 0x157, 0x158, 0x159, 0x160)
    _BatTempA = _BatteryTemp(0x122, 0x123, 0x128, 0x129)
    _BatTempB = _BatteryTemp(0x130, 0x131, 0x132, 0x133) 
    _BatTempC = _BatteryTemp(0x124, 0x125, 0x161, 0x162) 
    _BatTempD = _BatteryTemp(0x163, 0x164, 0x165, 0x166) 
    _BatTempE = _BatteryTemp(0x126, 0x127, 0x167, 0x168) 
    _BatTempF = _BatteryTemp(0x169, 0x170, 0x171, 0x172)
        #Assumes all values are being updated and an -1 is the temp,
        #and not non-updateing from default
    def _OverTemp_Battery(self):
        maxtemp = max(self._BatTempA._HighestTemp(),self._BatTempB._HighestTemp(),self._BatTempC._HighestTemp(),\
                      self._BatTempD._HighestTemp(),self._BatTempE._HighestTemp(),self._BatTempF._HighestTemp())
        if maxtemp < self.BatteryTempCaution:
            return 0
        elif maxtemp < self.BatteryTempWarning:
            return 1
        else:
            return 2
        
    def _LowerCharge(self):
        mincharge =  min(self._BatPair1._Capacity._value,self._BatPair2._Capacity._value,self._BatPair3._Capacity._value)
        if mincharge == -1:
            return -1
        elif mincharge > self.BatteryChargeCaution:
            return 0
        elif mincharge > self.BatteryChargeWarning:
            return 1
        else:
            return 2

    
        
    