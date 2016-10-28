
import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
app = QApplication(sys.argv)       
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
win = QWidget()
 
# Creates a message box that appears before the window of the app opens with two button options.
Choices = QMessageBox.question(win, 'Message', "Is Kivy well documented?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
 # Adds text to the buttons in Choices as yes and no
 
if Choices == QMessageBox.Yes:
    print ('Yes.')
else:
    print ('No.')        
 
win.show() 
 
sys.exit(app.exec_())