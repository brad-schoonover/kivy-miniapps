#Kivy Mini App #5 Screens and Screen management, FILES NEEDED: Screens.py, and screen.kv 
#The point of this app is show the very important screen manager, which allows us to have different screens and change between them
#From the last mini app we are going to use buttons to navigate between the screens. We are also going to introduce how to make 
#the app window full screen

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
#we import the screen, screenmanager, and Window. ScreenManager and screen are for changing and adding multiple screens
#and Window is for the purpose of the fullscreen app window.
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#The fullscreen value can be set to true but this conflicts when compiling for mobile devices so you set it to auto

Window.fullscreen = 'auto'

#Under this are the defining the 3 screens that are used in the app, noticed that they are not widgets,
#they are set as Screens and the management is done with the buttons in the kivy file and the screen manager in the app class.

class Screen1(Screen):
    pass

class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class screenApp(App):
    def build(self):
        
#We define a screenmanager and add the screens in like the add widgets we used in BasicShapes mini app, but 
#we also give the screen a callable name as screen1,screen2,screen3. We return sm like a parent widget.

        sm = ScreenManager()
        sm.add_widget(Screen1(name = 'screen1'))
        sm.add_widget(Screen2(name = 'screen2'))
        sm.add_widget(Screen3(name = 'screen3'))   
        return sm
if __name__ == '__main__':
    screenApp().run()
