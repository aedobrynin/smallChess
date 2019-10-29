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
        self.piece = None

    def mousePressEvent(self, event):
        self.removePiece()

    def updatePixmap(self):
        self.pixmap.fill(self.color)

        if self.piece is not None:
            painter = QtGui.QPainter(self.pixmap)
            painter.drawPixmap(0, 0, QtGui.QPixmap(self.piece))
            painter.end()

        self.setPixmap(self.pixmap)

    def setColor(self, color):
        self.color = color
        self.updatePixmap()

    def setPiece(self, piece):
        self.piece = piece
        self.updatePixmap()

    def removePiece(self):
        self.piece = None
        self.updatePixmap()

    def getCoordinates(self):
        return self.row, self.col
