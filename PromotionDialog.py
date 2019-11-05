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
        self.promoteToKnight.setIcon(QtGui.QIcon(P_DIR +
                                                 ('N' if self.piecesColor ==
                                                  chess.WHITE
                                                  else 'n') +
                                                 P_EXT))

        self.promoteToBishop.setIconSize(iconSize)
        self.promoteToBishop.setIcon(QtGui.QIcon(P_DIR +
                                                 ('B' if self.piecesColor ==
                                                  chess.WHITE
                                                  else 'b') +
                                                 P_EXT))

        self.promoteToRook.setIconSize(iconSize)
        self.promoteToRook.setIcon(QtGui.QIcon(P_DIR +
                                               ('R' if self.piecesColor ==
                                                chess.WHITE
                                                else 'r') +
                                               P_EXT))

        self.promoteToQueen.setIconSize(iconSize)
        self.promoteToQueen.setIcon(QtGui.QIcon(P_DIR +
                                                ('Q' if self.piecesColor ==
                                                 chess.WHITE
                                                 else 'q') +
                                                P_EXT))

        self.promotionButtons.buttonClicked.connect(self.promote)

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
