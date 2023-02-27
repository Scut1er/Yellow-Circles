import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        QMainWindow.setFixedSize(self, 800, 600)
        self.pushButton.clicked.connect(self.creating_cirles)
        self.drawing = False

    def paintEvent(self, event):
        if self.drawing:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QPen(Qt.yellow, 7, Qt.SolidLine))

            for i in range(3):
                x = randint(1, 700)
                y = randint(1, 500)
                d = randint(2, 300)
                painter.drawEllipse(x, y, d, d)

    def creating_cirles(self):
        self.drawing = True
        self.update()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
