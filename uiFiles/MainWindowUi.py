# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/MainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(570, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(570, 400))
        mainWindow.setMaximumSize(QtCore.QSize(570, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(387, 10, 174, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.movesList = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.movesList.setObjectName("movesList")
        self.gridLayout.addWidget(self.movesList, 2, 1, 1, 1)
        self.secondPlayerSurrenderBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.secondPlayerSurrenderBtn.setEnabled(False)
        self.secondPlayerSurrenderBtn.setObjectName("secondPlayerSurrenderBtn")
        self.gridLayout.addWidget(self.secondPlayerSurrenderBtn, 1, 1, 1, 1)
        self.firstPlayerSurrenderBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.firstPlayerSurrenderBtn.setEnabled(False)
        self.firstPlayerSurrenderBtn.setObjectName("firstPlayerSurrenderBtn")
        self.gridLayout.addWidget(self.firstPlayerSurrenderBtn, 4, 1, 1, 1)
        self.secondPlayerNickname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.secondPlayerNickname.setObjectName("secondPlayerNickname")
        self.gridLayout.addWidget(self.secondPlayerNickname, 0, 1, 1, 1)
        self.firstPlayerNickname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstPlayerNickname.setObjectName("firstPlayerNickname")
        self.gridLayout.addWidget(self.firstPlayerNickname, 3, 1, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        self.actions = QtWidgets.QMenu(self.menubar)
        self.actions.setObjectName("actions")
        mainWindow.setMenuBar(self.menubar)
        self.actionNewGame = QtWidgets.QAction(mainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
        self.actionPVSAI = QtWidgets.QAction(mainWindow)
        self.actionPVSAI.setObjectName("actionPVSAI")
        self.actionSeeStatistics = QtWidgets.QAction(mainWindow)
        self.actionSeeStatistics.setObjectName("actionSeeStatistics")
        self.actionSeePlayersList = QtWidgets.QAction(mainWindow)
        self.actionSeePlayersList.setObjectName("actionSeePlayersList")
        self.actions.addAction(self.actionNewGame)
        self.actions.addSeparator()
        self.actions.addAction(self.actionSeeStatistics)
        self.menubar.addAction(self.actions.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Small Chess"))
        self.secondPlayerSurrenderBtn.setText(_translate("mainWindow", "Surrender"))
        self.firstPlayerSurrenderBtn.setText(_translate("mainWindow", "Surrender"))
        self.secondPlayerNickname.setText(_translate("mainWindow", "Second player"))
        self.firstPlayerNickname.setText(_translate("mainWindow", "First player"))
        self.actions.setTitle(_translate("mainWindow", "Actions"))
        self.actionNewGame.setText(_translate("mainWindow", "New game"))
        self.actionPVSAI.setText(_translate("mainWindow", "Player VS AI"))
        self.actionSeeStatistics.setText(_translate("mainWindow", "See statistics"))
        self.actionSeePlayersList.setText(_translate("mainWindow", "See players list"))
