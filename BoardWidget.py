
from PyQt5 import QtWidgets, QtCore, QtGui
import chess

from Cell import Cell
from config import *


class BoardWidget(QtWidgets.QWidget):
    gameEnded = QtCore.pyqtSignal(str)
    moveMade = QtCore.pyqtSignal(chess.Move)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.gameStarted = False

    def initUi(self):
        self.resize(*FIELD_SIZE)
        self.cellsLayout = QtWidgets.QGridLayout(self)
        self.initBoard()

    def initBoard(self):
        self.board = chess.Board()

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

    def clearBoard(self):
        for row in range(8):
            for col in range(8):
                cell = self.cellsLayout.itemAtPosition(7 - row, col).widget()
                cell.removePiece()

    def startGame(self, force=False):
        if self.gameStarted and force is False:
            return False

        self.clearBoard()
        self.board.reset()

        for row in range(8):
            for col in range(8):
                cell = self.cellsLayout.itemAtPosition(7 - row, col).widget()

                square = chess.square(col, row)
                piece = self.board.piece_at(square)

                if piece is not None:
                    cell.setPiece(piece)

        self.gameStarted = True
        self.firstCell = None
        self.secondCell = None

        return True

    def cellClicked(self):
        if self.gameStarted is False:
            return

        cell = self.sender()

        if self.firstCell is None:
            piece = cell.getPiece()
            if piece is not None and piece.color == self.board.turn:
                self.firstCell = cell
                self.firstCell.pick()
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

                self.moveMade.emit(move)

                if self.board.result() != '*':
                    self.gameStarted = False
                    self.gameEnded.emit(self.board.result())

            self.firstCell.unpick()

            self.firstCell = None
            self.secondCell = None

    def getCurrentTurn(self):
        return self.board.turn

    def isGameStarted(self):
        return self.gameStarted

    def surrender(self, loser):
        self.gameStarted = False

        if loser == chess.WHITE:
            self.gameEnded.emit("0-1")
        else:
            self.gameEnded.emit("1-0")

    def isPossibleDrawWithoutOpponentApproval(self):
        return self.board.can_claim_draw()

    def draw(self):
        self.gameStarted = False
        self.gameEnded.emit("1/2-1/2")
