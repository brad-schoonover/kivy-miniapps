#Kivy Mini App #6| Misc Widgets     Required files: MiscWigdets.py and miscwidgets.py  Sources: Kivy ShowCase
#The point of this app is show how to implement the screen manager from the last mini app and to demonstrate the functions of 
#checkboxes, dropdowns, sliders, and switches in python and in kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch

#We will show two ways to make the drop down which involves one being created in python and another created in the Kivy file.
#Below this is the class CustomDropDown is to provide a class to design the kivy dropdown menu 

class CustomDropDown(DropDown):
    pass 


class DropDowns(Screen):

#top_layout is a layout defined in the .kv file so for us to use it here we must give it an object property
    
    top_layout = ObjectProperty(None)

#to create the drop down in python we nmust set up this Init definition to create it, it also to apply the kivy dropdown to the screen

    def __init__(self, *args, **kwargs):
        super(DropDowns, self).__init__(*args, **kwargs)

#This is the applying of the kivy dropdown to the screen

        self.drop_down = CustomDropDown()

#here we create a DropDown object and a set of options for the buttons in the drop menu

        dropdown = DropDown()
        options = ['Settings', 'Import', 'Help', 'Quit']
        
#Using a for loop we make a button with the text in each item in the options list and assign them to the dropdown when the main button is pressed 
        
        for i in options:
            
# when adding widgets, we need to specify the height manually, so size_hint_y = None
#  so the dropdown can calculate the area it needs.
            
            btn = Button(text='%r' % i, size_hint_y=None, height=30)

#This selects the btn on the release of the btn

            btn.bind(on_release=lambda btn: dropdown.select(btn.text))

# then add the button inside the dropdown when the main button is pressed
            
            dropdown.add_widget(btn)

# create a big main button
        
        mainbutton = Button(text='DropDown_Py', size_hint=(1, 1)) 

# show the dropdown menu when the main button is released 
        
        mainbutton.bind(on_release=dropdown.open)

# This takes the selection in the dropdown list and assign the data to the button text.
        
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        
#Finally We add it to the top_layout so it will be positioned at the top of the screen.      

        self.top_layout.add_widget(mainbutton)

#Creating the CheckBoxes screen and the rest of it is defined in kivy

class CheckBoxes(Screen):
    pass

#Creating the Sliders screen and the rest of it is defined in kivy

class Sliders(Screen):
    pass

#Creating the Switches screen and the rest of it is defined in kivy

class Switches(Screen):
    pass

class MiscWidgetsApp(App):
    def build(self):
        
#like in the last MiniApp we add the the screens in to the screen manager to change between them
        
        sm = ScreenManager()
        sm.add_widget(DropDowns(name = 'drop'))
        sm.add_widget(CheckBoxes(name = 'check'))
        sm.add_widget(Sliders(name = 'slide'))
        sm.add_widget(Switches(name = 'switch'))
        return sm
    
if __name__ == '__main__':
    MiscWidgetsApp().run()