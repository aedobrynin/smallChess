# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/ChoosePlayersDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choosePlayersDialog(object):
    def setupUi(self, choosePlayersDialog):
        choosePlayersDialog.setObjectName("choosePlayersDialog")
        choosePlayersDialog.resize(430, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(choosePlayersDialog.sizePolicy().hasHeightForWidth())
        choosePlayersDialog.setSizePolicy(sizePolicy)
        choosePlayersDialog.setMinimumSize(QtCore.QSize(430, 100))
        choosePlayersDialog.setMaximumSize(QtCore.QSize(430, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        choosePlayersDialog.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(choosePlayersDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1, 10, 426, 89))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.firstPlayerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstPlayerLabel.setObjectName("firstPlayerLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstPlayerLabel)
        self.secondPlayerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.secondPlayerLabel.setObjectName("secondPlayerLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.secondPlayerLabel)
        self.firstPlayerBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.firstPlayerBox.setObjectName("firstPlayerBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstPlayerBox)
        self.secondPlayerBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.secondPlayerBox.setObjectName("secondPlayerBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.secondPlayerBox)
        self.startGameBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.startGameBtn.setObjectName("startGameBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.startGameBtn)

        self.retranslateUi(choosePlayersDialog)
        QtCore.QMetaObject.connectSlotsByName(choosePlayersDialog)

    def retranslateUi(self, choosePlayersDialog):
        _translate = QtCore.QCoreApplication.translate
        choosePlayersDialog.setWindowTitle(_translate("choosePlayersDialog", "Choose players"))
        self.firstPlayerLabel.setText(_translate("choosePlayersDialog", "Choose first player:"))
        self.secondPlayerLabel.setText(_translate("choosePlayersDialog", "Choose second player:"))
        self.startGameBtn.setText(_translate("choosePlayersDialog", "Start game"))
