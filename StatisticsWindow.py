from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3

from config import *

import uiFiles.StatisticsWindowUi as StatisticsWindowUi


class StatisticsWindow(QtWidgets.QMainWindow,
                       StatisticsWindowUi.Ui_statisticsWindow):
    def __init__(self, statistics, parent=None):
        super().__init__(parent)

        self.statistics = statistics

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.statisticsTable.\
            customContextMenuRequested.connect(self.openContextMenu)

        columnNames = self.statistics.getColumnNames()
        self.columnNames = tuple(name.replace('_', ' ').capitalize()
                                 for name in columnNames)

        self.statisticsTable.setColumnCount(len(self.columnNames))
        self.statisticsTable.setHorizontalHeaderLabels(self.columnNames)

        self.updateStatisticsTable()

    def updateStatisticsTable(self):
        self.statisticsTable.setRowCount(0)

        players = self.statistics.getStatistics()

        for row, player in enumerate(players):
            self.statisticsTable.setRowCount(row + 1)

            for col, value in enumerate(player):
                widgetItem = QtWidgets.QTableWidgetItem(str(value))
                widgetItem.setFlags(widgetItem.flags() ^
                                    QtCore.Qt.ItemIsEditable)

                self.statisticsTable.setItem(row, col, widgetItem)

        self.statisticsTable.resizeColumnsToContents()
        self.statisticsTable.horizontalHeader().\
            setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def openContextMenu(self, pos):
        self.menu = QtWidgets.QMenu(self)

        addPlayerAction = QtWidgets.QAction("Add player", self.menu)
        addPlayerAction.triggered.connect(self.addPlayer)

        self.menu.addAction(addPlayerAction)

        tableClick = self.statisticsTable.itemAt(pos)

        if tableClick is not None:
            row = tableClick.row()
            playerId = self.statisticsTable.item(row, 0).text()
            variant = QtCore.QVariant(playerId)

            editPlayerAction = QtWidgets.QAction("Edit player", self.menu)
            editPlayerAction.triggered.connect(self.editPlayer)
            editPlayerAction.setData(variant)
            self.menu.addAction(editPlayerAction)

            deletePlayerAction = QtWidgets.QAction("Delete player", self.menu)
            deletePlayerAction.triggered.connect(self.removePlayer)
            deletePlayerAction.setData(variant)
            self.menu.addAction(deletePlayerAction)

        self.menu.popup(self.statisticsTable.mapToGlobal(pos))

    def addPlayer(self):
        nickname, state = QtWidgets.QInputDialog.getText(self,
                                                         "Add new player",
                                                         "Nickname:")
        if state is False:
            return

        self.statistics.addPlayer(nickname)
        self.updateStatisticsTable()

    def editPlayer(self):
        playerId = self.sender().data()
        curNickname = self.statistics.getPlayersData(playerId,
                                                     ("nickname",))[0]
        newNickname, state = QtWidgets.QInputDialog.getText(self,
                                                            "Edit player",
                                                            "Nickname:",
                                                            text=curNickname)
        if state is False:
            return

        self.statistics.updatePlayersData(playerId,
                                          (("nickname", newNickname), ))

        self.updateStatisticsTable()

    def removePlayer(self):
        playerId = self.sender().data()
        self.statistics.deletePlayer(playerId)

        self.updateStatisticsTable()
