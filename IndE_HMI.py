import sys
import DataLog
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.core.window import Window
Window.maximize() #Maximize the window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty, ColorProperty
)
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


DataLog_ = DataLog._Datalog()
Red_ =   (1, 0, 0, 1)
Green_ = (0, 1, 0, 1)
Blue_ =  (0, 0, 1, 1)

class HomeScreen(Screen):
    pass

class IndE_HMI_Manager(ScreenManager):
    pass

class Indicator(Widget):
    state = False
    color = ColorProperty()
    def update(self, dt):
        if self.state == True:
            self.color = Red_
        else:
            self.color = Green_

class IndE_Display(Widget):
    emergancyindicator = ObjectProperty(None)
    timestring = StringProperty()
    datestring = StringProperty()

    def update(self, dt):
        DataLog_._DateTimeUpdate()
        self.timestring = DataLog_._DateTime.strftime("%H:%M")
        self.datestring = DataLog_._DateTime.strftime("%Y/%m/%d")
        self.emergancyindicator.state = DataLog_._EmergencyStop


class IndE_DisplayApp(App):

    def build(self):
        HMI = IndE_Display()
        Clock.schedule_interval(HMI.update, 1.0/60.0)
        return IndE_HMI_Manager(transition=NoTransition())
    
#Run the app
if __name__ == '__main__':
    IndE_DisplayApp().run()








