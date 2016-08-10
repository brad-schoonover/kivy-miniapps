#MiniApp 1: The App window
#The goal of this app is to show how to create the app window in python and run a widget through it

#Below importing the proper kivy functions from the kivy library. 
#To accurately find where and what to input for the function you want to import,
#consult Kivy API at http://kivy.org/docs/api-kivy.html

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock

#This class is being defined as a widget so it can be returned at the app window. its definition __init__
#is initializing the build of the shape and defines a canvas in which to draw or ellipse on.
#With Kivy we wont have to use this easy to mess up and clunky way of making a shape with the init definition.

class Shape(Widget):
    def __init__(self, **kwargs):
        super(Shape, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, .4, mode='rgb')
            Ellipse(pos=(self.center_x, self.center_y), size=(200, 100))

#This class is created as an app, that will create an app window and display what is returned though in
#This build definition gives what the workapp will return when the program is called on, in this case
#the Shape widget with the variable Sh given to it.

class workapp(App):
    def build(self):
        Sh = Shape()
        return Sh
    
if __name__ == '__main__':
    workapp().run()
#Above is the statement that allows the App to run when the program is called upon. When the name of this file is
#ran the program with run the app function