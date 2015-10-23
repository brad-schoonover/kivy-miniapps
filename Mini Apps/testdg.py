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
import time 

class SampleWidget(FloatLayout):

	colo= [random.random() for i in range(3)] + [1]

	def __init__(self, **kwargs):
		super(SampleWidget,self).__init__(**kwargs)
		
		with self.canvas.before:
			Rectangle(pos=(100,100), size=(200,200))
					
class test(App):
	def build(self):
		return SampleWidget()

if __name__ == "__main__":
	test().run()
