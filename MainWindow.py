from PyQt5 import QtWidgets, QtCore, QtGui

from StatisticsWindow import StatisticsWindow
from BoardWidget import BoardWidget
from ChoosePlayersDialog import ChoosePlayersDialog
from config import *

import uiFiles.MainWindowUi as MainWindowUi


class MainWindow(QtWidgets.QMainWindow, MainWindowUi.Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.actionNewGame.triggered.connect(self.newGame)
        self.actionSeeStatistics.triggered.connect(self.openStatisticsWindow)

        self.board = BoardWidget(self)
        self.board.move(5, 30)
        self.board.gameEnded.connect(self.gameEnded)

    def newGame(self):
        gameStarted = self.board.isGameStarted()

        if gameStarted is True:
            force = QtWidgets.QMessageBox\
                    .question(self,
                              "",
                              """Do you really want to start new game?
This game is not ended.""",
                              QtWidgets.QMessageBox.Yes |
                              QtWidgets.QMessageBox.No)

            if force != QtWidgets.QMessageBox.Yes:
                return

        self.choosePlayersDialog = ChoosePlayersDialog(self)
        playersChoosen = self.choosePlayersDialog.exec()

        if playersChoosen:
            self.firstPlayer = self.choosePlayersDialog.getFirstPlayerData()
            self.secondPlayer = self.choosePlayersDialog.getSecondPlayerData()
            self.choosePlayersDialog.close()
        else:
            self.choosePlayersDialog.close()
            return

        print(self.firstPlayer, self.secondPlayer)

        self.actionSeeStatistics.setEnabled(False)

        self.board.startGame(force=True)

    def gameEnded(self):
        print(self.board.getResult())
        self.actionSeeStatistics.setEnabled(True)

    def openStatisticsWindow(self):
        self.statisticsWindow = StatisticsWindow(self)
        self.statisticsWindow.show()
