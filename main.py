import sys

from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.drawEllipse)
        self.ellipses = []
        self.paint = False

    def drawEllipse(self):
        self.paint = True
        self.ellipses.append({
            'radius': randrange(20, 60),
            'x': randrange(self.width()),
            'y': randrange(self.height())
        })
        self.repaint()

    def paintEvent(self, event):
        if not self.paint:
            return None
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QtGui.QColor('yellow'))
        for elem in self.ellipses:
            painter.drawEllipse(elem['x'] - elem['radius'],
                                elem['y'] - elem['radius'], elem['radius'] * 2, elem['radius'] * 2)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
