from PyQt5 import QtWidgets, QtCore, QtGui
import sqlite3

from config import *

import uiFiles.StatisticsWindowUi as StatisticsWindowUi


class StatisticsWindow(QtWidgets.QMainWindow, StatisticsWindowUi.Ui_statisticsWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.statisticsTable.customContextMenuRequested.connect(self.openContextMenu)

        self.con = sqlite3.connect(DB_PATH)

        cur = self.con.cursor()
        self.column_names = tuple(column_info[1].replace('_', ' ').capitalize() for column_info in cur.execute("PRAGMA table_info(Players);"))
        self.statisticsTable.setColumnCount(len(self.column_names))
        self.statisticsTable.setHorizontalHeaderLabels(self.column_names)

        self.updateStatisticsTable()

    def updateStatisticsTable(self):
        cur = self.con.cursor()
        players = cur.execute("""SELECT * FROM Players""")

        for row, player in enumerate(players):
            self.statisticsTable.setRowCount(row + 1)

            for col, value in enumerate(player):
                widgetItem = QtWidgets.QTableWidgetItem(str(value))
                widgetItem.setFlags(widgetItem.flags() ^ QtCore.Qt.ItemIsEditable)

                self.statisticsTable.setItem(row, col, widgetItem)

        self.statisticsTable.resizeColumnsToContents()
        self.statisticsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def closeEvent(self, event):
        self.con.commit()
        self.con.close()

        super().closeEvent(event)

    def openContextMenu(self, pos):
        self.menu = QtWidgets.QMenu(self)

        if self.statisticsTable.itemAt(pos) is not None:
            action = QtWidgets.QAction("Delete player", self.menu)
            action.triggered.connect(self.removePlayer)

            variant = QtCore.QVariant(self.statisticsTable.itemAt(pos))
            action.setData(variant)
        else:
            action = QtWidgets.QAction("Add player", self.menu)
            action.triggered.connect(self.addPlayer)

        self.menu.addAction(action)
        self.menu.popup(self.statisticsTable.mapToGlobal(pos))

    def addPlayer(self):
        nickname = "Abacaba"

        cur = self.con.cursor()
        cur.execute("""INSERT INTO Players(nickname) VALUES (?)""", (nickname, ))

        self.con.commit()
        self.updateStatisticsTable()

    def removePlayer(self):
        row = self.sender().data().row()
        id = self.statisticsTable.item(row, 0).text()

        print(id)

        cur = self.con.cursor()
        cur.execute("""DELETE FROM Players WHERE id = ?""", (id, ))

        self.con.commit()
        self.updateStatisticsTable()
