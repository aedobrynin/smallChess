from PyQt5 import QtWidgets, QtCore

import uiFiles.NewGameDialogUi as NewGameDialogUi


class NewGameDialog(QtWidgets.QDialog,
                    NewGameDialogUi.Ui_newGameDialog):
    def __init__(self, statistics, parent=None):
        super().__init__(parent)

        self.statistics = statistics

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.firstPlayerBox.currentIndexChanged.\
            connect(self.startGameBtnState)
        self.secondPlayerBox.currentIndexChanged.\
            connect(self.startGameBtnState)

        self.timeLimitCBox.stateChanged.connect(self.widgetStates)
        self.minutesSBox.valueChanged.connect(self.widgetStates)
        self.secondsSBox.valueChanged.connect(self.widgetStates)

        self.startGameBtn.clicked.connect(self.accept)

        players = self.statistics.getPlayersList()
        for playerId, nickname in players:
            variant = QtCore.QVariant(playerId)
            self.firstPlayerBox.addItem(nickname, variant)
            self.secondPlayerBox.addItem(nickname, variant)

    def startGameBtnState(self):
        state = True

        if self.firstPlayerBox.currentData() == \
           self.secondPlayerBox.currentData():
            state = False

        if self.timeLimitCBox.checkState() == QtCore.Qt.Checked and \
           self.secondsSBox.value() == 0 and \
           self.minutesSBox.value() == 0:
            state = False

        self.startGameBtn.setEnabled(state)

    def timePickBtnStates(self):
        if self.timeLimitCBox.checkState() == QtCore.Qt.Checked:
            self.secondsSBox.setEnabled(True)
            self.minutesSBox.setEnabled(True)
        else:
            self.secondsSBox.setEnabled(False)
            self.minutesSBox.setEnabled(False)

    def widgetStates(self):
        self.timePickBtnStates()
        self.startGameBtnState()

    def getFirstPlayerData(self):
        return (self.firstPlayerBox.currentData(),
                self.firstPlayerBox.currentText())

    def getSecondPlayerData(self):
        return (self.secondPlayerBox.currentData(),
                self.secondPlayerBox.currentText())

    def getTimerData(self):
        return (self.timeLimitCBox.checkState() == QtCore.Qt.Checked,
                self.minutesSBox.value() * 60 + self.secondsSBox.value())
