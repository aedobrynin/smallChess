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
                cell.moveMade.connect(self.makeMove)

                if (row + col) % 2 == 0:
                    cell.setColor(BLACK_CELL_COLOR)
                else:
                    cell.setColor(WHITE_CELL_COLOR)

                self.cellsLayout.addWidget(cell, 7 - row, col)

    def updateBoard(self):
        for row in range(8):
            for col in range(8):
                cell = self.cellsLayout.itemAtPosition(7 - row, col).widget()
                square = chess.square(col, row)
                piece = self.board.piece_at(square)
                cell.setPiece(piece)

    def startGame(self):
        self.board.reset()
        self.updateBoard()
        self.gameStarted = True

    def makeMove(self, firstCell, secondCell):
        if self.gameStarted is False:
            return

        firstSquare = chess.square(*firstCell.getCoordinates())
        secondSquare = chess.square(*secondCell.getCoordinates())

        move = chess.Move(firstSquare, secondSquare)

        if move in self.board.legal_moves:
            self.board.push(move)

            self.updateBoard()

            self.moveMade.emit(move)

            result = self.board.result()
            if result != '*':
                self.gameStarted = False
                self.gameEnded.emit(result)

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
