from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QLabel


class ChessClock(QtWidgets.QLabel):
    timeIsOver = QtCore.pyqtSignal()
    timeFormat = "{:02d}:{:02d}"

    def __init__(self, parent=None):
        super().__init__(parent)

        self.time = 0

        self.clock = QtCore.QTimer(None)
        self.clock.setTimerType(QtCore.Qt.PreciseTimer)
        self.clock.setSingleShot(True)
        self.clock.setInterval(self.time)
        self.clock.timeout.connect(self._timeIsOver)

        self.updateTimer = QtCore.QTimer(None)
        self.updateTimer.setTimerType(QtCore.Qt.PreciseTimer)
        self.updateTimer.setInterval(1000)
        self.updateTimer.timeout.connect(self.updateLabel)

        self.initUi()

    def initUi(self):
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText("00:00")

    def setTime(self, timeInSeconds):
        self.clock.stop()
        self.updateTimer.stop()

        self.time = timeInSeconds * 1000
        self.clock.setInterval(self.time)

        minutes = self.time // 1000 // 60
        seconds = self.time // 1000 % 60

        self.setText(self.timeFormat.format(minutes, seconds))

    def updateLabel(self):
        remainingTime = self.clock.remainingTime()

        self.time = max(0, remainingTime)

        minutes = self.time // 1000 // 60
        seconds = self.time // 1000 % 60

        self.setText(self.timeFormat.format(minutes, seconds))
        self.updateTimer.start()

    def start(self):
        self.clock.start(self.time)
        self.updateTimer.start()

    def stop(self):
        self.clock.stop()
        self.updateTimer.stop()

    def getTime(self):
        return self.time

    def _timeIsOver(self):
        self.updateTimer.stop()
        self.updateLabel()
        self.timeIsOver.emit()
