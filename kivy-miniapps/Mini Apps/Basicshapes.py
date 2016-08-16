#Mini-App: Basic shapes, widget management, and Kivy file.FILES NEEDED: basicshapes.kv
#The goal of this app is to show how to create the basic shapes you will need to design in Kivy.
#Also to give the user a look into the kivy file denoted as basicshapes.kv, this file is needed in the same folder
#as the Basicshapes.py file for this to work.
#I will also go over again the way you have to go about making the app window like the first app example

#Below importing the proper kivy functions from the kivy library. 
#To accurately find where and what to input for the function you want to import,
#consult Kivy API at http://kivy.org/docs/api-kivy.html

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, Triangle
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager

#I am creating classes below that build a reference widget that I use to define graphics in the kv file.
#Three (Rectangle1, Triangle1, and Line1) I put a pass and do everything in the kv file, the other (Circle1) I will use a numerical property to 
#manipulate context instructions (in this case color) into variables that we could potentially use for graphic manipulation.

class Rectangle1(Widget):
    pass

class Circle1(Widget):

#setting these variables as a numerical property for them to be used in the kv file as the rgb color code
#for the rgb color codes the value has to be between 0 an 1 but can have many decimal points for more control of the color.
  
    rC = NumericProperty(0)
    gC = NumericProperty(1)
    bC = NumericProperty(0.5)
        
class Triangle1(Widget):
    pass

class Line1(Widget):
    pass

#We create a widget Main to add the all the other widgets in it and return at the end of the build definition, 
#which is what shows up in the app window when running the program.
    
class Main(Widget):
    pass

class basicshapesApp(App):
    
#This build definition gives what the BasicshapeApp will return when the program is called on, which we define as main.
#The Main, Rectangle1, Triangle1, Line1, Circle1 widget are given variable names to be easier to work with. 
    
    def build(self):
        Rect = Rectangle1()
        Tri = Triangle1()
        Lin = Line1()
        Cir = Circle1()
        main = Main()
        main.add_widget(Rect)
        main.add_widget(Tri)
        main.add_widget(Lin)
        main.add_widget(Cir)
        return main
#Below is the statements that allows the App to run when the program is called upon. The App name and the Kv file name
#are important to running the App with the graphics defined in the Kv file. Kivy searches for the Kv file that is in the same folder with
#the same name as the App but in lower case and with out the word App at the end. Example: this App is called BasicShapesApp, and the Kv file is basicshape.kv
#so Kivy can grab the kv file as soon as the App starts to run with the same name.
    
if __name__ == '__main__':
    basicshapesApp().run()
