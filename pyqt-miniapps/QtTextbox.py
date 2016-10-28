import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
 
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Qt TextBox')
 
# Textbox creation with a LineEdit with the win widget
textbox = QLineEdit(win)

#Positions text box in the win widget

textbox.move(20, 20)

#sizes the text box

textbox.resize(40,40)
 
# Sizes the win window
win.resize(320, 150)
 
# Creates a button that will change the text above
Autobutton = QPushButton('Auto', win)

#positions the button in the widget

Autobutton.move(20,80)
 
# Uses pyqt slot to create the definition "on_click" to change the text in the text box to "On." or "Off."
@pyqtSlot()
def on_click():
    
    if textbox.text() != "On.":
        textbox.setText("On.")
        
    else:
        textbox.setText("Off.")
 
# Under the event of a clicked button it runs on_click
Autobutton.clicked.connect(on_click)
 
win.show()
app.exec_()