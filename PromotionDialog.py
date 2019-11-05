from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3
import chess

from config import *

import uiFiles.PromotionDialogUi as PromotionDialogUi


class PromotionDialog(QtWidgets.QDialog,
                      PromotionDialogUi.Ui_promotionDialog):
    def __init__(self, parent=None, piecesColor=chess.WHITE):
        super().__init__(parent)

        self.piecesColor = piecesColor
        self.promotion = None

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        iconSize = QtCore.QSize(CELL_SIZE + 10, CELL_SIZE + 10)

        self.promoteToKnight.setIconSize(iconSize)
        self.promoteToKnight.setIcon(QtGui.QIcon(self.getPathToIcon('n')))

        self.promoteToBishop.setIconSize(iconSize)
        self.promoteToBishop.setIcon(QtGui.QIcon(self.getPathToIcon('b')))

        self.promoteToRook.setIconSize(iconSize)
        self.promoteToRook.setIcon(QtGui.QIcon(self.getPathToIcon('r')))

        self.promoteToQueen.setIconSize(iconSize)
        self.promoteToQueen.setIcon(QtGui.QIcon(self.getPathToIcon('q')))

        self.promotionButtons.buttonClicked.connect(self.promote)

    def getPathToIcon(self, pieceLetter):
        return P_DIR +\
               (pieceLetter.upper() if self.piecesColor == chess.WHITE
                else pieceLetter.lower()) +\
               P_EXT

    def promote(self, button):
        if button is self.promoteToKnight:
            self.promotion = chess.KNIGHT
        elif button is self.promoteToBishop:
            self.promotion = chess.BISHOP
        elif button is self.promoteToRook:
            self.promotion = chess.ROOK
        elif button is self.promoteToQueen:
            self.promotion = chess.QUEEN

        self.accept()

    def getPromotion(self):
        return self.promotion
