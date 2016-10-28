import sys
import os
from time import strftime
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


##Slider Code

class Communicate(QObject):
    
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
  
    def __init__(self):      
        super(BurningWidget, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]


    def setValue(self, value):

        self.value = value


    def paintEvent(self, e):
      
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
      
    def drawWidget(self, qp):
      
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10.0))


        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))

        if self.value >= 700:
            
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
            
        else:
            
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)


        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)

        j = 0

        for i in range(step, 10*step, step):
          
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1
        
       
### In App Time work in progress


#class myLCDNumber(QLCDNumber):
#    value = 0
#    @pyqtSlot()
#    def count(self):
#        self.display(self.value)
#        self.value = self.value+1

#class MyTimer(QWidget):
    
#    def __init__(self):
#        super(MyTimer, self).__init__()
#        self.update()
           
#    def update(self):
        
#        self.num = myLCDNumber()
#        self.num.display(0)
#        self.timer = QTimer(self)
#        self.timer.timeout.connect(self.num, count())
#        self.timer.start(1000)

#add minute and second clock that runs with computer time
         
class MyClock(QWidget):
    
    def __init__(self):
        super(MyClock, self).__init__()
        self.update()
        
    def update(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
        
        self.lcd = QLCDNumber(self)

        self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
    
    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
 
 #------------------------------Tab1-------------------------------------
        
class Tab1(QWidget):
    
    def __init__(self):
        super(Tab1, self).__init__()
        self.tablayout()
    
    def tablayout(self):       
#intializing the first layout for tab1
        Boxlayout = QVBoxLayout()
        
#Creates 3 buttons and add them to the layout and sets that layout to tab1        
        startButton = QPushButton("Start")
        setButton = QPushButton("Settings")
        pauseButton = QPushButton("Pause")
        Boxlayout.addWidget(startButton)
        Boxlayout.addWidget(setButton)
        Boxlayout.addWidget(pauseButton)
        self.setLayout(Boxlayout)

#-------------------------------Tab2-------------------------------------        
class Tab2(QWidget):
    
    def __init__(self):
        super(Tab2,self).__init__()
        self.tablayout()
    
    def tablayout(self):                
#Creates the textbox and button for the tab2 Layout and adds tem to Boxlayout2        
        textbox = QLineEdit(self)
        Autobutton = QPushButton('Auto', self)
        Boxlayout2 = QVBoxLayout()
        Boxlayout2.addWidget(textbox)
        Boxlayout2.addWidget(Autobutton)
        self.setLayout(Boxlayout2) 
        # Uses pyqt slot to create the definition "on_click" to change the text in the text box to "On." or "Off."
        @pyqtSlot()
        def on_click():
    
            if textbox.text() != "On.":
                textbox.setText("On.")
        
            else:
                textbox.setText("Off.")
 
# Under the event of a clicked button it runs on_click
        Autobutton.clicked.connect(on_click)
        
#--------------------------------------------Tab3----------------------------------                
class Tab3(QWidget):
    
    def __init__(self):
        super(Tab3,self).__init__()
        self.tab_layout()
        
    def tab_layout(self):
        
        boxlayout3 = QVBoxLayout()
        clock = MyClock()
#        time = MyTimer()
#        boxlayout3.addWidget(time)
        boxlayout3.addWidget(clock)
        self.setLayout(boxlayout3)
        
    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(0, 0, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130, 200, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250, 200, 90, 60)
        
class Tab4(QWidget):
    
    def __init__(self):
        super(Tab4,self).__init__()
        self.tablayout()
    
    def tablayout(self): 
        
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, 750)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()        
        self.wid = BurningWidget()
        self.c.updateBW[int].connect(self.wid.setValue)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        
    def changeValue(self, value):
             
        self.c.updateBW.emit(value)        
        self.wid.repaint()
                       
class OpenWindow(QMainWindow):

    def __init__(self):
        super(OpenWindow, self).__init__()
        self.initUI()

    def initUI(self):
#setting up the main layout for widget sizing guidelines
        frame = QFrame()
        self.setCentralWidget(frame)
        mainlayout = QHBoxLayout()
        frame.setLayout(mainlayout)
        
#Toolbar UI buttons, text, shortcut, and event creation
        exitBut = QAction('Exit', self)
        exitBut.setShortcut('Ctrl+X')
        exitBut.setStatusTip('Exit application')
        exitBut.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitBut)
        
#Creates the central tab widget and 3 tabs with in them
        tab_widget = QTabWidget(self)
        tab1 = Tab1()
        tab2 = Tab2()
        tab3 = Tab3()
        tab4 = Tab4()
        
        
#adds the tabs created to the tab_widget and titles them        
        tab_widget.addTab(tab1, "Tab1")
        tab_widget.addTab(tab2, "Tab2")
        tab_widget.addTab(tab3, "Tab3")
        tab_widget.addTab(tab4, "Tab4")

#adds the tabs to the mainlayout of the window and positions it in the window 
        mainlayout.addWidget(tab_widget)
        tab_widget.move(0, 30)
        
#Window Title and shows it
        self.setWindowTitle('Qt Tabs')
        self.show()

#defines main which runs on launch and intializes the application.
#also runs the open window
def main():
    app = QApplication(sys.argv)
    open = OpenWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
