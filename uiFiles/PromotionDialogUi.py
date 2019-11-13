# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiFiles/PromotionDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_promotionDialog(object):
    def setupUi(self, promotionDialog):
        promotionDialog.setObjectName("promotionDialog")
        promotionDialog.resize(240, 90)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(promotionDialog.sizePolicy().hasHeightForWidth())
        promotionDialog.setSizePolicy(sizePolicy)
        promotionDialog.setMinimumSize(QtCore.QSize(240, 90))
        promotionDialog.setMaximumSize(QtCore.QSize(241, 91))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        promotionDialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtWidgets.QWidget(promotionDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 6, 240, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.promoteToKnight = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promoteToKnight.sizePolicy().hasHeightForWidth())
        self.promoteToKnight.setSizePolicy(sizePolicy)
        self.promoteToKnight.setMinimumSize(QtCore.QSize(55, 55))
        self.promoteToKnight.setMaximumSize(QtCore.QSize(55, 55))
        self.promoteToKnight.setText("")
        self.promoteToKnight.setIconSize(QtCore.QSize(45, 45))
        self.promoteToKnight.setObjectName("promoteToKnight")
        self.promotionButtons = QtWidgets.QButtonGroup(promotionDialog)
        self.promotionButtons.setObjectName("promotionButtons")
        self.promotionButtons.addButton(self.promoteToKnight)
        self.mainLayout.addWidget(self.promoteToKnight)
        self.promoteToBishop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promoteToBishop.sizePolicy().hasHeightForWidth())
        self.promoteToBishop.setSizePolicy(sizePolicy)
        self.promoteToBishop.setMinimumSize(QtCore.QSize(55, 55))
        self.promoteToBishop.setMaximumSize(QtCore.QSize(55, 55))
        self.promoteToBishop.setText("")
        self.promoteToBishop.setIconSize(QtCore.QSize(45, 45))
        self.promoteToBishop.setObjectName("promoteToBishop")
        self.promotionButtons.addButton(self.promoteToBishop)
        self.mainLayout.addWidget(self.promoteToBishop)
        self.promoteToRook = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promoteToRook.sizePolicy().hasHeightForWidth())
        self.promoteToRook.setSizePolicy(sizePolicy)
        self.promoteToRook.setMinimumSize(QtCore.QSize(55, 55))
        self.promoteToRook.setMaximumSize(QtCore.QSize(55, 55))
        self.promoteToRook.setText("")
        self.promoteToRook.setIconSize(QtCore.QSize(45, 45))
        self.promoteToRook.setObjectName("promoteToRook")
        self.promotionButtons.addButton(self.promoteToRook)
        self.mainLayout.addWidget(self.promoteToRook)
        self.promoteToQueen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promoteToQueen.sizePolicy().hasHeightForWidth())
        self.promoteToQueen.setSizePolicy(sizePolicy)
        self.promoteToQueen.setMinimumSize(QtCore.QSize(55, 55))
        self.promoteToQueen.setMaximumSize(QtCore.QSize(55, 55))
        self.promoteToQueen.setText("")
        self.promoteToQueen.setIconSize(QtCore.QSize(45, 45))
        self.promoteToQueen.setObjectName("promoteToQueen")
        self.promotionButtons.addButton(self.promoteToQueen)
        self.mainLayout.addWidget(self.promoteToQueen)

        self.retranslateUi(promotionDialog)
        QtCore.QMetaObject.connectSlotsByName(promotionDialog)

    def retranslateUi(self, promotionDialog):
        _translate = QtCore.QCoreApplication.translate
        promotionDialog.setWindowTitle(_translate("promotionDialog", "Pawn promotion"))
