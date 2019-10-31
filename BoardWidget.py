from PyQt5 import QtWidgets, QtCore, QtGui
import chess

from Cell import Cell
from config import *


class BoardWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.inGame = False

    def initUi(self):
        self.resize(*FIELD_SIZE)
        self.cellsLayout = QtWidgets.QGridLayout(self)

        for row in range(8):
            for col in range(8):
                cell = Cell(self, col, row,
                            FIELD_SIZE[0] // 8, FIELD_SIZE[1] // 8)
                cell.clicked.connect(self.cellClicked)

                if (row + col) % 2 == 0:
                    cell.setColor(BLACK_CELL_COLOR)
                else:
                    cell.setColor(WHITE_CELL_COLOR)

                self.cellsLayout.addWidget(cell, 7 - row, col)
                self.cellsLayout.addWidget(cell, 7 - row, col)

    def startGame(self):
        self.board = chess.Board()

        for row in range(8):
            for col in range(8):
                cell = self.cellsLayout.itemAtPosition(7 - row, col).widget()

                square = chess.square(col, row)
                piece = self.board.piece_at(square)

                if piece is not None:
                    cell.setPiece(piece)

        self.inGame = True
        self.firstCell = None
        self.secondCell = None

    def cellClicked(self):
        if self.inGame is False:
            return

        cell = self.sender()

        if self.firstCell is None:
            if cell.getPiece() is not None:
                self.firstCell = cell
        else:
            self.secondCell = cell

        if self.secondCell is not None:
            firstSquare = chess.square(*self.firstCell.getCoordinates())
            secondSquare = chess.square(*self.secondCell.getCoordinates())

            move = chess.Move(firstSquare, secondSquare)

            if move in self.board.legal_moves:
                self.board.push(move)

                firstCellPiece = self.board.piece_at(firstSquare)
                self.firstCell.setPiece(firstCellPiece)

                secondCellPiece = self.board.piece_at(secondSquare)
                self.secondCell.setPiece(secondCellPiece)

            self.firstCell = None
            self.secondCell = None
