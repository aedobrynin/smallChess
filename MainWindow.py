import datetime
import os
from PyQt5 import QtWidgets
import chess

from Statistics import Statistics
from StatisticsWindow import StatisticsWindow
from BoardWidget import BoardWidget
from NewGameDialog import NewGameDialog
from ChessClock import ChessClock

from config import RES_DIR, DB_PATH, resourcePath
import uiFiles.MainWindowUi as MainWindowUi


class MainWindow(QtWidgets.QMainWindow, MainWindowUi.Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.statistics = Statistics(resourcePath(DB_PATH))

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

        self.firstPlayerClock = ChessClock(self)
        self.firstPlayerClock.timeIsOver.connect(self.timeIsOver)
        self.rightColumnLayout.addWidget(self.firstPlayerClock, 3, 1)

        self.secondPlayerClock = ChessClock(self)
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

        self.newGameDialog = NewGameDialog(self.statistics, self)
        dataEnterSuccessful = self.newGameDialog.exec()

        if dataEnterSuccessful == 0:
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

    def updateStatistics(self, result):
        firstPlayerStats = self.statistics.getPlayersData(self.firstPlayer[0],
                                                          ("games_played",
                                                           "games_won",
                                                           "games_draw",
                                                           "games_lost"))
        firstPlayerStats = list(firstPlayerStats)

        secondPlayerStats = self.statistics.getPlayersData(self.secondPlayer[0],
                                                           ("games_played",
                                                            "games_won",
                                                            "games_draw",
                                                            "games_lost"))
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

        self.statistics.updatePlayersData(self.firstPlayer[0],
                                          zip(("games_played",
                                               "games_won",
                                               "games_draw",
                                               "games_lost"),
                                              firstPlayerStats))

        self.statistics.updatePlayersData(self.secondPlayer[0],
                                          zip(("games_played",
                                               "games_won",
                                               "games_draw",
                                               "games_lost"),
                                              secondPlayerStats))

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

        self.updateStatistics(result)

        saveResult, filename = self.savePGN()
        if saveResult:
            self.movesList.addItem("Game PGN was saved in")
            self.movesList.addItem(filename)
        else:
            self.movesList.addItem("Game PGN wasn't saved")

    def offerDraw(self):
        if self.sender().text() == "Offer a draw":
            """Check if draw can be claimed without opponent approval"""
            if self.board.isDrawPossibleWithoutOpponentApproval():
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
            if self.board.hasInsufficientMaterial(chess.BLACK):
                self.board.draw()
            else:
                self.board.forceLose(chess.WHITE)
        else:
            if self.board.hasInsufficientMaterial(chess.WHITE):
                self.board.draw()
            else:
                self.board.forceLose(chess.BLACK)

    def openStatisticsWindow(self):
        self.statisticsWindow = StatisticsWindow(self.statistics, self)
        self.statisticsWindow.show()

    def genPGN(self):
        game = self.board.getGame()
        game.headers["Date"] = datetime.datetime.now().strftime("%y.%m.%d")
        game.headers["White"] = self.firstPlayer[1]
        game.headers["Black"] = self.secondPlayer[1]
        return str(game)

    def savePGN(self, auto=True):
        if auto:
            curTime = datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S")
            if os.path.exists(RES_DIR) is False:
                try:
                    os.mkdir(RES_DIR)
                except PermissionError:
                    return 0, ""
            filePath = f"{RES_DIR}{curTime}-\
{self.firstPlayer[1]}-{self.secondPlayer[1]}.pgn"
        else:
            # TODO
            pass

        pgn = self.genPGN()

        try:
            file = open(filePath, 'w')
            file.write(pgn)
            file.close()
            return 1, filePath
        except PermissionError:
            return 0, ""
