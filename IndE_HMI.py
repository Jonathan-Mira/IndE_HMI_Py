import DataLog
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.maximize() #Maximize the window
Window.clearcolor = (0, 0.75, 0.75, 1) #Set the background color to IndE Blue
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, StringProperty, ColorProperty
)


DataLog_ = DataLog._Datalog()
White_    = (1, 1, 1, 1)
Black_    = (0, 0, 0, 1)
Red_      = (1, 0, 0, 1)
Green_    = (0, 1, 0, 1)
Blue_     = (0, 0, 1, 1)
Yellow_   = (1, 1, 0, 1)
IndE_Blue = (0, 0.75, 0.75, 1)
IndE_Grey = (0.2, 0.7, 0.7, 1)


class IndE_Display(Widget):
    timestring = StringProperty()
    datestring = StringProperty()
    page = NumericProperty(0)
    pagestring = StringProperty("Home")
    Temp_status = ColorProperty(Blue_)
    Battery_status = ColorProperty(Blue_)
    Emergancy_status = ColorProperty(Blue_)
    Record_status = ColorProperty(IndE_Blue)
    Recording = False
    textcolor = ColorProperty(Black_)
    but1string = StringProperty("Record")
    but2string = StringProperty("Km/h")

    #Home Screen 
    speedswitch = False
    speedstring = StringProperty("RPM")
    DataLog_._Speed._value = 120
    DataLog_._RPM._value = 4000
    throttlestring = StringProperty("100%")
    DataLog_._Throttle._value = 100
    Break_status = ColorProperty(Blue_)
    Wind_Sheild_status = ColorProperty(Blue_)
    Dr_Mode_Park_status = ColorProperty(Blue_)
    Dr_Mode_Rev_status = ColorProperty(Blue_)
    Dr_Mode_Slow_status = ColorProperty(Blue_)
    Dr_Mode_Drive_status = ColorProperty(Blue_)
    DataLog_._DriveMode._value = -1

    DataLog_._WindShieldWiper._value = False
    DataLog_._Brake._value = False

    #Battery Screen
    currentstring = StringProperty("Current: ###.#A")
    DataLog_._BatteryCurrent._value = 100.0
    BMS_status = ColorProperty(Blue_)
    MaxTempBatAstring = StringProperty("A00")
    MaxTempBatBstring = StringProperty("B00")
    MaxTempBatCstring = StringProperty("C00")
    MaxTempBatDstring = StringProperty("D00")
    MaxTempBatEstring = StringProperty("E00")
    MaxTempBatFstring = StringProperty("F00")
    LowChargestring = StringProperty("100%")

    #Motor Screen
    MSspeedstring = StringProperty()
    MSrotationstring = StringProperty()
    motortempstring = StringProperty()
    motortorquestring = StringProperty()
    motorcontrollertemp1string = StringProperty()
    motorcontrollertemp2string = StringProperty()
    motorcontrollertemp3string = StringProperty()
    motorcontrollertemp4string = StringProperty()
    motorcontrollertemp5string = StringProperty()
    motorcontrollertemp6string = StringProperty()
    phaseAcurrentstring = StringProperty("100")
    phaseBcurrentstring = StringProperty("100")
    phaseCcurrentstring = StringProperty("100")

    #Setting Screen
    filenamestring = StringProperty()


    def update(self, dt):
        DataLog_._DateTimeUpdate()
        self.timestring = DataLog_._DateTime.strftime("%H:%M")
        self.datestring = DataLog_._DateTime.strftime("%Y/%m/%d")
        if self.Recording:
            DataLog_._FileWrite()
        
        if DataLog_._EmergencyStop._value:
            self.Emergancy_status = Green_
        else:
            self.Emergancy_status = Red_
        
        match max(DataLog_._OverTemp_Controller(),DataLog_._OverTemp_Battery(),DataLog_._OverTemp_Motor()):
            case 0:
                self.Temp_status = Green_
            case 1:
                self.Temp_status = Yellow_
            case 2:
                self.Temp_status = Red_
            case _:
                self.Temp_status = Blue_

        match DataLog_._LowerCharge():
            case 0:
                self.Battery_status = Green_
            case 1:
                self.Battery_status = Yellow_
            case 2:
                self.Battery_status = Red_
            case _:
                self.Battery_status = Blue_

        if DataLog_._Brake._value:
            self.Break_status = Green_
        else:
            self.Break_status = IndE_Grey

        if DataLog_._WindShieldWiper._value:
            self.Wind_Sheild_status = Green_
        else:
            self.Wind_Sheild_status = IndE_Grey

        #Home Screen
        if self.speedswitch:
            self.speedstring = str(DataLog_._Speed._value) + " Km/h"
        else:
            self.speedstring = str(DataLog_._RPM._value) + " RPM"
        self.throttlestring = str(DataLog_._Throttle._value) + "%"
        if DataLog_._DriveMode._value == 0:
            self.Dr_Mode_Park_status = Black_
            self.Dr_Mode_Rev_status = White_
            self.Dr_Mode_Slow_status = White_
            self.Dr_Mode_Drive_status = White_
        elif DataLog_._DriveMode._value == 1:
            self.Dr_Mode_Park_status = White_
            self.Dr_Mode_Rev_status = Black_
            self.Dr_Mode_Slow_status = White_
            self.Dr_Mode_Drive_status = White_
        elif DataLog_._DriveMode._value == 2:
            self.Dr_Mode_Park_status = White_
            self.Dr_Mode_Rev_status = White_
            self.Dr_Mode_Slow_status = Black_
            self.Dr_Mode_Drive_status = White_
        elif DataLog_._DriveMode._value == 3:
            self.Dr_Mode_Park_status = White_
            self.Dr_Mode_Rev_status = White_
            self.Dr_Mode_Slow_status = White_
            self.Dr_Mode_Drive_status = Black_
        else:
            self.Dr_Mode_Park_status = Red_
            self.Dr_Mode_Rev_status = Red_
            self.Dr_Mode_Slow_status = Red_
            self.Dr_Mode_Drive_status = Red_

        #Battery Screen
        self.currentstring = str(DataLog_._BatteryCurrent._value) + "A"
        self.MaxTempBatAstring = str(DataLog_._BatTempA._HighestTemp())
        self.MaxTempBatBstring = str(DataLog_._BatTempB._HighestTemp())
        self.MaxTempBatCstring = str(DataLog_._BatTempC._HighestTemp())
        self.MaxTempBatDstring = str(DataLog_._BatTempD._HighestTemp())
        self.MaxTempBatEstring = str(DataLog_._BatTempE._HighestTemp())
        self.MaxTempBatFstring = str(DataLog_._BatTempF._HighestTemp())
        self.LowChargestring = str(min(DataLog_._BatPair1._Capacity._value,DataLog_._BatPair2._Capacity._value,DataLog_._BatPair3._Capacity._value)) +"%"
        if DataLog_._BMS1Status._value:
            self.BMS_status = Green_
        else:
            self.BMS_status = Red_

        #Motor Screen
        self.MSspeedstring = str(DataLog_._Speed._value) + " Km/h"
        self.MSrotationstring = str(DataLog_._RPM._value) + " RPM"
        self.motortempstring = str(DataLog_._MotorTemp._value) + "°C"
        self.motortorquestring = str(DataLog_._MotorTorque._value) + "Nm"
        self.motorcontrollertemp1string = str(DataLog_._ControllerTemp1._value)
        self.motorcontrollertemp2string = str(DataLog_._ControllerTemp2._value)
        self.motorcontrollertemp3string = str(DataLog_._ControllerTemp3._value)
        self.motorcontrollertemp4string = str(DataLog_._ControllerTemp4._value)
        self.motorcontrollertemp5string = str(DataLog_._ControllerTemp5._value)
        self.motorcontrollertemp6string = str(DataLog_._ControllerTemp6._value)
        self.phaseAcurrentstring = str(DataLog_._PhaseCurrentA._value) 
        self.phaseBcurrentstring = str(DataLog_._PhaseCurrentB._value) 
        self.phaseCcurrentstring = str(DataLog_._PhaseCurrentC._value) 

        #Setting Screen
    
    def record(self):
        self.Recording = not self.Recording
        if self.Recording:
            DataLog_._FileOpen(self.filenamestring)
            self.Record_status = Green_
        else:
            DataLog_._FileClose()
            self.Record_status = IndE_Blue

    def nextpage(self):
        self.page += 1
        if self.page > 3:
            self.page = -1
        self.update_Button_String()
        
    def prevpage(self):
        self.page -= 1
        if self.page < -1:
            self.page = 3
        self.update_Button_String()

    def update_Button_String(self):
        match self.page:
            case -1: 
                self.but1string = "Record"
                self.but2string = ""
                self.pagestring = "Setting"
            case 0:
                self.but1string = "Record"
                if self.speedswitch:
                    self.but2string = "RPM"
                else:
                    self.but2string = "km/h"
                self.pagestring = "Home"
            case 1:
                self.but1string = ""
                self.but2string = ""
                self.pagestring = "Battery"
            case 2:
                self.but1string = "Home"
                self.but2string = "Toggle"
                self.pagestring = "Motor"
            case 3:
                self.but1string = "Home"
                self.but2string = ""
                self.pagestring = "Misc"
            case _:
                print(self.page)

    def but1(self):
        match self.page:
            case -1:
                self.record()
            case 0:
                self.record()
            case 2:
                self.page = 0
                self.update_Button_String()
            case 3:
                self.page = 0
                self.update_Button_String()
            case _:
                print(self.page)

    def but2(self):
        match self.page:
            case 0:
                self.speedswitch = not self.speedswitch
                self.update_Button_String()
            case _:
                print(self.page)
    
    def filenameupdate(self):
        self.filenamestring = self.ids.filenameinput.text
        


class IndE_DisplayApp(App):

    def build(self):
        HMI = IndE_Display()
        Clock.schedule_interval(HMI.update, 1.0/60.0)
        return HMI
    
#Run the app
if __name__ == '__main__':
    IndE_DisplayApp().run()
