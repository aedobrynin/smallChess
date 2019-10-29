import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Cell import Cell
import Ui

import chess
from config import *


class MainWindow(QtWidgets.QMainWindow, Ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUi()

        self.firstCell = None
        self.secondCell = None

    def initUi(self):
        self.board = chess.Board()

        for row in range(8):
            for col in range(8):
                cell = Cell(self, col, row,
                            FIELD_SIZE[0] // 8, FIELD_SIZE[1] // 8)
                cell.clicked.connect(self.cellClicked)

                if (row + col) % 2 == 1:
                    cell.setColor(BLACK_CELL_COLOR)
                else:
                    cell.setColor(WHITE_CELL_COLOR)

                square = chess.square(col, row)
                piece = self.board.piece_at(square)
                if piece is not None:
                    cell.setPiece(piece.symbol())

                self.chessCellsGridLayout.addWidget(cell, 7 - row, col)

    def cellClicked(self):
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
                if firstCellPiece is not None:
                    self.firstCell.setPiece(firstCellPiece.symbol())
                else:
                    self.firstCell.removePiece()

                secondCellPiece = self.board.piece_at(secondSquare)
                if secondCellPiece is not None:
                    self.secondCell.setPiece(secondCellPiece.symbol())

            self.firstCell = None
            self.secondCell = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
