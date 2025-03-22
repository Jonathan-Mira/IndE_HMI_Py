import sys
import csv
from enum import Enum
import DataLog
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.core.window import Window
Window.maximize() #Maximize the window
Window.clearcolor = (0, 0.75, 0.75, 1) #Set the background color to IndE Blue
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, ColorProperty
)


DataLog_ = DataLog._Datalog()
White_    = (1, 1, 1, 1)
Black_    = (0, 0, 0, 1)
Red_      = (1, 0, 0, 1)
Green_    = (0, 1, 0, 1)
Blue_     = (0, 0, 1, 1)
IndE_Blue = (0, 0.75, 0.75, 1)


class IndE_Display(Widget):
    timestring = StringProperty()
    datestring = StringProperty()
    page = NumericProperty(0)
    pagestring = StringProperty("Home")
    Temp_status = ColorProperty(Blue_)
    Battery_status = ColorProperty(Blue_)
    Emergancy_status = ColorProperty(Blue_)
    Record_status = ColorProperty(Blue_)
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



    def update(self, dt):
        DataLog_._DateTimeUpdate()
        self.timestring = DataLog_._DateTime.strftime("%H:%M")
        self.datestring = DataLog_._DateTime.strftime("%Y/%m/%d")
        if self.Recording:
            DataLog_._FileWrite()
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
        #self.LowChargestring = str(min(DataLog_._BatPair1._Capacity._value,DataLog_._BatPair2._Capacity._value,DataLog_._BatPair3._Capacity._value)) +"%"

            

        
        
    
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
        


class IndE_DisplayApp(App):

    def build(self):
        HMI = IndE_Display()
        Clock.schedule_interval(HMI.update, 1.0/60.0)
        return HMI
    
#Run the app
if __name__ == '__main__':
    IndE_DisplayApp().run()
