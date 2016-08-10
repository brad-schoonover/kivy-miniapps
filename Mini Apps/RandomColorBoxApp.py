#Kivy Mini App #8 Random Color generation, FILES NEEDED: RandomColorBoxApp.py, and randomcolorbox.kv 
#The point of this app is show the how to generate random colors, which allows us generate random colors 
#to make a particular section of screen look flashy
#From the last mini app we are going to use clock for time intervals of colors to change 
#and random package to generate random numbers 
from kivy.app import App
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
import random

class RandomColorBox(Widget):
    cred = NumericProperty(0)
    cgreen = NumericProperty(0)
    cblue = NumericProperty(0)



    def __init__ (s, **kwargs):
        super(RandomColorBox, s).__init__(**kwargs)
        s.bind(cred=s.redraw)

    def redraw(s, * args):
        with s.canvas:
            Color(s.cred,1,1,1)
#this definition would generate random numbers for Color function
    def ChangeBoxColor(self, color):
        self.canvas.clear()
        self.cred = random.randint(0,9)
        self.cgreen = random.randint(0,9)
        self.cblue = random.randint(0,9)

        self.canvas.ask_update()

#Below definition would trigger a call to change color for every 3 seconds.
    def startChangingBox(self,interval=3):
        Clock.schedule_interval(self.ChangeBoxColor, interval)


class RandomColorBoxApp(App):
    rcb = None

    def build(self):
        rcb = RandomColorBox()
        rcb.startChangingBox()

        return rcb

if __name__ == '__main__':
    RandomColorBoxApp().run()
