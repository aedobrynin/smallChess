# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 400))
        MainWindow.setMaximumSize(QtCore.QSize(380, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 351))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(50, 50))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chessCellsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chessCellsGridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.chessCellsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.chessCellsGridLayout.setSpacing(0)
        self.chessCellsGridLayout.setObjectName("chessCellsGridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        self.newGameButton = QtWidgets.QMenu(self.menubar)
        self.newGameButton.setObjectName("newGameButton")
        MainWindow.setMenuBar(self.menubar)
        self.actionNewGame = QtWidgets.QAction(MainWindow)
        self.actionNewGame.setObjectName("actionNewGame")
        self.actionPVSAI = QtWidgets.QAction(MainWindow)
        self.actionPVSAI.setObjectName("actionPVSAI")
        self.actionSeeStatistics = QtWidgets.QAction(MainWindow)
        self.actionSeeStatistics.setObjectName("actionSeeStatistics")
        self.actionSeePlayersList = QtWidgets.QAction(MainWindow)
        self.actionSeePlayersList.setObjectName("actionSeePlayersList")
        self.newGameButton.addAction(self.actionNewGame)
        self.newGameButton.addSeparator()
        self.newGameButton.addAction(self.actionSeePlayersList)
        self.newGameButton.addAction(self.actionSeeStatistics)
        self.menubar.addAction(self.newGameButton.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Small Chess"))
        self.newGameButton.setTitle(_translate("MainWindow", "Actions"))
        self.actionNewGame.setText(_translate("MainWindow", "New game"))
        self.actionPVSAI.setText(_translate("MainWindow", "Player VS AI"))
        self.actionSeeStatistics.setText(_translate("MainWindow", "See statistics"))
        self.actionSeePlayersList.setText(_translate("MainWindow", "See players list"))
