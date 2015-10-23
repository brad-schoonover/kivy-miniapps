from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
#from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

class ScatterTextWidget(BoxLayout):
	def colorchange(self, *args):
		color=[random.random() for i in range(3)]+[2]
		label= self.ids['my1']
		label.color=color
class Dg(App):
        def build(self):
		return ScatterTextWidget()	
                

if __name__ == '__main__':
        Dg().run()

