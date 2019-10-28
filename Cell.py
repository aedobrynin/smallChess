from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt


class Cell(QtWidgets.QLabel):
    def __init__(self, parent, row, col, width, height, color=Qt.black):
        super().__init__(parent)

        self.row = row
        self.col = col

        self.width = width
        self.height = height

        self.color = color

        self.initUi()
        self.updatePixmap()

    def initUi(self):
        self.setFixedSize(self.width, self.height)
        self.pixmap = QtGui.QPixmap(self.width, self.height)
        self.figure = None

    def mousePressEvent(self, event):
        self.removeFigure()

    def updatePixmap(self):
        self.pixmap.fill(self.color)

        if self.figure is not None:
            painter = QtGui.QPainter(self.pixmap)
            painter.drawPixmap(0, 0, QtGui.QPixmap(self.figure))
            painter.end()

        self.setPixmap(self.pixmap)

    def setColor(self, color):
        self.color = color
        self.updatePixmap()

    def setFigure(self, figure):
        self.figure = figure
        self.updatePixmap()

    def removeFigure(self):
        self.figure = None
        self.updatePixmap()

    def getCoordinates(self):
        return self.row, self.col
