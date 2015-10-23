from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.app import App
import random
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import (Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color

class SampleWidget(FloatLayout):
	colour= ObjectProperty([1,1,0,1])
	def __init__(self, **kwargs):
		super(SampleWidget,self).__init__(**kwargs)	
		
		with self.canvas.after:
			Color(1,1,0,1)
			Rectangle(pos=(0,100), size=(100,100))
			Ellipse(pos=(0,100),size=(100,2 00))
			Line(points=[200,0,400,200, 200, 200], close=True, width=3)
			

	def sample(self,*args):
		color= [random.random() for i in range(3)] + [1]
		self.colour=color

	

class mykivy(App):
	def build(self):
		return SampleWidget()

if __name__ == "__main__":
	mykivy().run()
