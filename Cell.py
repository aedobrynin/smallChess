from PyQt5 import QtWidgets, QtCore, QtGui

from config import *


class Cell(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent, row, col, width, height, color=QtCore.Qt.black):
        super().__init__(parent)

        self.row = row
        self.col = col

        self.width = width
        self.height = height

        self.color = color
        self.picked = False
        self.piece = None

        self.initUi()
        self.updatePixmap()

    def initUi(self):
        self.setFixedSize(self.width, self.height)
        self.pixmap = QtGui.QPixmap(self.width, self.height)

    def mousePressEvent(self, event):
        self.clicked.emit()

    def updatePixmap(self):
        if self.picked:
            self.pixmap.fill(PICKED_CELL_COLOR)
        else:
            self.pixmap.fill(self.color)

        if self.piece is not None:
            painter = QtGui.QPainter(self.pixmap)
            painter.drawPixmap(0, 0,
                               QtGui.QPixmap(P_DIR +
                                             self.piece.symbol() +
                                             P_EXT))
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

    def pick(self):
        self.picked = True
        self.updatePixmap()

    def unpick(self):
        self.picked = False
        self.updatePixmap()

    def getCoordinates(self):
        return self.row, self.col

    def getPiece(self):
        return self.piece
