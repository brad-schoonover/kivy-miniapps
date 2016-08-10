#MiniApp 2: The Kivy File
#The goal of this app is to show how to set up and design in the Kv file, and go back over initializing the app class

#Below importing the proper kivy functions from the kivy library. 
#To accurately find where and what to input for the function you want to import,
#consult Kivy API at http://kivy.org/docs/api-kivy.html

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

#The class below builds a reference widget that I refer to in the kv file, and i just pass everything to be defined in the other file 

class Shape(Widget):
    pass

class Other(Widget):
    pass

class Main(Widget):
    pass
#The class below creates the App window itself for the program to run through

class Kivyfileapp(App):
#This build definition gives what the KivyfileApp will return when the program is called on, with in the
#build we define Shape to be Sh for ease of use and to return at the end of the definition for the app
#window will actually show
    def build(self):
        main = Main()
        Sh = Shape()
        Ot = Other()
        main.add_widget(Sh)
        main.add_widget(Ot)
        return main
        
if __name__ == '__main__':
    Kivyfileapp().run()
    
#Above is the statement that allows the App to run when the program is called upon. The App name and the Kv file name
#are important to running the App with the graphics defined in the Kv file. Kivy searches for the Kv file that is in the same folder with
#the same name as the App but in lower case and with out the word App at the end. Example: this App class is called Kivyfileapp, and the Kv file is kivyfile.kv
#so Kivy can grab the kv file as soon as the App starts to run with the same name.