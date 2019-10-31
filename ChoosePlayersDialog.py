from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3

from config import *

import uiFiles.ChoosePlayersDialogUi as ChoosePlayersDialogUi


class ChoosePlayersDialog(QtWidgets.QDialog,
                          ChoosePlayersDialogUi.Ui_choosePlayersDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.firstPlayerBox.currentIndexChanged.\
            connect(self.startGameBtnState)
        self.secondPlayerBox.currentIndexChanged.\
            connect(self.startGameBtnState)
        self.startGameBtn.clicked.connect(self.accept)

        self.con = sqlite3.connect(DB_PATH)

        cur = self.con.cursor()

        players = cur.execute("""SELECT id, nickname
FROM Players""").fetchall()

        for id, nickname in players:
            variant = QtCore.QVariant(id)
            self.firstPlayerBox.addItem(nickname, variant)
            self.secondPlayerBox.addItem(nickname, variant)

    def startGameBtnState(self):
        if self.firstPlayerBox.currentData() == \
           self.secondPlayerBox.currentData():
            self.startGameBtn.setEnabled(False)
        else:
            self.startGameBtn.setEnabled(True)

    def getFirstPlayerData(self):
        return (self.firstPlayerBox.currentData(),
                self.firstPlayerBox.currentText())

    def getSecondPlayerData(self):
        return (self.secondPlayerBox.currentData(),
                self.secondPlayerBox.currentText())

    def closeEvent(self, event):
        self.con.close()

        super().closeEvent(event)
