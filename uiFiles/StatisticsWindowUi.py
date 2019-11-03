# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/StatisticsWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statisticsWindow(object):
    def setupUi(self, statisticsWindow):
        statisticsWindow.setObjectName("statisticsWindow")
        statisticsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        statisticsWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(statisticsWindow.sizePolicy().hasHeightForWidth())
        statisticsWindow.setSizePolicy(sizePolicy)
        statisticsWindow.setMinimumSize(QtCore.QSize(800, 600))
        statisticsWindow.setMaximumSize(QtCore.QSize(800, 600))
        statisticsWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        statisticsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(statisticsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainGridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.statisticsTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.statisticsTable.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.statisticsTable.setObjectName("statisticsTable")
        self.statisticsTable.setColumnCount(0)
        self.statisticsTable.setRowCount(0)
        self.statisticsTable.horizontalHeader().setStretchLastSection(True)
        self.statisticsTable.verticalHeader().setVisible(False)
        self.mainGridLayout.addWidget(self.statisticsTable, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.mainGridLayout.addWidget(self.label, 1, 0, 1, 1)
        statisticsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(statisticsWindow)
        QtCore.QMetaObject.connectSlotsByName(statisticsWindow)

    def retranslateUi(self, statisticsWindow):
        _translate = QtCore.QCoreApplication.translate
        statisticsWindow.setWindowTitle(_translate("statisticsWindow", "Statistics"))
        self.statisticsTable.setSortingEnabled(True)
        self.label.setText(_translate("statisticsWindow", "Right mouse button click on empty space to add new player or on player to also edit or delete it."))
