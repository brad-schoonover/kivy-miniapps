import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

class MyRect(QGraphicsItem):
    def __init__(self, position, size, scene):
        super(MyRect, self.__init__(None, scene))
        self.rect = QRectF(position.x(), position.y(), size.x(), size.y())
        self.setPos(position)
        
class Scene1(QGraphicsScene):
    def __init__(self, parent = None):
        super(Scene1, self).__init__(parent)
        self.setSceneRect(0, 30, 400, 400) 
        
        
    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget):
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.black)
        pen.setWidth(1)
        painter.drawRectangle(self.rect)

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        ExLayout = QtGui.QVBoxLayout()
        

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
      
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)
        
 
class OpenWindow(QtGui.QMainWindow):

    def __init__(self):
        super(OpenWindow, self).__init__()
        self.initUI()

    def initUI(self):
#setting up the main layout for widget sizing guidelines
        frame = QFrame()
        self.setCentralWidget(frame)
        mainlayout = QHBoxLayout()
        frame.setLayout(mainlayout)
        
        tab_widget = QtGui.QTabWidget(self)
        tab1 = Example()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    op = OpenWindow
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()