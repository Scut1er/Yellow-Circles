import sys
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        QMainWindow.setFixedSize(self, 800, 600)
        self.pushButton.clicked.connect(self.creating_cirles)
        self.drawing = False

    def paintEvent(self, event):
        if self.drawing:
            painter = QPainter()
            painter.begin(self)

            for i in range(3):
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                painter.setPen(QPen(QColor(r, g, b), 7, Qt.SolidLine))
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
