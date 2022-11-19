import sys
from random import randint

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setPen(QColor(255, 225, 0))
        diameter = randint(100, 100)
        qp.drawEllipse(QRect(randint(0, 600), randint(0, 600), diameter, diameter))


app = QApplication(sys.argv)
ex = YellowCircles()
ex.show()
sys.exit(app.exec())
