from PyQt5 import QtWidgets, QtCore, QtGui
import chess

from Cell import Cell
from PromotionDialog import PromotionDialog
from config import *


class BoardWidget(QtWidgets.QWidget):
    gameEnded = QtCore.pyqtSignal(str)
    moveMade = QtCore.pyqtSignal(chess.Move)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()

        self.gameStarted = False

    def initUi(self):
        self.resize(FIELD_SIZE, FIELD_SIZE)
        self.cellsLayout = QtWidgets.QGridLayout(self)
        self.initBoard()

    def initBoard(self):
        self.board = chess.Board()

        for row in range(8):
            for col in range(8):
                cell = Cell(self, col, row, CELL_SIZE, CELL_SIZE)
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

        firstCellCoords = firstCell.getCoordinates()
        secondCellCoords = secondCell.getCoordinates()

        firstSquare = chess.square(*firstCellCoords)
        secondSquare = chess.square(*secondCellCoords)

        promotion = None

        if self.board.piece_at(firstSquare).piece_type == chess.PAWN:
            if secondCellCoords[1] == 0 or secondCellCoords[1] == 7:
                promotion = chess.QUEEN

        move = chess.Move(firstSquare, secondSquare, promotion=promotion)

        if move in self.board.legal_moves:
            if promotion is not None:
                self.promotionDialog = PromotionDialog(self.parent(),
                                                       self.board.turn)
                choosen = self.promotionDialog.exec()

                if choosen == 0:
                    return

                move.promotion = self.promotionDialog.getPromotion()

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

    def forceLose(self, loser):
        self.gameStarted = False

        if loser == chess.WHITE:
            self.gameEnded.emit("0-1")
        else:
            self.gameEnded.emit("1-0")

    def hasInsufficientMaterial(self, color):
        return self.board.has_insufficient_material(color)

    def isDrawPossibleWithoutOpponentApproval(self):
        return self.board.can_claim_draw()

    def draw(self):
        self.gameStarted = False
        self.gameEnded.emit("1/2-1/2")

    def getMovesQuantity(self):
        return len(self.board.move_stack)
