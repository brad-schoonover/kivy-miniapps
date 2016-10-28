import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Importing Qt classes and system arguments
 
# Creates the PyQT application.
app = QApplication(sys.argv)
 
# QWidget is the base class of all user interface objects and widgets in PyQt4, and we set it as win.
win = QWidget()
 
# Setting window size
win.resize(320, 240)
 
# Settign window Title
win.setWindowTitle("Qt App Window")
 
# Causes the window to show on app start up
win.show()

# executes app on runing 
 
sys.exit(app.exec_())