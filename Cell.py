from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt


class Cell(QtWidgets.QLabel):
    def __init__(self, parent, row, col, width, height):
        super().__init__(parent)

        self.row = row
        self.col = col

        self.width = width
        self.height = height

        self.initUi()

    def initUi(self):
        self.setFixedSize(self.width, self.height)

        self.pixmap = QtGui.QPixmap(self.width, self.height)

    def mousePressEvent(self, event):
        print("clicked")

    def setColor(self, color):
        self.pixmap.fill(color)
        self.setPixmap(self.pixmap)

    def getCoordinates(self):
        return self.row, self.col
