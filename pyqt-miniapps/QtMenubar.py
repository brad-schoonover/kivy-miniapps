import sys
from PyQt5.QtWidgets import *
 
app = QApplication(sys.argv)       
 

win = QMainWindow()
 

win.resize(320, 240)
 
 
win.setWindowTitle("Qt Menubar") 
 
# Creates a menubar in the app window and creates a file dropdown menu with the addmenu function
mainMenu = win.menuBar()
mainMenu.setNativeMenuBar(False)
QtMenu = mainMenu.addMenu('File')
 
# Creates an exit button action and icon and sets the text as Exit.
exitBut = QAction( 'Exit', win)

#creats a shortcut and places it in text next to the exit button

exitBut.setShortcut('Ctrl+Q')

#adds a hover tip that describes the exit function 

exitBut.setStatusTip('Exit application')

#Adds a trigger event that closes the window.

exitBut.triggered.connect(win.close)

#adds the exit button to the menubar

QtMenu.addAction(exitBut)
 
 
# Show window
win.show() 
 
sys.exit(app.exec_())