from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3
import chess

from StatisticsWindow import StatisticsWindow
from BoardWidget import BoardWidget
from NewGameDialog import NewGameDialog
from ChessClock import ChessClock

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
        self.board.moveMade.connect(self.inGameUpdate)

        self.firstPlayerSurrenderBtn.clicked.connect(self.surrender)
        self.firstPlayerOfferDrawBtn.clicked.connect(self.offerDraw)

        self.secondPlayerSurrenderBtn.clicked.connect(self.surrender)
        self.secondPlayerOfferDrawBtn.clicked.connect(self.offerDraw)

        self.firstPlayerClock = ChessClock(parent=self)
        self.firstPlayerClock.timeIsOver.connect(self.timeIsOver)
        self.rightColumnLayout.addWidget(self.firstPlayerClock, 3, 1)

        self.secondPlayerClock = ChessClock(parent=self)
        self.secondPlayerClock.timeIsOver.connect(self.timeIsOver)
        self.rightColumnLayout.addWidget(self.secondPlayerClock, 0, 1)

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

        self.newGameDialog = NewGameDialog(self)
        playersChoosen = self.newGameDialog.exec()
        if playersChoosen is False:
            return

        self.firstPlayer = self.newGameDialog.getFirstPlayerData()
        self.secondPlayer = self.newGameDialog.getSecondPlayerData()

        timerData = self.newGameDialog.getTimerData()
        self.countTime = timerData[0]

        if self.countTime:
            self.firstPlayerClock.setTime(timerData[1])
            self.secondPlayerClock.setTime(timerData[1])

        self.firstPlayerNickname.setText(self.firstPlayer[1])
        self.secondPlayerNickname.setText(self.secondPlayer[1])

        self.movesList.clear()

        self.actionSeeStatistics.setEnabled(False)

        self.board.startGame()

    def updateClocks(self):
        if self.countTime is False:
            return

        if self.board.getCurrentTurn() == chess.WHITE:
            self.secondPlayerClock.stop()
            self.firstPlayerClock.start()
        else:
            self.firstPlayerClock.stop()
            self.secondPlayerClock.start()

    def inGameUpdate(self, move):
        self.firstPlayerSurrenderBtn.setEnabled(True)
        self.secondPlayerSurrenderBtn.setEnabled(True)

        self.updateClocks()

        if self.board.getCurrentTurn() == chess.WHITE:
            self.firstPlayerOfferDrawBtn.setEnabled(True)
            self.secondPlayerOfferDrawBtn.setEnabled(False)
        else:
            self.firstPlayerOfferDrawBtn.setEnabled(False)
            self.secondPlayerOfferDrawBtn.setEnabled(True)

        self.firstPlayerOfferDrawBtn.setText("Offer a draw")
        self.secondPlayerOfferDrawBtn.setText("Offer a draw")

        movesQuantity = self.board.getMovesQuantity()
        self.movesList.addItem(f"{movesQuantity}. {move.uci()}")
        self.movesList.scrollToBottom()

    def gameEnded(self, result):
        self.firstPlayerClock.stop()
        self.secondPlayerClock.stop()

        self.firstPlayerOfferDrawBtn.setEnabled(False)
        self.firstPlayerOfferDrawBtn.setText("Offer a draw")
        self.firstPlayerSurrenderBtn.setEnabled(False)

        self.secondPlayerOfferDrawBtn.setEnabled(False)
        self.secondPlayerOfferDrawBtn.setText("Offer a draw")
        self.secondPlayerSurrenderBtn.setEnabled(False)

        self.actionSeeStatistics.setEnabled(True)

        self.movesList.addItem(result)
        self.movesList.scrollToBottom()

        self.con = sqlite3.connect(DB_PATH)

        cur = self.con.cursor()

        selectRequest = """SELECT games_played, games_won,
games_draw, games_lost
FROM Players
WHERE id = ?"""

        firstPlayerStats = cur.execute(selectRequest,
                                       (self.firstPlayer[0], )).fetchone()
        firstPlayerStats = list(firstPlayerStats)

        secondPlayerStats = cur.execute(selectRequest,
                                        (self.secondPlayer[0], )).fetchone()
        secondPlayerStats = list(secondPlayerStats)

        firstPlayerStats[0] += 1
        secondPlayerStats[0] += 1

        if result == "1-0":
            firstPlayerStats[1] += 1
            secondPlayerStats[3] += 1
        elif result == "1/2-1/2":
            firstPlayerStats[2] += 1
            secondPlayerStats[2] += 1
        else:
            firstPlayerStats[3] += 1
            secondPlayerStats[1] += 1

        updateRequest = """UPDATE Players
SET games_played = ?,
    games_won = ?,
    games_draw = ?,
    games_lost = ?

WHERE id = ?"""

        cur.execute(updateRequest, (*firstPlayerStats, self.firstPlayer[0]))

        cur.execute(updateRequest, (*secondPlayerStats, self.secondPlayer[0]))

        self.con.commit()
        self.con.close()

    def offerDraw(self):
        if self.sender().text() == "Offer a draw":
            """Check if draw can be claimed without opponent approval"""
            if self.board.isPossibleDrawWithoutOpponentApproval():
                self.board.draw()
            else:
                if self.sender() is self.firstPlayerOfferDrawBtn:
                    self.firstPlayerOfferDrawBtn.setEnabled(False)
                    self.secondPlayerOfferDrawBtn.setEnabled(True)
                    self.secondPlayerOfferDrawBtn.setText("Approve a draw")
                else:
                    self.secondPlayerOfferDrawBtn.setEnabled(False)
                    self.firstPlayerOfferDrawBtn.setEnabled(True)
                    self.firstPlayerOfferDrawBtn.setText("Approve a draw")
        else:
            self.board.draw()

    def surrender(self):
        if self.sender() is self.firstPlayerSurrenderBtn:
            self.board.forceLose(chess.WHITE)
        else:
            self.board.forceLose(chess.BLACK)

    def timeIsOver(self):
        if self.firstPlayerClock.getTime() == 0:
            if self.board.has_insufficient_material(chess.BLACK):
                self.board.draw()
            else:
                self.board.forceLose(chess.WHITE)
        else:
            if self.board.has_insufficient_material(chess.WHITE):
                self.board.draw()
            else:
                self.board.forceLose(chess.BLACK)

    def openStatisticsWindow(self):
        self.statisticsWindow = StatisticsWindow(self)
        self.statisticsWindow.show()
