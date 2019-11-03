from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3

from config import *

import uiFiles.StatisticsWindowUi as StatisticsWindowUi


class StatisticsWindow(QtWidgets.QMainWindow,
                       StatisticsWindowUi.Ui_statisticsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.statisticsTable.\
            customContextMenuRequested.connect(self.openContextMenu)

        self.con = sqlite3.connect(DB_PATH)

        cur = self.con.execute("SELECT * FROM Players")

        self.columnNames = tuple(descr[0] for descr in cur.description)
        self.columnNames = tuple(name.replace('_', ' ').capitalize()
                                 for name in self.columnNames)

        self.statisticsTable.setColumnCount(len(self.columnNames))
        self.statisticsTable.setHorizontalHeaderLabels(self.columnNames)

        self.updateStatisticsTable()

    def updateStatisticsTable(self):
        self.statisticsTable.setRowCount(0)

        cur = self.con.cursor()
        players = cur.execute("SELECT * FROM Players").fetchall()

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

        cur = self.con.cursor()
        cur.execute("""INSERT INTO Players(nickname) VALUES (?)""",
                    (nickname, ))

        self.con.commit()
        self.updateStatisticsTable()

    def editPlayer(self):
        playerId = self.sender().data()

        cur = self.con.cursor()
        cur_nickname = cur.execute("""SELECT nickname
FROM Players WHERE id = ?""",
                                   (playerId,)).fetchone()[0]

        new_nickname, state = QtWidgets.QInputDialog.getText(self,
                                                             "Edit player",
                                                             "Nickname:",
                                                             text=cur_nickname)

        if state is False:
            return

        cur = self.con.cursor()
        cur.execute("""UPDATE Players
SET nickname = ?
WHERE id = ?""",
                    (new_nickname, playerId))

        self.con.commit()
        self.updateStatisticsTable()

    def removePlayer(self):
        playerId = self.sender().data()

        cur = self.con.cursor()
        cur.execute("""DELETE FROM Players WHERE id = ?""", (playerId, ))

        self.con.commit()
        self.updateStatisticsTable()

    def closeEvent(self, event):
        self.con.commit()
        self.con.close()

        super().closeEvent(event)
