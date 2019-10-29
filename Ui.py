# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 532, 482))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(50, 50))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chessCellsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chessCellsGridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.chessCellsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.chessCellsGridLayout.setSpacing(0)
        self.chessCellsGridLayout.setObjectName("chessCellsGridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew_game = QtWidgets.QMenu(self.menubar)
        self.menuNew_game.setObjectName("menuNew_game")
        MainWindow.setMenuBar(self.menubar)
        self.actionPlayer_VS_Player = QtWidgets.QAction(MainWindow)
        self.actionPlayer_VS_Player.setObjectName("actionPlayer_VS_Player")
        self.actionPlayer_VS_AI = QtWidgets.QAction(MainWindow)
        self.actionPlayer_VS_AI.setObjectName("actionPlayer_VS_AI")
        self.menuNew_game.addAction(self.actionPlayer_VS_Player)
        self.menuNew_game.addAction(self.actionPlayer_VS_AI)
        self.menubar.addAction(self.menuNew_game.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Small Chess"))
        self.menuNew_game.setTitle(_translate("MainWindow", "New game"))
        self.actionPlayer_VS_Player.setText(_translate("MainWindow", "Player VS Player"))
        self.actionPlayer_VS_AI.setText(_translate("MainWindow", "Player VS AI"))
