import csv
import datetime

class _Data:
    def __init__(self, ID):
        self._ID = ID
    
    _ID = -1
    _value = -1

class _Battery:
    def __init__(self, CapID, V1ID, V2ID, V3ID, V4ID, V5ID, V6ID, V7ID, V8ID, T1ID, T2ID):
        self._Capacity = _Data(CapID)
        self._Voltage1 = _Data(V1ID)
        self._Voltage2 = _Data(V2ID)
        self._Voltage3 = _Data(V3ID)
        self._Voltage4 = _Data(V4ID)
        self._Voltage5 = _Data(V5ID)
        self._Voltage6 = _Data(V6ID)
        self._Voltage7 = _Data(V7ID)
        self._Voltage8 = _Data(V8ID)
        self._Temp1 = _Data(T1ID)
        self._Temp2 = _Data(T2ID)


class _Datalog:
   
    #Data Exporting Variables and Functions
    _filename = -1
    _CSVFile = -1
    _CSVWriter = -1
    def _FileOpen(self, filename): #Opens a new file and put the headers
        self._filename = filename
        self._CSVFile = open(self._filename, 'w', newline='')
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
                                        'Battery Current', 'BMS 1 Status', 'BMS 2 Status',\
                                        \
                                    \
                                        'Battery 1 Capacity', 'Battery 1 Temp 1', 'Battery 1 Temp 2',\
                                        'Battery 1 Voltage 1', 'Battery 1 Voltage 2', 'Battery 1 Voltage 3', 'Battery 1 Voltage 4',\
                                        'Battery 1 Voltage 5', 'Battery 1 Voltage 6', 'Battery 1 Voltage 7', 'Battery 1 Voltage 8',\
                                        \
                                    \
                                        'Battery 2 Capacity', 'Battery 2 Temp 1', 'Battery 2 Temp 2',\
                                        'Battery 2 Voltage 1', 'Battery 2 Voltage 2', 'Battery 2 Voltage 3', 'Battery 2 Voltage 4',\
                                        'Battery 2 Voltage 5', 'Battery 2 Voltage 6', 'Battery 2 Voltage 7', 'Battery 2 Voltage 8',\
                                        \
                                    \
                                        'Battery 3 Capacity', 'Battery 3 Temp 1', 'Battery 3 Temp 2',\
                                        'Battery 3 Voltage 1', 'Battery 3 Voltage 2', 'Battery 3 Voltage 3', 'Battery 3 Voltage 4',\
                                        'Battery 3 Voltage 5', 'Battery 3 Voltage 6', 'Battery 3 Voltage 7', 'Battery 3 Voltage 8',\
                                        \
                                    \
                                        'Battery 4 Capacity', 'Battery 4 Temp 1', 'Battery 4 Temp 2',\
                                        'Battery 4 Voltage 1', 'Battery 4 Voltage 2', 'Battery 4 Voltage 3', 'Battery 4 Voltage 4',\
                                        'Battery 4 Voltage 5', 'Battery 4 Voltage 6', 'Battery 4 Voltage 7', 'Battery 4 Voltage 8',\
                                        \
                                    \
                                        'Battery 5 Capacity', 'Battery 5 Temp 1', 'Battery 5 Temp 2',\
                                        'Battery 5 Voltage 1', 'Battery 5 Voltage 2', 'Battery 5 Voltage 3', 'Battery 5 Voltage 4',\
                                        'Battery 5 Voltage 5', 'Battery 5 Voltage 6', 'Battery 5 Voltage 7', 'Battery 5 Voltage 8',\
                                        \
                                    \
                                        'Battery 6 Capacity', 'Battery 6 Temp 1', 'Battery 6 Temp 2',\
                                        'Battery 6 Voltage 1', 'Battery 6 Voltage 2', 'Battery 6 Voltage 3', 'Battery 6 Voltage 4',\
                                        'Battery 6 Voltage 5', 'Battery 6 Voltage 6', 'Battery 6 Voltage 7', 'Battery 6 Voltage 8'\
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
                                        self._BatteryCurrent._ID, self._BMS1Status._ID, self._BMS2Status._ID,\
                                        \
                                    \
                                        self._Battery1._Capacity._ID, self._Battery1._Temp1._ID, self._Battery1._Temp2._ID,\
                                        self._Battery1._Voltage1._ID, self._Battery1._Voltage2._ID, self._Battery1._Voltage3._ID, self._Battery1._Voltage4._ID,\
                                        self._Battery1._Voltage5._ID, self._Battery1._Voltage6._ID, self._Battery1._Voltage7._ID, self._Battery1._Voltage8._ID,\
                                        \
                                    \
                                        self._Battery2._Capacity._ID, self._Battery2._Temp1._ID, self._Battery2._Temp2._ID,\
                                        self._Battery2._Voltage1._ID, self._Battery2._Voltage2._ID, self._Battery2._Voltage3._ID, self._Battery2._Voltage4._ID,\
                                        self._Battery2._Voltage5._ID, self._Battery2._Voltage6._ID, self._Battery2._Voltage7._ID, self._Battery2._Voltage8._ID,\
                                        \
                                    \
                                        self._Battery3._Capacity._ID, self._Battery3._Temp1._ID, self._Battery3._Temp2._ID,\
                                        self._Battery3._Voltage1._ID, self._Battery3._Voltage2._ID, self._Battery3._Voltage3._ID, self._Battery3._Voltage4._ID,\
                                        self._Battery3._Voltage5._ID, self._Battery3._Voltage6._ID, self._Battery3._Voltage7._ID, self._Battery3._Voltage8._ID,\
                                        \
                                    \
                                        self._Battery4._Capacity._ID, self._Battery4._Temp1._ID, self._Battery4._Temp2._ID,\
                                        self._Battery4._Voltage1._ID, self._Battery4._Voltage2._ID, self._Battery4._Voltage3._ID, self._Battery4._Voltage4._ID,\
                                        self._Battery4._Voltage5._ID, self._Battery4._Voltage6._ID, self._Battery4._Voltage7._ID, self._Battery4._Voltage8._ID,\
                                        \
                                    \
                                        self._Battery5._Capacity._ID, self._Battery5._Temp1._ID, self._Battery5._Temp2._ID,\
                                        self._Battery5._Voltage1._ID, self._Battery5._Voltage2._ID, self._Battery5._Voltage3._ID, self._Battery5._Voltage4._ID,\
                                        self._Battery5._Voltage5._ID, self._Battery5._Voltage6._ID, self._Battery5._Voltage7._ID, self._Battery5._Voltage8._ID,\
                                        \
                                    \
                                        self._Battery6._Capacity._ID, self._Battery6._Temp1._ID, self._Battery6._Temp2._ID,\
                                        self._Battery6._Voltage1._ID, self._Battery6._Voltage2._ID, self._Battery6._Voltage3._ID, self._Battery6._Voltage4._ID,\
                                        self._Battery6._Voltage5._ID, self._Battery6._Voltage6._ID, self._Battery6._Voltage7._ID, self._Battery6._Voltage8._ID\
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
                                        self._BatteryCurrent._value, self._BMS1Status._value, self._BMS2Status._value,\
                                        \
                                    \
                                        self._Battery1._Capacity._value, self._Battery1._Temp1._value, self._Battery1._Temp2._value,\
                                        self._Battery1._Voltage1._value, self._Battery1._Voltage2._value, self._Battery1._Voltage3._value, self._Battery1._Voltage4._value,\
                                        self._Battery1._Voltage5._value, self._Battery1._Voltage6._value, self._Battery1._Voltage7._value, self._Battery1._Voltage8._value,\
                                        \
                                    \
                                        self._Battery2._Capacity._value, self._Battery2._Temp1._value, self._Battery2._Temp2._value,\
                                        self._Battery2._Voltage1._value, self._Battery2._Voltage2._value, self._Battery2._Voltage3._value, self._Battery2._Voltage4._value,\
                                        self._Battery2._Voltage5._value, self._Battery2._Voltage6._value, self._Battery2._Voltage7._value, self._Battery2._Voltage8._value,\
                                        \
                                    \
                                        self._Battery3._Capacity._value, self._Battery3._Temp1._value, self._Battery3._Temp2._value,\
                                        self._Battery3._Voltage1._value, self._Battery3._Voltage2._value, self._Battery3._Voltage3._value, self._Battery3._Voltage4._value,\
                                        self._Battery3._Voltage5._value, self._Battery3._Voltage6._value, self._Battery3._Voltage7._value, self._Battery3._Voltage8._value,\
                                        \
                                    \
                                        self._Battery4._Capacity._value, self._Battery4._Temp1._value, self._Battery4._Temp2._value,\
                                        self._Battery4._Voltage1._value, self._Battery4._Voltage2._value, self._Battery4._Voltage3._value, self._Battery4._Voltage4._value,\
                                        self._Battery4._Voltage5._value, self._Battery4._Voltage6._value, self._Battery4._Voltage7._value, self._Battery4._Voltage8._value,\
                                        \
                                    \
                                        self._Battery5._Capacity._value, self._Battery5._Temp1._value, self._Battery5._Temp2._value,\
                                        self._Battery5._Voltage1._value, self._Battery5._Voltage2._value, self._Battery5._Voltage3._value, self._Battery5._Voltage4._value,\
                                        self._Battery5._Voltage5._value, self._Battery5._Voltage6._value, self._Battery5._Voltage7._value, self._Battery5._Voltage8._value,\
                                        \
                                    \
                                        self._Battery6._Capacity._value, self._Battery6._Temp1._value, self._Battery6._Temp2._value,\
                                        self._Battery6._Voltage1._value, self._Battery6._Voltage2._value, self._Battery6._Voltage3._value, self._Battery6._Voltage4._value,\
                                        self._Battery6._Voltage5._value, self._Battery6._Voltage6._value, self._Battery6._Voltage7._value, self._Battery6._Voltage8._value\
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
    _MotorTemp = _Data(0x109)
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
    _BMS2Status = _Data(0x189)
    #ID Refferance      (CapID, V1ID,  V2ID,  V3ID,  V4ID,  V5ID,  V6ID,  V7ID,  V8ID,  T1ID, T2ID):
    _Battery1 = _Battery(0x134, 0x135, 0x136, 0x137, 0x138, 0x139, 0x140, 0x141, 0x142, 0x122, 0x123)
    _Battery2 = _Battery(0x143, 0x144, 0x145, 0x146, 0x147, 0x148, 0x149, 0x150, 0x151, 0x124, 0x125)
    _Battery3 = _Battery(0x152, 0x153, 0x154, 0x155, 0x156, 0x157, 0x158, 0x159, 0x160, 0x126, 0x127)
    _Battery4 = _Battery(0x161, 0x162, 0x163, 0x164, 0x165, 0x166, 0x167, 0x168, 0x169, 0x128, 0x129)
    _Battery5 = _Battery(0x170, 0x171, 0x172, 0x173, 0x174, 0x175, 0x176, 0x177, 0x178, 0x130, 0x131)
    _Battery6 = _Battery(0x179, 0x180, 0x181, 0x182, 0x183, 0x184, 0x185, 0x186, 0x187, 0x132, 0x133)
       
        
    