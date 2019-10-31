from PyQt5 import QtWidgets, QtCore, QtGui
import chess

from Cell import Cell
from StatisticsWindow import StatisticsWindow
from config import *

import uiFiles.MainWindowUi as MainWindowUi


class MainWindow(QtWidgets.QMainWindow, MainWindowUi.Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()

        self.firstCell = None
        self.secondCell = None

    def initUi(self):
        self.actionNewGame.triggered.connect(self.newGame)
        self.actionSeeStatistics.triggered.connect(self.openStatisticsWindow)

        for row in range(8):
            for col in range(8):
                cell = Cell(self, col, row,
                            FIELD_SIZE[0] // 8, FIELD_SIZE[1] // 8)
                cell.clicked.connect(self.cellClicked)

                if (row + col) % 2 == 1:
                    cell.setColor(BLACK_CELL_COLOR)
                else:
                    cell.setColor(WHITE_CELL_COLOR)

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
                self.firstCell.setPiece(firstCellPiece)

                secondCellPiece = self.board.piece_at(secondSquare)
                self.secondCell.setPiece(secondCellPiece)

            self.firstCell = None
            self.secondCell = None

    def initBoard(self):
        self.board = chess.Board()

        for row in range(8):
            for col in range(8):
                cell = self.chessCellsGridLayout.\
                        itemAtPosition(7 - row, col).widget()

                square = chess.square(col, row)
                piece = self.board.piece_at(square)

                if piece is not None:
                    cell.setPiece(piece)

        self.firstCell = None
        self.secondCell = None

    def newGame(self):
        print("New game")
        self.initBoard()

    def openStatisticsWindow(self):
        self.statisticsWindow = StatisticsWindow(self)
        self.statisticsWindow.show()
