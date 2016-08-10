#Mini App 4, Buttons FILES NEEDED: Buttons.py, buttons.kv, GetStartedButtonN.png, GetStartedButtonD.png
#The point of this app is to show you how to use buttons and some implementation of float and box layout. 
#It mostly takes place in the in the buttons.kv file.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

#Heres the import of the Button Widget

from kivy.uix.button import Button

#We initiate the Button class to be edited in the 

class Buttons(Widget):
    pass
    

class ButtonsApp(App):
    def build(self):
        But = Buttons()
        return But
    
if __name__ == '__main__':
    ButtonsApp().run()

#The bulk of this app is in the Kivy file.