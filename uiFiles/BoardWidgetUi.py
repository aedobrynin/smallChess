# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/BoardWidgetUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_boardWidget(object):
    def setupUi(self, boardWidget):
        boardWidget.setObjectName("boardWidget")
        boardWidget.resize(360, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(boardWidget.sizePolicy().hasHeightForWidth())
        boardWidget.setSizePolicy(sizePolicy)
        boardWidget.setMinimumSize(QtCore.QSize(360, 360))
        boardWidget.setMaximumSize(QtCore.QSize(360, 360))
        self.gridLayoutWidget = QtWidgets.QWidget(boardWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -2, 371, 370))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.chessCellsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.chessCellsLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.chessCellsLayout.setContentsMargins(0, 0, 0, 0)
        self.chessCellsLayout.setSpacing(0)
        self.chessCellsLayout.setObjectName("chessCellsLayout")

        self.retranslateUi(boardWidget)
        QtCore.QMetaObject.connectSlotsByName(boardWidget)

    def retranslateUi(self, boardWidget):
        _translate = QtCore.QCoreApplication.translate
        boardWidget.setWindowTitle(_translate("boardWidget", "Form"))
