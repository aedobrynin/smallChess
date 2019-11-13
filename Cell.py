from PyQt5 import QtWidgets, QtCore, QtGui
import chess

from config import *


class Cell(QtWidgets.QLabel):
    pass


class Cell(QtWidgets.QLabel):
    moveMade = QtCore.pyqtSignal(Cell, Cell)

    def __init__(self, parent, row, col,
                 width, height, color=BLACK_CELL_COLOR):
        super().__init__(parent)

        self.row = row
        self.col = col

        self.width = width
        self.height = height

        self.color = color
        self.piece = None

        self.initUi()
        self.updatePixmap()

    def initUi(self):
        self.setAcceptDrops(True)
        self.setFixedSize(self.width, self.height)
        self.pixmap = QtGui.QPixmap(self.width, self.height)

    def getPathToPieceImg(self):
        color = ("w" if self.piece.color == chess.WHITE else "b")
        path = P_DIR + self.piece.symbol().lower() + color + P_EXT

        return resourcePath(path)

    def mouseMoveEvent(self, e):
        if self.piece is None:
            return

        mimeData = QtCore.QMimeData()
        drag = QtGui.QDrag(self)

        path = self.getPathToPieceImg()

        drag.setPixmap(QtGui.QPixmap(path))
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        cursor = QtGui.QPixmap(1, 1)
        cursor.fill(QtCore.Qt.transparent)
        drag.setDragCursor(cursor, QtCore.Qt.MoveAction)
        drag.exec(QtCore.Qt.MoveAction)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        source = event.source()

        if self is source:
            event.ignore()
            return

        event.accept()
        self.moveMade.emit(source, self)

    def updatePixmap(self):
        self.pixmap.fill(self.color)

        if self.piece is not None:
            painter = QtGui.QPainter(self.pixmap)
            path = self.getPathToPieceImg()
            painter.drawPixmap(0, 0, QtGui.QPixmap(path))
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
