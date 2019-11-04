# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/NewGameDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newGameDialog(object):
    def setupUi(self, newGameDialog):
        newGameDialog.setObjectName("newGameDialog")
        newGameDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        newGameDialog.resize(370, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newGameDialog.sizePolicy().hasHeightForWidth())
        newGameDialog.setSizePolicy(sizePolicy)
        newGameDialog.setMinimumSize(QtCore.QSize(370, 150))
        newGameDialog.setMaximumSize(QtCore.QSize(370, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        newGameDialog.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(newGameDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 1, 358, 153))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.secondsSBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.secondsSBox.setEnabled(False)
        self.secondsSBox.setObjectName("secondsSBox")
        self.mainLayout.addWidget(self.secondsSBox, 2, 3, 1, 1)
        self.minutesSBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.minutesSBox.setEnabled(False)
        self.minutesSBox.setObjectName("minutesSBox")
        self.mainLayout.addWidget(self.minutesSBox, 2, 1, 1, 1)
        self.firstPlayerLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.firstPlayerLabel.setObjectName("firstPlayerLabel")
        self.mainLayout.addWidget(self.firstPlayerLabel, 0, 0, 1, 1)
        self.secondPlayerLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondPlayerLabel.sizePolicy().hasHeightForWidth())
        self.secondPlayerLabel.setSizePolicy(sizePolicy)
        self.secondPlayerLabel.setObjectName("secondPlayerLabel")
        self.mainLayout.addWidget(self.secondPlayerLabel, 1, 0, 1, 1)
        self.minutes = QtWidgets.QLabel(self.gridLayoutWidget)
        self.minutes.setObjectName("minutes")
        self.mainLayout.addWidget(self.minutes, 2, 2, 1, 1)
        self.secondPlayerBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondPlayerBox.sizePolicy().hasHeightForWidth())
        self.secondPlayerBox.setSizePolicy(sizePolicy)
        self.secondPlayerBox.setObjectName("secondPlayerBox")
        self.mainLayout.addWidget(self.secondPlayerBox, 1, 1, 1, 5)
        self.startGameBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startGameBtn.setEnabled(False)
        self.startGameBtn.setObjectName("startGameBtn")
        self.mainLayout.addWidget(self.startGameBtn, 4, 0, 1, 6)
        self.firstPlayerBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.firstPlayerBox.setObjectName("firstPlayerBox")
        self.mainLayout.addWidget(self.firstPlayerBox, 0, 1, 1, 5)
        self.seconds = QtWidgets.QLabel(self.gridLayoutWidget)
        self.seconds.setObjectName("seconds")
        self.mainLayout.addWidget(self.seconds, 2, 4, 1, 2)
        self.timeLimitCBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.timeLimitCBox.setObjectName("timeLimitCBox")
        self.mainLayout.addWidget(self.timeLimitCBox, 2, 0, 1, 1)

        self.retranslateUi(newGameDialog)
        QtCore.QMetaObject.connectSlotsByName(newGameDialog)

    def retranslateUi(self, newGameDialog):
        _translate = QtCore.QCoreApplication.translate
        newGameDialog.setWindowTitle(_translate("newGameDialog", "New game"))
        self.firstPlayerLabel.setText(_translate("newGameDialog", "First player:"))
        self.secondPlayerLabel.setText(_translate("newGameDialog", "Second player:"))
        self.minutes.setText(_translate("newGameDialog", "minutes"))
        self.startGameBtn.setText(_translate("newGameDialog", "Start game"))
        self.seconds.setText(_translate("newGameDialog", "seconds"))
        self.timeLimitCBox.setText(_translate("newGameDialog", "With time limit"))
