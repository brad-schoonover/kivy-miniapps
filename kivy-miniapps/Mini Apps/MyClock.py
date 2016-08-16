import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty

#The class below is defined as a Boxlayout imported from the kivy language. With the date, hours, minutes and seconds defined as
#into string properties.

class MyClock(BoxLayout):
    hours = StringProperty()
    minutes = StringProperty()
    seconds = StringProperty()

#This update definition takes the date and time from the computer and splits it in to the hours, minutes, and seconds.
#These will be displayed in the app using the kivy language.

    def update(self, dt):
        delta = datetime.datetime.now()
        date = str(delta).split(', ')[0]
        hourstring = date.split(' ')[1]
        self.hours = hourstring.split(':')[0]
        self.minutes = hourstring.split(':')[1]
        self.seconds = hourstring.split(':')[2].split('.')[0]
        
#The mapp class takes our app clock and updates it every second the app is running using the the kivy clock function.

class myclockApp(App):
    def build(self):
        apptime = MyClock()
        Clock.schedule_interval(apptime.update, 1.0)
        return apptime


if __name__=='__main__':
    myclockApp().run()