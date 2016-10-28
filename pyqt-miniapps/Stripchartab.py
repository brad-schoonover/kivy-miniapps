import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Stripcharttab(QWidget):
    
    def __init__(self):
        super(Stripcharttab,self).__init__()
        self.tab_layout()
        
    def tab_layout(self):
        
        boxlayout3 = QVBoxLayout()
        self.setLayout(boxlayout3)