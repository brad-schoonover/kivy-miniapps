#Mini App 7: Alarms, Alarm buttons. Required Files: alarm.kv, RedAlert.wav API Ref: http://kivy.org/docs/api-kivy.core.audio.html
#This App will show how to create a button that if pressed it plays a looping sound, in this case an alarm.
#there is also a off button to to stop the sound. Like always the button handling is done in the kivy file.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

#We import the soundloader from kivy.core to manage and load the sound files we want to use

from kivy.core.audio import SoundLoader

#Below here we create the alarm class to house the alarm sound and the button to turn it on and of in the kivy file. 

class AlarmButton(Widget):
    
#we create this definition to start the alarm that we call upon when the button is pressed.

    def start(self):
        
#we set sound to the soundloader.load('Whatever file you want'), where we loaded it from nd the length of the sound will be diplayed
#in the shell. we also activate the sound with sound.play() and let it loop setting loop to True.
        
        sound = SoundLoader.load('RedAlert.wav')
        print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        sound.play()
        sound.loop = True
 
#Creating the app and returns the AlarmButton widget.
        
class AlarmApp(App):
    def build(self):
        AB = AlarmButton()
        return AB
    
if __name__ == '__main__':
    AlarmApp().run()
        